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


    # Create a common text property.
    temperatureProperty = vtk.vtkTextProperty()
    temperatureProperty.SetFontSize(20)
    temperatureProperty.SetColor(1.0, 0, 0)



    ####################################################################################################################

    ind00 = vtk.vtkTextActor()
    ind00.SetInput("19°")
    ind00.SetPosition(650,440)
    ind00prop = ind00.GetTextProperty()
    ind00prop = ind00.SetTextProperty(temperatureProperty)
    renderer.AddActor(ind00)



    ind01 = vtk.vtkCubeSource()
    ind01.SetXLength(2.5)
    ind01.SetYLength(3.5)
    ind01.SetZLength(50)
    ind01.SetCenter(400, 265, 0.0)

    indMapper01 = vtk.vtkPolyDataMapper()
    indMapper01.SetInputConnection(ind01.GetOutputPort())
    indActor01 = vtk.vtkActor()
    indActor01.GetProperty().SetColor(0, 0, 255)
    indActor01.SetMapper(indMapper01)
    renderer.AddActor(indActor01)



    ####################################################################################################################
    interactor = iren.GetRenderWindow().GetInteractor()
    interactor.Initialize()
    interactor.Start()
    return iren


