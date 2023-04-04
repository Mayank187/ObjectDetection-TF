import os

labels = ['thumbs up','thumbs down']

for label in labels:
    # Set the path to the directory where your images are located
    images_directory = 'images/'+label

    # Launch LabelImg and select the directory where your images are located
    os.system(f"labelImg {images_directory}")