# Tournament Scoring System
# BTEC Unit 4 Programming Assignment
# My first Python project with GUI

# Importing everything from the Tkinter library so I can Create a GUI (Graphical User Interface).
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

# Variable to keep track of which Event is currently selected.
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
    # THIS IS THE NEW CODE FOR SESSION 2 - REGISTRATION IMPLEMENTATION
    # Create popup window for registration
    reg = Toplevel()
    reg.title("Register Participant")
    reg.geometry("400x500")
    
    # Need to use global here so we can modify the main lists
    global teams, individuals
    
    Label(reg, text="Register New Participant", font=("Arial", 14)).pack(pady=10)
    
    # Type selection
    Label(reg, text="Type:").pack()
    p_type = StringVar(value="individual")
    Radiobutton(reg, text="Individual", variable=p_type, 
               value="individual").pack()
    Radiobutton(reg, text="Team", variable=p_type, 
               value="team").pack()
    
    # Name entry
    Label(reg, text="Name:").pack()
    name_entry = Entry(reg)
    name_entry.pack()
    
    # Event selection for registration
    Label(reg, text="Select events to enter:").pack()
    event_checks = []
    for i in range(5):
        var = BooleanVar(value=True)
        Checkbutton(reg, text=f"Event {i+1}", variable=var).pack()
        event_checks.append(var)
    
    # Team member entries (only shown if Team selected)
    # Using a frame to group these together
    team_frame = Frame(reg)
    team_frame.pack(pady=10)
    Label(team_frame, text="Team Members (if Team):").pack()
    
    member_entries = []
    for i in range(5):
        Label(team_frame, text=f"Member {i+1}:").pack(side=LEFT)
        entry = Entry(team_frame, width=10)
        entry.pack(side=LEFT, padx=5)
        member_entries.append(entry)
    
    def do_register():
        # Get the values from the form
        name = name_entry.get()
        
        # Basic validation
        if not name:
            tkinter.messagebox.showerror("Error", "Please enter a name!")
            return
        
        # Check for duplicates
        for t in teams:
            if t["name"] == name:
                tkinter.messagebox.showerror("Error", "Team name already exists!")
                return
        for p in individuals:
            if p["name"] == name:
                tkinter.messagebox.showerror("Error", "Individual name already exists!")
                return
        
        # Get selected events
        selected_events = []
        for i in range(5):
            if event_checks[i].get():
                selected_events.append(i+1)
        
        # Check limits and register
        if p_type.get() == "team":
            if len(teams) >= 4:
                tkinter.messagebox.showerror("Error", "Maximum 4 teams allowed!")
                return
            
            # Get member name - filter out empty ones
            members = []
            for entry in member_entries:
                member_name = entry.get()
                if member_name:
                    members.append(member_name)
            
            # Create team dictionary
            team = {
                "id": len(teams) + 1,
                "name": name,
                "members": members,
                "events": selected_events,
                "Points": 0
            }
            teams.append(team)
            tkinter.messagebox.showinfo("Success", f"Team {name} registered!")
            
        else:
            if len(individuals) >= 20:
                tkinter.messagebox.showerror("Error", "Maximum 20 individuals allowed!")
                return
            
            # Create Individual dictionary
            person = {
                "id": len(individuals) + 1,
                "name": name,
                "Events": selected_events,
                "Points": 0
            }
            individuals.append(person)
            tkinter.messagebox.showinfo("Success", f"Individual {name} registered!")
        
        reg.destroy()
    
    Button(reg, text="Register", command=do_register).pack(pady=20)

# Still empty - will implement in Session 3
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