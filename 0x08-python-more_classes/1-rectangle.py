#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
	"""Representation of a rectangle"""
	def __init__(self, width=0, hight=0):
		"""initializes the trangle"""
		self.height = height
		self.width = width

	@property
	def width(self):
		"""getter for private instance attribut width"""
		return self.__width
	
	@width.setter
	def width(self,value):
		"""setter for private instance attribut width"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >=0")
		self.__width = value

	@property 
	def height(self, value):
		"""getter for private instance attribute height"""
		return self.__height
	
	@height.setters
	def height(self, value):
		"""setters for private instanceattribute height"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height musht be >=0")
		self.__height = value
