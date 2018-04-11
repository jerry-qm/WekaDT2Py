# WekaDT2Py
Convert Weka (version 3.8.2) Decision Tree to python function for used in ArcGIS field calculator

## Requirement:
Python 2.7

## Syntax:

    Weka2Py.py -b <DecisionTreeFile> -o <OutputFile>

## Options:

- -b
--buffer
Mandatory, Text file containing **only** the Decision tree result from Weka, see sample/ResultBuffer-cleaned

- -o
--output
Mandatory, Full path filename text file which will store the conversion result

## Example:
### Input:

    i398_201_4 <= 971
    |   i398_201_4 <= 687: Water (723.0/2.0)
    |   i398_201_4 > 687
    |   |   i398_201_1 <= 1147: Land (11.0)
    |   |   i398_201_1 > 1147: Water (21.0/1.0)
    i398_201_4 > 971
    |   i398_201_3 <= 1150: Land (10477.0/2.0)
    |   i398_201_3 > 1150
    |   |   i398_201_7 <= 29622
    |   |   |   i398_201_7 <= 29386
    |   |   |   |   i398_201_7 <= 28823: Water (2.0)
    |   |   |   |   i398_201_7 > 28823: Land (30.0)
    |   |   |   i398_201_7 > 29386: Water (22.0/8.0)
    |   |   i398_201_7 > 29622: Land (42.0)

 ### Command:
 #### Windows: 
    python.exe Weka2Py.py -b "/dirname/wekadt.txt" -o "/dirname/wekadt-output.txt"
####  Linux:
    Weka2Py.py -b "/dirname/wekadt.txt" -o "/dirname/wekadt-output.txt"

### Output

    def Classify(i398_201_7,i398_201_4,i398_201_3,i398_201_1):
        if i398_201_4 <= 971:
            if i398_201_4 <= 687:
                return "Water"
            else:
                if i398_201_1 <= 1147:
                    return "Land"
                else:
                    return "Water"
        else:
            if i398_201_3 <= 1150:
                return "Land"
            else:
                if i398_201_7 <= 29622:
                    if i398_201_7 <= 29386:
                        if i398_201_7 <= 28823:
                            return "Water"
                        else:
                            return "Land"
                    else:
                        return "Water"
                else:
                    return "Land"
