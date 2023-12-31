import random
import sys
import pygame as pg

WIDTH, HEIGHT = 1600, 900

delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
    pg.K_UP and pg.K_LEFT:(-5,-5),######?????????????????????????
    pg.K_UP and pg.K_RIGHT:(+5,-5),
    pg.K_DOWN and pg.K_LEFT:(-5,+5),
    pg.K_DOWN and pg.K_RIGHT:(+5,+5)
}

def check_bound(obj_rct: pg.Rect):
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")

    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)
    be_img = pg.image.load("ex02/fig/6.png")
    be_img = pg.transform.rotozoom(be_img,0, 2.0)
    bd_img = pg.Surface((20, 20))
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_rct = bd_img.get_rect()
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    bd_rct.center = (x, y)
    vx, vy = +5, +5

    clock = pg.time.Clock()
    tmr = 0

    # 追加の変数と画像をロード
    kk_direction = 0  # 初期向きは右

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        if kk_rct.colliderect(bd_rct):
            screen.blit(bg_img, [0, 0])
            screen.blit(be_img, kk_rct)
            pg.display.update()
            print("ゲームオーバー")
            return

        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
                if key == pg.K_RIGHT:
                    kk_direction = 0
                elif key == pg.K_UP:
                    kk_direction = 1
                elif key == pg.K_DOWN:
                    kk_direction = 2
                elif key == pg.K_LEFT:
                    kk_direction = 3
                elif key == (pg.K_UP and pg.K_RIGHT):
                    kk_direction = 4
                elif key == (pg.K_UP and pg.K_LEFT):
                    kk_direction = 5
                elif key == (pg.K_DOWN and pg.K_RIGHT):
                    kk_direction = 6
                elif key == (pg.K_DOWN and pg.K_LEFT):
                    kk_direction = 7
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        # kk_directionに応じて画像を回転して表示
        if kk_direction == 0:  # 右向き
            rotated_kk_img = pg.transform.flip(kk_img, True, False)
        elif kk_direction == 1:  # 上向き
            rotated_kk_img = pg.transform.flip(pg.transform.rotate(kk_img, 90), False, True)
        elif kk_direction == 2:  # 下向き
            rotated_kk_img = pg.transform.flip(pg.transform.rotate(kk_img, 270), False, True)
        elif kk_direction == 3:  # 左向き
            rotated_kk_img = kk_img
        elif kk_direction == 4:  # 右上斜め
            rotated_kk_img = pg.transform.rotate(kk_img, -45)
        elif kk_direction == 5:  # 左上斜め
            rotated_kk_img = pg.transform.rotate(kk_img, 45)
        elif kk_direction == 6:  # 右下斜め
            rotated_kk_img = pg.transform.flip(pg.transform.rotate(kk_img, 45), False, True)
        elif kk_direction == 7:  # 左下斜め
            rotated_kk_img = pg.transform.flip(pg.transform.rotate(kk_img, -45), True, False)
        screen.blit(rotated_kk_img, kk_rct)

        bd_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bd_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bd_img, bd_rct)

        pg.display.update()
        tmr += 1
        clock.tick(50)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
