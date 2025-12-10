import pytest
from unittest.mock import patch
from e1 import intersecao_listas


@patch("intersecao_func.random.randint")
def test_intersecao_usando_mocker_completo(mock_randint):

    mock_randint.side_effect = [
        5,
        5,
        5,
        5,
        5,
        1,
        2,
        3,
        4,
        10,
        5,
        5,
        5,
        5,
        5,
        10,
        20,
        30,
        40,
        50,
    ]

    resultado = intersecao_listas()

    esperado = {5, 10}

    assert set(resultado) == esperado
