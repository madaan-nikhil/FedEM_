import torch
import argparse

def dist(state_dict1, state_dict2):
    assert state_dict1.keys() == state_dict2.keys(), "Model parameters different"
    l2_dists = []
    for param in state_dict1:
        if param.find('bias') > 0 or param.find('weight') > 0:
            l2_dists.append(torch.dist(state_dict1[param], state_dict2[param], p=2))
    l2_dists = torch.stack(l2_dists)
    return l2_dists.mean().item()

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        'state_1',
        type=str
    )
    
    parser.add_argument(
        'state_2',
        type=str
    )
    
    args = parser.parse_args()
    state_1 = torch.load(args.state_1)
    state_2 = torch.load(args.state_2)
    print(dist(state_1, state_2))
    
if __name__ == "__main__":
    main()