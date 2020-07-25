from rest_framework import serializers
from firstapp.models import Quizz

# code to convert all the dictionary items into JSON format (serialization)
class quizzserializer(serializers.ModelSerializer):
    class Meta:
        model = Quizz
        fields = "__all__"
