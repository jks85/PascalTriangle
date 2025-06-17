# Methods for printing  Pascal's triangle
import Pascal


def print_row_n(row_num:int) -> str:
    """
    Prints nth row of Pascal's triangle

    :param int: n, desired row of Pascal's triangle
    :return: string output of row n
    """

    for i in range(0,row_num+1):
        print(str(Pascal.fast_binom_coeff(row_num,i)), end = " ")



def print_thru_row_n(row_num:int) -> str:
    """
    Prints rows in Pascal's triangle up to row n. The triangle
    prints like a staircase. Each row prints on a separate line
    with values separated by spaces.

    :param int: n, desired row of Pascal's triangle
    :return: string of Pascal's triangle up to and including row n
    """
    # loop over row numbers and print each row
    for i in range(row_num+1):
        print_row_n(i)
        print("")


def print_Pascal(row_num:int, preceding_rows = True):
    """

    :param row_num: row number in Pascal's triangle
    :param all_rows: Boolean indicating whether to print  preceding rows
    :return: string of rows in Pascal's triangle or a single row
    """
    if preceding_rows:
        return print_thru_row_n(row_num)
    else:
        return str(print_row_n(row_num)) + "\n"



def pretty_print_row_n(row_num:int) -> str:
    """
    "Pretty" prints row n of Pascal's Triangle. Attempts
    to print triangle with top row element centered. However,
    the triangle will eventually become assymmetric as the
    numbers become large


    :param row_num: desired row number
    :return: string output of row n
    """





def pretty_print_thru_row_n(row_num) -> str:
    """
    "Pretty" prints up to row n of Pascal's Triangle.
    Prints triangle with top row element centered.

    Note: Triangle eventually becomes distorted as the
    number of digits increases.


    :param row_num: final row number
    :return: string of row(s) in Pascal's triangle
    """



def pretty_print_Pascal(row_num, preceding_rows = True):
    """
    Wrapper for pretty_print_row_n() and pretty_print_thru_row_n. Use
    "preceding_rows" parameter to indicate whether a single row or all
    rows should be printed

    :param row_num: (final) row number
    :param preceding_rows: boolean indicating whether to print preceding rows
    :return: string of row(s) in Pascal's triangle
    """

    if preceding_rows:
        return pretty_print_thru_row_n(row_num)
    else:
        return pretty_print_row_n(row_num) + "\n"