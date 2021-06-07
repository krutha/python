
open_file = open ('CupcakeInvoices.csv')

 for row in open_file:
     print (row)

for row in open_file:
  values = row.split(',')
  mul = int(values[3]) * float(values[4])
  print(round(mul,1)) # to limt the float values not exceed , we can use the round()
total = 0

for row in open_file:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))

print(total)
open_file.close()

# if values[2]== chocolate 
#  mul = int(values[3]) * float(values[4])
#  print(round(mul,1))
#  total = total +mul

# for line in open_file:
#   line = line.strip()
#   values = line.split(',')
#   print(values)
#   for value in values:
#     if value == "chocolate":
#       total_chocolate += 1
#     elif value == "Vanilla":
#       total_Vanilla += 1
#     elif value == "Strawberry:
#       total_Strawberry += 1
# print("chocolate", total_chocolate)
# print("Vanilla", total_vanilla)
# print("Strawberry", total_strawberry)


