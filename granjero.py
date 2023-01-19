import pygame
import tamaño
class Granjero:
    def __init__(self):
        self.imagen = pygame.image.load("juegos/imagenes/granjero.png")
        self.sprites = []
        self.recortar_sprites()
        self.sprite_actual = 0
        self.rect = pygame.Rect(5, 120, 30, 43)
        self.direccion = "abajo"
        
    def recortar_sprites(self):
        #Cargar imagen con los sprites
        sprites_image = pygame.image.load("juegos/imagenes/granjero.png")

        #Obtener sub-superficie del primer sprite (caminando hacia arriba)
        sprite_arriba1 = sprites_image.subsurface(pygame.Rect(0,129 ,30, 43))
        sprite_arriba2 = sprites_image.subsurface(pygame.Rect(41, 129, 30, 43))
        sprite_arriba3 = sprites_image.subsurface(pygame.Rect(86.21, 129, 30, 43))
        sprite_arriba4 = sprites_image.subsurface(pygame.Rect(133, 129, 30, 43))
        #sprite_arriba5 = sprites_image.subsurface(pygame.Rect(174, 129, 30, 43))
        #sprite_arriba6 = sprites_image.subsurface(pygame.Rect(220, 129, 30, 43))
        #Obtener sub-superficie del segundo sprite (caminando hacia arriba)
        sprite_derecha1 = sprites_image.subsurface(pygame.Rect(0, 86, 30, 43))
        sprite_derecha2 = sprites_image.subsurface(pygame.Rect(41, 86, 30, 43))
        sprite_derecha3 = sprites_image.subsurface(pygame.Rect(86, 86, 30, 43))
        sprite_derecha4 = sprites_image.subsurface(pygame.Rect(133, 86, 30, 43))
        #sprite_derecha5 = sprites_image.subsurface(pygame.Rect(174, 86, 30, 43))
        #sprite_derecha6 = sprites_image.subsurface(pygame.Rect(220, 86, 30, 43))
        
        sprite_izquierda1 = sprites_image.subsurface(pygame.Rect(0, 44, 30, 43))
        sprite_izquierda2 = sprites_image.subsurface(pygame.Rect(41, 44, 30, 43))
        sprite_izquierda3 = sprites_image.subsurface(pygame.Rect(86, 44, 30, 43))
        sprite_izquierda4 = sprites_image.subsurface(pygame.Rect(133, 44, 30, 43))
        #sprite_izquierda5 = sprites_image.subsurface(pygame.Rect(174, 44, 30, 43))
        #sprite_izquierda6 = sprites_image.subsurface(pygame.Rect(220, 44, 30, 43))

        sprite_abajo1 = sprites_image.subsurface(pygame.Rect(0, 0, 30, 43))
        sprite_abajo2 = sprites_image.subsurface(pygame.Rect(41, 0, 30, 43)) 
        sprite_abajo3 = sprites_image.subsurface(pygame.Rect(86, 0, 30, 43))
        sprite_abajo4 = sprites_image.subsurface(pygame.Rect(133, 0, 30, 43))
        #sprite_abajo5 = sprites_image.subsurface(pygame.Rect(174, 0, 30, 43))
        #sprite_abajo6 = sprites_image.subsurface(pygame.Rect(220, 0, 30, 43))

        self.sprites.append(sprite_arriba1)
        self.sprites.append(sprite_arriba2)
        self.sprites.append(sprite_arriba3)
        self.sprites.append(sprite_arriba4)
        #self.sprites.append(sprite_arriba5)
        #self.sprites.append(sprite_arriba6)
        self.sprites.append(sprite_derecha1)
        self.sprites.append(sprite_derecha2)
        self.sprites.append(sprite_derecha3)
        self.sprites.append(sprite_derecha4)
        #self.sprites.append(sprite_derecha5)
        #self.sprites.append(sprite_derecha6)
        self.sprites.append(sprite_izquierda1)
        self.sprites.append(sprite_izquierda2)
        self.sprites.append(sprite_izquierda3)
        self.sprites.append(sprite_izquierda4)
        #self.sprites.append(sprite_izquierda5)
        #self.sprites.append(sprite_izquierda6)
        self.sprites.append(sprite_abajo1)
        self.sprites.append(sprite_abajo2)
        self.sprites.append(sprite_abajo3)
        self.sprites.append(sprite_abajo4)
        #self.sprites.append(sprite_abajo5)
        #self.sprites.append(sprite_abajo6)
    def dibujar(self):
        tamaño.ventana.blit(self.sprites[self.sprite_actual], self.rect)

    def update(self):
        self.sprite_actual += 1
        if self.sprite_actual >= len(self.sprites):
            self.sprite_actual = 0
            tamaño.ventana.blit(self.sprites[self.sprite_actual], (self.x, self.y))
