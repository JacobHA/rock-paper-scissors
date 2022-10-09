from walkers import Walker
import matplotlib.pyplot as plt 
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Create a list of walkers
walkers = []
for i in range(5):
    walkers.append(Walker(name="Rock"))
    walkers.append(Walker(name="Paper"))
    walkers.append(Walker(name="Scissors"))

color = {"Rock": "k", "Paper": "b", "Scissors": "r"}

paths = {"Rock": "rock.jpg", "Paper": "paperimg.PNG", "Scissors": "scissors.jpg"}
zooms = {"Rock": 0.1, "Paper": 0.04, "Scissors": 0.07}
def getImage(name):
    path = paths[name]
    zoom = zooms[name]
    path = 'player_images/' + path
    try:
        return OffsetImage(plt.imread(path, format="jpg"), zoom=zoom)
    except:
        return OffsetImage(plt.imread(path, format="png"), zoom=zoom)



# Move the walkers
for t in range(5):
    # Plot the walkers:      
    fig, ax = plt.subplots()
    # set figure size
    fig.set_size_inches(10, 10)
    # set axis limits
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

 

    for walker in walkers:
        # Remove walker from list if position is None
        # LAZY WAY TO IGNORE WALKERS
        if walker.x is None:
            pass
        else:
            walker.move()

            for other_walker in walkers:
                if other_walker.x is None:
                    pass
                else:
                    if walker != other_walker:
                        walker.interact(other_walker)

 
        # plt.plot(walker.x, walker.y, f'{color[walker.player.name]}o')
        ab = AnnotationBbox(getImage(walker.player.name), (walker.x, walker.y), frameon=False)
        ax.add_artist(ab)
    # remove axes
    ax.axis('off')
    # save figure
    fig.savefig(f"plots/{t:03d}.png")

    # plt.savefig(f"plots/{t:03d}.png")

    # Close the figure
    plt.clf()

