import requests
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView

from api.models import ExchangeRates
from api.serializers import QuotesSerializer
from coinmena import settings


class QuotesAPI(GenericAPIView):
    serializer_class = QuotesSerializer

    def get_queryset(self):
        return ExchangeRates.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data:
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        return JsonResponse([], status=status.HTTP_200_OK)

    def post(self, request):
        from_currency = request.data['from_currency']
        to_currency = request.data['to_currency']
        data = self.get_quotes_from_alphaventage(from_currency, to_currency)
        if data:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        return JsonResponse([],status=status.HTTP_404_NOT_FOUND, safe=False)

    def get_quotes_from_alphaventage(self, from_currency, to_currency):
        params = {
            'function': 'CURRENCY_EXCHANGE_RATE',
            'from_currency': from_currency,
            'to_currency': to_currency,
            'apikey': settings.API_KEY
        }
        try:
            response = requests.get(
                'https://www.alphavantage.co/query',
                params=params
            )
            if response.status_code == status.HTTP_200_OK:
                data = response.json()['Realtime Currency Exchange Rate']
                return {
                    'from_currency': data['1. From_Currency Code'],
                    'from_currency_name': data['2. From_Currency Name'],
                    'to_currency': data['3. To_Currency Code'],
                    'to_currency_name': data['4. To_Currency Name'],
                    'exchange_rate': data['5. Exchange Rate'],
                    'last_refreshed': data['6. Last Refreshed'],
                }
        except Exception as e:
            print('An error occurred {}'.format(e))
