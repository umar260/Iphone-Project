# function to open the phone using a given PIN
class IPhone:
    def __init__(self, pin):
        self.pin = pin
        self.locked = True
        self.apps = ['Messages', 'Camera', 'Music']
        
    def open(self, input_pin):
      if self.pin == int(input_pin):
        self.locked = False
        print("IPhone unlocked!")
      else:
        print("Incorrect PIN. Try again.")

# function to lock the phone
    def close(self):
     self.locked = True
     print("IPhone locked.")

# function to open an app on the phone
    def open_app(self, app_name):
     if not self.locked: # check if the phone is locked
        if app_name in self.apps: # check if the app is installed on the phone

            if app_name == "Camera":
                self.camera = CameraApp()
                self.camera.open()

            elif app_name == "Music":
                self.music = MusicApp()
                self.music.open()

            elif app_name == "Messages":
                self.messages = MessagesApp()
                self.messages.open()
        else:
            print(f"{app_name} is not installed on this IPhone.")
     else:
        print("IPhone is locked. Enter the correct PIN to unlock.")


# CameraApp class simulates the camera app on the iPhone
class CameraApp:
    def open(self):
        print("Camera app opened")
        self.menu()

    # menu for camera app
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

    # method to click a photo
    def click_photo(self):
        print("Click!")
        print("Photo Taken!")

    # MusicApp class simulates the music app on the iPhone
class MusicApp:
    def __init__(self):
        self.is_playing = False
        self.current_song = ""

    def open(self):
        print("Music app opened")
        self.menu()

    # menu for music app
    def menu(self):
        while True:
            print("1. Play Daku Song")
            print("2. Play Bazigar Song")
            print("3. Play All Night")
            print("4. Stop Music")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.play_song("Daku")

            elif choice == '2':
                self.play_song("Bazigar")

            elif choice == '3':
                self.play_song("All Night")

            elif choice == '4':
                self.stop_music() # changed play_song("Players") to stop_music()

            elif choice == '5':
                print("Exiting Music App...")
                break
            else:
                print("Invalid choice. Please try again.")
                
    # method to play the song
    def play_song(self,song_name):
        self.current_song =song_name
        self.is_playing = True
        print(f"{song_name}song started")
        
    # method to stop the currently playing song
    def stop_music(self):
        if self.is_playing:
            self.is_playing = False
            print(f"{self.current_song}song stopped")
        else:
            print("No song is currently playing")

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
            choice = input("Enter your choice: ")

            if choice == '1':
                self.read_messages()

            elif choice == '2':
                self.send_message()

            elif choice == '3':
                print("Exiting Messages App...")
                break
            else:
                print("Invalid choice. Please try again.")

    # method to read the messages
    def read_messages(self):
        if len(self.messages) > 0:
            for i, message in enumerate(self.messages):
                print(f"{i+1}. {message}")
        else:
            print("No messages to read.")
            
    # method to send a message
    def send_message(self):
        mobile_number = input("Enter mobile number: ")
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            print("Invalid mobile number. Please enter a 10 digit number.")
            return
        message = input("Enter message: ")
        self.messages.append((mobile_number, message))
        print("Message sent.")



# This function displays a menu for the user to interact with their IPhone
def menu():
    # Create an instance of the IPhone class
    my_iphone = IPhone(1234)

    while True:
        # Print the menu options for the user
        print("1. Open IPhone")
        print("2. Open App")
        print("3. Exit")
        # Get the user's choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Get the user's PIN
            pin = input("Enter your PIN: ")
            # Attempt to open the iPhone with the provided PIN
            my_iphone.open(pin)

        elif choice == '2':
            # Check if the iPhone is locked
            if not my_iphone.locked:
                # Get the name of the app the user wants to open
                app_name = input("Enter the name of the app you want to open: ")
                # Attempt to open the app
                my_iphone.open_app(app_name)
            else:
                # If the iPhone is locked, tell the user to enter the correct PIN
                print("IPhone is locked. Enter the correct PIN to unlock.")

        elif choice == '3':
            # Exit the program
            print("Exiting...")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")

# Call the menu function to start the program
menu()
