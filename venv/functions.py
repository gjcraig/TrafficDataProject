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

def police_force():
    """Return the count for each police count"""
    # TODO add option for only specific forces
    counts = [0] * 51
    force = dict(zip(['Metropolitan Police','Cumbria','Lancashire',
                       'Merseyside','Greater Manchester','Cheshire',
                       'Northumbria','Durham','North Yorkshire',
                       'West Yorkshire','South Yorkshire','Humberside',
                       'Cleveland','West Midlands','Staffordshire',
                       'West Mercia','Warwickshire','Derbyshire',
                       'Nottinghamshire','Lincolnshire','Leicestershire',
                       'Northamptonshire','Cambridgeshire','Norfolk',
                       'Suffolk','Bedfordshire','Hertfordshire',
                       'Essex','Thames Valley','Hampshire',
                       'Surrey','Kent','Sussex',
                       'City of London','Devon and Cornwall','Avon and Somerset',
                       'Gloucestershire','Wiltshire','Dorset',
                       'North Wales','Gwent','South Wales',
                       'Dyfed-Powys','Northern','Grampian',
                       'Tayside','Fife','Lothian and Borders',
                       'Central','Strathclyde','Dumfries and Galloway'],counts))

    with open("Road_Safety_Data.csv", encoding="UTF-8") as f:
        f.readline() # skip header
        while True:
            line = f.readline()
            cols = [str(s) for s in line.split(',')]
            if len(cols) == 25:
                if cols[4] == 1:
                    force['Metropolitan Police'] = force.get('Metropolitan Police') + 1
                elif cols[4] == 3:
                    force['Cumbria'] = force.get('Cumbria') + 1
                elif cols[4] == 4:
                    force['Lancashire'] = force.get('Lancashire') + 1
                elif cols[4] == 5:
                    force['Merseyside'] = force.get('Merseyside') + 1
                elif cols[4] == 6:
                    force['Greater Manchester'] = force.get('Greater Manchester') + 1
                elif cols[4] == 7:
                    force['Cheshire'] = force.get('Cheshire') + 1
                elif cols[4] == 10:
                    force['Northumbria'] = force.get('Northumbria') + 1
                elif cols[4] == 11:
                    force['Durham'] = force.get('Durham') + 1
                elif cols[4] == 12:
                    force['North Yorkshire'] = force.get('North Yorkshire') + 1
                elif cols[4] == 13:
                    force['West Yorkshire'] = force.get('West Yorkshire') + 1
                elif cols[4] == 14:
                    force['South Yorkshire'] = force.get('South Yorkshire') + 1
                elif cols[4] == 16:
                    force['Humberside'] = force.get('Humberside') + 1
                elif cols[4] == 17:
                    force['Cleveland'] = force.get('Cleveland') + 1
                elif cols[4] == 20:
                    force['West Midlands'] = force.get('West Midlands') + 1
                elif cols[4] == 21:
                    force['Staffordshire'] = force.get('Staffordshire') + 1
                elif cols[4] == 22:
                    force['West Mercia'] = force.get('West Mercia') + 1
                elif cols[4] == 23:
                    force['Warwickshire'] = force.get('Warwickshire') + 1
                elif cols[4] == 30:
                    force['Derbyshire'] = force.get('Derbyshire') + 1
                elif cols[4] == 31:
                    force['Nottinghamshire'] = force.get('Nottinghamshire') + 1
                elif cols[4] == 32:
                    force['Lincolnshire'] = force.get('Lincolnshire') + 1
                elif cols[4] == 33:
                    force['Leicestershire'] = force.get('Leicestershire') + 1
                elif cols[4] == 34:
                    force['Northamptonshire'] = force.get('Northamptonshire') + 1
                elif cols[4] == 35:
                    force['Cambridgeshire'] = force.get('Cambridgeshire') + 1
                elif cols[4] == 36:
                    force['Norfolk'] = force.get('Norfolk') + 1
                elif cols[4] == 37:
                    force['Suffolk'] = force.get('Suffolk') + 1
                elif cols[4] == 40:
                    force['Bedfordshire'] = force.get('Bedfordshire') + 1
                elif cols[4] == 41:
                    force['Hertfordshire'] = force.get('Hertfordshire') + 1
                elif cols[4] == 42:
                    force['Essex'] = force.get('Essex') + 1
                elif cols[4] == 43:
                    force['Thames Valley'] = force.get('Thames Valley') + 1
                elif cols[4] == 44:
                    force['Hampshire'] = force.get('Hampshire') + 1
                elif cols[4] == 45:
                    force['Surrey'] = force.get('Surrey') + 1
                elif cols[4] == 46 :
                    force['Kent'] = force.get('Kent') + 1
                elif cols[4] == 47:
                    force['Sussex'] = force.get('Sussex') + 1
                elif cols[4] == 48:
                    force['City of London'] = force.get('City of London') + 1
                elif cols[4] == 50:
                    force['Devon and Cornwall'] = force.get('Devon and Cornwall') + 1
                elif cols[4] == 52:
                    force['Avon and Somerset'] = force.get('Avon and Somerset') + 1
                elif cols[4] == 53:
                    force['Gloucestershire'] = force.get('Gloucestershire') + 1
                elif cols[4] == 54:
                    force['Wiltshire'] = force.get('Wiltshire') + 1
                elif cols[4] == 55:
                    force['Dorset'] = force.get('Dorset') + 1
                elif cols[4] == 60:
                    force['North Wales'] = force.get('North Wales') + 1
                elif cols[4] == 61:
                    force['Gwent'] = force.get('Gwent') + 1
                elif cols[4] == 62:
                    force['South Wales'] = force.get('South Wales') + 1
                elif cols[4] == 63:
                    force['Dyfed-Powys'] = force.get('Dyfed-Powys') + 1
                elif cols[4] == 91:
                    force['Northern'] = force.get('Northern') + 1
                elif cols[4] == 92:
                    force['Grampian'] = force.get('Grampian') + 1
                elif cols[4] == 93:
                    force['Tayside'] = force.get('Tayside') + 1
                elif cols[4] == 94:
                    force['Fife'] = force.get('Fife') + 1
                elif cols[4] == 95:
                    force['Lothian and Borders'] = force.get('Lothian and Borders') + 1
                elif cols[4] == 96:
                    force['Central'] = force.get('Central') + 1
                elif cols[4] == 97:
                    force['Strathclyde'] = force.get('Strathclyde') + 1
                elif cols[4] == 98:
                    force['Dumfries and Galloway'] = force.get('Dumfries and Galloway') + 1
            if not line:
                break
    return force

# ^^ NOT WORKING

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

def day_of_week(day = -1):
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

