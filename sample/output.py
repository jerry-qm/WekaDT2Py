def Classify(!Asymmetry!, !Elliptic!, !Mean_B6!, !Mean_LWM!, !Mean_NDBI!, !Mean_NDWI!, !Mean_SLAVI!, !Q25_B3!, !Q25_B5!, !Q25_B6!, !Q25_NDBI!, !Q25_NDWI!, !Q75_B1!, !Q75_B2!, !Q75_B6!, !Q75_NDBI!, !Q75_NDVI!, !Q75_SLAVI!, !Q75_UI!, !Rectangula!, !Shape_idx!, !Width!):
    if !Mean_B6! <= 929.171429:
        if !Q75_NDVI! <= 6464.5:
            if !Q75_B6! <= 771:
                if !Mean_NDWI! <= -1745.026316:
                    if !Q75_B6! <= 48:
                        return "NoData"
                    else:
                        if !Q25_B5! <= 333:
                            if !Q25_NDWI! <= -1953:
                                return "Water"
                            else:
                                if !Q75_SLAVI! <= 13728:
                                    return "Water"
                                else:
                                    return "Vegetation"
                        else:
                            if !Q25_NDWI! <= -2070.5:
                                if !Mean_LWM! <= 14396.592593:
                                    if !Mean_LWM! <= 14341:
                                        return "Water"
                                    else:
                                        return "Vegetation"
                                else:
                                    return "Vegetation"
                            else:
                                if !Q75_UI! <= -6755:
                                    return "Vegetation"
                                else:
                                    if !Shape_idx! <= 2.016737:
                                        if !Q75_SLAVI! <= 11762.5:
                                            if !Q25_B5! <= 491:
                                                return "Water"
                                            else:
                                                if !Q75_NDBI! <= -3064:
                                                    return "Water"
                                                else:
                                                    return "Soil"
                                        else:
                                            return "Water"
                                    else:
                                        if !Mean_SLAVI! <= 10994.444444:
                                            return "Soil"
                                        else:
                                            return "Vegetation"
                else:
                    if !Q75_UI! <= -6756.5:
                        if !Q75_SLAVI! <= 11798.5:
                            return "Water"
                        else:
                            if !Q25_NDWI! <= -2070:
                                if !Mean_LWM! <= 14349:
                                    return "Water"
                                else:
                                    return "Vegetation"
                            else:
                                return "Vegetation"
                    else:
                        if !Q25_B5! <= 490.5:
                            if !Shape_idx! <= 2.012046:
                                if !Mean_LWM! <= 14342.9:
                                    return "Water"
                                else:
                                    if !Q25_B5! <= 334.5:
                                        return "Water"
                                    else:
                                        if !Q25_NDWI! <= -2058:
                                            return "Vegetation"
                                        else:
                                            return "Water"
                            else:
                                if !Q75_SLAVI! <= 11794.5:
                                    return "Water"
                                else:
                                    if !Q25_NDWI! <= -2067.5:
                                        if !Mean_LWM! <= 14348:
                                            return "Water"
                                        else:
                                            return "Vegetation"
                                    else:
                                        return "Vegetation"
                        else:
                            if !Mean_LWM! <= 14338.666667:
                                if !Mean_NDBI! <= -3059.988636:
                                    if !Shape_idx! <= 2.010283:
                                        return "Water"
                                    else:
                                        if !Q75_SLAVI! <= 11799.5:
                                            return "Water"
                                        else:
                                            if !Q25_NDWI! <= -2069.5:
                                                return "Water"
                                            else:
                                                return "Vegetation"
                                else:
                                    if !Q25_NDWI! <= 112:
                                        if !Q25_NDWI! <= -2070.5:
                                            return "Water"
                                        else:
                                            if !Q75_SLAVI! <= 11800:
                                                return "Soil"
                                            else:
                                                if !Shape_idx! <= 2.032932:
                                                    return "Water"
                                                else:
                                                    return "Vegetation"
                                    else:
                                        return "Water"
                            else:
                                if !Q25_NDWI! <= -2070:
                                    return "Vegetation"
                                else:
                                    if !Q75_SLAVI! <= 11769.5:
                                        return "Soil"
                                    else:
                                        return "Water"
            else:
                if !Q25_NDWI! <= -2069:
                    return "Soil"
                else:
                    if !Q25_NDWI! <= 116:
                        if !Mean_NDBI! <= -3062.7:
                            if !Shape_idx! <= 2.063396:
                                return "Water"
                            else:
                                if !Elliptic! <= 0.155556:
                                    return "Water"
                                else:
                                    return "Vegetation"
                        else:
                            if !Q25_B5! <= 489.5:
                                return "Water"
                            else:
                                if !Q75_SLAVI! <= 11775.5:
                                    return "Soil"
                                else:
                                    if !Width! <= 7.307254:
                                        return "Water"
                                    else:
                                        return "Vegetation"
                    else:
                        return "Water"
        else:
            if !Q25_NDWI! <= -2872:
                if !Q25_B6! <= 47:
                    return "NoData"
                else:
                    return "Vegetation"
            else:
                if !Q75_B2! <= 315:
                    if !Q25_NDWI! <= -2064.5:
                        if !Q75_B2! <= 161:
                            if !Q25_B3! <= 11:
                                return "NoData"
                            else:
                                return "Water"
                        else:
                            return "Water"
                    else:
                        if !Q75_UI! <= -6776.5:
                            if !Q75_B6! <= 65.5:
                                if !Q75_B1! <= -124:
                                    return "Water"
                                else:
                                    return "Vegetation"
                            else:
                                return "Vegetation"
                        else:
                            if !Shape_idx! <= 1.993782:
                                return "Water"
                            else:
                                return "Vegetation"
                else:
                    if !Q75_UI! <= -6756.5:
                        if !Q75_SLAVI! <= 15022:
                            if !Q75_SLAVI! <= 11098.5:
                                return "Water"
                            else:
                                return "Vegetation"
                        else:
                            return "Vegetation"
                    else:
                        if !Q25_NDWI! <= -2070.5:
                            return "Vegetation"
                        else:
                            if !Shape_idx! <= 2.008316:
                                if !Q75_SLAVI! <= 12600.5:
                                    if !Q25_B5! <= 514:
                                        return "Water"
                                    else:
                                        if !Asymmetry! <= 0.656981:
                                            return "Soil"
                                        else:
                                            return "Water"
                                else:
                                    return "Water"
                            else:
                                return "Vegetation"
    else:
        if !Rectangula! <= 0.89773:
            if !Q25_NDWI! <= -2070.5:
                return "Soil"
            else:
                if !Q25_NDWI! <= 110:
                    if !Q75_SLAVI! <= 11789.5:
                        if !Mean_NDBI! <= -3061.142857:
                            return "Water"
                        else:
                            return "Soil"
                    else:
                        if !Shape_idx! <= 1.941984:
                            return "Water"
                        else:
                            return "Vegetation"
                else:
                    return "Water"
        else:
            if !Q25_NDBI! <= -2359.5:
                if !Q25_NDWI! <= -2066.5:
                    return "Vegetation"
                else:
                    if !Mean_NDBI! <= -3058.166667:
                        return "Water"
                    else:
                        if !Q25_NDWI! <= 131:
                            if !Q75_SLAVI! <= 11777:
                                return "Soil"
                            else:
                                return "Water"
                        else:
                            return "Water"
            else:
                if !Q25_NDWI! <= -102:
                    return "Soil"
                else:
                    if !Q25_NDWI! <= 100.5:
                        return "Soil"
                    else:
                        return "Water"
