import pyglet
from pyglet.window import key
from pyglet.window import mouse
from os import listdir
import os.path
import random
from math import floor
from PIL import Image

class Group():
    """
    Class Group. Contains all information of a single group.

    Init variables:
    path (str): Path leading to the folder containing all data of the group. Does not include folder name itself.
    name (str): name of the group, and name of the folder.
    """
    
    def __init__(self, path, name, batch):
        self.path = path + name + "/"
        self.name = name
        self.members = []
        self.memberFiles = listdir(self.path)
        self.batch = batch
        self.load_members(self.checkGrey())
        
    def checkGrey(self):
        """ Checks if a grey scale image exists in the folder.
            Returns True if yes, False if no.
        """
        for f in self.memberFiles:
            if "grey" in f:
                return True
        return False

    def load_members(self, grey):
        """
        Loads all members/information from the folder. 
        """
        for memberfile in self.memberFiles:
            # Only creates a member for each colored image.
            if "grey" not in memberfile:
                self.add_member(Member(self.name, self.path, memberfile, self.batch, grey))
            

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

class Member(pyglet.sprite.Sprite):
    """
    Class Member of type pyglet.sprite.Sprite
    Contains all information of a single member.

    Init variables:
    group (str): Name of the group member belongs to.
    folder (str): Folder in which the image is saved.
    filename (str): Filename of the image.
    """
    def __init__(self, group, folder, filename, batch, grey):
        pyglet.sprite.Sprite.__init__(self, pyglet.image.load(folder + filename), batch=batch)
        self.group_name = group
        self.folder = folder
        self.filename = filename
        self.color_image = pyglet.image.load(folder + filename)
        self.colored = True # Initially the colored image is used
        split_filename = filename.split(".")
        if filename.count(".") == 1:
            self.name, self.extension = filename.split(".")
        else:
            split_filename = filename.split(".")
            self.name = ".".join(split_filename[:-1])
            self.extension = split_filename[-1:][0]
        self.get_texture = self.image.get_texture
        self.grey_path = self.folder + self.name + "_grey." + self.extension
        self.color_path = folder + filename
        
        if not grey:
            self.make_grey_image()
        self.grey_image = pyglet.image.load(self.grey_path)

    def make_grey_image(self):
        """ Creates the greyscale version of the image in question.
        Saves it in the same folder with _grey added to the filename.
        Returns None
        """
        img = Image.open(self.folder + self.filename).convert('L')
        img.save(self.grey_path)
        return None

    def clicked(self):
        """ Deals with the events of when an image is clicked.
        Turns the image greyscale and redraws it.
        Input: self
        Output: None
        """

        if self.colored:
            self.image = self.grey_image
            self.colored = False
            # self.update(x=self.x+self.width, y=self.y+self.height, rotation=180)
        else:
            self.image = self.color_image
            self.colored = True
            # self.update(x=self.x-self.width, y=self.y-self.height, rotation=0)
        self.draw()
        return None

    def __str__(self):
        return self.name

    def get_group(self):
        return self.group_name

    def get_folder(self):
        return self.folder

    def get_filename(self):
        return self.filename

    def get_image(self):
        return self.image

    def get_name(self):
        return self.name
    
    def size(self):
        return self.width, self.height


path = "Groups/"
possible_groups = listdir(path)
if "Groups-folder-explained" in possible_groups:
    possible_groups.remove("Groups-folder-explained")
# Set up MX and TXT data and shuffle
print("Hi, welcome to Wie is Het? Please enter the groups you would like to use for this game below, one by one. ")
print("So, if you want to play a game using both Monsta X and GOT7, first type Monsta X, then press enter, then type GOT7, then press enter.")
print("Please use the same capitalisation structure as the folders in your system.")
print("Once you have added all the groups you want to add, type done")
print("The possible groups are:")
print(", ".join(possible_groups))
group_input = input("What group would you like to add first?\n")
groups = []
pos_groups_lower = [group.lower() for group in possible_groups]
while group_input.lower() != "done" or not possible_groups:
    if not os.path.exists(path + group_input + "/"):
        print("\nSorry, I don't know the group " + group_input + ".")
        group_input = input("Please try again.\n")
    else:
        groups.append(group_input)
        i = pos_groups_lower.index(group_input.lower())
        possible_groups.pop(i)
        pos_groups_lower.pop(i)
        print(possible_groups)
        if len(groups) == 1:
            prints = group_input
        else: 
            prints = ', '.join(groups)
        print("\nYour currently selected groups are: " + prints)
        print("The possible groups left to choose are:")
        print(", ".join(possible_groups))
        group_input = input("What other group would you like to add? When you're done, please type done.\n")

photos = []
batch = pyglet.graphics.Batch()
for group_name in groups:
    group = Group(path, group_name, batch)
    photos += group.get_members()
random.shuffle(photos)

your_card = random.choice(photos)
text_batch = pyglet.graphics.Batch()
text_sprite = [pyglet.text.Label("Your card is:   ",
                          font_name='Times New Roman',
                          font_size=20,
                          x=10, y=40, batch=text_batch),
                pyglet.text.Label(your_card.name, font_name='Times New Roman',
                          font_size=20,
                          x=10, y=10, batch=text_batch)]
                        #   anchor_x='center', anchor_y='center')
text_sprite_width = max(text_sprite[0].content_width, text_sprite[1].content_width)

scale = 0.5
imx, imy = photos[0].size()
imx *= scale
imy *= scale
imborder = 10
bottom_border = 20


# Create display
display = pyglet.canvas.get_display()
screens = display.get_screens()
window = pyglet.window.Window(fullscreen=True,style='dialog', caption="Wie Is Het? K-Pop Edition")
# window = pyglet.window.Window(style='dialog', caption="Wie Is Het? K-Pop Edition")
window.set_minimum_size(320, 200)
window_width = 1280
# window.set_size(window_width, 720)

# Calculate how many photos fit in one row
windowx, windowy = window.get_size()
# num_photos = len(photos)
# fit_on_x = floor((windowsize[0] - 2 * imborder) / (imx + imborder))

# Caclulate location for each sprite and save these values
sprite_locs = []
grey_sprites = []
x = imborder
y = imborder

your_card_im = pyglet.sprite.Sprite(img=your_card, batch=batch, x=x+text_sprite_width, y=y)
your_card_im.update(scale=scale)
y += imy + bottom_border

for i, photo in enumerate(photos):
    imx, imy = photo.size()
    if x + imx*scale + imborder > windowx:
        x = imborder
        y += imy*scale + imborder
    photo.update(x=x, y=y, scale=scale)
    sprite_locs.append((x, y))
    x += imx*scale + imborder
    if x > windowx:
        x = imborder
        y += imy*scale + imborder
    # if (i + 1) % fit_on_x == 0:
        
    # else:
    #     x += imx*scale + imborder

# Set window height so that all images fit 
# window_height = y + imy + imborder
# window.set_size(window_width, int(window_height))

# Draw window
@window.event
def on_draw():
    window.clear()
    batch.draw()
    text_batch.draw()
    # text_sprite.draw()
    your_card_im.draw()

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
        i = locate_picture(x, y)
        if i >= 0:
            photos[i].clicked()

def locate_picture(mouse_x, mouse_y):
    """
    Checks which image was clicked in the window. 

    Input: 
    mouse_x (int): x coordinate of the mouse when the mouse press event happened
    mouse_y (int): y coordinate of the mouse when the mouse press event happened

    Output:
    If a person was clicked:
    i (int): the index of the member in sprites and photos

    If a person was not clicked: -1
    """
    for min_x, min_y in sprite_locs:
        max_x = min_x + imx
        max_y = min_y + imy
        if min_x < mouse_x and max_x > mouse_x and min_y < mouse_y and max_y > mouse_y:
            i = sprite_locs.index((min_x, min_y))
            return i
    return -1

pyglet.app.run() 
