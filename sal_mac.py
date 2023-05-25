
# De la variable prueba1, que imprima solo la mac address
# Y armar un listado con las mac address
switch_1 = [('XGigabitEthernet0/0/3', 'XGigabitEthernet0/0/3', '2113', '6c3b.6b60.60a3'), ('XGigabitEthernet0/0/1', 'XGigabitEthernet0/0/1', '2113', '744d.28e5.99a5')]
switch_2 = [('XGigabitEthernet0/0/3', 'XGigabitEthernet0/0/3', '2113', '744d.28e5.99a5'), ('XGigabitEthernet0/0/2', 'XGigabitEthernet0/0/2', '2113', '6c3b.6b60.60a3'), ('XGigabitEthernet0/0/2', 'XGigabitEthernet0/0/2', '2113', 'fcec.da78.ac35')]


for i in switch_1:
    print(i[3])


for i in switch_2:
    print(i[3])











































































