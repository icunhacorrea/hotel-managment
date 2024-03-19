from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

app_name = "core"

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('hotels/', views.HotelList.as_view()),
    path('hotels/<str:pk>/', views.HotelDetail.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

