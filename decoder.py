import csv

file_to_decode = 'build/schools_raw.csv'
decoder = {
    "LOCALE": {
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
    }
}


def decode_csv():
    with open(file_to_decode) as csvfile:
        reader   = csv.DictReader(csvfile)
        rows_collection = []
        for row in reader:
            for column in row:
                try:
                    value         = row[column]
                    decoded_value = decoder[str(column)][int(value)]
                    row[column]   = decoded_value

                    rows_collection.append(row)
                except KeyError:
                    pass

        output = open('schools_processed.csv', 'wb')
        writer = csv.DictWriter(output, row.keys())
        writer.writeheader()
        writer.writerows(rows_collection)

if __name__ == "__main__":
    decode_csv()