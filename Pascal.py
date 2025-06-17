# Two functions that generate binomial coefficients
# efficiency is compared in Testing.py
# results writeup in Analysis.md

import time

def get_binom_coeff(n:int, k:int) -> int:
    '''
    This function computes the element in Pascal's triangle corresponding to
    row n and index k. Note that the first row in Pascal's triangle is row 0
    and the index of the first element of is also 0.

    The coefficient is computed recursively using the known identity for
    computing interior row elements of Pascal's triangle:

                    (n,k) + (n,k+1) = (n+1,k+1)


    :param n: non-negative integer representing row in triangle
    :param k: non-negative integer less than n that represents the index of row element
    :return: value in Pascal's triangle corresponding to row n, index k
    '''

    assert n >= 0
    assert 0 <= k <= n


    if k == 0 or k == n:
        return 1            # return 1 at end of row

    return get_binom_coeff(n-1,k-1) + get_binom_coeff(n-1,k)



def fast_binom_coeff(n:int, k:int, coeff_dict = {(0,0):1, (1,0):1, (1,1):1}) -> int:
    '''
    This function computes the element in Pascal's triangle corresponding to
    row n and index k. This implementation optimizes the computation by using
    memoization to reduce the number of recursive calls. The memoization also
    takes advantage of the symmetry of Pascal's triangle

    Note that the first row in Pascal's triangle is row 0 and the index of the
    first element of is also 0.

    The coefficient is computed recursively using the known identity for
    computing interior row elements of Pascal's triangle:

                    (n,k) + (n,k+1) = (n+1,k+1)


    :param n: non-negative integer representing row in triangle
    :param k: non-negative integer less than n that represents the index of row element
    :return: value in Pascal's triangle corresponding to row n, index k
    '''

    # coeff_dict = {(0,0):1, (1,0):1, (1,1):1}     # initialize dict of binomial coefficients

    try:
        assert n >= 0

    except:
        return "Invalid value of n. Choose a non-negative integer"

    try:
        assert 0 <= k <= n

    except:
        return "Invalid value of n. Choose a non-negative integer between 0 and n (inclusive)"



    # check dict for (row,index) tuple
    if (n,k) in coeff_dict:
        return coeff_dict[(n,k)]

    # first and last element of row is always 1 (index 0 and n)
    if k == 0 or k == n:
        coeff_dict[(n,k)] = 1
        coeff_dict[(n, n - k)] = 1
        return 1

    # second element and next to last element of row is always n (index 1, index n-1)
    if k == 1 or k == n-1:
        coeff_dict[(n, k)] = n
        coeff_dict[(n, n - k)] = n
        return n

    # compute interior elements using identity and update dict
    row_n_coeff = fast_binom_coeff(n - 1, k - 1) + fast_binom_coeff(n - 1, k)
    coeff_dict[(n,k)] = row_n_coeff
    return row_n_coeff

######
# small tests below
# see Testing.py and Analysis.md

n = 50
k = 25

start_time = time.time()

fast_coeff = fast_binom_coeff(n,k)

end_time = time.time()

time_elapsed = round(end_time - start_time,2)

print("Coeff (",n,",",k,") is: ",fast_coeff,"Sim took", time_elapsed, "seconds")


# print(get_binom_coeff(0,0))
# print(get_binom_coeff(1,0))
# print(get_binom_coeff(1,1))
# print(get_binom_coeff(5,2))


# print(get_binom_coeff(6,4))
#
#
# # print pascal's triangle
# # prints space between elements on same row.
# for row in range(0,10):
#     for index in range(0,row + 1):
#         print(get_binom_coeff(row,index),end= " ")
#     print("")