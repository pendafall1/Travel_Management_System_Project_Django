''' /loginmodule/urls.py '''

from loginmodule.views import *
#from django.contrib.auth import views as auth_views
from django.urls import re_path

urlpatterns=[
    re_path(r'^home/',home),
    re_path(r'^login/',login),
    re_path(r'^logout/',logout),
    re_path(r'^auth/',auth_view),
    re_path(r'^aboutus/',aboutus),
]