import pandas as pd

import math

import datashader as ds
import datashader.transfer_functions as tf

from pip._vendor.distlib.compat import raw_input

output = pd.read_pickle("D:\\DSOutput")

# year_list = list(output['year'])nan
# latitude_list = list(output['artist_latitude'])
# longitude_list = list(output['artist_longitude'])

columns = ['year', 'artist_latitude', 'artist_longitude']
plot_dict = {}

df = pd.DataFrame(columns=columns)
df_pointer = 0

length = len(output)

for plot_dict_index, plot_dict_pointer in enumerate(output['year']):

    node_flag = True

    if output['year'][plot_dict_index] == 0:
        node_flag = False

    elif math.isnan(output['artist_latitude'][plot_dict_index]):
        node_flag = False

    elif math.isnan(output['artist_longitude'][plot_dict_index] == "NaN"):
        node_flag = False

    if node_flag:
        plot_dict['year'] = output['year'][plot_dict_index]
        plot_dict['artist_latitude'] = output['artist_latitude'][plot_dict_index]
        plot_dict['artist_longitude'] = output['artist_longitude'][plot_dict_index]

        df.loc[df_pointer] = plot_dict
        df_pointer += 1

