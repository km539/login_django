from django.db import models
import uuid

# db model for user
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    hashedpassword = models.TextField()
    salt = models.TextField()

    def __str__(self):
        return self.username
