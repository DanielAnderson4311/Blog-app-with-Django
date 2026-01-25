from django.db import models

# Create your models here.


class Permissions(models.Model):
    # Empty model that will just store the permissions that I will later make so that it will group them and keep userrs ffor doing things that they can do.....
    class Meta:
        permissions = [
            ("can_edit_posts", "Can edit posts"), # Dummy permission to begin with.... - the first one is the name of the perm and the second is the human way to read it....
        ]