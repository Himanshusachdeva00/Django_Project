from django.urls import path
from .views import ProductApi
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns =[
   path('product/', ProductApi.as_view()),
   path('product/<int:pk>/', ProductApi.as_view()),
   path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
   path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]

















