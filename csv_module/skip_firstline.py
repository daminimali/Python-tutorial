import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    
    for line in csv_reader:
        print(line[2])
'''O/p:
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
john-doe@bogusemail.com
maryjacobs@bogusemail.com
davesmith@bogusemail.com
janestuart@bogusemail.com
tomwright@bogusemail.com
steverobinson@bogusemail.com
nicolejacobs@bogusemail.com
janewright@bogusemail.com
janedoe@bogusemail.com
kurtwright@bogusemail.com
kurtrobinson@bogusemail.com
janejenkins@bogusemail.com
neilrobinson@bogusemail.com
tompatterson@bogusemail.com
samjenkins@bogusemail.com
stevestuart@bogusemail.com
maggiepatterson@bogusemail.com
maggiestuart@bogusemail.com
janedoe@bogusemail.com
stevepatterson@bogusemail.com
davesmith@bogusemail.com
samwilks@bogusemail.com
kurtjefferson@bogusemail.com
samstuart@bogusemail.com
janestuart@bogusemail.com
davedavis@bogusemail.com
sampatterson@bogusemail.com
tomjefferson@bogusemail.com
janestuart@bogusemail.com
maggiejefferson@bogusemail.com
marywilks@bogusemail.com
neilpatterson@bogusemail.com
coreydavis@bogusemail.com
stevejacobs@bogusemail.com
janejenkins@bogusemail.com
johnjacobs@bogusemail.com
neilsmith@bogusemail.com
coreywilks@bogusemail.com
coreysmith@bogusemail.com
marypatterson@bogusemail.com
janestuart@bogusemail.com
travisarnold@bogusemail.com
johnrobinson@bogusemail.com
travisarnold@bogusemail.com

Process finished with exit code 0
'''
import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
