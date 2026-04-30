models = [
    {"name": "GPT-4", "params_b": 1760, "open": False, "score": 92},
    {"name": "Llama-3", "params_b": 175, "open": True, "score": 85},
    {"name": "Gemini-1.5 Pro", "params_b": None, "open": False, "score": 90},
    {"name": "Mistral", "params_b": 7, "open": True, "score": 78},
    {"name": "Falcon-180B", "params_b": 7, "open": True, "score": 74},
]

#1. Get names of all open-source models[ list comprehension ]
names = [i["name"] for i in models if i["open"] == True]
print(names)

#2. Find the model with the highest score (hint: max())
Model_highest_score = [i['name'] for i in models if i['score'] == max(j['score'] for j in models)]
print(Model_highest_score)

#3. Calculate the average score of all models (hint: sum() and len())
average_score = sum([i['score'] for i in models])/ len(models)
print(average_score)

#4. Create a dict: model_name  --> "open-source" or "closed-source"
modl = {"name": "Claude", "params_b": 1000, "open": False, "score": 92.5}
models.append(modl)
print(models)

#5. Print a summary like:
# "5 models analyzed. Best model: GPT-4 with a score of 92.
# Open source models: Llama-3, Mistral, Falcon-180B."

print("=" * 50)
print(f"Total Models Analyzed: { len(models)}. Best Model: {''.join(i['name'] for i in models if i['score'] == max(j['score'] for j in models))}")
print(f" Open Source Models: {', '.join(i['name'] for i in models if i['open']== True)}")
print("=" * 50)
