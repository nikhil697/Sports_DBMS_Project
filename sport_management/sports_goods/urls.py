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
    path('resetpage/',views.resetpass, name='reset_page'),
    path('resetpass1/',views.resetpassfunc, name='reset_pass'),
    path('success/',views.success,name='success'),
    # path('book/', views.book_equipment, name='book_equipment'),

]

urlpatterns += staticfiles_urlpatterns()