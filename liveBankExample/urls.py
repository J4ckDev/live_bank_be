from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authAppExample                 import views

urlpatterns = [
    path('login/',                                  TokenObtainPairView.as_view()),
    path('refresh/',                                TokenRefreshView.as_view()),
    path('user/',                                   views.UserCreateView.as_view()),
    path('user/<int:pk>/',                          views.UserDetailView.as_view()),
    path('transaction/create/',                     views.TransactionCreateView.as_view()), 
    path('transaction/<int:user>/<int:pk>/',        views.TransactionDetailView.as_view()),
    path('transaction/update/<int:user>/<int:pk>/', views.TransactionUpdateView.as_view()),
    path('transaction/remove/<int:user>/<int:pk>/', views.TransactionDeleteView.as_view()),
    path('transactions/<int:user>/<int:account>/',  views.TransactionsAccountView.as_view()),
]