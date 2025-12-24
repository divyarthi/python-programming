import numpy as np

def macro_calculator(nutri_data):
    """
    understand broadcasting
    """
    total_calorie=nutri_data.sum(axis = 0)
    print(total_calorie.shape,nutri_data.shape)
    return 100*nutri_data/total_calorie

if __name__=="__main__":
    nutri = np.array([[10,20,30],[5,20,40]])
    print(macro_calculator(nutri))