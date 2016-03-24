#!/usr/bin/python3

import matplotlib.pyplot
import numpy

if __name__ == "__main__":

    x_points = []
    y_points = []

    data = open("plotpoints.txt", 'r')
    data_list = list(data)
    for points in data_list:
        coordinates = points.strip().split(",")
        print(coordinates[0] + " , " + coordinates[1]) 
        x_points.append(coordinates[0])
        y_points.append(coordinates[1])

    matplotlib.pyplot.scatter(x_points, y_points)
    matplotlib.pyplot.show()

