import argparse

# 'M' or more consecutive days not allowed to miss classes.
# default is 4 as per question
M_DAYS = 4


def attend(n):
    """
    calculate belows :
    [1] The number of ways to attend classes over N days.
    [2] The probability that you will miss your graduation ceremony.

        n :
            total of days to attend the class

        return :
            the string format as "Answer of [2] / Answer of [1]"
    """

    days = n

    matrix = [[0] * (M_DAYS + 1) for each in range(days + 1)]

    for each in range(M_DAYS):
        matrix[0][each] = 1

    for i in range(1, days + 1):
        for j in range(M_DAYS - 1, -1, -1):
            matrix[i][j] = matrix[i - 1][0] + matrix[i - 1][j + 1]

    # total ways to attend classes over N days
    attend_days = matrix[days][0]

    # total ways to miss graduation ceremony
    miss_days = matrix[days - 1][1]

    return f"{miss_days} / {attend_days}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Provide the Total Number of days to attend the class")

    parser.add_argument("--n_days", type=int, help="Total Number of days to attend the class", default=5)
    args = parser.parse_args()

    n_days = args.n_days

    print(attend(n_days))
