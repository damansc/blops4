import os
import pandas as pd

def import_cwl(Dates = [], PICKUP_FOLDER='./activision_github/cwl-data/data/', COPY_FOLDER='./data_imports/'):

    """
    Utility to import new cwl data from PICKUP_FOLDER in the cloned activision repository and stores this data
    in the COPY_FOLDER to use for analysis and further research.
    """ 

    EVENT_FILES = os.listdir(PICKUP_FOLDER)
    DATA_FILES = [s for s in EVENT_FILES if any(xs in s for xs in Dates)]
    data_list = []
    
    # picks up files cloned from activision repository and saves to the list "data_list".
    for x in DATA_FILES:
        with open('{}{}'.format(PICKUP_FOLDER, x)) as c:
            temp = pd.read_csv(c)
            data_list.append(temp)
    
    # converts data to a dataframe.
    for x in data_list:
        x = pd.DataFrame(x)
    
    # saves imported data over to the "data_imports" folder. This will allow for version control as 
    for x in data_list:
        for i in EVENT_FILES:
            x.to_csv('{}{}'.format(COPY_FOLDER, i))