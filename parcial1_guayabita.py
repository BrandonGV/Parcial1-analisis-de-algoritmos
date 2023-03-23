
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
			
#CUANDO SON 3 JUGADORES	
		if jugadores==3:
					monto_jugador11 = 1000000
					monto_jugador22 = 1000000
					monto_jugador33 = 1000000
					mesa2=0
					while mesa2==0:
						print("cuanto quiere apostar el jugador1?")
						apuestajugador11 = float(input())
						print("cuanto quiere apostar el jugador2?")
						apuestajugador22 = float(input())
						print("cuanto quiere apostar el jugador 3?")
						apuestajugador33 = float(input())
						mesa2 = apuestajugador11+apuestajugador22+apuestajugador33
						if apuestajugador11<monto_jugador11 or apuestajugador22<monto_jugador22 or apuestajugador33<monto_jugador33:
							if apuestajugador11>=10000 and apuestajugador22>=10000 and apuestajugador33>=10000:
									jugador1=1
									print(f"turno del jugador {jugador1}")
									print(f"el dado  del jugador {jugador1} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador11 = monto_jugador11-apuestajugador11
										print(f"el jugador {jugador1} tiene")
										print(monto_jugador11)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador11= monto_jugador11+apuestajugador11
											print("el jugador 1 tiene")
											print(monto_jugador11)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador11 = monto_jugador11-apuestajugador11
											print("el jugador 1 tiene")
											print(monto_jugador11)
									if dado1==4 or dado1==5:
										print("pasas de turno")
										
									jugador1+=1
								
									if jugador1==2:
										print(f"turno del jugador {jugador1}")
									print(f"el dado  del jugador {jugador1} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador22 = monto_jugador22-apuestajugador22
										print(f"el jugador {jugador1} tiene")
										print(monto_jugador22)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador22 = monto_jugador22+apuestajugador22
											print("el jugador 2 tiene")
											print(monto_jugador22)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador22 = monto_jugador22-apuestajugador22
											print("el jugador 2 tiene")
											print(monto_jugador22)
									if dado1==4 or dado1==5:
										print("pasas de turno") 
										
									print(f"la mesa va en {mesa2} pesos")
									jugador1+=1
								
									if jugador1==3:
										print(f"turno del jugador {jugador1}")
									print(f"el dado  del jugador {jugador1} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador33 = monto_jugador33-apuestajugador33
										print(f"el jugador {jugador1} tiene")
										print(monto_jugador33)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador33 = monto_jugador33+apuestajugador33
											print("el jugador 3 tiene")
											print(monto_jugador33)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador33 = monto_jugador33-apuestajugador33
											print("el jugador 3 tiene")
											print(monto_jugador33)
									if dado1==4 or dado1==5:
										print("pasas de turno") 
										
									print(f"la mesa va en {mesa2} pesos")
									if monto_jugador11<=0 or monto_jugador22<=0 or monto_jugador33<=0:
										print("juego Terminado")
										break
							else:
								print("El valor minimo son 10000$ tacaño :v")
						else:
		
							print("no se puede apostar mas de lo que tienes ")			
#CUANDO 
# SON 4 JUGADORES
		if jugadores==4:
					monto_jugador111 = 1000000
					monto_jugador222 = 1000000
					monto_jugador333 = 1000000
					monto_jugador444 = 1000000
					mesa4=0
					while mesa4==0:
						print("cuanto quiere apostar el jugador1?")
						apuestajugador111 = float(input())
						print("cuanto quiere apostar el jugador2?")
						apuestajugador222 = float(input())
						print("cuanto quiere apostar el jugador 3?")
						apuestajugador333 = float(input())
						print("cuanto quiere apostar el jugador 4?")
						apuestajugador444 = float(input())
						mesa4 = apuestajugador111+apuestajugador222+apuestajugador333+apuestajugador444
						if apuestajugador111<monto_jugador111 or apuestajugador222<monto_jugador222 or apuestajugador333<monto_jugador333 or apuestajugador444<monto_jugador444:
							if apuestajugador111>=10000 and apuestajugador222>=10000 and apuestajugador333>=10000 and apuestajugador444>=10000:
									jugador11=1
									print(f"turno del jugador {jugador11}")
									print(f"el dado  del jugador {jugador11} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador111 = monto_jugador111-apuestajugador111
										print(f"el jugador {jugador11} tiene")
										print(monto_jugador111)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador111= monto_jugador111+apuestajugador111
											print("el jugador 1 tiene")
											print(monto_jugador111)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador111 = monto_jugador111-apuestajugador111
											print("el jugador 1 tiene")
											print(monto_jugador111)
									if dado1==4 or dado1==5:
										print("pasas de turno")
										
									jugador11+=1
								
									if jugador11==2:
										print(f"turno del jugador {jugador11}")
									print(f"el dado  del jugador {jugador11} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador222 = monto_jugador222-apuestajugador222
										print(f"el jugador {jugador11} tiene")
										print(monto_jugador222)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador222 = monto_jugador222+apuestajugador222
											print("el jugador 2 tiene")
											print(monto_jugador222)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador222 = monto_jugador222-apuestajugador222
											print("el jugador 2 tiene")
											print(monto_jugador222)
									if dado1==4 or dado1==5:
										print("pasas de turno") 
										
									print(f"la mesa va en {mesa4} pesos")
									jugador11+=1
								
									if jugador11==3:
										print(f"turno del jugador {jugador11}")
									print(f"el dado  del jugador {jugador11} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador333 = monto_jugador333-apuestajugador333
										print(f"el jugador {jugador11} tiene")
										print(monto_jugador333)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador333 = monto_jugador333+apuestajugador333
											print("el jugador 3 tiene")
											print(monto_jugador333)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador333 = monto_jugador333-apuestajugador333
											print("el jugador 3 tiene")
											print(monto_jugador333)
									if dado1==4 or dado1==5:
										print("pasas de turno") 

									print(f"la mesa va en {mesa4} pesos")
									jugador11+=1

									if jugador11==4:
										print(f"turno del jugador {jugador11}")
									print(f"el dado  del jugador {jugador11} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador444 = monto_jugador444-apuestajugador444
										print(f"el jugador {jugador11} tiene")
										print(monto_jugador444)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador444 = monto_jugador444+apuestajugador444
											print("el jugador 4 tiene")
											print(monto_jugador444)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador444 = monto_jugador444-apuestajugador444
											print("el jugador 4 tiene")
											print(monto_jugador444)
									if dado1==4 or dado1==5:
										print("pasas de turno") 
										
									print(f"la mesa va en {mesa4} pesos")
									if monto_jugador111<=0 or monto_jugador222<=0 or monto_jugador333<=0 or monto_jugador444<=0:
										print("juego Terminado")
										break
							else:
								print("El valor minimo son 10000$ tacaño :v")
						else:
							print("no se puede apostar mas de lo que tienes ")
	#CUANDO SON 5 JUGADORES 
		if jugadores==5:
					monto_jugador1111 = 1000000
					monto_jugador2222 = 1000000
					monto_jugador3333 = 1000000
					monto_jugador4444 = 1000000
					monto_jugador5555 = 1000000
					mesa5=0
					while mesa5==0:
						print("cuanto quiere apostar el jugador1?")
						apuestajugador1111 = float(input())
						print("cuanto quiere apostar el jugador2?")
						apuestajugador2222 = float(input())
						print("cuanto quiere apostar el jugador 3?")
						apuestajugador3333 = float(input())
						print("cuanto quiere apostar el jugador 4?")
						apuestajugador4444 = float(input())
						print("cuanto quiere apostar el jugador 5?")
						apuestajugador5555 = float(input())
						mesa5 = apuestajugador1111+apuestajugador2222+apuestajugador3333+apuestajugador4444+apuestajugador5555
						if apuestajugador1111<monto_jugador1111 or apuestajugador2222<monto_jugador2222 or apuestajugador3333<monto_jugador3333 or apuestajugador4444<monto_jugador4444 or apuestajugador5555<monto_jugador5555:
							if apuestajugador1111>=10000 and apuestajugador2222>=10000 and apuestajugador3333>=10000 and apuestajugador4444>=10000 and apuestajugador5555>=10000:
									jugador111=1
									print(f"turno del jugador {jugador111}")
									print(f"el dado  del jugador {jugador111} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador1111 = monto_jugador1111-apuestajugador1111
										print(f"el jugador {jugador111} tiene")
										print(monto_jugador1111)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador1111= monto_jugador1111+apuestajugador1111
											print("el jugador 1 tiene")
											print(monto_jugador1111)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador1111 = monto_jugador1111-apuestajugador1111
											print("el jugador 1 tiene")
											print(monto_jugador1111)
									if dado1==4 or dado1==5:
										print("pasas de turno")
										
									jugador111+=1
								
									if jugador111==2:
										print(f"turno del jugador {jugador111}")
									print(f"el dado  del jugador {jugador111} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador2222 = monto_jugador2222-apuestajugador2222
										print(f"el jugador {jugador111} tiene")
										print(monto_jugador2222)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador2222 = monto_jugador2222+apuestajugador2222
											print("el jugador 2 tiene")
											print(monto_jugador2222)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador2222 = monto_jugador2222-apuestajugador2222
											print("el jugador 2 tiene")
											print(monto_jugador2222)
									if dado1==4 or dado1==5:
										print("pasas de turno") 
										
									print(f"la mesa va en {mesa5} pesos")
									jugador111+=1
								
									if jugador111==3:
										print(f"turno del jugador {jugador111}")
									print(f"el dado  del jugador {jugador111} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador3333 = monto_jugador3333-apuestajugador3333
										print(f"el jugador {jugador111} tiene")
										print(monto_jugador3333)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador3333 = monto_jugador3333+apuestajugador3333
											print("el jugador 3 tiene")
											print(monto_jugador3333)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador3333 = monto_jugador3333-apuestajugador3333
											print("el jugador 3 tiene")
											print(monto_jugador3333)
									if dado1==4 or dado1==5:
										print("pasas de turno") 

									print(f"la mesa va en {mesa5} pesos")
									jugador111+=1

									if jugador111==4:
										print(f"turno del jugador {jugador111}")
									print(f"el dado  del jugador {jugador111} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador4444 = monto_jugador4444-apuestajugador4444
										print(f"el jugador {jugador111} tiene")
										print(monto_jugador4444)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador4444 = monto_jugador4444+apuestajugador4444
											print("el jugador 4 tiene")
											print(monto_jugador4444)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador4444 = monto_jugador4444-apuestajugador4444
											print("el jugador 4 tiene")
											print(monto_jugador4444)
									if dado1==4 or dado1==5:
										print("pasas de turno") 

									print(f"la mesa va en {mesa5} pesos")
									jugador111+=1
								
									if jugador111==5:
										print(f"turno del jugador {jugador111}")
									print(f"el dado  del jugador {jugador111} es")
									dado1 = randint(0,5)+1
									print(dado1)
									if dado1==1 or dado1==6:
										print("perdiste ,deja el monto en la mesa")
										monto_jugador5555 = monto_jugador5555-apuestajugador5555
										print(f"el jugador {jugador111} tiene")
										print(monto_jugador5555)
									if dado1==2 or dado1==3:
										print("Vuelve a tirar el dado")
										dado2 = randint(0,5)+1
										print("el dado saco")
										print(dado2)
										if dado2>dado1:
											print("felicidades sumas lo apostado")
											monto_jugador5555 = monto_jugador5555+apuestajugador5555
											print("el jugador 5 tiene")
											print(monto_jugador5555)
										else:
											print("perdiste ,deja el monto en la mesa")
											monto_jugador5555 = monto_jugador5555-apuestajugador5555
											print("el jugador 5 tiene")
											print(monto_jugador5555)
									if dado1==4 or dado1==5:
										print("pasas de turno") 

									print(f"la mesa va en {mesa5} pesos")
									
									
									if monto_jugador1111<=0 or monto_jugador2222<=0 or monto_jugador3333<=0 or monto_jugador4444<=0 or monto_jugador5555<=0:
										print("juego Terminado")
										break
							else:
								print("El valor minimo son 10000$ tacaño :v")
						else:
							print("no se puede apostar mas de lo que tienes ")	
	print("NUMERO DE PARTICIPANTES INVALIDO")
							

