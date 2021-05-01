from django.db import models


class ExchangeRates(models.Model):
    from_currency = models.CharField(max_length=150)
    from_currency_name = models.CharField(max_length=150)
    to_currency = models.CharField(max_length=150)
    to_currency_name = models.CharField(max_length=150)
    exchange_rate = models.CharField(max_length=150)
    last_refreshed = models.DateTimeField()

    def __str__(self):
        return "{0}-{1} ({2})".format(
            self.from_currency,
            self.to_currency,
            self.exchange_rate
        )
