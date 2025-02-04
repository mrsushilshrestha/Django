from django.urls import path
from .views import user_login,signup_user,index

urlpatterns = [
    path('login/',user_login,name="login"),
    path('signup/',signup_user,name="signup"),
    path('',index,name="index"),
    
    
    
]
