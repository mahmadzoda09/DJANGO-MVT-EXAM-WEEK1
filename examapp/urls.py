from django.urls import path
from .views import *

urlpatterns = [
    path('main' , main , name='main'),
    path('author' , author , name='author'),
    path('create' , create , name='create'),
    path('book' , book , name='book'),
    path('detail/<int:id>' , detail , name='detail'),
    path('delete/<int:id>' , delete , name='delete'),
    path('update/<int:id>' , update , name='update'),
    path('add' , add , name='add'),
]