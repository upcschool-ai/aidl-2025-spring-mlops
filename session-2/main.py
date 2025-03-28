import torch

from dataset import MyDataset
from model import MyModel
from utils import accuracy

device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")


def train_single_epoch():
    # TODO: Implement training loop
    raise NotImplementedError


def eval_single_epoch():
    # TODO: Implement evaluation loop
    raise NotImplementedError


def train_model(config):
    
    my_dataset = MyDataset(...)
    my_model = MyModel(...).to(device)

    for epoch in range(config["epochs"]):
        train_single_epoch(...)
        eval_single_epoch(...)

    return my_model


if __name__ == "__main__":

    config = {
        "hyperparam_1": 1,
        "hyperparam_2": 2,
    }
    train_model(config)