import strawberry
from .models import Product


@strawberry.type
class ProductType:
    id: int
    name: str
    description: str
    price: float
    stock: int


@strawberry.type
class Query:
    products: list[ProductType] = strawberry.field(
        resolver=lambda: Product.objects.all()
    )


schema = strawberry.Schema(query=Query)
