from unittest import TestCase
from toyrobot import ToyRobot


class Test(TestCase):

    def test_placetest(self):
        robot = ToyRobot()

        robot.place(2, 2, "WEST")
        self.assertEqual(robot.report(), "(2, 2, WEST)")

        # more than board bounds
        robot.place(1, 6, "SOUTH")
        self.assertNotEqual(robot.report(), "(1, 6, SOUTH)")

        robot.place(0, 0, "SOUTH")
        self.assertEqual(robot.report(), "(0, 0, SOUTH)")


    def test_movetest(self):
        robot = ToyRobot()

        robot.place(3, 2, "WEST")

        robot.move()
        self.assertEqual(robot.report(), "(2, 2, WEST)")

        robot.move()
        self.assertEqual(robot.report(), "(1, 2, WEST)")

        robot.move()
        self.assertEqual(robot.report(), "(0, 2, WEST)")

        # shouldn't go more in west direction
        robot.move()
        self.assertEqual(robot.report(), "(0, 2, WEST)")


    def test_lefttest(self):
        robot = ToyRobot()

        robot.place(4, 4, "EAST")

        # turn around full circle
        robot.left()
        self.assertEqual(robot.report(), "(4, 4, NORTH)")

        robot.left()
        self.assertEqual(robot.report(), "(4, 4, WEST)")

        robot.left()
        self.assertEqual(robot.report(), "(4, 4, SOUTH)")

        robot.left()
        self.assertEqual(robot.report(), "(4, 4, EAST)")


    def test_righttest(self):
        robot = ToyRobot()

        robot.place(0, 3, "EAST")

        # turn around full circle
        robot.right()
        self.assertEqual(robot.report(), "(0, 3, SOUTH)")

        robot.right()
        self.assertEqual(robot.report(), "(0, 3, WEST)")

        robot.right()
        self.assertEqual(robot.report(), "(0, 3, NORTH)")

        robot.right()
        self.assertEqual(robot.report(), "(0, 3, EAST)")