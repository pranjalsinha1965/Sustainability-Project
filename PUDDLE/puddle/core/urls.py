from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('cards/', views.cards_view, name='cards'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    # path('import/', ImportAPIView.as_view(), name='import-api'),
    # path('import/', ExportAPIView.as_view(), name='import-api')
]
