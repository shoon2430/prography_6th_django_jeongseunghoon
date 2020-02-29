from django.db import models
from core import models as core_model

# Create your models here.


class Post(core_model.Core):

    title = models.CharField(max_length=300, blank=True, null=True)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    Contents = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.pk)
