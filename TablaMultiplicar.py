#Tabla de multiplicar
def tablaMultiplicar(N):
	
	N=int(input("Dar el numero del que desea obtener la tabla de multiplicar:"))
	if(N>0):
		for I in range(1,11):
			print(N,"X",I,"=",N*I)
	else:
		print("Ingresa un valor distinto de cero")
		retun tablaMultiplicar


print("Fin")