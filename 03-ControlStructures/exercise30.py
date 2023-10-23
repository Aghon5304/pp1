normal_time = str(input("Enter time (24-hour format): "))
if normal_time[0]=="2"and normal_time[1]!=":":
    normal_time=str(int(normal_time[0:2])-12)+normal_time[2:]
    print(f"Time in 12-hour format: {normal_time}pm")
elif normal_time[0] == "1" and normal_time[1]>"2" and normal_time[1]!=":":
    normal_time=normal_time[1:]
    normal_time=str(int(normal_time[0])-2)+normal_time[1:]
    print(f"{normal_time}")
else:
    print(f"Time in 12-hour format: {normal_time}am")