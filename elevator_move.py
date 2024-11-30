import os
import time

icon = "🛗"


class ElevatorMove:
    def __init__(self, door_logic):
        self.door_logic = door_logic
        self.current_floor = 0
    
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def animate_movement(self, target_floor, floor_dict):
        step = 1 if target_floor > self.current_floor else -1
        for floor in range(self.current_floor, target_floor + step, step):
            self.clear_terminal()
            for f in floor_dict:
                if f == floor:
                    print(f"{f}: {floor_dict[f]} {icon}")
                else:
                    print(f"{f}: {floor_dict[f]}")
            time.sleep(1)
        self.current_floor = target_floor
        
    
    def handle_passengers(self, passengers, floor_dict):
        while passengers:
            passengers.sort(key=lambda p: abs(self.current_floor - p.current_floor))
            next_passenger = passengers[0]
            print(f"Heading to {next_passenger.current_floor} to pick up {next_passenger.name}")
            self.door_logic.close_doors()
            self.animate_movement(next_passenger.current_floor, floor_dict)
            self.door_logic.open_doors()
            print(f"Picked up {next_passenger.name} at {next_passenger.current_floor} going to {next_passenger.target_floor}")
            passengers.pop(0)

            self.door_logic.close_doors()
            self.animate_movement(next_passenger.target_floor, floor_dict)
            self.door_logic.open_doors()
            print(f"Dropped off {next_passenger.name} at {next_passenger.target_floor}")
