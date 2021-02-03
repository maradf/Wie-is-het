import pyglet
from pyglet.window import key
from pyglet.window import mouse
from os import listdir

class Group():
    # Variable depth is for if the folder is embedded in a number of folders. 
    # Depth is the number of folders it is embedded. Standard 0.
    def __init__(self, path, depth=1):
        self.path = path
        self.name = path.split("/")[depth]
        self.members = []
        self.memberFiles = listdir(path)

    def __str__(self):
        return self.name
    
    def add_member(self, member):
        self.members.append(member)
    
    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
    
    def get_members(self):
        return self.members

    def print_members(self):
        return [member.name for member in self.members]


    def get_member_files(self):
        return self.memberFiles

    def get_path(self):
        return self.path

class Member():
    def __init__(self, group, folder, filename):
        self.group = group
        self.folder = folder
        self.filename = filename
        self.image = pyglet.resource.image(folder + filename)
        self.name = filename.split(".")[0]

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
mxpath = path + "Monsta X/"
mx = Group(mxpath)

txtpath = path + "TXT/"
txt = Group(txtpath)

# print(mx.path)
print(mx)
for memberfile in mx.memberFiles:
    mx.add_member(Member(mx.name, mxpath, memberfile))

print(mx.print_members())

print(txt)
# print(txt.memberFiles)
for memberfile in txt.memberFiles:
    txt.add_member(Member(txt.name, txtpath, memberfile))

print(txt.print_members())

"""
display = pyglet.canvas.get_display()
display.get_screens()
screens = display.get_screens()
window = pyglet.window.Window(resizable=True, style='dialog', caption="Wie Is Het? K-Pop Edition")
window.set_minimum_size(320, 200)
window.set_size(1280, 720)

image = pyglet.resource.image('jungkook.jpg')
image2 = pyglet.resource.image('scoups.jpg')
@window.event
def on_draw():
    window.clear()
    image.blit(10, 100)
    image2.blit(100, 100)

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

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')

pyglet.app.run() """ 