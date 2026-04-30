# API response
api_response = {
    "model" : "gpt-3.5-turbo",
    "choices" : [
        {
            "message": {
                "role": "assistant",
                "content": "Hello! How can I assist you today?"
            },
            "finish_reason": "stop",
            "index": 0
        }                                                                                           
    ],
    "usage": {
        "prompt_tokens": 10,
        "completion_tokens": 20,
        "total_tokens": 30
    }   
}

#Extract the finish reason value
reason = api_response["choices"][0]["finish_reason"]
print(f"Finish reason: {reason}")

#Extract the prompt tokens value
token = api_response["usage"]["prompt_tokens"]
print(f"Prompt tokens: {token}")    

#Print Model name used total_tokens and said content
print(f"Model: {api_response['model']} used {api_response['usage']['total_tokens']} tokens and said: {api_response['choices'][0]['message']['content']}")