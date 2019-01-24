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

    ######################################
    # mapper = vtk.vtkPolyDataMapper()
    # mapper.SetInputConnection(tf.GetOutputPort())
    # actor = vtk.vtkActor()
    # actor.SetMapper(mapper)
    ######################################

    renderer = vtk.vtkRenderer()

    renderer.AddActor(image_actor)
    renWin = vtk.vtkRenderWindow()
    #renWin.AddRenderer(renderer)

    iren = QVTKRenderWindowInteractor()
    #iren.SetRenderWindow(renWin)
    iren.GetRenderWindow().AddRenderer(renderer)

    interactor = iren.GetRenderWindow().GetInteractor()
    interactor.Initialize()
    interactor.Start()
    return iren













'''from __future__ import print_function
import sys
from vtk import (
    vtkJPEGReader, vtkImageCanvasSource2D, vtkImageActor, vtkPolyDataMapper,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkSuperquadricSource,
    vtkActor, VTK_MAJOR_VERSION
)
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk
import time
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor



def show_map():

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

    #renderer.AddActor(image_actor)
    #renderer.AddActor(cubeActor0)


    #################################################
    # renWin = vtk.vtkRenderWindow()
    # renWin.AddRenderer(renderer)
    #
    # iren = vtk.vtkRenderWindowInteractor()
    # iren.SetRenderWindow(renWin)
    #
    # iren.Initialize()
    # iren.Start()
    #################################################

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(tf.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()

    vtkWidget = QVTKRenderWindowInteractor()

    vtkWidget.GetRenderWindow().AddRenderer(renderer)

    interactor = vtkWidget.GetRenderWindow().GetInteractor()
    renderer.AddActor(actor)
    interactor.Initialize()
    interactor.Start()
    return vtkWidget'''
