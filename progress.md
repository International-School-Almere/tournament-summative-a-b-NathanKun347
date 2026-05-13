# Progress Journal

> Use this journal to track progress, decisions, problems, and next steps.
> Update it after each work session.
> 
---

# 1. Project Overview

## Project Title
Nathan Tournament summative A-B

## Project Description
[Briefly explain what the project is about]

## Start Date
[Unknown / add later]

## Target End Date
[Unknown / add later]

## File list.

## (Dependencies) API / library / module list.
---


# 2. Progress Log

> Add a new session at the top each time you work.

---
## Session [01]
**Date:** [15/04/2026]  
**Time spent:** 4 hours
**Focus:** researching about TKinter and how to set up the GUI as well as understanding requirements for the assignment.

### Problems / Challenges
- Forgotten some of the ways to get Tkinter running
- Kept getting errors because i forgot mainloop()
- Confused about differece of pack(), grid() and place()

### Solutions / Actions Taken
- Watched full youtube tutorial by DJ Oamen about Tkinter and GUI in a similar program + research on websites like w3schools
- Set up global variables list although I still lacked some understanding about dictionaries (reffered to pokidex librabry for assistance)

### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- DJ Oamen python tournament system on Youtube
- image visible in file of w3schools

### Reflection
- I planned the 5 events and 20 individuals quite well and finally got the window to appear after a long time of errors. I am behind and the empty functions need to be made to actually do something. I still am unsure about how to pass data between windows.
- I need to make more progress with the buttons I just introduced
- I learnt how to set up Tkinter properly without it closing.


## Session [02]
**Date:**  [17/04/2026] 
**Time spent:** [8 hours]  
**Focus:** Making the registration function - actually getting the button to function with the window pop up and data storage

### Problems / Challenges
- Took around 2 hours trying to understand Toplevel() and how to create and import it correctly.
- Kept getting errors of StringVar not updating then I finally noticed that it was because I was missing get() method.
- I struggled with the buttons logically as well, I kept trying "radio==True:" instead of "radio.get()"

### Solutions / Actions Taken
- To solve the first issue, I watched Tkinter.com's tutorial video on youtube titled, "New Top Level Windows - Tkinter CustomTkinter 15". I then applied the logic to resolve the issue.
- The fix was to add both StringVar and .get() for radio button values
- Just reread over my work and searched up on internet to reoslve the minor logic issue.

### Evidence
- [Added code]
- [Updated design]
- [Created sketch]
- [Researched source]
- [Uploaded image/screenshot]

### Reflection
- Something that went well is that the registration pop up finally works properly after having to learn how Toplevel() works.
- What needs improvement?
- What did I learn?

---
## Session [03]
**Date:** 19/03/2026  
**Time spent:** 8 hours  
**Focus:** Score Entry System and Point Calculation - Making Enter scores work with actual input fields and automatic point calculation  

### Problems / Challenges
- 3 hours was spent understanding how to create an Entry widget for each participant dynamically.
- I was very confused on how to map the values of the Entry fields back into the appropriate list of participants.
- Index Errors continually popped up whenever I tried to access teams[i] when less than 4 teams were registered.
- I had trouble at first as to why the dictionary used the event number as the key.
- I was very confused on why the sorting algorithm needed to work on its own and was trying to use the built-in function. For BTEC I needed to demonstrate I understood how sorting works so it had to be a custom sort.
- Took me 2 hours to get the point calculation to give correct points. I forgot how tied positions should have the same rank and then the following rank after the tie should skip forward.
- The calculation points function crashed when I gave it empty score lists; needed to have checks for these scenarios.

### Solutions / Actions Taken
- I consulted YouTube and found the following tutorial on "Python tkinter dynamic widgets tutorial."
- I used a Frame widget for the entry of the individual scores and another one for the teams' scores to separate the sections cleanly.
- I created a parallel list of Entry widgets for each of the teams and individuals registered to ensure each widget was assigned correctly.
- I manually programmed bubble sort for BTEC to prove my understanding of sorting algorithms.
- I ensured the correct rank was assigned after tied positions by skipping the following position in the sort.
- Before each point calculation I reset all point values to zero so there wasn't double counting occurring.
- I programmed a function called change_event and have added this to the dropdown menu so that the current event is updated.

### Evidence
- [Added code] - The score entry window is dynamically created with the appropriate amount of Entry fields based on the number of participants.
- [Added code] - The calculation_points function works with the sorting algorithm I coded manually which also deals with ties appropriately.
- [Added code] - The event dropdown menu has been wired up using a function called change_event().
- [Researched source] - Stack Overflow: "Python bubble sort implementation"
- [Screenshot] - A view of the score entry window with registered participants.

### Reflection

#### What went well?
The score entry window dynamically updates based on registered participants. The bubble sort implementation works and handles ties as needed. The points calculation for teams and individuals updates correctly.

#### What needs improvement?
The empty slot filler which is creating unused Entry fields is still quite messy. Although the sort function is O(n) it will not affect the speed very much due to the small number of registered users but I would consider a faster algorithm if there was likely to be more than 20–30 registered users. I also want to add feedback to the score entry so you can immediately see how the scores are affecting the totals.

#### What did I learn?
Toplevel can be organized using Frame widgets to keep it tidy. You can create dictionary keys by concatenating strings. Bubble sort is easy to understand and implement but is not very efficient. Remember to reset totals before recalculating!


## Session [04]

**Date:** 20/03/2026  
**Time spent:** 1 hour  
**Focus:** Implement leaderboard display. The "View Leaderboard" button will display current rankings.

### Problems / Challenges
- Only had one hour as next class started at 2pm and had to finish it by 1pm.
- Forgot how to create a Listbox widget. Kept trying to use label which doesn't scroll well.
- Difficulty understanding how to sort both team and individual data together within one list.
- Attempted to use Python's sort() function before realizing the assignment required manual sorting.
- Couldn't remember listbox syntax (insert(END, ...) versus append()).

### Solutions / Actions Taken
- Used the tkinter's Listbox widget for the display.
- Created a single list to hold both team and individual scores for unifying ranking and displayed as tuples (Score, Name).
- Re-used the bubble sort pattern from calculating points to make it consistent with the rest of the code.
- Included header row (Rank, Player/Team, Score) and a horizontal line separator for improved readability.
- Used END constant for inserting new data into the listbox.

### Evidence
- [Attached Code] - Functioning leaderboard popup with listbox display.
- [Attached Code] - Updated leaderboard button functionality.
- [Attached Screenshot] - Screenshot of the leaderboard showing test data with correct ranking order.

### Reflection

#### What went well?
Leaderboard is now visible and correctly sorts both teams and individuals together. The Listbox widget supports scrolling if the data is too large. Bubble sort algorithm used in the leaderboard implementation is consistent with other scoring aspects.

#### What needs improvement?
Was unable to implement a save/load system due to lack of time (only 1 hour before the next class). The leaderboard does not update automatically as scores change; the button must be clicked each time for it to refresh. No visual cue to highlight the current leader.

#### What did I learn?
Listbox widget is suitable for displaying lists of text. Using insert(END, ...) adds items to the bottom of the listbox. Combining data from different sources into a single list is possible using tuple structure. Bubble sort works regardless of the data types being sorted as long as they can be compared.

---
## Session [05]
**Date:** 24/03/2026  
**Time spent:** 3 hours  
**Focus:** Saving and loading data between runs of the program using text files.

### Problems / Challenges
- Took an hour to decide how to format the file ( CSV seemed to complex and went for a simple custom format with a pipe delimiter instead).
- Had issues with 'File Not Found' exceptions when loading but there wasn't a file to load from.
- Got confused about how to write out the nested score data ( participant score).
- Completely forgot to save each participant's events. This was a backward step.
- Had issues with loading data from the text file; code would error when trying to cast back to integers.
- Spent 30 minutes trying to fix a bug which was stopping loaded participants from having their names loaded. The members list was not being correctly saved.

### Solutions / Actions Taken
- Used a simple text file save.txt with section headings ( TEAMS, INDIVIDUALS, SCORES ).
- Used try-except blocks for file loading to gracefully handle cases where no file was present.
- saved the participant's members as a CSV in between the other delimited fields.
- Added a strip() statement to remove newline characters before reading the data from a line.
- Added a section tracking variable to track which section of the text file the parsing function was in.
- Used split("|") on read data to reconstruct each line from it's separate fields.

### Evidence
- [Code Added] The save function is writing out data to the text file.
- [Code Added] The load function is reading data back in from the text file.
- [Tested] Registered participants, save and close, re-open and load – all works.
- [Screenshot] showing a successfully loaded data file named save.txt.

### Reflection

#### What went well?
Save and load are both functional, proved by loading the program and seeing registered members in it. The use of a custom pipe-delimited format with section headers simplifies the saving and loading logic greatly, as it's easy to manage where one section begins and ends and the pipe avoids commas appearing within participant names.

#### What could be better?
The current text format is very brittle - manually editing this file will likely crash the load function. Also, there is currently no validation built in to check that data being loaded adheres to current tournament rules (e.g. The ability to load 5 teams when a maximum of 4 are registered). The 'except:' in the load function is very general; should be more specific in terms of what error type can be expected.

#### What I learned?
File IO requires closing the file, and I must remember to save all relevant data (like members' associated events). Strip() is essential to deal with newline characters read from a file, and the split() function is crucial for parsing the data that uses a specific delimiter. Organizing different types of data in a single text file requires using section headers. Global variables need to be explicitly declared with global within any function that is intended to entirely overwrite the existing global variable.

## Session [06]

**Date:** 29/04/2026  
**Time spent:** 6 hours  
**Focus:** Export function, final testing, bug fixes and code completion

### Problems / Challenges
- Export format takes 2 hours to develop as it needs to be professional for the college.
- Still confusing write() and print(), with write() not automatically having a newline.
- Integers are not getting to the export file, results in TypeError.
- No proper formatting of the export file was available, so the file look untidy.
- Had to implement headers, separators, and structured parts to the file to make it readable.
- Full tournament workflow testing (register, score, calculate, export) took an hour.
- Bug where calculate_points() crash when no scores have been entered was found, had to include checks.
- Found that loading doesn't restore events list of individuals/teams, this had to be fixed.

### Solutions / Actions Taken
- A well formatted export file was developed to be professional with title, standings and event analysis sections.
- String multiplication was used to create easy to read separators ("=" * 40).
- Newlines were included into the write function (write("\n")).
- The complete tournament workflow was tested end-to-end.
- The missing events list in load was fixed by default loading to [1,2,3,4,5].
- Detailed comments are present which explain the structure of the export file.
- All 6 buttons now work together in a sequence.

### Evidence
- [Code was added] - export function used to create formattted results.txt.
- [Bug fix] - Events list is now restored from loading function correctly.
- [Testing] - A full tournament was played with 2 teams and 3 individuals, two events were scored.
- [Screenshot] - Shows a formatted result.txt file with clearly visible sections.
- [Final checks] - FR-001 to FR-008 are all now successfully implemented.

### Reflection

#### What went well?
The export function works correctly and produce a professional report with sections, the load bug was fixed, and all 6 buttons now operate perfectly when working together through the tournament's workflow; which is (register 2 teams and 3 individuals, enter scores for 2 events, view leaderboard, save and export).

#### What needs improvement?
More details are needed in the report such as per-participant event score breakdown. Loading file is not robust and can be crashed by validation errors on loading, so it should be improved, and also an additional "Clear All" button should be added to reset the system.

#### What did I learn?
The use of string multiplication ( "=" * 40 ) simplifies visual separators. A structured and well-formatted report needs clear sections with relevant headings. Testing the whole workflow of the tournament is very crucial, not just the features individually. Fixing one function (load) may affect other components, so thorough testing is mandatory.

## Session [07]

**Date:** 13/05/2026  
**Time spent:** 4 hours  
**Focus:** Essential GUI screen fixes - scrollable popups, Mac window management, and leaderboard bug fix, narrowed GUI screen for registration

### Problems / Challenges
- The score entry window currently shows 20 individuals alongside 4 teams and eaders This is way too narrow and tall for a normal laptop screen(with feasible font size etc.)
- Users cannot see the bottom of the screen that they are meant to press in order to save the progress because it is cut off.
- A scroll bar or much smaller layout is required for the score entry.

### Solutions / Actions Taken
- The score entry window has now become scrollable. Created a scrollbar and a Canvas. This works similar to a webpage with the use of a Canvas. It was not easy and not my prefferred method as I still have to scroll by dragging the slider downwards (Cannot scroll with a mouse or touchpad like usual but it allows full visibility and is not super time consuming thus making it worth it).
- Added window.attributes('-topmost', True) so that the window remains on the current Mac desktop environment.
- Used wm_attributes for Mac specific window behaviour.
- The score entry window is set to show only a maximum number of people or teams so all can be viewed. The rest is accessible using scroll bar. This works because the UI was also narrowed to make this possible.
- Registering window is now also scrollable.
- Created center_popup() helper that will center all popups in the middle of the screen.
- CRITICAL FIX: Added eventstr = str(eventnum) and checking for both int and string forms.
- Successfully tested this on the Mac. All windows no longer have to be searched via Spaces and the leaderboard is showing correct scores.

### Evidence
- [Fixed UI] - The Registration pop up now correctly displays all the information in the window with the Register button visible.
- [Fixed UI] - The stack of people and teams are now displayed vertically with the correct spacing.
- [Fixed UI] - All pop up windows are now shown centrally on the screen, on the current desktop environment.
- [Fixed bug] - The Leaderboard now correctly displays points after data has been entered and loaded.
- [Screenshot] - Score entry window showing the new scroll bar which is now fully functional.
- [Screenshot] - Leaderboard showing a non-zero score.

### Reflection

#### What went well?
The scrollable popups have worked great and I am now able to view all 24 people, as well as the register button. The Mac window management has been successfully sorted and all windows will stay in the current desktop space. The crucial leaderboard bug has also been solved, the points calculation is correct.

#### What needs improvement?
The UI design is basic, it would be nice to change some colors and styles later. The scroll bar is functional but doesn't look brilliant. The maximum number of people will need to be tested with, specifically 4 teams + 20 people.

#### What did I learn?
Canvases and scroll bars in Tkinter allow for the creation of scrollable frames. The way Windows and Mac manage windows are fundamentally different and I have learnt that top-most attribute needs to be used in conjunction with window attributes. When saving information and reading it from a JSON file, an integer could become a string, this can lead to errors if you are not prepared to test every variable. This has highlighted the importance of tracing all data within the program.
# 7. Issues & Resolutions

| Problem | Reason | Fix | Status |
|---|---|---|---|
| UnboundLocalError while registering participants | `global teams, individuals` was omitted within the `register()` function and Python requires an explicit statement to modify global lists | Added `global teams, individuals` at the beginning of the function and researched Python variable scope rules | Fixed |
| Registration popup not appearing when the **Register** button was clicked | The behavior of `Toplevel()` and how it creates secondary windows independently of the main `Tk()` root window was not fully understood | Watched a Python `Toplevel()` tutorial, analyzed the classroom password manager example, and created the popup using `geometry()` and `title()` correctly | Fixed |
| Empty name fields being added to the system | No validation was performed on the `name` `Entry` widget before appending it to the participant list | Added `if not name:` validation using `tkinter.messagebox.showerror()` to prevent invalid registrations and provide user feedback | Fixed |
| Duplicate participant names could be registered | No logic existed to compare the newly entered name against all existing entries in the `teams` and `individuals` lists | Implemented a linear search using nested `for` loops to compare the input with all previously registered names | Fixed |
| Index errors when the Score Entry window accessed `teams[i]` | Fewer than four teams were registered, causing `list index out of range` when attempting to access non-existent elements | Added `if i < len(teams):` before accessing list elements and used placeholders for unused slots | Fixed |
| Points were calculated incorrectly when scores were updated multiple times | `calculate_points()` continued adding to existing totals rather than resetting and recalculating them | Added two `for` loops at the beginning of the function to reset all point values to `0` before recalculating | Fixed |
| `FileNotFoundError` when pressing Load without an existing save file | The program attempted to open `save.txt` without checking whether the file existed | Wrapped file operations in a `try-except` block and displayed a user-friendly error message if the file was missing | Fixed |
| Missing events data after loading a file | The save file did not store the `events` list associated with each participant | Added a default `"events": [1, 2, 3, 4, 5]` when recreating participant dictionaries during loading | Fixed |
| Export reports were poorly formatted and unprofessional | Output generated by `write()` lacked structure and formatting | Created a structured report with a title, separator lines (`"=" * 40`), and ranked participant standings | Fixed |
| `current_event` did not update when selecting a different event | No callback function was attached to the `OptionMenu` | Added `command=change_event` and used `selection.split()[1]` within the function to extract the selected event number | Fixed |
| Bubble sort failed on edge cases involving empty or single-item lists | The loop ranges were not suitable when `score_list` contained zero or one element | Added checks for small lists and ensured loops only ran when the list contained more than one item | Fixed |
| Tied scores were assigned incorrect rankings and point values | Points were originally assigned according to list position rather than actual ranking with ties | Introduced a `last_score` variable to detect equal scores and assign the same rank and points | Fixed |

---

## 11. Final Reflection/ evaluation for distinction

> Write the contents of this section at the end of your project.

---

# 7. Issues & Resolutions

| Problem | Reason | Fix | Status |
|---|---|---|---|
| Points added to current total rather than restarting calculation | Added points to current total rather than restarting the calculation | Added 2 for loops at the start of the function to reset points for each point entry before re-calculating | Fixed |
| FileNotFoundError on loading when no save.txt file existed | The code was trying to open the save.txt file when none existed | Code wrapped in a try-except block to catch the error and tell the user about this | Fixed |
| Missing events on loading save.txt file | Each event list for the participants was not stored in the save.txt file | When reloading the participant dictionaries, added a default `"events": [1,2,3,4,5]` for each participant if it was missing | Fixed |
| Poor quality & unprofessional report output | The print/write() did not have sufficient formatting | Created an organized report including titles and separators (`"=" * 40`) along with sorted standings | Fixed |
| `current_event` value not changing when changing to a different event | The OptionMenu didn't have a callback function set | Added `command=change_event` and used `selection.split()[1]` inside the function to extract event number | Fixed |
| Edge cases for Bubble Sort failing when the list was too small | Loops ran at invalid values for score list sizes of 0 or 1 | Added conditions to the loops, stating that if the list had more than 1 entry, then it will run the loops | Fixed |
| Tied scores wrongly allocated to ranking/points | Original points allocated based on position on the score list, not the actual rank (considering ties) | A `last_score` was used to compare scores, this made sure tied scores were given the same value/rank | Fixed |

---

# 11. Final Reflection / Evaluation

## What I achieved
I successfully created a fully functional GUI application using Python which is fully capable of performing all tournament score keeping. This program, named "Tournament Scoring System," allows a user to enter team names, participants, enter each score, and display rankings. This project was the first one where I have truly understood the concept of nested lists, lists of lists and dictionaries, as these were heavily involved in my program. I made a custom bubble sort algorithm which worked effectively and in fact handled tied scores without having to use any pre-programmed sorts, and was very excited about that. The program includes features for opening and saving files, in addition to the custom way of saving and loading data I came up with. Furthermore, the project demonstrates my understanding of multiple windows and how to effectively integrate them. My programming also highlighted my abilities to write reliable, well validated code as there are several input validations in place and it's robust enough to handle multiple different types of exceptions. In essence, my program successfully implemented and developed the entire SDLC in a project for Unit 4, from the conceptual stage to a finished piece.

---

## What worked well
I had very well organized, function-based code which makes it easily readable and understandable. I feel that the bubble sort algorithm implemented clearly demonstrates my programming capabilities. The way in which I stored data and wrote it into a file was very organized and effective. It's very efficient at storing the vast amounts of different data and allows me to correctly re-load everything I need to when reading. Tkinter was reliable, the whole program gave a smooth, professional and efficient user experience with very good layout. Input validation was extremely useful and efficient in helping the user fill out everything and prevent them from making errors.

---

## What did not work well
Using pack() as a layout manager was one of the things that did not go well. It became incredibly difficult to organize the widgets as my program got bigger and the spacing became increasingly unbalanced, making the program look less and less professional. Registering an 'Individual' member should not have prompted all the team fields to come up. The fact that I can't add new individuals and teams after the initial registration and that the blank spaces for the fields still exist after registering are things which should be avoided in future applications. Having no option to edit and delete already saved teams and individuals is another thing that was definitely lacking. Writing to a file using the format I did also had its vulnerabilities. Corruption would occur if any file editor was used that didn't exactly follow that format and it could even delete my file if I made a mistake writing it in the file. The saving/loading of events data were also being lost, and you also lose data this way. Having a massive amount of global variables makes things a lot harder to work with than it needed to be.

---

## What I would improve next time
I would probably switch to using the grid() manager for the layout rather than pack() in order to get everything organized perfectly. The biggest thing I would improve is to introduce object-oriented programming, to make the program cleaner and easier to work with. Having buttons for editing and deleting registered teams and individuals would also significantly improve the usability of the program. If there's no valid file present and I press "Load", a simple message will show up and a default template will be filled, allowing the user to use the program to enter new scores even if it's their first time using it. If I were writing to a pipe-delimited text file, I'd add code so that it wouldn't overwrite all of your data if you made a mistake when using a text editor or if some unexpected event occurred, rather than completely wipe it out. The missing events data issue would also be addressed more thoroughly, possibly storing them more securely or having them re-initialized correctly. I'd try to reduce the number of global variables.

---

## Final outcome
The Tournament Scoring System is a complete and fully functional GUI Python program, capable of performing all specified operations for Unit 4. It is capable of entering teams of up to five individuals and 20 individuals with individual IDs, scores for five defined events, automatic calculation and display of real-time scores and leaderboards, saving and loading of tournament data into a text file, and professional reporting. The project spanned over 6 documented sessions where it evolved from a prototype to its current fully functional state and has demonstrated my capabilities with Tkinter, advanced data structures, algorithmic programming and thorough exception handling.

---

## Did I meet the success criteria (design specifications)?
- [x] FR-001: Participant Registration - Register 4 teams of 5 members each and 20 individual competitors with unique ID assignment.
- [x] FR-002: Event Definition - Support exactly 5 distinct events with team and individual participant types.
- [x] FR-003: Scoring System - Award points using the distribution [20, 18, 16, 14, 12, 10, 8, 6, 4, 2] with tie handling.
- [x] FR-004: Flexible Entry - Allow full tournament or selected event participation.
- [x] FR-005: Real-time Scoring - Input raw scores and automatically calculate rankings and points.
- [x] FR-006: Leaderboard Display - Show a live combined ranking of teams and individuals.
- [x] FR-007: Results Export - Generate a formatted results.txt report.
- [x] FR-008: Data Validation - Prevent duplicate names, empty entries, invalid types, and exceeded limits.
- [x] NFR-001: Usability - Intuitive GUI with clear labels, buttons and feedback.
- [x] NFR-002: Reliability - Save/load functionality and exception handling prevent data loss and crashes.
- [x] NFR-003: Performance - Instant updates with acceptable O(n) complexity for fewer than 30 participants.
- [x] NFR-004: Portability - Runs on standard Windows PCs with Python 3.x and Tkinter.
- [x] NFR-005: Maintainability - Well-commented procedural structure that is easy to modify.

---

## Final evaluation
This project exhibits distinction-level programming skills by integrating a robust GUI, advanced data structures, a custom sorting algorithm, comprehensive input validation, file handling capabilities, and exception management. The implementation of a bubble sort algorithm with accurate handling of tied scores directly addresses the requirements for demonstrating algorithmic understanding at the distinction level. The system effectively manages the entire tournament lifecycle, from data input to report generation, while ensuring data integrity and user-friendliness. Despite the limitations of pack() layout and a purely procedural approach, the core functionality is stable and meets all specified design criteria. The project's iterative development across six documented sessions highlights strong problem-solving and project management skills, making it a significant achievement that fulfills the criteria for a distinction grade for Unit 4 Programming.