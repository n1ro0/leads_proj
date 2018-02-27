from django.db import models
from django.core.exceptions import ValidationError


from . import validators


class Lead(models.Model):
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_CHOICES = (
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female')
    )

    PROFESSIONAL_YES = 'y'
    PROFESSIONAL_NO='n'
    PROFESSIONAL_CHOICES = (
        (PROFESSIONAL_YES, 'yes'),
        (PROFESSIONAL_NO, 'no')
    )

    name = models.CharField(max_length=255, verbose_name='name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_MALE)
    card_number = models.CharField(
        max_length=15, blank=True, unique=True, null=True,
        validators=[validators.card_number_validator]
    )
    expiry_date = models.DateField(
        blank=True, null=True,
        validators=[validators.date_validator]
    )
    professional = models.CharField(max_length=1, choices=PROFESSIONAL_CHOICES, default=PROFESSIONAL_YES)

    def clean(self):
        if self.card_number:
            if not self.expiry_date:
                raise ValidationError('Expiry data has to be at least 6 months into the future')
        return super(Lead, self).clean()


class Language(models.Model):
    name = models.CharField(max_length=100)
    lead = models.ForeignKey(Lead, related_name='languages')

    class Meta:
        unique_together = (('name', 'lead'),)

