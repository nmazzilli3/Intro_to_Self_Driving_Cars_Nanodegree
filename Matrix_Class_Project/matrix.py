import math
from math import sqrt
import numbers

def zeroes(height, width):
		"""
		Creates a matrix of zeroes.
		"""
		g = [[0.0 for _ in range(width)] for __ in range(height)]
		return Matrix(g)

def identity(n):
		"""
		Creates a n x n identity matrix.
		"""
		I = zeroes(n, n)
		for i in range(n):
			I.g[i][i] = 1.0
		return I

def dot_product(vectorA, vectorB):
	if len(vectorA) != len(vectorB):
		print('Error with Vector Sizes!') 
	result = 0
	
	for i in range(len(vectorA)):
		result += vectorA[i] * vectorB[i]
		
	return result
	
class Matrix(object):

	# Constructor
	def __init__(self, grid):
		self.g = grid
		self.row_len = len(grid)
		self.col_len = len(grid[0])

	#
	# Primary matrix math methods
	#############################
 
	def determinant(self):
		"""
		Calculates the determinant of a 1x1 or 2x2 matrix.
		"""
		if not self.is_square():
			raise(ValueError, "Cannot calculate determinant of non-square matrix.")
		if self.row_len > 2:
			raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
		
		# TODO - your code here
		"""
		A = [[a,b],
			 [c,d]] 
			 then det(A) = ad - bc
		"""
		if self.row_len == 1 and self.col_len == 1:
			determinate = 1/self.g[0][0]
			
		else: 
			a = self.g[0][0]
			b = self.g[0][1]
			c = self.g[1][0]
			d = self.g[1][1]
			determinate = 1 / (a * d - b * c)
		
		return determinate
	
	def dotproduct(self,s_idx,other,o_idx):
		vectorA = self.get_row(s_idx)
		vectorB = other.get_column(o_idx)
		if len(vectorA) != len(vectorB):
			print('Error with Vector Sizes!') 
		
		result = 0
	
		for i in range(len(vectorA)):
			result += vectorA[i] * vectorB[i]

		return result
			

	def trace(self):
		"""
		Calculates the trace of a matrix (sum of diagonal entries).
		"""
		if not self.is_square():
			raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
		sum_diagnols = 0 
		# TODO - your code here
		for row_idx in range(self.row_len):
			for col_idx in range(self.col_len):
				if row_idx == col_idx: 
					sum_diagnols += self.g[row_idx][col_idx]
		return sum_diagnols
				

	def inverse(self):
		"""
		Calculates the inverse of a 1x1 or 2x2 Matrix.
		"""
		if not self.is_square():
			raise(ValueError, "Non-square Matrix does not have an inverse.")
		if self.row_len > 2:
			raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
	
		# TODO - your code here
		inverse = [] 
		if self.row_len == 1: 
			inverse.append([1 / self.g[0][0]])
		elif self.row_len == 2: 
			# If the matrix is 2x2, check that the matrix is invertible
			if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
				raise ValueError('The matrix is not invertible.')
			else:
				det = self.determinant() 
				a = self.g[0][0]
				b = self.g[0][1]
				c = self.g[1][0]
				d = self.g[1][1]
				inverse = [[d, -b],[-c, a]]

				for i in range(len(inverse)):
					for j in range(len(inverse[0])):
						inverse[i][j] = det * inverse[i][j]
				
		return Matrix(inverse)
			

	def T(self):
		"""
		Returns a transposed copy of this Matrix.
		"""
		# TODO - your code ere
		matrix_transpose = []
		# Loop through columns on outside loop
		for c in range(self.col_len):
			new_row = []
			# Loop through columns on inner loop
			for r in range(self.row_len):
				# Column values will be filled by what were each row before
				new_row.append(self.g[r][c])
			matrix_transpose.append(new_row)

		return Matrix(matrix_transpose)

	def is_square(self):
		return self.row_len == self.col_len

	def get_column(self, column_number):
		column = []
		for row_idx in range(self.row_len):
			column.append(self.g[row_idx][column_number])
		return column
	
	def get_row(self, row):
		return self.g[row]
	#
	# Begin Operator Overloading
	############################
	def __getitem__(self,idx):
		"""
		Defines the behavior of using square brackets [] on instances
		of this class.

		Example:

		> my_matrix = Matrix([ [1, 2], [3, 4] ])
		> my_matrix[0]
		  [1, 2]

		> my_matrix[0][0]
		  1
		"""
		return self.g[idx]

	def __repr__(self):
		"""
		Defines the behavior of calling print on an instance of this class.
		"""
		s = ""
		for row in self.g:
			s += " ".join(["{} ".format(x) for x in row])
			s += "\n"
		return s

	def __add__(self,other):
		"""
		Defines the behavior of the + operator
		"""
		if self.row_len != other.row_len or self.col_len != other.col_len:
			raise(ValueError, "Matrices can only be added if the dimensions are the same") 
		#	
		# TODO - your code here
		#
		row = [] 
		matrix_add = []
		for row_idx in range(self.row_len):
			row = []
			for col_idx in range(self.col_len): 
				row.append(self.g[row_idx][col_idx]+other.g[row_idx][col_idx])
			matrix_add.append(row)
		return Matrix(matrix_add)				

	def __neg__(self):
		"""
		Defines the behavior of - operator (NOT subtraction)

		Example:

		> my_matrix = Matrix([ [1, 2], [3, 4] ])
		> negative	= -my_matrix
		> print(negative)
		  -1.0	-2.0
		  -3.0	-4.0
		"""
		#	
		# TODO - your code here
		#
		row = [] 
		matrix_neg = []
		for row_idx in range(self.row_len):
			row = []
			for col_idx in range(self.col_len): 
				row.append(-1*self.g[row_idx][col_idx])
			matrix_neg.append(row)
		return Matrix(matrix_neg)
	
	def __sub__(self, other):
		"""
		Defines the behavior of the - operator
		"""
		if self.row_len != other.row_len or self.col_len != other.col_len:
			raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
		#	
		# TODO - your code here
		#
		row = [] 
		matrix_sub = []
		for row_idx in range(self.row_len):
			row = []
			for col_idx in range(self.col_len): 
				row.append(self.g[row_idx][col_idx]-other.g[row_idx][col_idx])
			matrix_sub.append(row)
		return Matrix(matrix_sub)
			
	def __mul__(self, other):
		"""
		Defines the behavior of * operator (matrix multiplication)
		"""
		#	
		# TODO - your code here
		#
		if len(self.g[0]) != len(other.g):
			raise(ValueError, "Matrices can only be multiplied if the dimensions of 1st columns = dimensions of 2nd rows")
			
		product = []
		m_rows = self.row_len
		p_columns = other.col_len

		# Use a nested for loop to iterate through the rows
		# of matrix A and the rows of the tranpose of matrix B
		for row_idx in range(m_rows):
			new_row = []	
			for col_idx in range(p_columns):
				# Calculate the dot product between each row of matrix A
				# with each row in the transpose of matrix B 
				new_row.append(self.dotproduct(row_idx, other,col_idx))
			# Store the results in the product variable
			product.append(new_row)

		return Matrix(product)

	def __rmul__(self, other):
		"""
		Called when the thing on the left of the * is not a matrix.

		Example:

		> identity = Matrix([ [1,0], [0,1] ])
		> doubled  = 2 * identity
		> print(doubled)
		  2.0  0.0
		  0.0  2.0
		"""
		if isinstance(other, numbers.Number):
			pass
			#	
			# TODO - your code here
			#
		row = [] 
		matrix_mult = []
		for row_idx in range(self.row_len):
			row = []
			for col_idx in range(self.col_len): 
				row.append(other*self.g[row_idx][col_idx])
			matrix_mult.append(row)
		return Matrix(matrix_mult)
			