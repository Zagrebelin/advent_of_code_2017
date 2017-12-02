"""
The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right
track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the
largest value and the smallest value; the checksum is the sum of all of these differences.
"""
data = open('data//day_02').read()
ch = 0
for line in data.split('\n'):
    ch += max(map(int, line.split()))-min(map(int, line.split()))

print(ch)
