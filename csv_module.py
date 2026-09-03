import csv
# with open("student.csv","r") as file:
    # f=csv.reader(file)
    # for i in f:
    #     print (i)
with open("student.csv","w") as file:
    f=csv.writer(file)
    f.writerow(["Name","Age"])
    f.writerow(["Manikarnika",3])
    values=[("Malhar",1),
            ("Siva",1)]
    f.writerows(values)