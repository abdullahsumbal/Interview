## Documentation for Class Point

class Point(builtins.object)
 |  A class used to represent a Point
 |
 |  ...
 |
 |  Attributes
 |  ----------
 |  x : float
 |      X Coordiante
 |  x : float
 |      Y Corrdiante
 |
 |  Methods
 |  -------
 |  __str__()
 |      For pretty print
 |
 |  Methods defined here:
 |
 |  __init__(self, x=0.0, y=0.0)
 |      Parameters
 |      ----------
 |      x: Float
 |          X Coordinate
 |      y: Float
 |          Y Coordinate
 |
 |  __str__(self)
 |      Pretty Print
 |
 |
 |      Returns
 |      -------
 |      point_str: str
 |          string to represent points
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)



## Documentation for Line Class

class Line(builtins.object)
 |  A class used to represent a Line
 |
 |  Attributes
 |  ----------
 |  p1 : Point
 |      first point
 |  p2 : Point
 |      second point
 |
 |  Methods
 |  -------
 |  slope()
 |      Return the Gradient of the slope
 |
 |  Methods defined here:
 |
 |  __init__(self, p1, p2)
 |      Parameters
 |      ----------
 |      p1: Point
 |          Point Object
 |      p2: Point
 |          Point Object
 |
 |  overlap(self, line)
 |      Check if the line segment overlap
 |
 |      Parameters
 |      ----------
 |      line : Line
 |          Line object
 |
 |      Returns
 |      -------
 |      isOverlapping : Boolean
 |          True/False if the line segments are overlap
 |
 |  parallel(self, line)
 |      Check if the line segment are parallel
 |
 |      Parameters
 |      ----------
 |      line : Line
 |          Line object
 |
 |      Returns
 |      -------
 |      isPrallel : Boolean
 |          True/False if the line segments are parallel
 |
 |  slope(self)
 |      Return the Gradient of the slope
 |
 |      Parameters
 |      ----------
 |
 |      Returns
 |      -------
 |      Gradient: float
 |          Slope of the line
 |
 |      Raises
 |      ------
 |      NotImplementedError
 |          If change in x is zero, division by zero will happen. Currently,
 |          does not support divison by zero.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
