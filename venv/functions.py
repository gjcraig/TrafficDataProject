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
    return sum((i - m) ** 2 for i in a) / (len(a)-1)


def student_two(x, y, sample=0):
    """Return a two-sample t-test for unpaired data"""
    # test statistic
    if sample == 0:
        t = (mean(x) - mean(y)) / (math.sqrt((var(x)/len(x))+(var(y)/len(y))))
    else:
        t = (mean(x) - mean(y)) / (math.sqrt((svar(x)/len(x))+(svar(y)/len(y))))
    # critical value
    return print("Test statistic:  T = ", t)


def regression():
    return 0


def anova_one():
    return 0


def head_filter(header):
    """ Return a list of list for a filter for one header"""
    return 0


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


def severity(level):
    """Return the number of entries for given severity"""
    # TODO add error checking on input
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[5]) == level:
                    count += 1
            if not line:
                break
    return count


def number_of_vehicles(number):
    """Return count of accidents involeing a specific number of vehicles"""
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[6]) == number:
                    count += 1
            if not line:
                break
    return count


def number_of_casualties(number):
    """Return count of accidents involving a specific number of casualties"""
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[7]) == number:
                    count += 1
            if not line:
                break
    return count


def road_type(type):
    """Return count of accidents involving a specific road type"""
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[12]) == type:
                    count += 1
            if not line:
                break
    return count


def light_condition(con):
    """Return count of accidents involving a specific light level"""
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[20]) == con:
                    count += 1
            if not line:
                break
    return count


def weather_condition(con):
    """Return count of accidents involving a specific weather condition"""
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[21]) == con:
                    count += 1
            if not line:
                break
    return count


def road_condition(con):
    """Return count of accidents involving a specific road condition"""
    count = 0
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if int(cols[22]) == con:
                    count += 1
            if not line:
                break
    return count


def speed_limits():
    """Return dictionary of number of accidents at different speed limits"""
    speeds = {}
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline()  # skip header line
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                speeds[cols[13]] = speeds.get(cols[13],0) +1
            if not line:
                break

    return speeds


def day_of_week(day=-1):
    """Return dictionary of number of accidents at different times or count for specific day"""
    days = {}
    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        if day == -1:
            f.readline()  # skip header line
            while True:
                line = f.readline()
                cols = [str(s) for s in line.split(',')]
                if len(cols) == 25:
                    days[cols[9]] = days.get(cols[9],0) +1
                if not line:
                    break
            return days
        else:
            count = 0
            f.readline()
            while True:
                line = f.readline()
                cols = [str(s) for s in line.split(',')]
                if len(cols) == 25:
                    if int(cols[9]) == day:
                        count += 1
                if not line:
                    break
            return count

# Junction_Detail
# Junction_Control
# nd_Road_Class
# nd_Road_Number
# Pedestrian_Crossing-Human_Control
# Pedestrian_Crossing-Physical_Facilities
# Special_Conditions_at_Site
# Carriageway_Hazards
# st_Road_Class
# st_Road_Number
