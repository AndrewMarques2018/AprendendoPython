from enum import Enum, auto

class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()

def move(direction):
    if not isinstance(direction, Directions):
        return f'value error: {direction}'
    else:
        return f'move to {direction.name}'

if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))
    print(move('vertical'))
