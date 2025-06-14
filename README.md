# Grid Jump Designer

A lightweight visual tool built with Python and Pygame to design and test 2D movement patterns based on custom "jump" vectors. Originally inspired by knight-like moves in chess, this project allows users to explore how directional sequences generate paths on a grid.

---

## Project Overview

The tool takes a string of digits (0–7), each representing a direction, and simulates movement across a grid. The movement is defined by customizable X and Y jump values. It displays the resulting path step-by-step using labeled blocks, providing real-time visual feedback as users edit the input string.

---

## Features

- Real-time drawing of paths on a grid
- Configurable X and Y jump values
- Editable jump string via interactive textbox
- Visual block labeling (a, b, c, …) to trace path
- Mouse and keyboard support:
  - Live editing
  - Cut, copy, paste, undo
  - Shift+Arrow for text selection

---

## How It Works

- Digits `0` to `7` correspond to 8 possible movement directions.
- You define how far each move jumps in the X and Y directions (`jumpx`, `jumpy`).
- The path is drawn by applying each move in sequence, avoiding revisiting previous cells.
- The grid resizes and centers automatically based on the path's size.


