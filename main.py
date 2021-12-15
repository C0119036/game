import pygame
from pygame.locals import *
import sys
import random

# import ss
# import gun
# import mato

def main():
    pygame.init()       # pygame初期化
    pygame.display.set_mode((600, 600), 0, 32)  # 画面設定
    pygame.display.set_caption("Aim")
    screen = pygame.display.get_surface()

    x = random.randint(100, 500)
    y = random.randint(100, 500)
    q = random.randint(100, 500)
    w = random.randint(100, 500)
    pygame.draw.rect(screen, (255,255,255), (70,70,460,460), 2)
    pygame.draw.line(screen, (255,255,255), (70, 70), (0, 0), 2)
    pygame.draw.line(screen, (255,255,255), (530, 70), (600, 0), 2)
    pygame.draw.line(screen, (255,255,255), (70, 530), (0, 600), 2)
    pygame.draw.line(screen, (255,255,255), (530, 530), (600, 600), 2)

    gun = pygame.image.load("gun.bmp").convert_alpha()
    gun = pygame.transform.scale(gun, (100, 100))
    screen.blit(gun, (500, 530))

    while (1):

        #ここから

        pygame.draw.rect(screen, (255,0,0), (x,y,30,30))

        pressed=pygame.mouse.get_pressed()	
        if pressed[0]:		
            (m, n) = pygame.mouse.get_pos()
            mause = (m, n)
            X = mause[0]
            Y = mause[1]

            if  x <= X <= x+30:
                if y <= Y <= y+30:
                    pygame.draw.rect(screen, (0,0,0), (x,y,30,30))
                    x = random.randint(100, 500)
                    y = random.randint(100, 500)

        #ここまでが敵のはず
        #ここから

        pygame.draw.rect(screen, (255,0,0), (q,w,30,30))

        pressed=pygame.mouse.get_pressed()	
        if pressed[0]:		
            (e, r) = pygame.mouse.get_pos()
            mause = (e, r)
            E = mause[0]
            R = mause[1]

            if  q <= E <= q+30:
                if w <= R <= w+30:
                    pygame.draw.rect(screen, (0,0,0), (q,w,30,30))
                    q = random.randint(100, 500)
                    w = random.randint(100, 500)
        #ここまでが敵のはず
        G = random.randint(1,10)
        if G == 1:
            pygame.draw.line(screen, (255,0,0), (500, 530), (470, 500), 4)#真ん中
        elif G == 3:
            pygame.draw.line(screen, (255,0,0), (500, 550), (450, 550), 4)#下
        elif G == 7:
            pygame.draw.line(screen, (255,0,0), (520, 520), (490, 470), 4)#↑
        elif G == 4:
            pygame.draw.line(screen, (0,0,0), (500, 530), (470, 500), 4)
        elif G == 2:
            pygame.draw.line(screen, (0,0,0), (500, 550), (450, 550), 4)
        elif G == 9:
            pygame.draw.line(screen, (0,0,0), (520, 520), (490, 470), 4)

        pygame.display.update() #描画処理を実行
        for event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()

if __name__ == "__main__":
    main()