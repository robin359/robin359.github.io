import yagmail

sender = input('Gib bitte deine Email-Adresse ein: ')
password = input('Um mit deiner E-Mail Adresse Nachrichten schreiben zu können brauchen wir natürlich dein Passwort: ')
receiver = input('Nun die Email-Adresse des Empängers:')
subject = input('Welchen Betreff soll deine Email haben? ')
content = input('Jetzt kannst du hier deine Nachricht eingeben: ')
durchlauf = input('Wie oft soll die Email versendet werden? ')

while int(durchlauf) > 0:
    yagmail.SMTP(sender, password).send(receiver, subject, content)
    int(durchlauf) - 1
else:
    print('Emails sent.')