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

    # Added command=change_event so when user picks different event it updates current_event variable
    OptionMenu(window, event_var, "Event 1", "Event 2", "Event 3",
               "Event 4", "Event 5", command=change_event).pack()

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


# NEW FUNCTION FOR SESSION 3 - EVENT CHANGE HANDLER
# This function runs when user picks different event from dropdown
# It updates the current_event variable so scores go to right event
def change_event(selection):
    global current_event
    current_event = int(selection.split()[1])


# REGISTRATION FUNCTION - COMPLETED IN SESSION 2
def register():
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
                "points": 0
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
                "events": selected_events,
                "points": 0
            }
            individuals.append(person)
            tkinter.messagebox.showinfo("Success", f"Individual {name} registered!")
        
        reg.destroy()
    
    Button(reg, text="Register", command=do_register).pack(pady=20)


# NEW CODE FOR SESSION 3 - SCORE ENTRY IMPLEMENTATION
# This creates a popup window where user enters scores for current event
# It shows all registered teams and individuals with Entry boxes for their scores
def enter_scores():
    # Create the score entry popup window
    score_win = Toplevel()
    score_win.title("Enter Scores - Event " + str(current_event))
    score_win.geometry("300x500")
    
    # Show which event we are entering scores for
    Label(score_win, text="Event " + str(current_event)).pack()
    
    # TEAM SCORES SECTION
    # Show label for teams section
    Label(score_win, text="TEAMS:").pack()
    
    # Create a list to store the Entry widgets for team scores
    # This is needed so we can read the values later when saving
    team_entries = []
    
    # Loop through registered teams and create Entry boxes for each
    for i in range(len(teams)):
        # Use Frame to put label and Entry side by side
        frame = Frame(score_win)
        frame.pack()
        Label(frame, text=teams[i]["name"] + ":").pack(side=LEFT)
        entry = Entry(frame, width=8)
        entry.pack(side=LEFT)
        team_entries.append(entry)
    
    # Fill empty slots if less than 4 teams registered
    # This keeps the layout consistent and allows for future teams
    for i in range(len(teams), 4):
        frame = Frame(score_win)
        frame.pack()
        Label(frame, text="Team " + str(i+1) + ":").pack(side=LEFT)
        entry = Entry(frame, width=8)
        entry.pack(side=LEFT)
        team_entries.append(entry)
    
    # INDIVIDUAL SCORES SECTION
    # Show label for individuals section
    Label(score_win, text="INDIVIDUALS:").pack()
    
    # Create a list to store the Entry widgets for individual scores
    ind_entries = []
    
    # Loop through registered individuals and create Entry boxes for each
    for i in range(len(individuals)):
        frame = Frame(score_win)
        frame.pack()
        Label(frame, text=individuals[i]["name"] + ":").pack(side=LEFT)
        entry = Entry(frame, width=8)
        entry.pack(side=LEFT)
        ind_entries.append(entry)
    
    # Fill empty slots if less than 20 individuals registered
    for i in range(len(individuals), 20):
        frame = Frame(score_win)
        frame.pack()
        Label(frame, text="Person " + str(i+1) + ":").pack(side=LEFT)
        entry = Entry(frame, width=8)
        entry.pack(side=LEFT)
        ind_entries.append(entry)
    
    # Function to save the scores when button is clicked
    def save_scores():
        global scores
        
        # Create dictionary for this event if it doesn't exist yet
        if current_event not in scores:
            scores[current_event] = {}
        
        # Save team scores from Entry widgets
        for i in range(4):
            try:
                # Try to convert the Entry text to an integer
                score = int(team_entries[i].get())
                if i < len(teams):
                    # Use TEAM + id as key to identify which team
                    scores[current_event]["TEAM" + str(teams[i]["id"])] = score
                else:
                    scores[current_event]["TEAM" + str(i+1)] = score
            except:
                # If Entry is empty or not a number, skip it
                pass
        
        # Save individual scores from Entry widgets
        for i in range(20):
            try:
                score = int(ind_entries[i].get())
                if i < len(individuals):
                    # Use IND + id as key to identify which individual
                    scores[current_event]["IND" + str(individuals[i]["id"])] = score
                else:
                    scores[current_event]["IND" + str(i+1)] = score
            except:
                pass
        
        # Calculate points based on the new scores
        calculate_points()
        tkinter.messagebox.showinfo("Done", "Scores saved!")
        score_win.destroy()
    
    Button(score_win, text="Save", command=save_scores).pack(pady=10)


# NEW FUNCTION FOR SESSION 3 - POINT CALCULATION
# This calculates points for all participants based on their scores across all events
# Uses manual sorting (bubble sort) to demonstrate algorithm understanding for BTEC
def calculate_points():
    # Reset all points to 0 before recalculating
    # This prevents double-counting if scores are updated multiple times
    for t in teams:
        t["points"] = 0
    for p in individuals:
        p["points"] = 0
    
    # Calculate points for each event (1 through 5)
    for event_num in range(1, 6):
        # Skip events that don't have any scores entered yet
        if event_num not in scores:
            continue
        
        # Make a list of (participant_id, score) tuples from the scores dictionary
        score_list = []
        for pid in scores[event_num]:
            score_list.append((pid, scores[event_num][pid]))
        
        # Sort by score using bubble sort (manual implementation for BTEC)
        # This demonstrates understanding of sorting algorithms
        for i in range(len(score_list)):
            for j in range(len(score_list)-1):
                # Compare adjacent elements and swap if out of order
                if score_list[j][1] < score_list[j+1][1]:
                    temp = score_list[j]
                    score_list[j] = score_list[j+1]
                    score_list[j+1] = temp
        
        # Give points based on position
        position = 1
        last_score = None
        
        for i in range(len(score_list)):
            pid, score = score_list[i]
            
            # If score is different from previous, update position
            # This handles ties - same score gets same position
            if score != last_score:
                position = i + 1
            
            # Only give points if position is 10 or better
            if position <= 10:
                pts = points[position-1]
            else:
                pts = 0
            
            # Add points to team or individual based on ID prefix
            if pid.startswith("TEAM"):
                tid = int(pid.replace("TEAM", ""))
                for t in teams:
                    if t["id"] == tid:
                        t["points"] += pts
            else:
                iid = int(pid.replace("IND", ""))
                for p in individuals:
                    if p["id"] == iid:
                        p["points"] += pts
            
            last_score = score


# Still empty - will implement in Session 4
def leaderboard():
    # TODO: Calculate total points and display the ranking of competitors.
    pass

# Program starts here as it calls the main() function which then sets up the GUI screen leaving it ready for the user to interact with.

# This line ensures the main() function only runs when the file is executed directly.
if __name__ == "__main__":
    main()