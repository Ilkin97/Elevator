class ElevatorWeight:
    def __init__(self, max_weight) -> None:
        self.max_weight = max_weight
        self.current_weight = 0

    def weight(self, people_weight):
        total_weight = sum(people_weight)
        if total_weight > self.max_weight:
            return f"Too much weight. The elevator can't lift that much load. Max weight: {self.max_weight} kg"
        else:
            self.current_weight = total_weight
            return f"Current weight: {self.current_weight} kg. The elevator can safely lift this load."
        
        
class WeightSensor:
    def __init__(self, elevator_weight) -> None:
        self.elevator_weight = elevator_weight
        
    def check_weight(self, people_weights):
        message = self.elevator_weight.weight(people_weights)
        return message