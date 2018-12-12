class Fila:
  def __init__(self):
    self.fila = []
  
  def dequeue(self):
    if not(self.isEmpty()):
      self.fila.pop[0]

  def enqueue(self,elemento):
    self.fila.append(elemento)

  def lenght(self):
    return len(self.fila)

  def isEmpty(self):
    return len(self.fila)==0
