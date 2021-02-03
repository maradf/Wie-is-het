import pyglet
from pyglet.window import key
from pyglet.window import mouse
from os import listdir
import random
from math import floor

class Group():
    """
    Class Group. Contains all information of a single group.

    Init variables:
    path (str): Path leading to the folder containing all data of the group. Does not include folder name itself.
    name (str): name of the group, and name of the folder.
    """
    
    def __init__(self, path, name):
        self.path = path + name + "/"
        self.name = name
        self.members = []
        self.memberFiles = listdir(self.path)
        self.load_members()

    def load_members(self):
        """
        Loads all members/information from the folder. 
        """
        for memberfile in self.memberFiles:
            self.add_member(Member(self.name, self.path, memberfile))

    def __str__(self):
        return self.name

    def __len__(self):
        return len(members)
    
    def add_member(self, member):
        """ Add member to group"""
        self.members.append(member)
    
    def remove_member(self, member):
        """ If member exists in group, remove it"""
        if member in self.members:
            self.members.remove(member)
    
    def get_members(self):
        """ Get all members of the group"""
        return self.members

    def print_members(self):
        """ Prints the names of all members"""
        return [member.name for member in self.members]

    def get_member_files(self):
        """ Gets the memberfiles."""
        return self.memberFiles

    def get_path(self):
        """ Gets self.path"""
        return self.path

class Member():
    """
    Class Member. Contains all information of a single member.

    Init variables:
    group (str): Name of the group member belongs to.
    folder (str): Folder in which the image is saved.
    filename (str): Filename of the image.
    """
    def __init__(self, group, folder, filename):
        self.group = group
        self.folder = folder
        self.filename = filename
        self.image = pyglet.image.load(folder + filename)
        self.name = filename.split(".")[0]

        # The following variables were required for subsequent code to work
        # as some functions require the image to have certain features
        self.width = self.image.width
        self.height = self.image.height
        self.blit_to_texture = self.image.blit_to_texture
        self.get_texture = self.image.get_texture

    def __str__(self):
        return self.name

    def get_group(self):
        return self.group

    def get_folder(self):
        return self.folder

    def get_filename(self):
        return self.filename

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name


class Board():

    def __init__(self, groups, path="Groups/"):
        self.people, self.names = load_people(groups, path)

    def __str__(self):
        return self.names
    
    def __len__(self):
        return len(self.names)
    
    def get_names(self):
        return self.names
    
    def get_people(self):
        return self.people
    
    def get_image(self, name):
        return self.people[self.names.index(name)]

    
    def load_people(groups, path):
        people = []
        names = []
        for groupname in groups:
            grouppath = path + groupname + "/"
            for memberfile in listdir(grouppath):
                member = Member(groupname, grouppath, memberfile)
                people.append(member)
                names.append(member.name)

        return people, names

path = "Groups/"

# Set up MX and TXT data and shuffle
mx = Group(path, "BTS")
txt = Group(path, "Astro")
photos = mx.get_members() + txt.get_members()
random.shuffle(photos)

# Create display
display = pyglet.canvas.get_display()
screens = display.get_screens()
window = pyglet.window.Window(resizable=True, style='dialog', caption="Wie Is Het? K-Pop Edition")
window.set_minimum_size(320, 200)
window_width = 1280
window.set_size(window_width, 720)

# Create batch
batch = pyglet.graphics.Batch()
windowsize = window.get_size()
num_photos = len(photos)
fit_on_x = floor((windowsize[0] - 10) / 250)
print("fit on x", fit_on_x)

# Caclulate location for each sprite and save these values
sprites = []
sprite_locs = []
x = 10
y = 10
for i, photo in enumerate(photos):
    sprites.append(pyglet.sprite.Sprite(img=photo, batch=batch, x=x, y=y))
    sprite_locs.append((x, y))
    if (i + 1) % fit_on_x == 0:
        x = 10
        y += 330
    else:
        x += 250

# Set window height so that all images fit        
window.set_size(window_width, y + 330)

# Draw window
@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

# Events for when mouse button is pressed
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        person = locate_picture(x, y)
        if person:
            print("The picture in question is", person)
        else:
            print("Please click on a picture.")

def locate_picture(mouse_x, mouse_y):
    """
    Checks which image was clicked in the window. 

    Input: 
    mouse_x (int): x coordinate of the mouse when the mouse press event happened
    mouse_y (int): y coordinate of the mouse when the mouse press event happened

    Output:
    If a person was clicked:
    Member: the member clicked by the user

    If a person was not clicked: False (bool)
    """
    for min_x, min_y in sprite_locs:
        max_x = min_x + 240
        max_y = min_y + 320
        if min_x < mouse_x and max_x > mouse_x and min_y < mouse_y and max_y > mouse_y:
            i = sprite_locs.index((min_x, min_y))
            return(photos[i])
        else: 
            False

pyglet.app.run() 