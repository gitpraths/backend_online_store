from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView

from product.schemas import schema

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(schema=schema))),
    path("api/", include("accounts.urls")),
]
