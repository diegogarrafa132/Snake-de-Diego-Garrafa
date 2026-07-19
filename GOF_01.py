import pygame
import random

FILAS = 20
COLUMNAS = 20
TAM_CELDA = 30

ANCHO = COLUMNAS * TAM_CELDA
ALTO = FILAS * TAM_CELDA

NEGRO = (30, 30, 30)
GRIS = (80, 80, 80)
VERDE = (0, 200, 0)
BLANCO = (255, 255, 255)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Vida")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 20)

def inicializar_aleatorio(probabilidad=0.2):
    vivas = set()
    for f in range(FILAS):
        for c in range(COLUMNAS):
            if random.random() < probabilidad:
                vivas.add((f, c))
    return vivas

def contar_vecinos(vivas, fila, columna):
    vecinos = 0
    for df in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if df == 0 and dc == 0:
                continue
            f_vecino = fila + df
            c_vecino = columna + dc
            if 0 <= f_vecino < FILAS and 0 <= c_vecino < COLUMNAS:
                if (f_vecino, c_vecino) in vivas:
                    vecinos += 1
    return vecinos

def siguiente_generacion(vivas):
    nuevas_vivas = set()
    celdas_a_revisar = set()
    for (f, c) in vivas:
        celdas_a_revisar.add((f, c))
        for df in (-1, 0, 1):
            for dc in (-1, 0, 1):
                f_aux = f + df
                c_aux = c + dc
                if 0 <= f_aux < FILAS and 0 <= c_aux < COLUMNAS:
                    celdas_a_revisar.add((f_aux, c_aux))
    
    for (f, c) in celdas_a_revisar:
        vecinos = contar_vecinos(vivas, f, c)
        viva = (f, c) in vivas
        if viva:
            if vecinos == 2 or vecinos == 3:
                nuevas_vivas.add((f, c))
        else:
            if vecinos == 3:
                nuevas_vivas.add((f, c))
    return nuevas_vivas

def dibujar_tablero(vivas, generacion, pausado):
    """Dibuja la grilla y las células vivas, además de la información."""
    pantalla.fill(NEGRO)
    
    for (f, c) in vivas:
        pygame.draw.rect(
            pantalla,
            VERDE,
            (c * TAM_CELDA + 2, f * TAM_CELDA + 2,
             TAM_CELDA - 4, TAM_CELDA - 4)
        )
    
    for f in range(FILAS + 1):
        pygame.draw.line(pantalla, GRIS, (0, f * TAM_CELDA), (ANCHO, f * TAM_CELDA))
    for c in range(COLUMNAS + 1):
        pygame.draw.line(pantalla, GRIS, (c * TAM_CELDA, 0), (c * TAM_CELDA, ALTO))
    
    texto_gen = fuente.render(f"Generación: {generacion}", True, BLANCO)
    pantalla.blit(texto_gen, (10, 10))
    estado = "PAUSADO" if pausado else "CORRIENDO"
    texto_estado = fuente.render(f"Estado: {estado}", True, BLANCO)
    pantalla.blit(texto_estado, (10, 35))
    texto_ayuda = fuente.render("Espacio: Pausa | R: Reiniciar aleatorio", True, BLANCO)
    pantalla.blit(texto_ayuda, (10, ALTO - 25))
    
    pygame.display.flip()

def main():
    vivas = inicializar_aleatorio(0.2)
    generacion = 0
    pausado = False
    ejecutando = True
    
    while ejecutando:
        reloj.tick(10)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pausado = not pausado
                elif evento.key == pygame.K_r:
                    vivas = inicializar_aleatorio(0.2)
                    generacion = 0
        
        if not pausado:
            vivas = siguiente_generacion(vivas)
            generacion += 1
        
        dibujar_tablero(vivas, generacion, pausado)
    
    pygame.quit()

main()
