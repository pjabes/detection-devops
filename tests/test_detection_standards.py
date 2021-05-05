""" 
    Standards are defined as 'MUST HAVES' for each detection.
"""

import pytest 
import os
import yaml

detection = yaml.safe_load(open("detections/DetectDNSRequestsToPhishingSites.yaml", "r"))

def test_detection_has_index():
    assert "index=" in detection['search']

def test_detection_has_sourcetype():
    assert "sourcetype=" in detection['search']

def test_detection_has_earliest():
    assert "earliest=" in detection['search']

def test_detection_has_latest():
    assert "latest=" in detection['search']

def test_detection_has_index_earliest():
    assert "index_earliest=" in detection['search']

def test_detection_has_index_latest():
    assert "index_latest=" in detection['search']
