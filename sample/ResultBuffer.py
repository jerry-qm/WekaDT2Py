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
