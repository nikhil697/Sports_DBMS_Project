from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('insertusers/', views.insertusers, name='insertusers'),
    path('showall/', views.show_students, name='show_students'),
    path('particular/', views.particular, name='particular_student'),

]

urlpatterns += staticfiles_urlpatterns()