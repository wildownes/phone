import openai
import os
from dotenv import load_dotenv

class Troubleshooter:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_troubleshooting_suggestion(self, conversation):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Ruby, a witty, charming conversationalist. Answer concisely. Answer in sentences. Break long responses into smaller parts and confirm the user would like to continue."}
            ] + conversation
        )
        return response['choices'][0]['message']['content']
    
    def raw_api_call(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Answer as concisely as possible."},
                {"role": "user", "content": text}
            ]
        )
        return response
