"""
    Metadata is defined as the required data to describe a detection.
"""

import pytest 
import os
import yaml

detection_config = yaml.safe_load(open("detections/DetectDNSRequestsToPhishingSites.yaml", "r"))

def test_detection_config_has_friendly_name():
    assert detection_config['detection']['friendly_name']

def test_detection_config_has_intent():
    assert detection_config['detection']['description']

def test_detection_config_has_state():
    assert detection_config['state']

def test_detection_config_has_type():
    assert detection_config['detection']['type']