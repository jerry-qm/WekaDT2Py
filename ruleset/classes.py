## Copyright (C) 2018  Yerry Quarry <jerry.qm@gmail.com>

## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Rule():
	"""docstring for Rule"""
	def __init__(self, leftOperand, operator, rightOperand, lineNo=0, depth=0):
		self.leftOperand = leftOperand
		self.operator = operator
		self.rightOperand = rightOperand
		self.lineNo = lineNo
		self.trueBlock = None
		self.falseBlock = None
		self.depth = depth
		self.parentLine = None

	def leftOperand():
	    doc = "The leftOperand property."
	    def fget(self):
	        return self.__leftOperand
	    def fset(self, value):
	        self.__leftOperand = value
	    def fdel(self):
	        del self.__leftOperand
	    return locals()
	leftOperand = property(**leftOperand())

	def operator():
	    doc = "The operator property."
	    def fget(self):
	        return self.__operator
	    def fset(self, value):
	        self.__operator = value
	    def fdel(self):
	        del self.__operator
	    return locals()
	operator = property(**operator())

	def rightOperand():
	    doc = "The rightOperand property."
	    def fget(self):
	        return self.__rightOperand
	    def fset(self, value):
	        self.__rightOperand = value
	    def fdel(self):
	        del self.__rightOperand
	    return locals()
	rightOperand = property(**rightOperand())

	def trueBlock():
	    doc = "The trueBlock property."
	    def fget(self):
	        return self.__trueBlock
	    def fset(self, value):
	        self.__trueBlock = value
	    def fdel(self):
	        del self.__trueBlock
	    return locals()
	trueBlock = property(**trueBlock())

	def falseBlock():
	    doc = "The falseBlock property."
	    def fget(self):
	        return self.__falseBlock
	    def fset(self, value):
	        self.__falseBlock = value
	    def fdel(self):
	        del self.__falseBlock
	    return locals()
	falseBlock = property(**falseBlock())

	def lineNo():
	    doc = "The lineNo property."
	    def fget(self):
	        return self.__lineNo
	    def fset(self, value):
	        self.__lineNo = value
	    def fdel(self):
	        del self.__lineNo
	    return locals()
	lineNo = property(**lineNo())

	def depth():
	    doc = "The depth property."
	    def fget(self):
	        return self.__depth
	    def fset(self, value):
	        self.__depth = value
	    def fdel(self):
	        del self.__depth
	    return locals()
	depth = property(**depth())

	def parentLine():
	    doc = "The parentLine property."
	    def fget(self):
	        return self.__parentLine
	    def fset(self, value):
	        self.__parentLine = value
	    def fdel(self):
	        del self.__parentLine
	    return locals()
	parentLine = property(**parentLine())

	def __str__(self, is_else=False):
		tab = " "*4

		if is_else:
			str_condition  = "{}else:\n".format(tab*(self.depth+1))
		else:
			str_condition = "{}if !{}! {} {}:\n".format(tab*(self.depth+1), self.leftOperand, self.operator, self.rightOperand)

		str_condition += "{}".format(self.trueBlock.__str__()) if self.trueBlock != None else ""
		str_condition += "{}".format(self.falseBlock.__str__(True)) if self.falseBlock != None else ""
		return str_condition



class Assignment(object):
	"""docstring for Assignment"""
	def __init__(self, value, depth):
		super(Assignment, self).__init__()
		self.assignmentValue = value
		self.depth = depth

	def assignmentValue():
	    doc = "The assignmentValue property."
	    def fget(self):
	        return self.__assignmentValue
	    def fset(self, value):
	        self.__assignmentValue = value
	    def fdel(self):
	        del self.__assignmentValue
	    return locals()
	assignmentValue = property(**assignmentValue())

	def depth():
	    doc = "The depth property."
	    def fget(self):
	        return self.__depth
	    def fset(self, value):
	        self.__depth = value
	    def fdel(self):
	        del self.__depth
	    return locals()
	depth = property(**depth())

	def __str__(self):
		tab = " "*4
		return "{}return \"{}\"\n".format(tab*(self.depth+2), self.assignmentValue)
