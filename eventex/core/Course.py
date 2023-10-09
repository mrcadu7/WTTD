from eventex.core.models import Activity


from django.db import models


class Course(Activity):
    slots = models.IntegerField()

    class Meta:
        verbose_name_plural = 'cursos'
        verbose_name = 'curso'
