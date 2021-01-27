import folium
import sqlite3
import webbrowser
import os

class map:

    def createmap(self, start_coords, zoom):
        print("create map")
        self.m = folium.Map(location=start_coords, zoom_start=zoom)

    def create_station(self, m, db):
        print("create station")
        folium.Circle(
        radius=5000,
        location=[db[1], db[2]],
        popup=db[5],
        icon=folium.Icon(icon="cloud"),
        color="crimson",
        fill=True,
        fill_color="#3186cc",
        ).add_to(self.m)

    def pull_from_db(self, m):
        print("pull from db")
        conn = sqlite3.connect('./data/station_list.db')
        c = conn.cursor()
        c.execute("SELECT * FROM stations")
        rows = c.fetchall()
        for row in rows:
            self.create_station(m, row)
        conn.close()

    def open():
        print("open")
        new = 2
        url = os.path.abspath("./data/index.html")
        webbrowser.open(url,new=new)

    def __init__(self):
        print("testing")
        self.createmap([39.538, -97.251], 5)
        self.pull_from_db(self)
        self.m.save("./data/index.html")

map()