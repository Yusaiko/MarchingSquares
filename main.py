from display import *
from vector import createVector
pygame.init()


#Auflösung des Grids und Berechnung der Zeilen und Spalten
resolution = 10
cols = WIDTH // resolution + 1
rows = HEIGHT // resolution + 1
WHITE = (255, 255, 255)

def color(rgb):
    return int(rgb), int(rgb), int(rgb)
 
def getState(a, b, c, d):
    return a * 8 + b * 4 + c * 2 + d * 1

def line(a, b):
    pygame.draw.line(screen, WHITE, (a.x, a.y), (b.x, b.y), 1)


field = []
for i in range(cols):
    field.append([])
    for j in range(rows):
        field[i].append(
            math.floor(random.randint(0, 1))
        )

run = True
while run:
    screen.fill(color(0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            field = []
            for i in range(cols):
                field.append([])
                for j in range(rows):
                    field[i].append(
                        math.floor(random.randint(0, 1))
                    )

    for i in range(cols):
        for j in range(rows):
            strokeWeight = round(resolution * 0.2)

            pygame.draw.circle(screen, color(10), (i*resolution, j*resolution), strokeWeight, strokeWeight)

    for i in range(cols-1):
        for j in range(rows-1):
            x = i * resolution
            y = j * resolution

            a = createVector(x + resolution // 2, y)
            b = createVector(x + resolution, y + resolution // 2)
            c = createVector(x + resolution // 2, y + resolution)
            d = createVector(x, y + resolution // 2)
            
            state = getState(field[i][j], field[i+1][j], field[i+1][j+1], field[i][j+1])

            if state == 1: line(c, d)
            elif state == 2: line(b, c)
            elif state == 3: line(b, d)
            elif state == 4: line(a, b)
            elif state == 5: line(a, d); line(b, c)
            elif state == 6: line(a, c)
            elif state == 7: line(a, d)
            elif state == 8: line(a, d)
            elif state == 9: line(a, c)
            elif state == 10: line(a, b); line(c, d)
            elif state == 11: line(a, b)
            elif state == 12: line(b, d)
            elif state == 13: line(b, c)
            elif state == 14: line(c, d)



    pygame.display.update()

pygame.quit()