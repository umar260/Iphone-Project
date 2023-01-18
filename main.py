import sys
# function to open the phone using a pin
class IPhone:
    def __init__(self, pin):
        self.pin = pin
        self.locked = True
        self.apps = ['Messages', 'Camera', 'Music']

    def open(self, usrinput):
      if self.pin == int(usrinput):
        self.locked = False
        print("iphone unlocked")
      else:
        print("incorrect pin")

# function to lock the phone
    def close(self):
     self.locked = True
     print("iphone locked")

# function to open an app on the phone
    def openiphoneapp(self, appname):
     if not self.locked: # check if the phone is locked
        if appname in self.apps: # check if the app is installed on the phone

            if appname == "Camera":
                self.camera = CameraApp()
                self.camera.open()

            elif appname == "Music":
                self.music = MusicApp()
                self.music.open()
                
            elif appname == "Messages":
                self.messages = MessagesApp()
                self.messages.open()
        else:
            print(f"{appname} is not installed on this iphone")
     else:
        print("your iPhone is locked enter the correct pin to unlock.")


    def menuforinstalledapps(self):
        print("select the app you want to open: ")
        print("1 camera")
        print("2 music")
        print("3 messages")
        usrinput = input("enter your usrinput: ")
        if usrinput == '1':
            self.openiphoneapp("Camera")
        elif usrinput == '2':
            self.openiphoneapp("Music")
        elif usrinput == '3':
            self.openiphoneapp("Messages")
        else:
            print("invalid option please try again.")    


#  the camera app on the iPhone
class CameraApp:
    def open(self):
        print("camera app opened")
        self.menu()

    # menu for camera app
    def menu(self):
        while True:
            print("1 click photo")
            print("2 exit")
            usrinput = input("Enter your usrinput: ")

            if usrinput == '1':
                self.takephoto()
            elif usrinput == '2':
                print("exiting camera app")
                break
            else:
                print("wrong option please try again")

    # method to click a photo
    def takephoto(self):
        print("photo clicked")


    # the music app on the iPhone
class MusicApp:
    def __init__(self):
        self.isplaying = False
        self.current_song = ""

    def open(self):
        print("Music app opened")
        self.menu()

    # menu for music app
    def menu(self):
        while True:
            print("1 play Daku song")
            print("2 play Bazigar song")
            print("3 play AllNight song")
            print("4 stop music")
            print("5 exit")
            usrinput = input("Enter your usrinput: ")

            if usrinput == '1':
                self.playsong("Daku")

            elif usrinput == '2':
                self.playsong("Bazigar")

            elif usrinput == '3':
                self.playsong("All Night")

            elif usrinput == '4':
                self.stopmusic() # changed playsong("Players") to stopmusic()

            elif usrinput == '5':
                print("exiting music app")
                break
            else:
                print("invalid input please try again")
                
    # function to play the song
    def playsong(self,song_name):
        self.current_song =song_name
        self.isplaying = True
        print(f"{song_name}song started")
        
    # method to stop the currently playing song
    def stopmusic(self):
        if self.isplaying:
            self.isplaying = False
            print(f"{self.current_song}song stopped")
        else:
            print("no song is currently playing")

class MessagesApp:
    def __init__(self):
        self.messages = []
        
    def open(self):
        print("Messages App opened")
        self.menu()
        
    # menu for messages app
    def menu(self):
        while True:
            print("1. Read Messages")
            print("2. Send Message")
            print("3. Exit")
            usrinput = input("Enter your usrinput: ")

            if usrinput == '1':
                self.readmessage()

            elif usrinput == '2':
                self.sendmessage()

            elif usrinput == '3':
                print("Exiting Messages App...")
                break
            else:
                print("invalid input please try again")

    # method to read the messages
    def readmessage(self):
        if len(self.messages) > 0:
            for i, message in enumerate(self.messages):
                print(f"{i+1}. {message}")
        else:
            print("No messages to read.")
            
    # method to send a message
    def sendmessage(self):
        mobilenumber = input("Enter mobile number: ")
        if not mobilenumber.isdigit() or len(mobilenumber) != 10:
            print("invalid mobile number please enter a 10 digit number")
            return
        message = input("enter message ")
        self.messages.append((mobilenumber, message))
        print("message sent")


umariphone = IPhone(1234)
# menu for umariphone
def menu():
    

    while True:
        # print the menu options for the user
        print("1 Open iphone")
        print("2 Exit")
        # getting user input
        usrinput = input("Enter your choice: ")

        if usrinput == '1':
            # user pin
            pin = input("Enter your PIN: ")
            if not pin:# user pin is empty
                print("Invalid input. Please enter a valid PIN.")
            else:
                # checking pin and opeing if correct pin
                umariphone.open(pin)
                if not umariphone.locked:
                    menu1()
                    

        elif usrinput == '2':
            # exiting the program
            print("exiting the program bye")
            sys.exit()
        else:
            print("invalid input please try again")

def menu1():
    while True:
        print("1 open App")
        print("2 lock Iphone")
        usrinput1 = input("Enter your usrinput: ")

        if usrinput1 == '1':
            if not umariphone.locked:
                # menu for installed apps open
                umariphone.menuforinstalledapps()
            else:
                
                print("iphone is locked enter the correct pin to unlock")

        elif usrinput1 == '2':
            umariphone.close
            menu()


        else:
            print("Invalid input Please Try Again")            
            




menu()