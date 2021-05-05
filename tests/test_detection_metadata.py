"""
    Metadata is defined as the required data to describe a detection.
"""

import pytest 
import os
import yaml

detection = yaml.safe_load(open("detections/DetectDNSRequestsToPhishingSites.yaml", "r"))

def test_detection_has_friendly_name():
    assert detection['friendly_name']

def test_detection_has_intent():
    assert detection['description']

def test_detection_has_enabled_state():
    assert detection['enabled']

def test_detection_has_type():
    assert detection['type']