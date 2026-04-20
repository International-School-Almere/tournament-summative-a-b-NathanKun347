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
Session [03]
Date: 19/03/2026
Time spent: 8 hours
Focus: Score Entry System and Point Calculation - Making Enter scores work with actual input fields and automatic point calculation
Problems / Challenges


3 hours was spent understanding how to create an Entry widget for each participant dynamically.


I was very confused on how to map the values of the Entry fields back into the appropriate list of participants.


Index Errors continually popped up whenever I tried to access teams[i] when less than 4 teams were registered.


I had trouble at first as to why the dictionary used the event number as the key.


I was very confused on why the sorting algorithm needed to work on its own and was trying to use the built-in function. For BTEC I needed to demonstrate I understood how sorting works so it had to be a custom sort.


Took me 2 hours to get the point calculation to give correct points. I forgot how tied positions should have the same rank and then the following rank after the tie should skip forward.


The calculation points function crashed when I gave it empty score lists; needed to have checks for these scenarios.


Solutions / Actions Taken


I consulted YouTube and found the following tutorial on "Python tkinter dynamic widgets tutorial."


I used a Frame widget for the entry of the individual scores and another one for the teams' scores to separate the sections cleanly.


I created a parallel list of Entry widgets for each of the teams and individuals registered to ensure each widget was assigned correctly.


I manually programmed bubble sort for BTEC to prove my understanding of sorting algorithms.


I ensured the correct rank was assigned after tied positions by skipping the following position in the sort.


Before each point calculation I reset all point values to zero so there wasn't double counting occurring.


I programmed a function called change_event and have added this to the dropdown menu so that the current event is updated.


Evidence


[Added code] - The score entry window is dynamically created with the appropriate amount of Entry fields based on the number of participants.


[Added code] - The calculation_points function works with the sorting algorithm I coded manually which also deals with ties appropriately.


[Added code] - The event dropdown menu has been wired up using a function called change_event().


[Researched source] - Stack Overflow: "Python bubble sort implementation"


[Screenshot] - A view of the score entry window with registered participants.


Reflection


What went well? The score entry window dynamically updates based on registered participants. The bubble sort implementation works and handles ties as needed. The points calculation for teams and individuals updates correctly.


What needs improvement? The empty slot filler which is creating unused Entry fields is still quite messy. Although the sort function is O(n) it will not affect the speed very much due to the small number of registered users but I would consider a faster algorithm if there was likely to be more than 20–30 registered users. I also want to add feedback to the score entry so you can immediately see how the scores are affecting the totals.


What did I learn? Toplevel can be organized using Frame widgets to keep it tidy. You can create dictionary keys by concatenating strings. Bubble sort is easy to understand and implement but is not very efficient. Remember to reset totals before recalculating!



---

---


# 7. Problems and Fixes

| Problem | Cause | Fix | Status |
|---|---|---|---|
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |
| [Describe issue] | [Why it happened] | [What you did] | Open / Fixed |

---

# 11. Final Reflection

> Complete this section at the end of the project.

## What I achieved
- 
- 
- 

## What worked well
- 
- 
- 

## What did not work well
- 
- 
- 

## What I would improve next time
- 
- 
- 

## Final outcome
[Describe the final result]

## Did I meet the success criteria (designspecifications)?
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Final evaluation
[Write a short final judgment of the project]

---
- 
