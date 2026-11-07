from django.conf import settings
from openai import OpenAI

openai_client = OpenAI(
    base_url=settings.AI_URL, 
    api_key=settings.AI_API_KEY
)