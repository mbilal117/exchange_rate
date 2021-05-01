from rest_framework import serializers

from api.models import ExchangeRates


class QuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRates
        fields = '__all__'
