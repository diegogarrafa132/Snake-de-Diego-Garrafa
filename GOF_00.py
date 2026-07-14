import pygame
import random

FILAS = 10
COLUMNAS = 10
TAM_CELDA = 50

ANCHO = COLUMNAS * TAM_CELDA
ALTO = FILAS * TAM_CELDA
pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la vida")

reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 30)

NEGRO = (30, 30, 30)
GRIS = (80, 80, 80)
VERDE = (0, 200, 0)
def vivas_iniciales():
 for i in range(5):
    while True:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if (fila, columna) not in vivas:
            return (fila, columna)
   
def celulas(celula,N_alrededores):
    if N_alredores==3 or N_alrededores==2:
       return True
    elif N_alrededores>3:
       return False 
    elif N_alrededores==1 or N_alrededores==0:
       return False 
     
     
def crear_celdas():
    pantalla.fill(NEGRO)
    for i in range(FILAS):
     for j in range(COLUMNAS):
        pygame.draw.rect(pantalla,GRIS,(j * TAM_CELDA, i * TAM_CELDA,TAM_CELDA, TAM_CELDA),1)
    pygame.display.flip()

def Imprimir(vivas):
   pantalla.fill(NEGRO)
   for i in range(FILAS):
        for j in range(COLUMNAS):

            pygame.draw.rect(
                pantalla,
                GRIS,
                (j * TAM_CELDA, i * TAM_CELDA,
                 TAM_CELDA, TAM_CELDA),
                1
            )

   for fila, col in vivas:
        pygame.draw.rect(
            pantalla,
            VERDE,
            (
                col * TAM_CELDA + 2,
                fila * TAM_CELDA + 2,
                TAM_CELDA - 4,
                TAM_CELDA - 4
            )
        )

def game():
    vivas=[]
    vivas.append(vivas_iniciales)
    ejecutando = True
    while ejecutando==True:
        reloj.tick(5)
        crear_celdas()
        Imprimir(vivas)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
    pygame.quit()

game()
