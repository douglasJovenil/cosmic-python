from pytest import raises, fixture, mark
from restaurante import Restaurante


@fixture
def restaurante_fila_vazia():
    return Restaurante('Pizzaria X')


@fixture
def restaurante_com_um_pedido():
    return Restaurante('Pizzaria X', 1)


def test_pedidos_na_fila_valor_inical_padrao_igual_a_zero(restaurante_fila_vazia: Restaurante):
    assert restaurante_fila_vazia.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_Finicial_maior_que_zero(restaurante_com_um_pedido: Restaurante):
    assert restaurante_com_um_pedido.pedidos_na_fila == 1


def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with raises(ValueError):
        Restaurante('Pizzaria X', -1)


def test_adiciona_um_pedido_na_fila(restaurante_com_um_pedido: Restaurante):
    restaurante_com_um_pedido.adiciona_pedido()
    assert restaurante_com_um_pedido.pedidos_na_fila == 2


def test_remove_um_pedido_na_fila(restaurante_com_um_pedido: Restaurante):
    restaurante_com_um_pedido.remove_pedido()
    assert restaurante_com_um_pedido.pedidos_na_fila == 0


def test_remove_um_pedido_vazio_na_fila_vazia(restaurante_fila_vazia: Restaurante):
    restaurante_fila_vazia.remove_pedido()
    restaurante_fila_vazia.pedidos_na_fila == 0


@mark.parametrize('inicial, final', [(0, 0), (1, 0), (2, 1)])
def test_remocao_de_pedidos(inicial: int, final: int):
    restaurante = Restaurante('Pizzaria X', inicial)
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == final
