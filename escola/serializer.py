#Nesse arquivo sao criados os serializers que sao os tratudores entre django e Json 
#Esses 'dicionarios' sao importantes pois  geralmente as API's sao em JSON e o backend e escrito  em python


from rest_framework import serializers                                  #importando  o serializer do rest_framework
from  .models import Aluno, Curso, Matricula                            #importando os modelos do DB criandos em python

class AlunoSerializer(serializers.ModelSerializer):                     #Essa classe vai serializar os modelos do DB, ou seja transformar eles em JSON
    class  Meta:
        model = Aluno                                                   #aqui escolhemos qual eh o modelo que queremos serializar
        fields = ['id','nome','rg','cpf','data_nascimento']             #aqui escolhemos quais propriedades queremos disponibilizar

class CursoSerializer(serializers.ModelSerializer):                     
    class  Meta:
        model = Curso                                                   #escolhemos  qual eh o modelo que queremos serializar
        fields = '__all__'                                              #essa forma pega todas as propriedades do modelo do DB

class MatriculaSerializer(serializers.ModelSerializer):                 #essa classe vai serializar os modelos Matricula do  DB
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasDoAlunoSerializer(serializers.ModelSerializer):    #essa classe eh responsavel por listar e serializar somente as matriculas de alunos selecionados
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']