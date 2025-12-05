def sum(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 - num2
    return result

def multiplicar(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    if num2 == 0:
        return "Erro"     
    return num1 / num2

def percent(num1, total):
    return (num1 / 100) * total

