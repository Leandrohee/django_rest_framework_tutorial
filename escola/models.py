# Nesse arquivo é onde se configura os modelos para o banco de dados
# O caminho da criacao do model ate a sua disponibilizacao em uma URL eh a seguinte: models --> serializer --> views --> urls
# O caminho da criacao do model ate a sua disponibilizacao no campo ADMIN eh a seguiinte: models --> admin

from django.db import models                                                                            #Vem padronizado

class Aluno(models.Model):                                                                              #Criado uma classe Aluno que funcionará como uma table de um database
    nome = models.CharField(max_length=30)                                                              #Criando um cabeçalho "nome" na table Aluno 
    rg = models.CharField(max_length=9)                                                                 #Criando um cabeçalho "rg" na table Aluno
    cpf = models.CharField(max_length=11)                                                               #Criando um cabeçalho "cpf" na table Aluno
    data_nascimento = models.DateField()                                                                #Criando um cabeçalho "data de nascimento" na table Aluno

    def __str__(self):                                                                                  #Essa funcao representa algum objeto da classe aluno como o nome don aluno
        return self.nome


class Curso(models.Model):                                                                              #Criado uma classe Curso que funcionará como uma table de um database

    NIVEL_CURSO = (                                                                                     #tupla contendo 3 escolhas diferntes para o nivel
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A','Avancado'),
    )

    codigo_curso = models.CharField(max_length=30)                                                      #Criando um cabeçalho "codigo  do curso" na table Curso 
    descricao = models.CharField(max_length=100)                                                        #Criando um cabeçalho "descricao" na table Curso 
    nivel = models.CharField(max_length=1,choices=NIVEL_CURSO, blank=False, null=False, default='B')    #Criando um cabeçalho "nivel" na table Curso 

    def __str__(self):                                                                                  #Essa funcao representa algum objeto da classe Curso com a descricao do curso
        return self.descricao
    
class Matricula(models.Model):                                                                          #Criano um modelo matricula que sera VINCULADO com outros dois modelos do DB, o ALuno e o Curso

    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)                                          #a variavel|cabecalho aluno do modelo Matricula eh referente a um objeto do modelo Aluno do DB
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)                                          #a variavel|cabecalho curso do modelo Matricula eh referente a um objeto do modelo Curso do DB
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, default='M')                 #essa variaval|cabecalho periodo eh uma variavel nova do tipo escolhas

    def __str__(self):
        return (f'{self.aluno} em {self.curso}')