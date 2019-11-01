#calculadora N°02
#esta calculadora calcula la aceleracion media de un movil.

#declaracion de las variables
velocidad1,velocidad2,tiempo,aceleracion_media=0.0,0.0,0.0,0.0

#calculadora
velocidad2=132
velocidad1=60
tiempo=6
aceleracion_media=((velocidad2-velocidad1)/tiempo)

#mostrar datos
print("la velocidad 1 es="+ str(velocidad1) + " km/h")
print("la velocidad 2 es="+ str(velocidad2) + " km/h")
print("el tiempo es=", str(tiempo) + " minutos")
print("La aceleracion media es:"+ str(aceleracion_media) + " km/h")
