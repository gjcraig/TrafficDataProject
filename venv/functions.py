import math


def df(file):
    """Return a csv file as a 2d array"""
    data_list = []
    with open(file, encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                data_list.append(cols)
            if not line:
                break
    return data_list


def mean(a):
    """Return the mean value of a list"""
    return sum(a) / len(a)


def var(a):
    """Return the variance of a population"""
    m = mean(a)
    return sum((i - m) ** 2 for i in a) / len(a)


def svar(a):
    """Return the variance of a sample"""
    m = mean(a)
    return float(sum((i - m) ** 2 for i in a) / (len(a)-1))


def student_two(x, y, sample=0):
    """Return a two-sample t-test for unpaired data"""
    # test statistic
    if sample == 0:
        t = (mean(x) - mean(y)) / (float((var(x)/len(x))+(var(y)/len(y)))**0.5)
    else:
        t = (mean(x) - mean(y)) / (float((svar(x)/len(x))+(svar(y)/len(y)))**0.5)
    # degrees of freedom
    if sample == 0:  # sample or population variance
        s1 = var(x)
        s2 = var(y)
    else:
        s1 = svar(x)
        s2 = svar(y)
    n1 = len(x)
    n2 = len(y)
    degf = (((s1/n1)+(s2/n2))**2) / (((s1/n1)**2) / (n1 - 1) + ((s2/n2)**2) / (n2 - 1))
    print("Test statistic:  T = ", t, "\nd.f = ", int(degf))


def sum_squares(a):
    return sum(i**2 for i in a)


def anova_one(*args):
    # n groups each in a list
    args = [arg for arg in args]
    n_groups = len(args)
    flat = [num for sublist in args for num in sublist]
    N = len(flat)

    #  Calculate the mean within each group
    group_means = [mean(i) for i in args]

    #  Calculate the overall mean
    overall_mean = mean(flat)

    # Calculate the "between-group" sum of squared differences
    between_ss = 0
    for i in range(n_groups):
        between_ss += len(args[i]) * ((group_means[i] - overall_mean)**2)
    between_freedom = n_groups - 1
    between_mean_square = between_ss / between_freedom

    # center data in each group
    for i in range(n_groups):
        args[i][:] = [x - group_means[i] for x in args[i]]

    # Calculate the "within-group" sum of squares.
    flat_center = [num for sublist in args for num in sublist]
    within_ss = sum_squares(flat_center)
    within_freedom = sum(len(args[i]) - 1 for i in range(n_groups))
    within_mean_square = within_ss / within_freedom

    # F-ratio
    F = between_mean_square / within_mean_square

    print("Test statistic:  F = ", F, "\nd\u2081 = ", between_freedom, "\nd\u2082 = ", within_freedom)


def head_filter(header, data, file):
    """ Return a list of list for a filter for one header"""
    data_list = []
    with open(file, encoding="UTF-8") as f:
        head = [str(s) for s in f.readline().split(',')]
        for i in range(len(head)):
            if head[i] == header:
                data_list = [row[i] for row in data]
                break
        else:
            print("Header not found")
    return data_list


def header_count(header, filter):
    """Return the number of entries for given filter"""
    # TODO add error checking on input
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        headers = [str(s) for s in f.readline().split(',')]
        for i in range(len(headers)):
            if headers[i] == header:
                j = i
                break
        else:
            print('Header not found')
            return
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[j]) == filter:
                    count += 1
            if not line:
                break
    return count


def date_filter(date1, date2):
    """Return the number of entries between two dates; inclusive"""
    # TODO add error checking on input
    count = 0
    date1 = [int(s) for s in date1.split('/')]
    date2 = [int(s) for s in date2.split('/')]
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline() # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                date = [int(s) for s in cols[8].split('/')]
            if len(date) == 3:
                if (date1[0] <= date[0] <= date2[0] and
                        date1[1] <= date[1] <= date2[1] and
                        date1[2] <= date[2] <= date2[2]):
                    count += 1
            if not line:
                break
    return count
