# Press the green button in the gutter to run the script.
import turtle
import random

wn = turtle.Screen()
triangle = turtle.Turtle()
triangle.speed(0)

def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return (s * pt1[0] + t * pt2[0] + u * pt3[0],
            s * pt1[1] + t * pt2[1] + u * pt3[1])


def midpoint_formula(x1, y1, x2, y2):
    return (x1 + x2) // 2, (y1 + y2) // 2


def sierpinksi_triangle(dots, point_list, last_point):
    current_point = last_point
    for i in range(dots):
        chosen_point = random.choice(point_list)
        midpoint = midpoint_formula(chosen_point[0], chosen_point[1], current_point[0], current_point[1])
        triangle.goto(midpoint[0], midpoint[1])
        triangle.dot()
        current_point = midpoint


if __name__ == '__main__':
    base_points = []
    x, y = midpoint_formula(2, 2, 4, 4)
    triangle.up()
    triangle.goto(0, 300)
    triangle.right(60)
    for i in range(3):
        triangle.dot()
        triangle.forward(600)
        triangle.right(120)
        base_points.append([int(triangle.xcor()), int(triangle.ycor())])
    last_point = point_on_triangle(base_points[0], base_points[1], base_points[2])
    triangle.goto(last_point[0], last_point[1])
    triangle.dot()
    sierpinksi_triangle(25000, base_points, last_point)

wn.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
