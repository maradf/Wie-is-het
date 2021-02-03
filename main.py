import pyglet
from pyglet.window import key
from pyglet.window import mouse
from os import listdir

class Group():
    # Variable depth is for if the folder is embedded in a number of folders. 
    # Depth is the number of folders it is embedded. Standard 0.
    def __init__(self, path, depth=0):
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

path = "Monsta X/"
mx = Group(path)
print(mx.path)
print(mx)
for memberfile in mx.memberFiles:
    mx.add_member(Member(mx.name, path, memberfile))

print(mx.print_members())
