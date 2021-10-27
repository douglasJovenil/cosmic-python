class Restaurante(object):
  def __init__(self, nome: str, pedidos_na_fila: int=0):
    self.pedidos_na_fila = pedidos_na_fila
    self.__nome = nome
  
  @property
  def pedidos_na_fila(self) -> int:
    return self.__pedidos_na_fila
  
  @pedidos_na_fila.setter
  def pedidos_na_fila(self, pedidos_na_fila: int):
    if pedidos_na_fila < 0:
      raise ValueError('Pedidos devem ser maiores que 1')
    self.__pedidos_na_fila = pedidos_na_fila

  def adiciona_pedido(self):
    self.pedidos_na_fila += 1
  
  def remove_pedido(self):
    try: 
      self.pedidos_na_fila -= 1
    except ValueError:
      self.pedidos_na_fila = 0
