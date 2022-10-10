from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.getChatBot),
    path('predict/', views.getPrecdict),

]
