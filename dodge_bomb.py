import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    
    # 爆弾Surfaceを作成
    bomb_surface = pg.Surface((20, 20), pg.SRCALPHA)
    pg.draw.circle(bomb_surface, (255, 0, 0), (10, 10), 10)
    bomb_surface.set_colorkey((0, 0, 0))  # 黒を透明に設定
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        
        # ランダムな位置に爆弾を配置
        bomb_x = random.randint(0, WIDTH - 20)
        bomb_y = random.randint(0, HEIGHT - 20)
        screen.blit(bomb_surface, (bomb_x, bomb_y))
        
        pg.display.update()
        tmr += 1
        clock.tick(10)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()