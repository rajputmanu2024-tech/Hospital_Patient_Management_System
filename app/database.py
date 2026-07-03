import json

file='data/patients.json'
def load_data():
    with open(file, 'r') as f:

        data =json.load(f)
    return data

def save_data(data):
    with open(file, 'w') as f:
        json.dump(data, f)