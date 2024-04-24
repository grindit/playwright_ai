import json

# Load your JSON file
with open('reference_data4.jsonl', 'r') as file:
    data = json.load(file)

# Assuming 'data' is a list of dictionaries
with open('output.jsonl', 'w') as outfile:
    for entry in data:
        json.dump(entry, outfile)
        outfile.write('\n')