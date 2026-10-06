students = {"name":"xyz", "age":20, "course":"python"}
# print(dir(students))
"""clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']"""
# get() the value of a key
print(students.get("name"))     
# items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(students.items())
# keys() method returns a view object that displays a list of all the keys in the dictionary.
print(students.keys())
# pop() method removes the specified key and returns the corresponding value.
print(students.pop("age"))
# popitem() method removes the last inserted key-value pair from the dictionary and returns it as a tuple.
print(students.popitem())
# values() method returns a view object that displays a list of all the values in the dictionary.
print(students.values())
# if key is present it will return the value of that key, if not present it will add the key with the default value and return that value    
print(students.setdefault("college", "abesit"))
