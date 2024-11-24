from rest_framework import serializers
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    field="__all__"