import pygame


w, hue = int(input()), int(input())
if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна: 
    size = width, height = 300, 300
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    pygame.display.set_caption('Куб')
    
    color = pygame.Color(255, 0, 0)
    hsv = color.hsva
    # увеличиваем параметр Value, который влияет на яркость
    color.hsva = (hue, hsv[1], 75, hsv[3])
    pygame.draw.polygon(screen, color, [(10, 290), (10 + w, 290), (10 + w, 290 - w), (10, 290 - w)])
    
    color.hsva = (hue, hsv[1], 100, hsv[3])
    pygame.draw.polygon(screen, color, [(10 + w, 290 - w), (10, 290 - w), (10 + w / 2, 290 - 1.5 * w), (10 + 1.5 * w, 290 - 1.5 * w)])
    
    color.hsva = (hue, hsv[1], 50, hsv[3])
    pygame.draw.polygon(screen, color, [(10 + 1.5 * w, 290 - 1.5 * w), (10 + w, 290 - w), (10 + w, 290), (10 + 1.5 * w, 290 - 0.5 * w)])
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
