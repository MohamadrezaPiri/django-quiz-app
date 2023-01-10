from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from .models import Quizzes, Question

# Create your views here.


class QuizzesList(ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(
            quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
