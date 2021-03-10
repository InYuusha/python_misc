formatter="%10s%10s%10s"

header=formatter%("Team","Won","Lost")
middle=formatter%("Griff",5,1)
last=formatter%("latte",3,3)

table="%s\n%s\n %s"%(header,middle,last)
print(table)
