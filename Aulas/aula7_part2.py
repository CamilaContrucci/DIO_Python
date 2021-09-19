# A partir dos 15m. Aqui de fato é uma definição de método porque não tem return.

class Televisao:
    def __init__(self):
        self.ligada = False # tv começa desligada
        self.canal = 5 # começa no canal 5

    def power(self): # Botão power. Se ela estiver ligada, eu desligo. Se não estiver ligada, eu ligo.
        if self.ligada:
            self.ligada = False
            
        else:
            self.ligada = True
    
    def aumenta_canal(self): # incluindo canal
        if self.ligada:
            self. canal += 1

    def diminui_canal(self): # descendo canal
        if self.ligada:
            self. canal -= 1
    
    
print (__name__)
if __name__ == '__main__':
    televisao = Televisao()
    print('Televsão está ligada: {}'. format(televisao.ligada))
    televisao.power()
    print('Televsão está ligada: {}'. format(televisao.ligada))
    televisao.power()
    print('Televsão está ligada: {}'. format(televisao.ligada))

    print('Canal: {}' .format(televisao.canal))
    televisao.power()
    print('Televsão está ligada: {}'. format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}' .format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}' .format(televisao.canal))
