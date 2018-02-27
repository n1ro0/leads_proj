from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone


def date_validator(date):
    if date < timezone.now().date() + timezone.timedelta(365 / 2):
        raise ValidationError('Expiry date has to be 6 month in the future!')


card_number_validator = RegexValidator(
    regex=r'^[XTW\d]{8,15}$',
    message='Only numbers and capital letters: X, T, W are allowed'
)
