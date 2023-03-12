from django.urls import path

from . import views, auth

urlpatterns = [
    path('', views.create, name='create'),
    path('textloop', views.textloop, name='textloop'),
    path('signIn/', auth.signIn),
    path('postsignIn/', auth.postsignIn),
    path('signUp/', auth.signUp, name="signup"),
    path('logout/', auth.logout, name="log"),
    path('postsignUp/', auth.postsignUp),
]

