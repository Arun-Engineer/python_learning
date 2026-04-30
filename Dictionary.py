# Create a dict for an AI model: name, parameters, context_window,, is_open_source
ai_model = {
    "name": "GPT-3",
    "parameters": 250,
    "context_window": 2048,
    "is_open_source": True
}
# Print each field using for loop
for key ,values in ai_model.items():
    print(f"{key}: {values}")
# Add a release year key and update it
ai_model["release_year"] = 2020
print(ai_model)
#use .get() to safely access that doesn't exist
print(ai_model.get("safety", "N/A"))
