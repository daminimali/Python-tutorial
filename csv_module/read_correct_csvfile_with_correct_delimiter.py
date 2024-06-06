import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

'''D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
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
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)

''' 
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
['first_name,last_name,email']
['John,Doe,john-doe@bogusemail.com']
['Mary,Smith-Robinson,maryjacobs@bogusemail.com']
['Dave,Smith,davesmith@bogusemail.com']
['Jane,Stuart,janestuart@bogusemail.com']
['Tom,Wright,tomwright@bogusemail.com']
['Steve,Robinson,steverobinson@bogusemail.com']
['Nicole,Jacobs,nicolejacobs@bogusemail.com']
['Jane,Wright,janewright@bogusemail.com']
['Jane,Doe,janedoe@bogusemail.com']
['Kurt,Wright,kurtwright@bogusemail.com']
['Kurt,Robinson,kurtrobinson@bogusemail.com']
['Jane,Jenkins,janejenkins@bogusemail.com']
['Neil,Robinson,neilrobinson@bogusemail.com']
['Tom,Patterson,tompatterson@bogusemail.com']
['Sam,Jenkins,samjenkins@bogusemail.com']
['Steve,Stuart,stevestuart@bogusemail.com']
['Maggie,Patterson,maggiepatterson@bogusemail.com']
['Maggie,Stuart,maggiestuart@bogusemail.com']
['Jane,Doe,janedoe@bogusemail.com']
['Steve,Patterson,stevepatterson@bogusemail.com']
['Dave,Smith,davesmith@bogusemail.com']
['Sam,Wilks,samwilks@bogusemail.com']
['Kurt,Jefferson,kurtjefferson@bogusemail.com']
['Sam,Stuart,samstuart@bogusemail.com']
['Jane,Stuart,janestuart@bogusemail.com']
['Dave,Davis,davedavis@bogusemail.com']
['Sam,Patterson,sampatterson@bogusemail.com']
['Tom,Jefferson,tomjefferson@bogusemail.com']
['Jane,Stuart,janestuart@bogusemail.com']
['Maggie,Jefferson,maggiejefferson@bogusemail.com']
['Mary,Wilks,marywilks@bogusemail.com']
['Neil,Patterson,neilpatterson@bogusemail.com']
['Corey,Davis,coreydavis@bogusemail.com']
['Steve,Jacobs,stevejacobs@bogusemail.com']
['Jane,Jenkins,janejenkins@bogusemail.com']
['John,Jacobs,johnjacobs@bogusemail.com']
['Neil,Smith,neilsmith@bogusemail.com']
['Corey,Wilks,coreywilks@bogusemail.com']
['Corey,Smith,coreysmith@bogusemail.com']
['Mary,Patterson,marypatterson@bogusemail.com']
['Jane,Stuart,janestuart@bogusemail.com']
['Travis,Arnold,travisarnold@bogusemail.com']
['John,Robinson,johnrobinson@bogusemail.com']
['Travis,Arnold,travisarnold@bogusemail.com']

Process finished with exit code 0
'''
import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
'''D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
{'first_name': 'John', 'last_name': 'Doe', 'email': 'john-doe@bogusemail.com'}
{'first_name': 'Mary', 'last_name': 'Smith-Robinson', 'email': 'maryjacobs@bogusemail.com'}
{'first_name': 'Dave', 'last_name': 'Smith', 'email': 'davesmith@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Stuart', 'email': 'janestuart@bogusemail.com'}
{'first_name': 'Tom', 'last_name': 'Wright', 'email': 'tomwright@bogusemail.com'}
{'first_name': 'Steve', 'last_name': 'Robinson', 'email': 'steverobinson@bogusemail.com'}
{'first_name': 'Nicole', 'last_name': 'Jacobs', 'email': 'nicolejacobs@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Wright', 'email': 'janewright@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Doe', 'email': 'janedoe@bogusemail.com'}
{'first_name': 'Kurt', 'last_name': 'Wright', 'email': 'kurtwright@bogusemail.com'}
{'first_name': 'Kurt', 'last_name': 'Robinson', 'email': 'kurtrobinson@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Jenkins', 'email': 'janejenkins@bogusemail.com'}
{'first_name': 'Neil', 'last_name': 'Robinson', 'email': 'neilrobinson@bogusemail.com'}
{'first_name': 'Tom', 'last_name': 'Patterson', 'email': 'tompatterson@bogusemail.com'}
{'first_name': 'Sam', 'last_name': 'Jenkins', 'email': 'samjenkins@bogusemail.com'}
{'first_name': 'Steve', 'last_name': 'Stuart', 'email': 'stevestuart@bogusemail.com'}
{'first_name': 'Maggie', 'last_name': 'Patterson', 'email': 'maggiepatterson@bogusemail.com'}
{'first_name': 'Maggie', 'last_name': 'Stuart', 'email': 'maggiestuart@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Doe', 'email': 'janedoe@bogusemail.com'}
{'first_name': 'Steve', 'last_name': 'Patterson', 'email': 'stevepatterson@bogusemail.com'}
{'first_name': 'Dave', 'last_name': 'Smith', 'email': 'davesmith@bogusemail.com'}
{'first_name': 'Sam', 'last_name': 'Wilks', 'email': 'samwilks@bogusemail.com'}
{'first_name': 'Kurt', 'last_name': 'Jefferson', 'email': 'kurtjefferson@bogusemail.com'}
{'first_name': 'Sam', 'last_name': 'Stuart', 'email': 'samstuart@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Stuart', 'email': 'janestuart@bogusemail.com'}
{'first_name': 'Dave', 'last_name': 'Davis', 'email': 'davedavis@bogusemail.com'}
{'first_name': 'Sam', 'last_name': 'Patterson', 'email': 'sampatterson@bogusemail.com'}
{'first_name': 'Tom', 'last_name': 'Jefferson', 'email': 'tomjefferson@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Stuart', 'email': 'janestuart@bogusemail.com'}
{'first_name': 'Maggie', 'last_name': 'Jefferson', 'email': 'maggiejefferson@bogusemail.com'}
{'first_name': 'Mary', 'last_name': 'Wilks', 'email': 'marywilks@bogusemail.com'}
{'first_name': 'Neil', 'last_name': 'Patterson', 'email': 'neilpatterson@bogusemail.com'}
{'first_name': 'Corey', 'last_name': 'Davis', 'email': 'coreydavis@bogusemail.com'}
{'first_name': 'Steve', 'last_name': 'Jacobs', 'email': 'stevejacobs@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Jenkins', 'email': 'janejenkins@bogusemail.com'}
{'first_name': 'John', 'last_name': 'Jacobs', 'email': 'johnjacobs@bogusemail.com'}
{'first_name': 'Neil', 'last_name': 'Smith', 'email': 'neilsmith@bogusemail.com'}
{'first_name': 'Corey', 'last_name': 'Wilks', 'email': 'coreywilks@bogusemail.com'}
{'first_name': 'Corey', 'last_name': 'Smith', 'email': 'coreysmith@bogusemail.com'}
{'first_name': 'Mary', 'last_name': 'Patterson', 'email': 'marypatterson@bogusemail.com'}
{'first_name': 'Jane', 'last_name': 'Stuart', 'email': 'janestuart@bogusemail.com'}
{'first_name': 'Travis', 'last_name': 'Arnold', 'email': 'travisarnold@bogusemail.com'}
{'first_name': 'John', 'last_name': 'Robinson', 'email': 'johnrobinson@bogusemail.com'}
{'first_name': 'Travis', 'last_name': 'Arnold', 'email': 'travisarnold@bogusemail.com'}

Process finished with exit code 0
'''
import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])

'''
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


  
