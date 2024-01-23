#!/usr/bin/python3
"""reads from stdin and computes metrics"""
import re
import sys

file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0
            }


def printCodes(dict, file_s):
    """Prints the status code and the number of times they appear"""
    print("File size: {}".format(file_s))
    for key in sorted(dict.keys()):
        if dict_sc[key] != 0:
            print("{}: {}".format(key, dict[key]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            statusC_and_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                printCodes(dict_sc, file_size)
            counter = counter + 1
            try:
                statusC = int(statusC_and_file_s.split()[0])
                f_size = int(statusC_and_file_s.split()[1])
                # print("Status Code {} size {}".format(statusC, f_size))
                if statusC in dict_sc:
                    dict_sc[statusC] += 1
                file_size = file_size + f_size
            except:
                pass
        printCodes(dict_sc, file_size)
    except KeyboardInterrupt:
        printCodes(dict_sc, file_size)
        raise
