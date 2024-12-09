"""
creatures.py - class definitions for the creatures in FOP Assignment, Sem 1 2024

Written by : Muhammad Annas Atif
Student ID : 22224125

Includes:
    Puppy
    Squirrel
    Human
    Neighbor

Versions:
    - 1.0 - 20/4/2024
    - 2.0 - 21/4/2024
    - 3.0 - 22/4/2024
    - 4.0 - 23/4/2024
    - 5.0 - 23/4/2024
    - 6.0 - 24/4/2024
    - 7.0 - 25/4/2024
    - 8.0 - 26/4/2024
    - 9.0 - 27/4/2024
    - 10.0 - 28/4/2024
    - 11.0 - 29/4/2024
    - 12.0 - 29/4/2024
"""
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def flip_coords(pos, LIMITS):
    return((pos[1],pos[0]))

class Puppy():

    """
    Class and Function Information:

    Holds information and behaviour of puppy creature.

    The __init__() function defines the basic info about the puppy
    This information includes, name, colour, position, previous
    position and age. It also defines some class variables such as
    the boolean value for whether toy/treat is collected, if the
    treat/toy exists, its health, whether it is tired, 
    and whether it is moving towards the treat/toy.

    get_pos() returns the current position as a a tuple.
    
    get_prevpos() returns the previous position as a tuple.

    step_change() contains all movement code including colliders by 
    checking for the position of x and y coordinates of the puppy and 
    comparing it to predefined boundaries of the house, tree and
    fences. The function also contains the movement behavious which in 
    this case is Von Neumann Up, Down, Left and Right as well as 
    diagonals. This functions also prints out current coordinates, 
    previous position, and the move made.

    move_towards_treat() and move_towards_toy() are functions that
    take the positon of the puppy, and the treat/toy respeectivley
    and take the difference resulting in dx and dy of the treat/toy.
    If the position of the puppy == to that of the treat/toy, it sets 
    the boolean that allows the normal movement to be overriden to
    be set to False, it also sets the health of the puppy to 200
    giving it an extra 100hp boost (treat only). Finally it sets the 
    boolean that determines whether the treat/toy has been 
    collected to True. This the in snoo.py results in the clearing of
    the treat/toy on the plots.

    treat_collected() and toy_collected() returns the boolean 
    value of whether the treat/toy has been collected as True of False.

    sitdown() is responsible for making the puppy to go to sleep when
    its health falls below 50 in snoo.py.

    healthloss() is used to calculate the health loss of the creature.

    plot_me() flips the coordiantes of the puppy given that the plot
    is plotted with flipped coordinates. Patches from the Matplotlib
    allow for the plotting of the various shapes that make up the 
    design of the puppy. Within patches, the position, sizes, colours
    are assigned. Finally the annotate function annotates the name of
    the puppy.

    """
    def __init__(self, name, colour, pos, prevpos, age):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]

        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.age = age
        
        self.prevpos = prevpos
        self.move_towards_treat = False
        self.move_towards_toy = False
        self.treat_position = None
        self.toy_position = None
        self.toy_collected = False
        self.treat_collected = False
        self.tired = False
        self.health = 100

    def get_pos(self):
        return self.pos

    def get_prevpos(self):
        return self.prevpos

    def step_change(self):
        if self.move_towards_treat is True:
            self.move_towards_treats()
            print(f"Previous Puppy Position {self.prevpos}\n")

        elif self.move_towards_toy is True:
            self.move_towards_toys()
            print(f"Previous Puppy Position {self.prevpos}\n")

        elif self.tired is True:
            self.sitdown()

        else:
            self.prevpos = (self.pos[0], self.pos[1])
            print(f"Current X: {self.pos[1]}, Current Y: {self.pos[0]}")

            if self.pos[1] == 1 or (self.pos[1] == 31 and 30<self.pos[0]<49):
                validmoves = [(-1,0), (1,0), (0,1)]

            elif self.pos[0] == 1 or (self.pos[0]==10 and 31<self.pos[1] <38):
                validmoves = [(1,0), (0,1), (0,-1)]
                
            elif self.pos[1] == 38 or (self.pos[1]==30 and 0<self.pos[0]<10): 
                # Tree collider for dog only
                validmoves = [(-1,0), (1,0), (0,-1)]

            elif self.pos[0] == 49 or (self.pos[0]==35 and 0<self.pos[1]<30):
                validmoves = [(-1,0), (0,1), (0,-1)]

            else:
                validmoves = [(-1,0), (-1,1), (-1,-1), (1,0), (1,1), 
                              (1,-1), (0,1), (0,-1)] 
                
                # (-1,0) = up | (1,0) = down | (0,1) = right | (0,-1) = left. 
                # This validmoves algorithm also accepts diag movements.
                # diagonals are a combination of values in line
            print(f"Puppy valid moves {validmoves}")

            move = random.choice(validmoves)
            print(f"Puppy move made {move}")
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            print(f"Previous Puppy Position {self.prevpos}\n")

    def move_towards_treats(self):
        tx, ty = self.treat_position
        px, py = self.pos
        dx = tx - px
        dy = ty - py

        if dx == 0 and dy == 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.move_towards_treat = False
            self.treat_collected = True
            self.health = 200

        if dx != 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.pos = (px + dx // abs(dx), px)
            

        elif dy != 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.pos = (px, py + dy // abs(dy))


    def treat_collected(self):
        return str(self.treat_collected)
    
    def move_towards_toys(self):
        tx, ty = self.toy_position
        px, py = self.pos
        dx = tx - px
        dy = ty - py

        if dx == 0 and dy == 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.move_towards_toy = False
            self.toy_collected = True

        if dx != 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.pos = (px + dx // abs(dx), px)
            
        elif dy != 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.pos = (px, py + dy // abs(dy))

    def toy_collected(self):
        return str(self.toy_collected)
    
    def sitdown(self):
        px, py = self.pos
        self.pos = (px, py)

    def health(self):
        return int(self.health)

    def healthloss(self, health, i):
        currenthealth = health - (0.25 * i)
        return currenthealth

    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)

        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]-0.3), height=1.5, 
                            width=0.3, color=self.colour2)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]-0.3), height=1.5, 
                            width=0.3, color=self.colour2)
        ax.add_patch(patch)


        ax.annotate(self.name, (self.pos[1], self.pos[0]-1.25), 
                    ha="center", color="white")


class Squirrel():
    """

    Class and Function Information:

    Holds information and behaviour of squirrel creature

    The __init__() function defines the basic info about the squirrel
    This information includes, name, colour, position, previous
    position and age. It also defines some class variables such as
    the boolean value for whether acorn is collected, if the acorn
    exists, its health, whether it is tired, and whether it is 
    moving towards the acorn.

    get_pos() returns the current position as a a tuple.
    
    get_prevpos() returns the previous position as a tuple.

    step_change() contains all movement code including colliders by 
    checking for the position of x and y coordinates of the squirrel and 
    comparing it to predefined boundaries of the house, tree and
    fences. The function also contains the movement behavious which in 
    this case is Von Neumann Up, Down, Left and Right as well as 
    diagonals.

    move_towards_treat() is a functions that takes the positon of the 
    squirrel, and the treat and takes the difference resulting in dx 
    and dy of the treat. If the position of the squirrel == to that of 
    the treat, it sets the boolean that allows the normal movement to
    be overriden to be set to False, it also sets the health of the
    squirrel to 200 giving it an extra 100hp boost. Finally it sets 
    the boolean that determines whether the treat has been 
    collected to True. This the in snoo.py results in the clearing of
    the treat on the plots.

    step_change() is the default moving algorithm that allows for
    Von Neumann (up, down, left and right) movements which are 
    randomly selected. There are also colliders that prevent the 
    squirrel from entering the house. There is also a interaction
    algorithm that prevents the squirrel from coming within 3 units
    of the puppy.

    treat_collected() returns the boolean value of whether the treat has 
    been collected as True of False.

    sitdown() is responsible for making the squirrel to go to sleep when
    its health falls below 50 in snoo.py.

    healthloss() is used to calculate the health loss of the creature.

    plot_me() flips the coordiantes of the squirrel given that the plot
    is plotted with flipped coordinates. Patches from the Matplotlib
    allow for the plotting of the various shapes that make up the 
    design of the squirrel. Within patches, the position, sizes, colours
    are assigned. Finally the annotate function annotates the name of
    the squirrel.

    """
    def __init__(self, name, colour, pos, prevpos, age):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.age = age
        self.prevpos = prevpos
        self.move_towards_acorn = False
        self.acorn_position = None
        self.acorn_collected = False
        self.tired = False
        self.health = 100

    def health(self, timestep):
        self.health = self.health - (0.25 * timestep)

        print(f"{self.name} Health: {self.health}")

    def get_pos(self):
        return self.pos

    def get_prevpos(self):
        return self.prevpos

    def step_change(self):
        if self.move_towards_acorn is True:
            self.move_towards_acorns()
            print(f"Previous Squirrel Position {self.prevpos}\n")

        elif self.tired is True:
            self.sitdown()

        else:
            self.prevpos = (self.pos[0], self.pos[1])
            print(f"Current X: {self.pos[1]}, Current Y: {self.pos[0]}")
            psx = self.pos[1] - Puppy.get_pos(self)[1]
            psy = self.pos[0] - Puppy.get_pos(self)[0]
            if self.pos[1] == 1 or (self.pos[1]==30 and 29<self.pos[0]<49): 
                # Collider for left movements
                validmoves = [(-1,0), (1,0), (0,1)]
            
            elif self.pos[0] == 1: 
                # Collider for up movements
                validmoves = [(1,0), (0,1), (0,-1)]

            elif self.pos[1] == 39: 
                # Collider for right movement
                validmoves = [(-1,0), (1,0), (0,-1)]

            elif self.pos[1] == 38: 
                # Collider for right movement (2)
                validmoves = [(-1,0), (1,0), (0,-1)]

            elif self.pos[0] == 49 or (self.pos[0]==29 and 0 <self.pos[1]<30): 
                # Collider for down movement
                validmoves = [(-1,0), (0,1), (0,-1)]

            elif 0 < psx < 3:
                validmoves = [(-1,0), (1,0), (0,-1)]
            
            elif -3 < psx < 0:
                validmoves = [(-1,0), (1,0), (0,1)]
            
            elif 0 < psy < 3:
                validmoves = [(1,0), (0,1), (0,-1)]

            elif -3 < psy < 0:
                validmoves = [(-1,0), (0,1), (0,-1)]

            else:
                validmoves = [(-1,0), (1,0), (0,1), (0,-1)] 
                # (-1,0) = up | (1,0) = down | (0,1) = right | (0,-1) = left

            print(f"Squirrel valid moves {validmoves}")

            move = random.choice(validmoves)
            print(f"Squirrel move made {move}")
            self.move = move
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
            print(f"Squirrel previous position {self.prevpos}\n")


    def move_towards_acorns(self):
        ax, ay = self.acorn_position
        px, py = self.pos
        dx = ax - px
        dy = ay - py

        if dx == 0 and dy == 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.move_towards_acorn = False
            self.acorn_collected = True
            self.health = 200
        
        if dx != 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.pos = (px + dx // abs(dx), px)
            

        elif dy != 0:
            self.prevpos = (self.pos[0], self.pos[1])
            self.pos = (px, py + dy // abs(dy))  
    
    def acorn_collected(self):
        return str(self.acorn_collected)

    def health(self):
        return self.health
        
    def sitdown(self):
        px, py = self.pos
        self.pos = (px, py)

    def healthloss(self, health, i):
        currenthealth = health - (0.25 * i)
        return currenthealth
    
    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)

        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]-0.6), height=0.8, 
                            width=0.3, color=self.colour2)
        ax.add_patch(patch)
        
        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]-0.9), height=0.8, 
                            width=0.3, color=self.colour2)
        ax.add_patch(patch)

        ax.annotate((self.name), (self.pos[1], self.pos[0]-1.25), 
                    ha="center", color="white")


class Human():
    """
    Class and Function Information:

    Holds information and behaviour of human

    The __init__() function defines the basic info about the human
    This information includes, name, colour, position, previous
    position and age.

    get_pos() returns the current position as a a tuple.
    
    get_prevpos() returns the previous position as a tuple.

    step_change_drop_treat() contains all movement code takes the 
    difference in y value between the human and the edge of the
    verandah and if the value != 0 then it sets the validmove list
    to only allow movements in the upwards directtion. If the value
    == 0, then the position will not allow for it to move outside the
    collider boundary.

    step_change_normal() is the default moving algorithm for the human.
    There are colliders that prevent the human from moving off the map
    and into the yard, unless it is in a specific position. The
    allowed moves are Von Neumann (up, down, left and right).
    The function also prints the validmoves, the move made and 
    the previous and current position.

    plot_me() flips the coordiantes of the human given that the plot
    is plotted with flipped coordinates. Patches from the Matplotlib
    allow for the plotting of the various shapes that make up the 
    design of the human. Within patches, the position, sizes, colours
    are assigned. Finally the annotate function annotates the name of
    the human.

    """
    def __init__(self, name, colour, pos, prevpos, age):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.prevpos = prevpos

    def get_pos(self):
        return self.pos
    
    def get_prevpos(self):
        return self.prevpos

    def step_change_drop_treat(self):
        self.prevpos = (self.pos[0], self.pos[1])
        print(f"Current X: {self.pos[1]}, Current Y: {self.pos[0]}")

        dy = self.pos[0] - 30 # distance of human from house exit into yard.

        validmoves = [(-1,0), (1,0)]      
     
        if dy > 0:
            move = validmoves[0]
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        if dy == 0:
            self.pos = (self.pos[0], self.pos[1])

    def step_change_normal(self):
        if self.pos[1] == 1: # Collider for left movements
            validmoves = [(-1,0), (1,0), (0,1)]
        
        elif self.pos[0] == 30: # Collider for up movements
            validmoves = [(1,0), (0,1), (0,-1)]

        elif self.pos[1] == 30: # Collider for right movement
            validmoves = [(-1,0), (1,0), (0,-1)]

        elif self.pos[1] == 49: # Collider for down movement
            validmoves = [(-1,0), (0,1), (0,-1)]

        else:
            validmoves = [(-1,0), (1,0), (0,1), (0,-1)] 
            # (-1,0) = up | (1,0) = down | (0,1) = right | (0,-1) = left

    
        print(f"Human valid moves {validmoves}")
        move = random.choice(validmoves)
        print(f"Human move made {move}")
        self.move = move
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        print(f"Human previous position {self.prevpos}\n")

    
    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]), height=1, 
                            width=0.5, color=self.colour2)
        ax.add_patch(patch) 

        patch = pat.Circle(fpos, radius = 0.5, color = self.colour2)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]), height=1, 
                            width=0.5, color=self.colour2)
        ax.add_patch(patch)

        ax.annotate(self.name, (self.pos[1], self.pos[0]-1.25), 
                    ha="center", color="white")

class Neighbor():
    """
    Class and Function Information:

    The __init__() function defines the basic info about the neighbor
    This information includes, name, colour, position, previous
    position and age.

    Holds information and behaviour of neighbor

    get_pos() returns the current position as a a tuple.
    
    get_prevpos() returns the previous position as a tuple.

    step_change_drop_treat() contains all movement code takes the 
    difference in y value between the neighbor and the edge of the
    verandah and if the value != 0 then it sets the validmove list
    to only allow movements in the upwards directtion. If the value
    == 0, then the position will not allow for it to move outside the
    collider boundary.

    step_change_normal() is the default moving algorithm for the neighbor.
    There are colliders that prevent the neighbor from moving off the map
    and into the yard, unless it is in a specific position. The
    allowed moves are Von Neumann (up, down, left and right).
    The function also prints the validmoves, the move made and 
    the previous and current position.

    plot_me() flips the coordiantes of the neighbor given that the plot
    is plotted with flipped coordinates. Patches from the Matplotlib
    allow for the plotting of the various shapes that make up the 
    design of the neighbor. Within patches, the position, sizes, colours
    are assigned. Finally the annotate function annotates the name of
    the neighbor.
    """
    def __init__(self, name, colour, pos, prevpos, age):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos
        self.prevpos = prevpos
        self.age = age
        self.moveright = True
        self.moveleft = False

    def get_pos(self):
        return self.pos
    
    def get_prevpos(self):
        return self.prevpos

    def step_change_right(self):

        self.prevpos = (self.pos[0], self.pos[1])

        if self.pos[1] == 39: # Collider for right movement
            validmoves = [(0,-39)]

        else:
            validmoves = [(0,1)]
    
        print(f"Neighbor valid moves {validmoves}")
        move = random.choice(validmoves)
        print(f"Neighbor move made {move}")
        self.move = move
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        print(f"Neighbor previous position {self.prevpos}\n")


    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]), height=1, 
                            width=0.5, color=self.colour2)
        ax.add_patch(patch) 

        patch = pat.Circle(fpos, radius = 0.5, color = self.colour2)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]), height=1, 
                            width=0.5, color=self.colour2)
        ax.add_patch(patch)

        ax.annotate((self.name + " the Neighbor"), 
                    (self.pos[1], self.pos[0]-1.25), ha="center",
                    color="white")