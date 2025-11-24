from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('addPicture/',views.addPicture,name='addPicture'),
    path('picture_detail/<int:pk>',views.picture_detail,name='picture_detail'),
    path('delete_picture/<int:pk>',views.delete_picture,name='delete_picture'),
    path('edit_picture/<int:pk>',views.edit_picture,name='edit_picture'),
]