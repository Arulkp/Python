a =  [
{
"Firstname": "Arul",
"Lastname": "Kumar",
"Mark": 80,
"Subject": "Maths"
},

{
"Firstname": "Arul",
"Lastname": "Kumar",
"Mark": 85,
"Subject": "Physics"
},
{
"Firstname": "sathish",
"Lastname": "Narayanan",
"Mark": 60,
"Subject": "science"
},
{
"Firstname": "Pradeep",
"Lastname": "Kumar",
"Mark": 70,
"Subject": "Maths"
},
{
"Firstname": "sathish",
"Lastname": "Narayanan",
"Mark": 90,
"Subject": "Tamil"
},
]


a1 = []	
[a1.append({"Firstname":x["Firstname"],"Lastname":x["Lastname"],"Subject":x["Subject"] ,"Total Marks":x["Mark"]	}) if not any(d['Firstname'] == x["Firstname"] for d in a1) else a1[next(i for i, item in enumerate(a1) if item["Firstname"] == x["Firstname"])].update({"Firstname":x["Firstname"],"Lastname":x["Lastname"],"Subject":a1[next(i for i, item in enumerate(a1) if item["Firstname"] == x["Firstname"])]["Subject"] if a1[next(i for i, item in enumerate(a1) if item["Firstname"] == x["Firstname"])]["Total Marks"] > x["Mark"] else x["Subject"],"Total Marks":a1[next(i for i, item in enumerate(a1) if item["Firstname"] == x["Firstname"])]["Total Marks"] + x["Mark"]}) for x in a]
print(max(a1, key=lambda x:x['Total Marks']))
