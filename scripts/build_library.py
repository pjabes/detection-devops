from jinja2 import Template
import yaml

template = """

## Detection
Name: {{ friendly_name }}
Description: {{ description }}
Detection Type: {{ type }}
Author: {{ author }}
Created: {{ created }}
Last Updated: {{ last_updated }}
---

## Dependencies

"""
with open("../detections/DetectDNSRequestsToPhishingSites.yaml") as file:
    detectionFile = yaml.load(file, Loader=yaml.FullLoader)

j2_template = Template(template)

output = j2_template.render(detectionFile)
print(output)
with open('../docs/DetectDNSRequestsToPhishingSites.md', 'w') as file:
    file.write(output)