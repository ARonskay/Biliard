import pygame
import math

pygame.init()
win = pygame.display.set_mode((310, 480))
pygame.display.set_caption("Bilard")

# Tworzenie pustych list, zmiennych odpowiadających za kulki

rB = []  # promień piłek
xB = []  # współrzędna X środków piłek
yB = []  # współrzędna Y środków piłek
aB = []  # kierunek ruchu kulki (od osi X zgodnie z ruchem wskazówek zegara)
vB = []  # prędkość
mB = []  # masa
cB = []  # kolor
n = 22  # liczba piłek

# Napełnianie list wartościami

for i in range(n + 1):
    rB.append(7)
    xB.append(0)
    yB.append(0)
    aB.append(i * math.pi / 3)
    vB.append(0.0000005)
    cB.append(0)
    mB.append(rB[i] ** 2)

cB[1] = "yellow"
cB[2] = "blue"
cB[3] = "red"
cB[4] = "pink"
cB[5] = "orange"
cB[6] = "yellow"
cB[7] = "brown"
cB[8] = "black"
cB[9] = "green"
cB[10] = "blue"
cB[11] = "red"
cB[12] = "pink"
cB[13] = "orange"
cB[14] = "green"
cB[15] = "brown"

cB[16] = "white"

xB[1] = 150

xB[2] = 142
xB[3] = 158

xB[4] = 134
xB[5] = 150
xB[6] = 166

xB[7] = 126
xB[8] = 142
xB[9] = 158
xB[10] = 174

xB[11] = 118
xB[12] = 134
xB[13] = 150
xB[14] = 166
xB[15] = 182

xB[16] = 150

xB[17] = 41
xB[18] = 270
xB[19] = 46
xB[20] = 264
xB[21] = 46
xB[22] = 264

yB[1] = 164

yB[2] = 148
yB[3] = 148

yB[4] = 132
yB[5] = 132
yB[6] = 132

yB[7] = 116
yB[8] = 116
yB[9] = 116
yB[10] = 116

yB[11] = 100
yB[12] = 100
yB[13] = 100
yB[14] = 100
yB[15] = 100

yB[16] = 300

yB[17] = 240
yB[18] = 240
yB[19] = 46
yB[20] = 46
yB[21] = 434
yB[22] = 434

vB[16] = 2.5
aB[16] = (-math.pi / 2)

vB[17] = 0
vB[18] = 0
vB[19] = 0
vB[20] = 0
vB[21] = 0
vB[22] = 0

for i in range(17, 23):
    rB[i] = 16

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # cykl, który odświeża współrzędne położenia kul z uwzględnieniem ich prędkości :
    for i in range(1, 17):
        xB[i] += vB[i] * math.cos(aB[i])
        yB[i] += vB[i] * math.sin(aB[i])
        # rysowanie stołu
        pygame.draw.rect(win, 'saddlebrown', (20, 20, 270, 440))
        pygame.draw.rect(win, 'darkgreen', (40, 40, 230, 400))
        we = pygame.draw.rect(win, 'forestgreen', (50, 50, 210, 380))
        pygame.draw.rect(win, 'goldenrod', (20, 225, 20, 30))
        pygame.draw.rect(win, 'goldenrod', (270, 225, 20, 30))
        pygame.draw.rect(win, 'goldenrod', (20, 20, 30, 30))
        pygame.draw.rect(win, 'goldenrod', (260, 20, 30, 30))
        pygame.draw.rect(win, 'goldenrod', (20, 430, 30, 30))
        pygame.draw.rect(win, 'goldenrod', (260, 430, 30, 30))
        pygame.draw.rect(win, 'goldenrod', (20, 20, 40, 20))
        pygame.draw.rect(win, 'goldenrod', (20, 20, 20, 40))
        pygame.draw.rect(win, 'goldenrod', (250, 20, 30, 20))
        pygame.draw.rect(win, 'goldenrod', (20, 420, 20, 40))
        pygame.draw.rect(win, 'goldenrod', (20, 440, 40, 20))
        pygame.draw.rect(win, 'goldenrod', (270, 20, 20, 40))
        pygame.draw.rect(win, 'goldenrod', (270, 420, 20, 40))
        pygame.draw.rect(win, 'goldenrod', (250, 440, 40, 20))
        # otwory
        # pygame.draw.circle(win, 'black', (41, 240), 14)
        # pygame.draw.circle(win, 'black', (270, 240), 14)
        # pygame.draw.circle(win, 'black', (46, 46), 14)
        # pygame.draw.circle(win, 'black', (264, 46), 14)
        # pygame.draw.circle(win, 'black', (46, 434), 14)
        # pygame.draw.circle(win, 'black', (264, 434), 14)
        # kropki
        pygame.draw.circle(win, 'goldenrod', (103, 30), 2)
        pygame.draw.circle(win, 'goldenrod', (156, 30), 2)
        pygame.draw.circle(win, 'goldenrod', (209, 30), 2)

        pygame.draw.circle(win, 'goldenrod', (103, 450), 2)
        pygame.draw.circle(win, 'goldenrod', (156, 450), 2)
        pygame.draw.circle(win, 'goldenrod', (209, 450), 2)

        pygame.draw.circle(win, 'goldenrod', (30, 101), 2)
        pygame.draw.circle(win, 'goldenrod', (30, 142), 2)
        pygame.draw.circle(win, 'goldenrod', (30, 183), 2)

        pygame.draw.circle(win, 'goldenrod', (280, 101), 2)
        pygame.draw.circle(win, 'goldenrod', (280, 142), 2)
        pygame.draw.circle(win, 'goldenrod', (280, 183), 2)

        pygame.draw.circle(win, 'goldenrod', (30, 297), 2)
        pygame.draw.circle(win, 'goldenrod', (30, 338), 2)
        pygame.draw.circle(win, 'goldenrod', (30, 379), 2)

        pygame.draw.circle(win, 'goldenrod', (280, 297), 2)
        pygame.draw.circle(win, 'goldenrod', (280, 338), 2)
        pygame.draw.circle(win, 'goldenrod', (280, 379), 2)
        # Rysowanie kul
        pygame.draw.circle(win, cB[1], (xB[1], yB[1]), rB[1])
        pygame.draw.circle(win, cB[2], (xB[2], yB[2]), rB[2])
        pygame.draw.circle(win, cB[3], (xB[3], yB[3]), rB[3])
        pygame.draw.circle(win, cB[4], (xB[4], yB[4]), rB[4])
        pygame.draw.circle(win, cB[5], (xB[5], yB[5]), rB[5])
        pygame.draw.circle(win, cB[6], (xB[6], yB[6]), rB[6])
        pygame.draw.circle(win, cB[7], (xB[7], yB[7]), rB[7])
        pygame.draw.circle(win, cB[8], (xB[8], yB[8]), rB[8])
        pygame.draw.circle(win, cB[9], (xB[9], yB[9]), rB[9])
        pygame.draw.circle(win, cB[10], (xB[10], yB[10]), rB[10])
        pygame.draw.circle(win, cB[11], (xB[11], yB[11]), rB[11])
        pygame.draw.circle(win, cB[12], (xB[12], yB[12]), rB[12])
        pygame.draw.circle(win, cB[13], (xB[13], yB[13]), rB[13])
        pygame.draw.circle(win, cB[14], (xB[14], yB[14]), rB[14])
        pygame.draw.circle(win, cB[15], (xB[15], yB[15]), rB[15])
        pygame.draw.circle(win, cB[16], (xB[16], yB[16]), rB[16])

        # otwory

        pygame.draw.circle(win, cB[17], (xB[17], yB[17]), rB[17])
        pygame.draw.circle(win, cB[18], (xB[18], yB[18]), rB[18])
        pygame.draw.circle(win, cB[19], (xB[19], yB[19]), rB[19])
        pygame.draw.circle(win, cB[20], (xB[20], yB[20]), rB[20])
        pygame.draw.circle(win, cB[21], (xB[21], yB[21]), rB[21])
        pygame.draw.circle(win, cB[22], (xB[22], yB[22]), rB[22])

    pygame.time.delay(10)
    pygame.display.update()

    # zderzenia piłek ze ścianami:
    for i in range(1, n + 1):
        # z lewą ścianą
        if xB[i] <= 63 - rB[i] and (aB[i] > math.pi / 2 or aB[i] < -math.pi / 2):
            aB[i] = math.pi - aB[i]
        # z prawą ścianą
        if xB[i] >= 259 - rB[i] and (aB[i] > -math.pi / 2 or aB[i] < math.pi / 2):
            aB[i] = math.pi - aB[i]
        # z górną scianą
        if yB[i] <= 65 - rB[i] and (aB[i] < 0 and aB[i] > -math.pi):
            aB[i] = -aB[i]
        # z dolną scianą
        if yB[i] >= 430 - rB[i] and (aB[i] > 0 and aB[i] < math.pi):
            aB[i] = -aB[i]

        while aB[i] > math.pi: aB[i] -= 2 * math.pi
        while aB[i] < -math.pi: aB[i] += 2 * math.pi
    # przejść przez wszystkie kulki od pierwszej do ostatniej i
    # porównać z kulką o wyższej liczbie porządkowej
    for i in range(1, 17):
        for j in range(i + 1, 17):
            # odległość między kulami
            # jeśli odległość między środkami kul jest mniejsza niż suma ich promieni, to kule się dotykają
            odl = ((xB[i] - xB[j]) ** 2 + (yB[i] - yB[j]) ** 2) ** 0.5

            if odl <= rB[i] + rB[j]:  # Kontrola zbliżenia kuli
                # Następnie sprawdzamy, czy w wyniku kolejnego kroku odległość
                # między kulami zmniejszyła się (wiersz 169-174), w przeciwnym razie kule rozlecą się.
                # Jeśli ta kontrola nie zostanie przeprowadzona, kulki mogą się do siebie przyklejać.
                xB1new = xB[i] + vB[i] * math.cos(aB[i])
                yB1new = yB[i] + vB[i] * math.sin(aB[i])
                xB2new = xB[i] + vB[j] * math.cos(aB[j])
                yB2new = yB[i] + vB[j] * math.sin(aB[j])
                # Nowa odległość między kulami, gdyby ruch był kontynuowany
                odlnew = ((xB1new - xB2new) ** 2 + (yB1new - yB2new) ** 2) ** 0.5
                if odl > odlnew:  # kule zderzyły się na podejściu
                    # kąt obrotu promienia (w) od środka kuli (i)
                    # do środka kuli (j), z którą nastąpiła kolizja:
                    BB = math.atan((yB[j] - yB[i]) / (xB[j] - xB[i]))
                    if (xB[j] - xB[i]) < 0:
                        BB += math.pi
                        while BB > math.pi / 2: BB -= 2 * math.pi
                        while BB < -math.pi / 2: BB += 2 * math.pi
                    # kąt od promienia w (między środkami kul ) do kierunku ruchu kuli
                    w1 = aB[i] - BB
                    w2 = aB[j] - BB

                    # rzut prędkości kuli na promień w i
                    # na prostą prostopadłą do niego (wt) przed zderzeniem

                    Vw1 = vB[i] * math.cos(w1)
                    Vw2 = vB[j] * math.cos(w2)
                    Vwt1 = vB[i] * math.sin(w1)
                    Vwt2 = vB[j] * math.sin(w2)

                    # rzut prędkości kuli na promień w po zderzeniu
                    # (rzut prędkości na płaszczyznę prostopadłą do osi w nie zmienia się)

                    # wzory zderzenia centralnie sprężystego

                    Vw1 = (2 * mB[j] * vB[j] * math.cos(w2) + (mB[i] - mB[j]) * vB[i] * math.cos(w1)) / (mB[i] + mB[j])
                    Vw2 = (2 * mB[i] * vB[i] * math.cos(w1) + (mB[j] - mB[i]) * vB[j] * math.cos(w2)) / (mB[i] + mB[j])

                    # prędkość kul po zderzeniu
                    vB[i] = (Vw1 ** 2 + Vwt1 ** 2) ** 0.5
                    vB[j] = (Vw2 ** 2 + Vwt2 ** 2) ** 0.5

                    # kąt od promienia w do kierunku ruchu po zderzeniu
                    w1 = math.atan(Vwt1 / (Vw1))
                    if Vw1 < 0: w1 += math.pi
                    w2 = math.atan(Vwt2 / (Vw2))
                    if Vw2 < 0: w2 += math.pi

                    # Nowy wypadkowy kierunek ruchu po zderzeniu

                    aB[i] = BB + w1
                    while aB[i] > math.pi: aB[i] -= 2 * math.pi
                    while aB[i] < - math.pi: aB[i] += 2 * math.pi
                    aB[j] = BB + w2
                    while aB[j] > math.pi: aB[j] -= 2 * math.pi
                    while aB[j] < - math.pi: aB[j] += 2 * math.pi

    # wpadają do dziur
    for i in range(17, 23):
        for j in range(1, 17):
            odl1 = ((xB[i] - xB[j]) ** 2 + (yB[i] - yB[j]) ** 2) ** 0.5

            if odl1 <= rB[i] + rB[j]:
                rB[j] = 0

pygame.quit()
