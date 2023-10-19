import sys

lines = []  # Holds the lines inside the input.txt file.
message_id = []  # Holds the message ids.
mydict = {}  # Holds the message id as value and packet id and message together as key.


# This is the function that writes to the output file when called.
def write(output):
    with open(sys.argv[2], 'a') as f:
        f.write(output)


with open(sys.argv[1], 'r') as reading:
    for line in reading:
        line = line.split('\t')
        if "\n" not in line[2]:  # Adds new line to the line (possibly the last line) if it doesn't already have one.
            new_line = [line[0], line[1], line[2] + "\n"]
            lines.append(new_line)
        else:
            lines.append(line)
for data in lines:
    if data[0] not in message_id:
        message_id.append(data[0])
        message_id.sort()
for data in message_id:
    mydict[data] = []
for data in lines:
    for num in message_id:
        if num == data[0]:
            mydict[num].append(data[1] + data[2])  # The packet id and message are connected to sort the order easily.
            mydict[num].sort()
# We set a counter to find each message number.
counter = 0
for num in message_id:
    counter += 1
    write("Message\t{}\n".format(counter))
    for i in range(len(mydict[num])):
        write("{}\t{}\t{}".format(num, mydict[num][i][0], mydict[num][i][1:]))
