class ElevatorCommand:
    def elevator_command(self):
        self.floors = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.floor_dict = {
            floor: "Ground Floor" if floor == 0 
                   else "Garage" if floor == -1 or floor == -2 
                   else f"Floor {floor}" 
            for floor in self.floors[::-1]
        }
        return self.floor_dict
    
    def elevator_door(self):    
        self.open_door = "Doors are opening"
        self.close_door = "Doors are closing"
        return self.open_door, self.close_door
    
    def elevator_movement(self):    
        self.down = "Going down"
        self.up = "Going up"
        return self.down, self.up