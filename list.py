
'''
Student Name: Iqra Tahir
Roll No: PIAIC234522
Assignment: Python Exercises on Lists
'''

#Exercise 3-1: Names
'''● Task: Store the names of a few of your friends in a list called names. Print each person’s
name by accessing each element in the list, one at a time.
'''
friends = ['Zufishan','Hamna','Zaib','Tehreem']
for x in friends: print(x)

#Exercise 3-2: Greetings
'''● Task: Start with the list you used in Exercise 3-1. Instead of just printing each person’s
name, print a message to them. The text of each message should be the same, but each
message should be personalized with the person’s name.
'''
for x in friends:
 print(f'Welcome! {x}')

#Exercise 3-3: Your Own List
'''● Task: Think of your favorite mode of transportation, such as a motorcycle or a car, and
make a list that stores several examples. Use your list to print a series of statements
about these items, such as “I would like to own a Honda motorcycle.”
'''
vehicles = ['car','bicycle','bike','scootie']
print(f'I want to buy a {vehicles[0]} with my own money.\nI want to ride carefree ride a {vehicles[1]}\nI want to buy an elctric-{vehicles[2]}\nI want to buy a {vehicles[3]} for my daily commute.')

#Exercise 3-4: Guest List
'''● Task: If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you’d like to invite to dinner. Then use your
list to print a message to each person, inviting them to dinner.
'''
guests = ['Mama','Sister','Brother','Papa']
for x in guests:
 print(f'Dear {x}, I want to invite you to dinner at my home next Sunday.')

#Exercise 3-5: Changing Guest List
'''● Task: Start with your program from Exercise 3-4. Add a print() call at the end of your
program, stating the name of the guest who can’t make it. Modify your list, replacing the
name of the guest who can’t make it with the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in your list.
'''
print('"Papa can\'t come as he is no more in this world.')
guests[-1] = 'Niece'
for x in guests:
 print(f'Dear {x}, I want to invite you dinner at my home next Sunday.')

#Exercise 3-6: More Guests
'''● Task: Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end
of your program, informing people that you found a bigger table. Use insert() to add
one new guest to the beginning of your list. Use insert() to add one new guest to the
middle of your list. Use append() to add one new guest to the end of your list. Print a
new set of invitation messages, one for each person in your list.
'''
print('Dear guests, I have found a bigger table so let\'s invite more people!')
guests.insert(0,'Nephew')
guests.insert(3,'Aunt')
guests.append('Husband')
for x in guests:
 print(f'Dear {x}! You are invited for dinner at my home next Sunday.')

#Exercise 3-7: Shrinking Guest List
'''● Task: Start with your program from Exercise 3-6. Add a new line that prints a message
saying that you can invite only two people for dinner. Use pop() to remove guests from
your list one at a time until only two names remain in your list. Each time you pop a
name from your list, print a message to that person letting them know you’re sorry you
can’t invite them to dinner. Print a message to each of the two people still on your list,
letting them know they’re still invited. Use del to remove the last two names from your
list, so you have an empty list. Print your list to make sure you actually have an empty
list at the end of your program.
'''
print('I can invite only two people for dinneer.')
guests.pop()
print(f'Soory {guests[-1]}! I can\'t invite you to dinner')
guests.pop()
print(f'Soory {guests[-1]}! I can\'t invite you to dinner')
guests.pop()
print(f'Soory {guests[-1]}! I can\'t invite you to dinner')
guests.pop()
print(f'Soory {guests[-1]}! I can\'t invite you to dinner')
guests.pop()
print(f'Soory {guests[-1]}! I can\'t invite you to dinner')
print(f'Dear {guests[0]}, you are still invited!')
print(f'Dear {guests[1]}, you are still invited!')
del guests[0:2]
print(guests)

#Exercise 3-8: Seeing the World
'''● Task: Think of at least five places in the world you’d like to visit. Store the locations in a
list. Make sure the list is not in alphabetical order. Print your list in its original order. Don’t
worry about printing the list neatly; just print it as a raw Python list. Use sorted() to
print your list in alphabetical order without modifying the actual list. Show that your list is
still in its original order by printing it. Use sorted() to print your list in
reverse-alphabetical order without changing the order of the original list. Show that your
list is still in its original order by printing it again. Use reverse() to change the order of
your list. Print the list to show that its order has changed. Use reverse() to change the
order of your list again. Print the list to show it’s back to its original order. Use sort() to
change your list so it’s stored in alphabetical order. Print the list to show that its order
has been changed. Use sort() to change your list so it’s stored in reverse-alphabetical
order. Print the list to show that its order has changed.
'''
locations = ['Makkah','Skardu','Turkey','Madina','Ladakh']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

#Exercise 3-9: Every Function
'''● Task: Think of things you could store in a list. For example, you could make a list of
mountains, rivers, countries, cities, languages, or anything else you’d like. Write a
program that creates a list containing these items and then uses each function
introduced in this chapter at least once.
'''
rivers = ['Sindh','Ravi','Satlaj','Chenab','Jhelum']
print(len(rivers)) #Length function
print(sorted(rivers)) #Sorted function
print(sorted(rivers,reverse=True)) #Sorted function to reverse list
print(max(rivers)) #Max function
print(min(rivers))  #Min function
print(any(rivers)) #any function
print(all(rivers)) #all function
for index,value in enumerate(rivers): #enumerate function
 print(index,value)
 
#Exercise 3-10: Intentional Error
'''● Task: If you haven’t received an index error in one of your programs yet, try to make one
happen. Change an index in one of your programs to produce an index error. Make sure
you correct the error before closing the program.'''
#Solution:
'''print(sum(rivers))
TypeError: unsupported operand type(s) for +: 'int' and str
'''