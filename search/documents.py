from django_elasticsearch_dsl import Index, DocType

from products.models import Product

products = Index('products')


@products.doc_type
class ProductDocument(DocType):
    class Meta:
        model = Product

        fields = [
            'name',
            'colors',
        ]
