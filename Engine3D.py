from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, unlit, gourad, toon, glow, textureBlend



#Medium Shot
def mediumShot():
    rend = Renderer(960, 540)
    rend.glViewMatrix(translate=V3(1, 0, 0), rotate=V3(0,0,0))
    rend.active_texture = Texture("models/model.bmp")
    rend.active_shader = gourad
    rend.glLoadModel("models/model.obj",
                    translate = V3(0,0,-10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/mediumShot.bmp")

#High Angle
def highAngle():
    rend = Renderer(960, 540)
    rend.glViewMatrix(translate=V3(0, 5, 0), rotate=V3(-15,0,0))
    rend.active_texture = Texture("models/model.bmp")
    rend.active_shader = gourad
    rend.glLoadModel("models/model.obj",
                    translate = V3(0,0,-10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/highAngle.bmp")


#Low Angle
def lowAngle():
    rend = Renderer(960, 540)
    rend.glViewMatrix(translate=V3(1, -2.2, 0), rotate=V3(0,0,0))
    rend.active_texture = Texture("models/model.bmp")
    rend.active_shader = gourad
    rend.glLoadModel("models/model.obj",
                    translate = V3(0,0,-10),
                    scale = V3(3,3,3),
                    rotate = V3(0,0,0))
    rend.glFinish("outputs/lowAngle.bmp")


#Dutch Angle
def dutchAngle():
    rend = Renderer(960, 540)
    rend.glViewMatrix(translate=V3(1, 0, 0), rotate=V3(0,0,-10))
    rend.active_texture = Texture("models/model.bmp")

    rend.active_shader = gourad
    rend.glLoadModel("models/model.obj",
                    translate = V3(0,0,-10),
                    scale = V3(3,3,3),
                    rotate = V3(0,35,0))
    rend.glFinish("outputs/dutchAngle.bmp")

def glowModel():
    rend = Renderer(960, 540)
    rend.glViewMatrix(translate=V3(0, 0, 0), rotate=V3(0,0,0))
    rend.active_texture = Texture("models/model.bmp")

    rend.active_shader = glow
    rend.glLoadModel("models/model.obj",
                     translate = V3(0, 0, -8),
                     scale = V3(3,3,3),
                     rotate = V3(0,0,0))
    rend.glFinish("outputs/glowModel.bmp")


def menu():
    print('\nEjercicio 5 - Graficas\n\nOpciones:\n1. Medium Shot \
           \n2. High Angle\n3. Low Angle\n4. Dutch Angle\n5. Renderizar modelo glow (Generado en clase)\n6. Salir\n')

menu()
option = int(input('Elija un angulo para el photoshoot: '))
while option != 6:
    if option == 1: mediumShot()
    elif option == 2: highAngle()
    elif option == 3: lowAngle()
    elif option == 4: dutchAngle()
    elif option == 5: glowModel()
    else: print('\nOpcion invalida\n')

    menu()
    option = int(input('Elija un angulo para el photoshoot: '))

print('Se ha acabado el photoshoot! Chequee los resultados en la carpeta de outputs.\n')