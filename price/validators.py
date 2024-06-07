from rest_framework.exceptions import ValidationError


def validate_positive_price(price):
    """Валидатор на положительную цену"""
    if price.start_price < 0:
        raise ValidationError('Укажите положительную цену.')
