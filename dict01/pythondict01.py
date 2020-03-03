#!/usr/dir/bin/env python3

## create a dictionary

switch= {"hostname": "swq", "ip": "10.0.1.1", "version": "1.2", "Vendor": "cisco"}

print(switch["hostname"])
print(switch["ip"])
print(switch["Vendor"])


print("First test - .get()")
print(switch.get("lynx"))
print("Second test - .get()")
print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))
print("Third test - .get()")
print( switch.get("version"))

print( "Fourth test - .keys()")
print( switch.keys())

print( "Fifth test - .values()" )
print(switch.values())

print( "Sixth test - .pop()")
switch.pop("version")
print( switch.keys())
print( switch.values())

print( "Seventh test - ADD a new value")
switch ["adminlogin"] = "karl08"
print( switch.keys())
print( switch.values())




