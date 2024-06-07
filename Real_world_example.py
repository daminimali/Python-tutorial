import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    print(csv_data)

'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
<_csv.reader object at 0x000002567368E080>

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    print(list(csv_data))
'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
[['FirstName', 'LastName', 'Email', 'Pledge', 'Lifetime', 'Status', 'Country', 'Start'], ['1 + Reward', 'Description I will add your name to the contributors page on my website.\n\nYou will also be eligible for Patreon-only rewards. I will occasionally give away books that I have read, and will choose a Patron at random to receive those.', '', '', '', '', '', ''], ['John', 'Doe', 'johndoe@bogusemail.com', '10.00', '20.00', 'Ok', '', '2017-05-06 21:28:06.183108'], ['Dave', 'Smith', 'davesmith@bogusemail.com', '5.00', '10.00', 'Ok', '', '2017-05-29 16:13:58.318920'], ['Mary', 'Jacobs', 'maryjacobs@bogusemail.com', '5.00', '10.00', 'Ok', '', '2017-05-14 07:37:01.074648'], ['Jane', 'Stuart', 'janestuart@bogusemail.com', '5.00', '25.00', 'Ok', '', '2016-12-30 18:12:13'], ['Tom', 'Wright', 'tomwright@bogusemail.com', '5.00', '15.00', 'Ok', '', '2017-04-14 04:02:06.658439'], ['Steve', 'Robinson', 'steverobinson@bogusemail.com', '5.00', '20.00', 'Ok', '', '2017-03-17 02:20:14'], ['Nicole', 'Jacobs', 'nicolejacobs@bogusemail.com', '5.00', '20.00', 'Ok', '', '2017-03-12 17:07:29'], ['Jane', 'Wright', 'janewright@bogusemail.com', '5.00', '25.00', '', '', '2017-01-14 17:40:06'], ['Jane', 'Doe', 'janedoe@bogusemail.com', '2.50', '5.00', 'Ok', '', '2017-05-14 11:20:50.798440'], ['Kurt', 'Wright', 'kurtwright@bogusemail.com', '2.00', '2.00', 'Ok', '', '2017-06-23 21:12:15.662157'], ['Kurt', 'Robinson', 'kurtrobinson@bogusemail.com', '2.00', '4.00', 'Ok', '', '2017-05-03 03:18:54.877885'], ['Jane', 'Jenkins', 'janejenkins@bogusemail.com', '2.00', '8.00', 'Ok', '', '2017-03-23 16:37:47.708634'], ['Neil', 'Robinson', 'neilrobinson@bogusemail.com', '1.50', '3.00', 'Ok', '', '2017-05-26 19:59:51.013984'], ['Tom', 'Patterson', 'tompatterson@bogusemail.com', '1.34', '4.02', 'Ok', '', '2017-04-27 01:55:12.313799'], ['Sam', 'Jenkins', 'samjenkins@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-16 02:34:47.674287'], ['Steve', 'Stuart', 'stevestuart@bogusemail.com', '1.00', '1.00', 'Ok', '', '2017-06-12 03:32:00.706554'], ['Maggie', 'Patterson', 'maggiepatterson@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-26 01:23:14.097393'], ['Maggie', 'Stuart', 'maggiestuart@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-19 23:11:08.624354'], ['Jane', 'Doe', 'janedoe@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-15 19:40:17.044921'], ['Steve', 'Patterson', 'stevepatterson@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-09 17:14:23.591656'], ['Dave', 'Smith', 'davesmith@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-01 18:35:10.731005'], ['Sam', 'Wilks', 'samwilks@bogusemail.com', '1.00', '4.00', 'Ok', '', '2017-03-01 09:40:56'], ['Kurt', 'Jefferson', 'kurtjefferson@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-24 08:23:05'], ['Sam', 'Stuart', 'samstuart@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-12 00:14:31'], ['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-06 14:52:28'], ['Dave', 'Davis', 'davedavis@bogusemail.com', '1.00', '0.00', '', '', '2016-11-18 01:37:25'], ['Sam', 'Patterson', 'sampatterson@bogusemail.com', '1.00', '8.00', 'Ok', '', '2016-11-01 11:27:17'], ['Tom', 'Jefferson', 'tomjefferson@bogusemail.com', '1.00', '10.00', 'Ok', '', '2016-09-27 09:56:48'], ['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '7.00', '', '', '2016-08-09 14:42:25'], ['Maggie', 'Jefferson', 'maggiejefferson@bogusemail.com', '1.00', '12.00', 'Ok', '', '2016-07-26 05:02:16'], ['No Reward', 'Description: (None for No Reward)', '', '', '', '', '', ''], ['Mary', 'Wilks', 'marywilks@bogusemail.com', '20.00', '60.00', 'Ok', '', '2017-04-21 02:44:43.395224'], ['Neil', 'Patterson', 'neilpatterson@bogusemail.com', '10.00', '80.00', 'Ok', '', '2016-11-12 17:49:37'], ['Corey', 'Davis', 'coreydavis@bogusemail.com', '6.00', '90.00', 'Ok', '', '2016-04-01 15:19:52'], ['Steve', 'Jacobs', 'stevejacobs@bogusemail.com', '5.00', '21.00', 'Ok', '', '2017-01-04 19:38:44'], ['Jane', 'Jenkins', 'janejenkins@bogusemail.com', '5.00', '30.00', 'Ok', '', '2017-01-15 17:24:39'], ['John', 'Jacobs', 'johnjacobs@bogusemail.com', '3.14', '34.54', 'Ok', '', '2016-08-23 16:09:25'], ['Neil', 'Smith', 'neilsmith@bogusemail.com', '3.00', '24.00', 'Ok', '', '2016-11-28 02:57:48'], ['Corey', 'Wilks', 'coreywilks@bogusemail.com', '2.00', '8.00', 'Ok', '', '2017-03-26 20:13:08.207869'], ['Corey', 'Smith', 'coreysmith@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-05 01:50:35.171076'], ['Mary', 'Patterson', 'marypatterson@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-04 18:05:23.052059'], ['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-21 19:42:36.098523'], ['Travis', 'Arnold', 'travisarnold@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-19 08:04:33.428559'], ['John', 'Robinson', 'johnrobinson@bogusemail.com', '1.00', '4.00', 'Ok', '', '2017-03-30 14:59:33.850333'], ['Travis', 'Arnold', 'travisarnold@bogusemail.com', '1.00', '6.00', 'Ok', '', '2017-01-28 22:02:57']]

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    for line in csv_data:
        print(line)
'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
['FirstName', 'LastName', 'Email', 'Pledge', 'Lifetime', 'Status', 'Country', 'Start']
['1 + Reward', 'Description I will add your name to the contributors page on my website.\n\nYou will also be eligible for Patreon-only rewards. I will occasionally give away books that I have read, and will choose a Patron at random to receive those.', '', '', '', '', '', '']
['John', 'Doe', 'johndoe@bogusemail.com', '10.00', '20.00', 'Ok', '', '2017-05-06 21:28:06.183108']
['Dave', 'Smith', 'davesmith@bogusemail.com', '5.00', '10.00', 'Ok', '', '2017-05-29 16:13:58.318920']
['Mary', 'Jacobs', 'maryjacobs@bogusemail.com', '5.00', '10.00', 'Ok', '', '2017-05-14 07:37:01.074648']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '5.00', '25.00', 'Ok', '', '2016-12-30 18:12:13']
['Tom', 'Wright', 'tomwright@bogusemail.com', '5.00', '15.00', 'Ok', '', '2017-04-14 04:02:06.658439']
['Steve', 'Robinson', 'steverobinson@bogusemail.com', '5.00', '20.00', 'Ok', '', '2017-03-17 02:20:14']
['Nicole', 'Jacobs', 'nicolejacobs@bogusemail.com', '5.00', '20.00', 'Ok', '', '2017-03-12 17:07:29']
['Jane', 'Wright', 'janewright@bogusemail.com', '5.00', '25.00', '', '', '2017-01-14 17:40:06']
['Jane', 'Doe', 'janedoe@bogusemail.com', '2.50', '5.00', 'Ok', '', '2017-05-14 11:20:50.798440']
['Kurt', 'Wright', 'kurtwright@bogusemail.com', '2.00', '2.00', 'Ok', '', '2017-06-23 21:12:15.662157']
['Kurt', 'Robinson', 'kurtrobinson@bogusemail.com', '2.00', '4.00', 'Ok', '', '2017-05-03 03:18:54.877885']
['Jane', 'Jenkins', 'janejenkins@bogusemail.com', '2.00', '8.00', 'Ok', '', '2017-03-23 16:37:47.708634']
['Neil', 'Robinson', 'neilrobinson@bogusemail.com', '1.50', '3.00', 'Ok', '', '2017-05-26 19:59:51.013984']
['Tom', 'Patterson', 'tompatterson@bogusemail.com', '1.34', '4.02', 'Ok', '', '2017-04-27 01:55:12.313799']
['Sam', 'Jenkins', 'samjenkins@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-16 02:34:47.674287']
['Steve', 'Stuart', 'stevestuart@bogusemail.com', '1.00', '1.00', 'Ok', '', '2017-06-12 03:32:00.706554']
['Maggie', 'Patterson', 'maggiepatterson@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-26 01:23:14.097393']
['Maggie', 'Stuart', 'maggiestuart@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-19 23:11:08.624354']
['Jane', 'Doe', 'janedoe@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-15 19:40:17.044921']
['Steve', 'Patterson', 'stevepatterson@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-09 17:14:23.591656']
['Dave', 'Smith', 'davesmith@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-01 18:35:10.731005']
['Sam', 'Wilks', 'samwilks@bogusemail.com', '1.00', '4.00', 'Ok', '', '2017-03-01 09:40:56']
['Kurt', 'Jefferson', 'kurtjefferson@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-24 08:23:05']
['Sam', 'Stuart', 'samstuart@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-12 00:14:31']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-06 14:52:28']
['Dave', 'Davis', 'davedavis@bogusemail.com', '1.00', '0.00', '', '', '2016-11-18 01:37:25']
['Sam', 'Patterson', 'sampatterson@bogusemail.com', '1.00', '8.00', 'Ok', '', '2016-11-01 11:27:17']
['Tom', 'Jefferson', 'tomjefferson@bogusemail.com', '1.00', '10.00', 'Ok', '', '2016-09-27 09:56:48']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '7.00', '', '', '2016-08-09 14:42:25']
['Maggie', 'Jefferson', 'maggiejefferson@bogusemail.com', '1.00', '12.00', 'Ok', '', '2016-07-26 05:02:16']
['No Reward', 'Description: (None for No Reward)', '', '', '', '', '', '']
['Mary', 'Wilks', 'marywilks@bogusemail.com', '20.00', '60.00', 'Ok', '', '2017-04-21 02:44:43.395224']
['Neil', 'Patterson', 'neilpatterson@bogusemail.com', '10.00', '80.00', 'Ok', '', '2016-11-12 17:49:37']
['Corey', 'Davis', 'coreydavis@bogusemail.com', '6.00', '90.00', 'Ok', '', '2016-04-01 15:19:52']
['Steve', 'Jacobs', 'stevejacobs@bogusemail.com', '5.00', '21.00', 'Ok', '', '2017-01-04 19:38:44']
['Jane', 'Jenkins', 'janejenkins@bogusemail.com', '5.00', '30.00', 'Ok', '', '2017-01-15 17:24:39']
['John', 'Jacobs', 'johnjacobs@bogusemail.com', '3.14', '34.54', 'Ok', '', '2016-08-23 16:09:25']
['Neil', 'Smith', 'neilsmith@bogusemail.com', '3.00', '24.00', 'Ok', '', '2016-11-28 02:57:48']
['Corey', 'Wilks', 'coreywilks@bogusemail.com', '2.00', '8.00', 'Ok', '', '2017-03-26 20:13:08.207869']
['Corey', 'Smith', 'coreysmith@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-05 01:50:35.171076']
['Mary', 'Patterson', 'marypatterson@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-04 18:05:23.052059']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-21 19:42:36.098523']
['Travis', 'Arnold', 'travisarnold@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-19 08:04:33.428559']
['John', 'Robinson', 'johnrobinson@bogusemail.com', '1.00', '4.00', 'Ok', '', '2017-03-30 14:59:33.850333']
['Travis', 'Arnold', 'travisarnold@bogusemail.com', '1.00', '6.00', 'Ok', '', '2017-01-28 22:02:57']

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)
    
    #We don't want headers or firstline of the data
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        print(line)

'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
['John', 'Doe', 'johndoe@bogusemail.com', '10.00', '20.00', 'Ok', '', '2017-05-06 21:28:06.183108']
['Dave', 'Smith', 'davesmith@bogusemail.com', '5.00', '10.00', 'Ok', '', '2017-05-29 16:13:58.318920']
['Mary', 'Jacobs', 'maryjacobs@bogusemail.com', '5.00', '10.00', 'Ok', '', '2017-05-14 07:37:01.074648']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '5.00', '25.00', 'Ok', '', '2016-12-30 18:12:13']
['Tom', 'Wright', 'tomwright@bogusemail.com', '5.00', '15.00', 'Ok', '', '2017-04-14 04:02:06.658439']
['Steve', 'Robinson', 'steverobinson@bogusemail.com', '5.00', '20.00', 'Ok', '', '2017-03-17 02:20:14']
['Nicole', 'Jacobs', 'nicolejacobs@bogusemail.com', '5.00', '20.00', 'Ok', '', '2017-03-12 17:07:29']
['Jane', 'Wright', 'janewright@bogusemail.com', '5.00', '25.00', '', '', '2017-01-14 17:40:06']
['Jane', 'Doe', 'janedoe@bogusemail.com', '2.50', '5.00', 'Ok', '', '2017-05-14 11:20:50.798440']
['Kurt', 'Wright', 'kurtwright@bogusemail.com', '2.00', '2.00', 'Ok', '', '2017-06-23 21:12:15.662157']
['Kurt', 'Robinson', 'kurtrobinson@bogusemail.com', '2.00', '4.00', 'Ok', '', '2017-05-03 03:18:54.877885']
['Jane', 'Jenkins', 'janejenkins@bogusemail.com', '2.00', '8.00', 'Ok', '', '2017-03-23 16:37:47.708634']
['Neil', 'Robinson', 'neilrobinson@bogusemail.com', '1.50', '3.00', 'Ok', '', '2017-05-26 19:59:51.013984']
['Tom', 'Patterson', 'tompatterson@bogusemail.com', '1.34', '4.02', 'Ok', '', '2017-04-27 01:55:12.313799']
['Sam', 'Jenkins', 'samjenkins@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-16 02:34:47.674287']
['Steve', 'Stuart', 'stevestuart@bogusemail.com', '1.00', '1.00', 'Ok', '', '2017-06-12 03:32:00.706554']
['Maggie', 'Patterson', 'maggiepatterson@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-26 01:23:14.097393']
['Maggie', 'Stuart', 'maggiestuart@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-19 23:11:08.624354']
['Jane', 'Doe', 'janedoe@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-15 19:40:17.044921']
['Steve', 'Patterson', 'stevepatterson@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-09 17:14:23.591656']
['Dave', 'Smith', 'davesmith@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-01 18:35:10.731005']
['Sam', 'Wilks', 'samwilks@bogusemail.com', '1.00', '4.00', 'Ok', '', '2017-03-01 09:40:56']
['Kurt', 'Jefferson', 'kurtjefferson@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-24 08:23:05']
['Sam', 'Stuart', 'samstuart@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-12 00:14:31']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '5.00', 'Ok', '', '2017-02-06 14:52:28']
['Dave', 'Davis', 'davedavis@bogusemail.com', '1.00', '0.00', '', '', '2016-11-18 01:37:25']
['Sam', 'Patterson', 'sampatterson@bogusemail.com', '1.00', '8.00', 'Ok', '', '2016-11-01 11:27:17']
['Tom', 'Jefferson', 'tomjefferson@bogusemail.com', '1.00', '10.00', 'Ok', '', '2016-09-27 09:56:48']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '7.00', '', '', '2016-08-09 14:42:25']
['Maggie', 'Jefferson', 'maggiejefferson@bogusemail.com', '1.00', '12.00', 'Ok', '', '2016-07-26 05:02:16']
['No Reward', 'Description: (None for No Reward)', '', '', '', '', '', '']
['Mary', 'Wilks', 'marywilks@bogusemail.com', '20.00', '60.00', 'Ok', '', '2017-04-21 02:44:43.395224']
['Neil', 'Patterson', 'neilpatterson@bogusemail.com', '10.00', '80.00', 'Ok', '', '2016-11-12 17:49:37']
['Corey', 'Davis', 'coreydavis@bogusemail.com', '6.00', '90.00', 'Ok', '', '2016-04-01 15:19:52']
['Steve', 'Jacobs', 'stevejacobs@bogusemail.com', '5.00', '21.00', 'Ok', '', '2017-01-04 19:38:44']
['Jane', 'Jenkins', 'janejenkins@bogusemail.com', '5.00', '30.00', 'Ok', '', '2017-01-15 17:24:39']
['John', 'Jacobs', 'johnjacobs@bogusemail.com', '3.14', '34.54', 'Ok', '', '2016-08-23 16:09:25']
['Neil', 'Smith', 'neilsmith@bogusemail.com', '3.00', '24.00', 'Ok', '', '2016-11-28 02:57:48']
['Corey', 'Wilks', 'coreywilks@bogusemail.com', '2.00', '8.00', 'Ok', '', '2017-03-26 20:13:08.207869']
['Corey', 'Smith', 'coreysmith@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-05 01:50:35.171076']
['Mary', 'Patterson', 'marypatterson@bogusemail.com', '1.00', '0.00', 'Ok', '', '2017-07-04 18:05:23.052059']
['Jane', 'Stuart', 'janestuart@bogusemail.com', '1.00', '2.00', 'Ok', '', '2017-05-21 19:42:36.098523']
['Travis', 'Arnold', 'travisarnold@bogusemail.com', '1.00', '3.00', 'Ok', '', '2017-04-19 08:04:33.428559']
['John', 'Robinson', 'johnrobinson@bogusemail.com', '1.00', '4.00', 'Ok', '', '2017-03-30 14:59:33.850333']
['Travis', 'Arnold', 'travisarnold@bogusemail.com', '1.00', '6.00', 'Ok', '', '2017-01-28 22:02:57']

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)

'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
John Doe
Dave Smith
Mary Jacobs
Jane Stuart
Tom Wright
Steve Robinson
Nicole Jacobs
Jane Wright
Jane Doe
Kurt Wright
Kurt Robinson
Jane Jenkins
Neil Robinson
Tom Patterson
Sam Jenkins
Steve Stuart
Maggie Patterson
Maggie Stuart
Jane Doe
Steve Patterson
Dave Smith
Sam Wilks
Kurt Jefferson
Sam Stuart
Jane Stuart
Dave Davis
Sam Patterson
Tom Jefferson
Jane Stuart
Maggie Jefferson
No Reward Description: (None for No Reward)
Mary Wilks
Neil Patterson
Corey Davis
Steve Jacobs
Jane Jenkins
John Jacobs
Neil Smith
Corey Wilks
Corey Smith
Mary Patterson
Jane Stuart
Travis Arnold
John Robinson
Travis Arnold

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")

for name in names:
    print(name)
'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
John Doe
Dave Smith
Mary Jacobs
Jane Stuart
Tom Wright
Steve Robinson
Nicole Jacobs
Jane Wright
Jane Doe
Kurt Wright
Kurt Robinson
Jane Jenkins
Neil Robinson
Tom Patterson
Sam Jenkins
Steve Stuart
Maggie Patterson
Maggie Stuart
Jane Doe
Steve Patterson
Dave Smith
Sam Wilks
Kurt Jefferson
Sam Stuart
Jane Stuart
Dave Davis
Sam Patterson
Tom Jefferson
Jane Stuart
Maggie Jefferson

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!<p>'
print(html_output)

'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
<p>There are currently 30 public contributors. Thank You!<p>

Process finished with exit code 0
'''

import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!<p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}<li>'

html_output += '\n</ul>'

print(html_output)

'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
<p>There are currently 30 public contributors. Thank You!<p>
<ul>
	<li>John Doe<li>
	<li>Dave Smith<li>
	<li>Mary Jacobs<li>
	<li>Jane Stuart<li>
	<li>Tom Wright<li>
	<li>Steve Robinson<li>
	<li>Nicole Jacobs<li>
	<li>Jane Wright<li>
	<li>Jane Doe<li>
	<li>Kurt Wright<li>
	<li>Kurt Robinson<li>
	<li>Jane Jenkins<li>
	<li>Neil Robinson<li>
	<li>Tom Patterson<li>
	<li>Sam Jenkins<li>
	<li>Steve Stuart<li>
	<li>Maggie Patterson<li>
	<li>Maggie Stuart<li>
	<li>Jane Doe<li>
	<li>Steve Patterson<li>
	<li>Dave Smith<li>
	<li>Sam Wilks<li>
	<li>Kurt Jefferson<li>
	<li>Sam Stuart<li>
	<li>Jane Stuart<li>
	<li>Dave Davis<li>
	<li>Sam Patterson<li>
	<li>Tom Jefferson<li>
	<li>Jane Stuart<li>
	<li>Maggie Jefferson<li>
</ul>

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.DictReader(data_file)

    for item in csv_data:
        print(item)

    # next(csv_data)
    # next(csv_data)
    #
    # for line in csv_data:
    #     if line[0] == 'No Reward':
    #         break
    #     names.append(f"{line[0]} {line[1]}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!<p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}<li>'

html_output += '\n</ul>'

print(html_output)

'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
{'FirstName': '1 + Reward', 'LastName': 'Description I will add your name to the contributors page on my website.\n\nYou will also be eligible for Patreon-only rewards. I will occasionally give away books that I have read, and will choose a Patron at random to receive those.', 'Email': '', 'Pledge': '', 'Lifetime': '', 'Status': '', 'Country': '', 'Start': ''}
{'FirstName': 'John', 'LastName': 'Doe', 'Email': 'johndoe@bogusemail.com', 'Pledge': '10.00', 'Lifetime': '20.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-06 21:28:06.183108'}
{'FirstName': 'Dave', 'LastName': 'Smith', 'Email': 'davesmith@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '10.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-29 16:13:58.318920'}
{'FirstName': 'Mary', 'LastName': 'Jacobs', 'Email': 'maryjacobs@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '10.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-14 07:37:01.074648'}
{'FirstName': 'Jane', 'LastName': 'Stuart', 'Email': 'janestuart@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '25.00', 'Status': 'Ok', 'Country': '', 'Start': '2016-12-30 18:12:13'}
{'FirstName': 'Tom', 'LastName': 'Wright', 'Email': 'tomwright@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '15.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-04-14 04:02:06.658439'}
{'FirstName': 'Steve', 'LastName': 'Robinson', 'Email': 'steverobinson@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '20.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-03-17 02:20:14'}
{'FirstName': 'Nicole', 'LastName': 'Jacobs', 'Email': 'nicolejacobs@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '20.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-03-12 17:07:29'}
{'FirstName': 'Jane', 'LastName': 'Wright', 'Email': 'janewright@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '25.00', 'Status': '', 'Country': '', 'Start': '2017-01-14 17:40:06'}
{'FirstName': 'Jane', 'LastName': 'Doe', 'Email': 'janedoe@bogusemail.com', 'Pledge': '2.50', 'Lifetime': '5.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-14 11:20:50.798440'}
{'FirstName': 'Kurt', 'LastName': 'Wright', 'Email': 'kurtwright@bogusemail.com', 'Pledge': '2.00', 'Lifetime': '2.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-06-23 21:12:15.662157'}
{'FirstName': 'Kurt', 'LastName': 'Robinson', 'Email': 'kurtrobinson@bogusemail.com', 'Pledge': '2.00', 'Lifetime': '4.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-03 03:18:54.877885'}
{'FirstName': 'Jane', 'LastName': 'Jenkins', 'Email': 'janejenkins@bogusemail.com', 'Pledge': '2.00', 'Lifetime': '8.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-03-23 16:37:47.708634'}
{'FirstName': 'Neil', 'LastName': 'Robinson', 'Email': 'neilrobinson@bogusemail.com', 'Pledge': '1.50', 'Lifetime': '3.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-26 19:59:51.013984'}
{'FirstName': 'Tom', 'LastName': 'Patterson', 'Email': 'tompatterson@bogusemail.com', 'Pledge': '1.34', 'Lifetime': '4.02', 'Status': 'Ok', 'Country': '', 'Start': '2017-04-27 01:55:12.313799'}
{'FirstName': 'Sam', 'LastName': 'Jenkins', 'Email': 'samjenkins@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '0.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-07-16 02:34:47.674287'}
{'FirstName': 'Steve', 'LastName': 'Stuart', 'Email': 'stevestuart@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '1.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-06-12 03:32:00.706554'}
{'FirstName': 'Maggie', 'LastName': 'Patterson', 'Email': 'maggiepatterson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '2.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-26 01:23:14.097393'}
{'FirstName': 'Maggie', 'LastName': 'Stuart', 'Email': 'maggiestuart@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '2.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-19 23:11:08.624354'}
{'FirstName': 'Jane', 'LastName': 'Doe', 'Email': 'janedoe@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '3.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-04-15 19:40:17.044921'}
{'FirstName': 'Steve', 'LastName': 'Patterson', 'Email': 'stevepatterson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '3.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-04-09 17:14:23.591656'}
{'FirstName': 'Dave', 'LastName': 'Smith', 'Email': 'davesmith@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '3.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-04-01 18:35:10.731005'}
{'FirstName': 'Sam', 'LastName': 'Wilks', 'Email': 'samwilks@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '4.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-03-01 09:40:56'}
{'FirstName': 'Kurt', 'LastName': 'Jefferson', 'Email': 'kurtjefferson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '5.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-02-24 08:23:05'}
{'FirstName': 'Sam', 'LastName': 'Stuart', 'Email': 'samstuart@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '5.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-02-12 00:14:31'}
{'FirstName': 'Jane', 'LastName': 'Stuart', 'Email': 'janestuart@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '5.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-02-06 14:52:28'}
{'FirstName': 'Dave', 'LastName': 'Davis', 'Email': 'davedavis@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '0.00', 'Status': '', 'Country': '', 'Start': '2016-11-18 01:37:25'}
{'FirstName': 'Sam', 'LastName': 'Patterson', 'Email': 'sampatterson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '8.00', 'Status': 'Ok', 'Country': '', 'Start': '2016-11-01 11:27:17'}
{'FirstName': 'Tom', 'LastName': 'Jefferson', 'Email': 'tomjefferson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '10.00', 'Status': 'Ok', 'Country': '', 'Start': '2016-09-27 09:56:48'}
{'FirstName': 'Jane', 'LastName': 'Stuart', 'Email': 'janestuart@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '7.00', 'Status': '', 'Country': '', 'Start': '2016-08-09 14:42:25'}
{'FirstName': 'Maggie', 'LastName': 'Jefferson', 'Email': 'maggiejefferson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '12.00', 'Status': 'Ok', 'Country': '', 'Start': '2016-07-26 05:02:16'}
{'FirstName': 'No Reward', 'LastName': 'Description: (None for No Reward)', 'Email': '', 'Pledge': '', 'Lifetime': '', 'Status': '', 'Country': '', 'Start': ''}
{'FirstName': 'Mary', 'LastName': 'Wilks', 'Email': 'marywilks@bogusemail.com', 'Pledge': '20.00', 'Lifetime': '60.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-04-21 02:44:43.395224'}
{'FirstName': 'Neil', 'LastName': 'Patterson', 'Email': 'neilpatterson@bogusemail.com', 'Pledge': '10.00', 'Lifetime': '80.00', 'Status': 'Ok', 'Country': '', 'Start': '2016-11-12 17:49:37'}
{'FirstName': 'Corey', 'LastName': 'Davis', 'Email': 'coreydavis@bogusemail.com', 'Pledge': '6.00', 'Lifetime': '90.00', 'Status': 'Ok', 'Country': '', 'Start': '2016-04-01 15:19:52'}
{'FirstName': 'Steve', 'LastName': 'Jacobs', 'Email': 'stevejacobs@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '21.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-01-04 19:38:44'}
{'FirstName': 'Jane', 'LastName': 'Jenkins', 'Email': 'janejenkins@bogusemail.com', 'Pledge': '5.00', 'Lifetime': '30.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-01-15 17:24:39'}
{'FirstName': 'John', 'LastName': 'Jacobs', 'Email': 'johnjacobs@bogusemail.com', 'Pledge': '3.14', 'Lifetime': '34.54', 'Status': 'Ok', 'Country': '', 'Start': '2016-08-23 16:09:25'}
{'FirstName': 'Neil', 'LastName': 'Smith', 'Email': 'neilsmith@bogusemail.com', 'Pledge': '3.00', 'Lifetime': '24.00', 'Status': 'Ok', 'Country': '', 'Start': '2016-11-28 02:57:48'}
{'FirstName': 'Corey', 'LastName': 'Wilks', 'Email': 'coreywilks@bogusemail.com', 'Pledge': '2.00', 'Lifetime': '8.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-03-26 20:13:08.207869'}
{'FirstName': 'Corey', 'LastName': 'Smith', 'Email': 'coreysmith@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '0.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-07-05 01:50:35.171076'}
{'FirstName': 'Mary', 'LastName': 'Patterson', 'Email': 'marypatterson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '0.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-07-04 18:05:23.052059'}
{'FirstName': 'Jane', 'LastName': 'Stuart', 'Email': 'janestuart@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '2.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-05-21 19:42:36.098523'}
{'FirstName': 'Travis', 'LastName': 'Arnold', 'Email': 'travisarnold@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '3.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-04-19 08:04:33.428559'}
{'FirstName': 'John', 'LastName': 'Robinson', 'Email': 'johnrobinson@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '4.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-03-30 14:59:33.850333'}
{'FirstName': 'Travis', 'LastName': 'Arnold', 'Email': 'travisarnold@bogusemail.com', 'Pledge': '1.00', 'Lifetime': '6.00', 'Status': 'Ok', 'Country': '', 'Start': '2017-01-28 22:02:57'}
<p>There are currently 0 public contributors. Thank You!<p>
<ul>
</ul>

Process finished with exit code 0
'''
import csv
html_output = ''
names = []

with open('patrons.csv','r') as data_file:
    csv_data = csv.DictReader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!<p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}<li>'

html_output += '\n</ul>'

print(html_output)

'''
D:\python\.venv\Scripts\python.exe D:\python\parse_csv.py 
<p>There are currently 29 public contributors. Thank You!<p>
<ul>
	<li>Dave Smith<li>
	<li>Mary Jacobs<li>
	<li>Jane Stuart<li>
	<li>Tom Wright<li>
	<li>Steve Robinson<li>
	<li>Nicole Jacobs<li>
	<li>Jane Wright<li>
	<li>Jane Doe<li>
	<li>Kurt Wright<li>
	<li>Kurt Robinson<li>
	<li>Jane Jenkins<li>
	<li>Neil Robinson<li>
	<li>Tom Patterson<li>
	<li>Sam Jenkins<li>
	<li>Steve Stuart<li>
	<li>Maggie Patterson<li>
	<li>Maggie Stuart<li>
	<li>Jane Doe<li>
	<li>Steve Patterson<li>
	<li>Dave Smith<li>
	<li>Sam Wilks<li>
	<li>Kurt Jefferson<li>
	<li>Sam Stuart<li>
	<li>Jane Stuart<li>
	<li>Dave Davis<li>
	<li>Sam Patterson<li>
	<li>Tom Jefferson<li>
	<li>Jane Stuart<li>
	<li>Maggie Jefferson<li>
</ul>

Process finished with exit code 0
'''


