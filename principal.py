import pygame
import random
import sys
import tamaño
from granjero import Granjero
from Enemigo import Enemigo1


pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Tu hermana 1")
def menu():
    pygame.mixer.music.load("juegos/musica/hola1.mp3")
    fondonivel = pygame.image.load("juegos/imagenes/fondomenu.jpg")

    # Reproducir música del menú en loop
    pygame.mixer.music.play(loops=-1)

    
    opcion = 1
    fuente = pygame.font.Font(None, 30)
    

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    opcion -= 1
                elif event.key == pygame.K_DOWN:
                    opcion += 1
                elif event.key == pygame.K_RETURN:
                    if opcion == 1:
                        # Iniciar juego
                        jugar()
                    elif opcion == 2:
                        # Mostrar opciones
                        creditos()
                    elif opcion == 3:
                        # Salir del juego
                        pygame.quit()
                        sys.exit()
        tamaño.ventana.blit(fondonivel,(0,0))
        opciones = ["Iniciar juego", "creditos", "Salir"]
        y = 50
        for i, texto in enumerate(opciones):
            if i + 1 == opcion:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)
            opcion_texto = fuente.render(texto, 1, color)
            text_rect = opcion_texto.get_rect()
            text_rect.center = ((tamaño.Ancho / 2), (tamaño.Altura / 2)+y)
            tamaño.ventana.blit(opcion_texto, text_rect)
            y +=50
        
        pygame.display.update()
        pygame.display.flip()
        



def jugar():
   
    granjero = Granjero()
    enemigo = Enemigo1()
    
    fondojuego = pygame.image.load("juegos/imagenes/fondonivel.jpg")
    tamaño.ventana.blit(fondojuego,(0,0))
    tamaño.ventana.blit(granjero.sprites[granjero.sprite_actual], granjero.rect)
    pygame.mixer.music.load("juegos/musica/bebe.ogg")
    pygame.mixer.music.play(loops=-1)

    pygame.mixer.music.play()
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 30)


    while True:
        
        enemigo.movimiento_aleatorio()
        reloj.tick(30) # 30 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "w":
                    granjero.rect.y -= 5+velocidad_y
                    granjero.cambiar_animacion("arriba")
                    
                elif event.unicode == "s":
                    granjero.rect.y += 5+velocidad_y
                    granjero.cambiar_animacion("abajo")
                    
                elif event.unicode == "a":
                    granjero.rect.x -= 5+velocidad_x
                    granjero.cambiar_animacion("izquierda")
                   
                elif event.unicode == "d":
                    granjero.rect.x += 5+velocidad_x
                    granjero.cambiar_animacion("derecha")
            enemigo.movimiento_aleatorio()
            granjero.dibujar(tamaño.ventana) #Aqui es donde se llama a la funcion dibujar del granjero
            pygame.display.update()
            reloj.tick(60)
        if granjero.left < 0 or granjero.right > 1200:
            velocidad_x = -velocidad_x
        if granjero.top < 20 or granjero.bottom > 600:
            velocidad_y = -velocidad_y
        if enemigo.left < 0 or enemigo.right > 1200:
            velocidad_x_enemigo = -velocidad_x_enemigo
        if enemigo.top < 20 or enemigo.bottom > 600:
            velocidad_y_enemigo = -velocidad_y_enemigo  
        enemigo.x += velocidad_x_enemigo
        enemigo.y += velocidad_y_enemigo
        
        if granjero.rect.colliderect(enemigo.rect):
            granjero.vida -= 1
            enemigo.rect.x = random.randint(10, 1200)
            enemigo.rect.y = random.randint(10, 600)

       
        if granjero.vida == 0:
            pygame.mixer.music.stop()
            Gameover()
        

        tamaño.ventana.blit(fondojuego, (0, 0))
        tamaño.ventana.blit(granjero.sprites[granjero.sprite_actual], granjero.rect)
        tamaño.ventana.blit(enemigo.sprites[enemigo.sprite_actual], enemigo.rect)

        #tamaño.ventana.blit(puntos_texto, (10, 10))
        tamaño.ventana.blit(vida_texto, (200, 10))
        pygame.display.flip()
        pygame.display.update()
        

       


        ###puntos_texto = fuente.render("Puntos: " + str(puntos), 1, (255, 255, 255))
        vida_texto= fuente.render("Vida:"  +str(granjero.vida),1,(255, 255, 255) )
        #tamaño.ventana.blit(puntos_texto, (10, 10))
        tamaño.ventana.blit(vida_texto, (200, 10))
        pygame.display.flip()
        pygame.display.update()

        reloj.tick(130)
        

def creditos():
        # Aquí puedes crear una variable con el texto de los créditos
    creditos_texto = "Créditos: Juego desarrollado por: Tu hermana, hola mama"
    # Crea una variable con la fuente a utilizar
    fuente = pygame.font.Font(None, 20)
    # Renderiza el texto en la pantalla
    creditos_renderizado = fuente.render(creditos_texto, 1, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # si se presiona la tecla esc, volvemos al menu
                    return
        tamaño.ventana.fill((0, 0, 0))
        tamaño.ventana.blit(creditos_renderizado, (50, 50))
        pygame.display.update()
def Gameover():
    pygame.mixer.music.load("juegos/musica/perdiste.ogg")
    pygame.mixer.music.play(loops=-1)
    perdedor_texto = "Perdiste,perdedor,patetico"
    # Crea una variable con la fuente a utilizar
    fuente = pygame.font.Font(None, 20)
    # Renderiza el texto en la pantalla
    creditos_renderizado = fuente.render(perdedor_texto, 1, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # si se presiona la tecla esc, volvemos al menu
                    menu()
        tamaño.ventana.fill((0, 0, 0))
        tamaño.ventana.blit(creditos_renderizado, (50, 50))
        pygame.display.update()
    
menu()


