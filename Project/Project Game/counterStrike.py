from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Sky()

ground = Entity(
    model = 'plane',
    texture = 'brick',
    scale = (100,1,100),
    collider = 'mesh',
    
)


player = FirstPersonController(
    position = (0,2,5)
)

wall1 = Entity(
    model = 'cube',
    texture = 'wall',
    scale = (100,10,5),
    position = (0,5,50),
    color = color.gray,
    collider = 'mesh'
)

wall2 = duplicate(wall1, z=-50)
wall3 = duplicate(wall1, rotation_y= 90, x = -50, z= 0)
wall4 = duplicate(wall3, x=50)
wall5 = duplicate(wall1, position = (0,2,0) , scale = (20,5,0.5), color = color.white)

weapon = Entity(
    model = 'cube',
    texture = 'wall',
    parent = camera.ui,
    rotation = (30,-40),
    position = (.5,-.6),
    scale = .25
)

app.run()
