#strings in python - python string methods
name = 'Cambodia'
 
names = ['aizwal', 'imphal', 'shillong', 'agartala']
 
print(name)
print(name.upper())             #Return a copy of the string with all the cased characters converted to uppercase
print(name.count('a'))
print(name.count('A'))
print(name.upper().count('A'))  #we 1st convert the string into uppercase
print(name.upper().count('a'))
print(name.find('o'))
print(name.find('dia'))
print(name.find('xx'))
print(name.capitalize())        #Return a copy of the string with its first character capitalized and the rest lowercased.
print(name.lower())
print(name.casefold())      #Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss"

