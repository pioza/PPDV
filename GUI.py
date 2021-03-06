import sys
import vtk
import datetime
import PyQt5
from PyQt5.QtWidgets import *
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from d2_gen import DiagramGenerator
from map import show_map


class Window(QWidget):
    def __init__(self, layout, parent=None):
        QWidget.__init__(self, parent)

        self.fc = None
        self.gen2d = DiagramGenerator()
        self.gen2d.read_data()



        label1 = QLabel("Choose date:")
        layout.addWidget(label1, 0, 0, 1, 1)

        self.date_list = QListWidget()
        day_list = []
        today = self.gen2d.data['Poznan'][0][0]

        for i in range(16):
            day = today + datetime.timedelta(hours=i * 3)
            day_list.append('%s-%s-%s at %s.00' % (day.day, day.month, day.year, day.hour))

        self.date_list.addItems(day_list)
        layout.addWidget(self.date_list, 0, 1, 1, 2)
        self.date_list.setCurrentRow(0)



        self.city_list = QListWidget()
        self.city_list.addItems(
            ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz', 'Olsztyn', 'Opole',
             'Poznan', 'Rzeszow', 'Szczecin', 'Warszawa', 'Wroclaw', 'Zielona Gora'])
        layout.addWidget(self.city_list, 0, 5, 1, 2)
        self.city_list.setCurrentRow(0)

        label2 = QLabel("Choose city:")
        layout.addWidget(label2, 0, 4, 1, 1)



        self.show_diagrams()

        self.temp_chbox = QCheckBox("Temperature")
        self.rain_chbox = QCheckBox("Rainfall")
        # self.pres_chbox = QCheckBox("Pressure")
        # self.wind_chbox = QCheckBox("Wind")
        # self.clou_chbox = QCheckBox("Cloudiness")

        self.temp_chbox.setChecked(True)
        self.temp_chbox.stateChanged.connect(self.change_chbox)
        layout.addWidget(self.temp_chbox, 0, 7, 1, 1)

        self.rain_chbox.setChecked(True)
        self.rain_chbox.stateChanged.connect(self.change_chbox)
        layout.addWidget(self.rain_chbox, 0, 8, 1, 1)

        # self.pres_chbox.setChecked(True)
        # self.pres_chbox.stateChanged.connect(self.change_chbox)
        # layout.addWidget(self.pres_chbox, 0, 7, 1, 1)
        #
        # self.wind_chbox.setChecked(True)
        # self.wind_chbox.stateChanged.connect(self.change_chbox)
        # layout.addWidget(self.wind_chbox, 0, 8, 1, 1)
        #
        # self.clou_chbox.setChecked(True)
        # self.clou_chbox.stateChanged.connect(self.change_chbox)
        # layout.addWidget(self.clou_chbox, 0, 9, 1, 1)
        self.date_list.itemClicked.connect(self.change_chbox)
        self.city_list.itemClicked.connect(self.show_diagrams)


        self.change_chbox()

    def show_diagrams(self):


        place = str(self.city_list.currentItem().text())

        self.diag_figure = DiagramGenerator.draw_diagram(self.gen2d, place)
        self.canvas = FigureCanvasQTAgg(self.diag_figure)
        self.canvas.setFixedWidth(700)
        self.canvas.setFixedHeight(476*1.75)

        layout.addWidget(self.canvas, 2, 0, 4, 4)

    def get_data(self):
        time = str(self.date_list.currentItem().text())
        date = time.split()[0].split('-')
        ch_time = datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(float(time.split()[2])))

        to_show = []
        for city in ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz', 'Olsztyn', 'Opole',
             'Poznan', 'Rzeszow', 'Szczecin', 'Warszawa', 'Wroclaw', 'Zielona Gora']:
            index = self.gen2d.data[city][0].index(ch_time)
            to_show.append([city, int(self.gen2d.data[city][1][index]), int(self.gen2d.data[city][6][index])])

        return to_show


    def change_chbox(self):
        controls = []

        # if self.clou_chbox.isChecked():
        #     controls.append(True)
        # else:
        #     controls.append(False)

        if self.temp_chbox.isChecked():
            controls.append(True)
        else:
            controls.append(False)

        # if self.wind_chbox.isChecked():
        #     controls.append(True)
        # else:
        #     controls.append(False)

        # if self.pres_chbox.isChecked():
        #     controls.append(True)
        # else:
        #     controls.append(False)
        #
        if self.rain_chbox.isChecked():
            controls.append(True)
        else:
            controls.append(False)
        #
        #TO ZMIEN GDY ZROBISZ WCZYTYWANIE DANYCH
        #
        self.vtkWidget = show_map(self.get_data(), controls)
        #self.vtkWidget = show_map()
        self.vtkWidget.setFixedWidth(636 * 1.75)
        self.vtkWidget.setFixedHeight(476 * 1.75)
        layout.addWidget(self.vtkWidget, 2, 4, 4, 5)


app = QApplication(sys.argv)

layout = QGridLayout()
mainWindow = Window(layout)
win = QWidget()
# win.setFixedHeight(500)
# win.setFixedWidth(1300)
win.setLayout(layout)
win.setWindowTitle("Weather Forecast")
win.show()

app.exec_()
