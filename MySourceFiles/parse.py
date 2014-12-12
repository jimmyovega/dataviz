"""Data Visualization Parse File by Jimmy Vega"""

import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file,delimiter):
    """Parses a raw CSV file into a JSON-line object"""

    # Open CSV file
    opened_file = open(raw_file)

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Initialize an array to build a data structure to return parsed_data
    parsed_data = []

    # This will get the header columns and put it in the fields variable
    fields = csv_data.next()
    for row in csv_data:
        parsed_data.append(dict(zip(fields,row)))

    # Close CSV file
    opened_file.close()

    return parsed_data

def main():
    #Call our parse function and give the filename and delimiter as arguments
    new_data = parse(MY_FILE,",")

    #Print out the data
    print new_data

if __name__ == "__main__":
    main()
