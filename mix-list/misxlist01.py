#!/usr/bin/env/ python3

#create a list containing three items 
p_list = [ "192.168.0.5", 5060, "UP" ]
#display the first item in the list 
print("The first item in the list (IP):" + p_list[0])
#display the second item in the list
print("the second item in the list (Port):" + str(p_list[1]))
print("the last item in the list (State):" + p_list[2])
new_list= [ 5060, "80", 55, "50.0.0.1", "10.20.30.1", "ssh" ]
print("When I " + new_list[5] + "into IP Addresses " + new_list[3])
print("or" + new_list[4] + " I am unable to ping ports")
print(str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]))






