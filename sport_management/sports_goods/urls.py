from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('insertusers/', views.insertusers, name='insertusers'),
    path('showall/', views.show_students, name='show_students'),
    # path('particular/', views.particular, name='particular_student'),
    path('login/',views.loginpage, name='login'),
    path('loginview/',views.login_view, name='login_view'),

]

urlpatterns += staticfiles_urlpatterns()