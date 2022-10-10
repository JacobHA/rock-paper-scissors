from walkers import Walker
import matplotlib.pyplot as plt 
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from io import BytesIO

MAX_X = 50
MAX_Y = 50

# Create a list of walkers
walkers = []
for i in range(5):
    walkers.append(Walker(name="Rock", max_x=MAX_X, max_y=MAX_Y))
    walkers.append(Walker(name="Paper", max_x=MAX_X, max_y=MAX_Y))
    walkers.append(Walker(name="Scissors", max_x=MAX_X, max_y=MAX_Y))


images = {"rock": 0, "paper": 1, "scissors": 2}
imagepics = [plt.imread(f'player_images/{name}.png', format="png") for name in images.keys()]

def savefig(*args, **kwargs):
    plt.savefig(*args, **kwargs)
    plt.close(plt.gcf())

# Move the walkers
for t in range(500):
    # Plot the walkers:      
   
    plt.figure()#figsize=(10, 10))
    plt.xlim(0, MAX_X)
    plt.ylim(0, MAX_Y)

    print(f'Timestep {t}')
    for walker in walkers:
        walker.move()

        for other_walker in walkers:
            if other_walker.player.name != walker.player.name:
                walker.interact(other_walker)

        # Plot the walker
        plt.imshow(imagepics[images[walker.player.name.lower()]], extent=(walker.x-3, walker.x+3, walker.y-3, walker.y+3))

    savefig(f"plots/{t:03d}.png")

