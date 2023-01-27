from django.db import models

class SlugMixin(models.Model):
    slug = models.SlugField(unique=True, editable=False, null=True, blank=True)

    class Meta:
        abstract = True
