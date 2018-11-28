
# Import required packages
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
#print("file name :"+file_to_load)


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as bank_data:
    reader = csv.reader(bank_data)

    header = next(reader)

    #Define the dictionary
    dict_bankdata = {}
    # Loop through each row, and add row to the dictionary

    key = ""
    profit_loss = 0
    for row in reader:
       # print("Line from file year-month= "  + row[0] + " profit/loss=" + row[1])
       dict_bankdata[row[0]] = int(row[1])

     # The total number of months included in the dataset
    Total_Months = 0

  # The total net amount of "Profit/Losses" over the entire period
    Total_Profit_loss = 0

  # The average change in "Profit/Losses" between months over the entire period
    Avg_change = 0
  # The greatest increase in profits (date and amount) over the entire period
    Greatest_Increase_Date = ""
    Greatest_Increase_Value = 0

  # The greatest decrease in losses (date and amount) over the entire period
    Greatest_Decrease_Date = ""
    Greatest_Decrease_Value = 0

    previous_profit_loss = dict_bankdata["Jan-2010"]
    total_change = 0
    for dict_key_date, cur_profit_loss in dict_bankdata.items():
        Total_Profit_loss = Total_Profit_loss + cur_profit_loss

        change = cur_profit_loss - previous_profit_loss
        total_change = total_change + change

        if(Greatest_Increase_Value < change):
            Greatest_Increase_Value = change
            Greatest_Increase_Date = dict_key_date

        if (Greatest_Decrease_Value > change):
            Greatest_Decrease_Value = change
            Greatest_Decrease_Date = dict_key_date

        previous_profit_loss = cur_profit_loss

    Total_Months = len(dict_bankdata)
    Avg_change = total_change / (Total_Months - 1)
    # Output Strings:

    str1 = "Financial Analysis"
    str2 = "----------------------------"
    str3 = "Total Months: " + str(Total_Months)
    str4 = "Total: $" + str(Total_Profit_loss)
    str5 = "Average  Change: $" + str(Avg_change)
    str6 = "Greatest Increase in Profits: " + Greatest_Increase_Date + " ($" + str(Greatest_Increase_Value) + ")"
    str7 = "Greatest Decrease in Profits: " + Greatest_Decrease_Date + " ($" + str(Greatest_Decrease_Value) + ")"

    print (str1 + "\n"
        + str2 + "\n"
        + str3 + "\n"
        + str4 + "\n"
        + str5 + "\n"
        + str6 + "\n"
        + str7 + "\n")

Output_Text = input("Would you like to export a text file of the results? If yes, type 'y':")
if Output_Text == 'y':
    f = open('PythonHW_PyBank_Results.txt','w')
    f.write (str1 + "\n"
           + str2 + "\n"
           + str3 + "\n"
           + str4 + "\n"
           + str5 + "\n"
           + str6 + "\n"
           + str7 + "\n")
    f.close()
else:
    print("Okay, a text file of the results will not be exported :)")

