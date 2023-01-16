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

    def close(self):
        self.locked = True
        print("IPhone locked.")


    def open_app(self, app_name):
        if not self.locked:
            if app_name in self.apps:
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

class CameraApp:
    def open(self):
        print("Camera app opened")
        self.menu()
        
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

    def click_photo(self):
        print("Click!")
        print("Photo Taken!")

class MusicApp:
    def __init__(self):
        self.is_playing = False
        self.current_song = ""
        
    def open(self):
        print("Music app opened")
        self.menu()
        
    def menu(self):
        while True:
            print("1. Play Daku Song")
            print("2. Play Bazigar Song")
            print("3. Stop Music")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.play_song("Daku")
            elif choice == '2':
                self.play_song("Bazigar")
            elif choice == '3':
                self.stop_music()
            elif choice == '4':
                print("Exiting Music App...")
                break
            else:
                print("Invalid choice. Please try again.")

    def play_song(self,song_name):
        self.current_song = song_name
        self.is_playing = True
        print(f"{song_name}song started")
        
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

    def read_messages(self):
        if len(self.messages) > 0:
            for i, message in enumerate(self.messages):
                print(f"{i+1}. {message}")
        else:
            print("No messages to read.")
            
    def send_message(self):
        mobile_number = input("Enter mobile number: ")
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            print("Invalid mobile number. Please enter a 10 digit number.")
            return
        message = input("Enter message: ")
        self.messages.append((mobile_number, message))
        print("Message sent.")



def menu():
    my_iphone = IPhone(1234)

    while True:
        print("1. Open IPhone")
        print("2. Open App")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pin = input("Enter your PIN: ")
            my_iphone.open(pin)
        elif choice == '2':
            if not my_iphone.locked:
                app_name = input("Enter the name of the app you want to open: ")
                my_iphone.open_app(app_name)
            else:
                print("IPhone is locked. Enter the correct PIN to unlock.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()