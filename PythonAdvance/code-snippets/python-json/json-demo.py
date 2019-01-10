''' JavaScript Object Notation '''
import json

# loads(f) load from string
# load(f) load as object
with open('states.json', 'r') as f:
  data = json.load(f)

# uses following decoding
# object(json)          -> dict (python) 
# array(json)           -> list (python)
# string(json)          -> str (python)
# number(int)(json)     -> int (python)
# number(real)(json)    -> float (python)
# true, false(json)     -> True, False (python)
# null(json)            -> None (python)

print(type(data))                 # dict
print(type(data['states']))       # list

for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    # to store data as json format using some indentation and sorting it
    json.dump(data, f, indent=2, sort_keys=True)   