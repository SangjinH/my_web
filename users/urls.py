from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('signup/', views.SignupView.as_view()),
]

urlpatterns += [
    path('api-token-auth/', views.CustomAuthToken.as_view()),
]









# urlpatterns = [
#     path('', views.User
#     path('<int:pk>/', views.UserDetail.as_view()),
#     path('signup/', views.SignupView.as_view()),
# ]

# urlpatterns += [
#     path('api-token-auth/', CustomAuthToken.as_view())
# ]

    
    