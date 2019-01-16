#Question A
#Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
import math

class Point:
    """
        A class used to represent a Point

        ...

        Attributes
        ----------
        x : float
            X Coordiante
        x : float
            Y Corrdiante

        Methods
        -------
        __str__()
            For pretty print
    """
    def __init__(self, x=0.0, y=0.0):
        """
        Parameters
        ----------
        x: Float
            X Coordinate
        y: Float
            Y Coordinate
        """
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """
        Pretty Print


        Returns
        -------
        point_str: str
            string to represent points
        """
        point_str = "(%f,%f)".format(self.x, self.y)
        return point_str


class Line:
    """
    A class used to represent a Line

    Attributes
    ----------
    p1 : Point
        first point
    p2 : Point
        second point

    Methods
    -------
    slope()
        Return the Gradient of the slope
    """
    def __init__(self, p1, p2):
        """
        Parameters
        ----------
        p1: Point
            Point Object
        p2: Point
            Point Object
        """
        self.p1 = p1
        self.p2 = p2

    def slope(self):
        """Return the Gradient of the slope

        Parameters
        ----------

        Returns
        -------
        Gradient: float
            Slope of the line

        Raises
        ------
        NotImplementedError
            If change in x is zero, division by zero will happen. Currently,
            does not support divison by zero.
        """
        dist_y = self.p2.y - self.p1.y
        dist_x = self.p2.x - self.p1.x
        if math.isclose(dist_x, 0.0, rel_tol=1e-5):
            raise NotImplementedError("Can not handle division by zero")
        line_slope = dist_y/dist_x
        return line_slope

    def parallel(self, line):
        """ Check if the line segment are parallel

        Parameters
        ----------
        line : Line
            Line object

        Returns
        -------
        isPrallel : Boolean
            True/False if the line segments are parallel
        """
        line1_slope = self.slope()
        line2_slope = line.slope()
        isParallel = math.isclose(line1_slope, line2_slope, rel_tol=1e-5)
        return isParallel

    def overlap(self, line):
        """ Check if the line segment overlap

        Parameters
        ----------
        line : Line
            Line object

        Returns
        -------
        isOverlapping : Boolean
            True/False if the line segments are overlap
        """

        # If the lines are not parallel they can not overlap
        if not self.parallel(line):
            return False

        # Check if the X coordiante of a line lays between the X Cordiantes of the other line
        minX = min([self.p1.x, self.p2.x])
        maxX = max([self.p1.x, self.p2.x])
        if minX <= line.p1.x <= maxX or minX <= line.p2.x <= maxX:
            return True
        else:
            return False

if __name__ == '__main__':
    p1 = Point(3)
    p2 = Point(1)
    p3 = Point(2)
    p4 = Point(4)
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    if line1.overlap(line2):
        print("Lines overlap")
    else:
        print("Lines does not")
