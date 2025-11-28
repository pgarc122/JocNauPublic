import pygame
import sys
import random

# Inicialització de Pygame
pygame.init()

# --- Configuració ---
AMPLADA, ALCADA = 800, 400
FINESTRA = pygame.display.set_mode((AMPLADA, ALCADA))
pygame.display.set_caption("🚀 Esquiva els meteorits")

VELOCITAT_NAU = 5
VELOCITAT_METEORITS = 2
VELOCITAT_BALA = 5

# Colors HEXADECIMAL (RGB)
NEGRE = (10, 10, 20)
BLANC = (255, 255, 255)
BLAU = (80, 180, 255)
VERMELL = (255, 80, 80)
GRIS = (150, 150, 150)
GROC = (255,222,33)

# Rellotge
rellotge = pygame.time.Clock()
FPS = 60
frame = 0

# --- Variables del joc ---
# Creem un rectangle (x, y, amplada, alçada)
NAU_AX = 50
NAU_AY = 30
nau = pygame.Rect(100, 300, NAU_AX, NAU_AY)

METEORS_PER_FRAME = 10
meteorits = []

# Creación de estrellitas
MIDA_ESTRELLA = 3
estrelles = []

# Creem bala
bales = []
BALES_PER_FRAME = 10


# --- Bucle principal del joc ---
while True:
    # 1️⃣ Gestió d'esdeveniments (sortir del joc)
    for esdeveniment in pygame.event.get():
        if esdeveniment.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tecles = pygame.key.get_pressed()

    # 2️⃣ Actualització de variables (de moment, res a actualitzar)

    # Creem estrelles
    estrelles = []
    for i in range(0, 50):
        estrella = pygame.Rect(random.randint(0, AMPLADA),
                               random.randint(0, ALCADA),
                               MIDA_ESTRELLA,
                               MIDA_ESTRELLA)
        estrelles.append(estrella)

    # Creem els meteorits
    if frame % (100/METEORS_PER_FRAME) == 0:
        meteorit = pygame.Rect(random.randint(0, AMPLADA), -20, 20, 20)
        velocitat = random.randint(4,8)
        meteorits.append((meteorit,velocitat))

    # Moviment de la nau
    if tecles[pygame.K_RIGHT] or tecles[pygame.K_d]:
        if nau.x < AMPLADA - NAU_AX:
            nau.x += VELOCITAT_NAU

    if tecles[pygame.K_LEFT] or tecles[pygame.K_a]:
        if nau.x > 0:
            nau.x -= VELOCITAT_NAU

    # Creem bales
    if tecles[pygame.K_SPACE] and frame % BALES_PER_FRAME == 0:
        bala = pygame.Rect(nau.x + NAU_AX/2 - 2, nau.y, 5, 20)
        bales.append(bala)

    # Moviment meteorits
    for m, v in meteorits:
        m.y += v

        if m.y > ALCADA:
            meteorits.remove((m,v))

    # Moviment bala
    for b in bales:
        b.y -= VELOCITAT_BALA

    # 3️⃣ Dibuix a la pantalla
    FINESTRA.fill(NEGRE)                # Fons negre

    for estrella in estrelles:
        pygame.draw.rect(FINESTRA, GRIS, estrella)

    for b in bales:
        pygame.draw.rect(FINESTRA, GROC, b)  # Dibuixar bala

    pygame.draw.rect(FINESTRA, BLAU, nau)  # Dibuixar nau

    for m, _ in meteorits:
        pygame.draw.ellipse(FINESTRA, VERMELL, m)  # Dibuixar el rectangle
        pygame.draw.ellipse(FINESTRA, BLANC, m, width=2)  # Dibuixar el rectangle

    # 4️⃣ Actualitzar la pantalla
    pygame.display.flip()
    rellotge.tick(FPS)
    frame += 1