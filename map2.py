import vtk
import time
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk import (
    vtkJPEGReader, vtkImageCanvasSource2D, vtkImageActor, vtkPolyDataMapper,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkSuperquadricSource,
    vtkActor, VTK_MAJOR_VERSION
)

def 
# Read the image
jpeg_reader = vtkJPEGReader()
jpeg_reader.SetFileName('map1.jpg')
jpeg_reader.Update()
image_data = jpeg_reader.GetOutput()

# Create an image actor to display the image
image_actor = vtkImageActor()
image_actor.SetInputData(image_data)


######################################
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(tf.GetOutputPort())
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
######################################

cube0 = vtk.vtkCubeSource()
cube0.SetXLength(2.5)
cube0.SetYLength(3.5)
cube0.SetZLength(4.5)
cube0.SetCenter(110.0, 0.0, 0.0)
cubeMapper0 = vtk.vtkPolyDataMapper()
cubeMapper0.SetInputConnection(cube0.GetOutputPort())
cubeActor0 = vtk.vtkActor()
cubeActor0.GetProperty().SetColor(255, 0, 0)
cubeActor0.SetMapper(cubeMapper0)


renderer = vtk.vtkRenderer()

renderer.AddActor(image_actor)
####
renderer.AddActor(cubeActor0)

####
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()
iren.Start()
