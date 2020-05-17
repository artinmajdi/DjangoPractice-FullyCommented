from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Info(models.Model):
    """Model definition for Info."""

    name = models.CharField(max_length=150)

    slug = models.SlugField(max_length=250, unique_for_date='contract_date')

    representative = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers_info')

    description = models.TextField()

    revenue = models.FloatField()

    contract_date = models.DateTimeField(default=timezone.now)

    PRODUCT_LIST = (
        ('mri_segmentation', 'MRI Segmentation'),
        ('administrative_manager', 'Administrative Manager'),
    )

    bought_product = models.CharField(max_length=50, choices=PRODUCT_LIST, default='administrative_manager')

    class Meta:
        ordering = ('-contract_date',)

    def __str__(self):
        return self.name


""" this is the field for my customer companies information such as what they are buying,
how much they are buying, how long they have been my customers, etc. """
