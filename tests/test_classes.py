import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product() -> Product:
    return Product("name", "description", 15.99, 100)


@pytest.fixture()
def category() -> Category:
    return Category("name", "description", [product])


def test_product(product: Product) -> None:
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 15.99
    assert product.quantity == 100


def test_category(category: Category) -> None:
    assert category.name == "name"
    assert category.description == "description"
    assert category.products == [product]
    assert category.product_count == 1


def test_number_of_categories() -> None:
    assert Category.category_count == 1
    cat2 = Category('something', 'description', [])
    assert Category.category_count == 2
