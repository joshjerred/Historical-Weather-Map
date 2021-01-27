import folium
import sqlite3
import webbrowser
import os


def createmap(start_coords, zoom):
    m = folium.Map(location=start_coords, zoom_start=zoom)
    return m

def create_station(m, db):
    folium.Circle(
    radius=5000,
    location=[db[1], db[2]],
    popup=db[5],
    icon=folium.Icon(icon="cloud"),
    color="crimson",
    fill=True,
    fill_color="#3186cc",
    ).add_to(m)
    return m

def pull_from_db(m):
    conn = sqlite3.connect('./data/station_list.db')
    c = conn.cursor()
    c.execute("SELECT * FROM stations")
    rows = c.fetchall()
    for row in rows:
        create_station(m, row)
    conn.close()
    return m

def main():
    m = createmap([39.538, -97.251], 5)
    m = pull_from_db(m)
    m.save("./data/index.html")
    new = 2
    url = os.path.abspath("./data/index.html")
    webbrowser.open(url,new=new)



if __name__ == "__main__":
    m = createmap([39.538, -97.251], 5)
    m = pull_from_db(m)
    m.save("index.html")
