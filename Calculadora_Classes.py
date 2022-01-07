# a ideia seria continuar implenentando para deixa-la mais completa
# e mais proxima da realidade possivel!!!
class Calc:
    def soma(a,b):
        return a + b
        
    def subtracao(a,b):
        return a - b
        
    def multiplicacao(a,b):
        return a * b
        
    def divisao(a,b):
        return a / b
        
if __name__=='__main__':
    calculadora = Calc(10,2)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
