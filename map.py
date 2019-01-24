from __future__ import print_function
import sys
from vtk import (
    vtkJPEGReader, vtkImageCanvasSource2D, vtkImageActor, vtkPolyDataMapper,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkSuperquadricSource,
    vtkActor, VTK_MAJOR_VERSION
)
import vtk
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

    # Create a renderer to display the image in the background
    background_renderer = vtkRenderer()


    ########################################################################################################

    cube0 = vtk.vtkCubeSource()
    cube0.SetXLength(10)
    cube0.SetYLength(33.5)
    cube0.SetZLength(4.5)
    cube0.SetCenter(0.0, 0.0, 0.0)


    cubeMapper0 = vtk.vtkPolyDataMapper()
    cubeMapper0.SetInputConnection(cube0.GetOutputPort())

    cubeActor0 = vtk.vtkActor()

    cubeActor0.GetProperty().SetColor(0, 0, 255)

    cubeActor0.SetMapper(cubeMapper0)

    ren0 = vtk.vtkRenderer()
    ren0.SetViewport(0.6, 0.55, 0.7, 0.6)
    ren0.SetLayer(1)
    ren0.AddActor(cubeActor0)

    ren1 = vtk.vtkRenderer()
    ren1.SetViewport(0.65, 0.55, 0.7, 0.6)
    ren1.SetLayer(1)

    ################################################################################

    temp0 = vtk.vtkTextActor()

    temp0.SetInput("19")
    temp0prop = temp0.GetTextProperty()
    temp0prop.SetFontFamilyToArial()
    temp0prop.SetFontSize(40)
    temp0prop.SetColor(1.0, 0, 0)
    ren0.AddActor(temp0)




    ################################################################################

    pressure0 = vtk.vtkTextActor()

    pressure0.SetInput("1050")
    pressure0prop = pressure0.GetTextProperty()
    pressure0prop.SetFontFamilyToArial()
    pressure0prop.SetFontSize(30)
    pressure0prop.SetColor(0, 0, 1.0)
    ren1.AddActor(pressure0)

    ################################################################################








    scene_renderer = vtkRenderer()

    render_window = vtkRenderWindow()

    # Set up the render window and renderers such that there is
    # a background layer and a foreground layer
    background_renderer.SetLayer(0)
    background_renderer.InteractiveOff()
    scene_renderer.SetLayer(1)
    render_window.SetNumberOfLayers(3)
    render_window.AddRenderer(background_renderer)
    render_window.AddRenderer(scene_renderer)
    render_window.AddRenderer(ren0)
    render_window.AddRenderer(ren1)


    render_window_interactor = QVTKRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(render_window)


    ###########################################################################################################
    # Add actors to the renderers

    background_renderer.AddActor(image_actor)

    ###############################################################################################################

    # Render once to figure out where the background camera will be
    render_window.Render()

    # Set up the background camera to fill the renderer with the image
    origin = image_data.GetOrigin()
    spacing = image_data.GetSpacing()
    extent = image_data.GetExtent()

    camera = background_renderer.GetActiveCamera()
    camera.ParallelProjectionOn()

    xc = origin[0] + 0.5*(extent[0] + extent[1]) * spacing[0]
    yc = origin[1] + 0.5*(extent[2] + extent[3]) * spacing[1]
    # xd = (extent[1] - extent[0] + 1) * spacing[0]
    yd = (extent[3] - extent[2] + 1) * spacing[1]
    d = camera.GetDistance()
    camera.SetParallelScale(0.5 * yd)
    camera.SetFocalPoint(xc, yc, 0.0)
    camera.SetPosition(xc, yc, d)

    # Render again to set the correct view
    render_window.Render()

    # Interact with the window
    #render_window_interactor.Start()
    return render_window_interactor
