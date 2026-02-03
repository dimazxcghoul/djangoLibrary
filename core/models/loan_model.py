from datetime import datetime

import django.utils.timezone
from django.db import models

from core.models.book_copy import BookCopy
from core.models.loan_status_model import Status
from core.models.reader_model import Reader


class Loan(models.Model):
    loan_id = models.AutoField(primary_key = True)
    issue_date = models.DateField(default=django.utils.timezone.now().date()) # Дата выдачи
    due_date = models.DateField()   # Дата к которой нужно вернуть
    return_date = models.DateField()  # Фактическая дата возврата
    status = models.ForeignKey(Status,
        on_delete=models.CASCADE,
        db_column='status_id'
        )
    reader = models.ForeignKey(Reader,
        on_delete=models.CASCADE,
        db_column='reader_id'
        )
    book_copy = models.ForeignKey(BookCopy,
        on_delete=models.CASCADE,
        db_column='bookcopy_id'
        )

    class Meta():
        db_table = 'loan'