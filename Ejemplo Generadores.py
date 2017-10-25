def cuadrados(numeros):
    resultado = []
    for i in numeros:
        resultado.append(i*i)
    return resultado

mis_num = cuadrados([1,2,3,4,5])

print mis_num
print cuadrados
def cuadrados_gen(numeros):
    for i in numeros:
        yield i*i


mis_num = cuadrados_gen([1,2,3,4,5])

print mis_num
print cuadrados_gen
#for num in mis_num:
#    print num
print list(mis_num)
for i in mis_num:
    print i

