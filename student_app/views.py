from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer


class StudentView(APIView):

    def get(self, request, id=None):
        if id:
            student = get_object_or_404(Student, id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()

        return Response({"message": "Student deleted successfully"})