from pprint import pprint
import csv
import re



with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

    pattern_name = r"^([\w]+)(\s)?([\w]+)?(\s)?([\w]+)?,([\w]+)?(\s)?([\w]+)?,([\w]+)?"
    result_name = re.compile(pattern_name)

    pattern_phone = r"((\+7)|8)\s?\(?([\d]{3}?)(\)|\s|-)?\s?([\d]{3}?)(\s|-)?([\d]{2}?)(\s|-)?([\d]{2}?)(\s\(?(доб\.)?\s?([\d]*)\)?)?"
    result_phone = re.compile(pattern_phone)

    contacts_list_2 = []
    for contact in contacts_list:
        contact = ','.join(contact)
        contact = result_name.sub(r"\1,\3\6,\5\8\9", contact)
        contact = result_phone.sub(r"+7(\3)\5-\7-\9 \11\12", contact)
        contact = contact.split(',')
        contacts_list_2.append(contact)
    # print(contacts_list_2)


key_contacts = []
for key_contact in contacts_list_2:
    uniq_key = (key_contact[0], key_contact[1])
    key_contacts.append(uniq_key)
key_contacts = set(key_contacts)
# pprint(key_contacts)

uniq_phone_book= []

for uniq_key in key_contacts:
    empty = ['', '', '', '', '', '', '']
    for key_contact in contacts_list_2:
        if uniq_key[0] and uniq_key[1] in key_contact:
            i = -2
            for field in key_contact:
                i+=1
                if empty[i] != key_contact[i]:
                    empty[i] =empty[i] + key_contact[i]
            uniq_phone_book.append(empty)
            uniq_phone_book.sort()

res_list=[]
for item in uniq_phone_book: 
    if item not in res_list: 
        res_list.append(item)
pprint(res_list)

with open("phonebook_correct_uniq.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(res_list)




       
       
