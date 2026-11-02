class BurgerData:
    BUN_NAME = "Краторная булка"
    BUN_PRICE = 100
    SAUCE_NAME = "Соус"
    SAUCE_TYPE = "SAUCE"
    SAUCE_PRICE = 25
    FILLING_NAME = "Начинка"
    FILLING_TYPE = "FILLING"
    FILLING_PRICE = 50

    PRICES = [
        (0, BUN_PRICE * 2),
        (1, BUN_PRICE * 2 + SAUCE_PRICE),
        (2, BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE),
    ]
    BUN_LINE = f"(==== {BUN_NAME} ====)"
    RECEIPTS = [
        (0, f"{BUN_LINE}\n{BUN_LINE}\n\nPrice: {BUN_PRICE * 2}"),
        (2, f"{BUN_LINE}\n= {SAUCE_TYPE.lower()} {SAUCE_NAME} =\n"
            f"= {FILLING_TYPE.lower()} {FILLING_NAME} =\n{BUN_LINE}\n\n"
            f"Price: {BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE}"),
    ]
