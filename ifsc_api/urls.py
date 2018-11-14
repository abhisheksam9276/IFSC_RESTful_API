from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

urlpatterns=[
    url(r'^ifsc/', views.ifsc_details, name='ifsc'),
]