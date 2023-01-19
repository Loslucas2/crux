import pygame
import tamaño

import random
class Enemigo1:
    def __init__(self):
        self.imagen = pygame.image.load("juegos/imagenes/Caballo1.png")
        self.sprites = []
        self.recortar_sprites()
        self.sprite_actual = 0
        self.rect = pygame.Rect(random.randint(10, 1200), random.randint(10, 600), 38,160)
        self.direccion = "abajo"
        
    def recortar_sprites(self):

        #Cargar imagen con los sprites
        sprites_image = pygame.image.load("juegos/imagenes/Caballo1.png")
        sprite_caballo_abajo1 = sprites_image.subsurface(pygame.Rect(32, 0, 38, 160))
        sprite_caballo_abajo2 = sprites_image.subsurface(pygame.Rect(139, 0, 38, 160))
        sprite_caballo_abajo3 = sprites_image.subsurface(pygame.Rect(248, 0, 38, 160)) 
        ##sprite_caballo_abajo4 = sprites_image.subsurface(pygame.Rect(350, 0, 38, 160))
        
       

        
        
        
        sprite_izquierda1 = sprites_image.subsurface(pygame.Rect(0, 44, 30, 43))
        sprite_izquierda2 = sprites_image.subsurface(pygame.Rect(41, 44, 30, 43))
        sprite_izquierda3 = sprites_image.subsurface(pygame.Rect(86, 44, 30, 43))
        sprite_izquierda4 = sprites_image.subsurface(pygame.Rect(133, 44, 30, 43))
        

        sprite_derecha1 = sprites_image.subsurface(pygame.Rect(0, 86, 30, 43))
        sprite_derecha2 = sprites_image.subsurface(pygame.Rect(41, 86, 30, 43))
        sprite_derecha3 = sprites_image.subsurface(pygame.Rect(86, 86, 30, 43))
        sprite_derecha4 = sprites_image.subsurface(pygame.Rect(133, 86, 30, 43))
        

        

        #Obtener sub-superficie del primer sprite (caminando hacia arriba)
        sprite_caballo_arriba1 = sprites_image.subsurface(pygame.Rect(0,129 ,30, 43))
        sprite_caballo_arriba2 = sprites_image.subsurface(pygame.Rect(41, 129, 30, 43))
        sprite_caballo_arriba3 = sprites_image.subsurface(pygame.Rect(86.21, 129, 30, 43))
        sprite_caballo_arriba4 = sprites_image.subsurface(pygame.Rect(133, 129, 30, 43))
        

        self.sprites.append(sprite_caballo_arriba1)
        self.sprites.append(sprite_caballo_arriba2)
        self.sprites.append(sprite_caballo_arriba3)
        self.sprites.append(sprite_caballo_arriba4)
   
        self.sprites.append(sprite_derecha1)
        self.sprites.append(sprite_derecha2)
        self.sprites.append(sprite_derecha3)
        self.sprites.append(sprite_derecha4)
       
        self.sprites.append(sprite_izquierda1)
        self.sprites.append(sprite_izquierda2)
        self.sprites.append(sprite_izquierda3)
        self.sprites.append(sprite_izquierda4)
        
        self.sprites.append(sprite_caballo_abajo1)
        self.sprites.append(sprite_caballo_abajo2)
        self.sprites.append(sprite_caballo_abajo3)
        #self.sprites.append(sprite_caballo_abajo4)

    
    
    def movimiento_aleatorio(self):
        direccion_aleatoria = random.randint(1, 4)
        if direccion_aleatoria == 1:
            self.rect.x += 5 # se mueve hacia la derecha
        elif direccion_aleatoria == 2:
            self.rect.x -= 5 # se mueve hacia la izquierda
        elif direccion_aleatoria == 3:
            self.rect.y += 5 # se mueve hacia abajo
        elif direccion_aleatoria == 4:
            self.rect.y -= 5 # se mueve hacia arriba
    def dibujar(self):
        tamaño.ventana.blit(self.sprites[self.sprite_actual], self.rect)  


    def update(self):
        self.sprite_actual += 1
        if self.sprite_actual >= len(self.sprites):
            self.sprite_actual = 0
            tamaño.ventana.blit(self.sprites[self.sprite_actual], (self.x, self.y))
    def colision(self, granjero):
        if self.rect.colliderect(granjero.rect):
            print("Colision detectada")
