import json
from datetime import datetime
from collections import defaultdict
from matplotlib.figure import Figure


class DiagramGenerator:
    def __init__(self):
        self.city = ['Bialystok', 'Bydgoszcz', 'Gdansk', 'Katowice', 'Kielce', 'Krakow', 'Lublin', 'Lodz', 'Olsztyn',
                     'Opole', 'Poznan', 'Rzeszow', 'Szczecin', 'Warszawa', 'Wroclaw', 'Zielona Gora']
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
        temp_x = diag_fig.add_subplot(511)
        temp_x.clear()
        temp_x.set_ylabel('Temperature\n')
        #temp_x.plot(self.data[city][0], self.data[city][1], color='yellow', marker='.', linestyle='dashed', linewidth=1,
         #           markersize=5)
        temp_x.plot(self.data[city][0], self.data[city][2], color='red', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        temp_x.plot(self.data[city][0], self.data[city][3], color='cyan', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        temp_x.grid()
        temp_x.get_xaxis().set_ticklabels([])


        pres_x = diag_fig.add_subplot(512)
        pres_x.clear()
        pres_x.set_ylabel('Pressure\n')
        pres_x.plot(self.data[city][0], self.data[city][4], color='orange', marker='.', linestyle='dashed', linewidth=1,
                    markersize=5)
        pres_x.grid()
        pres_x.get_xaxis().set_ticklabels([])

        wind_x = diag_fig.add_subplot(513)
        wind_x.clear()
        wind_x.set_ylabel('Wind\n')
        wind_x.bar(self.data[city][0], self.data[city][5], color='green', width=0.025, align='center')
        wind_x.grid()
        wind_x.get_xaxis().set_ticklabels([])

        rain_x = diag_fig.add_subplot(514)
        rain_x.clear()
        rain_x.set_ylabel('Downfall\n')
        rain_x.bar(self.data[city][0], self.data[city][6], color='blue', width=0.025, align='center')
        rain_x.grid()
        rain_x.get_xaxis().set_ticklabels([])

        clou_x = diag_fig.add_subplot(515)
        clou_x.clear()
        clou_x.set_ylabel('Clouds\n')
        clou_x.bar(self.data[city][0], self.data[city][7], color='grey', width=0.025, align='center')
        for tick in clou_x.get_xticklabels():
            tick.set_rotation(60)
            #new_tick = tick.get_text() + '.00'
            #print(str(tick.get_text()))
            #tick.set_text(new_tick)
        diag_fig.set_tight_layout(True)

        return diag_fig


mp = DiagramGenerator()
mp.read_data()
