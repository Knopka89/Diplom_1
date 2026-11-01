import pytest


class TestBurger:
    def test_new_burger_is_empty(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

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

    @pytest.mark.parametrize("count,expected", [(0, 200), (1, 225), (2, 275)])
    def test_get_price(self, burger, bun, ingredients, count, expected):
        burger.set_buns(bun)
        burger.ingredients = ingredients[:count]

        assert burger.get_price() == expected

    @pytest.mark.parametrize(
        "count,expected",
        [
            (0, "(==== Краторная булка ====)\n(==== Краторная булка ====)\n\nPrice: 200"),
            (2, "(==== Краторная булка ====)\n= sauce Соус =\n= filling Начинка =\n"
                "(==== Краторная булка ====)\n\nPrice: 275"),
        ],
    )
    def test_get_receipt(self, burger, bun, ingredients, count, expected):
        burger.set_buns(bun)
        burger.ingredients = ingredients[:count]

        assert burger.get_receipt() == expected
