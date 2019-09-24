from django.urls import path

from exampleapp.views import *

app_name = 'exampleapp'

urlpatterns = [
    path('', ExampleView.as_view(), name='example'),
]
