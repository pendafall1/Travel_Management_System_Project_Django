''' /BookTicketApp/urls.py '''

from BookTicketApp.views import *
from django.urls import re_path

urlpatterns=[
	re_path(r'^book_ticket/',book_ticket),
	re_path(r'^bookingdataadd/',bookingdataadd),
	re_path(r'^booking_history/', booking_history),
	re_path(r'^delete/',delete),
	re_path(r'^feedback/',feedback),

]