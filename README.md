# Wie Is Het?

## Running the file

To be able to run the game, some packages are required. These packages are as follows:

- ```pyglet```
- ```os```
- ```random```
- ```math```
- ```pillow```

Install these packages (if you do not have them installed yet) one by one by running the following command in your terminal:

```pip3 install <package name>```

Then, start the game by typing ```python3 main.py``` in the terminal.

## Images requirements

***All*** images should be the same ***height***, and put into subfolders in the ```Groups/``` folder. For each pack of images (a group of people) use one folder. Then you can play while combining different groups as you would like.

The recommended height for images is 320px, that way you will probably not have to change the scale used in the code.

Additionally, when using pictures of a single person (a headshot-esque picture), the size of ```240x320p``` is recommended. This means the images are in 3:4 ratio. If the images are already in a 3:4 ratio, the file ```resize_images.py``` can be used to turn them all into ```240x320p```. 