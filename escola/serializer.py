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

class MatriculaSerializer(serializers.ModelSerializer):                 #essa classe vai serializar os modelos Matricula do DB
    periodo = serializers.SerializerMethodField()                       #aqui estou configurando para ao inves de mostrar a sigla do periodo especifico, mostrar o nome do periodo inteiro. porem eh necessario um funcao para puxar essa informacao chamada get_periodo
    curso = serializers.ReadOnlyField(source='curso.descricao')         #aqui estou configurando para ao inves de mostrar o id do curso especifico, mostrar a descricao do curso
    aluno = serializers.ReadOnlyField(source='aluno.nome')              #aqui estou configurando para mostrar o nome do aluno ao invez do id do aluno

    class Meta:
        model = Matricula
        fields = ['periodo','aluno','curso']

    def get_periodo(self,obj):                                                      #essa funcao eh responsavel por puxar qual o periodo foi selecionado no objeto especifico. Tem que ter o mesmo nome da constante referente precedido de get_
        return obj.get_periodo_display()

class ListaMatriculasDoAlunoSerializer(serializers.ModelSerializer):                #essa classe eh responsavel por listar e serializar somente as matriculas de alunos selecionados
    curso = serializers.ReadOnlyField(source='curso.descricao')                     #aqui estou configurando para ao inves de mostrar o id do curso especifico, mostrar a descricao do curso
    periodo = serializers.SerializerMethodField()                                   #aqui estou configurando para mostrar a opcao do periodo selecionada, nao basta apenas fazer esse codigo preciso criar uma funcao em baixo para puxar qual a opcao foi selecionada 
    
    class Meta:
        model = Matricula                                                           #aqui escolhemos qual eh o modelo que queremos serializar
        fields = ['curso', 'periodo']                                               #aqui escolhemos quais propriedades queremos disponibilizar
    
    def get_periodo(self,obj):                                                      #essa funcao eh responsavel por puxar qual o periodo foi selecionado no objeto especifico. Tem que ter o mesmo nome da constante referente precedido de get_
        return obj.get_periodo_display()
    
class AlunosMatriculadosNoCursoSerializer(serializers.ModelSerializer):
    nome_do_aluno = serializers.ReadOnlyField(source='aluno.nome')                  #aqui estou configurando para mostrar o nome do aluno ao invez do id do aluno

    class Meta:
        model = Matricula
        fields = ['nome_do_aluno']