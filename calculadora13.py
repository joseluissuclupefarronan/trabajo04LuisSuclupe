#calculadora N°13
#esta calculadora calcula el tiempo de alcance entre dos moviles.

#declaracion de las variables
velocidad2,distacia,velocidad1,tiempo_alcance=0.0,0.0,0.0,0.0

#calculadora
velocidad1=20
velocidad2=10
distacia=120
tiempo_alcance=(distacia)/(velocidad1-velocidad2)

#mostrar datos
print("la velocidad 1 es=", str(velocidad1) + " mtr/s")
print("la velocidad 2 es=", str(velocidad2)+ " mtr/s")
print("la distancia es=",str(distacia) + " metros")
print("el tiempo de alcance es en=", str(tiempo_alcance) + " minutos")
