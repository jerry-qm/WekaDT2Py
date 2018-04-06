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

def ReadBuffer(bufferFilename):
	with open(bufferFilename, 'rb') as bufferFile:
		content = bufferFile.readlines()
		content = [x.strip() for x in content];
	return content

def CleanDT(buffer):
	decisionTree = []
	isDT = False

	p = re.compile('\(.*\)$')
	for idx, line in enumerate(buffer):
		buffer[idx] = p.sub('', line.replace(' ', ''))

	return buffer

def FindMatch(buf, condition):
	for line in buf:
		if line.find(condition) >= 0:
			return True
	return False

def GenStatement(buf, classFieldname, level=0):
	conditionString = ''
	thenString = ''
	elseString = ''

	p = re.compile('^(?P<depth>\|*)(?P<leftOperand>[\w\-]+)(?P<operator>[<>=]+)(?P<rightOperand>[\d\.\-]+)(?P<thenSymbol>\:?)(?P<ifTrue>[\w\-]+)?$')
	match = p.match(buf[level])

	if match:
		matchTuple = match.groupdict()
		depth = matchTuple['depth'].count('|')
		tab = '    '
		tabs = tab*depth

		if matchTuple['operator'] == '>':
			strMatchCondition = '<='
		elif matchTuple['operator'] == '>=':
			strMatchCondition = '<'
		elif matchTuple['operator'] == '<':
			strMatchCondition = '>='
		elif matchTuple['operator'] == '<=':
			strMatchCondition = '>'

		strCondition = "{}{}{}".format(matchTuple['leftOperand'], strMatchCondition, matchTuple['rightOperand'])

		if level > 0:
			if FindMatch(buf[:level], strCondition):
				conditionString = '{}else:'.format(tabs)
			else:
				conditionString = '{}if {} {} {}:'.format(tabs, matchTuple['leftOperand'], matchTuple['operator'], matchTuple['rightOperand'])
		else: 
			conditionString = '{}if {} {} {}:'.format(tabs, matchTuple['leftOperand'], matchTuple['operator'], matchTuple['rightOperand'])

		if (matchTuple['ifTrue']):
			thenString = '{}{}{} = "{}"\n'.format(tab, tabs, classFieldname, matchTuple['ifTrue'])
	return "{}\n{}".format(conditionString, thenString)

def main(argv):
	os.system('cls')

	try:
		opts, args = getopt.getopt(argv, "hb:o:c:", ['buffer=',  'output=', 'classField='])
	except getopt.GetoptError:
		print 'Weka2Arc -b <fullpath filename of buffer file> -f <fullpath filename to output file>'
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print 'Weka2Arc -b <fullpath filename of buffer file> -f <fullpath filename to output file>'
			sys.exit()
		elif opt in ("-b", "--buffer"):
			bFile = arg
		elif opt in ("-o", "--output"):
			oFile = arg
		elif opt in ("-c", "--classField"):
			classFieldname = arg
		else:
			print 'Weka2Arc -b <fullpath filename of buffer file> -f <fullpath filename to output file>'
			sys.exit()


	content = ReadBuffer(bFile)
	decisionTree = CleanDT(content)

	strDecisionTree = ''
	for idx, line in enumerate(decisionTree):
		strDecisionTree += GenStatement(decisionTree, classFieldname, idx)

	with open(oFile, 'w') as outputFile:
		outputFile.write(strDecisionTree)

if __name__ == '__main__':
	try:
		arg = sys.argv[1]
	except IndexError:
		print 'Weka2Arc -b <fullpath filename of buffer file> -f <fullpath filename to output file>'
		sys.exit(2)

	main(sys.argv[1:])