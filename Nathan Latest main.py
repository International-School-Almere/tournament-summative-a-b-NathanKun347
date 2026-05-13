# Tournament Scoring System
# BTEC Unit 4 Programming Assignment
# My first Python project with GUI

# Importing everything from the Tkinter library so I can Create a GUI (Graphical User Interface).
# I used the classroom examples for this from the code python password manager to get the GUI.
from tkinter import *

# Importing the messagebox module from Tkinter so the program can show pop-up alerts
import tkinter.messagebox

# Importing json module for saving and loading data in JSON format
# JSON is better than custom text files because it handles nested dictionaries automatically
# and doesn't break if names contain special characters like commas or pipes
import json

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
    # INCREASED in Session 7 - was 800x600 but now 900x650 for better spacing
    window.geometry("900x650")

    # NEW IN SESSION 7 - Mac fix: keep window on current desktop/Space
    # Without this, Mac puts tkinter windows on separate Spaces and you have to swipe
    # topmost keeps it above other apps, but we turn it off after opening so it's not annoying
    window.attributes('-topmost', True)
    window.after(100, lambda: window.attributes('-topmost', False))

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

    # Save button that saves all current data to a JSON file so it can be loaded later.
    # Changed from text file to JSON in Session 6 because JSON is more reliable and handles nested data better.
    # Added in Session 5 - needed for data persistence between program runs.
    Button(window, text="Save", command=save).pack(pady=5)

    # Load button that reads data back from the JSON file into the program.
    # Changed from text file to JSON in Session 6 - JSON automatically converts back to Python lists/dictionaries.
    # Added in Session 5 - allows resuming a tournament after closing the program.
    Button(window, text="Load", command=load).pack(pady=5)

    # Export button that generates a formatted results report for the college.
    # Added in Session 6 - creates a professional tournament results file.
    Button(window, text="Export", command=export).pack(pady=5)

#MAIN LOOP
    # mainloop() keeps the program running and waits for user interaction.
    window.mainloop()


# EVENT CHANGE HANDLER - COMPLETED IN SESSION 3
# This function runs when user picks different event from dropdown
# It updates the current_event variable so scores go to right event
def change_event(selection):
    global current_event
    current_event = int(selection.split()[1])


# NEW HELPER FUNCTION FOR SESSION 7 - CENTER POPUP ON SCREEN
# This calculates the center position of the screen so popups appear in the middle
# Instead of appearing at random positions where users might miss them
# Added because popups were appearing off-screen or behind the main window
def center_popup(popup, width, height):
    # Get the screen width and height in pixels
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    
    # Calculate x and y coordinates to center the popup
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    # Set the geometry with the calculated position
    popup.geometry(f"{width}x{height}+{x}+{y}")


# NEW HELPER FUNCTION FOR SESSION 7 - CREATE SCROLLABLE POPUP
# This creates a popup with Canvas + Scrollbar so content never gets cut off
# Needed because score entry with 20 individuals is taller than any laptop screen
# Returns the popup window and a scrollable Frame to put widgets in
def create_scrollable_popup(title, width, height):
    # Create the popup window
    popup = Toplevel()
    popup.title(title)
    center_popup(popup, width, height)
    
    # Mac fix: keep popup on current desktop and force it to front
    popup.attributes('-topmost', True)
    popup.after(100, lambda: popup.attributes('-topmost', False))
    popup.lift()
    popup.focus_force()
    
    # Create a Canvas widget that will hold the scrollable content
    # Canvas is like a drawing board that can be larger than the window
    canvas = Canvas(popup)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    # Add a vertical scrollbar linked to the Canvas
    scrollbar = Scrollbar(popup, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Tell the Canvas to use the scrollbar for vertical scrolling
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Create a Frame inside the Canvas - this is where you put your actual widgets
    # The Frame will be as tall as needed, and the Canvas will let you scroll through it
    scrollable_frame = Frame(canvas)
    
    # Add the Frame to the Canvas window
    # This is a special Canvas method that embeds a widget inside the Canvas
    canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor=NW)
    
    # Function that runs whenever the Frame changes size
    # It updates the Canvas scroll region so the scrollbar knows how much content there is
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        # Also make the embedded window match the Canvas width so it fills horizontally
        canvas.itemconfig(canvas_window, width=canvas.winfo_width())
    
    # Bind the configure event so it updates when widgets are added
    scrollable_frame.bind("<Configure>", on_frame_configure)
    
    # Also update when Canvas itself is resized (e.g., user drags window corner)
    def on_canvas_configure(event):
        canvas.itemconfig(canvas_window, width=event.width)
    
    canvas.bind("<Configure>", on_canvas_configure)
    
    # Enable mouse wheel scrolling on Mac (uses different event than Windows)
    # Mac mouse wheel generates <MouseWheel> events with delta values
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    # Bind mouse wheel to the popup so scrolling works anywhere in the window
    popup.bind("<MouseWheel>", on_mousewheel)
    
    return popup, scrollable_frame


# REGISTRATION FUNCTION - REDESIGNED IN SESSION 7
# Fixed layout issues: popup was too tall and team member entries overflowed horizontally
# Now uses vertical layout for members and scrollable popup so nothing gets cut off
def register():
    # Create scrollable popup window for registration
    # Using create_scrollable_popup helper so content never gets cut off
    reg, content = create_scrollable_popup("Register Participant", 450, 650)
    
    # Need to use global here so we can modify the main lists
    global teams, individuals
    
    Label(content, text="Register New Participant", font=("Arial", 14)).pack(pady=10)
    
    # Type selection
    Label(content, text="Type:").pack()
    p_type = StringVar(value="individual")
    Radiobutton(content, text="Individual", variable=p_type, 
               value="individual").pack()
    Radiobutton(content, text="Team", variable=p_type, 
               value="team").pack()
    
    # Name entry
    Label(content, text="Name:").pack()
    name_entry = Entry(content)
    name_entry.pack()
    
    # Event selection for registration
    # This lets the user choose which events this participant will compete in
    # FR-004 from design doc: Allow full tournament or single-event participation
    Label(content, text="Select events to enter:").pack()
    event_checks = []
    for i in range(5):
        var = BooleanVar(value=True)
        Checkbutton(content, text=f"Event {i+1}", variable=var).pack()
        event_checks.append(var)
    
    # Team member entries - FIXED LAYOUT IN SESSION 7
    # Changed from horizontal (side-by-side) to vertical (stacked) layout
    # Horizontal layout caused overflow - entries went off the right side of the window
    # Vertical layout ensures all 5 members are visible and properly spaced
    team_frame = Frame(content)
    team_frame.pack(pady=10)
    Label(team_frame, text="Team Members (if Team):").pack()
    
    # NEW IN SESSION 7 - Stack member entries vertically instead of side-by-side
    # Each member gets its own row with label and entry aligned
    member_entries = []
    for i in range(5):
        # Create a frame for each member row
        member_row = Frame(team_frame)
        member_row.pack(fill=X, pady=2)
        
        # Label on the left
        Label(member_row, text=f"Member {i+1}:", width=10, anchor=W).pack(side=LEFT)
        
        # Entry on the right, fills available width
        entry = Entry(member_row)
        entry.pack(side=LEFT, fill=X, expand=True, padx=5)
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
        
        # Get selected events from checkboxes
        # This determines which events the participant will score points in
        selected_events = []
        for i in range(5):
            if event_checks[i].get():
                selected_events.append(i+1)
        
        # Check limits and register
        if p_type.get() == "team":
            if len(teams) >= 4:
                tkinter.messagebox.showerror("Error", "Maximum 4 teams allowed!")
                return
            
            # Get member names - filter out empty ones
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
    
    Button(content, text="Register", command=do_register).pack(pady=20)


# SCORE ENTRY FUNCTION - COMPLETELY REDESIGNED IN SESSION 7
# Now uses scrollable popup so all 20 individuals + 4 teams fit without cutting off
# Also fixed Mac window management so it stays on current desktop
def enter_scores():
    # Create scrollable popup for score entry
    # Height is limited - content scrolls if taller than screen
    score_win, content = create_scrollable_popup(
        "Enter Scores - Event " + str(current_event), 450, 700)
    
    # Show which event we are entering scores for
    # This comes from the main window dropdown (current_event variable)
    Label(content, text="Event " + str(current_event), font=("Arial", 14)).pack(pady=5)
    
    # TEAM SCORES SECTION
    # Show label for teams section
    Label(content, text="TEAMS:", font=("Arial", 12, "bold")).pack()
    
    # Create a list to store the Entry widgets for team scores
    # This is needed so we can read the values later when saving
    team_entries = []
    
    # Loop through registered teams and create Entry boxes for each
    for i in range(len(teams)):
        # Use Frame to put label and Entry side by side
        frame = Frame(content)
        frame.pack(fill=X, padx=20, pady=2)
        Label(frame, text=teams[i]["name"] + ":", width=15, anchor=W).pack(side=LEFT)
        entry = Entry(frame, width=10)
        entry.pack(side=LEFT)
        team_entries.append(entry)
    
    # Fill empty slots if less than 4 teams registered
    # This keeps the layout consistent and allows for future teams
    for i in range(len(teams), 4):
        frame = Frame(content)
        frame.pack(fill=X, padx=20, pady=2)
        Label(frame, text="Team " + str(i+1) + ":", width=15, anchor=W).pack(side=LEFT)
        entry = Entry(frame, width=10)
        entry.pack(side=LEFT)
        team_entries.append(entry)
    
    # INDIVIDUAL SCORES SECTION
    # Show label for individuals section
    Label(content, text="INDIVIDUALS:", font=("Arial", 12, "bold")).pack(pady=(10,0))
    
    # Create a list to store the Entry widgets for individual scores
    ind_entries = []
    
    # Loop through registered individuals and create Entry boxes for each
    for i in range(len(individuals)):
        frame = Frame(content)
        frame.pack(fill=X, padx=20, pady=2)
        Label(frame, text=individuals[i]["name"] + ":", width=15, anchor=W).pack(side=LEFT)
        entry = Entry(frame, width=10)
        entry.pack(side=LEFT)
        ind_entries.append(entry)
    
    # Fill empty slots if less than 20 individuals registered
    for i in range(len(individuals), 20):
        frame = Frame(content)
        frame.pack(fill=X, padx=20, pady=2)
        Label(frame, text="Person " + str(i+1) + ":", width=15, anchor=W).pack(side=LEFT)
        entry = Entry(frame, width=10)
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
    
    Button(content, text="Save Scores", command=save_scores).pack(pady=15)


# POINT CALCULATION FUNCTION - FIXED IN SESSION 7
# This calculates points for all participants based on their scores across all events
# Uses manual sorting (bubble sort) to demonstrate algorithm understanding for BTEC
# FIXED IN SESSION 7: Now checks if participant actually entered the event before giving points
# CRITICAL BUG FIX: JSON save/load converts integers to strings, so we check both types
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
            # FIXED IN SESSION 7: Check if participant actually entered this event
            # CRITICAL FIX: JSON converts integers to strings, so we check both int and string
            event_str = str(event_num)
            if pid.startswith("TEAM"):
                tid = int(pid.replace("TEAM", ""))
                for t in teams:
                    # Only add points if this team registered for this specific event
                    # Check both integer and string forms to handle both cases
                    if t["id"] == tid and (event_num in t["events"] or event_str in t["events"]):
                        t["points"] += pts
            else:
                iid = int(pid.replace("IND", ""))
                for p in individuals:
                    # Only add points if this individual registered for this specific event
                    # Check both integer and string forms to handle both cases
                    if p["id"] == iid and (event_num in p["events"] or event_str in p["events"]):
                        p["points"] += pts
            
            last_score = score


# LEADERBOARD FUNCTION - FIXED IN SESSION 7
# Added centering and focus so it appears properly on screen
# Also made scrollable in case there are many participants
def leaderboard():
    # Create scrollable popup for leaderboard
    lb, content = create_scrollable_popup("Leaderboard", 500, 550)
    
    # Title for the leaderboard window
    Label(content, text="Leaderboard", font=("Arial", 16)).pack(pady=10)
    
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
    listbox = Listbox(content, width=50, font=("Courier", 10))
    listbox.pack(padx=10, pady=10, fill=BOTH, expand=True)
    
    # Add header row to the Listbox
    listbox.insert(END, f"{'Rank':<6}{'Name':<20}{'Type':<12}{'Points':<6}")
    
    # Add separator line for visual clarity
    listbox.insert(END, "-" * 50)
    
    # Loop through sorted list and add each participant to the Listbox
    for i in range(len(everyone)):
        name, ptype, pts = everyone[i]
        # Format each line with proper column alignment using f-string
        line = f"{i+1:<6}{name:<20}{ptype:<12}{pts:<6}"
        listbox.insert(END, line)


# SAVE FUNCTION - CONVERTED TO JSON IN SESSION 6
# This saves all tournament data to a JSON file called save.json
# JSON is better than the old custom text format because:
# - It preserves nested dictionary structures automatically (like the scores dictionary)
# - No manual string parsing with split() and join() needed
# - Handles special characters in names (commas, pipes, etc.) without breaking the format
# - Less code and fewer bugs because json.dump() does all the work
# - Still human-readable because JSON is plain text with proper formatting
def save():
    try:
        # Create a dictionary holding ALL the data that needs to be saved
        # This includes teams, individuals, and scores in one structure
        data = {
            "teams": teams,
            "individuals": individuals,
            "scores": scores
        }
        
        # Open the file in write mode
        # 'w' means write, and we use .json extension to show it's JSON format
        file = open("save.json", "w")
        
        # json.dump writes the dictionary to the file as formatted JSON text
        # indent=4 makes it human-readable with proper spacing (good for debugging)
        json.dump(data, file, indent=4)
        
        # Close the file to ensure data is written to disk
        file.close()
        
        # Show success message to user
        tkinter.messagebox.showinfo("Done", "Saved to save.json!")
    except:
        # If anything goes wrong (file permissions, disk full, etc.)
        # show an error message instead of crashing
        tkinter.messagebox.showerror("Error", "Couldn't save!")


# LOAD FUNCTION - CONVERTED TO JSON IN SESSION 6
# This reads tournament data back from save.json into the program
# JSON automatically converts back to Python lists and dictionaries
# No need for manual parsing like with the old pipe-delimited format
# This means less code and fewer places for bugs to happen
def load():
    # Need to modify the global lists and dictionary
    global teams, individuals, scores
    
    try:
        # Open the file in read mode
        file = open("save.json", "r")
        
        # json.load reads the JSON text and converts it back to Python objects
        # This gives us back the exact same dictionary structure we saved
        data = json.load(file)
        
        # Close the file as soon as we're done reading
        file.close()
        
        # Extract the data back into our global variables
        # JSON preserves the list of dictionaries structure perfectly
        teams = data["teams"]
        individuals = data["individuals"]
        scores = data["scores"]
        
        # Show success message to user
        tkinter.messagebox.showinfo("Done", "Loaded from save.json!")
    except FileNotFoundError:
        # Specific error for when the file doesn't exist yet
        # This is better than a generic error because it tells the user exactly what went wrong
        tkinter.messagebox.showerror("Error", "No save file found!")
    except:
        # If file is corrupted or not valid JSON
        tkinter.messagebox.showerror("Error", "Couldn't load - file may be corrupted!")


# EXPORT FUNCTION - COMPLETED IN SESSION 6
# This generates a professional tournament results report as a text file
# The report includes standings, event breakdowns, and winner announcements
# This fulfills FR-007 (Results Export) from the design document
def export():
    try:
        # Open results.txt in write mode to create the report
        file = open("results.txt", "w")
        
        # Write the main title of the report
        file.write("TOURNAMENT RESULTS\n")
        
        # Add a visual separator line using equals signs
        file.write("=" * 40 + "\n\n")
        
        # STANDINGS SECTION
        # This section shows the final rankings of all participants
        file.write("STANDINGS\n")
        
        # Combine teams and individuals into one list for unified ranking
        everyone = []
        
        # Add all teams with their type and points
        for t in teams:
            everyone.append((t["name"], "Team", t["points"]))
        
        # Add all individuals with their type and points
        for p in individuals:
            everyone.append((p["name"], "Individual", p["points"]))
        
        # Sort by points using bubble sort (manual implementation for BTEC)
        for i in range(len(everyone)):
            for j in range(len(everyone)-1):
                if everyone[j][2] < everyone[j+1][2]:
                    temp = everyone[j]
                    everyone[j] = everyone[j+1]
                    everyone[j+1] = temp
        
        # Write each participant's ranking to the file
        for i in range(len(everyone)):
            name, ptype, pts = everyone[i]
            # Format: 1. Team Name (Team) - 50 points
            file.write(str(i+1) + ". " + name + " (" + ptype + ") - " + str(pts) + "\n")
        
        # EVENTS SECTION
        # This section shows the scores for each event
        file.write("\nEVENTS\n")
        
        # Loop through all 5 events (1 to 5)
        for e in range(1, 6):
            file.write("Event " + str(e) + ":\n")
            
            # Check if this event has any scores entered
            if e in scores:
                # Write each participant's score for this event
                for pid in scores[e]:
                    file.write("  " + pid + ": " + str(scores[e][pid]) + "\n")
            else:
                # If no scores for this event yet
                file.write("  No scores\n")
        
        # Close the file to ensure all data is written
        file.close()
        
        # Show success message to user
        tkinter.messagebox.showinfo("Done", "Exported to results.txt!")
    except:
        # If anything goes wrong during export
        tkinter.messagebox.showerror("Error", "Couldn't export!")


# Program starts here as it calls the main() function which then sets up the GUI screen leaving it ready for the user to interact with.

# This line ensures the main() function only runs when the file is executed directly.
if __name__ == "__main__":
    main()