from django.db import models

class AiInstruction(models.Model):
    slug = models.SlugField(max_length=150, unique=True, verbose_name='instruction name as slug')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='instruction description')
    instruction = models.TextField(verbose_name='instruction text')
    
    def __str__(self):
        return f"Instruction: {self.slug}"