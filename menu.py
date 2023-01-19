import pygame
import principal
import granjero
import tamaño
import sys
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
                        principal.jugar()
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