import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import convolve2d
import matplotlib
matplotlib.use('TkAgg')

# Configuration
GRID_SIZE = (100, 100)
NUM_GENERATIONS = 1000
INTERVAL = 1  # Milliseconds between frames

# Initialize the grid
field = np.random.randint(0, 2, GRID_SIZE)
#field = np.zeros(GRID_SIZE, dtype=int)
#field[2,0]=1
#field[2,1]=1
#field[2,2]=1
#field[1,2]=1
#field[0,1]=1

# Kernel for neighbor sum computation
kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

# Set up the plot
fig, ax = plt.subplots()
im = ax.imshow(field, animated=True)
ax.set_title("Generation 0")


def update_plot(frame, field, im, kernel):
    # Compute the sum of neighbors using convolution
    neighbor_count = convolve2d(field, kernel, mode='same', boundary='wrap')

    # Apply Game of Life rules
    new_field = (neighbor_count == 3) | ((field == 1) & (neighbor_count == 2))

    # Update the image and title
    im.set_array(new_field)
    ax.set_title(f"Generation {frame}")

    # Copy the new state to the field
    field[:] = new_field


# Run the animation
anim = FuncAnimation(fig, update_plot, frames=NUM_GENERATIONS,
                     fargs=(field, im, kernel), interval=INTERVAL, blit=False)

plt.show()
