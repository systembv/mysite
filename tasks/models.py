from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Task(models.Model):

    STATUS = (
        ("Em andamento", "Em andamento"),
        ("Concluído", "Concluído"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=15, choices=STATUS,)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
