# Nesse arquivo é onde configuramos os dados que seráo gerenciados e exibidos na página de administrador

from django.contrib import admin
from .models import Aluno, Curso, Matricula                              #importei as tables|classes criadas nos models


class Alunos(admin.ModelAdmin):                                         #criei uma classe que fará a visualização|alteração dos objetos da classe|tabble Aluno na página adm
    list_display = ('id','nome','rg','cpf','data_nascimento')           #os itens que iram aparecer na pagina do adm
    list_display_links = ('id','nome')                                  #os itens que serao clicaveis
    search_fields = ('nome',)                                           #os itens que poderao ser pesquisáveis
    list_per_page = 20

admin.site.register(Aluno,Alunos)                                       #sobe a classe Alunos para o adm

class Cursos(admin.ModelAdmin):                                         #criei uma classe que fará a visualização|alteração dos objetos da classe|tabble Curso na página adm
    list_display = ('id','codigo_curso','descricao','nivel')
    list_display_links = ('id','descricao',)
    search_fields = ('codigo',)

admin.site.register(Curso,Cursos)                                       #sobe a classe Cursos para o adm

class Matriculas(admin.ModelAdmin):
    list_display = ('id','aluno','curso','periodo')
    list_display_links = ('id',)
    search_fields = ('aluno',)

admin.site.register(Matricula,Matriculas)