menu = '''Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12
'''
print(menu)
dict1={"Oil change":35,"Tire rotation":19,"Car wash":7,"Car wax":12,"-":"No service"}

print("Select first service:\n", end="")
service1=input()
print("Select second service:\n", end="")
service2=input()


print("\nDavy's auto shop invoice\n")

if service1 != '-' and service2 != '-':
    print("Service 1: "+service1+", $" + str(dict1[service1]))
    print("Service 2: "+ service2 + ", $" + str(dict1[service2]))
elif service =='-':
    print('Service 1: '+'No service')
    print('service 2: '+service2+', $'+str(dict1[service2]))
else:
    print('service 1: '+ service1 + ', $' + str(dict1[service1]))
    print('Service 2: '+'No service')
total = dict1[service1]

print("Total: $") + str(total)
