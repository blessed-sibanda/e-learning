from rest_framework import generics, viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from ..models import Course, Subject
from .serializers import CourseWithContentsSerializer, SubjectSerializer, CourseSerializer, \
    CourseWithContentsSerializer
from .permissions import IsEnrolled


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

    @action(detail=True, methods=['get'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def status(self, request, *args, **kwargs):
        if self.get_object().students.filter(id=request.user.id) \
                .exists():
            return Response({'enrolled': True})
        else:
            return Response({'enrolled': False})

    @action(detail=True, methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
