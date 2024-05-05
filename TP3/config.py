import json
from TP3.src.optimization import *

with open('/Users/motegui/Documents/GitHub/SIA-TP-S/TP3/config.json', 'r') as file:
    config = json.load(file)

optimizers = {
    "gradient_descend": gradient_descend
}
