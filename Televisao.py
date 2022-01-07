from Calculadora import Calc

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal=4
        self.volume=10
        
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumenta_canal(self):
        self.canal +=1
        
    def diminui_canal(self):
        self.canal -=1
        
    def aumenta_volume(self):
        self.canal +=1
        
    def diminui_volume(self):
        self.canal -=1

if __init__== '__main__': 
#O if diz que se eu importar esse código 
#para outro o que está abaixo do if não será chamado!!!

    televisao = Televisao()
    print(televisao.ligada())
    televisao.power()
    print(televisao.ligada())
    televisao.power()
    print(televisao.ligada())
    
    print("Canais\n")
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    televisao.diminui_canal()
    
    print("Volume\n")
    televisao.aumenta_volume()
    televisao.aumenta_volume()
    televisao.aumenta_volume()
    televisao.diminui_volume()
    
    print("Calculadora\n")
    calculadora = Calc(10,2)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())