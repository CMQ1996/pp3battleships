# Battleships Game

Developer: Cormac McQuillan ([CMQ1996](https://www.github.com/CMQ1996))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/CMQ1996/pp3battleships)](https://www.github.com/CMQ1996/pp3battleships/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/CMQ1996/pp3battleships)](https://www.github.com/CMQ1996/pp3battleships/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/CMQ1996/pp3battleships)](https://www.github.com/CMQ1996/pp3battleships)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://pp3battleships-704cde5f0e84.herokuapp.com)

---

## ⚠️ PROJECT INTRODUCTION AND RATIONALE ⚠️

This project is a simple **terminal-based Battleships game written in Python**. The purpose of the game is to demonstrate core programming concepts such as lists, loops, functions, random number generation, and input validation.

The game generates a 5x10 grid and randomly places a single hidden battleship on the board. The player must attempt to locate and sink the battleship by entering row and column guesses. After each guess, the game provides feedback on whether the player has hit or missed the target and updates the board accordingly.

This project was created as a learning exercise to strengthen my understanding of Python logic and control flow, particularly around loops, conditionals, and user input handling. The Battleships theme was chosen because it provides a clear, interactive, and engaging way to apply these fundamental programming concepts.

---

## 🛑 README NOTES 🛑

Do not add a **Table of Contents** to Markdown files. GitHub generates this automatically.

Store project documentation such as wireframes, testing, and screenshots in a `/documentation` folder rather than `/assets` or `/static`.

---

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**

* Provide an interactive command-line game where users attempt to find and sink a hidden battleship.
* Demonstrate core Python programming concepts through gameplay.

**Primary User Needs**

* A simple and easy-to-understand game interface.
* Clear feedback on guesses (hit or miss).
* Continuous gameplay until the ship is found.

**Business Goals**

* Showcase Python development skills.
* Demonstrate understanding of loops, functions, and input validation.
* Provide an engaging beginner-level game experience.

---

#### 2. Scope

**Features**

* 5x10 grid-based game board
* Random placement of a single battleship
* User input for row and column guesses
* Input validation to prevent invalid entries
* Hit and miss feedback system
* Board updates after each guess
* Win condition when the battleship is found

---

#### 3. Structure

**Information Architecture**

* The game runs in a single linear flow within the terminal.

**User Flow**

1. Game starts and board is displayed
2. User enters row guess
3. User enters column guess
4. System checks result
5. Board updates with hit or miss
6. Repeat until ship is found
7. Game ends and final board is displayed

---

#### 4. Skeleton

**Layout**

* Terminal-based grid display (5 rows x 10 columns)
* Numeric input prompts for row and column guesses

---

#### 5. Surface

**Visual Design Elements**

* Simple text-based grid interface
* Symbols used:

  * `0` = unexplored cell
  * `X` = miss
  * `S` = ship (revealed on win)

---

## GAME FEATURES

### Game Board

A 5x10 grid is generated using nested lists.

### Random Ship Placement

A single battleship is randomly placed using Python’s `random` module.

### Input Validation

User input is validated to ensure:

* Row is between 0–4
* Column is between 0–9
* Only valid integers are accepted

### Gameplay Loop

The game continues until the player correctly guesses the ship location.

---

## TESTING

### Manual Testing

* Tested valid and invalid row inputs
* Tested valid and invalid column inputs
* Confirmed game ends when ship is found
* Verified board updates correctly after each guess

---

## TECHNOLOGIES USED

* Python 3
* Random module

---

## FUTURE IMPROVEMENTS

* Add multiple battleships
* Limit number of guesses
* Add difficulty levels
* Improve board display with coordinates
* Prevent repeated guesses

---

## DEPLOYMENT

This project is deployed using Heroku:
https://pp3battleships-704cde5f0e84.herokuapp.com

---

## FINAL NOTE

This project demonstrates fundamental Python programming concepts through an interactive Battleships game built in a command-line environment.
