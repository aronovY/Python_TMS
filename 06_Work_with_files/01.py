import csv
import json

"""The program converts data from a .json file to a .csv file."""


def csv_writer(data, path):
    field_names = []
    for row in data:  # Get column names
        for key in row:
            if key not in field_names:
                field_names.append(key)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def json_reader(file):  # Method for reading data from a .json file
    with open(file, 'r') as json_file:
        json_str = json_file.read()  # Save json data in a string
        obj_data = json.loads(json_str)  # Deserialize the data
        return obj_data  # We return the received data


if __name__ == '__main__':
    path_csv = 'csv_file.csv'  # Path on .csv file
    path_json = 'json_file.json'  # Path on .json file
    obj = json_reader(path_json)
    csv_writer(obj, path_csv)
