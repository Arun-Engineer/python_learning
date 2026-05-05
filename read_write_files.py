# "w" --> write mode (creates or overwrites)
# with open("notes.txt", "w")as f:
#     f.write("Line 1: Learning Python\n")
#     f.write("Line 2: For AI Engineering\n")
#     f.write("Line 3: Files are easy\n")

# "r" ---> read mode (reading a file)
# with open("notes.txt", "r")as f:
#     file = f.read()
# print(file)

# with open("notes.txt", "r")as f:
#     content = f.readlines()
# for i in content:
#     print(i)

# "a" ---> append mode (adds to the end, doesnt overwrite)
# with open("notes.txt", "a")as f:
#     f.write("Line 4: Appended this later\n")

# with open("notes.txt", "r")as f:
#     content = f.read()
# print(content)

# with open("grocery.txt", "w")as file:
#     file.write("Line 1: Milk\n")
#     file.write("Line 2: Egg\n")
#     file.write("Line 3: Biscuits\n")
#     file.write("Line 4: Sweets\n")

# with open("grocery.txt", "r")as file:
#     content = file.readlines()
# for i in content:
#     print(i.strip())

# with open("grocery.txt", "a")as f:
#     f.write("Line 5: Oil\n")

# with open("grocery.txt", "r")as f:
#     content = f.readlines()
# for i in content:
#     print(i.strip())

# JSON  - the language of AI APIs

{
    "name": "GPT-4",
    "score": 92,
    "features": ["text", "image", "code"],
    "pricing": {
        "input": 0.03,
        "output": 0.06
    }
}

import json

models = [
    {"name": "GPT-4", "score": 92, "price": 0.03},
    {"name": "Llama-3", "score": 82, "price": 0.00},
]

#save to file
with open("models.json", "w")as f:
    json.dump(models, f, indent =2)

# Load the JSON file
import json

# Load from file
with open("models.json", "r")as f:
    loaded_models = json.load(f)

print(loaded_models[0]["name"])
print(type(loaded_models))

# Convert between JSON string and python dict

import json

data = {"name": "claude", "score": 90}
# Dict ---> JSON string (for sending to APIs)
json_string = json.dunps(data)
print(json_string)
print(type(json_string))

#JSON string ---> Dict(for reading API responses)
json.loads()