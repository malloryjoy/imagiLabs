from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation



#neutral colors
black = (0,0,0)
white = (255,255,255)
#January colors
lipu = (242, 165, 165) #lightpurple
mdpu = (252, 131, 228) #mediumpurple
pu = (151, 119, 224) #lavender
pabl = (140, 190, 255) #paleblue
p = (148, 0, 210) #true purple
b = (20,0,255) #true blue

#February colors
lp = (248, 176, 192) #light pink
mp = (253, 119, 150) #medium pink
dp = (231, 66, 103) #dark pink

#March colors
lg = (0, 255, 0) #light green
dg = (0, 128, 0) #dark green


#April colors
aq = (102, 212, 238) #rainblue
y = (253,255,0)

#May colors
gold = (255, 243, 107) 
rp = (108, 59, 170) #royal purple
br = (88,49,23) #brown 
bl = (120, 6, 6) #blood red
hr = (181, 3, 26) #high red 


#June colors
gold = (255, 243, 107) #gold
aq = (102, 212, 238) #candle
pn = (254, 4, 255) #pink
lp = (248,176,192) #lightpink


#July colors
rb = (66,68,84) #rock border
rc = (157,157,157) #rock center
ebr = (116, 76, 4) #eagle brown
bk = (255, 243, 107) #BEAK!!


#August colors
g = (0, 159, 39) #tree green
tr= (102,76,45) #tree trunk
sn = (255,189,99) #sand
liblu = (0, 255,253 ) #lightblue


#September colors
brrd = (104, 13, 12) #brick red
choc = (106, 89, 74) #chocolate
si = (153, 92, 32) #sienna
ol = (55, 83,24) #olive
lf = (219,114, 23) #maple

#October colors
pb = (124,83,6) #pumpkinborder
pmpk = (209,93,7) #pumpkincenter
st = (12,55,34) #stem


#November colors
cran = (165, 8, 61) #cranberry
mapo = (225, 225, 225) #mashed potatoes
bwl = (55,86,240) #bowl
trk = (98,63,5) #turkey
ds = (229,151,18) #wing
hb = (149,11,52) #heartborder
hc = (240,0,164) #heartcenter


#December colors
xst = (255,238,100) #tree star
xtb = (0,87,5) #tree leaves
xlb =  (102,212,238) #ornaments
tt =  (66,33,17) #tree trunk
hy =  (255,234,0) #hannukahyellow
hdb =  (20,0,255) #dreidelblue
xsr =  (171,0,2)#santa red 
xsw = (225,225,225) #santa white
fp = (102, 102, 102) #festivus aluminum pole

#declare variable current_month as the current month 

current_month = datetime.now().month
#print(current_month)

ROWS, COLS = 8, 8

def empty_matrix():
    """Create an 8x8 grid filled with 'black'"""
    return [[black for _ in range(COLS)] for _ in range(ROWS)]

# --- Build frames of the animation ---
frames = []

def isJanuary():
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
    m[7][5] = pabl
    frames.append(np.array(m))

    # Frame 9
    m = empty_matrix()
    m[6][5] = pabl
    frames.append(np.array(m))

    # Frame 10
    m = empty_matrix()
    m[5][5] = pabl
    frames.append(np.array(m))

    # Frame 11
    m = empty_matrix()
    m[4][5] = pabl
    frames.append(np.array(m))

    # Frame 12 - light blue cross
    m = empty_matrix()
    m[4][5] = pabl
    m[4][4] = pabl
    m[4][6] = pabl
    m[3][5] = pabl
    m[5][5] = pabl
    frames.append(np.array(m))

    # Frame 13 - blue "B" pattern
    m = empty_matrix()

    m[4][5] = black
    m[4][4] = black
    m[4][6] = black
    m[3][5] = black
    m[5][5] = black
    m[2][5] = pabl
    m[3][4] = pabl
    m[3][6] = pabl
    m[4][3] = pabl
    m[4][7] = pabl
    m[5][4] = pabl
    m[5][6] = pabl
    m[6][5] = pabl



    frames.append(np.array(m))

    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('black')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=200, blit=True)

    plt.show()

def isFebruary():
    #Frame 1
    m = empty_matrix()
    m[1][1] = mp
    m[2][3] = mp
    m[1][2] = mp
    m[2][0] = mp
    m[4][0] = mp
    m[3][0] = mp
    m[7][3] = mp
    m[5][1] = mp
    m[6][2] = mp
    m[1][6] = mp
    m[2][7] = mp
    m[2][4] = mp
    m[1][5] = mp
    m[4][7] = mp
    m[5][6] = mp
    m[3][7] = mp
    m[7][4] = mp
    m[6][5] = mp

    m[5][0] = lp
    m[5][7] = lp
    m[6][1] = lp
    m[6][6] = lp
    m[7][2] = lp
    m[7][5] = lp
    m[1][0] = lp
    m[1][7] = lp
    m[0][1] = lp
    m[0][2] = lp
    m[0][5] = lp
    m[0][6] = lp
    m[1][3] = lp
    m[1][4] = lp

    m[2][1] = dp
    m[2][2] = dp
    m[2][5] = dp
    m[2][6] = dp
    m[3][1] = dp
    m[3][3] = dp
    m[3][4] = dp
    m[3][6] = dp
    m[4][1] = dp
    m[4][6] = dp
    m[5][2] = dp
    m[5][5] = dp
    m[6][3] = dp
    m[6][4] = dp

    m[3][2] = lp
    m[3][5] = lp
    m[4][2] = lp
    m[4][3] = lp
    m[4][4] = lp
    m[4][5] = lp
    m[5][3] = lp
    m[5][4] = lp

    frames.append(np.array(m))

    m[1][1] = dp
    m[2][3] = dp
    m[1][2] = dp
    m[2][0] = dp
    m[4][0] = dp
    m[3][0] = dp
    m[7][3] = dp
    m[5][1] = dp
    m[6][2] = dp
    m[1][6] = dp
    m[2][7] = dp
    m[2][4] = dp
    m[1][5] = dp
    m[4][7] = dp
    m[5][6] = dp
    m[3][7] = dp
    m[7][4] = dp
    m[6][5] = dp

    m[5][0] = mp
    m[5][7] = mp
    m[6][1] = mp
    m[6][6] = mp
    m[7][2] = mp
    m[7][5] = mp
    m[1][0] = mp
    m[1][7] = mp
    m[0][1] = mp
    m[0][2] = mp
    m[0][5] = mp
    m[0][6] = mp
    m[1][3] = mp
    m[1][4] = mp

    m[2][1] = lp
    m[2][2] = lp
    m[2][5] = lp
    m[2][6] = lp
    m[3][1] = lp
    m[3][3] = lp
    m[3][4] = lp
    m[3][6] = lp
    m[4][1] = lp
    m[4][6] = lp
    m[5][2] = lp
    m[5][5] = lp
    m[6][3] = lp
    m[6][4] = lp

    m[3][2] = mp
    m[3][5] = mp
    m[4][2] = mp
    m[4][3] = mp
    m[4][4] = mp
    m[4][5] = mp
    m[5][3] = mp
    m[5][4] = mp

    frames.append(np.array(m))

    m[1][1] = lp
    m[2][3] = lp
    m[1][2] = lp
    m[2][0] = lp
    m[4][0] = lp
    m[3][0] = lp
    m[7][3] = lp
    m[5][1] = lp
    m[6][2] = lp
    m[1][6] = lp
    m[2][7] = lp
    m[2][4] = lp
    m[1][5] = lp
    m[4][7] = lp
    m[5][6] = lp
    m[3][7] = lp
    m[7][4] = lp
    m[6][5] = lp

    m[5][0] = dp
    m[5][7] = dp
    m[6][1] = dp
    m[6][6] = dp
    m[7][2] = dp
    m[7][5] = dp
    m[1][0] = dp
    m[1][7] = dp
    m[0][1] = dp
    m[0][2] = dp
    m[0][5] = dp
    m[0][6] = dp
    m[1][3] = dp
    m[1][4] = dp

    m[2][1] = mp
    m[2][2] = mp
    m[2][5] = mp
    m[2][6] = mp
    m[3][1] = mp
    m[3][3] = mp
    m[3][4] = mp
    m[3][6] = mp
    m[4][1] = mp
    m[4][6] = mp
    m[5][2] = mp
    m[5][5] = mp
    m[6][3] = mp
    m[6][4] = mp

    m[3][2] = dp
    m[3][5] = dp
    m[4][2] = dp
    m[4][3] = dp
    m[4][4] = dp
    m[4][5] = dp
    m[5][3] = dp
    m[5][4] = dp


    frames.append(np.array(m))



    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('black')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=200, blit=True)

    plt.show()

def isMarch():
    # Frame 1
    m = empty_matrix()
    def stem():
        m[3][3] = dg
        m[4][3] = dg
        m[5][3] = dg
        m[6][3] = dg
        m[7][4] = dg

    def leaf1():
        m[4][4] = lg
        m[4][5] = lg
        m[5][4] = lg
        m[5][5] = lg
        m[5][6] = lg
        m[6][5] = lg

    def leaf2():
        m[0][5] = lg
        m[1][4] = lg
        m[1][5] = lg
        m[1][6] = lg
        m[2][4] = lg
        m[2][5] = lg

    def leaf3():
        m[0][1] = lg
        m[1][0] = lg
        m[1][1] = lg
        m[1][2] = lg
        m[2][1] = lg
        m[2][2] = lg
    
    def leaf4():
        m[4][1] = lg
        m[4][2] = lg
        m[5][0] = lg
        m[5][1] = lg
        m[5][2] = lg
        m[6][1] = lg
    
    
    stem()
    frames.append(np.array(m))
    stem()
    leaf1()
    frames.append(np.array(m))
    stem()
    leaf1()
    leaf2()
    frames.append(np.array(m))
    stem()
    leaf1()
    leaf2()
    leaf3()
    frames.append(np.array(m))
    stem()
    leaf1()
    leaf2()
    leaf3()
    leaf4()
    frames.append(np.array(m))

    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('black')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=400, blit=True)

    plt.show()

def isApril():
    #Frame 1
    m = empty_matrix()
    def umbrella():
        m[2][3] = y
        m[2][4] = y
        m[3][2] = y
        m[3][3] = y
        m[3][4] = y
        m[3][5] = y
        m[4][1] = y
        m[4][2] = y
        m[4][3] = y
        m[4][4] = y
        m[4][5] = y
        m[4][6] = y
        m[5][4] = p
        m[6][2] = p
        m[6][4] = p
        m[7][3] = p
    
    umbrella()
    frames.append(np.array(m))

    #Frame 2
    umbrella()
    m[0][1] = aq

    #Frame 3
    frames.append(np.array(m))
    m[0][1] = black
    m[1][1] = aq

    #Frame 4
    frames.append(np.array(m))
    m[0][1] = black
    m[1][1] = black
    m[2][1] = aq
    m[0][5] = aq

    #Frame 5
    frames.append(np.array(m))
    m[0][1] = black
    m[1][1] = black
    m[2][1] = black
    m[3][1] = aq
    m[0][5] = black
    m[1][5] = aq

    #Frame 6
    frames.append(np.array(m))
    m[0][1] = black
    m[1][1] = black
    m[2][1] = black
    m[3][1] = black
    m[0][5] = black
    m[1][5] = black
    m[2][5] = aq
    m[0][2] = aq

    #Frame 7
    frames.append(np.array(m))
    m[0][1] = black
    m[1][1] = black
    m[2][1] = black
    m[3][1] = black
    m[0][5] = black
    m[1][5] = black
    m[2][5] = black
    m[0][2] = black
    m[1][2] = aq
    m[0][6] = aq
    m[0][4] = aq


    #Frame 8
    frames.append(np.array(m))

    m[0][1] = black
    m[1][1] = black
    m[2][1] = black
    m[3][1] = black
    m[0][5] = black
    m[1][5] = black
    m[2][5] = black
    m[0][2] = black
    m[1][2] = black
    m[2][2] = aq
    m[0][6] = black
    m[0][4] = aq
    m[1][6] = aq

    #Frame 9
    frames.append(np.array(m))

    m[0][1] = black
    m[1][1] = black
    m[2][1] = black
    m[3][1] = black
    m[0][5] = black
    m[1][5] = black
    m[2][5] = black
    m[0][3] = black
    m[1][3] = black
    m[0][6] = black
    m[0][4] = black
    m[1][4] = aq
    m[1][6] = black
    m[2][6] = aq

    
    frames.append(np.array(m))
    #Frame 10
    m[0][1] = black
    m[1][1] = black
    m[2][1] = black
    m[3][1] = black
    m[0][5] = black
    m[1][5] = black
    m[2][5] = black
    m[0][3] = black
    m[1][3] = black
    m[0][6] = black
    m[0][4] = black
    m[1][4] = black

    m[1][6] = black
    m[2][6] = black
    m[3][6] = aq


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

#isJanuary()
#isFebruary()
#isMarch()
isApril()
#isMay()
#isJune()
#isJuly()
#isAugust()
#isSeptember()
#isOctober()
#isNovember()
#isDecember()


