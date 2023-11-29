from django.urls import path
from api.views import ItemView, PaymentView

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='index'),
    path('buy/<int:pk>/', PaymentView.as_view(), name='payment')
]
