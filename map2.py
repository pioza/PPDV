import vtk
import time
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk import (
    vtkJPEGReader, vtkImageCanvasSource2D, vtkImageActor, vtkPolyDataMapper,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkSuperquadricSource,
    vtkActor, VTK_MAJOR_VERSION
)


# Read the image
def show_map():
    jpeg_reader = vtkJPEGReader()
    jpeg_reader.SetFileName('map1.jpg')
    jpeg_reader.Update()
    image_data = jpeg_reader.GetOutput()

    # Create an image actor to display the image
    image_actor = vtkImageActor()
    image_actor.SetInputData(image_data)

    renderer = vtk.vtkRenderer()

    renderer.AddActor(image_actor)
    renWin = vtk.vtkRenderWindow()
    #renWin.AddRenderer(renderer)

    iren = QVTKRenderWindowInteractor()
    #iren.SetRenderWindow(renWin)
    iren.GetRenderWindow().AddRenderer(renderer)

    ####################################################################################################################
    cube00 = vtk.vtkCubeSource()
    cube00.SetXLength(2.5)
    cube00.SetYLength(3.5)
    cube00.SetZLength(12)
    cube00.SetCenter(400, 265, 0.0)

    cubeMapper0 = vtk.vtkPolyDataMapper()
    cubeMapper0.SetInputConnection(cube00.GetOutputPort())
    cubeActor0 = vtk.vtkActor()
    cubeActor0.GetProperty().SetColor(0, 0, 255)
    cubeActor0.SetMapper(cubeMapper0)




    renderer.AddActor(cubeActor0)
    
    
    ####################################################################################################################
    interactor = iren.GetRenderWindow().GetInteractor()
    interactor.Initialize()
    interactor.Start()
    return iren


