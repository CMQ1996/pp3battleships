# Battleships Game

Developer: Cormac McQuillan ([CMQ1996](https://www.github.com/CMQ1996))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/CMQ1996/pp3battleships)](https://www.github.com/CMQ1996/pp3battleships/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/CMQ1996/pp3battleships)](https://www.github.com/CMQ1996/pp3battleships/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/CMQ1996/pp3battleships)](https://www.github.com/CMQ1996/pp3battleships)
[![Deployment](https://img.shields.io/badge/deployment-Heroku-purple)](https://pp3battleships-704cde5f0e84.herokuapp.com)

---

##  Project Introduction and Rationale

This project is a **terminal-based Battleships game written in Python**. It demonstrates key programming concepts such as lists, loops, functions, random number generation, and input validation.

The game generates a 5x10 grid and randomly places a single hidden battleship. The player must guess its location by entering row and column coordinates. After each guess, the game provides feedback and updates the board.

This project was created as a learning exercise to strengthen understanding of Python logic, control flow, and user input handling.

---

## UX (User Experience)

### 1. Strategy

**Purpose**
- Create an interactive command-line game where the user finds a hidden battleship.
- Demonstrate Python fundamentals in a practical project.

**User Needs**
- Simple and intuitive gameplay
- Clear feedback after each guess
- A complete game loop until the ship is found

**Project Goals**
- Demonstrate Python programming skills
- Show understanding of loops, functions, and validation
- Create a beginner-friendly interactive game

---

### 2. Scope

**Features**
- 5x10 grid-based board
- Random battleship placement
- Row and column user input
- Input validation
- Hit and miss feedback
- Board updates after each guess
- Win condition when ship is found

---

### 3. Structure

**User Flow**
1. Game starts and board is displayed

![Initial board](images/game%20start.png)

2. User enters row guess
3. User enters column guess
4. System checks result
5. Board updates after each guess

![Missed ship example](images/missed%20ship%20example.png)
6. Repeat until ship is found
7. Game ends and final board is shown

![Win screen](images/victory%20image.png)

---

### 4. Skeleton

**Layout**
- Terminal-based grid (5 rows × 10 columns)
- Numeric input prompts for row and column guesses

![Input example](images/game%20start.png)

---

### 5. Surface

**Visual Design**
- Text-based grid interface
- Symbols:
  - `0` = unexplored cell
  - `X` = miss
  - `S` = ship (revealed on win)

---

## GAME FEATURES

### Game Board
A 5x10 grid created using nested lists in Python.

![Gameplay board](images/game%20start.png)

---

### Random Ship Placement
A single battleship is randomly placed using Python’s `random` module.

---

### Input Validation
Ensures:
- Row input is between 0–4
- Column input is between 0–9
- Only valid integers are accepted

![Validation error](images/valid%20input%20pass%200.png)

---

### Gameplay Loop
The game continues until the player successfully finds the battleship.

---



## TESTING

### Manual Testing

The game was manually tested to ensure all core functionality works as expected, including valid gameplay, invalid input handling, and win conditions.

| Test Case | Input | Expected Result | Actual Result |
|-----------|------|----------------|---------------|
| Valid row input | 2 | Accepted | Pass |
| Invalid row input | "a" | Error message shown | Pass |
| Valid column input | 5 | Accepted | Pass |
| Out of range column | 99 | Error message shown | Pass |
| Correct guess | Matching ship coordinates | Win message displayed | Pass |

### Manual Testing Evidence

The following screenshots demonstrate successful manual testing of key features:

- Valid input accepted  
![Valid input](images/valid%20col%20input%205.png)

- Invalid row input handling  
![Invalid row](images/invalid%20row%20input%20a.png)

- Invalid column input handling  
![Invalid column](images/valid%20col%20input%205.png)

- Game win condition  
![Win screen](images/victory%20image.png)

---

## CODE VALIDATION (PEP8 CI)

The Python code was validated using the CI Python Linter to ensure PEP8 compliance.

- All Python files passed validation with no major errors.
- Minor style warnings were reviewed and corrected where necessary.

| File | Validation Tool | Result | Screenshot |
|------|----------------|--------|------------|
| run.py | PEP8 CI Linter | Pass | ![PEP8 validation](images/Pep8%20validator..png) |

---

## BUGS

### Fixed Bugs

- Fixed issue where non-integer input caused the program to crash by implementing `try/except` validation.
- Fixed out-of-range input allowing invalid board positions.
- Fixed repeated input crashes during gameplay loop.

### Unfixed Bugs

- No known unfixed bugs at time of submission.
---

## TECHNOLOGIES USED

- Python 3
- Random module
- W3Schools
- CodeAcademy
- Youtube
- ChatGPT
---

## FUTURE IMPROVEMENTS

- Add multiple battleships
- Limit number of guesses
- Add difficulty levels
- Improve board display with coordinates
- Prevent repeated guesses

---

## DEPLOYMENT

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of **KEY** to `PORT`, and the **VALUE** to `8000` then select **ADD**.
- If using any confidential credentials, such as **CREDS.JSON**, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important; select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs some additional files in order to deploy properly.


![Deployment screenshot](images/deployed%20in%20heroku.png)

---

## FINAL NOTE

This project demonstrates fundamental Python programming concepts through an interactive Battleships game built in a command-line environment. I based this project off Codeacademies pracitice Battleships game, however I customised the code to my own design. 
Codeacademy video link: https://www.youtube.com/watch?v=7Ki_2gr0rsE&t=935s