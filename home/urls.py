
from django.urls import path
from home import views

urlpatterns = [
    path('' , views.index , name="index"),
    path('login/' , views.login_page, name='login_page'),
    path('register/' , views.register, name='register')

]
