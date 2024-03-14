#Eh nesse arquivo que sao enviadas as informacoes para renderizacao seja em html, texto simples, json ou qualquer outra funcao

from rest_framework import viewsets, views, response                                #importando  o viewset que fara a disponibilizacao dos objetos do banco de dados no  formato JSON
from .models import Aluno, Curso,  Matricula                                        #importando os modelos do DB 
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer       #importando  os serializador
from .serializer import ListaMatriculasDoAlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()                                                  #pega todos os objetos do model Aluno
    serializer_class = AlunoSerializer                                              #pega o serializador de Aluno

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()                                                  #pega todos os objetos do model Curso
    serializer_class = CursoSerializer                                              #pega o serializador de Curso

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriclas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    


"""ESSE EH UM OUTRO METODO PARA MOSTRAR O SERIALIZER DE TODOS OS ALUNOS USANDO O APIVIEWS AO INVES DO VIEWSETS"""
class AlunoListView(views.APIView):
    def get (self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return response.Response(serializer.data)
    