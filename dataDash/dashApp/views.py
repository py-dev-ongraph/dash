from django.shortcuts import render

import pandas as pd
import os
from .models import Dentrix
#finding all excel files and sheets inside each files

def file_reader(file_name,sheet):
    file_path = os.getcwd()+'/static/data/'+str(file_name)
    print(file_path)

    #loading data into pandas
    data = pd.read_excel(file_path,header=None,sheet_name=sheet)
    #transposing the data to get each column name in one list
    tr_data = data.transpose()
    column_names = []
    for key in tr_data:
        # print(tr_data[key][0])
        column_names.append(tr_data[key][0])
    print (column_names) 

