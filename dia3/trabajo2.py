#cuanto vamos invertir
# cuantos años
#cuantos interes
def calcular_interes_compuesto(principal, tasa, tiempo, frecuencia):
  monto_total = principal * (1 + (tasa / (100 * frecuencia))) ** ( frecuencia * tiempo)
  interes_compuesto = monto_total - principal
  return monto_total, interes_compuesto
principal= int(input("escribe lo que vas a invertir:"))
tiempo=  int(input("escribe por cuanto tiempo: "))
tasa= int(input("ingresa el porcentaje de interes:"))
frecuencia=int(input("ingrese la frecuencia:"))
result=calcular_interes_compuesto(principal,tasa,tiempo,frecuencia)
print (result)
### HECHO POR BASTOS_THOMAS / C.C 1091358058
