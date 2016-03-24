#!/usr/bin/python3

if __name__ == "__main__":
    y_points = []
    x_points = list(range(0,1000))

    for x_point in x_points:
        new_point = ( (4*(x_point**2)) + (-7 * x_point) + 42)
        y_points.append(new_point)

    print(y_points)
    print(x_points)

    data = open("plotpoints.txt", 'w')
    for i in range(0, len(x_points)):
        line = (str(x_points[i]) + "," + str(y_points[i]) + "\n")
        data.write(line)
