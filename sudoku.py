import numpy as np
from math import sqrt

class Sudoku(object):
    def __init__(self, data):
      try:
        self.matrix = np.array(data)
      except:
        self.matrix = np.array([])

    def is_valid(self):
      shape = self.matrix.shape
      if (self.matrix.size  == 0 or len(shape) != 2 or shape[0] != shape[1] or
         not np.issubdtype(self.matrix.dtype, np.integer)):
        return False

      number_range = [c for c in range(1, shape[1]+1)]
      for row, elements in enumerate(self.matrix):
        for col, number in enumerate(elements):
          if ((elements==number).sum() != 1 or
             (self.matrix[:,col]==number).sum() != 1 or
             number not in number_range):
            return False

      return self.valid_squares()

    def get_quadrants(self):
      shape = self.matrix.shape
      N = shape[0]

      divisions = int(N ** 0.5)  
      if N % divisions != 0:
          return None

      quadrant_size = N // divisions
      quadrants = []

      for i in range(divisions):
          for j in range(divisions):
              quadrant = []
              for row in range(i * quadrant_size, (i + 1) * quadrant_size):
                  for col in range(j * quadrant_size, (j + 1) * quadrant_size):
                      quadrant.append((row, col))
              quadrants.append(quadrant)

      return quadrants

    def valid_squares(self) -> bool:
      quadrants = self.get_quadrants()
      if not quadrants:
        return False
        
      shape = self.matrix.shape
      number_range = [c for c in range(1, shape[0]+1)]

      for quadrant in quadrants:
        elements = []

        for position in quadrant:
          elements.append(self.matrix[position[0], position[1]])

        invalid_numbers = [number for number in elements if number not in number_range]

        if len(invalid_numbers) > 0 or len(elements) != len(set(elements)):
          return False

      return True

