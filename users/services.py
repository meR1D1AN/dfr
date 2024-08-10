import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount):
    """
    Создаёт цену в страйпе
    :param amount:
    :return:
    """
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": "DONAT"},
    )


def create_stripe_session(price):
    """
    Создаёт сессию в страйпе
    :param price:
    :return session_id, url:
    """
    sessoin = stripe.checkout.Session.create(
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
        success_url="http://127.0.0.1:8000/",
    )
    return sessoin.get("id"), sessoin.get("url")

