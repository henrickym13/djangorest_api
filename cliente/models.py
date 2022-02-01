from django.db import models

# Create your models here.
class Cliente(models.Model):

    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=14)
    data_de_nascimento = models.DateField()
    genero = models.CharField(max_length=17)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.IntegerField()
