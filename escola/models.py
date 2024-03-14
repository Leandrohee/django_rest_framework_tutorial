# Nesse arquivo é onde se configura os modelos para o banco de dados

from django.db import models                                    #Vem padronizado

class Aluno(models.Model):                                      #Criado uma classe Aluno que funcionará como uma table de um database
    nome = models.CharField(max_length=30)                      #Cabeçalho nome do db
    rg = models.CharField(max_length=9)                         #Cabeçalho cpf do db
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):                                          #Essa funcao representa algum objeto da classe aluno como o nome don aluno
        return self.nome


class Curso(models.Model):                                      #Criado uma classe Curso que funcionará como uma table de um database

    NIVEL_CURSO = (                                             #tupla contendo 3 escolhas diferntes para o nivel
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A','Avancado'),
    )

    codigo_curso = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1,choices=NIVEL_CURSO, blank=False, null=False, default='B')

    def __str__(self):                                       #Essa funcao representa algum objeto da classe Curso com a descricao do curso
        return self.descricao