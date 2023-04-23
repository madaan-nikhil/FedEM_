"""Run Experiment pFedDef

This script runs a pFedDef training on the FedEM model.
"""
from utils.utils import *
from utils.constants import *
from utils.args import *
from run_experiment import * 

from torch.utils.tensorboard import SummaryWriter

# Import General Libraries
import os
import argparse
import torch
import copy
import pickle
import random
import numpy as np
import pandas as pd
from models import *

# Import Transfer Attack
from transfer_attacks.Personalized_NN import *
from transfer_attacks.Params import *
from transfer_attacks.Transferer import *
from transfer_attacks.Args import *
from transfer_attacks.TA_utils import *

import time
from datetime import datetime
import pytz


if __name__ == "__main__":
    newYorkTz = pytz.timezone("America/New_York") 
    timeInNewYork = datetime.now(newYorkTz)
    currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")

    print("The current time in New York is:", currentTimeInNewYork)
    
    ## INPUT GROUP 1 - experiment macro parameters ##
    lr_set = [0.05, 0.08, 0.10]
    exp_names = [f'rep_lr_00{int(i*100)}' for i in lr_set]
    G_val = [0.4]*len(exp_names)
    n_learners = 1
    ## END INPUT GROUP 1 ##
    
    for itt in range(len(exp_names)):
        
        print("\n\nrunning trial:", itt)
        
        ## INPUT GROUP 2 - experiment macro parameters ##
        args_ = Args()
        args_.experiment = "cifar10"      # dataset name
        args_.method = 'FedAvg'       # Method of training
        args_.decentralized = False
        args_.sampling_rate = 1.0
        args_.input_dimension = None
        args_.output_dimension = None
        args_.n_learners= n_learners      # Number of hypotheses assumed in system
        args_.n_rounds = 100              # Number of rounds training takes place
        args_.bz = 128
        args_.local_steps = 1
        args_.lr_lambda = 0
        args_.lr = 0.03                   # Learning rate
        args_.lr_scheduler = 'multi_step'
        args_.log_freq = 10
        args_.device = 'cuda'
        args_.optimizer = 'sgd'
        args_.mu = 0
        args_.communication_probability = 0.1
        args_.q = 1
        args_.locally_tune_clients = False
        args_.seed = 1234
        args_.verbose = 1
        args_.logs_root = f'logs'
        args_.aggregation_op = 'median'
        args_.save_path = f'weights/{args_.experiment}/{args_.method}_replacement/{args_.aggregation_op}/{exp_names[itt]}'      # weight save path
        # args_.load_path = f'/home/ubuntu/Documents/jiarui/experiments/{args_.method}/{args_.experiment}/replace/replace_fail_1/weights'
        args_.validation = False
        args_.tune_steps = 0

        # Q = 10                            # ADV dataset update freq
        # G = G_val[itt]                    # Adversarial proportion aimed globally
        # S = 0.05                          # Threshold param for robustness propagation
        # step_size = 0.01                  # Attack step size
        # K = 10                            # Number of steps when generating adv examples
        # eps = 0.1                         # Projection magnitude 
        num_clients = 40                  # Number of clients to train with

        num_classes = 10                  # Number of classes in the data set we are training with
        atk_count = 1
        ## END INPUT GROUP 2 ##
        

        # Randomized Parameters
        Ru = np.ones(num_clients)
        
        # Generate the dummy values here
        aggregator, clients = dummy_aggregator(args_, num_clients)

        if "load_path" in args_:
            print(f"Loading model from {args_.load_path}")
            load_root = os.path.join(args_.load_path)
            aggregator.load_state(load_root)

            args_.n_rounds = 1
            print("Update clients before training")
            aggregator.update_clients()     # update the client's parameters immediatebly, since they should have an up-to-date consistent global model before training starts

        # Perform label swapping attack for a set number of clients
        atk_round = 1
        for i in range(atk_count):
            aggregator.clients[i].turn_malicious(
                factor = num_clients / lr_set[itt],  
                attack = "replacement",
                atk_round = args_.n_rounds - atk_round, # attack rounds in the end
                replace_model_path = "weights/cifar10/backdoor/all_label_switch_atk/chkpts_0.pt"
            )

        # Train the model
        print("Training..")
        pbar = tqdm(total=args_.n_rounds)
        current_round = 0
        while current_round <= args_.n_rounds:
            print(f"Global round {current_round}")

            
            if current_round == args_.n_rounds - atk_round:
                save_root = os.path.join(args_.save_path, "before_rep")
                os.makedirs(save_root, exist_ok=True)
                aggregator.save_state(save_root)

            if current_round >= args_.n_rounds - atk_round:
                print(f"Global Round {current_round} - Start Replacement!")
                aggregator.mix(replace = True)
            else:
                aggregator.mix()
            

            if aggregator.c_round != current_round:
                pbar.update(1)
                current_round = aggregator.c_round

        if "save_path" in args_:
            save_root = os.path.join(args_.save_path)

            os.makedirs(save_root, exist_ok=True)
            aggregator.save_state(save_root)
            
        del args_, aggregator, clients
        torch.cuda.empty_cache()
            