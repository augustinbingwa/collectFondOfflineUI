from django.urls import path
from .views import CustomAuthToken
from .views import ClientList, ClientDetail
from .views import CotisationList, CotisationDetail

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
    path('cotisations/', CotisationList.as_view(), name='cotisation-list'),
    path('cotisations/<int:pk>/', CotisationDetail.as_view(), name='cotisation-detail'),
]