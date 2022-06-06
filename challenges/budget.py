# code per budget.py assignment
def calc_bills():
  my_bills = { 'Electric': 120.00, 'Rent': 1200.00, 'Water/Sewer': 60.00, 
              'Car Insurance': 75.00, 'Phone:': 65.00 }
  total = 0
  for i in my_bills:
    total += my_bills[i]
  owed = 'The total owed for bills this month is: ${}'.format(total)
  return owed