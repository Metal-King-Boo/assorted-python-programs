# this program displays a simple line graph
import matplotlib.pyplot as pit

def main():
    # create lists with the x and y coordinates of each data points
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # build the line graph
    pit.plot(x_coords, y_coords)

    # add a title
    pit.title('Sample Data')

    # add labels to the axes
    pit.xlabel('This is the X axis')
    pit.ylabel('This is the Y axis')

    # set the axis limits
    pit.xlim(xmin =- 1, xmax = 10)
    pit.ylim(ymin =- 1, ymax = 6)

    # add a grid
    pit.grid(True)

    # display the line graph
    pit.show()

# call the main function
main()