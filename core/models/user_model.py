from django.db import models
from core.models.role_model import Role
from core.models.reader_model import Reader


class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=20)
    hashed_password = models.CharField(max_length=20)
    role = models.ForeignKey(Role,
        on_delete=models.CASCADE,
        db_column='role'
    )
    reader = models.ForeignKey(Reader,
        on_delete=models.CASCADE,
        db_column='reader_id'
    )

    class Meta():
        db_table = 'user'