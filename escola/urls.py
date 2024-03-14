#Esse arquivo eh responsavel por gerenciar as urls que chegam 

from .views import AlunoViewSet, CursoViewSet, MatriculaViewSet, AlunoListView, ListaMatriculasPorAluno, ListaAlunosMatriculadosPorCurso
from django.urls import path,include
from rest_framework import routers                                    

router = routers.DefaultRouter()                                                        #criando uma rota base para acessar a api 
router.register('alunos', AlunoViewSet, basename='Alunos')                              #criando a rota relativa alunos para acessar o modelo Aluno com o serializer 
router.register('cursos', CursoViewSet, basename='Cursos')                              #criando a rota relativa cursos para acessar o modelo Curso com o serializer
router.register('matriculas',MatriculaViewSet,basename='Matriculas')                    #criando a rota relativa matriculas para acessar o modelo Matricula com o serializer

urlpatterns = [
    path('',include(router.urls)),                                                      #essa rota padrao direciona para as duas rotas relativas criadas usando o viewset
    path('alunoslista/', AlunoListView.as_view()),                                      #essa rota eh referente a uma outra visualizacao da serializacao de ALunos usando o APIVIEW ao invez do Viewset                         
    path('alunos/<int:pk>/matriculas/', ListaMatriculasPorAluno.as_view()),             #essa rota eh a rota para filtrar todas as matriculas de um aluno. Eh necessario que tenha o "pk" que eh o mesmo nome criado na class ListaMatriculasPorAluno
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculadosPorCurso.as_view())      #essa rota eh a rota para filtrar todas os alunos matriculas em um curso. Eh necessario que tenha o "pk" que eh o mesmo nome criado na class ListaMatriculasPorAluno
]