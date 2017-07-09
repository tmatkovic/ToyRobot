
class ToyRobot:
    _orientation = ["EAST", "WEST", "SOUTH", "NORTH"]

    def __init__(self):
        self._width = 5
        self._height = 5
        self._facing = None
        self._xPosition = None
        self._yPosition = None
        self._placed = False


    def place(self, x, y, facing):
        # first check are coordinates valid
        if self._are_coordinates_inside_board(x, y) is False:
            return

        # then check orientation validity
        if facing not in self._orientation:
            print("Unknown orientation, robot not placed")
            return

        # if everything OK, consider robot placed
        self._placed = True

        self._xPosition = x
        self._yPosition = y
        self._facing = facing

        print("Robot placed")


    def move(self):
        if self._placed is False:
            print("Robot not placed yet...")
            return

        if self._facing == "EAST":
            x, y = self._xPosition + 1, self._yPosition
        elif self._facing == "WEST":
            x, y = self._xPosition - 1, self._yPosition
        elif self._facing == "SOUTH":
            x, y = self._xPosition, self._yPosition - 1
        elif self._facing == "NORTH":
            x, y = self._xPosition, self._yPosition + 1
        else:
            print("Unknown orientation, robot not moved")
            return

        # not when we have new position, see if it is inside the board
        if self._are_coordinates_inside_board(x, y) is True:
            # move the robot
            self._xPosition = x
            self._yPosition = y
            print("Moved")


    def left(self):
        if self._placed is False:
            print("Robot not placed yet...")
            return

        leftside = \
            [
                # current facing, left of current facing
                ("EAST", "NORTH"),
                ("WEST", "SOUTH"),
                ("SOUTH", "EAST"),
                ("NORTH", "WEST"),
            ]

        # (facing, left)
        for (f, l) in leftside:
            if self._facing == f:
                self._facing = l
                print("Turned left")
                break


    def right(self):
        if self._placed is False:
            print("Robot not placed yet...")
            return

        rightside = \
            [
                # current facing, right of current facing
                ("EAST", "SOUTH"),
                ("WEST", "NORTH"),
                ("SOUTH", "WEST"),
                ("NORTH", "EAST"),
            ]

        # (facing, right)
        for (f, r) in rightside:
            if self._facing == f:
                self._facing = r
                print("Turned right")
                break


    def report(self):
        if self._placed is False:
            print("Robot not placed yet...")
            return

        # info = "X: {0}, Y: {1}, FACING: {2}".format(self._xPosition, self._yPosition, self._facing)
        info = "({0}, {1}, {2})".format(self._xPosition, self._yPosition, self._facing)
        print(info)
        return info

    def _are_coordinates_inside_board(self, x, y):
        if x < 0 or x >= self._width:
            print("X position not valid")
            return False

        if y < 0 or y >= self._height:
            print("Y position not valid")
            return False

        return True

