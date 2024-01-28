from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField

    def __str__(self):
        return self.text

class Choices(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:50]} - {self.choice_text}"