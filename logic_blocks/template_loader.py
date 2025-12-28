import json
import os

def load_template(filename):
    path = os.path.join("templates", filename)
    with open(path, "r") as f:
        return json.load(f)
