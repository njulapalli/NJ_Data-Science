# Import required packages
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join(".", "employee_data1.csv")
#print("file name :"+file_to_load)


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as employeeNewformat_data1:
    reader = csv.reader(employeeNewformat_data1)

    header = next(reader)

# The `Name` column should be split into separate `First Name` and `Last Name` columns.

employee_data1dict = {"first name": [], "last name": []}
    for row in reader:
        first = row[0].split()[0]
        last = row[0].split()[1]
        employee_data1dict["first name"].append(first)
        employee_data1dict["last name"].append(last)

with open('new.csv', 'wb') as f:
    w = csv.DictWriter(f, employee_data1dict.keys())
    w.writeheader()
    w.writerows(employee_data1dict)



#  The `DOB` data should be re-written into `MM/DD/YYYY` format.

#  The `SSN` data should be re-written such that the first five numbers are hidden from view.

#  The `State` data should be re-written as simple two-letter abbreviations.

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
