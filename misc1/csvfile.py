import csv
with open("C:\\Users\\op\\Desktop\\data.csv",'w') as file:
    writer=csv.writer(file)
    writer.writerow(("int" ,"int+2","int*2"))
    for i in range(5):
        writer.writerow((i,i+2,i*2))
