from random import randint

if __name__ == '__main__':
	mesa=True
	print("Bienvenido al juego de la guayabita, minimo 2 jugadores maximo 5")
	print("Tienes un solo lanzamiento por jugador, la apuesta minima son 10000 y tienes un 1000000 al principio")
	juego = 1
	
while juego==True:
	print("cuantos jugadores seran?")
	jugadores= int (input())
	while jugadores>=2 and jugadores<=5:
#CUANDO SON 2 JUGADORES 
		if jugadores==2:
			monto_jugador1 = 1000000
			monto_jugador2 = 1000000
			while mesa>0 or monto_jugador1>0 or monto_jugador2>0:
					print("cuanto quiere apostar el jugador1?")
					apuestajugador1 = float(input())
					print("cuanto quiere apostar el jugador2?")
					apuestajugador2 = float(input())
					mesa = apuestajugador1+apuestajugador2
					if apuestajugador1<monto_jugador1 or apuestajugador2<monto_jugador2:
							if apuestajugador1>=10000 and apuestajugador2>=10000:
									jugador=1
									print(f"turno del jugador {jugador}")
									print(f"el dado  del jugador {jugador} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador1 = monto_jugador1-apuestajugador1
										print(f"el jugador {jugador} tiene")
										print(monto_jugador1)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador1 = monto_jugador1+apuestajugador1
											print("el jugador 1 tiene")
											print(monto_jugador1)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador1 = monto_jugador1-apuestajugador1
											print("el jugador 1 tiene")
											print(monto_jugador1)
									if dado1==4 or dado1==5:
										print("pasas de turno")
										
									jugador+=1
								
									if jugador==2:
										print(f"turno del jugador {jugador}")
									print(f"el dado  del jugador {jugador} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador2 = monto_jugador2-apuestajugador2
										print(f"el jugador {jugador} tiene")
										print(monto_jugador2)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador2 = monto_jugador2+apuestajugador2
											print("el jugador 2 tiene")
											print(monto_jugador2)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador2 = monto_jugador2-apuestajugador2
											print("el jugador 2 tiene")
											print(monto_jugador2)
									if dado1==4 or dado1==5:
										print("pasas de turno") 
										
									print(f"la mesa va en {mesa} pesos")
									if monto_jugador1<=0 or monto_jugador2<=0:
										print("juego Terminado")
										break
							   

							else:
								print("El valor minimo son 10000$ tacaño :v")
					else:
							print("no se puede apostar mas de lo que tienes ")			