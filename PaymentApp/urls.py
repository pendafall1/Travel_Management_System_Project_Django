'''/PaymentApp/urls.py'''

from PaymentApp.views import *
from django.urls import re_path

urlpatterns=[
	re_path(r'^CalculateAmount/',CalculateAmount),
	re_path(r'^makepayment/',makepayment),
	re_path(r'^bill/',bill),
]