from turtle import reset
from ursina import * 

def reset():
    ball.x = 0
    ball.z = -.2

def update():
    global dx,dz, score_A, score_B
    paddle_A.x += held_keys['d']*time.dt
    paddle_A.x -= held_keys['a']*time.dt
    paddle_B.x += held_keys['right arrow']*time.dt
    paddle_B.x -= held_keys['left arrow']*time.dt
    ball.x += time.dt*dx
    ball.z += time.dt*dz

    if paddle_A.x > .4:
        paddle_A.x -= .1

    if paddle_A.x < -.4:
        paddle_A.x += .1

    if paddle_B.x > .4:
        paddle_B.x -= .1

    if paddle_B.x < -.4:
        paddle_B.x += .1

    # boundary checking
    # left and right
    if abs(ball.x) > .4:
        dx = -dx

    # top and bottom
    if ball.z > .25:
        score_B += 1
        Audio('sounds/whistle.wav')
        print_on_screen(f'Player A: Player B = {score_A}: {score_B}', position=(-.85, .45), duration = 2)
        reset()

    if ball.z < -.65:
        score_A += 1
        Audio('sounds/whistle.wav')
        print_on_screen(f'Player A: Player B = {score_A}: {score_B}', position=(-.85, .45), duration = 2)
        reset()

    # collisions
    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == paddle_A or hit_info.entity == paddle_B:
            Audio('sounds/pong_sound.wav')
            dz = -dz

app = Ursina()

window.color = color.orange

table = Entity(model = 'cube', color = color.green, scale = (10,.5,14), position = (0,0,0), texture = 'white_cube')

paddle_A = Entity(parent = table, color = color.blue, model = 'cube', scale = (.2, .03, .05), position = (0, 3.7, .22), collider = 'box')
paddle_B = duplicate(paddle_A, z = -.62)

camera.position = (0,15,-26)
camera.rotation_x = 30

Text(text = "Player A", scale =2, position = (-.1, .32))
Text(text = "Player B", scale =2, position = (-.1, -.4))

line = Entity(parent = table, scale = (.88, .2, .1), model = 'quad', position = (0, 3.5, -.2))
ball = Entity(parent = table, model = 'circle', color = color.red, scale = .05, position = (0, 3.71, -.2), collider = 'box')
dx = .1
dz = .2
score_A = 0
score_B = 0

app.run()