# Case Study 26: Nested Loop Examination Seating Generator

print("EXAMINATION SEATING PLAN")
rows = 4
columns = 5
reserved = [(1, 3), (3, 2)]
reserved_count = 0

for row in range(1, rows + 1):
    for column in range(1, columns + 1):
        if (row, column) in reserved:
            print("R", end=" ")
            reserved_count += 1
        else:
            print("A", end=" ")
    print()

total_seats = rows * columns
available = total_seats - reserved_count

print("Total Seats:", total_seats)
print("Reserved Seats:", reserved_count)
print("Available Seats:", available)
