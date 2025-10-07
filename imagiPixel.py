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
red = (255,2,0) #Flag Red


#August colors
g = (0, 159, 39) #tree green
tr= (102,76,45) #tree trunk
sn = (255,189,99) #sand
liblu = (0, 255,253 ) #lightblue
y = (253,255,0) #yellow


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

def isMay():
    m = empty_matrix()
    def cornflower():
        m[3][3] = aq
        m[3][4] = aq
        m[4][3] = aq
        m[4][4] = aq    
        m[1][1] = b
        m[1][2] = b
        m[1][5] = b
        m[1][6] = b
        m[2][1] = b
        m[2][3] = b
        m[2][4] = b
        m[2][6] = b
        m[3][2] = b
        m[3][5] = b
        m[4][2] = b
        m[4][5] = b
        m[5][1] = b
        m[5][3] = b
        m[5][4] = b
        m[5][6] = b
        m[6][1] = b
        m[6][2] = b
        m[6][5] = b
        m[6][6] = b
    
    def violet():
        m[3][3] = gold
        m[3][4] = gold
        m[4][3] = gold
        m[4][4] = gold
        
        m[1][1] = rp
        m[1][2] = rp
        m[1][5] = rp
        m[1][6] = rp
        m[2][1] = rp
        m[2][3] = rp
        m[2][4] = rp
        m[2][6] = rp
        m[3][2] = rp
        m[3][5] = rp
        m[4][2] = rp
        m[4][5] = rp
        m[5][1] = rp
        m[5][3] = rp
        m[5][4] = rp
        m[5][6] = rp
        m[6][1] = rp
        m[6][2] = rp
        m[6][5] = rp
        m[6][6] = rp

    def rose():
        m[3][3] = hr
        m[3][4] = hr
        m[4][3] = hr
        m[4][4] = hr
        
        m[1][1] = bl
        m[1][2] = bl
        m[1][5] = bl
        m[1][6] = bl
        m[2][1] = bl
        m[2][3] = bl
        m[2][4] = bl
        m[2][6] = bl
        m[3][2] = bl
        m[3][5] = bl
        m[4][2] = bl
        m[4][5] = bl
        m[5][1] = bl
        m[5][3] = bl
        m[5][4] = bl
        m[5][6] = bl
        m[6][1] = bl
        m[6][2] = bl
        m[6][5] = bl
        m[6][6] = bl


    def sunflower():
        m[3][3] = br
        m[3][4] = br
        m[4][3] = br
        m[4][4] = br
        
        m[1][1] = gold
        m[1][2] = gold
        m[1][5] = gold
        m[1][6] = gold
        m[2][1] = gold
        m[2][3] = gold
        m[2][4] = gold
        m[2][6] = gold
        m[3][2] = gold
        m[3][5] = gold
        m[4][2] = gold
        m[4][5] = gold
        m[5][1] = gold
        m[5][3] = gold
        m[5][4] = gold
        m[5][6] = gold
        m[6][1] = gold
        m[6][2] = gold
        m[6][5] = gold
        m[6][6] = gold
    
    #Frame 1
    cornflower() 
    frames.append(np.array(m))

    #Frame 2
    violet() 
    frames.append(np.array(m))

    #Frame 3
    rose() 
    frames.append(np.array(m))

    #Frame 4
    sunflower()
    frames.append(np.array(m))

        # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('off')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=500, blit=True)

    plt.show()

def isJune():
    m = empty_matrix()
    
    def cake():
        
        m[1][1] = gold
        m[1][3] = gold
        m[1][4] = gold
        m[1][6] = gold
        m[2][1] = aq
        m[3][1] = aq
        m[2][3] = aq
        m[3][3] = aq
        m[2][4] = aq
        m[3][4] = aq
        m[2][6] = aq
        m[3][6] = aq
        for col in range(1,7):
            m[4][col] = pn
            m[7][col] = pn
            m[6][col] = lp
        m[5][1] = pn
        m[5][2] = lp
        m[5][3] = pn
        m[5][4] = pn
        m[5][5] = lp
        m[5][6] = pn
    
    
    cake()

    frames.append(np.array(m))
    cake()
    m[1][1] = gold
    m[1][3] = gold
    m[1][4] = gold
    m[1][6] = black


    frames.append(np.array(m))
    cake()
    m[1][1] = gold
    m[1][3] = gold
    m[1][4] = black
    m[1][6] = black
        
    frames.append(np.array(m))
    cake()
    m[1][1] = gold
    m[1][3] = black
    m[1][4] = black
    m[1][6] = black
        
    frames.append(np.array(m))
    cake()
    m[1][1] = black
    m[1][3] = black
    m[1][4] = black
    m[1][6] = black
        
    frames.append(np.array(m))
    cake()
    m[1][1] = black
    m[1][3] = black
    m[1][4] = black
    m[1][6] = black

    frames.append(np.array(m))

    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('off')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=200, blit=True)

    plt.show()

def isJuly():
    m = empty_matrix()
    def rock():
        m[0][3] = rb
        m[0][4] = rb
        m[1][2] = rb
        m[1][5] = rb
        m[2][1] = rb
        m[2][6] = rb
        m[3][0] = rb
        m[3][7] = rb
        m[4][0] = rb
        m[4][7] = rb
        m[5][0] = rb
        m[5][7] = rb
        m[6][1] = rb
        m[6][7] = rb
        m[0][4] = rb
        for col in range(2,7):
            m[7][col] = rb
        for row in range(3,6):
            m[row][1] = rc
        for row in range(2,7):
            m[row][2] = rc
        for row in range(1,7):
            m[row][3] = rc
        for row in range(1,7):
            m[row][4] = rc
        for row in range(2,7):
            m[row][5] = rc
        for row in range(3,7):
            m[row][6] = rc
        

    def flag():
        for col in range(0,3):
            m[0][col] = b
            m[1][col] = b
            m[2][col] = b
        for col in range(3,8):
            m[0][col] = red
            m[1][col] = white
            m[2][col] = red
        for col in range(0,8):
            m[3][col] = white
            m[4][col] = red
            m[5][col] = white
            m[6][col] = red
            m[7][col] = white

    def eagle():
        m[2][5] = bk
        m[3][1] = br
        m[3][6] = br
        m[4][1] = white
        m[4][2] = br
        m[4][5] = br
        m[4][6] = white
        m[5][1] = br
        m[5][6] = br
        for row in range (2,6):
            m[row][3] = white
            m[row][4] = white
        for col in range (2,6):
            m[6][col] = br
        for col in range (3,5):
            m[7][col] = bk
        for row in range (3,5):
            m[row][0] = br
            m[row][7] = br
        for col in range (2,6):
            m[5][col] = white
    
    def clear():
        
        for row in range(8):
            for col in range(8):
                m[row][col] = black   # reset everything to "off"

    rock()
    frames.append(np.array(m))
    clear()
    flag()
    frames.append(np.array(m))
    clear()
    eagle()
    frames.append(np.array(m))

    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('off')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=500, blit=True)

    plt.show()

def isAugust():
    m = empty_matrix()
    def tree():
        m[1][3] = g
        m[0][4] = g
        m[1][5] = g
        for row in range(1,4):
            m[row][4] = tr
    def sand():
        for col in range(0,4):
            m[3][col] = sn
        for col in range(5,8):
            m[3][col] = sn
        for col in range(0,8):
            m[4][col] = sn
        for col in range(1,3):
            m[5][col] = sn
        for col in range(5,7):
            m[5][col] = sn

    def sea():
        for row in range(5,7):
            m[row][0] = b
            m[row][7] = b
        for col in range(0,8):
            m[7][col] = b
        for col in range(1,7):
            m[6][col] = aq
        for col in range(3,5):
            m[5][col] = aq

    m[0][0] = y


    tree()
    sand()
    sea()

    frames.append(np.array(m))
    m[5][1] = aq
    m[5][2] = aq
    m[5][5] = aq
    m[5][6] = aq
    m[5][3] = sn
    m[5][4] = sn

    frames.append(np.array(m))
    m[4][1] = aq
    m[5][2] = aq
    m[4][6] = aq
    m[5][5] = aq

    frames.append(np.array(m))

    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('off')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=200, blit=True)

    plt.show()

def isSeptember():
    m = empty_matrix()
    def gazebo():
        for row in range(2,7):
            m[1][row]= ol
        for row in range(2,7):
            m[2][row] = choc
        for col in range(3,6):
            m[col][2] = white
        for col in range(3,6):
            m[col][4] = white
        for col in range(3,6):
            m[col][6] = white
        for row in range(2,7):
            m[6][row] = br
        for row in range(1,8):
            m[7][row] = br
        m[2][1] = ol
        m[2][7] = ol
        m[6][0] = si
        m[6][1] = si
        m[6][7] = si
        m[7][0] = si
    frames.append(np.array(m))
    gazebo()
    
    m[0][0] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[1][1] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[2][2] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[3][3] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[2][4] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[1][3] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[2][2] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[3][3] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[4][4] =lf
    frames.append(np.array(m))
    m = empty_matrix()
    gazebo()
    m[5][5]  = lf
    frames.append(np.array(m))


    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('off')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=200, blit=True)

    plt.show()

def isOctober():
    m = empty_matrix()
    def pumpkin():
        for col in range(0,3):
            m[1][col]= pb
        for col in range(5,8):
            m[1][col] = pb
        for row in range(2,7):
            m[row][0] = pb
        for row in range(2,7):
            m[row][7] = pb
        for col in range(2,6):
            m[2][col]= pb
        for col in range(1,7):
            m[7][col] = pb
        for row in range(0,2):
            m[row][4] = st
            m[0][5] = st
        for row in range(2,7):
            m[row][1] = pmpk
            m[row][6] = pmpk
        for col in range(1,7):
            m[3][col] = pmpk
            m[4][col] = pmpk
            m[5][col] = pmpk
            m[6][col] = pmpk

    def face1():
        m[3][2] = black
        m[3][5] = black
        m[5][1] = black
        m[5][6] = black
        for col in range(2,6):
            m[6][col] = black

    def face2():
        m[3][2] = black
        m[3][5] = black
        for col in range(3,5):
            m[5][col] = black
            m[6][col] = black
    def face3():
        m[3][1] = black
        m[3][6] = black
        m[4][2] = black
        m[4][5] = black
        for col in range(2,6):
            m[6][col] = black
    frames.append(np.array(m))
    pumpkin()
    frames.append(np.array(m))
    pumpkin()
    face1()
    frames.append(np.array(m))
    pumpkin()
    face2()
    frames.append(np.array(m))
    pumpkin()
    face3()
    frames.append(np.array(m))

    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('off')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=400, blit=True)

    plt.show()

def isNovember():
    m = empty_matrix()
    def bowl():
        for col in range(0,8):
            m[5][col] = bwl
        for col in range(1,7):
            m[6][col] = bwl
        for col in range(2,6):
            m[7][col] = bwl

    def cranberry():
        for col in range(1,7):
            m[4][col] = cran
            m[3][col] = cran
        m[2][3] = cran
        m[2][4] = cran

    def mashedpotatoes():
        for col in range(1,7):
            m[4][col] = white
            m[3][col] = white
        m[2][3] = white
        m[2][4] = white
   

    def turkey():
        for col in range(3,6):
            m[4][col] = trk
        for col in range(2,7):
            m[5][col] = trk
        for col in range(1,4):
            m[6][col] = trk
            m[7][col] = trk
        for col in range(4,6):
            m[6][col] = ds
        for col in range(4,8):
            m[7][col] = ds
            
        m[5][7] = ds
        m[6][6] = trk

    def heart():
        for col in range(1,3):
            m[1][col] = hb
        for col in range(5,7):
            m[1][col] = hb
        for col in range(3,5):
            m[2][col] = hb
        for col in range(3,5):
            m[7][col] = hb
        for row in range(2,5):
            m[row][0] = hb
            m[row][7] = hb
        for row in range(2,5):
            m[row][1] = hc
        for row in range(2,6):
            m[row][2] = hc
        for row in range(3,7):
            m[row][3] = hc
        for row in range(3,7):
            m[row][4] = hc
        for row in range(2,6):
            m[row][5] = hc
        for row in range(2,5):
            m[row][6] = hc
        m[5][1] = hb
        m[5][6] = hb
        m[6][2] = hb
        m[6][5] = hb


    frames.append(np.array(m))
    bowl()
    cranberry()
    frames.append(np.array(m))

    bowl()
    mashedpotatoes()
    frames.append(np.array(m))

    m = empty_matrix()
    turkey()
    frames.append(np.array(m))

    m = empty_matrix()
    heart()
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

def isDecember():
    m = empty_matrix()
    def tree():
        for col in range(3,5):
            m[7][col] = tt
            m[6][col] = tt
        for col in range(0,3):
            m[6][col] = xtb
        for col in range(5,7):
            m[6][col] = xtb
        for col in range(0,8):
            m[5][col] = xtb
        for col in range(1,7):
            m[4][col] = xtb
        for col in range(2,6):
            m[3][col] = xtb
        for col in range(3,5):
            m[2][col] = xtb
        for col in range(3,5):
            m[1][col] = xst
        m[2][3] = liblu
        m[3][5] = liblu
        m[4][3] = liblu
        m[5][1] = liblu
        m[5][5] = liblu
        m[6][7] = liblu

    def dreidel():
        for col in range(3,5):
            m[0][col] = hy
            m[1][col] = hy
        for col in range(1,7):
            m[2][col] = hdb
            m[3][col] = hdb
            m[4][col] = hdb
            m[5][col] = hdb
        for col in range(2,6):
            m[6][col] = hdb
        for col in range(3,5):
            m[7][col] = hdb
        for col in range(3,5):
            m[3][col] = hy
        for row in range(3,6):
            m[row][5] = hy
        m[5][3] = hy
        
    def santa():
        for col in range(1,7):
            m[7][col] = xsw
        for col in range(2,6):
            m[6][col] = xsr
            m[5][col] = xsr
        for row in range(2,5):
            m[row][3] = xsr
            m[row][4] = xsr
        for col in range(4,6):
            m[1][col] = xsr
        m[2][6] = xsr
        m[3][6] = xsw

    def pole():
        for row in range(1,8):
            m[row][3] = fp



    tree()
    frames.append(np.array(m))
    m = empty_matrix()
    dreidel()
    frames.append(np.array(m))
    m = empty_matrix()
    santa()
    frames.append(np.array(m))
    m = empty_matrix()
    pole()

    frames.append(np.array(m))

    # --- Set up the figure for animation ---
    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], interpolation='none')
    ax.axis('off')  # hide axes

    def update(frame):
        im.set_data(frame)
        return [im]

        # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=600, blit=True)

    plt.show()

if current_month == 1:
    isJanuary()
elif current_month == 2: 
    isFebruary()
elif current_month == 3: 
    isMarch()
elif current_month == 4: 
    isApril()
elif current_month == 5:
    isMay()
elif current_month == 6: 
    isJune()
elif current_month == 7:
    isJuly()
elif current_month == 8:
    isAugust()
elif current_month == 9:
    isSeptember()
elif current_month == 10:
    isOctober()
elif current_month == 11:
    isNovember()
elif current_month == 12:
    isDecember()
else:
    m = empty_matrix

#isJanuary()
#isFebruary()
#isMarch()
#isApril()
#isMay()
#isJune()
#isJuly()
#isAugust()
#isSeptember()
#isOctober()
#isNovember()
#isDecember()


