from django.db import models

class Filme(models.Model):
    id = models.AutoField(primary_key=True) 
    titulo = models.CharField(max_length=200, help_text="Título")
    ano = models.IntegerField(help_text="Ano de lançamento")
    genero = models.CharField(max_length=100, help_text="Gênero")

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ['titulo'] 

    def __str__(self):
        return f"{self.titulo} ({self.ano})"