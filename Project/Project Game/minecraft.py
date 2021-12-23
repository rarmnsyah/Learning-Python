from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Sky(texture = 'sky_sunset')
player = FirstPersonController()

hand = Entity(
    model = 'cube',
    texture = 'brick',
    rotation = (30,-40),
    position = (0.5, -0.6),
    parent = camera.ui,
    scale = (0.25, .25,.25)
)

boxes = []
for n in range(12):
    for k in range(12):
        box = Button(
            color = color.white,
            model = 'cube',
            texture = 'brick',
            position = (k,0,n),
            parent = scene,
            origin_y = 0.5,
        )
        boxes.append(box)

def update():
    if held_keys['left mouse']:
        hand.position = (0.4, -0.5)
    elif held_keys['right mouse']:
        hand.position = (0.4, -.5)
    else:
        hand.position = (.4, -.6)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color = color.white,
                    model = 'cube',
                    texture = 'brick',
                    position = box.position + mouse.normal,
                    parent = scene,
                    origin_y = 0.5,
                )
                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)



app.run()