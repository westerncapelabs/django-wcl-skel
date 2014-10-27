from django.db import models
from django_hstore import hstore

# Create your models here.

class HStoreModel(models.Model):
    objects = hstore.HStoreManager()

    class Meta:
        abstract = True

class DummyModel(HStoreModel):
    """
    - Nice docstring please
    """
    msisdn = models.BigIntegerField()
    product_code = models.CharField(max_length=20)
    data = hstore.DictionaryField()  # can pass attributes like null, blank, ecc.
   
