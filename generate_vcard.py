import csv

encoding = 'utf-8'

# open csv source file containing email list
# place the source file in the same folder as script file, 
# indicate the filename in the following statement
with open('dummy_mails.csv', newline ='', encoding=encoding) as f:
    freader = csv.reader(f, delimiter= ';', quotechar='|')
    
    # define str constants for resulting vcard file
    ENTRY_START = 'BEGIN:VCARD\nVERSION:3.0\n'
    ENTRY_END = 'END:VCARD\n' 
 
    # create vcard file and populate it with formatted entries
    with open('vcard_collection.vcf', 'w', encoding=encoding) as vcard_file:
        for i, line in enumerate(freader):

            #check email field is not empty
            if (len(line) > 1) and (line[1] != ''):
                
                fn = 'FN:' + line[0] + '\n'
                email = 'EMAIL;TYPE=internet, work:' + line[1] + '\n'
                entry = (ENTRY_START + fn + email + ENTRY_END)
                vcard_file.write(entry)

        # show this text on the end of the conversion        
        print(i+1, 'entries have just been placed into vcard_collection.vcf')