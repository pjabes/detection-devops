from jinja2 import Template
import yaml

template = """

## {{detection.friendly_name}}

**Description**: {{ detection.description }}  
**Detection Type**: {{ detection.type }}

---

### Detection Concepts
**Intention**: {{ detection.intention }}  
**Known FPs**:  
{% for known_fp in detection.known_falsepositives %}
    * {{ known_fp }}
{% endfor %}  
**Blindspots**: 
{% for blindspot in detection.blindspots %}
    * {{ blindspot }}
{% endfor %}
**Detection Dependencies**:  
Logging Policies (LPs):  
{% for LP in detection.dependencies.LPs %}
    * {{ LP }}
{% endfor %}
Hardening Policies (HPs):  
{% for HP in detection.dependencies.HPs %}
    * {{ HP }}
{% endfor %}

---
## Response 


"""

with open("../detections/DetectDNSRequestsToPhishingSites.yaml") as file:
    detectionFile = yaml.load(file, Loader=yaml.FullLoader)

print(detectionFile)
j2_template = Template(template)

output = j2_template.render(detectionFile)
print(output)
with open('../docs/DetectDNSRequestsToPhishingSites.md', 'w') as file:
    file.write(output)