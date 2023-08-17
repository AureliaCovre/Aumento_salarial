# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e 
# o índice reajustado (em porcentagem)


salario = int(input("Qual o salário? ")) 

if salario <= 600:
    percentual = 0.17
elif salario <= 900:
    percentual = 0.13
elif salario <= 1500:
    percentual = 0.12
elif salario <= 2000:
    percentual = 0.10
else:
    percentual = 0.05
    
aumento = salario * percentual
novo_salario = salario + aumento
percentual_1 = percentual * 100

print("{:.2f} \n{:.2f} \n{:.0f} %".format(novo_salario, aumento, percentual_1))  