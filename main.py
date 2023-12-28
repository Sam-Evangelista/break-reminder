from tkinter import *
import random

class BreakReminderApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Take a Break")
        self.root.configure(background="black")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.timer_clicked = 0

        self.get_screen_dimensions()

        self.root.geometry("{0}x{1}+{2}+{3}".format(self.screen_width, self.screen_height, 0, 0))

        self.create_gui()
        self.bind_events()
        
        # Schedule the GUI changes
        self.root.after(3000, self.change_text_to_press_anywhere)

    def get_screen_dimensions(self):
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

    def create_gui(self):
        self.text = Label(self.root, text="It's time to take a break", font=("Helvetica", 20), fg="white", bg="black")
        self.text.pack(expand=True)

    def bind_events(self):
        self.root.bind("<Escape>", self.toggle_fullscreen)
        self.root.bind("<F11>", self.toggle_fullscreen)

    def toggle_fullscreen(self, event):
        if self.root.attributes('-fullscreen'):
            self.root.attributes('-fullscreen', False)
        else:
            self.root.attributes('-fullscreen', True)

    def change_text_to_press_anywhere(self):
        self.text.config(text="Press anywhere to continue")
        self.root.bind("<Button-1>", self.start_timer)

    def start_timer(self, event):
        if self.timer_clicked == 0:    
            self.text.config(text="Timer started!")
            
            # Generate a random time between 10 and 30 minutes in seconds
            random_minutes = random.randint(10, 30)
            countdown_seconds = random_minutes * 60

            # Schedule the countdown
            self.root.after(1000, lambda: self.update_timer(countdown_seconds))
            self.timer_clicked += 1
        else:
            self.text.config(text="Timer already started!")
            self.root.unbind("<Button-1>")

    def update_timer(self, seconds_left):
        if seconds_left > 0:
            # Update the text with the remaining time
            self.text.config(text=f"Break Time: {seconds_left // 60}:{seconds_left % 60:02}")
            # Schedule the next update after 1000 milliseconds (1 second)
            self.root.after(1000, lambda: self.update_timer(seconds_left - 1))
        else:
            # Countdown finished
            self.text.config(text="Time's up! You can go back to whatever you were doing")
            self.root.after(3000, lambda: self.root.destroy())
    
    def run(self):
        self.root.mainloop()

def main():
    app = BreakReminderApp()
    app.run()

if __name__ == "__main__":
    main()
