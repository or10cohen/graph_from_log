import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import linecache


def search_str(file_path, first_word):
    NumberDataLines = []
    Datalines = []

    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if first_word in content:
            print(Fore.GREEN + 'first_word exist in a file')
        else:
            print(Fore.RED + 'first_word does not exist in a file')
    file.close()

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(first_word) != -1:
                NumberDataLines.append(lines.index(line))
    file.close()

    def get_lines(file_path, line_numbers):
        return (x for i, x in enumerate(file_path) if i in line_numbers)

    with open(file_path, 'r') as fp:
        lines = get_lines(fp, NumberDataLines)
        for line in lines:
            Datalines.append(line.strip())
    file.close()

    return NumberDataLines, Datalines

if __name__ == '__main__':
    logFileText = "log.txt"
    firstTextSearch = "'graph_title': 'DS1 Flatness and Tilt 0.0'"
    NumberDataLines, DataLines = search_str(logFileText, firstTextSearch)
    print(Fore.GREEN + str(NumberDataLines))
    print(Fore.GREEN + str(len(NumberDataLines)))
    DataLines = str(DataLines)
    DataLines = DataLines[81:-2]
    print(type(DataLines))
    print(DataLines)
