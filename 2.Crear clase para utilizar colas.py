class Cola:
    def __init__(self):
        self.items = []
        
    def estaVacia(self):
        return self.items == []
    
    def agregar(self, item):
        self.items.insert(0,item)
    
    def avanzar(self):
        return self.items.pop()
        
    def tamaño(self):
        return len(self.items)
        
c=Cola()

c.agregar(4)
c.agregar('perro')
c.agregar(True)
print(c.tamaño())

print(c.estaVacia())
c.agregar(8.4)
print(c.avanzar())
print(c.avanzar())
print(c.tamaño())