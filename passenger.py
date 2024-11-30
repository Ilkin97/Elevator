class Passenger:
    def __init__(self, current_floor, target_floor, name, weight):
        self.current_floor = current_floor
        self.target_floor = target_floor
        self.name = name
        self.weight = weight
        self.direction = 'up' if target_floor > current_floor else 'down'

    def __str__(self):
        return f"{self.name} (Weight: {self.weight} kg) at Floor {self.current_floor} going to Floor {self.target_floor}"