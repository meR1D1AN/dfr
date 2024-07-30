from rest_framework.serializers import ValidationError

danger_words = ["ставки", "крипта", "продам", "гараж"]


def validate_danger_words(value):
    if value.lower() in danger_words:
        raise ValidationError("Слова запрещены")
    return value
