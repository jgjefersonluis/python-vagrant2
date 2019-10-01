from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    descricao = models.TextField(u'Descrição')

class Tarefa(models.Model):
    PRIORIDADE_CHOICES=(
        ('B', 'Baixa'),
        ('M', 'Media'),
        ('A', 'Alta'),
    )
    nome = models.CharField(u'Nome', max_length=100)
    descricao = models.TextField(u'Descrição', blank=True)
    data_final = models.DateField(u'Data final')
    prioridade = models.CharField(u'Prioridade', max_length=1, choices=PRIORIDADE_CHOICES)
    categoria = models.ForeignKey(Categoria, verbose_name=('Categoria'), on_delete=models.CASCADE)