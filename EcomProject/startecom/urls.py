from django.urls import path
from startecom import views
from django.contrib.auth import views as auth_views
from startecom.forms import LoginForm

app_name='startecom'


urlpatterns=[
    path('',views.index,name="index"),
    path('login/',auth_views.LoginView.as_view(template_name='startecom/login.html',authentication_form=LoginForm),name='login'),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name="signup"),
    path('logout',views.logout_user,name="logout"),
]