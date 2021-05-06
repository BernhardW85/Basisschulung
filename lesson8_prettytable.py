from prettytable import PrettyTable

table = PrettyTable(["name", "ps"])

table.add_row(["audi", 500])
table.add_row(["vw", 400])
table.add_row(["porsche", 500])
table.add_row(["ferrari", 500])

print(table)