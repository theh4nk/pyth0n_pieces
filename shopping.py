#shopping list
shoplist = ["tuna","milk","eggs","bread","chapstick","deodorant","toofpaste",]

print("I have", len(shoplist), "items in my cart")

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

#add items
print('\nI also have to buy cookies.')
shoplist.append('cookies')
print('My shopping list is now', len(shoplist))

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', len(shoplist))
