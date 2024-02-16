#!/usr/bin/env python
import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersSources import vtkCubeSource
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
vtkActor,
vtkPolyDataMapper,
vtkRenderWindow,
vtkRenderWindowInteractor,
vtkRenderer,
vtkLight
)


def main():
    ncolors = vtkNamedColors()
    ncolors.SetColor('red', [255, 0, 0, 255])
    ncolors.SetColor('green', [0, 255, 0, 255])
    ncolors.SetColor('blue', [0, 0, 255, 255])
    ncolors.SetColor('yellow', [255, 255, 51, 255])
    ncolors.SetColor('white', [255, 255, 255, 255])

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)    
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    centers = [(0,0,0), (0,10,0), (10,0,0), (10,10,0)]
    colors = ['red','green','blue', 'yellow']

    for cen, col in zip(centers, colors):
        cubeSource = vtkCubeSource()
        cubeSource.SetCenter(*cen)
        cubeSource.SetXLength(2.5)
        cubeSource.SetYLength(3.5)
        cubeSource.SetZLength(4.5)

        # Create a mapper and actor
        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(cubeSource.GetOutputPort())
        actor = vtkActor()
        actor.GetProperty().SetColor(ncolors.GetColor3d('white'))
        actor.SetMapper(mapper)

        renderer.AddActor(actor)

    light = vtkLight()
    light.SetFocalPoint(0, 0, 0)
    light.SetPosition(30, 0, 1)
    light.SetColor(ncolors.GetColor3d('white'))
    renderer.AddLight(light)

    light = vtkLight()
    light.SetFocalPoint(0, 0, 0)
    light.SetPosition(0, 30, 1)
    light.SetColor(ncolors.GetColor3d('red'))
    renderer.AddLight(light)

    light = vtkLight()
    light.SetFocalPoint(0, 0, 0)
    light.SetPosition(0, 30, 30)
    light.SetColor(ncolors.GetColor3d('blue'))
    renderer.AddLight(light)


    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == "__main__":
    main()
