from django.db import models
from services.generator import Generator
from services.mixin import SlugMixin

class Todo(SlugMixin):
    task_name = models.CharField(max_length=200)
    deadline = models.DateField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo Lists'

    def __str__(self):
        return self.task_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Todo)
        super(Todo, self).save(*args, **kwargs)
