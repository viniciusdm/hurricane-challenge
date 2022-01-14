#Desafio Hurricane BTG - Vinicius Bueno de Moraes - 14/01/2022

#Libraries
import re
import time
from matplotlib.path import Path
from matplotlib import path
from functools import wraps
import pandas as pd
import numpy as np
import os


def timeit(log_string: str):
    """ Decorator that logs a function time elapsed, with a custom message """

    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = function(*args, **kwargs)
            time_elapsed = f'{(time.perf_counter() - start):.2f}'
            print(log_string.format(time_elapsed=time_elapsed))
            return result
        return wrapper
    return real_decorator


def read_rain_file(file_path: str) -> pd.DataFrame:
    with open(file_path, 'r') as f:
        raw_file = f.readlines()

    list_dados = [line.split() for line in raw_file]
    float_raw_lines = [list(map(float, raw_line)) for raw_line in list_dados]
    return pd.DataFrame(float_raw_lines, columns=['lat', 'long', 'data_value'])


def read_contour_file(file_path: str) -> pd.DataFrame:
    line_split_comp = re.compile(r'\s*,')

    with open(file_path, 'r') as f:
        raw_file = f.readlines()

    l_raw_lines = [line_split_comp.split(raw_file_line.strip()) for raw_file_line in raw_file]
    l_raw_lines = list(filter(lambda item: bool(item[0]), l_raw_lines))
    float_raw_lines = [list(map(float, raw_line))[:2] for raw_line in l_raw_lines]
    header_line = float_raw_lines.pop(0)
    assert len(float_raw_lines) == int(header_line[0])
    return pd.DataFrame(float_raw_lines, columns=['lat', 'long'])


def apply_contour(contour_df: pd.DataFrame, rain_df: pd.DataFrame) -> pd.DataFrame:
    pass

def main() -> None:

    #Local da pasta raiz PC / local baseConda run
    my_path = "/Users/viniciusmoraes/Downloads/hurricane-challenge/"

    start = time.time()

    contour_df: pd.DataFrame = read_contour_file(my_path+"PSATCMG_CAMARGOS.bln")
    
    rain_df = pd.DataFrame()
    dates = ["021221", "031221", "041221", "051221", "061221", "071221", "081221", "091221", "101221", "111221"]
    for i in dates:
        rain_mult_df : pd.DataFrame = read_rain_file(my_path+"forecast_files/ETA40_p011221a"+i+".dat")
        #copy_rain = rain_mult_df.copy()
        rain_df = rain_df.append(rain_mult_df)
        del rain_mult_df

    contour_df_array = contour_df[["lat", "long"]].to_numpy()
    rain_df_array = rain_df[["lat", "long"]].to_numpy()
    
    polygon = path.Path(contour_df_array)
    inOut = pd.DataFrame(polygon.contains_points(rain_df_array), columns=["In"])

    rain_df["In"] = inOut
    selection = rain_df[rain_df["In"] == True]

    tempExec = time.time() - start

    print("\nA precipitação média na Bacia do Grande no período foi de: %s" %round(selection["data_value"].mean(), 3))
    print("Executado em %s segundos\n" %tempExec)

#Executa main    
if __name__ == '__main__':
    main()