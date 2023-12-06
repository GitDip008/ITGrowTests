import gspread

sa = gspread.service_account(filename="creds.json")

sh = sa.open("demo")    # Defining the google sheet that we'll work on
wks = sh.worksheet("Sheet1")    # Defining the worksheet

data = wks.get_all_records()

print("\nOriginal Data:")
for row in data:
    print(row)

# Update values in the spreadsheet
cell_range = 'C2'  # Cell to update
new_value = '999-888-7777'  # New value for the cell

# Use named arguments to update the cell
wks.update(range_name=cell_range, values=[[new_value]])

# Append a new row to the spreadsheet
new_row = ['Eve', 'eve@example.com', '333-444-5555']  # Data for the new row
wks.append_row(new_row)

# Fetch updated data after modifications
updated_data = wks.get_all_records()
print("\nUpdated data:")
for row in updated_data:
    print(row)