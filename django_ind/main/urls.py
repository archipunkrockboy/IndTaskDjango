from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),# если перешли на главную страницу то вызывай index из views
    path('view_picture', views.view_picture),
    path('view_pictures', views.view_pictures),
    path('view_painters', views.view_painters),
    path('view_galleries', views.view_galleries),
    path('thanks', views.thanks, name='thanks'),
    path('change_picture', views.change_picture),
    path('change_gallery', views.change_gallery),
    path('change_painter', views.change_painter)
]
