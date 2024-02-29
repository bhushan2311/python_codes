
l1=["john","brock","randy","sheamus","roman","khali","jinder"]
for i in l1:
    print(i,end=" , ")         # it does not removes last " , "

print("\n\nPrinting using join function")
j=" , ".join(l1)               # it removes last " , "
print(j)