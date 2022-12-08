# -*- coding: utf8 -*-
from get_yaml_all_data import get_yaml

path = "\\coffee_ros_desired_caps.yaml"


def get_platform_name():
    return get_yaml(file=path)['platformName']


def get_url():
    return get_yaml(file=path)['url']


def get_platform_version():
    return get_yaml(file=path)['platformVersion']


def get_app_package():
    return get_yaml(file=path)['appPackage']


def get_app_activity():
    return get_yaml(file=path)['appActivity']


def get_devices_name():
    return get_yaml(file=path)['devicesName']
