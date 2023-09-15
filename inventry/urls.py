from django.urls import path
from .views import *

urlpatterns = [
    path('',All_items),
    path('<str:id>',get_item)
]
