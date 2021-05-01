from django.urls import path
from api.views import QuotesAPI

urlpatterns = [
    path('v1/quotes/', QuotesAPI.as_view(), name='quotes')
]
