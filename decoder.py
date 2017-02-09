import csv
import sys

decoder = {
    "state": {
        "AK": "Alaska",
        "AL": "Alabama",
        "AR": "Arkansas",
        "AS": "American Samoa",
        "AZ": "Arizona",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DC": "District of Columbia",
        "DE": "Delaware",
        "FL": "Florida",
        "FM": "Federated States of Micronesia",
        "GA": "Georgia",
        "GU": "Guam",
        "HI": "Hawaii",
        "IA": "Iowa",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "MA": "Massachusetts",
        "MD": "Maryland",
        "ME": "Maine",
        "MH": "Marshall Islands",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MO": "Missouri",
        "MP": "Northern Marianas",
        "MS": "Mississippi",
        "MT": "Montana",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "NE": "Nebraska",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NV": "Nevada",
        "NY": "New York",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "PR": "Puerto Rico",
        "PW": "Palau",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VA": "Virginia",
        "VI": "Virgin Islands",
        "VT": "Vermont",
        "WA": "Washington",
        "WI": "Wisconsin",
        "WV": "West Virginia",
        "WY": "Wyoming",
    },
    "locale": {
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
    "size": {
        -1: "Not reported",
        -2: "Not applicable",
        1: "Under 1,000",
        2: "1,000 - 4,999",
        3: "5,000 - 9,999",
        4: "10,000 - 19,999",
        5: "20,000 and above",
    },
    "level": {
         -3: "Not available",
         1:  "Four or more years",
         2:  "At least 2 but less than 4 years",
         3:  "Less than 2 years (below associate)",
    },
    "hbcu": {
        1: "Yes",
        2: "No",
    },
    "campus_housing_required": {
          -1: "Not reported",
          -2: "Not applicable",
          1:  "Yes",
          2:  "No",
    },
    "campus_housing": {
          -1: "Not reported",
          -2: "Not applicable",
          1:  "Yes",
          2:  "No",
    },
    "meal_plan": {
          -1: "Not reported",
          -2: "Not applicable",
          1:  "Yes, number of meals in the maximum meal plan offered",
          2:  "Yes, number of meals per week can vary",
          3:  "No",
    },
    "religious_affiliation": {
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
    'UNITID': 'unit_id',
    'INSTNM': 'name',
    'ADDR': 'address',
    'CITY': 'city',
    'STABBR': 'state',
    'ZIP': 'zipcode',
    'LOCALE': 'locale',
    'WEBADDR': 'website',
    'INSTSIZE': 'size',
    'ICLEVEL': 'level',
    'HBCU': 'hbcu',
    'ALLONCAM': 'campus_housing_required',
    'ROOM': 'campus_housing',
    'BOARD': 'meal_plan',
    'RELAFFIL': 'religious_affiliation',
    'BAGR150': 'six_year_grad_rate',
    'GRRTBK': 'black_grad_rate',
    'GRRTHS': 'hispanic_grad_rate',
    'DVADM01': 'percent_admitted',
    'ENRFT': 'full_time',
    'RMINSTTP':'in_state',
    'RMOUSTTP': 'out_of_state',
    'PCTENRW': 'percent_women',
    'PCTENRBK': 'percent_black',
    'PCTENRHS': 'percent_hispanic',
    'PCTENRWH': 'percent_white',
    'PGRNT_P': 'percent_pell',
    'FGRNT_P': 'percent_federal_aid',
    'ADMSSN': 'admission',
    'APPLCN': 'application',
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
                value = row[column]

                if value.lstrip("-").isdigit():
                  decoded_value = decoder[str(column)][int(value)]
                else:
                  decoded_value = decoder[str(column)][value]

                row[column]   = decoded_value
            except KeyError:
                pass
            except ValueError:
                pass

        writer.writerow(row)

if __name__ == "__main__":
    decode_csv()

