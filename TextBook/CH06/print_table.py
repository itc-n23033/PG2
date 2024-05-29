def print_table(table_data):
    max_length = max(len(item) for table in table_data for item in table)
    for row in zip(*table_data):
        print(" ".join(item.rjust(max_length) for item in row))

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
