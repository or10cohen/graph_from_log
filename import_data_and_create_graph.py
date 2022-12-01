from graph_data_analyzer import create_graph
from import_txt import search_str
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import json
import ast

logFileText = "log.txt"
firstTextSearch = "'graph_title': 'DS1 Flatness and Tilt 0.0'"
NumberDataLines, DataLines = search_str(logFileText, firstTextSearch)
print(Fore.GREEN + str(NumberDataLines))
print(Fore.GREEN + str(len(NumberDataLines)))
DataLines = DataLines[0][79:]
# print(DataLines)
DataLines = ast.literal_eval(DataLines)
# print(DataLines)
print(type(DataLines))
DataLines = [DataLines]
create_graph(DataLines)







