import os
import json
import requests

# for pushover
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

def push(message):
    print(f"Push: {message}")
    payload = {"user" : pushover_user, "token" : pushover_token, "message" : message}
    response = requests.post(pushover_url, data = payload)
    return "OK" if response.status_code == 200 else "Failed"

def record_user_details(email, name="Name not provided.", notes="not provided."):
    print(f"Record user_details : {email}, {name}, {notes}")
    file_path = "record_user_details.txt"

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            new_line = sum(1 for line in f if "Details of User" in line) + 1
    else:
        new_line = 1

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"Details of User {new_line} :\n e-mail -> {email}\n name -> {name}\n notes -> {notes}\n\n")
    return "OK"

def record_unknown_question(question):
    print(f"Record question that I couldn't answer : {question}")
    file_path = "record_unknown_questions.txt"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            new_line = sum(1 for line in f) + 1
    else:
        new_line = 1

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"Number {new_line} : {question}\n")
    return "OK"

def record_fav_tool(fav):
    print(f"Tool to record user's favourite food : {fav}")
    file_path = "fav_foods.txt"
    
    with open(file_path, 'a', encoding="utf-8") as f:
        f.write(fav + '\n')
    return "Successfully added new entry to favourite food!"

record_user_details_json = {
    "name": "record_user_details",
    "description": "Records a user's details including their email address, name, and any additional notes.",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The user's email address."
            },
            "name": {
                "type": "string",
                "description": "The user's name. Defaults to 'Name not provided.' if omitted."
            },
            "notes": {
                "type": "string",
                "description": "Any additional notes or comments from the user. Defaults to 'not provided.' if omitted."
            }
        },
        "required": ["email"],
        "additionalProperties": False
    }
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Records or logs a question that could not be answered by the assistant.",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The specific question that the assistant was unable to answer."
            }
        },
        "required": ["question"],
        "additionalProperties": False
    }
}

record_fav_tool_json = {
    "name": "record_fav_tool",
    "description": "Records the user's favourite food.",
    "parameters": {
        "type": "object",
        "properties": {
            "fav": {
                "type": "string",
                "description": "The user's favourite food."
            }
        },
        "required": ["fav"],
        "additionalProperties": False
    }
}

tools = [
    {"type": "function", "function": record_user_details_json},
    {"type": "function", "function": record_unknown_question_json},
    {"type": "function", "function": record_fav_tool_json}
]

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
    "record_fav_tool": record_fav_tool 
}

def handle_tool_calls_with_manual_if(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)
        
        tool = tool_map.get(tool_name)
        result = tool(**arguments) if tool else "No tool found."
        results.append({"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id})
    return results