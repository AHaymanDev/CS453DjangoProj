import django_tables2 as tables
from bookrental.models import Book


class BookTable(tables.Table):

    class Meta:
        model = Book
        attrs = {'width': '200%'}
    selection = tables.CheckBoxColumn(accessor='pk')
