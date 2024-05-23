import vitaldb
import pandas as pd
import yaml
import numpy as np

#config function
def get_config():
    with open('vitaldb.yaml','r') as stream:
        config = yaml.safe_load(stream)
    return config
