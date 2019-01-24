import vtk
import time
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk import (
    vtkJPEGReader, vtkImageCanvasSource2D, vtkImageActor, vtkPolyDataMapper,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkSuperquadricSource,
    vtkActor, VTK_MAJOR_VERSION
)
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



renderer = vtk.vtkRenderer()

renderer.AddActor(image_actor)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

iren.Initialize()
iren.Start()



