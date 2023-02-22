from django.contrib.auth import views as auth_view
from django.urls import path


from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('signup/', view=views.signup, name='signup'),
    path('login/', view=auth_view.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', view=auth_view.LogoutView.as_view(), name='logout'),
]
