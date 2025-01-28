import uuid
from django.utils.translation import gettext_lazy as _

from django.db import models


class AbstractBaseModel(models.Model):
    """
    Base abstract model, that has `uuid` instead of `id` and includes `created_at`, `updated_at` fields.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    is_active = models.BooleanField(_('Is active'), default=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    created_by = models.CharField('Create by', max_length=255, null=True)
    updated_by = models.CharField('Update by', max_length=255, null=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'
