from django.conf.urls import url, include
from . import views

urlpatterns =[
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^contact/', views.contact, name='contact'),
]