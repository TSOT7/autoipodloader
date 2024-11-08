# autoipodloader

### What it do???
Automates the process of uploading and managing files to my iPod 5th generation with Rockbox installed

Rockbox treats the ipod like an external drive, making the use of iTunes completely uneccesarily

This script takes a path and creates a directory on the Music folder based off of the artist name and project name 

It then uses Image from the Pillow Library to disable progressive JPEG because Rockbox does not support progressive images

Finally it copies the files from the path to its appropriate directory

