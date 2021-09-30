from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = 'Tag'


class Snippet(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    created = models.DateTimeField( auto_now=True)
    tag = models.ForeignKey(Tag,  on_delete=models.CASCADE)

    class Meta:
        db_table = 'Snippet'