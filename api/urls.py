from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.getChat),
    path('predict/', views.getPredict),

]
