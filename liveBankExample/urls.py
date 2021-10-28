from django.urls                    import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authAppExample                 import views as authViews

urlpatterns = [
    path('login/',                                  TokenObtainPairView.as_view()),
    path('refresh/',                                TokenRefreshView.as_view()),
    path('user/',                                   authViews.UserCreateView.as_view()),
    path('user/<int:pk>/',                          authViews.UserDetailView.as_view()),
    path('transaction/create/',                     authViews.TransactionCreateView.as_view()), 
    path('transaction/<int:user>/<int:pk>/',        authViews.TransactionDetailView.as_view()),
    path('transaction/update/<int:user>/<int:pk>/', authViews.TransactionUpdateView.as_view()),
    path('transaction/remove/<int:user>/<int:pk>/', authViews.TransactionDeleteView.as_view()),
    path('transactions/<int:user>/<int:account>/',  authViews.TransactionsAccountView.as_view()),
    path('account/myAccounts/<int:user>/',          authViews.ListAccountsView.as_view()), 
    path('account/clientsAccounts/<int:user>/',     authViews.ListAnotherAccountsView.as_view()), 
]