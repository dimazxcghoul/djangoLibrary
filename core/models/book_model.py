from django.db import models

from core.models.publisher_model import Publisher


class Book(models.Model):
    book_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=17)
    bbc = models.CharField(max_length=30)
    published_city = models.CharField(max_length=50)
    published_year = models.IntegerField()
    pages = models.IntegerField()

    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  db_column='publisher_id'
                                  )

    class Meta():
        db_table = 'book'



