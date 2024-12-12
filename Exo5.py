print("Runner 1:")
r1 = input("Name : ")
time1 = int(input("Time (in secons): "))
print("Runner 2:")
r2 = input("Name : ")
time2 = int(input("Time (in secons): "))

if time1 < time2 :
    print(f"The faster runne id {r2}")
if time1 > time2 : 
    print(f"The faster runner is {r1}")
else:
    print(f"{r1} and {r2} have the same time")
