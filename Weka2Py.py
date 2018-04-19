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

#! /usr/bin/python

import os, sys, getopt, re
import argparse
import ruleset.weka

def main(argv):
	os.system('cls')

	parser = argparse.ArgumentParser(description='Translate Weka decision tree to python conditional')
	parser.add_argument(
		'-b',
		'--buffer',
		type=argparse.FileType('r'),
		required=True,
		help='Fullpath filename containing decision tree text',
		dest='bFile')
	parser.add_argument(
		'-o',
		'--output',
		type=argparse.FileType('w'),
		required=True,
		help='Fullpath filename for output',
		dest='oFile')

	args = parser.parse_args()

	print("Read {}...\n".format(args.bFile.name))
	content = ruleset.weka.ReadBuffer(args.bFile)
	decisionTree = ruleset.weka.CleanDT(content)


	print("Translate script...\n")
	objDTs = []
	for idx, line in enumerate(decisionTree):
		objDTs.append(ruleset.weka.GenStatement(decisionTree, idx))

	#Find True condition
	for idx, objDT in enumerate(objDTs):
		if objDT.trueBlock == None:
			objDT.trueBlock = objDTs[idx+1]
			objDTs[idx+1].parentLine = objDT.lineNo

	#Find False condition and collect band name
	band_list = []
	main_operator = objDTs[0].operator
	if main_operator == '<=':
		else_operator = '>'
	elif main_operator == '>=':
		else_operator = '<='
	for idx, objDT in enumerate(objDTs):

		band_list.append(objDT.leftOperand)
		if objDT.falseBlock == None and objDT.operator == main_operator:

			for idxFalse, objFalse in enumerate(objDTs[idx+1:]):
				if (objFalse.leftOperand == objDT.leftOperand) and (objFalse.operator == else_operator) and (objFalse.rightOperand == objDT.rightOperand) and (objFalse.depth == objDT.depth) and (objFalse.parentLine == None):
					objDT.falseBlock = objFalse
					objFalse.parentLine = objDT.lineNo-1
					break

	sorted_operand = list(set(band_list))
	sorted_operand = sorted(sorted_operand)
	for idx, operand in enumerate(sorted_operand):
		sorted_operand[idx] = '!{}!'.format(operand)

	print('Write output to {}\n'.format(args.oFile.name))
	with args.oFile as outputFile:
		outputFile.write("def Classify({}):\n".format(', '.join(sorted_operand)))
		outputFile.write(objDTs[0].__str__())

	print('Done!!\n')

if __name__ == '__main__':
	try:
		arg = sys.argv[1]
	except IndexError:
		print('Weka2Arc -b <fullpath filename of buffer file> -o <fullpath filename to output file>')
		sys.exit(2)

	main(sys.argv[1:])