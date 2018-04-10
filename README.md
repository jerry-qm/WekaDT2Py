
# WekaDT2Py
Convert Weka (version 3.8.2) Decision Tree to python if statement


## Syntax:

    Weka2Py.py -b <DTFile> -o <OutputFil> -c <classname>

## Options:

- -b
--buffer
Mandatory, Text file containing **only** the Decision tree result from Weka, see sample/ResultBuffer-cleaned

- -o
--output
Mandatory, Fullpath filename text file which will store the conversion result

- -c
--classField
Mandatory, any alphanumeric string field name that you use in your featur attribute table that containing the class name

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
    python.exe Weka2Py.py -b "/dirname/wekadt.txt" -o "/dirname/wekadt-output.txt" -c "class"
####  Linux:
    Weka2Py.py -b "/dirname/wekadt.txt" -o "/dirname/wekadt-output.txt" -c "class"

### Output

    if i398_201_4 <= 971:
        if i398_201_4 <= 687:
            class = "Water"
        else:
            if i398_201_1 <= 1147:
                class = "Land"
            else:
                class = "Water"
    else:
        if i398_201_3 <= 1150:
            class = "Land"
        else:
            if i398_201_7 <= 29622:
                if i398_201_7 <= 29386:
                    if i398_201_7 <= 28823:
                        class = "Water"
                    else:
                        class = "Land"
                else:
                    class = "Water"
            else:
                class = "Land"