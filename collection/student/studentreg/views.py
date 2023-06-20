# from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def register_student(request):
    serializer = StudentSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)