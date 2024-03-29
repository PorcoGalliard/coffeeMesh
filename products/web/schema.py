from pathlib import Path

from ariadne import make_executable_schema

from web.queries import query

from web.types import product_type, datetime_scalar

from web.mutations import mutation

schema = make_executable_schema(
    (Path(__file__).parent /
     'products.graphql').read_text(),
    [query, mutation, product_type, datetime_scalar]
)
