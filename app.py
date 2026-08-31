from dotenv import load_dotenv
import os
from openai import OpenAI
import gradio as gr

from context import TWIN_SYSTEM_PROMPT
import styles
# FIX: Import tools array and the execution function from tools.py
from tools import tools, handle_tool_calls_with_manual_if

load_dotenv(override=True)

client = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}] 
MODEL_NAME = 'gpt-4o-mini'

def chat(message, history):
    messages = system + history + [{'role': 'user', 'content': message}]
    
    # FIX: Included tools=tools in the INITIAL request
    response = client.chat.completions.create(
        messages=messages, 
        model=MODEL_NAME, 
        tools=tools
    )

    while response.choices[0].finish_reason == "tool_calls":
        response_msg = response.choices[0].message
        tool_calls = response_msg.tool_calls

        results = handle_tool_calls_with_manual_if(tool_calls)
        messages.append(response_msg)
        messages.extend(results)

        response = client.chat.completions.create(
            model=MODEL_NAME, 
            messages=messages, 
            tools=tools
        )
        
    return response.choices[0].message.content


# FIX: Removed theme/css from Blocks constructor to fix Gradio 6 warning
with gr.Blocks(theme=styles.custom_theme, css=styles.CUSTOM_CSS) as demo:
    gr.ChatInterface(
        fn=chat,
        examples=styles.EXAMPLE_QUESTIONS,
        title="Samali's Digital Twin",
        description="Ask me about my career, skills, or experience.",
        chatbot=gr.Chatbot(show_label=False),
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)