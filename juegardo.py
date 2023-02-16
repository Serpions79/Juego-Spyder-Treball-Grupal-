import random

class Personaje:
    nombre=""
    vida=15
    ataque_actual=0
    defensa_actual=0
    objetos=[]
    def __init__(self,nombre,vida,ataque_actual,defensa_actual,objetos):
        self.nombre = nombre
        self.vida = vida
        self.ataque_actual = ataque_actual
        self.defensa_actual = defensa_actual
        self.objetos = objetos
    def buscarObjeto(self,nombre):
        encontrado=0
        i=0
        while i<len(self.objetos) and encontrado==0:
            if self.objetos[i].nombre ==nombre:
                encontrado=1
            else:
                i=i+1
        if encontrado==1:
            return 1
        else:
            return 0

class Objeto:
    ataque=0
    defensa=0
    resistencia=0
    def __init__(self,nombre,ataque,defensa,resistencia,valor):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.resistencia = resistencia
        self.valor = valor
class Enemigo:
    nombre=""
    vida=0
    ataque=0
    defensa=0
    def __init__(self,nombre,vida,ataque,defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
def Combate(personaje,enemigos):
   turno_player = 0
   num_enemigos = 0
   if turno_player == 0:
       while num_enemigos < len(enemigos):
           if enemigos[num_enemigos] > personaje.defensa_actual:
               resultado = - personaje.defensa_actual + enemigos[num_enemigos].ataque
               personaje.vida = personaje.vida - resultado
               print(enemigos[num_enemigos].nombre + "Te ha atacado y te ha hecho " + resultado + " de daño.")
           else:
               print("No te ha hecho daño") 
monedero=Objeto("monedero",0,0,0,11)

enemigos=[]

player=Personaje("",100,0,0,[])

print("Bienvenido a caminos distintos donde tendras que escoger tu propio camino segun que opciones escogas")
print("Empezaremos con algo sencillo ")
print("Elige 1 o 2 ")
decision=int(input())
if decision==1:
    print("Has escogido el numero 1 apareceras en una selva" )
elif decision==2:
     print("Has escogido el numero 2 apareceras en un desierto")
print("Vaya has aparecido en este bioma peculiar ten te puedo dar 3 objetos pero solo puedes escoger 1 para sobrevivir ")
print("Si quieres una cuerda escoge 1 si quieres una bengala escoge 2 si quieres un machete escoge 3")
decision=int(input())
if  decision==1:
    print("Has escogido la cuerda buena eleccion ")
    player.objetos.append(Objeto("Cuerda",1,0,6,5))
elif decision==2:
     print("Has escogido la bengala magnifica idea ") 
     player.objetos.append(Objeto("Bengala",2,0,5,7))
elif decision==3:
     print("Has escogido el machete, si te soy sincero yo tambien lo habria escogido")
     player.objetos.append(Objeto("Machete",6,0,5,4))
print("Ahora que ya estamos listos vamonos")
print("4 HORAS DESPUES")
print("Ya se esta haciendo de noche. Vaya mira lo que veo es una cabanya de madera a tu derecha pero veo una cueva tambien a tu izquierda ")
print("Escoge 1 para pasar la noche en la cabanya o escoge 2 para pasar la noche en la cueva")
decision=int(input())
if decision==1:
   print("Has escogido la cabanya me parece correcto ")
elif decision==2:
     print("Has escogido la cueva buena eleccion ")
print("HAS PASADO LA 1r NOCHE FIN DE LA PARTIDA")
print("SI TE QUEDASTE CON GANAS DE MAS PODRAS JUGAR LA SEGUNDA PARTE DENTRO DE 1 ANYO")
print("INSERTAR MUSICA DE VIDEOJUEGOS")
print("Oh vaya estas aqui aun")
print("Bueno te dejo jugar la segunda parte")
print("MUSICA DE ACCION")
numerorandom=random.uniform(0,100)

if 30>=numerorandom:
    enemigos.append(Enemigo("Lobo",5,6,4))
    print("Oh no te estan persiguiendo unos lobos salvajes y es de noche")
    
    if player.buscarObjeto("Bengala")==1:
        print("Teniendo la bengala puedes utilizarla, Quieres utilizarla ahora? 1 si 2 no") 
        decision=int(input())
        if decision==1:
           print("Has utilizado la bengala y los lobos se han ido")
           
        elif decision==2:
            print("Como no has utilizado la Bengala PREPARATE PARA COMBATIR")
            enemigos.append(Enemigo("Lobo",5,6,4))
    else:
        print("Como no puedes hacer nada los lobos te han dejado a media vida PREPARATE POR QUE LA VAS A PASAR MAL")
        print("EMPIEZA EL COMBATE")
print("Ya llevas 3 horas y aun no has comido pero mira lo que veo es un ciervo")
if player.buscarObjeto("Machete")==1:
    print("Puedes utilizar el machete para comer el ciervo (1) o puedes seguir caminando y buscar otra comida (2)")
    decision=int(input())
    if decision==1:
        print("Has utilizado el Machete... pero el ciervo a escapado")
    elif decision==2:
        print("Bien hecho, como podrias matar a un ciervo tu solo con un machete?")
else:
    print("No tienes un machete para cazarlo, ya sera la proxima vez")
print("Mira has encontrado otra casa abandonada")
print("Quieres ir a investigar esa casa?")
print("1 SI 2 NO")
decision=int(input())
if decision==1:
    print("Has entrado a la casa y mira habia un monton de comida toda esta comida nos bastara para 1 semana")
elif decision==2:
    print("Mejor no entraremos a esa casa pero parece oler bastante bien seguro que no quieres entrar a la casa? Pon 1 si al final quieres ir o pon 2 si no quieres ir")
    decision=int(input())
    if decision==1:
        print("Has entrado a la casa y mira habia un monton de comida toda esta comida nos bastara para 1 semana")
    elif decision==2:
        print("Ok no iremos a la casa abandonada")
        
print("Hola, David malo")

print("Vaya mira un pozo pero que hara un pozo por estas tierras?")
print("Para ir a mirar el pozo pulsa 1 para pasar del pozo pulsa 2")
decision=int(input())
if decision==1:
    print("Mira que precioso es el pozo oye te acuerdas cuando la gente tiraba monedas a un pozo para cumplir un deseo")
    print("Pulsa 1 para tirar un deseo o pulsa 2 para no hacer nada")
    decision=int(input())
    if decision==1:
        print("Tiraste la moneda pero que esta pasando?")
        print("Parece como si hubiera un tornado rapido ve a esa cueva para ponernos a salvo pero pareze que el pozo comienza a hacer cosas raras")
        print("escoge 1 para ponerte a salvo escoge 2 para mirar lo que pasa en ese pozo")
        decision=int(input())
        if decision==1:
            print("Aqui estamos sanos y salvos")
            print("Escuche un ruido extranyo, ¿quieres ir a investigar que es eso?")
            print("1 para investigar 2 para permanezer quieto")
            decision=int(input())
            if decision==1:
                print("No me lo puedo creer es un Pikachu pero esto no tiene sentido esas cosas no son reales")
                print("FIN DE LA PARTE 2")
                print("Parece que pikachu te esta guiando a lo mas profundo de la cueva")
                print("1 para seguir 2 para no seguir")
                decision=int(input())
                if decision==1:
                    print("Ves una especie de rectangulo lleno de luz y ves como pikachu entra a esa cosa")
                    print("1 para ir a esa especie de rectangulo lleno de luz 2 para quedarte en la cueva y esperar a que pase el tornado")
                    decision=int(input())
                    if decision==1:
                        print("Entras y ves una especie de campo lleno de...POKEMONS")
                        print("Ves a una persona a la lejos que se esta acercando")
                        print("1 para quedarte a esperarlo 2 para huir")
                        decision=int(input())
                        if decision==1:
                            print("Esa persona resulta ser un señor de unos 50 años y quiere que te quedes a dormir a su casa")
                            print("Señor: Por la noche este lugar es muy peligroso puedes quedarte a dormir esta noche en mi hogar sin problemas")
                            print("1 para aceptar 2 para rechazar")
                            decision=int(input())
                            if decision==1:
                                print("Aceptas y entraste a su casa")
                                print("Resulta que su casa esta llena de objetos extraños")
                                print("Señor: Mi nombre es OAK")
                                print("FIN DE LA 3R PARTE")
                            elif decision==2:
                                print("Corres a toda velocidad y entras en un bosque")
                                print("En ese bosque ves que hay 2 caminos")
                                print("1 izquierda 2 derecha")
                                decision=int(input())
                                if decision==1:
                                   print("Ves una especie de figura extraña y va hacia ti")
                                   print("1 quedarte quieto 2 huir")
                                   decision=int(input())
                                   if decision==1:
                                       print("Es pikachu y te ha traido una baya")
                                       print("Y el señor de antes estaba detras tuyo y te deice que el es OAK EL PROFESOR POKEMON")
                                       print("FIN DE LA 3r PARTE")
                                   elif decision==2:
                                       print("Huiste por un camino un tanto extraño")
                    elif decision==2:
                        print("Te quedas en la cueva y escuchas un rugido")
                        print("Es un CHARIZARD")
                        print("1 para huir 2 para quedarte quieto")
                        decision=int(input())
                        if decision==1:
                            print("1 para esconder 2 para correr")
                            decision=int(input())
                            if decision==1:
                                print("Te escondes y el CHARIZARD se ha ido")
                            elif decision==2:
                                print("El CHARIZARD es mas rapido y te mata")
                        elif decision==2:
                            print("CHARIZARD se te queda mirando fijamente y decide no hacerte nada y se va")
                            print("CHARIZARD parece que tiene una especie de chip en la cabeza")
                            print("Fuiste a la salida de esa cueva y ves que el tornado se fue")
                            print("Al parecer CHARIZARD te sigue")
                            print("1 dejarle que te siga 2 decirle que se vaya")
                            decision=int(input())
                            if decision==1:
                                print("CHARIZARD se siente feliz")
                                print("FIN DE LA PARTE 3")
                            elif decision==2:
                                print("CHARIZARD se enfada y te mata")
                                print("Fuiste la comida para CHARIZARD fin de la partida")
            elif decision==2:
                print("Pareze que ya se fue el tornado")
                print("Que raro el pozo a desaparecido me pregunto que habra pasado")
                print("FIN DE LA PARTE 2")
                print("Hay una luz al final de este camino que brilla demasiado")
                print("DAVID CONTINUA")
        elif decision==2:
            print("Voz extraña: Ayudanos necesitamos tu ayuda")
            print("Voz extraña: Necesito que te tires al pozo")
            print("Escoge 1 para tirarte al pozo o escoge 2 para mejor ir a la cueva")
            decision=int(input())
            if decision==1:
                print("TE HAS TIRADO AL POZO")
                print("Puedes observar como la oscuridad de la parte profunda del pozo poco a poco se esta haciendo mas clara")
                print("FIN DE LA PARTE 2")
                print("David continua")
            elif decision==2:
                print("Corres como puedes hacia la cueva pero el tornado te pillo")
                print("HAS MUERTO")
                print("Puedes volver a intentarlo y no morir en el intento")
    elif decision==2:
        print("Sigues tu camino como si nada")
        print("Y escuchas un ruido extraño")
        print("*Se da la vuelta y observa que no esta el pozo mas*")
        print("Que raro")
        print("Oyes eso es un ruido en esos arbustos")
        print("Parecen peligrosos pero ¿valdra la pena mirar que es?")
        print("Pulsa 1 para mirar que es o pulsa 2 para no arriesgarte")
        decision=int(input())
        if decision==1:
            print("Es un Charmander pero eso no era un Pokemon")
            print("¿Que hace esta cosa aqui acaso no era un videojuego?")
            print("FIN DE LA PARTE 2")
            print("DAVID CONTINUA")
        elif decision==2:
            print("Que acaba de pasar HAY UN MURO DE FUEGO DELANTE")
            print("FIN DE LA PARTE 2")
            print("David continua")
elif decision==2:
    print("Te das cuenta que el pozo desaparecio magicamente")
    print("FIN DE LA PARTE 2")
    print("David continua")




"""
RULETA DE LA SUERTE :)
Buscar una funcion que nos de un numero aleatorio del 1 al 100 (solo en el caso de utilizar porcentajes) 
Ejemplo: Que pase un 30% de probabilidad de que ocurra cierta acción
Cada vez que sea de noche alla un 30% de que alla lobos 
Si el numero aleatorio es menor o igual a 30 pues te aparece lo de los lobos o si no continua la historia 


MEJORAR LA CLASE OBJETO (Hacer que el objeto sea equipable o no) Separar el objeto que tienes equipado con los de la bolsa de objetos
Y añadir tipos en los objetos 
añadir la clase enemigo (Nombre, vida, ataque, defensa,)
Añadir una clase jugador para añadir a nosotros (Ayuda)

Hacer el turno del jugador, que tenga 2 opciones si es luchar es lo mismo que el enemigo pero saber a que enemigo hacerle daño, o la otra opcion que es huir.

"""
