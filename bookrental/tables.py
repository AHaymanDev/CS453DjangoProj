import django_tables2 as tables
from bookrental.models import Book
from bookrental.models import Cart
from bookrental.models import Prices


class BookTable(tables.Table):

    class Meta:
        model = Book
        attrs = {'width': '120%'}
    selection = tables.CheckBoxColumn(accessor='pk')


class CartTable(tables.Table):
    class Meta:
        model = Cart
        attrs = {'width': '120%'}


class PriceTable(tables.Table):
    class Meta:
        model = Prices
        attrs = {'width': '120%'}
