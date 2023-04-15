import pathlib
from re import compile
from chardet import detect
from pathlib import Path
import csv
import inspect
import os
import sys


def get_script_dir(follow_symlinks=True) -> str:
    if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def detect_enc(file_path: Path, n_lines: int = 20) -> str:
    with Path(file_path).open('rb') as f:
        rawdata = b''.join([f.readline() for _ in range(n_lines)])
    return str(detect(rawdata)['encoding'])


def get_data(find_value: list, path_dir, path_file) -> list[dict]:
    match_value = []
    for path_file in pathlib.Path(path_dir).glob(path_file):
        dict_value = {}
        for x in find_value:
            with open(path_file, 'r', encoding=detect_enc(path_file)) as f_r:
                os_prod_reg = compile(fr'{x}\s*\S*')
                data = f_r.read()
                findall_data = os_prod_reg.findall(data)
                dict_value[x] = findall_data[0].split()[2]
        match_value.append(dict_value)
    return match_value


def write_to_csv(data: list[dict], path_file):
    with open(f'{path_file}', 'w') as f_w:
        csv_w = csv.DictWriter(f_w, fieldnames=list(data[0].keys()),
                               quoting=csv.QUOTE_NONNUMERIC)
        csv_w.writeheader()
        for d in data:
            csv_w.writerow(d)


find_value = ['Изготовитель системы:',
              'Название ОС:', 'Код продукта:', 'Тип системы:']
match_value = get_data(find_value, get_script_dir(), r'info*.txt')
write_to_csv(match_value, os.path.join(get_script_dir(), 'csv_data.csv'))