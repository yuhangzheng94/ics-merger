from os import listdir
from datetime import datetime

# declare the list of ics files to be merged
files = list()
candidates = listdir('to_be_merged')
for candidate in candidates:
    if candidate.endswith(".ics"):
        files.append(candidate)

# create and open the master ics file
now = datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print('[{timestamp}] Merging started.'.format(timestamp=now_str))
master_file_str = "merged-calendar-" + now_str + ".ics"
master_file = open(master_file_str, "a")
master_file.write("""BEGIN:VCALENDAR
PRODID:-//github.com/yuhangzheng94//ICS Merger 1.0//EN
VERSION:2.0
""")

# append each event to the master ics file

for file in files:
    file_str = "to_be_merged/" + file
    f = open(file_str, "r")
    line = f.readline()
    while not line.startswith("BEGIN:VEVENT"):
        line = f.readline()
    while not line.startswith("END:VEVENT"):
        master_file.write(line)
        line = f.readline()
    master_file.write(line)
    f.close()
    print("\t" + file + " has been merged.")

# close the master ics file
master_file.write("""END:VCALENDAR
""")

master_file.close()

print('[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "] All events have been merged into \"" + master_file_str + "\".")