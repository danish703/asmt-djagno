from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.create,name='blog_create'),
    path('all/',views.allnews,name="allnews"),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.remove,name='del'),
]