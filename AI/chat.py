from django.conf import settings
from .client import openai_client


def get_chat_response(prompt: str, system_instruction: str) -> str:
    try:
        response = openai_client.chat.completions.create(
            model=settings.AI_MODEL,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content or ""
        
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"OpenAI Error: {e}")
        return f"Ошибка при запросе к OpenAI API: {e}"