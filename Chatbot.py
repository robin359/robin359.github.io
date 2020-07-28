print('Hallo ich bin dein persönlicher Chatbot.')
name = input('Wie heißt du? ')
print('Schön dich kennen zu lernen', name)
age = input('Wie alt bist du? ')

if int(age) > 17:
    print('Dann bist du ja schon volljährig!')
else:
    print('Dann bist du ja noch minderjährig!')

home = input('Wo wohnst du? ')
print('In', home, 'gefällt es mir ja besonders gut.' )

gender = input('Bist du Mann oder Frau? ')

if gender == 'Mann':
    print('Mann bist du männlich!')
else:
    print('Fraulautern ist auch schön!')
