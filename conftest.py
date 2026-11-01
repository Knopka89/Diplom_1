from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Краторная булка"
    mock_bun.get_price.return_value = 100
    return mock_bun


@pytest.fixture
def ingredients():
    sauce = Mock()
    sauce.get_name.return_value = "Соус"
    sauce.get_type.return_value = "SAUCE"
    sauce.get_price.return_value = 25
    filling = Mock()
    filling.get_name.return_value = "Начинка"
    filling.get_type.return_value = "FILLING"
    filling.get_price.return_value = 50
    return [sauce, filling]
