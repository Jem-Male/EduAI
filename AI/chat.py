from django.conf import settings
from .client import openai_client
from.models import AiInstruction

class AI:
    @classmethod
    def get_chat_response(cls, prompt: str, system_instruction: str | None = None) -> str:
        msg = []
        if system_instruction:
            msg.append({"role": "system", "content": system_instruction})
        msg.append({"role": "user", "content": prompt})

        response = openai_client.chat.completions.create(
            model=settings.AI_MODEL,
            messages=msg,
        )
        return response.choices[0].message.content or ""


    @classmethod
    def chat_with_instruction(cls, prompt: str, instruction_slug: str) -> str:
        instruction = AiInstruction.objects.get(slug=instruction_slug)
        return cls.get_chat_response(prompt, instruction.instruction)