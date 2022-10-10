# Make a gif from all images in the plots folder
# Each image is of the form: f"{t:03d}.png"

import imageio
import os

images = []
for file_name in os.listdir("plots"):
    if file_name.endswith(".png"):
        file_path = os.path.join("plots", file_name)
        images.append(imageio.imread(file_path))


imageio.mimsave("rock_paper_scissors_.gif", images, fps=7)
