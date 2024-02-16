import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersSources import vtkCubeSource
from vtkmodules.vtkRenderingCore import (
vtkActor,
vtkPolyDataMapper,
vtkRenderWindow,
vtkRenderWindowInteractor,
vtkRenderer
)


def main():
    cubeSource = vtkCubeSource()
    cubeSource.SetCenter(0.0,0.0,0.0)
    cubeSource.SetXLength(2.5)
    cubeSource.SetYLength(3.5)
    cubeSource.SetZLength(4.5)


    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(cubeSource.GetOutputPort())
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)    
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderWindow.Render()

    renderWindowInteractor.Start()


if __name__ == "__main__":
    main()
