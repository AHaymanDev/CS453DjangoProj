import django_tables2 as tables
import django_tables2.columns.CheckBoxColumn
from bookrental.models import Book


class BookTable(tables.Table):

    class Meta:
        model = Book
    selection = tables.CheckBoxColumn(accessor='pk')
