#Nessa formatação o valor ter um loop.
#Criamos myMixedTypeList tem varios valores 
#for = loop 
#item = vai receber os valores da lista um de cada.
#in = direcionamento a lista (myMixedTypeList)
#print("{item} is of the data type {item <type o tipo>}".format(item,type(item)))
#o loop só vai finalizar quando todos da lista acabar.

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(myMixedTypeList)
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
