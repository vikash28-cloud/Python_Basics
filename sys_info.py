from __future__ import print_function
import wmi
c = wmi.WMI()
my_system = c.win32_computersystem()[0]
print("\t\t SYSTEM INFORMATION\n")
print(f"model:{my_system.model}")
print(f"name: {my_system.Name}")
print(f"Number_of_processors: {my_system.NumberOfProcessors}")
print(f"SystemType: {my_system.SystemType}")
print(f"SystemFamily: {my_system.SystemFamily}")

