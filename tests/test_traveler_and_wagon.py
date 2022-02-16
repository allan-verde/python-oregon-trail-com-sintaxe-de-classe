from Traveler import Traveler
from Wagon import Wagon


def test_exercise_1():

    wagon = Wagon(2)

    expect = 2
    result = wagon.get_available_seat_count()

    assert type(result) is int, "Verificar se está retornando um inteiro"

    assert (
        result == expect
    ), "Verificar se o resultado é igual a 2"


def test_exercise_2():

    wagon = Wagon(2)
    henrietta = Traveler('Henrietta')
    wagon.join(henrietta)

    expect = 1
    result = wagon.get_available_seat_count()

    assert type(result) is int, "Verificar se está retornando um inteiro"

    assert (
        result == expect
    ), "Verificar se o resultado é igual a 1"

  
def test_exercise_3():

    wagon = Wagon(2)
    henrietta = Traveler('Henrietta')
    juan = Traveler('Juan')
    maude = Traveler('Maude')
    wagon.join(henrietta)
    wagon.join(juan)
    wagon.join(maude)

    expect = 0
    result = wagon.get_available_seat_count()

    assert type(result) is int, "Verificar se está retornando um inteiro"

    assert (
        result == expect
    ), "Verificar se o resultado é igual a 0"


def test_exercise_4():

    wagon = Wagon(2)
    henrietta = Traveler('Henrietta')
    juan = Traveler('Juan')
    maude = Traveler('Maude')
    wagon.join(henrietta)
    wagon.join(juan)
    wagon.join(maude)
    henrietta.hunt()
    juan.eat()
    juan.eat()

    expect = True
    result = wagon.should_quarantine()

    assert type(result) is bool, "Verificar se está retornando um boleano"

    assert (
        result == expect
    ), "Verificar se o resultado é True"


def test_exercise_5():

    wagon = Wagon(2)
    henrietta = Traveler('Henrietta')
    juan = Traveler('Juan')
    maude = Traveler('Maude')
    wagon.join(henrietta)
    wagon.join(juan)
    wagon.join(maude)
    henrietta.hunt()
    juan.eat()
    juan.eat()

    expect = 3
    result = wagon.total_food()

    assert type(result) is int, "Verificar se está retornando um inteiro"

    assert (
        result == expect
    ), "Verificar se o resultado é 3"