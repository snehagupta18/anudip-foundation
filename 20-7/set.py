# set methods add() and update()

months={"january","february","march","april","may","june"}
print(months)
print(id(months))
months.add('august')
months.update(["july","august","september","october"])
print(id(months))
print(months)

# difference between discard and remove method
# discard- no error if element is not found
# remove- gives error if element is not found
months.discard("december")
print(months)
# months.remove("december")

# pop() method gives the deleted value as output
delete=months.pop()
print(delete)

# union() method to add 2 sets
x={'a','b','c'}
y={'d','e','a'}
z=x.union(y)
print(z)