## Analysis

This document compares the efficiency of the functions *get_binom_coeff()* and 
*fast_binom_coeff()* from *Pascal.py*.

### Summary of Results

Unsurprisingly, *fast_binom_coeff* performed substantially faster than *get_binom_coeff()*. However, the absolute speed
of *fast_binom_coeff* was surprising, computing coefficients into the hundreds of rows effectively instantly.


The function *get_binom_coeff()* returned coefficients essentially instantly until row 15, after which return times
began to take hundredths of a second. The return time appeared to roughly double with each new row. This exponential 
growth pattern is reasonable, as each element is computed using two elements from the preceding row. By row 25 the wait
time became somewhat noticeable and row 30 took nearly 1.5 minutes to compute the middle coefficient.

On the other hand *fast_binom_coeff* computed each coefficient effectively instantly up to row 30. However, this 
comparison still understates the efficiency-- *fast_binom_coeff* computed the middle element of row 1000 in ~0.5 seconds.


See the **Comparsion Methods** for details about the comparison design.


### Description of Functions

#### get_binom_coeff

- Uses recursion to compute coefficients of Pascal's triangle
- Exploits triangle symmetry to find the first and last element of each row
- Exploits triangle symmetry to find the second and next to last element of each row


#### fast_binom_coeff

- Optimizes *get_binom_coeff* by also using memoization to cache computed coefficients


### Comparison Methods

The file  includes code for functions that test. The code uses the **time** module and allows for the user
to choose a number of trials to repeat the computations. The average time is reported. Due to the slow speed of
*get_binom_coeff* a large number of trials were not performed.

The **time** module was used in *Testing.py* to compare function efficiency. The middle value in each row was computed 
up to row 30. A large number of recursive calls are required as we move deeper into the triangle and computing each row 
element could take quite some time. Generally, the "middle" coefficient is the most computationally expensive to 
compute, so this was the only value computed in each row. Note that odd indexed rows lack a middle value, but due to 
triangle symmetry the two values closest to the "middle" are equal.

