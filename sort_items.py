import csv
import os
import random

cwd_path = os.getcwd()


def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    # file_path = os.path.join(cwd_path, file_name)

    with open(file_name, "r",) as f:
        reader = csv.reader(f, delimiter="\t")

        for row in reader:
            list_of_num = [int(num) for num in row]

        return list_of_num


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """


def selection_sort(number_array):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    # hlavny cyklus prechadzania sekvencie

    for count, _ in enumerate(number_array):
        min_idx = count
        for num_idx, number in enumerate(number_array[count:]):
            if number < number_array[min_idx]:
                min_idx = num_idx + count #priebezne minimum

        number_array[count], number_array[min_idx] = number_array[min_idx], number_array[count]

    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """


def main():

    row = read_row("numbers_one.csv")

    # Ukol: Selection Sort
    sorter_row = selection_sort(row)
    print(sorter_row)

    # Ukol: Selection Sort - se smerem razeni
    

    # Ukol: Bubble Sort


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

