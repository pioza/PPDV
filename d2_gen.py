import json
from datetime import datetime
from collections import defaultdict
from matplotlib.figure import Figure


class DiagramGenerator:
    def __init__(self):
        self.city = ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz', 'Olsztyn',
                     'Opole',
                     'Poznan', 'Rzeszow', 'Szczecin', 'Warszawa', 'Wroclaw', 'Zielona Gora']
        self.data = defaultdict(list)

    def read_data(self):
        for c in self.city:
            self.data[c].append([])
            self.data[c].append([])
            self.data[c].append([])
            self.data[c].append([])
            self.data[c].append([])
            self.data[c].append([])
            self.data[c].append([])
            self.data[c].append([])
            with open(c + '.json') as f:
                d = json.load(f)
                i = 0
                for point in d["list"]:
                    if i == 16:
                        break
                    i = i + 1
                    self.data[c][0].append(datetime.utcfromtimestamp(point['dt']))
                    self.data[c][1].append(float(point['main']['temp']) - 273.15)
                    self.data[c][2].append(float(point['main']['temp_max']) - 273.15)
                    self.data[c][3].append(float(point['main']['temp_min']) - 273.15)
                    self.data[c][4].append(float(point['main']['pressure']))
                    self.data[c][5].append(float(point['wind']['speed']))
                    try:
                        self.data[c][6].append(float(point['rain']['3h']))

                    except Exception:
                        try:
                            self.data[c][6].append(float(point['snow']['3h']))

                        except Exception:
                            self.data[c][6].append(0)
                    self.data[c][7].append(float(point['clouds']['all']))

    def draw_diagram(self, city):
        diag_fig = Figure()
        # hours = []
        # h = self.data[city][0][0].hour
        # for i in range(16):
        #    hours.append((h + 3*i) % 24)
        # print(hours)
        temp_x = diag_fig.add_subplot(611)
        temp_x.clear()
        temp_x.set_ylabel('Temp\n')
        temp_x.plot(self.data[city][0], self.data[city][1], color='red', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        temp_x.grid()
        temp_x.get_xaxis().set_ticklabels([])

        temp_x = diag_fig.add_subplot(612)
        temp_x.clear()
        temp_x.set_ylabel('Pressure\n')
        temp_x.plot(self.data[city][0], self.data[city][4], color='orange', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        temp_x.grid()
        temp_x.get_xaxis().set_ticklabels([])

        temp_x = diag_fig.add_subplot(613)
        temp_x.clear()
        temp_x.set_ylabel('Wind\n')
        temp_x.plot(self.data[city][0], self.data[city][5], color='green', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        temp_x.grid()
        temp_x.get_xaxis().set_ticklabels([])

        temp_x = diag_fig.add_subplot(614)
        temp_x.clear()
        temp_x.set_ylabel('Rainfall\n')
        temp_x.plot(self.data[city][0], self.data[city][6], color='blue', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        temp_x.grid()
        temp_x.get_xaxis().set_ticklabels([])

        temp_x = diag_fig.add_subplot(615)
        temp_x.clear()
        temp_x.set_ylabel('Clouds\n')
        temp_x.plot(self.data[city][0], self.data[city][7], color='grey', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        temp_x.grid()
        temp_x.get_xaxis().set_ticklabels([])

        return diag_fig


mp = DiagramGenerator()
mp.read_data()
