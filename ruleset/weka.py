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
from ruleset.classes import Rule, Assignment
import re

def GenDTList(buff):
    content = ReadBuff(buff)
    DTList = CleanDT(content)
    return DTList

def ReadBuffer(buff):
    with buff as buffFile:
        content = buffFile.readlines()
        content = [x.strip() for x in content];
    return content

def CleanDT(buff):
    decisionTree = []
    isDT = False

    p = re.compile('\(.*\)$')
    for idx, line in enumerate(buff):
        buff[idx] = p.sub('', line.replace(' ', ''))

    return buff

def GenStatement(buf, lineNo=0):
    conditionString = ''
    thenString = ''
    elseString = ''

    p = re.compile('^(?P<depth>\|*)(?P<leftOperand>[\w\-]+)(?P<operator>[<>=]+)(?P<rightOperand>[\d\.\-]+)(?P<hasColon>\:?)(?P<trueBlock>[\w\-]+)?$')
    match = p.match(buf[lineNo])

    if match:
        matchTuple = match.groupdict()
        depth = matchTuple['depth'].count('|')

        objRule = Rule(matchTuple['leftOperand'], matchTuple['operator'], matchTuple['rightOperand'], lineNo, depth)

        if matchTuple['hasColon'] == ':':
            objRule.trueBlock = Assignment(matchTuple['trueBlock'], depth)

    return objRule
