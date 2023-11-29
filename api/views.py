from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from api.models import Item
import stripe
from payment_tz import settings

# Create your views here.


class ItemView(DetailView):
    queryset = Item.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(csrf_exempt, name="dispatch")
class PaymentView(DetailView):
    queryset = Item.objects.all()
    template_name = 'payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_key'] = settings.STRIPE_PUBLIC_KEY_TEST
        return context

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
        session_stripe = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    "price_data":
                        {
                            'currency': 'usd',
                            "product_data":
                                {
                                    "name": "Item",
                                },
                            "unit_amount": 1200
                        },
                    'quantity': 1
                },
            ],
            customer_creation='always',
            mode='payment',
            success_url=f'http://127.0.0.1:8000/api/item/1/'
        )

        return JsonResponse({'id': session_stripe.id})



