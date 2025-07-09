from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import LoginForm 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('inbox/', include('conversation.urls')),
    path('contact/', views.contact, name='contact'),
    path('cards/', views.cards_view, name='cards'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    # path('import/', ImportAPIView.as_view(), name='import-api'),
    # path('import/', ExportAPIView.as_view(), name='import-api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
