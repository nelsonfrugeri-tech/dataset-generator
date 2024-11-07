import os
from openai import OpenAI


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_text(
        self, messages, model="gpt-4o", temperature=0, response_format=None
    ):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            response_format=response_format,
        )
        return response.choices[0].message.content
