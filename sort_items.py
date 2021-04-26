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
    with open(file_name, "r",) as csv_f:
        reader = csv.reader(csv_f)

        for line_idx, line in enumerate(reader):
            if line_idx == row_number:
                list_of_num = [int(num) for num in line]

        return list_of_num


def selection_sort(number_array, direction="ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    # hlavny cyklus prechadzania sekvencie

    for count, _ in enumerate(number_array):
        extreme_idx = count
        for num_idx, number in enumerate(number_array[count:]):
            if direction == "ascending":
                if number < number_array[extreme_idx]:
                    extreme_idx = num_idx + count #priebezne minimum
            elif direction == "descending":
                if number > number_array[extreme_idx]:
                    extreme_idx = num_idx + count


        number_array[count], number_array[extreme_idx] = number_array[extreme_idx], number_array[count]

    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """


def main():



    # Ukol: Selection Sort
    row = read_row("numbers_one.csv")
    sorter_row = selection_sort(row)

    # Ukol: Selection Sort - se smerem razeni

    # Ukol: Bubble Sort
    selected_row = read_rows("numbers_two.csv", 2)
    print(selected_row)

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

