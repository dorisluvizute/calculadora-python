class Calculos:

    def soma(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def multi(self, num1, num2):
        return num1 * num2

    def divi(self, num1, num2):
        return num1 / num2

    def math(self, operacao, num1, num2):
        if operacao is not 'm' and operacao is not 'd' and operacao is not 's' and operacao is not 'sub':
            return False

        if operacao == 'm':
            conta1 = self.multi(num1, num2)          
            return conta1
        elif operacao == 'd':
            conta2 = self.divi(num1, num2)
            return conta2
        elif operacao == 's':
            conta3 = self.soma(num1, num2)          
            return conta3
        else:
            conta4 = self.sub(num1, num2)          
            return conta4
 