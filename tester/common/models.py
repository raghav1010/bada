from django.db import models

# Create your models here.
# Create your models here.
import uuid

from django.db import models


class BaseModel(models.Model):
    """
    A base model
    NOTE: Make sure to inherit this base class in every model creation
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        related_name="created_%(class)ss",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        related_name="updated_%(class)ss",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class BaseModelWithOutPrimaryKey(models.Model):
    """
    This model without primary key making
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        related_name="created_%(class)ss",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        related_name="updated_%(class)ss",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    """
    A base model  with only timestamp
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        related_name="created_%(class)ss",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        "sample.User",
        on_delete=models.CASCADE,
        related_name="updated_%(class)ss",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
