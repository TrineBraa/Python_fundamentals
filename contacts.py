contacts =  {
    'number' : 4,
    'students' : [
        {'name' : 'Harry Potter', 'email' : 'Harry.potter@example.com'},
        {'name' : 'Hermione Granger', 'email' : 'Hermione@example.com'},
        {'name' : 'Ron Weasley', 'email' : 'Ron@example.com'},
        {'name' : 'Draco Malfoy', 'email' : 'Draco@example.com'}
    ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])