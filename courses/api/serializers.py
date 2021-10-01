from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
