import numpy as np

field_size = (10, 10)
number_boats = 1
hits = 0
field = np.zeros(field_size, dtype=bool)
rand_flat = np.random.choice(field_size[0]*field_size[1], number_boats, replace=False)
field[np.unravel_index(rand_flat, field_size)] = True

print(field)

while True:
    try:
        x, y = map(int, input("Enter coordinates (x,y): ").split(','))
        coordinates = (y-1, x-1)
        if field[coordinates]:
            hits+=1
            field[coordinates] = False
            print(f"Hit number {hits}!")
        else:
            close_miss = False
            for iy in range(coordinates[0]-1, coordinates[0]+2):
                for ix in range(coordinates[1]-1, coordinates[1]+2):
                    if (iy != coordinates[0] or ix != coordinates[1]) and 0 <= iy < field_size[0] and 0 <= ix < field_size[1] and field[iy, ix]:
                        close_miss = True
                        break
            if close_miss:
                print("Close miss!")
            else:
                print("Miss!")
    except (IndexError, ValueError):
        print("Invalid coordinates.")