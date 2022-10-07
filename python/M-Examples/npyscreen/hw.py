import npyscreen

# This application class serves as a wrapper for the initialization of curses
# and also manages the actual forms of the application

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

# This form class defines the display that will be presented to the user.

class MainForm(npyscreen.Form):
    def create(self):
        y, x = self.useable_space()
        self.add(npyscreen.TitleDateCombo, name="Date:", max_width=x // 2)
        self.add(npyscreen.TitleMultiSelect, relx=x // 2 + 1, rely=2, value=[1, 2], name="Pick Several", values=["Option1", "Option2", "Option3"], scroll_exit=True)
        # You can use the negative coordinates
        self.add(npyscreen.TitleFilename, name="Filename:", rely=-5)
    def afterEditing(self):
        self.parentApp.setNextForm(None)

if __name__ == '__main__':
    TA = MyTestApp()
    TA.run()
