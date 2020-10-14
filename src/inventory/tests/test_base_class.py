from src.inventory.base_class import BaseProduct


def test_is_base_class_has_name_attr():
    x = BaseProduct(1, 2, "ala")
    assert hasattr(x, "name")


def test_is_base_class_has_quantity_attr():
    x = BaseProduct(1, 2, "ala")
    assert hasattr(x, "quantity")


def test_is_base_class_has_price_attr():
    x = BaseProduct(1, 2, "ala")
    assert hasattr(x, "price")


def test_base_class_repr():
    x = BaseProduct(1, 2, "ala")
    assert repr(x) == "ala"