import pandas as pd
import numpy as np

def clean_new_house(new_house):
    new_house[new_house["bathroom"] >= 2] = 2
    new_house["exterior"] = new_house["exterior"].replace("Si",True).replace("No",False)
    new_house["parkingSpace_included_in_listing"] = new_house["parkingSpace_included_in_listing"].replace("Si",True).replace("No",False)
    new_house[new_house["rooms"] >= 3] = "3 or more"
    new_house[new_house["floor_grouped"] >= 4] = "4 or more"
    new_house["p_area_property_grouped"] = new_house["p_area_property_grouped"].str.lower()
    new_house[new_house["p_area_property_grouped"] != "studio"] = "flat or other"
    new_house["hasPlan"] = new_house["hasPlan"].replace("Si",True).replace("No",False)
    
    return new_house