import pandas as pd
import numpy as np
import datashader
import bokeh.plotting
import collections
import xarray
import time
from datashader import utils

import os
import sys
import time
import plotly
import h5py as reza

import pandas as pd
from pip._vendor.distlib.compat import raw_input


files = []
files_number = 0


def directory_find(directory):
    temp_list = os.listdir(directory)

    for files_list_index in temp_list:
        if os.path.isdir(directory + "\\" + files_list_index):
            directory_find(directory + "\\" + files_list_index)

        elif os.path.isfile(directory + "\\" + files_list_index):
            files.append(directory + "\\" + files_list_index)


def get_directory_from_user(message_to_show, dir_type):
    while True:
        print(message_to_show)
        # directory = "E:\project\python\projectTest\instacart_2017_05_01\order_products__train.csv"
        directory = "D:\Project files\MillionSongSubset\data\A\A\A\TRAAAAW128F429D538.h5"

        if dir_type == 0:
            if os.path.isdir(directory):
                break
            else:
                print("your address is not a valid directory . please try again")
                raw_input("Press Enter to continue...")
                os.system('cls')
        else:
            if os.path.isfile(directory):
                break
            else:
                print("your path is not for a file . please try again")
                raw_input("Press Enter to continue...")
                os.system('cls')

    return directory


file_path = get_directory_from_user("\nplease insert your file directory to load it : ", 1)

print("**********************************************")
print("app is begin process , please be patient ...")

start_time = time.process_time()

# titles = ["order_id", "user_id", "eval_set", "order_number", "order_dow", "order_hour_of_day",
#          "days_since_prior_order"]


file = reza.File(file_path, 'r')

group = list(file.keys())

hala = file.require_group('metadata').keys()
# print(list(hala))
# raw_input("khb")

# print("\ngroups are : ")
print(group, "\n")

print(file['metadata']['songs'][0][14].decode("utf-8"))
raw_input("enter")

for group_index in group:
    # print(group_index, "group are : ")
    data = list(file[group_index])
    # print(data, "\n")
    for data_index in data:
        my_data = list(file[group_index][data_index])

work_type = raw_input("1. read pickle\n2. write pickle\n")

if work_type == "1":
    output = pd.read_pickle("D:\\DSOutput")
    output_dict = dict(output)
    print(len(output_dict['release']))

elif work_type == "2":

    columns = ['release', 'duration', 'loudness', 'tempo', 'danceability', 'song_hotness', 'artist_name',
               'artist_latitude', 'artist_longitude',
               'artist_location', 'artist_familiarity', 'artist_hotness', 'year']

    data = {}

    print(data)

    source_directory = "D:\Project files\MillionSongSubset\data"

    directory_find(source_directory)

    print("number of files = ", len(files), "\n\n")

    df = pd.DataFrame(columns=columns)

    for files_pointer, files_index in enumerate(files):
        file = reza.File(files_index, 'r')

        data['release'] = file['metadata']['songs'][0][14].decode("utf-8")

        data['duration'] = file['analysis']['songs'][0][3]

        data['loudness'] = file['analysis']['songs'][0][23]

        data['tempo'] = file['analysis']['songs'][0][27]

        data['danceability'] = file['analysis']['songs'][0][2]

        data['song_hotness'] = file['metadata']['songs'][0][16]

        data['artist_name'] = file['metadata']['songs'][0][9].decode("utf-8")

        data['artist_latitude'] = file['metadata']['songs'][0][5]

        data['artist_longitude'] = file['metadata']['songs'][0][7]

        data['artist_location'] = file['metadata']['songs'][0][6].decode("utf-8")

        data['artist_familiarity'] = file['metadata']['songs'][0][2]

        data['artist_hotness'] = file['metadata']['songs'][0][3]

        data['year'] = file['musicbrainz']['songs'][0][1]

        # df = df.append(data, ignore_index=True)
        df.loc[files_pointer] = data

    # print("size of data dictionary = ", len(data['release']))
    # print("size of danceability in data dictionary = ", len(data['danceability']))
    # print("size of year in data dictionary = ", len(data['year']))

    df.to_pickle("D:\\DSOutput", protocol=4)

    print(df)

########################################################################################################
"""


end_time = time.process_time() - start_time

raw_input("Press Enter to show run time...")

print("\ntime : ")
print(end_time)
"""
# raw_input("Press Enter to continue...")
# print(order_list)
