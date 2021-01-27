from tkinter import *
import station_generation as st
import map_generation as Map
import time


class GUI:
    def __init__(self):
        self.__mainWindow = Tk()


        self.__mainWindow.title("Generate Database")
        self.__mainWindow.resizable(height = False, width = False)


        # Variables
        network_code_var = StringVar(self.__mainWindow)
        network_code_var.set("Select One")

        # Buttons/Dropdowns/Textboxes setup
            # Row 0
        guide_country = Label(self.__mainWindow, text = "Two Letter\nCountry Code")
        guide_network = Label(self.__mainWindow, text = "Select a\nNetwork Code")
        guide_generate = Label(self.__mainWindow, text = "Click to\ntest")
            # Row 1
        country_code = Text(self.__mainWindow, height = 1, width = 4) 
        network_code = OptionMenu(self.__mainWindow, network_code_var, "Select One","0", "1", "C", "E", "M", "N", "R", "S", "W")
        test_button = Button(text = "Test", command = lambda: test_db(country_code.get("1.0","end-1c").upper(), network_code_var.get()))
            # Row 2
        action_menu = Label(self.__mainWindow, text = "Click test to check for\nstations with different settings")
            # Row 3

            # Row 4
        delete_database = Button(text = "Delete DB", command = lambda: delete())
        check_database = Button(text = "Check DB", command = lambda: check())
        build_database = Button(text = "Build DB", command = lambda: build(country_code.get("1.0","end-1c").upper(), network_code_var.get()))
            # Row 5
        build_map = Button(text = "Generate Map", command = lambda: open_map())
        download_button = Button(text = "Download List", command = lambda: download())
        help_button = Button(text = "Help", command = lambda: help_interface())


        # GUI item location setup
            # Row 0
        guide_country.grid(row = 0, column = 1)
        guide_network.grid(row = 0, column = 2)
        guide_generate.grid(row = 0, column = 3)
            # Row 1
        country_code.grid(row = 1, column = 1)
        network_code.grid(row = 1, column = 2)
        test_button.grid(row = 1, column = 3)

        country_code.configure(width = 10)
        network_code.configure(width = 10)
        test_button.configure(width = 10)
            # Row 3
        action_menu.grid(row = 2, column = 1, columnspan = 3)
            # Row 4
        delete_database.grid(row = 3, column = 1)
        check_database.grid(row = 3, column = 2)
        build_database.grid(row = 3, column = 3)

        delete_database.configure(width = 10)
        check_database.configure(width = 10)
        build_database.configure(width = 10)
            # Row 5
        build_map.grid(row = 4, column = 1)
        download_button.grid(row = 4, column = 2)
        help_button.grid(row = 4, column = 3)

        build_map.configure(width = 10)
        download_button.configure(width = 10)
        help_button.configure(width = 10)

        def test_db(country, network):
            action_menu['text'] = ("These settings have " + str(len(st.pull_info(country + network))) + " stations")

        def delete():
            action_menu['text'] = (st.delete_db())

        def check():
            action_menu['text'] = (st.check_db())

        def build(country, network):
            action_menu['text'] = (str(st.generate_table(st.pull_info(country + network))) + " stations added to database." )

        def open_map():
            Map.main()

        def help_interface():
            print("tmp help")

        def download():
            action_menu['text'] = ("Download started")
            action_menu['text'] = (st.download_station_list())

        mainloop()




    

if __name__ == '__main__':
    GUI = GUI()
