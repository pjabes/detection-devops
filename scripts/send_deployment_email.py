"""
Constructs an email to notify the stakeholders of deployment status
"""

from jinja2 import Template
import yaml

template = """

Hi Team,

This is a courtesy email to inform you that the following detections have been enabled:

{% for detection in detections %}
    * {{ detection.friendly_name }}
{% endfor %}

"""

# TODO:  Actually emailing this thing.  