python3 run_experiment.py cifar10 local --n_learners 1 --n_rounds 100 --bz 128 --lr 0.01  --lr_scheduler multi_step --log_freq 5 --device cuda --optimizer sgd --seed 1244 --verbose 1  --save_path weights/cifar10/local/

python3 run_experiment.py cifar10 FedAvg --n_learners 1 --n_rounds 100 --bz 128 --lr 0.01  --lr_scheduler multi_step --log_freq 5 --device cuda --optimizer sgd --seed 1234 --verbose 1  --save_path weights/cifar10/FedAvg/

python3 run_experiment.py cifar10 FedEM --n_learners 3 --n_rounds 100 --bz 128 --lr 0.03  --lr_scheduler multi_step --log_freq 5 --device cuda --optimizer sgd --seed 1244 --verbose 1  --save_path weights/cifar10/FedEM/

python3 run_experiment_fig3.py
