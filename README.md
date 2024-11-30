# Elevator

# Elevator Simulation in Python 3.13🚀

This project is a terminal-based elevator simulation for a 9-story building (including 2 garage floors: -1, -2). The elevator moves between floors based on passenger requests, with realistic weight constraints and floor movement animations. The project demonstrates object-oriented programming concepts and random passenger generation using the `Faker` library.

## Features
- A building with 9 floors (from floor -2 to floor 9).
- Each floor can spawn random passengers with:
  - Random names
  - Random weights (50-120 kg)
  - Random floor requests (up or down)
- The elevator has a weight limit of 700 kg and cannot take more passengers once the limit is exceeded.
- The elevator moves up and down between floors, stopping to pick up or drop off passengers.
- A terminal-based animation shows the elevator icon (`🛗`) moving between floors.
- Passenger details (name, weight, current floor, and target floor) are displayed in the terminal.
  
## Requirements
- Python 3.x
- Faker library (`pip install faker`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/elevator-simulation.git

Navigate to the project directory:
cd elevator-simulation

Install the dependencies:
pip install faker

How to Run
python3 main.py



Example Output:

Passenger spawned: John Doe (Weight: 82 kg) at Floor 7 going to Floor -1
Passenger spawned: Jane Smith (Weight: 75 kg) at Floor 3 going to Floor 9

🛗 Floor 7: John Doe (82 kg)
Going down... ding... ding... ding...
Stopping at Floor -1: John Doe exited

🛗 Floor 3: Jane Smith (75 kg)
Going up... ding... ding... ding...
Stopping at Floor 9: Jane Smith exited

