
import vtk
import time
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtk import (
    vtkJPEGReader, vtkImageCanvasSource2D, vtkImageActor, vtkPolyDataMapper,
    vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor, vtkSuperquadricSource,
    vtkActor, VTK_MAJOR_VERSION
)



def show_map(dane, kontrolki):

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

    #Warszawa
    if kontrolki[0]==True:
        ind00 = vtk.vtkTextSource()
        ind00.SetText(str(dane[13][1]))
        ind00.SetBackgroundColor(1, 0, 0)
        ind00.BackingOn()
        ind00.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind00.GetOutputPort())
        indActor01 = vtk.vtkActor()
        indActor01.SetMapper(textMapper)
        indActor01.SetScale(1)
        indActor01.SetPosition(420, 260, 0.0)
        renderer.AddActor(indActor01)

    if kontrolki[1]==True:
        ind01 = vtk.vtkCubeSource()
        ind01.SetXLength(20)
        ind01.SetYLength(20)
        ind01.SetZLength(50*dane[13][2])
        ind01.SetCenter(400, 265, 0.0)
        indMapper01 = vtk.vtkPolyDataMapper()
        indMapper01.SetInputConnection(ind01.GetOutputPort())
        indActor01 = vtk.vtkActor()
        indActor01.GetProperty().SetColor(0, 0, 255)
        indActor01.SetMapper(indMapper01)
        renderer.AddActor(indActor01)


    #szczecin
    if kontrolki[0]==True:
        ind10 = vtk.vtkTextSource()
        ind10.SetText(str(dane[12][1]))
        ind10.SetBackgroundColor(1, 0, 0)
        ind10.BackingOn()
        ind10.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind10.GetOutputPort())
        indActor10 = vtk.vtkActor()
        indActor10.SetMapper(textMapper)
        indActor10.SetScale(1)
        indActor10.SetPosition(130, 390, 0.0)
        renderer.AddActor(indActor10)

    if kontrolki[1]==True:
        ind11 = vtk.vtkCubeSource()
        ind11.SetXLength(20)
        ind11.SetYLength(20)
        ind11.SetZLength(50*dane[12][2])
        ind11.SetCenter(110, 395, 0.0)
        indMapper01 = vtk.vtkPolyDataMapper()
        indMapper01.SetInputConnection(ind11.GetOutputPort())
        indActor11 = vtk.vtkActor()
        indActor11.GetProperty().SetColor(0, 0, 255)
        indActor11.SetMapper(indMapper01)
        renderer.AddActor(indActor11)

    #gorzow wlkp
    if kontrolki[0]==True:
        ind20 = vtk.vtkTextSource()
        ind20.SetText(str(dane[9][1]))
        ind20.SetBackgroundColor(1, 0, 0)
        ind20.BackingOn()
        ind20.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind20.GetOutputPort())
        indActor20 = vtk.vtkActor()
        indActor20.SetMapper(textMapper)
        indActor20.SetScale(1)
        indActor20.SetPosition(130, 320, 0.0)
        renderer.AddActor(indActor20)

    if kontrolki[1]==True:
        ind21 = vtk.vtkCubeSource()
        ind21.SetXLength(20)
        ind21.SetYLength(20)
        ind21.SetZLength(50*dane[9][2])
        ind21.SetCenter(110, 320, 0.0)
        indMapper21 = vtk.vtkPolyDataMapper()
        indMapper21.SetInputConnection(ind21.GetOutputPort())
        indActor21 = vtk.vtkActor()
        indActor21.GetProperty().SetColor(0, 0, 255)
        indActor21.SetMapper(indMapper21)
        renderer.AddActor(indActor21)



    #zielona gora
    if kontrolki[0]==True:
        ind30 = vtk.vtkTextSource()
        ind30.SetText(str(dane[15][1]))
        ind30.SetBackgroundColor(1, 0, 0)
        ind30.BackingOn()
        ind30.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind30.GetOutputPort())
        indActor30 = vtk.vtkActor()
        indActor30.SetMapper(textMapper)
        indActor30.SetScale(1)
        indActor30.SetPosition(130, 250, 0.0)
        renderer.AddActor(indActor30)

    if kontrolki[1]==True:
        ind31 = vtk.vtkCubeSource()
        ind31.SetXLength(20)
        ind31.SetYLength(20)
        ind31.SetZLength(50*dane[15][2])
        ind31.SetCenter(110, 250, 0.0)
        indMapper31 = vtk.vtkPolyDataMapper()
        indMapper31.SetInputConnection(ind31.GetOutputPort())
        indActor31 = vtk.vtkActor()
        indActor31.GetProperty().SetColor(0, 0, 255)
        indActor31.SetMapper(indMapper31)
        renderer.AddActor(indActor31)


    #Gdansk
    if kontrolki[0]==True:
        ind40 = vtk.vtkTextSource()
        ind40.SetText(str(dane[2][1]))
        ind40.SetBackgroundColor(1, 0, 0)
        ind40.BackingOn()
        ind40.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind40.GetOutputPort())
        indActor40 = vtk.vtkActor()
        indActor40.SetMapper(textMapper)
        indActor40.SetScale(1)
        indActor40.SetPosition(290, 430, 0.0)
        renderer.AddActor(indActor40)

    if kontrolki[1]==True:
        ind41 = vtk.vtkCubeSource()
        ind41.SetXLength(20)
        ind41.SetYLength(20)
        ind41.SetZLength(dane[2][2]*50)
        ind41.SetCenter(270, 430, 0.0)
        indMapper41 = vtk.vtkPolyDataMapper()
        indMapper41.SetInputConnection(ind41.GetOutputPort())
        indActor41 = vtk.vtkActor()
        indActor41.GetProperty().SetColor(0, 0, 255)
        indActor41.SetMapper(indMapper41)
        renderer.AddActor(indActor41)


    #poznan
    if kontrolki[0]==True:
        ind50 = vtk.vtkTextSource()
        ind50.SetText(str(dane[10][1]))
        ind50.SetBackgroundColor(1, 0, 0)
        ind50.BackingOn()
        ind50.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind50.GetOutputPort())
        indActor50 = vtk.vtkActor()
        indActor50.SetMapper(textMapper)
        indActor50.SetScale(1)
        indActor50.SetPosition(300, 290, 0.0)
        renderer.AddActor(indActor50)

    if kontrolki[1]==True:
        ind51 = vtk.vtkCubeSource()
        ind51.SetXLength(20)
        ind51.SetYLength(20)
        ind51.SetZLength(50*dane[10][2])
        ind51.SetCenter(290, 290, 0.0)
        indMapper51 = vtk.vtkPolyDataMapper()
        indMapper51.SetInputConnection(ind51.GetOutputPort())
        indActor51 = vtk.vtkActor()
        indActor51.GetProperty().SetColor(0, 0, 255)
        indActor51.SetMapper(indMapper51)
        renderer.AddActor(indActor51)


    #bydgoszcz
    if kontrolki[0]==True:
        ind60 = vtk.vtkTextSource()
        ind60.SetText(str(dane[1][1]))
        ind60.SetBackgroundColor(1, 0, 0)
        ind60.BackingOn()
        ind60.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind60.GetOutputPort())
        indActor60 = vtk.vtkActor()
        indActor60.SetMapper(textMapper)
        indActor60.SetScale(1)
        indActor60.SetPosition(270, 370, 0.0)
        renderer.AddActor(indActor60)

    if kontrolki[1]==True:
        ind61 = vtk.vtkCubeSource()
        ind61.SetXLength(20)
        ind61.SetYLength(20)
        ind61.SetZLength(50*dane[1][2])
        ind61.SetCenter(260, 370, 0.0)
        indMapper61 = vtk.vtkPolyDataMapper()
        indMapper61.SetInputConnection(ind61.GetOutputPort())
        indActor61 = vtk.vtkActor()
        indActor61.GetProperty().SetColor(0, 0, 255)
        indActor61.SetMapper(indMapper61)
        renderer.AddActor(indActor61)

    #olsztyn
    if kontrolki[0]==True:
        ind70 = vtk.vtkTextSource()
        ind70.SetText(str(dane[8][1]))
        ind70.SetBackgroundColor(1, 0, 0)
        ind70.BackingOn()
        ind70.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind70.GetOutputPort())
        indActor70 = vtk.vtkActor()
        indActor70.SetMapper(textMapper)
        indActor70.SetScale(1)
        indActor70.SetPosition(390, 360, 0.0)
        renderer.AddActor(indActor70)

    if kontrolki[1]==True:
        ind71 = vtk.vtkCubeSource()
        ind71.SetXLength(20)
        ind71.SetYLength(20)
        ind71.SetZLength(50*dane[8][2])
        ind71.SetCenter(380, 360, 0.0)
        indMapper71 = vtk.vtkPolyDataMapper()
        indMapper71.SetInputConnection(ind71.GetOutputPort())
        indActor71 = vtk.vtkActor()
        indActor71.GetProperty().SetColor(0, 0, 255)
        indActor71.SetMapper(indMapper71)
        renderer.AddActor(indActor71)



    #bialystok
    if kontrolki[0]==True:
        ind80 = vtk.vtkTextSource()
        ind80.SetText(str(dane[0][1]))
        ind80.SetBackgroundColor(1, 0, 0)
        ind80.BackingOn()
        ind80.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind80.GetOutputPort())
        indActor80 = vtk.vtkActor()
        indActor80.SetMapper(textMapper)
        indActor80.SetScale(1)
        indActor80.SetPosition(510, 315, 0.0)
        renderer.AddActor(indActor80)

    if kontrolki[1]==True:
        ind81 = vtk.vtkCubeSource()
        ind81.SetXLength(20)
        ind81.SetYLength(20)
        ind81.SetZLength(dane[0][1]*50)
        ind81.SetCenter(500, 315, 0.0)
        indMapper81 = vtk.vtkPolyDataMapper()
        indMapper81.SetInputConnection(ind81.GetOutputPort())
        indActor81 = vtk.vtkActor()
        indActor81.GetProperty().SetColor(0, 0, 255)
        indActor81.SetMapper(indMapper81)
        renderer.AddActor(indActor81)


    #suwalki
    if kontrolki[0]==True:
        ind90 = vtk.vtkTextSource()
        ind90.SetText(str(dane[4][1]))
        ind90.SetBackgroundColor(1, 0, 0)
        ind90.BackingOn()
        ind90.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind90.GetOutputPort())
        indActor90 = vtk.vtkActor()
        indActor90.SetMapper(textMapper)
        indActor90.SetScale(1)
        indActor90.SetPosition(485, 395, 0.0)
        renderer.AddActor(indActor90)

    if kontrolki[1]==True:
        ind91 = vtk.vtkCubeSource()
        ind91.SetXLength(20)
        ind91.SetYLength(20)
        ind91.SetZLength(50*dane[4][2])
        ind91.SetCenter(475, 395, 0.0)
        indMapper91 = vtk.vtkPolyDataMapper()
        indMapper91.SetInputConnection(ind91.GetOutputPort())
        indActor91 = vtk.vtkActor()
        indActor91.GetProperty().SetColor(0, 0, 255)
        indActor91.SetMapper(indMapper91)
        renderer.AddActor(indActor91)


    #wroclaw
    if kontrolki[0]==True:
        ind100 = vtk.vtkTextSource()
        ind100.SetText(str(dane[14][1]))
        ind100.SetBackgroundColor(1, 0, 0)
        ind100.BackingOn()
        ind100.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind100.GetOutputPort())
        indActor100 = vtk.vtkActor()
        indActor100.SetMapper(textMapper)
        indActor100.SetScale(1)
        indActor100.SetPosition(210, 175, 0.0)
        renderer.AddActor(indActor100)

    if kontrolki[1]==True:
        ind101 = vtk.vtkCubeSource()
        ind101.SetXLength(20)
        ind101.SetYLength(20)
        ind101.SetZLength(50*dane[14][2])
        ind101.SetCenter(200, 180, 0.0)
        indMapper101 = vtk.vtkPolyDataMapper()
        indMapper101.SetInputConnection(ind101.GetOutputPort())
        indActor101 = vtk.vtkActor()
        indActor101.GetProperty().SetColor(0, 0, 255)
        indActor101.SetMapper(indMapper101)
        renderer.AddActor(indActor101)


    #lodz
    if kontrolki[0]==True:
        ind110 = vtk.vtkTextSource()
        ind110.SetText(str(dane[7][1]))
        ind110.SetBackgroundColor(1, 0, 0)
        ind110.BackingOn()
        ind110.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind110.GetOutputPort())
        indActor110 = vtk.vtkActor()
        indActor110.SetMapper(textMapper)
        indActor110.SetScale(1)
        indActor110.SetPosition(345, 195, 0.0)
        renderer.AddActor(indActor110)

    if kontrolki[1]==True:
        ind111 = vtk.vtkCubeSource()
        ind111.SetXLength(20)
        ind111.SetYLength(20)
        ind111.SetZLength(50*dane[7][2])
        ind111.SetCenter(335, 200, 0.0)
        indMapper111 = vtk.vtkPolyDataMapper()
        indMapper111.SetInputConnection(ind111.GetOutputPort())
        indActor111 = vtk.vtkActor()
        indActor111.GetProperty().SetColor(0, 0, 255)
        indActor111.SetMapper(indMapper111)
        renderer.AddActor(indActor111)



    #krakow
    if kontrolki[0]==True:
        ind120 = vtk.vtkTextSource()
        ind120.SetText(str(dane[5][1]))
        ind120.SetBackgroundColor(1, 0, 0)
        ind120.BackingOn()
        ind120.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind120.GetOutputPort())
        indActor120 = vtk.vtkActor()
        indActor120.SetMapper(textMapper)
        indActor120.SetScale(1)
        indActor120.SetPosition(400, 95, 0.0)
        renderer.AddActor(indActor120)

    if kontrolki[1]==True:
        ind121 = vtk.vtkCubeSource()
        ind121.SetXLength(20)
        ind121.SetYLength(20)
        ind121.SetZLength(50*dane[5][2])
        ind121.SetCenter(390, 95, 0.0)
        indMapper121 = vtk.vtkPolyDataMapper()
        indMapper121.SetInputConnection(ind121.GetOutputPort())
        indActor121 = vtk.vtkActor()
        indActor121.GetProperty().SetColor(0, 0, 255)
        indActor121.SetMapper(indMapper121)
        renderer.AddActor(indActor121)

    #rzeszow
    if kontrolki[0]==True:
        ind130 = vtk.vtkTextSource()
        ind130.SetText(str(dane[11][1]))
        ind130.SetBackgroundColor(1, 0, 0)
        ind130.BackingOn()
        ind130.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind130.GetOutputPort())
        indActor130 = vtk.vtkActor()
        indActor130.SetMapper(textMapper)
        indActor130.SetScale(1)
        indActor130.SetPosition(500, 90, 0.0)
        renderer.AddActor(indActor130)

    if kontrolki[1]==True:
        ind131 = vtk.vtkCubeSource()
        ind131.SetXLength(20)
        ind131.SetYLength(20)
        ind131.SetZLength(50*dane[11][2])
        ind131.SetCenter(480, 95, 0.0)
        indMapper131 = vtk.vtkPolyDataMapper()
        indMapper131.SetInputConnection(ind131.GetOutputPort())
        indActor131 = vtk.vtkActor()
        indActor131.GetProperty().SetColor(0, 0, 255)
        indActor131.SetMapper(indMapper131)
        renderer.AddActor(indActor131)

    #lublin
    if kontrolki[0]==True:
        ind140 = vtk.vtkTextSource()
        ind140.SetText(str(dane[6][1]))
        ind140.SetBackgroundColor(1, 0, 0)
        ind140.BackingOn()
        ind140.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind140.GetOutputPort())
        indActor140 = vtk.vtkActor()
        indActor140.SetMapper(textMapper)
        indActor140.SetScale(1)
        indActor140.SetPosition(500,190, 0.0)
        renderer.AddActor(indActor140)

    if kontrolki[1]==True:
        ind141 = vtk.vtkCubeSource()
        ind141.SetXLength(20)
        ind141.SetYLength(20)
        ind141.SetZLength(50*dane[6][2])
        ind141.SetCenter(490,190, 0.0)
        indMapper141 = vtk.vtkPolyDataMapper()
        indMapper141.SetInputConnection(ind141.GetOutputPort())
        indActor141 = vtk.vtkActor()
        indActor141.GetProperty().SetColor(0, 0, 255)
        indActor141.SetMapper(indMapper141)
        renderer.AddActor(indActor141)


    #katowice
    if kontrolki[0]==True:
        ind150 = vtk.vtkTextSource()
        ind150.SetText(str(dane[3][1]))
        ind150.SetBackgroundColor(1, 0, 0)
        ind150.BackingOn()
        ind150.Update()
        textMapper = vtk.vtkPolyDataMapper()
        textMapper.SetInputConnection(ind150.GetOutputPort())
        indActor150 = vtk.vtkActor()
        indActor150.SetMapper(textMapper)
        indActor150.SetScale(1)
        indActor150.SetPosition(320, 120, 0.0)
        renderer.AddActor(indActor150)

    if kontrolki[1]==True:
        ind151 = vtk.vtkCubeSource()
        ind151.SetXLength(20)
        ind151.SetYLength(20)
        ind151.SetZLength(50*dane[3][2])
        ind151.SetCenter(310, 130, 0.0)
        indMapper151 = vtk.vtkPolyDataMapper()
        indMapper151.SetInputConnection(ind151.GetOutputPort())
        indActor151 = vtk.vtkActor()
        indActor151.GetProperty().SetColor(0, 0, 255)
        indActor151.SetMapper(indMapper151)
        renderer.AddActor(indActor151)

    ####################################################################################################################
    interactor = iren.GetRenderWindow().GetInteractor()
    interactor.Initialize()
    interactor.Start()
    return iren


