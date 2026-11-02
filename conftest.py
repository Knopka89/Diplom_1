from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from data import BurgerData


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = BurgerData.BUN_NAME
    mock_bun.get_price.return_value = BurgerData.BUN_PRICE
    return mock_bun


@pytest.fixture
def ingredients():
    sauce = Mock()
    sauce.get_name.return_value = BurgerData.SAUCE_NAME
    sauce.get_type.return_value = BurgerData.SAUCE_TYPE
    sauce.get_price.return_value = BurgerData.SAUCE_PRICE
    filling = Mock()
    filling.get_name.return_value = BurgerData.FILLING_NAME
    filling.get_type.return_value = BurgerData.FILLING_TYPE
    filling.get_price.return_value = BurgerData.FILLING_PRICE
    return [sauce, filling]
