"""
snoo.py - base simulation for the FOP Assignment, Sem 1 2024

Written by : Muhammad Annas Atif
Student ID : 22224125

Usage:

    contains all files for simulation runtime
    
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

# LIBRARY IMPORTS -----------------------------------
while True:
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        import time
        import random
        import math as math
        break
    except:
        print("One or More Missing Dependancies. "
              "Missing Libraries Could Include: "
              "Numpy, Matplotlib")
        break

# FILE IMPORTS -----------------------------------
while True:
    try:
        from creatures import *
        from colourtable import *
        break
    except ImportError:
        print("One or More Missing Files."
              "Files Could Include: "
              "creatures.py OR colourtable.py")
        break

# FUNCTION DEFINITIONS -----------------------------------

def build_yard(dims):
    
    '''
    Function Info:

    This is the function responsible for plotting the yard. 
    
    An array of zeros is made in accordance with the defined 
    dimensions when called into main through the argument 'dims'. 
    
    In this case it is 60x40.

    '''

    plan = np.zeros(dims)   # Defines the variable 'plan' to be the array of 
                            # zeros of the defined dimensions 'dims' which
                            # when calledinto mains creates a 60x40 zeros 
                            # array.

    fenceroad = plan[0:60, 0:40] = 0    # Assigned the fence to be equal to 0. 
                                    # When the colourmap is applied, this will 
                                    # represent a black colour. Array slicing 
                                    # is used in order to save time instead of  
                                    # doing each array coordiante individually

    grass = plan[1:49, 1:39] = 5    # Assigned the grass to be equal to 5. 
                                    # When the colourmap is applied, this will 
                                    # represent a green colour. Array slicing 
                                    # is used in order to save time instead of  
                                    # doing each array coordiante individually

    house = plan[30:50, 1:30] = 7   # Assigned the fence to be equal to 8. 
                                    # When the colourmap is applied, this will 
                                    # represent a yellow colour. Array slicing 
                                    # is used in order to save time instead of  
                                    # doing each array coordiante individually

    veranda = plan[30:35, 1:30] = 4.5   # Assigned the fence to be equal to 0. 
                                        # When the colourmap is applied, this
                                        # will represent a black colour. Array 
                                        # slicing is used in order to save   
                                        # time instead of doing each array 
                                        # coordiante individually

    path = plan[50:55, 0:40] = 10   # Assigned the grass to be equal to 10. 
                                    # When the colourmap is applied, this will 
                                    # represent a grey colour. Array slicing 
                                    # is used in order to save time instead of  
                                    # doing each array coordiante individually
                                    
    tree = plan[2:9, 31:38] = 4.5   # Assigned the grass to be equal to 4.5. 
                                    # When the colourmap is applied, this will 
                                    # represent a brown/green colour. Array
                                    # slicing is used in order to save time  
                                    # instead of doing each array coordiante 
                                    # individually

    return plan    # Returns the plan array when all slicing is applied when 
                   # called in main.


def build_smells(dims):

    '''
    Function Info:

    This function is responsible for building the smell yard for the 
    secondary plot. 
    
    An array of zeros is made in accordance with the 
    defined dimensions when called into mains through the argument 
    'dims'. 
    
    In this case it is a 60x40 array.

    '''

    plan = np.zeros(dims)
    return plan   


def build_sounds(dims):

    '''
    Function Info:

    This function is responsible for building the sounds yard for the 
    secondary plot. 
    
    An array of zeros is made in accordance with the 
    defined dimensions when called into mains through the argument 
    'dims'. 
    
    In this case it is a 60x40 array.

    '''

    plan = np.zeros(dims)
    return plan


def update_smells(smells, creatures):

    '''
    Function Info:

    This function is responsible for updating the smells of the 
    creatures based on there position on the plot. 
    
    An array which is argumented as smells assigns the current 
    position of the creatures (humans,neighbor, puppy and squirrel)
    to be 10 through the process of overwriting the current value of
    the array at said position.

    The value of 10 is used as when the 'grey' colourmap is applied, 
    the value represents white. 
    
    When the creature moves, the previous position is assigned to a 
    lighter colour due to the fact that the creature has moved and the
    source of smell has reduced.

    '''

    smells[creatures.get_pos()] = 10
    smells[creatures.get_prevpos()] = 3
    

def update_sounds(sounds, creatures):

    '''
    Function Info:

    This function is responsible for updating the sounds of the 
    creatuers based on there position on the plot.

    An array which is argumented as sounds assigns the current position
    of the creatures (humans,neighbor, puppy and squirrel) to be 10 
    through the process of overwriting the current value of the array 
    at said position.

    The value of 10 is used as when the 'grey' colourmap is applied, 
    the value represents white. 
    
    When the creatures move, there previous position is marked as 0 
    as the source of sound has moved away.

    '''

    sounds[creatures.get_pos()] = 10
    sounds[creatures.get_prevpos()] = 0


#def clear_sound(sounds, creatures):

    '''
    Function Info:
    
    This function was used as a test function to check whether previous
    positions of sounds wound be overwritten to the default value of 0.

    '''

    #sounds[creatures.get_prevpos()] = 0


def plot_yard(axis, plot):

    '''
    Function Info:

    This function is responsible for for plotting the yard on the first
    set of axes with the 'nipy-spectral' colourmap.

    There are 5 calls of the annotate function of matplotlib which 
    allow for the labeling of the parts of the plot.
    
    The imshow function calls for the plot to be displayed with the 
    desired axis when called into the simulation function with the 
    desired plotting information derived from the argument 'plot'.

    '''

    axis.annotate("HOUSE", xy = (12,40), xytext = (12, 40))
    axis.annotate("VERANDAH" , xy = (15, 35) , xytext = (11,31))
    axis.annotate("TREE", xy = (32, 5), xytext = (32,2))
    axis.annotate("PATH" , xy = (15, 53) , xytext = (11,53))
    axis.annotate("ROAD", xy = (15, 57) , xytext = (11,57), c="white")
    axis.imshow(plot, cmap = "nipy_spectral")


def plot_smells(axis, plot):

    '''
    Function Info:

    This function is responsible for plotting the smells onto the 
    second set of axes.
    
    The inshow function calls the plot image of the smells axis on the 
    desired axis set with the 'gray' colourmap using the desired plot 
    information derived from the argument 'plot'.

    '''

    axis.imshow(plot, cmap = "gray")


def plot_sounds(axis, plot):

    '''
    Function Info:

    This function is responsible for plotting the sounds onto the 
    second set of axes.

    The inshow function calls the plot image of the sounds axis on the 
    desired axis set with the 'gray' colourmap using the desired plot 
    information derived from the argument 'plot'.

    '''

    axis.imshow(plot, cmap = "gray")


def creature(listname):

    '''
    Function Info:

    Test function used to test the creation of creatures to be called 
    into the simulation function to be plotted. Listname is the desired
    list of creatures where the objects will be appended.

    '''

    #listname.append(Puppy("Snoopy", "white/black", (5,15), (5,14), 74))
    #listname.append(Squirrel("Sandy Cheeks","Orange/Beige",(5,35),(5,4), 43))
    pass


def human(humanlist):

    '''
    Function Info:

    Test function used to test the creation of humans to be called into
    the simulation function to be plotted. 

    Listname is the desired list of humans where the objects will be 
    appended.

    '''

    #humanlist.append(Human("Charles", "black/bisque", (35, 15), (35,15), 30))
    pass


def neighbor(neighborlist):

    '''
    Function Info:

    Test function used to test the creation of neighbors to be called
    into the simulation function to be plotted. Listname is the desired
    list of neighbors where the objects will be appended.

    '''

    #neighborlist.append(Neighbor("Geoff","red/bisque", (50,1), (50,0), "35"))
    pass


def human_move_drop_treat(humanlist):

    '''
    Function Info:

    This function is used when the owner/human moves towards the edge 
    of the verandah to drop the treat and it calls the respective 
    stepchange function that lets him achieve that. 

    The argument humanlist is targeting this function to only apply to 
    all elements in the desired list of humans.

    '''

    for i in humanlist:
        i.step_change_drop_treat()


def human_move_normal(humanlist):
    
    '''
    Function Info:

    This function is used when the owner/human has dropped and it calls
    the respective stepchange function ('step_change_normal()') that 
    initiates normal movement.

    The argument humanlist is targeting this function to only apply to 
    all elements in the desired list of humans.

    '''

    for i in humanlist:
        i.step_change_normal()


def creature_move(listname):

    '''
    Function Info:

    This function is used when the creatures are moving normally and 
    the respective stepchange function ('step_change()') that initiates
    normal movement.

    The argument listname is targeting this function to only apply to 
    all elements in the desired list of creatures.

    '''

    for i in listname:
        i.step_change()


def neighbor_move(neighborlist):

    '''
    Function Info:

    This function is used for the normal movement of the neighbor when 
    the respective stepchange function ('step_change_right()') is called.

    The argument neighborlist is targeting this function to only apply 
    to all elements in the desired list of neighbors.

    '''

    for i in neighborlist:
        i.step_change_right()


def creature_plot(listname, axis, sizing, smell, sound):
   
    '''
    Function Info:

    This major function is responsible for some major behavious of the 
    plots and creatures. 

    For every creature in the respetive creatures list, the 'plot_me()' 
    function of the creatures are called to plot them on the respective
    set of axes and in accordance to the matplotlib patch sizings.

    Furthermore, for every creature, there smells and sounds are 
    updated automatically on the respective axes using corresponding 
    arrays for smells and sounds.

    '''

    for c in range(len(listname)):
        listname[c].plot_me(axis, sizing)
        update_smells(smell, listname[c])
        update_sounds(sound, listname[c])
        #clear_sound(sound, listname[c])


def human_plot(humanlist, axis, sizing, smell, sound):
    
    '''
    Function Info:

    This major function is responsible for some major behavious of the 
    plots and humans. 
    
    For every human in the respetive humans list, the 'plot_me()' 
    function of the humans are called to plot them on the respective 
    set of axes and in accordance to the matplotlib patch sizings.

    Furthermore, for every human, there smells and sounds are updated
    automatically on the respective axes using the corresponding arrays
    for smells and sounds.

    '''

    for c in range(len(humanlist)):
        humanlist[c].plot_me(axis, sizing)
        update_smells(smell, humanlist[c])
        update_sounds(sound, humanlist[c])
        #clear_sound(sound, humanlist[c])   # Test code used to test the 
                                            # clear_sound function before it
                                            # was implemeneted into 
                                            # update_sounds.


def neighbor_plot(neighborlist, axis, sizing, smell, sound):

    '''
    Function Info:

    This major function is responsible for some major behavious of the
    plots and neighbors. 

    For every neighbor in the respetive neighbor list, the 'plot_me()' 
    function of the neighbor are called to plot them on the respective
    set of axes and in accordance to the matplotlib

    patch sizings. Furthermore, for every neighbor, there smells and 
    sounds are updated automatically on the respective axes using the
    corresponding arrays for smells and sounds.

    '''

    for c in range(len(neighborlist)):
        neighborlist[c].plot_me(axis,sizing)
        update_smells(smell, neighborlist[c])
        update_sounds(sound, neighborlist[c])
        #clear_sound(sound, neighborlist[c])    # Test code used to test 
                                                # clear_sound function before 
                                                # it was implemented into 
                                                # update_sounds.


def treat_plot(treatno):

    '''
    Function Info:

    This function is responsible for assigning and printing the 
    randomised positions of the treats to a list called treatpositions
    and returning the value of that list when it is called in the plot
    function for treats, toys and acorns.

    The number of spawns are based on the input argument treatno which
    is defined to be 1.

    '''

    treatpositions = []

    for i in range(treatno):
        treatpositions.append((random.randrange(1,29), 
                               random.randrange(1,25)))
        
    print(f"Treat Spawns {treatpositions}")

    return treatpositions


def toy_plot(toyno):

    '''
    Function Info:

    This function is responsible for assigning and printing the 
    randomised positions of the toys to a list called toyposition and 
    returning the value of that list when it is called in the plot 
    function fortreats, toys and acorns.

    The number of spawns are based on the input argument toyno which 
    is defined to be 1.

    '''

    toyposition = []

    for i in range(toyno):
        toyposition.append((random.randrange(1,29), 
                            random.randrange(1,30)))
        
    print(f"Treat Spawns {toyposition}")

    return toyposition


def acorn_plot(acornno):

    '''
    Function Info:

    This function is responsible for assigning and printing the 
    randomised positions of the acorns to a list called acornposition 
    and returning thevalue of that list when it is called in the plot 
    function for treats, toys and acorns.

    The number of spawns are based on the input argument acornno which 
    is defined to be 1.

    '''

    acornposition = []

    for i in range(acornno):
        acornposition.append((random.randrange(1,29), 
                              random.randrange(1,30)))
        
    print(f"Acorn Spawns {acornposition}")

    return acornposition


def place_toy(toyno, listname):

    '''
    Function Info:

    This function is responsible for assigning the position of the 
    burying or placing of the toy based on the x and y coordinate of 
    the puppy. 

    The position is assigned to an empty list and the position is 
    printined. This is done for the amount of toys assigned by the 
    argument toyno which is defined as 1. 

    Furthermore it gains the positional information from the argument
    listname and position 0 "[0]" which corresponds to the position of 
    the puppy. 

    This funciton returns the values in the list.

    '''

    toyplace = []
    x = listname[0].get_pos()[1]
    y = listname[0].get_pos()[0]

    for i in range(toyno):
        toyplace.append((y,x))
    print(f"Toy was Placed/Buried at {toyplace}")

    return toyplace


def plot_placed_toy(toyno, yard, smell, listname):

    '''
    Function Info:

    This function is responsible for reflecting the position of the toy
    when the puppy decides to place/bury it.
    
    The function calls placement coordinates from the 'place_toy' 
    function and then based on 2 values (7 = bury, 8 = place/drop)
    which are randomly selected determine whether the puppy either 
    drops or burys the toy. 
    
    Furthermore the smells is also plotted on the respective smell plot
    and since toys typically don't have a strong scent the intensity of
    the smell is 5.

    '''
    
    toyplaced = place_toy(toyno, listname)

    pval = [7, 8]

    for i in toyplaced:
        yard[i] = random.choice(pval)
        smell[i] = 5



def plot_treat_acorn_toy(treatno, acornno, yard, smell, listname):

    '''
    Function Info:

    This function is responsible for printing the number of treats and 
    acorns. It also calls the list of positions for the treats and 
    acorns generated above by the treat_plot and acorn_plot functions.

    For each element in the treat and acorn list, the treat is plotted
    to the yard with a blue colour (2) and to the smells plot with a 
    white colour (10) and the acorn is plotted to the yard with a light
    brown colour (4.6) and smell plot with a white colour (10).
    
    Furthermore, this function also assigns the positional information 
    of the treat/acorn to the puppy and squirrel respectivley and then 
    sets the alternative movement algorithm to True that allows the 
    puppy and squirrel to move towards the treat and acorn respectivley
    by overriding the default movement algorithm.

    '''

    print(f"Number of Treats: {treatno}")
    print(f"Number of Acorns: {acornno}")

    treatpositions = treat_plot(treatno)
    acornposition = acorn_plot(acornno)

    for i in treatpositions:
        yard[i] = 2
        smell[i] = 10
        listname[0].treat_position = i
        listname[0].move_towards_treat = True

    for i in acornposition:
        yard[i] = 4.6
        smell[i] = 10
        listname[1].acorn_position = i
        listname[1].move_towards_acorn = True


def plot_toy(toyno, yard, smell, sound, listname):

    '''
    Function Info:

    This function is responsible for printing the number toys. It also
    calls the list of positions for the toys generated above by the 
    toy_plot function.
    
    For each element in the toy list, the toy is plotted to the yard 
    with an orange colour (8), to the smells plot with a white colour
    (10) and the sounds plot with a grey colour (8) which indicates
    a fairly loud sound.
    
    Furthermore, this function also assigns the positional information 
    of the toy to the puppy and then sets the alternative movement 
    algorithm to True that allows the puppy to move towards the toy by
    overriding the defauly movement algorithm.

    '''

    print(f"Number of Toys: {toyno}")
    toyposition = toy_plot(toyno)  
    
    for i in toyposition:
        yard[i] = 8
        smell[i] = 5
        sound[i] = 8
        listname[0].toy_position = i
        listname[0].move_towards_toy = True    


def clear_acorns(yard, listname):
    
    '''
    Function Info:

    This function is responsible for clearing the position of the acorn 
    off of the yard using the yard array and position of the squirrel 
    which is in the first position of the creatures list. 5 represents 
    the grass colour.

    '''

    x = (listname[1].acorn_position)[1]
    y = (listname[1].acorn_position)[0]

    yard[y,x] = 5


def clear_toys(yard, listname):

    '''
    Function Info:

    This function is responsible for clearing the position of the toy 
    off of the yard using the yard array and position of the puppy 
    which is in the zero position of the creatures list. 5 represents
    the grass colour.

    '''

    x = (listname[0].toy_position)[1]
    y = (listname[0].toy_position)[0]

    yard[y,x] = 5


def clear_treats(yard, listname):

    '''
    Function Info:

    This function is responsible for clearing the position of the treat
    off of the yard using the yard array and position of the puppy 
    which is in the zero position of the creatures list. 5 represents 
    the grass colour.

    '''

    x = (listname[0].treat_position)[1]
    y = (listname[0].treat_position)[0]

    yard[y,x] = 5


def creaturehealth(listname, i):

    '''
    Function Info:

    This function is responsible assigning the health loss of each 
    creature in the list of creatures. 
    
    If the heath of the creature is < 50, the normal movement algorithm
    is overwritten and the creatures stop moving signifiying that they 
    have gone to sleep and are tired this is activated using the
    n.tired = True statement. 

    The health is only displayed when it is > 0.

    '''

    for n in listname:
        hp = n.healthloss(n.health, i)

        if hp > 0:
            print(f"{n.name} Health: {hp}")

        if hp < 50:
            n.tired = True


def simulation(timestep, axis1, axis2, axis3, listname, sizing, 
               mainyard_build, smells_build, sounds_build, figure, sleep_time,
               humanlist, iteration, treatno, acornno, yard, smell, sound, 
               toyno, holdtime, neighborlist):
    
    '''
    This is the main simulation function that draws from all the above
    functions and creatures.py to run the simulation itself.
    
    The timestep is a userdefined value which determines for how long
    the simulation will run.

    axis 1, 2 and 3 represent the yard, smells and sound plots 
    respectivley and so the set_title function is called to set the 
    titles of the plot.

    When the iteration, a user defined value which determines at what
    n'th timestep the neighbor and human move, and the timestep (i) 
    have modulus == 0, the humans movement towards dropping the treat 
    is activated. 

    Furthermore, the normal movement is also activated as a combination
    of both are used in order to achieve a natural movement towards 
    dropping the treat and then having a smooth transition to normal 
    movement once treats have been dropped. 
    
    The movmement of the neighbor is also initiated when the modulus 
    is == 0.

    When the humans position is == 30 on the y-axis, (edge of verandah) 
    and the counter is < 1, the treat and acorn are plotted on the map. 
    The counter is used to avoid duplicate and unwanted spawns as once
    a spawn cycle occurs the counter is set to 1 and so it is not 
    possible for unwanted spawns to occur.

    When the neighbors position is == 35 on the x-axis (fence) and the 
    counter is < 1, the toy are plotted on the map as if the neighbor 
    threw the toy over the fence. 
    
    The counter is used to avoid duplicate and unwanted spawns as once
    a spawn cycle occurs the counter is set to 1 and so it is not 
    possible for unwanted spawns to occur.

    If the position of the squirrel (listname[1]) and acorn are equal,
    then the acorn_collected boolean is set to True and then only is it
    removed off the plot.

    If the position of the puppy (listname[0]) and the toy/treat are 
    equal, then the treat_collected/toy_collceted booleans are set to 
    True and then only are they removed off the plot.

    There is a counter system within the toy removal code that only 
    removes it for a certain number of timesteps which is userdefined
    by "holdtime" afterwhich the toy will either be buried or placed.

    creaturehealth is a function that calls the current health of each
    creature at the given timestep.

    The three successive creature_plot, human_plot, neighbor_plot 
    functions all have the same purpose which is the plot the position
    of the respective elements on the the yard, smells and sounds plot 
    usingthe respective arguments for each function.

    The three successive plot_yard, plot_smells, plot_sounds functions 
    all have the same purpose which is to plot the respective plots in 
    the figure window using the respective axes and data arrays.

    The use of the canvas_draw function allows for the refreshing of 
    the plot without having to reopen the plot window. This then as a
    result refreshes the plot at each timestep.

    canvas.flush_events clears all the commands running on the plot 
    before refreshing the plot.

    axis1.clear() to axis3.clear() clear the axis after all commands 
    have been flushed.

    time.sleep(sleep_time) is a function that allows the user to input
    for how long each timestep is displayed on the figure before being 
    flushed.

    '''


    creature(listname)  # testcode that returns values from the creatures 
                        # function

    human(humanlist)    # testcode that returns values from the humans 
                        # function

    neighbor(neighborlist)  # testcode that returns values from the neighbor
                            # function.

    counter = 0

    counter2 = 0

    counter3 = 0

    for i in range(timestep):
        
        print(f"\n---- TIMESTEP {i+1} ----")
        axis1.set_title(f'Simulation Movement Timestep {i+1}')
        axis2.set_title(f'Smell Timestep {i+1}')
        axis3.set_title(f'Sound Timestep {i+1}')

        creature_move(listname)
        
        if i % iteration == 0:
            
            human_move_drop_treat(humanlist)
            human_move_normal(humanlist)
            neighbor_move(neighborlist)

        if humanlist[0].get_pos()[0] == 30 and counter < 1:

            counter = counter + 1
            plot_treat_acorn_toy(treatno, acornno, yard, smell, listname)

        if neighborlist[0].get_pos()[1] == 35 and counter3 < 1:
            counter3 = counter3 + 1
            plot_toy(toyno, yard, smell, sound, listname)

        if listname[1].acorn_collected is True:
            clear_acorns(yard, listname)
        
        if listname[0].treat_collected is True:
            clear_treats(yard, listname)

        if listname[0].toy_collected is True:
            clear_toys(yard, listname)
            counter2 = counter2 + 1

        if counter2 == holdtime:
            plot_placed_toy(toyno, yard, smell, listname)

        creaturehealth(listname, i)

        creature_plot(listname, axis1, sizing, smells_build, sounds_build)
        human_plot(humanlist, axis1, sizing, smells_build, sounds_build)
        neighbor_plot(neighborlist, axis1, sizing, smells_build, sounds_build)

        plot_yard(axis1, mainyard_build)
        plot_smells(axis2, smells_build)
        plot_sounds(axis3, sounds_build)

        figure.canvas.draw()
        figure.canvas.flush_events()
        axis1.clear()
        axis2.clear()
        axis3.clear()
        time.sleep(sleep_time)

        

# MAIN FUNCTION DEFINITION -----------------------------------


def main():
    
    '''
    This is the main function that calls in all the other respective 
    functions in order to allow the simulation to work.

    Some predefined values are determined as defaults which allows the
    simulation to work regardless whether the user gives inputs or not.
    Such values include all values from simrun to sounds as well as 
    simrun to holdtime.

    There is also some quality of life/ease of life implementations 
    such as the strings that allow bolding and unbolding of text for 
    the command line. These are defined as btext = bold and unbtext 
    = unbold.

    verifyedits is the first input that allows the user to run the 
    simulation based off there own parameters or use the predefined
    values.

    The whileloop may be frowned upon, however in this instance it 
    has valid reason to exist as it allows for the perpetual existance
    of the terminal until the user decides to terminate it. This is for
    ease of use as well as to cycle through inputs again if invalid 
    inputs are selected/entered.


    While the input of verifyexits is not equal to X then the program 
    will run. If Y is entered, the "Customisation Studio" is launched 
    which allows for a comprehensive amount of changes to the 
    simulation to be made by the user ranging from timesteps all the
    way to names, ages and colours of elements in the simulation. 
    If "N" is selected in verifyedits, then the preloaded default 
    parameters will takeover to run the simulation.

    Exception handling is used in the Customisation Studio as it 
    ensures that user-inputs are valid and do not crash the program. 
    Exception handling is particularly used to avoid non-integer values 
    from being entered into the code causing a ValueError and the use 
    of the absolute function of integer inputs simrun to holtime ensure
    there is no negative integer errors.

    The user in the Customisation Studio is expected to choose the 
    name, colours and age of the human, squirrel, puppy and neighbor.
    The user is also presented with the option to display an allowable 
    selection of CSS4 compatible colours in Matplotlib.

    Then the simulation function is called and the simulation is run. 
    This is done when plt.ion() (Interactive Plot) is enabled and the 
    subplots of yard, smells and sounds is plotted with a figuresize 
    total of 15x10.

    Once all timesteps are run, the plot will close.


    '''
    size = (60,40)
    treatno = 1
    acornno = 1
    toyno = 1
    yard = build_yard(size)
    smells = build_smells(size)
    sounds = build_sounds(size)

    btext = "\033[1m"
    unbtext = "\033[0m"

    #creature_list = [] testcode for predetermined values
    #human_list = [] testcode for predtermined values
    #neighbor_list = [] testcode for predetermined values

    simrun = 200
    timesleep = 0
    iteration = 2
    holdtime = 30
 
    
    print(f"\n{btext}WELCOME TO THE SIMULATION{unbtext}\n")

    verifyedits = input("Would you like to adjust any parameters? (Y/N) "
                        "or Enter (X) to exit... ")
    
    while verifyedits.upper() != "X":

        if verifyedits.upper() == "Y":

            creature_list = []
            human_list = []
            neighbor_list = []

            print(f"\n{btext}Welcome to the customisation studio{unbtext}\n\n" 
                  f"Please take note of the following things before getting\n"
                  f"started...\n1) If you choose to use the default values,\n"
                  f"   please enter as shown\n\n2) The format of colours\n"
                  f"   are 'colour1/colour2' one is also accepted.\n\n3)"
                  f" Be very careful as to how you enter the values otherwise\n"
                  f"   errors may occur")

                

            print(f"\n{btext}GENERAL PARAMETERS{unbtext}\n")

            while True:
                try:
                    simrun = abs(int(input("Please enter the amount of "
                                           "simulation iterations you would "
                                           "like to run (Default: 200)... ")))
        
                    timesleep = abs(int(input("Please enter the how long you "
                                              "would like each timestep to "
                                              "last (seconds) (Default: 0)... ")))
                    
                    iteration = abs(int(input("At what interval of timestep "
                                              "would you like the human and "
                                              "neighbour to move to place the "
                                              "toy, acorn and treat? "
                                              "(Default: 1)... ")))
                    
                    holdtime = abs(int(input("For how many timesteps would "
                                             "you like the "
                                             "puppy to play with the toy? "
                                             "(Default: 30)... ")))

                except ValueError:
                    print("Invalid Input. " 
                          "Entered value(s) was/were not an integer.")

                else:
                    print(f"\n{btext}PUPPY CREATOR{unbtext}\n")
                    puppyname = input("What is the name of the Puppy "
                                      "(Default: Snoopy)... ")
                    
                    ctable = input(f"Enter (Y) to see the table of colours "
                                   f"for the colour(s) of {puppyname} or "
                                   "anything else to continue... ")
                    
                    if ctable.upper() == "Y":
                        plot_colortable(mcolors.CSS4_COLORS)
                        plt.show()

                    else:
                        print("\nContinuing\n")

                    puppycolour = input(f"What is the colour(s) of "
                                        f"{puppyname} (Please enter 2 colours "
                                        "separated only by a '/' with no "
                                        "spaces. Note that the second colour "
                                        "is primary. (Default: white/black)"
                                        "... ")
                    
                    puppyage = abs(int(input(f"How old is {puppyname}... ")))

                    creature_list.append(Puppy(puppyname, puppycolour, (5,15), 
                                               (5,14), puppyage))
                    
                    print(f"\n{btext}SQUIRREL CREATOR{unbtext}\n")

                    squirrelname = input("What is the name of the Squirrel "
                                         "(Default: Sandy Cheeks)... ")

                    ctable = input(f"Enter (Y) to see the table of colours "
                                   f"for the colour(s) of {squirrelname} or "
                                   "anything else to continue... ")
                    
                    if ctable.upper() == "Y":
                        plot_colortable(mcolors.CSS4_COLORS)
                        plt.show()

                    else:
                        print("\nContinuing\n")

                    squirrelcolour = input(f"What is the colour(s) of "
                                           f"{squirrelname} (Please enter 2 "
                                           "colours separated only by a '/' "
                                           "with no spaces. Note that the "
                                           "second colour is primary. "
                                           "Default: orange/beige)... ")
                    
                    squirrelage = abs(int(input(f"How old is "
                                                f"{squirrelname}... ")))

                    creature_list.append(Squirrel(squirrelname, 
                                                  squirrelcolour, (5,35), 
                                                  (5,34), squirrelage))


                    print("\nOWNER/HUMAN CREATOR\n")

                    humanname = input("What is the name of the Human/Owner "
                                      "(Default: Charles)... ")
                    

                    ctable = input(f"Enter (Y) to see the table of colours "
                                   f"for the colour(s) of {humanname} "
                                   "or anything else to continue... ")
                    
                    if ctable.upper() == "Y":
                        plot_colortable(mcolors.CSS4_COLORS)
                        plt.show()

                    else:
                        print("\nContinuing\n")

                    humancolour = input(f"What is the colour(s) of "
                                        f"{humanname} (Please enter 2 colours "
                                        "separated only by a '/' with no "
                                        "spaces. Note that the second colour "
                                        "is primary. Default: "
                                        "black/bisque)... ")
                    
                    humanage = abs(int(input(f"How old is {humanname}... ")))

                    human_list.append(Human(humanname, humancolour, (35,15), 
                                            (35,15), humanage))
                    

                    print("\nNEIGHBOR CREATOR\n")

                    neighborname = input("What is the name of the Neighbor "
                                         "(Default: Geoff)... ")
                    
                    ctable = input(f"Enter (Y) to see the table of colours "
                                   f"for the colour(s) of {neighborname} or "
                                   "anything else to continue ... ")
                    
                    if ctable.upper() == "Y":
                        plot_colortable(mcolors.CSS4_COLORS)
                        plt.show()
                    else:
                        print("\nContinuing\n")

                    neighborcolour = input(f"What is the colour(s) of "
                                           f"{neighborname} (Please enter 2 "
                                           "colours separated only by a '/' "
                                           "with no spaces. Note that the "
                                           "second colour is primary. "
                                           "Default: red/bisque)... ")
                    
                    neighborage = abs(int(input(f"How old is "
                                                f"{neighborname}... ")))

                    neighbor_list.append(Neighbor(neighborname, 
                                                  neighborcolour, (50,1), 
                                                  (50,0), neighborage))


                    print("-- STARTING SIMULATION WITH CUSTOM VALUES --")
                    print(f"Simulation Runs: {simrun} | Run Length: "
                          "{timesleep}")

                    yard = build_yard(size)
                    smells = np.zeros(size)
                    sounds = np.zeros(size)

                    plt.ion()
                    fig, (axs1, axs2, axs3) = plt.subplots(1,3,
                                                           figsize=(15,10))
                    
                    simulation(simrun, axs1, axs2, axs3, creature_list, size, 
                               yard, smells, sounds, fig, timesleep, 
                               human_list, iteration, treatno, acornno, 
                               yard, smells, sounds, toyno, holdtime, 
                               neighbor_list)
                
                    plt.close()

        elif verifyedits.upper() == "N":
            
            creature_list = []
            human_list = []
            neighbor_list = []

            creature_list.append(Puppy("Snoopy", "white/black", (5,15), 
                                       (5,14), 74))
            
            creature_list.append(Squirrel("Sandy Cheeks", "Orange/Beige", 
                                          (5,35), (5,34), 43))
            
            human_list.append(Human("Charles", "black/bisque", (35, 15), 
                                    (35,15), 30))
            
            neighbor_list.append(Neighbor("Geoff", "red/bisque", (50,1), 
                                          (50,0), "35"))
    
            print("-- STARTING SIMULATION WITH DEFAULT VALUES --")
            print(f"Simulation Runs: {simrun} | Run Length: {timesleep}")

            yard = build_yard(size)
            smells = np.zeros(size)
            sounds = np.zeros(size)

            plt.ion()
            fig, (axs1, axs2, axs3) = plt.subplots(1,3,figsize=(15,10))
            simulation(simrun, axs1, axs2, axs3, creature_list, size, 
                       yard, smells, sounds, fig, timesleep, 
                       human_list, iteration, treatno, acornno, 
                       yard, smells, sounds, toyno, holdtime, 
                       neighbor_list)
            
            plt.close()
        
        else:
            print("You have entered an invalid input. Please try again.")

        verifyedits = input("Would you like to adjust any parameters? (Y/N) "
                            "or Enter (X) to exit... ")

    else:
        print(f"\n{btext}GOODBYE{unbtext}\n")
    
    


# CODE RUNNING HARNESS -----------------------------------
if __name__ == "__main__":

    '''
    Runs the main function.
    '''

    main()
