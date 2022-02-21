import csv
import email

encoding = 'utf-8'

# open csv source file containing email list
# place the source file in the same folder as script file, 
# indicate the filename in the following statement
with open('dummy_mails.csv', newline ='', encoding=encoding) as f:
    freader = csv.reader(f, delimiter= ';', quotechar='|')

    # define empty lists to sort email address there
    mailru = []
    gmail = []
    yandex = []
    tutby = []
    otherms = []

    email_count = 0

    # sort email strings in the source files
    for i, line in enumerate(freader):
        
        #check email field is not empty
        if (len(line) > 1) and (line[1] != ''):
            #calculate non-empty email strings
            email_count +=1

            if (
                line[1].endswith('mail.ru') or 
                line[1].endswith('list.ru') or
                line[1].endswith('inbox.ru') or
                line[1].endswith('bk.ru') or
                line[1].endswith('internet.ru')
                ):
                mailru.append(line)

            elif line[1].endswith('gmail.com'):
                gmail.append(line)

            elif line[1].count('yandex.') == 1:
                yandex.append(line)

            elif line[1].endswith('tut.by'):
                tutby.append(line)
                
            else:
                otherms.append(line)
    
    # count the number of addresses belonging to indicated mail servers
    # place them into a dictionary
    resulting_count = {
        'Mailru': len(mailru),
        'Gmail': len(gmail),
        'Yandex': len(yandex),
        'Tutby': len(tutby),
        'Otherms': len(otherms),
        'Total emails': email_count,
        'Total entries': i+1
    }
    
    print('Arrangement of mail addresses by mail servers (ms): ')
    print(*[str(k) + ': ' + str(v) for k,v in resulting_count.items()], sep='\n')
    

                