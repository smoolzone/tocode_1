from data_structure.class_1 import ExObjects


client_saif = ExObjects.ClientBill("Saif")
client_shmulik = ExObjects.ClientBill("Shmulik")

client_saif.add_drink("Been", 25)
client_shmulik.add_drink("Wisky", 40)


s = ExObjects.Summer()
t = ExObjects.Summer()

s.add(10, 20)
t.add(50)
s.add(30)
s.add()
t.add()

s.print_total()

t.print_total()
