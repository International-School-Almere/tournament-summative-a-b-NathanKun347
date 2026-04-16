# Tournament Scoring System

# Importing everything from the Tkinter library so I can create a GUI (Graphical User Interface).
# I used the classroom examples for this from the code python password manager to get the GUI.
from tkinter import *

# Importing the messagebox module from Tkinter so the program can show pop-up alerts
import tkinter.messagebox

# Global variables are created outside functions so they can be accessed by multiple functions.

# List to store team names that get registered in the system.
teams = []

# List to store individual competitors registered in the system.
individuals = []

# Dictionary to store scores.
# A dictionary is used because it allows data to be stored as key:value pairs,
# which makes it easier to link a team/individual to their score.
scores = {}

# Variable to keep track of which event is currently selected.
# The assignment requires 5 events so this helps track them.
current_event = 1

# Points awarded based on finishing position.
# The first value (20) is for 1st place, 18 for 2nd place, etc.
# Using a list makes it easy to automatically assign points based on position.
points = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

#MAIN FUNCTION
def main():

    # Creating the main window of the application.
    # The Tk() function creates the root window that everything else will appear inside.
    # Learnt from Tkinter tutorials and the password manager example we did in class.
    window = Tk()

    # Set the title for the top of the window.
    window.title("Tournament Scorer")

    # Set the size of the window for pixels (width x height).
    window.geometry("800x600")

#TITLE LABEL

    # Set the main label. Labels are used for text in TkinterGUIs.
    # pack() puts widgets in the window and pady adds vertical space so that the interface does not get too crowded.
    Label(window, text="Tournament Scoring System",
          font=("Arial", 20)).pack(pady=10)

#EVENT SELECTOR

    # Set a label for the dropdown menu.
    Label(window, text="Select Event:").pack()

    # Define the drop-down list options with an initial value for the dropdown.
    global event_var
    event_var = StringVar(value="Event 1")

    OptionMenu(window, event_var, "Event 1", "Event 2", "Event 3",
               "Event 4", "Event 5").pack()

#MAIN BUTTONS

    # Define and place buttons that are important to the GUI. Buttons launch functions when they are clicked on.

    # Registration button that will launch a separate window to register players or teams.
    Button(window, text="Register", command=register).pack(pady=5)

    # Enter scores button that launches a separate window for inputting the scores for the select event.
    Button(window, text="Enter Scores", command=enter_scores).pack(pady=5)

    # Leaderboard button that launches a window to display rankings based on points awarded.
    Button(window, text="View Leaderboard", command=leaderboard).pack(pady=5)

#MAIN LOOP
    # mainloop() keeps the program running and waits for user interaction.
    window.mainloop()


#PLACEHOLDER FUNCTIONS

# These functions are placeholders so the buttons don't cause errors.
# They will be implemented later when the rest of the program is developed.

def register():
    # TODO: Create a new window that allows users to register teams or individuals.
    # This will include Entry widgets for typing names.
    pass


def enter_scores():
    # TODO: Create a form where the user can input finishing positions
    # and the program will automatically assign points.
    pass


def leaderboard():
    # TODO: Calculate total points and display the ranking of competitors.
    pass

# Program starts here as it calls the main() function which then sets up the GUI screen leaving it ready for the user to interact with.

# This line ensures the main() function only runs when the file is executed directly.
if __name__ == "__main__":
    main()