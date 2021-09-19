# Função é tudo que retorna ao valor, método é o que não retorna.No Python o método é chamado de definição.
def soma(a, b):
    return a + b

print(soma(1, 2))
print(soma(3, 4))

def subtracao(a, b):
    return a - b

print(soma(5, 3))

# Ensinando a fazer criando a classe

class Calculadora:
    def __init__(self, num1, num2): # tem dois underline antes e dois depois essa merda aqui
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b 

if __name__ == '__main__':
    calculadora = Calculadora(10, 2) 
#chamei a classe da calculadora

    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())

# Fazer a mesma coisa sem definir os num
class Calculadora2:
    def __init__(self): 
    # tem dois underline antes e dois depois essa merda aqui
        pass 
        #não faz nada, só pro init não fica vazio
    # poderia acabar o def init e o pass tbm

    def soma(self, valor_a, valor_b): #tem que declarar eles aqui
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b): #tem que declarar eles aqui
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b): #tem que declarar eles aqui
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b): #tem que declarar eles aqui
        return valor_a / valor_b 


calculadora = Calculadora2() 
print(calculadora.soma(10, 2))
print(calculadora.subtracao(10, 5))
print(calculadora.multiplicacao(2, 3))
print(calculadora.divisao(9, 3))