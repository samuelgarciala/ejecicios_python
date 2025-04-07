class Cuenta_bancaria:
    def __init__(self,titular,saldo):
        self.__titular_cuenta=titular
        self.saldo_cuenta=saldo
    
    def depositar(self,monto):
        if monto > 0:
            self.saldo_cuenta += monto
            self.mostrar_saldo()          
        else:
            print("monto invalido")
                
    def retirar(self,monto):
        if monto < 0 or monto>self.saldo_cuenta: 
            print("monto invalido")
            
        else:
            self.saldo_cuenta -= monto
            self.mostrar_saldo()   
            
    def mostrar_saldo(self):
        print(f"{self.__titular_cuenta} , su saldo actual  es: {self.saldo_cuenta}")
    
    def get_titular(self):
        return self.__titular_cuenta
    
    def set_titular(self,nuevo_titular):
        self.__titular_cuenta=nuevo_titular
        

    
banco=Cuenta_bancaria("Pablo",2000)

banco.mostrar_saldo()
banco.saldo_cuenta=-1000
banco.mostrar_saldo()