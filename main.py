import random
from faker import Faker
from command import ElevatorCommand
from passenger import Passenger
from doors_logic import DoorLogic
from elevator_move import ElevatorMove
from weight import ElevatorWeight, WeightSensor

faker = Faker()

elevator_command = ElevatorCommand()
floor_dict = elevator_command.elevator_command()

door_logic = DoorLogic()
elevator_move = ElevatorMove(door_logic)

people_weights = [random.randint(50, 100) for _ in range(5)]
elevator_weight = ElevatorWeight(700)

sensor = WeightSensor(elevator_weight)
print(sensor.check_weight(people_weights))

passengers = []
for floor in floor_dict:
    if random.random() < 0.5:
        target_floor = random.choice([f for f in floor_dict if f != floor])
        name = faker.name()
        weight = random.randint(50, 120)
        passengers.append(Passenger(floor, target_floor, name, weight))
        print(f"Passenger spawned: {passengers[-1]}")


elevator_move.handle_passengers(passengers, floor_dict)