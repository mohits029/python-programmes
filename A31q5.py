l1=[
    "Mumbai",
    "Pune",
    "Delhi",
    "Amritsir",
    "Dehradoon",
    "Chennai",
    "Patna",
    "Jaipur",
    "Surat",
    "Simla",
    "Agara",
    "Bhopal",
    "Indore",
    "Barelly",
    "Srinagar",
    "Rudrapur",
    "Haldwani",
    "Kullu",
    "Nanital",
    "Allahabad",
    "Ranchi",
    "Jabalpur",
    "Kota",
    "Chandigarh",
    "Noida",
    "Amravati",
    "Kochi",
    "Bangalore"
]

d1={}
temp= []

sm_alpha= 'abcdefghijklmnopqrstuvwxyz'
cp_alpha= 'ABCDEFGHJJKLMNOPQRSTUVWXYZ'

for i in range(0,26):
    for j in l1:
        if j.startswith(cp_alpha[i]) or j.startswith(sm_alpha[i]):
            temp.append(j)
    
    if len(temp)>0:
        print(cp_alpha[i], ":", temp)
    temp.clear()


print(d1)