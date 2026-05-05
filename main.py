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

    # Save button that saves all current data to a text file so it can be loaded later.
    # Added in Session 5 - needed for data persistence between program runs.
    Button(window, text="Save", command=save).pack(pady=5)

    # Load button that reads data back from the text file into the program.
    # Added in Session 5 - allows resuming a tournament after closing the program.
    Button(window, text="Load", command=load).pack(pady=5)

#MAIN LOOP
    # mainloop() keeps the program running and waits for user interaction.
    window.mainloop()


# EVENT CHANGE HANDLER - COMPLETED IN SESSION 3
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


# SCORE ENTRY FUNCTION - COMPLETED IN SESSION 3
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


# POINT CALCULATION FUNCTION - COMPLETED IN SESSION 3
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


# LEADERBOARD FUNCTION - COMPLETED IN SESSION 4
# This creates a popup window showing the current rankings of all participants
# It combines teams and individuals into one sorted list for them to be shown together
def leaderboard():
    # Create the leaderboard popup window
    lb = Toplevel()
    lb.title("Leaderboard")
    lb.geometry("400x500")
    
    # Title for the leaderboard window
    Label(lb, text="Leaderboard", font=("Arial", 16)).pack()
    
    # Combine everyone into one list for ranking
    # Each entry is a tuple: (name, type, points)
    everyone = []
    
    # Add all teams to the combined list
    for t in teams:
        everyone.append((t["name"], "Team", t["points"]))
    
    # Add all individuals to the combined list
    for p in individuals:
        everyone.append((p["name"], "Individual", p["points"]))
    
    # Sort by points using bubble sort (manual implementation for BTEC)
    # Sorts in descending order so highest points are at the top
    for i in range(len(everyone)):
        for j in range(len(everyone)-1):
            if everyone[j][2] < everyone[j+1][2]:
                temp = everyone[j]
                everyone[j] = everyone[j+1]
                everyone[j+1] = temp
    
    # Create a Listbox widget to display the rankings
    # Listbox is better than Labels because it can scroll if there are many entries
    listbox = Listbox(lb, width=50)
    listbox.pack(padx=10, pady=10, fill=BOTH, expand=True)
    
    # Add header row to the Listbox
    listbox.insert(END, "Rank Name Type Points")
    
    # Add separator line for visual clarity
    listbox.insert(END, "-" * 40)
    
    # Loop through sorted list and add each participant to the Listbox
    for i in range(len(everyone)):
        name, ptype, pts = everyone[i]
        # Format each line with rank, name, type and points
        line = str(i+1) + " " + name + " " + ptype + " " + str(pts)
        listbox.insert(END, line)


# NEW CODE FOR SESSION 5 - SAVE FUNCTION
# This saves all tournament data to a text file called save.txt
# Uses a custom format with sections so it can be loaded back later
def save():
    try:
        # Open the file in write mode - this will create it if it doesn't exist
        # or overwrite it if it does exist
        file = open("save.txt", "w")
        
        # Write the TEAMS section header
        file.write("TEAMS\n")
        
        # Loop through each team and write its data as a line
        # Format: id|name|member1,member2,member3|points
        for t in teams:
            file.write(str(t["id"]) + "|" + t["name"] + "|")
            # Join member names with commas so they stay together in one field
            file.write(",".join(t["members"]))
            file.write("|" + str(t["points"]) + "\n")
        
        # Write the INDIVIDUALS section header
        file.write("INDIVIDUALS\n")
        
        # Loop through each individual and write its data as a line
        # Format: id|name|points
        for p in individuals:
            file.write(str(p["id"]) + "|" + p["name"] + "|" + str(p["points"]) + "\n")
        
        # Write the SCORES section header
        file.write("SCORES\n")
        
        # Loop through each event in the scores dictionary
        for e in scores:
            file.write("EVENT " + str(e) + "\n")
            # For each event, write each participant's score
            for pid in scores[e]:
                file.write(pid + "|" + str(scores[e][pid]) + "\n")
        
        # Close the file to ensure data is written to disk
        file.close()
        
        # Show success message to user
        tkinter.messagebox.showinfo("Done", "Saved!")
    except:
        # If anything goes wrong (file permissions, disk full, etc.)
        # show an error message instead of crashing
        tkinter.messagebox.showerror("Error", "Couldn't save!")


# NEW CODE FOR SESSION 5 - LOAD FUNCTION
# This reads tournament data back from save.txt into the program
# Reverses the save process by parsing the custom format
def load():
    # Need to modify the global lists and dictionary
    global teams, individuals, scores
    
    try:
        # Open the file in read mode
        file = open("save.txt", "r")
        
        # Read all lines into a list
        lines = file.readlines()
        
        # Close the file as soon as we're done reading
        file.close()
        
        # Clear existing data before loading new data
        # This prevents duplicates if load is clicked multiple times
        teams = []
        individuals = []
        scores = {}
        
        # Track which section we're currently reading
        section = ""
        current_event = 0
        
        # Loop through each line in the file
        for line in lines:
            # Remove the newline character from the end of each line
            line = line.strip()
            
            # Check for section headers to know what data follows
            if line == "TEAMS":
                section = "teams"
            elif line == "INDIVIDUALS":
                section = "individuals"
            elif line == "SCORES":
                section = "scores"
            elif line.startswith("EVENT"):
                # Extract the event number from "EVENT 1", "EVENT 2", etc.
                current_event = int(line.split()[1])
                # Create empty dictionary for this event's scores
                scores[current_event] = {}
                section = "event"
            else:
                # Process data lines based on which section we're in
                if section == "teams":
                    # Split the line by pipe character to get fields
                    parts = line.split("|")
                    # Reconstruct the team dictionary
                    team = {
                        "id": int(parts[0]),
                        "name": parts[1],
                        # Split members by comma to get list back
                        "members": parts[2].split(","),
                        "points": int(parts[3])
                    }
                    teams.append(team)
                elif section == "individuals":
                    parts = line.split("|")
                    person = {
                        "id": int(parts[0]),
                        "name": parts[1],
                        "points": int(parts[2])
                    }
                    individuals.append(person)
                elif section == "event":
                    # Score lines are format: TEAM1|100 or IND1|50
                    parts = line.split("|")
                    scores[current_event][parts[0]] = int(parts[1])
        
        # Show success message to user
        tkinter.messagebox.showinfo("Done", "Loaded!")
    except:
        # If file doesn't exist or is corrupted, show error
        tkinter.messagebox.showerror("Error", "No save file!")


# Program starts here as it calls the main() function which then sets up the GUI screen leaving it ready for the user to interact with.

# This line ensures the main() function only runs when the file is executed directly.
if __name__ == "__main__":
    main()