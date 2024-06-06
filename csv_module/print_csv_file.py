import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader)

'''O/P:
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
<_csv.reader object at 0x000001D6AC8BE080>

Process finished with exit code 0'''

import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)
'''O/p:
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
['first_name', 'last_name', 'email']
['John', 'Doe', 'john-doe@bogusemail.com']
['Mary', 'Smith-Robinson', 'maryjacobs@bogusemail.com']
['Dave', 'Smith', 'davesmith@bogusemail.com']
['Jane', 'Stuart', 'janestuart@bogusemail.com']
['Tom', 'Wright', 'tomwright@bogusemail.com']
['Steve', 'Robinson', 'steverobinson@bogusemail.com']
['Nicole', 'Jacobs', 'nicolejacobs@bogusemail.com']
['Jane', 'Wright', 'janewright@bogusemail.com']
['Jane', 'Doe', 'janedoe@bogusemail.com']
['Kurt', 'Wright', 'kurtwright@bogusemail.com']
['Kurt', 'Robinson', 'kurtrobinson@bogusemail.com']
['Jane', 'Jenkins', 'janejenkins@bogusemail.com']
['Neil', 'Robinson', 'neilrobinson@bogusemail.com']
['Tom', 'Patterson', 'tompatterson@bogusemail.com']
['Sam', 'Jenkins', 'samjenkins@bogusemail.com']
['Steve', 'Stuart', 'stevestuart@bogusemail.com']
['Maggie', 'Patterson', 'maggiepatterson@bogusemail.com']
['Maggie', 'Stuart', 'maggiestuart@bogusemail.com']
['Jane', 'Doe', 'janedoe@bogusemail.com']
['Steve', 'Patterson', 'stevepatterson@bogusemail.com']
['Dave', 'Smith', 'davesmith@bogusemail.com']
['Sam', 'Wilks', 'samwilks@bogusemail.com']
['Kurt', 'Jefferson', 'kurtjefferson@bogusemail.com']
['Sam', 'Stuart', 'samstuart@bogusemail.com']
['Jane', 'Stuart', 'janestuart@bogusemail.com']
['Dave', 'Davis', 'davedavis@bogusemail.com']
['Sam', 'Patterson', 'sampatterson@bogusemail.com']
['Tom', 'Jefferson', 'tomjefferson@bogusemail.com']
['Jane', 'Stuart', 'janestuart@bogusemail.com']
['Maggie', 'Jefferson', 'maggiejefferson@bogusemail.com']
['Mary', 'Wilks', 'marywilks@bogusemail.com']
['Neil', 'Patterson', 'neilpatterson@bogusemail.com']
['Corey', 'Davis', 'coreydavis@bogusemail.com']
['Steve', 'Jacobs', 'stevejacobs@bogusemail.com']
['Jane', 'Jenkins', 'janejenkins@bogusemail.com']
['John', 'Jacobs', 'johnjacobs@bogusemail.com']
['Neil', 'Smith', 'neilsmith@bogusemail.com']
['Corey', 'Wilks', 'coreywilks@bogusemail.com']
['Corey', 'Smith', 'coreysmith@bogusemail.com']
['Mary', 'Patterson', 'marypatterson@bogusemail.com']
['Jane', 'Stuart', 'janestuart@bogusemail.com']
['Travis', 'Arnold', 'travisarnold@bogusemail.com']
['John', 'Robinson', 'johnrobinson@bogusemail.com']
['Travis', 'Arnold', 'travisarnold@bogusemail.com']

Process finished with exit code 0
'''
import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2])
'''o/p:
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
email
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
