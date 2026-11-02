import pytest

from data import BurgerData


class TestBurger:
    def test_burger_without_ingredients_has_bun_price(self, burger, bun):
        burger.set_buns(bun)

        assert burger.get_price() == BurgerData.BUN_PRICE * 2

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredients_preserves_order(self, burger, ingredients):
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.ingredients == ingredients

    @pytest.mark.parametrize("index", [0, 1])
    def test_remove_ingredient(self, burger, ingredients, index):
        burger.ingredients = ingredients.copy()

        burger.remove_ingredient(index)

        assert burger.ingredients == [ingredients[1 - index]]

    @pytest.mark.parametrize("index,new_index", [(0, 1), (1, 0)])
    def test_move_ingredient(self, burger, ingredients, index, new_index):
        burger.ingredients = ingredients.copy()

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == [ingredients[1], ingredients[0]]

    @pytest.mark.parametrize("count,expected", BurgerData.PRICES)
    def test_get_price(self, burger, bun, ingredients, count, expected):
        burger.set_buns(bun)
        burger.ingredients = ingredients[:count]

        assert burger.get_price() == expected

    @pytest.mark.parametrize("count,expected", BurgerData.RECEIPTS)
    def test_get_receipt(self, burger, bun, ingredients, count, expected):
        burger.set_buns(bun)
        burger.ingredients = ingredients[:count]

        assert burger.get_receipt() == expected
