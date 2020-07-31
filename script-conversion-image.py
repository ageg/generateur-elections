import csv
import requests

PHOTO_STRING = "Photo"
GOOGLE_DRIVE_API_URL = "https://drive.google.com/uc?export=view&id="

with open("example/executif.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    photo_column_index = 0;
    for line_count, row in enumerate(csv_reader):
        if line_count == 0:
            for index, column in enumerate(row):
              if column == PHOTO_STRING:
                photo_column_index = index
        else:
            photo_id = row[photo_column_index].split("id=")[1]
            public_photo_url =  GOOGLE_DRIVE_API_URL + photo_id

            # Check if the photo is public
            response = requests.get(public_photo_url)
            print({response.status_code})