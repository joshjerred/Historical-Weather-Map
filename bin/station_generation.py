import urllib.request
import time
import sqlite3
import sys 
import os

def download_station_list(er = 0):
    try:
        print("Download stated of: ghcnd-stations.txt")
        f = urllib.request.urlopen("ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt", timeout=120)
        f = f.read()
        with open('./data/station_list/stations.txt', 'wb') as file:
            file.write(f)
        print("Download complete")
        return "Download and write complete."
        
    except:
        if er == 0:
            print("Error, trying again in 5 seconds.")
            time.sleep(5)
            try_again = download_station_list(1)
            if try_again == False:
                print("Error again, exiting.")
                return "Unable to download"
            else:
                return try_again
        elif er == 1:
            return False

def pull_info(region):
    if not os.path.exists("./data/station_list/stations.txt"):
        return "File does not exist. Please download."
    fulllist = []
    f = open('./data/station_list/stations.txt', 'r') 
    lines = f.readlines() 
    for line in lines: 
        if line[0:3] == region: #line[0:3] == "USW" # Use this for US stations only
            short = [line[0:11], line[12:21], line[21:30], line[31:37], line[38:40], line[41:72]]
            for item in enumerate(short):
                short[item[0]] = item[1].strip()
            fulllist.append(short)
    return fulllist
 

def generate_table(fulllist): # Format: [ID, LAT, LON, ELEV, STATE, NAME]
    conn = sqlite3.connect('./data/station_list.db')
    c = conn.cursor()
    createtable = '''CREATE TABLE IF NOT EXISTS stations (
        id TEXT,
        lat REAL,
        lon REAL,
        elev REAL,
        state TEXT,
        name TEXT
    )'''
    c.execute(createtable)

    for x in fulllist:
        print(x)
        c.execute('''INSERT INTO stations(id, lat, lon, elev, state, name) VALUES(?, ?, ?, ?, ?, ?)''', x)

    conn.commit()
    conn.close()
    return len(fulllist)

def build_database(region):
    if not os.path.exists("./data/station_list/stations.txt"):
        os.system('clear')
        print("Please download the station list.")
        time.sleep(3)
        os.system('clear')
        return False
    if os.path.exists("./data/station_list.db"):
        os.system('clear')
        print("Database already exists, please delete or backup and delete.")
        time.sleep(3)
        os.system('clear')
        return False
    if len(region) == 3:
        print("Building stations for: " + region)
        x_station = generate_table(pull_info(region))
        os.system('clear')
        print("Built a list of " + str(x_station) + " stations.")
        time.sleep(2)
    elif region == "":
        os.system('clear')
        print("Please select a region!")
        time.sleep(1)
        os.system('clear')
    else:
        print("'" + region + "' is not an acceptable country code" )

def select_region():
    while True:
        os.system('clear')
        region = input("Enter: ").upper()
        if len(region) == 3:
            return region
        else:
            print("Please try again.")
            time.sleep(1)
            os.system('clear')

def delete_db():
    try:
        os.remove("./data/station_list.db")
        return "Database deleted."
    except:
        return("File either does not exist yet or there was an error.")

def check_db():
    if os.path.exists("./data/station_list.db"):
        try:
            conn = sqlite3.connect('./data/station_list.db')
            c = conn.cursor()
            c.execute("SELECT * FROM stations")
            rows = c.fetchall()
            m = 0
            for row in rows:
                m += 1
            conn.close()
            return str(m) + " stations in the database"
        except:
            return "There is nothing in the database"
    else:
        return "Database does not exist"

#def menu():
#    os.system('clear')
#    region = ""
#    while True:
#        option = ""
#        print("""
#        Please select an option:
#        [D] Download Station List
#        [R] Select Region
#        [B] Build and Station Database
#        [X] Delete Database
#        [H] Help
#        [E] Exit
#        """)
#        option = input("Please type a letter and press enter to select an option: ").strip().upper()
#        if option == "D":
#            os.system('clear')
#            download_station_list()
#            time.sleep(2)
#            os.system('clear')
#        elif option == "R":
#            region = select_region()
#            os.system('clear')
#            print("You selected: " + region)
#            time.sleep(2)
#            os.system('clear')
#        elif option == "B":
#            build_database(region)
#        elif option == "X":
#            delete_db()
#        elif option == "H":
#            pass
#        elif option == "E":
#            os.system('clear')
#            sys.exit("EXITING")
#        else:
#            print("That is not an option.")


if __name__ == "__main__":
    menu()