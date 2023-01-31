''' JavaScript Object Notation '''
import json

with open('states.json') as f:
  data = json.load(f)

for state in data['states']:
  del state['area_codes']

# with open('new_states.json', 'w') as f:
print(json.dumps(data, indent=2))
