import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name):
    """Создание продукта в Stripe."""
    return stripe.Product.create(name=name)


def create_stripe_price(product_id, amount):
    """Создание цены для продукта в Stripe."""
    return stripe.Price.create(
        product=product_id,
        unit_amount=amount,
        currency="rub",
    )


# def create_stripe_checkout_session(price_id):
#     """Создание сессии оплаты в Stripe."""
#     return stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price': price_id,
#             'quantity': 1,
#         }],
#         mode='payment',
#         success_url="http://127.0.0.1:8000"
#     )

def create_stripe_checkout_session(price_id, success_url, cancel_url):
    """Создание сессии оплаты в Stripe."""
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )
