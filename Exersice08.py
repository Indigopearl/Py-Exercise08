
# Task 1

data = """id,first_name,last_name,email,ip_address
1,Jennine,Kohnert,jkohnert0@disqus.com,45.55.73.106
2,Katalin,Nolda,knolda1@123-reg.co.uk,223.30.112.215
3,Atalanta,Kaming,akaming2@gmpg.org,254.219.7.208
4,Kassie,Covell,kcovell3@cafepress.com,150.145.187.71
5,Vonni,Dignam,vdignam4@cafepress.com,138.219.98.53
6,Billie,Neubigging,bneubigging5@addthis.org,180.79.192.175
7,Etan,Peers,epeers6@cafepress.com,199.1.3.70
8,Pail,Walcher,pwalcher7@cafepress.com,199.170.155.126
9,Edlin,Kosel,ekosel8@columbia.edu,217.59.107.252
10,Jennifer,Tibalt,jtibalt9@sun.com,73.29.190.227
11,Douglas,Howe,dhowea@cafepress.com,93.94.19.71
12,Galina,Antoniewski,gantoniewskib@freewebs.com,69.177.160.104
13,Emelita,Pauer,epauerc@house.gov,178.243.169.131
14,Edmon,Cleugh,POTATOKING.2000@furl.net,100.219.252.98
15,kyo,zipulimakkarakeitto,kz@guardian.com,78.226.120.240
16,Harlin,Goodrich,hgoodrichf@guardian.com,232.242.92.122
17,Paddie,Brittain,pbrittaing@jigsy.com,230.116.80.29
18,Blisse,Barbrook,bbarbrookh@nytimes.com,153.237.126.205
19,Latia,Roughey,lrougheyi@guardian.co.uk,184.128.166.8
20,Gregoire,Castelow,gcastelowj@51.la,87.181.120.134
21,lorenza,kurn,ljurnk@nsw.gov.au,192.238.146.135
22,Dulciana,Wilce,dwilcel@noaa.gov,234.245.232.7
23,Boyd,Sponton,bspontonm@guardian.com,106.75.217.74
24,Lenora,Issard,lissardn@guardian.com,167.91.15.190
25,Lissi,Davidovitz,ldavidovitzo@guardian.com,48.7.220.5"""

# Task 1

# Save the list of strings in a variable called lines
lines = data.strip().split("\n")

print("Amount of lines:", len(lines))  # Print the amount of lines

print()

for a in range(0, len(lines), 5):  # Loop over the lines using a for loop and print every 5th line
    print(lines[a])

print()

# Task 2

for line in lines:  # Split each line by the commas, saving the result to a variable
    email_only = line.split(",")
    print(email_only[3])

print()

# Task 3

print("Number of users with email ending with .co.uk in it: ", data.count(".co.uk"))

print()

counter = 0

for line in lines:
    name = line.split(",")
    if name[1].upper().startswith('K') or name[2].upper().startswith('K'):
        counter += 1
print(f"Number of users whose first or last name starts with 'K': ", counter)

# Task 4
print()

short = data.split('\n')

for c in range(1,len(short)):
    name = short[c].split(",")
    ip = name[4].split(".")

    print(name[1], name[2][0]+"."+","+ip[0]+"."+ip[1]+".xxx.xxx")
