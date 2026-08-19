from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    idade = models.PositiveIntegerField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.nome

# Create your models here.
