import sys

#function to open the phone using a given PIN
class IPhone:
    def __init__(self, pin):
        self.pin = pin
        self.locked = True
        self.apps = ['Messages', 'Camera', 'Music']

    def open(self, input_pin):
      if self.pin == int(input_pin):
        self.locked = False
        print("iPhone is unlocked!")
      else:
        print("incorrect pIN. please Try again.")

#function to lock the iphone
    def close(self):
     self.locked = True
     print("iPhone is locked now.")

#function to open the app on the iphone
    def openapp(self, appname):
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
            print(f"{appname} is not installed on this IPhone.")
     else:
        print("IPhone is locked. Enter the correct PIN to unlock.")


#CameraApp class simulates the camera app on the iPhone
class CameraApp:
    def open(self):
        print("Camera app opened")
        self.menu()

    #menu for camera app
    def menu(self):
        while True:
            print("1. Click Photo")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.click_photo()
            elif choice == '2':
                print("Exiting Camera App...")
                break
            else:
                print("Invalid choice. Please try again.")

    #method to click a photo
    def clickphoto(self):
        print("Click!")
        print("Photo is Taken!")


    #MusicApp class simulates the music app on the iPhone
class MusicApp:
    def __init__(self):
        self.is_playing = False
        self.current_song = ""

    def open(self):
        print("Music app opened")
        self.menu()

    #menu for music app
    def menu(self):
        while True:
            print("1. Play Daku Song")
            print("2. Play Bazigar Song")
            print("3. Play All Night")
            print("4. Stop Music")
            print("5. Exit")
            selection = input("Enter your choice: ")

            if selection == '1':
                self.playsong("Daku")

            elif selection == '2':
                self.playsong("Bazigar")

            elif selection == '3':
                self.playsong("All Night")

            elif selection == '4':
                self.stopmusic() # changed play_song("Players") to stop_music()

            elif selection == '5':
                print("Exiting Music App...")
                break
            else:
                print("Invalid choice. Please try again.")
                
    #method to play the song
    def playsong(self,song_name):
        self.current_song =song_name
        self.is_playing = True
        print(f"{song_name}song started")
        
    #method to stop the currently playing song
    def stopmusic(self):
        if self.is_playing:
            self.is_playing = False
            print(f"{self.current_song}song stopped")
        else:
            print("No song is currently playing")

class MessagesApp:
    def __init__(self):
        self.messages = []
        
    def open(self):
        print("Messages App is opened")
        self.menu()
        
    #menu for messages app
    def menu(self):
        while True:
            print("1.Read Messages")
            print("2.Send Message")
            print("3.Exit")
            selection1 = input("Enter your choice: ")

            if selection1 == '1':
                self.readmessages()

            elif selection1 == '2':
                self.sendmessage()

            elif selection1 == '3':
                print("Exiting Messages App...")
                break
            else:
                print("Invalid choice. Please try again.")

    #method to read the messages
    def readmessages(self):
        if len(self.messages) > 0:
            for i, message in enumerate(self.messages):
                print(f"{i+1}. {message}")
        else:
            print("No messages to read.")
            
    #method to send a message
    def sendmessage(self):
        mobilenumber = input("Enter mobile number: ")
        if not mobilenumber.isdigit() or len(mobilenumber) != 10:
            print("Invalid mobile number. Please enter a 10 digit number.")
            return
        message = input("Enter message: ")
        self.messages.append((mobilenumber, message))
        print("Message sent.")


myiphone = IPhone(1234)
#this function displays a menu for the user to interact with their IPhone
def menu():
    #create an instance of the IPhone class
    

    while True:
        #print the menu options for the user
        print("1. Open IPhone")
        print("2. Exit")
        #get the user's choice
        choice = input("Enter your choice: ")

        if choice == '1':
            #get the user's PIN
            pin = input("Enter your PIN: ")
            #attempt to open the iPhone with the provided PIN
            myiphone.open(pin)
            if not myiphone.locked:
                menu1()
                

        elif choice == '2':
            #exit the program
            print("exiting...")
            sys.exit()
        else:
            print("invalid choice. please try again.")

def menu1():
    while True:
        print("1.Open App")
        print("2.Lock Iphone")
        choice1 = input("Enter your choice: ")

        if choice1 == '1':
            if not myiphone.locked:
                #get the name of the app the user wants to open
                app_name = input("Enter the name of the app you want to open: ")
                #attempt to open the app
                myiphone.openapp(app_name)
            else:
                #if the iPhone is locked, tell the user to enter the correct PIN
                print("IPhone is locked. Enter the correct PIN to unlock.")

        elif choice1 == '2':
            myiphone.close()
            menu()

        else:
            print("Invalid Choice.Please Try Again")            
            




menu()