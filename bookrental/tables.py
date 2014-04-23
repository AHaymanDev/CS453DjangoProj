import django_tables2 as tables
from bookrental.models import Book


class BookTable(tables.Table):

    class Meta:
        model = Book
    selection = tables.CheckBoxColumn(accessor='pk')
