import pytest

from src.category import Category
from src.product import BaseProduct, LawnGrass, Product, Smartphone


@pytest.fixture()
def product() -> Product:
    return Product("name", "description", 15.99, 100)


@pytest.fixture()
def smartphone() -> Smartphone:
    return Smartphone("name", "description", 51799, 6, 99.2, "model", 32, "color")


@pytest.fixture()
def lawngrass() -> LawnGrass:
    return LawnGrass("name", "description", 1730, 158, "country", "period", "color")


@pytest.fixture()
def category(product: Product) -> Category:
    return Category("name", "description", [product])


def test_product(product: Product) -> None:
    assert product.name == "name"
    assert product.description == "description"
    assert product.price == 15.99
    assert product.quantity == 100


def test_smartphone(smartphone: Smartphone) -> None:
    assert smartphone.name == "name"
    assert smartphone.description == "description"
    assert smartphone.price == 51799
    assert smartphone.quantity == 6
    assert smartphone.efficiency == 99.2
    assert smartphone.model == "model"
    assert smartphone.memory == 32
    assert smartphone.color == "color"


def test_lawngrass(lawngrass: LawnGrass) -> None:
    assert lawngrass.name == "name"
    assert lawngrass.description == "description"
    assert lawngrass.price == 1730
    assert lawngrass.quantity == 158
    assert lawngrass.country == "country"
    assert lawngrass.germination_period == "period"
    assert lawngrass.color == "color"


def test_category(category: Category) -> None:
    assert category.name == "name"
    assert category.description == "description"
    assert category.products == ["name, 15.99 руб. Остаток: 100 шт."]
    assert category.product_count == 1


def test_number_of_categories() -> None:
    assert Category.category_count == 1
    cat2 = Category("something", "description", [])
    assert Category.category_count == 2


def test_add_product(category: Category) -> None:
    prod1 = Product("name1", "-", 1600, 1)
    category.add_product(prod1)
    assert category.product_count == 2
    category.add_product("something")
    assert category.product_count == 2


def test_new_product() -> None:
    prod2 = Product.new_product({"name": "name1", "description": "-", "price": 43892.39, "quantity": 432})
    assert type(prod2) is Product


def test_price_setter(product: Product) -> None:
    product.price = -1
    assert product.price == 15.99
    product.price = 16
    assert product.price == 16


def test_str(product: Product, category: Category) -> None:
    assert str(product) == "name, 15.99 руб. Остаток: 100 шт."
    assert str(category) == "name, количество продуктов: 1 шт."


def test_product_add(product: Product, smartphone: Smartphone, lawngrass: LawnGrass) -> None:
    prod2 = Product.new_product({"name": "name1", "description": "-", "price": 150, "quantity": 2})
    assert product + prod2 == 1899
    with pytest.raises(TypeError):
        smartphone + lawngrass


def test_abstract_class() -> None:
    with pytest.raises(TypeError):
        prod = BaseProduct()
