class Avioes:
  def __init__(self):
    self.fila = []

  def AutorizarDecolagem(self):
    if not (len(self.fila)==0):
      self.fila.pop(0)

  def adicionarAviao(self,aviao):
    self.fila.append(aviao)

  def AvioesEspera(self):
    return len(self.fila)

  def PrimeiroAviao(self):
    return self.fila[0]

  
