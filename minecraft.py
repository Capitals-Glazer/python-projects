from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
mouse.visible = False  # <<< Hides the pink reticle


# Choose block texture colors
block_colors = {
    1: color.lime,
    2: color.gray,
    3: color.rgb(200, 100, 100),
    4: color.brown
}

current_block = 1

class Voxel(Button):
    def __init__(self, position=(0,0,0), color=color.white):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            color=color,
            scale=1
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, color=block_colors[current_block])

# Generate a flat world
for x in range(-20, 20):
    for z in range(-20, 20):
        for y in range(-3, 1):  # Make the ground 4 blocks thick
            Voxel(position=(x, y, z), color=block_colors[1])


# Player & sky
player = FirstPersonController()
Sky()

def update():
    global current_block
    if held_keys['1']: current_block = 1
    if held_keys['2']: current_block = 2
    if held_keys['3']: current_block = 3
    if held_keys['4']: current_block = 4

app.run()

