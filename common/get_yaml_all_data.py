# -*- coding: utf8 -*-
import os
import yaml


def get_yaml(file):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + file
    f = open(path, "r")
    data = f.read()
    dict_ = yaml.safe_load(data)
    return dict_

