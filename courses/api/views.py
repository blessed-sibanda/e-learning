from django.views.generic import detail
from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from ..models import Course, Subject
from .serializers import SubjectSerializer, CourseSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post', 'delete'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        if request.method == 'POST':
            course.students.add(request.user)
        elif request.method == 'DELETE':
            course.students.remove(request.user)
        return Response({'success': True})
