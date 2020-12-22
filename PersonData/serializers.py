from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person 
        fields = ('name', 'gender', 'age', 'react_time', 'test_variant')
