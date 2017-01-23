import csv
import sys

decoder = {
    "Locale": {
        11: "City: Large",
        12: "City: Midsize",
        13: "City: Small",
        21: "Suburb: Large",
        22: "Suburb: Midsize",
        23: "Suburb: Small",
        31: "Town: Fringe",
        32: "Town: Distant",
        33: "Town: Remote",
        41: "Rural: Fringe",
        42: "Rural: Distant",
        43: "Rural: Remote",
    },
    "InstitutionSize": {
        -1: "Not reported",
        -2: "Not applicable",
        1: "Under 1,000",
        2: "1,000 - 4,999",
        3: "5,000 - 9,999",
        4: "10,000 - 19,999",
        5: "20,000 and above",
    },
    "Level": {
         -3: "Not available",
         1:  "Four or more years",
         2:  "At least 2 but less than 4 years",
         3:  "Less than 2 years (below associate)",
    },
    "HBCU": {
        1: "Yes",
        2: "No",
    },
    "CampusHousingRequired": {
          -1: "Not reported",
          -2: "Not applicable",
          1:  "Yes",
          2:  "No",
    },
    "CampusHousing": {
          -1: "Not reported",
          -2: "Not applicable",
          1:  "Yes",
          2:  "No",
    },
    "MealPlan": {
          -1: "Not reported",
          -2: "Not applicable",
          1:  "Yes, number of meals in the maximum meal plan offered",
          2:  "Yes, number of meals per week can vary",
          3:  "No",
    },
    "ReligiousAffiliation": {
          -1:  "Not reported",
          -2:  "Not applicable",
          22:  "American Evangelical Lutheran Church",
          24:  "African Methodist Episcopal Zion Church",
          27:  "Assemblies of God Church",
          28:  "Brethren Church",
          30:  "Roman Catholic",
          33:  "Wisconsin Evangelical Lutheran Synod",
          34:  "Christ and Missionary Alliance Church",
          35:  "Christian Reformed Church",
          36:  "Evangelical Congregational Church",
          37:  "Evangelical Covenant Church of America",
          38:  "Evangelical Free Church of America",
          39:  "Evangelical Lutheran Church",
          40:  "International United Pentecostal Church",
          41:  "Free Will Baptist Church",
          42:  "Interdenominational",
          43:  "Mennonite Brethren Church",
          44:  "Moravian Church",
          45:  "North American Baptist",
          47:  "Pentecostal Holiness Church",
          48:  "Christian Churches and Churches of Christ",
          49:  "Reformed Church in America",
          50:  "Episcopal Church, Reformed",
          51:  "African Methodist Episcopal",
          52:  "American Baptist",
          53:  "American Lutheran",
          54:  "Baptist",
          55:  "Christian Methodist Episcopal",
          57:  "Church of God",
          58:  "Church of Brethren",
          59:  "Church of the Nazarene",
          60:  "Cumberland Presbyterian",
          61:  "Christian Church (Disciples of Christ)",
          64:  "Free Methodist",
          65:  "Friends",
          66:  "Presbyterian Church (USA)",
          67:  "Lutheran Church in America",
          68:  "Lutheran Church - Missouri Synod",
          69:  "Mennonite Church",
          71:  "United Methodist",
          73:  "Protestant Episcopal",
          74:  "Churches of Christ",
          75:  "Southern Baptist",
          76:  "United Church of Christ",
          77:  "Protestant, not specified",
          78:  "Multiple Protestant Denomination",
          79:  "Other Protestant",
          80:  "Jewish",
          81:  "Reformed Presbyterian Church",
          84:  "United Brethren Church",
          87:  "Missionary Church Inc",
          88:  "Undenominational",
          89:  "Wesleyan",
          91:  "Greek Orthodox",
          92:  "Russian Orthodox",
          93:  "Unitarian Universalist",
          94:  "Latter Day Saints (Mormon Church)",
          95:  "Seventh Day Adventists",
          97:  "The Presbyterian Church in America",
          99:  "Other (none of the above)",
          100: "Original Free Will Baptist",
          101: "Ecumenical Christian",
          102: "Evangelical Christian",
          103: "Presbyterian",
          104: "Virginia Baptist General Association",
          105: "General Baptist",
    }
}

headers = {
    'UNITID': 'UnitID',
    'INSTNM': 'InstitutionName',
    'ADDR': 'Address',
    'CITY': 'City',
    'STABBR': 'State',
    'ZIP': 'Zip',
    'LOCALE': 'Locale',
    'WEBADDR': 'Website',
    'INSTSIZE': 'InstitutionSize',
    'ICLEVEL': 'Level',
    'HBCU': 'HBCU',
    'ALLONCAM': 'CampusHousingRequired',
    'ROOM': 'CampusHousing',
    'BOARD': 'MealPlan',
    'RELAFFIL': 'ReligiousAffiliation',
    'BAGR150': '6YearGraduationRate',
    'GRRTBK': 'BlackGraduationRate',
    'GRRTHS': 'HispanicGraudationRate',
    'DVADM01': 'PercentAdmitted',
    'ENRFT': 'FulltimeEnrollment',
    'RMINSTTP':'InState',
    'RMOUSTTP': 'OutOfState',
    'PCTENRW': 'PercentWomen',
    'PCTENRBK': 'PercentBlack',
    'PCTENRHS': 'PercentHispanic',
    'PCTENRWH': 'PercentWhite',
    'PGRNT_P': 'PercentPell',
    'FGRNT_P': 'PercentFederalAid',
}

def decode_csv():
    # Use sys.stdin, which takes the dependency listed in the Makefile.
    reader = csv.DictReader(sys.stdin)
    new_header = []

    # Decode the header.
    for h_name in reader.fieldnames:
        new_header.append(headers.get(h_name, None))

    # Use sys.stdout, which takes the target listed in the Makefile.
    writer = csv.DictWriter(sys.stdout, fieldnames=new_header)
    writer.writeheader()

    for row in reader:
        # Decode the header name in the individual row dict.
        row = dict((headers[key], value) for (key, value) in row.items())
        for column in row:
            try:
                value         = row[column]
                decoded_value = decoder[str(column)][int(value)]
                row[column]   = decoded_value
            except KeyError:
                pass

        writer.writerow(row)

if __name__ == "__main__":
    decode_csv()

