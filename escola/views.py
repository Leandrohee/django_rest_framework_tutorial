#Eh nesse arquivo que sao enviadas as informacoes para renderizacao seja em html, texto simples, json ou qualquer outra funcao

from rest_framework import viewsets                                                                 #importando  o viewset que fara a disponibilizacao dos objetos do banco de dados no  formato JSON
from rest_framework import views, response, generics                                                #o views e reponse são necessarios no APIView o generics é necessario no listAPiView      
from rest_framework import authentication, permissions                                              #essas importações sao referentes a seguranca da Api, ela garante uma autenticacao e uma permissividade, garantindo que só consiga acesasr e alterar nossa API quem estiver logado no server
from .models import Aluno, Curso,  Matricula                                                        #importando os modelos do DB 
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer                       #importando  os serializador
from .serializer import ListaMatriculasDoAlunoSerializer, AlunosMatriculadosNoCursoSerializer       #importando os serializers responsáveis por fazer filtragens específicas

class ClasseBaseFeitaPeloLeandro(viewsets.ModelViewSet):                            #ESSA CLASSE EU QUE CRIEI COM INTUITO DE EVITAR CODIGO GRANDE E REPETIDO E ELA SERVIRA PARA HERDAR O "viewsets.ModelViewSet" E ACRESCENTAR A SEGURANCA QUE FICA EM TDS AS OUTRAS CLASSES
    authentication_classes =  [authentication.BasicAuthentication]                  #autenticacao basica para a API
    permission_classes = [permissions.IsAuthenticated]                              #somente acessa essa classe quem esta autenticado|logado

class AlunoViewSet(ClasseBaseFeitaPeloLeandro):                                     #essa classe esta herdando as caracteristicas da minha classe oq simplifica o codigo. Eh so comparar essa classe com as demais que nao heram a minha classe
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()                                                  #pega todos os objetos do model Aluno
    serializer_class = AlunoSerializer                                              #pega o serializador de Aluno

class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()                                                  #pega todos os objetos do model Curso
    serializer_class = CursoSerializer                                              #pega o serializador de Curso
    authentication_classes =  [authentication.BasicAuthentication]                  #autenticacao basica para a API
    permission_classes = [permissions.IsAuthenticated]                              #somente acessa essa classe quem esta autenticado|logado

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriclas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes =  [authentication.BasicAuthentication]                  #autenticacao basica para a API
    permission_classes = [permissions.IsAuthenticated]                              #somente acessa essa classe quem esta autenticado|logado

class ListaMatriculasPorAluno(generics.ListAPIView):                                #essa classe eh responsavel por filtrar os dados de matricula para somente um id|Aluno especifico  
    """Listando a(s) matriculas de um aluno especifico"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])             #pega um id especifica na url por exempli: 8000/escola/alunos/3/ --> pega o numero 3
        return queryset
    serializer_class = ListaMatriculasDoAlunoSerializer
    authentication_classes =  [authentication.BasicAuthentication]                  #autenticacao basica para a API
    permission_classes = [permissions.IsAuthenticated]                              #somente acessa essa classe quem esta autenticado|logado

class ListaAlunosMatriculadosPorCurso(generics.ListAPIView):                        #essa classe eh responsavel por filtrar os dados de alunos matriculados em um curso
    """Listando o(s) alunos matriculados em um curso específico"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])             #pega um id especifica na url por exempli: 8000/escola/cursos/4/ --> pega o numero 4
        return queryset
    serializer_class = AlunosMatriculadosNoCursoSerializer
    authentication_classes =  [authentication.BasicAuthentication]                  #autenticacao basica para a API
    permission_classes = [permissions.IsAuthenticated]                              #somente acessa essa classe quem esta autenticado|logado

"""ESSE EH UM OUTRO METODO PARA MOSTRAR O SERIALIZER DE TODOS OS ALUNOS USANDO O APIVIEWS AO INVES DO VIEWSETS"""
class AlunoListView(views.APIView):
    def get (self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return response.Response(serializer.data)
    # authentication_classes =  [authentication.BasicAuthentication]                  #autenticacao basica para a API
    # permission_classes = [permissions.IsAuthenticated]                              #somente acessa essa classe quem esta autenticado|logado
    