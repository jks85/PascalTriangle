# functions for comparing the speeds of get_binom_coeff and fast_binom_coeff
# See file Analysis.md for results summary

import time
import Pascal

##### CODE FOR FUNCTIONS USE FOR TESTING #####

def get_binom_coeff_time(n,k, num_trials):
    '''
    Calls get_binom_coeff num_trials times and returns the time
    required to compute the value


    :param n: non-negative integer representing row in triangle
    :param k: non-negative integer less than n that represents the index of row element
    :return: average elapsed time to compute binom coefficient n,k for num_trials attempts
    '''

    # initialize list to contain elapsed time of each computation
    trial_times = []

    # repeatedly compute binomial coefficient
    for trial in range(num_trials):
        # compute elapsed time to find binomial coefficient
        start_time = time.time()
        Pascal.get_binom_coeff(n,k)
        end_time = time.time()
        time_elapsed = end_time - start_time

        # add time to list
        trial_times.append(time_elapsed)

    # compute average time
    avg_time = sum(trial_times)/len(trial_times)

    # return trial_times[0]
    return round(avg_time, 2)      # round to hundredths of a second


def fast_binom_coeff_time(n,k, num_trials):
    '''
    Calls fast_binom_coeff num_trials times and returns the time
    required to compute the value


    :param n: non-negative integer representing row in triangle
    :param k: non-negative integer less than n that represents the index of row element
    :return: average elapsed time to compute binom coefficient of (n,k) for num_trials attempts
    '''

    # initialize list to contain elapsed time of each computation
    trial_times = []

    # repeatedly compute binomial coefficient
    for trial in range(num_trials):
        # compute elapsed time to find binomial coefficient
        start_time = time.time()
        Pascal.fast_binom_coeff(n,k)
        end_time = time.time()
        time_elapsed = end_time - start_time

        # add time to list
        trial_times.append(time_elapsed)

    # compute average time
    avg_time = sum(trial_times)/len(trial_times)

    # return trial_times[0]
    return round(avg_time, 2)      # round to hundredths of a second

#####################################
# TESTS BELOW
#####################################


# time tests below. see Analysis.md file for writeup

num_trials = 5

# n = 26
# k= 12
# print(Pascal.get_binom_coeff(n,k))
# print(get_binom_coeff_time(n,k,5))

# elements in middle of row take longest to create.
# compute "middle" element in each row
# odd row has no middle element so using integer division
# "middle" element is (n,n//2)




num_rows = 20

# using fast method

fast_start_time = time.time()
# dictionary holding tuples corresponding to coeff and time elapsed
# fast method is surprisingly fast
coeff_dict = {(row,row//2):fast_binom_coeff_time(row,row//2,1) for row in range(num_rows+1)}
fast_end_time = time.time()

fast_time_elapsed = round(fast_end_time - fast_start_time,2)
print("Fast method took", fast_time_elapsed, "seconds")
print("Results:")
print(coeff_dict.items())



# using slow method
# line 114 is commented out as it can take a while to run depending on the parameters


naive_start_time = time.time()
# dictionary holding tuples corresponding to coeff and time elapsed
# next line is commented out as it can take a *VERY LONG TIME* to run depending on 'num_rows_ parameter
#coeff_dict = {(row,row//2):get_binom_coeff_time(row,row//2,1) for row in range(num_rows+1)}
naive_end_time = time.time()

naive_time_elapsed = round(naive_end_time - naive_start_time,2)
print("Naive method took", naive_time_elapsed, "seconds")
print("Results:")
print(coeff_dict.items())




# "slow" results below:
# only ran this once. since it took a while
# dict item is (row, index):time
# dict_items([((0, 0), 0.0), ((1, 0), 0.0), ((2, 1), 0.0), ((3, 1), 0.0), ((4, 2), 0.0), ((5, 2), 0.0), ((6, 3), 0.0),
# ((7, 3), 0.0), ((8, 4), 0.0), ((9, 4), 0.0), ((10, 5), 0.0), ((11, 5), 0.0), ((12, 6), 0.0), ((13, 6), 0.0),
# ((14, 7), 0.0), ((15, 7), 0.0), ((16, 8), 0.01), ((17, 8), 0.01), ((18, 9), 0.01), ((19, 9), 0.03), ((20, 10), 0.05),
# ((21, 10), 0.1), ((22, 11), 0.19), ((23, 11), 0.37), ((24, 12), 0.73), ((25, 12), 1.48), ((26, 13), 2.82),
# ((27, 13), 5.51), ((28, 14), 11.08), ((29, 14), 31.41), ((30, 15), 80.22)])

# for middle coefficient of row
# naive method get_coeff works basically instantly up until row 15
# ~row 16 it begins to take hundredths of a second

# the time appears roughly to double for each row, exponential time complexity?
# this is sensible. based on the identity, each interior element is computed using two elements from the prior row
# at row 30 we see a computation time of ~80 seconds




# "fast" results
# dict_items([((0, 0), 0.0), ((1, 0), 0.0), ((2, 1), 0.0), ((3, 1), 0.0), ((4, 2), 0.0), ((5, 2), 0.0), ((6, 3), 0.0),
# ((7, 3), 0.0), ((8, 4), 0.0), ((9, 4), 0.0), ((10, 5), 0.0), ((11, 5), 0.0), ((12, 6), 0.0), ((13, 6), 0.0),
# ((14, 7), 0.0), ((15, 7), 0.0), ((16, 8), 0.0), ((17, 8), 0.0), ((18, 9), 0.0), ((19, 9), 0.0), ((20, 10), 0.0),
# ((21, 10), 0.0), ((22, 11), 0.0), ((23, 11), 0.0), ((24, 12), 0.0), ((25, 12), 0.0), ((26, 13), 0.0), ((27, 13), 0.0),
# ((28, 14), 0.0), ((29, 14), 0.0), ((30, 15), 0.0)])


# The fast method is considerably faster