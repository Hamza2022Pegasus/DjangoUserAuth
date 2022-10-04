from django.urls import path
from account.views import UserRegistationView, UserLoginView

urlpatterns =[
    path('register/', UserRegistationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

]