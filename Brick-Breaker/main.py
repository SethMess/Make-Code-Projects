@namespace
class SpriteKind:
    block = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    sprite.set_velocity(sprite.vx, -1 * sprite.vy)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprite2.set_velocity(sprite2.vx, -1 * sprite2.vy)
    otherSprite2.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.block, on_on_overlap2)

tile: Sprite = None
x = 0
paddle = sprites.create(img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ....bbbbbbbbbbbbbbbbbbbbbbbb....
            ....bbbbbbbbbbbbbbbbbbbbbbbb....
            ....bbbbbbbbbbbbbbbbbbbbbbbb....
            ................................
            ................................
            ................................
            ................................
    """),
    SpriteKind.player)
paddle.set_position(79, 100)
paddle.set_stay_in_screen(True)
controller.move_sprite(paddle, 100, 0)
projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 9 9 9 . . . . . . . 
            . . . . . 9 6 7 6 9 . . . . . . 
            . . . . 9 6 7 6 7 6 9 . . . . . 
            . . . . 1 7 1 7 1 7 1 . . . . . 
            . . . . 8 6 7 6 7 6 8 . . . . . 
            . . . . . 8 6 7 6 8 . . . . . . 
            . . . . . . 8 8 8 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    paddle,
    50,
    -55 + randint(-10, 10))
projectile.set_flag(SpriteFlag.DESTROY_ON_WALL, False)
projectile.set_bounce_on_wall(True)
for index in range(10):
    for index2 in range(3):
        x = index * 18 + 8
        tile = sprites.create(img("""
                6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
                            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
                            6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6 
                            6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6 
                            6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6 
                            6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6 
                            6 9 c 6 6 6 9 9 9 6 9 c c c 9 6 
                            6 9 c c c 9 6 9 9 9 6 6 6 c 9 6 
                            6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6 
                            6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6 
                            6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6 
                            6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6 
                            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
                            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
                            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
            """),
            SpriteKind.block)
        tile.set_position(x, index2 * 18 + 20)
info.set_score(1)
scene.set_background_color(13)
direction = 1

def on_forever():
    if projectile.bottom > 119:
        game.over(False, effects.slash)
    if info.score() == 28:
        game.over(True, effects.bubbles)
forever(on_forever)
