from django.db import models

class BookCopyCondition(models.Model):
    condition_id = models.AutoField(primary_key = True)
    condition = models.CharField(30, null=True, unique=True)

    class Meta():
        db_table = 'bookcopycondition'