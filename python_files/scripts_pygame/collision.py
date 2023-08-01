import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))

rectangle = {
    "x": 200,
    "y": 200,
    "width": 100,
    "height": 200,
}

circle = {
    "x": 300,
    "y": 300,
    "r": 50
}

line = [
    {"x": 100, "y": 100},
    {"x": 200, "y": 100},
]

point = {
    "x": 100,
    "y": 100,
}

polygon = [
    {"x": 100, "y": 100},
    {"x": 200, "y": 100},
    {"x": 200, "y": 300},
    {"x": 100, "y": 200}
]


def in_interval(value, interval):
    interval[0], interval[1] = min(interval), max(interval)
    return interval[0] <= value <= interval[1]


def collision_line_point(line, point):
    x1, y1 = line[0]["x"], line[0]["y"]
    x2, y2 = line[1]["x"], line[1]["y"]
    x, y = point["x"], point["y"]
    if x1 == x2:
        return in_interval(y, [y1, y2]) and x == x1
    elif y1 == y2:
        return in_interval(x, [x1, x2]) and y == y1
    else:
        return in_interval(x, [x1, x2]) and y == y1 + (x - x1) * (y2 - y1) / (x2 - x1)


def collision_line_line(line1, line2):
    x11, y11 = line1[0]["x"], line1[0]["y"]
    x12, y12 = line1[1]["x"], line1[1]["y"]
    x21, y21 = line2[0]["x"], line2[0]["y"]
    x22, y22 = line2[1]["x"], line2[1]["y"]
    if x11 == x12:
        return collision_line_point(line2, {"x": x11, "y": y11})
    elif x21 == x22:
        return collision_line_point(line1, {"x": x21, "y": y21})
    else:
        a1 = (y12 - y11) / (x12 - x11)
        b1 = y11 - a1 * x11
        a2 = (y22 - y21) / (x22 - x21)
        b2 = y21 - a2 * x21
        if a1 == a2:
            return b1 == b2
        else:
            x = (b2 - b1) / (a1 - a2)
            return in_interval(x, [x11, x12]) and in_interval(x, [x21, x22])


def collision_rectangle_point(rectangle, point):
    x, y = point["x"], point["y"]
    return in_interval(x, [rectangle["x"], rectangle["x"] + rectangle["width"]]) and \
        in_interval(y, [rectangle["y"], rectangle["y"] + rectangle["height"]])


def collision_circle_point(circle, point):
    x, y = point["x"], point["y"]
    return (x - circle["x"]) ** 2 + (y - circle["y"]) ** 2 <= circle["r"] ** 2


def get_corners(rectangle):
    return [
        {"x": rectangle["x"], "y": rectangle["y"]},
        {"x": rectangle["x"] + rectangle["width"], "y": rectangle["y"]},
        {"x": rectangle["x"] + rectangle["width"],
            "y": rectangle["y"] + rectangle["height"]},
        {"x": rectangle["x"], "y": rectangle["y"] + rectangle["height"]}
    ]


def collision_rectangle_line(rectangle, line):
    x1, y1 = line[0]["x"], line[0]["y"]
    x2, y2 = line[1]["x"], line[1]["y"]
    if collision_rectangle_point(rectangle, {"x": x1, "y": y1}) or \
            collision_rectangle_point(rectangle, {"x": x2, "y": y2}):
        return True
    collision = False
    for corner in get_corners(rectangle):
        x, y = corner["x"], corner["y"]
        if collision_line_point(line, corner):
            collision = True
            break
    return collision


def collision_rectangle_rectangle(rectangle1, rectangle2):
    corners1 = get_corners(rectangle1)
    corners2 = get_corners(rectangle2)
    for corner in corners1:
        if collision_rectangle_point(rectangle2, corner):
            return True
    for corner in corners2:
        if collision_rectangle_point(rectangle1, corner):
            return True
    return False
