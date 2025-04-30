# module 5 assignment.
class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)


box = Rectangle((0,0), 100, 200)
bomb = Rectangle((100, 80), 5, 10) # In my video game
print("box: ", box)
print("bomb: ", bomb)

def create_rectangle(x, y, width, height):
    """ Create a rectangle instance"""
    posn = (x, y)
    return Rectangle(posn, width, height)


def str_rectangle(rect):
    """ Return a string representation of a rectangle """
    x, y = rect.corner
    return "({0}, {1}, {2}, {3})".format(x, y, rect.width, rect.height)


def shift_rectangle(rect, dx, dy):
    """ Shift rectangle by dx and dy """
    rect.corner = (rect.corner[0] + dx, rect.corner[1] + dy)


def offset_rectangle(rect, dx, dy):
    """ Create rectangle instance and offset rectangle by dx and dy """
    off_pos = (rect.corner[0] + dx, rect.corner[1] + dy)
    return Rectangle(off_pos, rect.width, rect.height)


r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1))
r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1))  # should be same as previous
print(str_rectangle(r2))


