import pygame
import random

FILAS = 10
COLUMNAS = 10
TAM_CELDA = 50

ANCHO = COLUMNAS * TAM_CELDA
ALTO = FILAS * TAM_CELDA

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake")

reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 30)

NEGRO = (30, 30, 30)
GRIS = (80, 80, 80)
VERDE = (0, 200, 0)
ROJO = (220, 30, 30)
BLANCO = (255, 255, 255)

def crear_manzana(serpiente):
    while True:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)

        if (fila, columna) not in serpiente:
            return (fila, columna)


def mover_serpiente(serpiente, direccion, crecer):

    cabeza_fila, cabeza_col = serpiente[-1]

    if direccion == "d":
        nueva = (cabeza_fila, cabeza_col + 1)

    elif direccion == "a":
        nueva = (cabeza_fila, cabeza_col - 1)

    elif direccion == "w":
        nueva = (cabeza_fila - 1, cabeza_col)

    elif direccion == "s":
        nueva = (cabeza_fila + 1, cabeza_col)

    nueva_serpiente = serpiente[:]
    nueva_serpiente.append(nueva)

    if not crecer:
        nueva_serpiente.pop(0)

    return nueva_serpiente


def colision(serpiente):

    cabeza = serpiente[-1]
    fila, col = cabeza

    if fila < 0 or fila >= FILAS:
        return True

    if col < 0 or col >= COLUMNAS:
        return True

    if cabeza in serpiente[:-1]:
        return True

    return False


def dibujar(serpiente, manzana, puntuacion):
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

    for fila, col in serpiente:

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
        
    pygame.draw.circle(
        pantalla,
        ROJO,
        (
            manzana[1] * TAM_CELDA + TAM_CELDA // 2,
            manzana[0] * TAM_CELDA + TAM_CELDA // 2
        ),
        TAM_CELDA // 3
    )

    texto = fuente.render(f"Puntos: {puntuacion}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()

def game():
    serpiente = [(0, 0), (0, 1)]
    direccion = "d"
    puntuacion = 0
    manzana = crear_manzana(serpiente)
    ejecutando = True
    while ejecutando==True:
        reloj.tick(5)
        tecla = None
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    tecla = "w"
                elif evento.key == pygame.K_s:
                    tecla = "s"
                elif evento.key == pygame.K_a:
                    tecla = "a"
                elif evento.key == pygame.K_d:
                    tecla = "d"
                elif evento.key == pygame.K_q:
                    ejecutando = False
        opuestas = {
            "w": "s",
            "s": "w",
            "a": "d",
            "d": "a"
        }

        if tecla in opuestas and opuestas[tecla] != direccion:
            direccion = tecla
        cabeza = serpiente[-1]
        if direccion == "d":
            nueva = (cabeza[0], cabeza[1] + 1)
        elif direccion == "a":
            nueva = (cabeza[0], cabeza[1] - 1)
        elif direccion == "w":
            nueva = (cabeza[0] - 1, cabeza[1])
        elif direccion == "s":
            nueva = (cabeza[0] + 1, cabeza[1])

        come = nueva == manzana
        serpiente = mover_serpiente(serpiente, direccion, come)
        if colision(serpiente):
            break
        if come:
            puntuacion += 1
            manzana = crear_manzana(serpiente)
        dibujar(serpiente, manzana, puntuacion)
    print("GAME OVER")
    print("Puntuación:", puntuacion)
    pygame.quit()
game()
