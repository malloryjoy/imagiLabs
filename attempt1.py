import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# --- Define Colors as RGB tuples (0-1 for Matplotlib) ---
lp = (242/255, 165/255, 165/255)   # light pink
mp = (252/255, 131/255, 228/255)   # medium pink
pu = (151/255, 119/255, 224/255)   # purple
lb = (140/255, 190/255, 255/255)   # light blue
B  = (0, 0, 1)                      # blue
off = (0, 0, 0)                     # off / black

ROWS, COLS = 8, 8

def empty_matrix():
    """Create an 8x8 grid filled with 'off'"""
    return [[off for _ in range(COLS)] for _ in range(ROWS)]

# --- Build frames of the animation ---
frames = []

# Frame 1
m = empty_matrix()
m[7][2] = pu
frames.append(np.array(m))

# Frame 2
m = empty_matrix()
m[6][2] = pu
frames.append(np.array(m))

# Frame 3
m = empty_matrix()
m[5][2] = pu
frames.append(np.array(m))

# Frame 4
m = empty_matrix()
m[4][2] = pu
frames.append(np.array(m))

# Frame 5
m = empty_matrix()
m[3][2] = pu
frames.append(np.array(m))

# Frame 6 - purple cross
m = empty_matrix()
m[2][2] = pu
m[2][1] = pu
m[1][2] = pu
m[2][3] = pu
m[3][2] = pu
frames.append(np.array(m))

# Frame 7 - P pattern
m = empty_matrix()
m[0][2] = pu
m[2][0] = pu
m[2][4] = pu
m[4][2] = pu
m[1][3] = pu
m[1][1] = pu
m[3][1] = pu
m[3][3] = pu
frames.append(np.array(m))

# Frame 8 - light blue falling pixel
m = empty_matrix()
m[7][5] = lb
frames.append(np.array(m))

# Frame 9
m = empty_matrix()
m[6][5] = lb
frames.append(np.array(m))

# Frame 10
m = empty_matrix()
m[5][5] = lb
frames.append(np.array(m))

# Frame 11
m = empty_matrix()
m[4][5] = lb
frames.append(np.array(m))

# Frame 12 - light blue cross
m = empty_matrix()
m[4][5] = lb
m[4][4] = lb
m[4][6] = lb
m[3][5] = lb
m[5][5] = lb
frames.append(np.array(m))

# Frame 13 - blue "B" pattern
m = empty_matrix()

m[4][5] = off
m[4][4] = off
m[4][6] = off
m[3][5] = off
m[5][5] = off
m[2][5] = lb
m[3][4] = lb
m[3][6] = lb
m[4][3] = lb
m[4][7] = lb
m[5][4] = lb
m[5][6] = lb
m[6][5] = lb



frames.append(np.array(m))

# --- Set up the figure for animation ---
fig, ax = plt.subplots()
im = ax.imshow(frames[0], interpolation='none')
ax.axis('off')  # hide axes

def update(frame):
    im.set_data(frame)
    return [im]

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=400, blit=True)

plt.show()
