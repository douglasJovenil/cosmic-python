from pytest import raises


def soma_1(n: int) -> int:
  return int(n) + 1

def test_soma_1():
  assert soma_1(41) == 42

def test_soma_1_numero_como_string():
  assert soma_1('41') == 42

def test_soma_1_palavra():
  with raises(ValueError):
    soma_1('fabio')

