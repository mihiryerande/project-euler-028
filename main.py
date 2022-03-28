# Problem 28:
#     Number Spiral Diagonals
#
# Description:
#     Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#         [21] 22  23  24  [25]
#          20  [7]  8  [9]  10
#          19   6  [1]  2   11
#          18  [5]  4  [3]  12
#         [17] 16  15  14  [13]
#
#     It can be verified that the sum of the numbers on the diagonals is 101.
#
#     What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Idea:
#     Find a closed-form solution for diagonals' sum, for given `n`.
#
# Derivation:
#     Diagonal Sum
#       = (sum(i^2 + (i^2-w) + (i^2-2*w) + (i^2-3*w)) [i in [1,n] stepping 2]) - 3
#             * Summing corners of each successive square in the spiral
#             * Let `w` = i-1, the step from one corner of square to previous corner, 1 less than square's "width"
#             * Subtract 3 from total to account for initial 1-by-1 square in center, which only has one corner
#
#       = (sum(4*i^2 - 6*w) [i in [1,n] stepping 2]) - 3
#             * Simplify
#
#       = (sum(4*i^2 - 6*i + 6) [i in [1,n] stepping 2]) - 3
#             * Substitute (i-1) for `w`
#
#       = (sum(4*(2*i-1)^2 - 6*(2*i-1) + 6) [i in [1,(n+1)/2]]) - 3
#             * Adjust indexing to avoid stepping by 2
#             * [i in [1,n] stepping 2] => [i in [1,(n+1/2)]]
#
#       = (sum(16*i^2 - 28*i + 16) [i in [1,(n+1)/2]]) - 3
#             * Simplify
#
#       = (sum(16*i^2 - 28*i + 16) [i in [1,m]]) - 3
#             * Substitute upper limit (n+1)/2 with `m`, for readability
#
#       = 16*[sum(i^2)[i in [1,m]] - 28*[sum(i)[i in [1,m]] + 16*[sum(1)[i in [1,m]] - 3
#             * Break summation into parts
#
#       = 16*(m*(m+1)*(2*m+1)/6) - 28*[m*(m+1)/2] + 16*m - 3
#             * Substitute individual summations with known closed-form expressions
#
#       = (16/3)*m^3 - 6*m^2 + (14/3)*m - 3
#             * Simplify
#
#       = (16/3)*((n+1)/2)^3 - 6*((n+1)/2)^2 + (14/3)*((n+1)/2) - 3
#             * Substitute (n+1)/2 back in for `m`
#
#       = (4*n^3 + 3*n^2 + 8*n - 9) / 6
#             * Simplify

def main(n):
    """
    Returns the sum of the numbers on the diagonals of an `n` by `n` number spiral.

    Args:
        n (int): Odd natural number

    Returns:
        Sum of diagonals of `n` by `n` spiral

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0 and n % 2 == 1

    return (4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) // 6


if __name__ == '__main__':
    num = int(input('Enter an odd natural number: '))
    diagonal_sum = main(num)
    print('Sum of numbers on diagonals of {0} by {0} spiral:'.format(num))
    print('  {}'.format(diagonal_sum))
