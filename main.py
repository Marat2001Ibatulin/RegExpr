from pprint import pprint
import csv
import re

with open("phonebook.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_list = [contacts_list[0]]

phone_pattern = r'(\+7|8)\s*\(?(\d{3})\)?(\s*|-)?(\d{3})-?(\d{2})-?(\d{2})\s*\(?(доб\.)?\s*(\d{4})?\)?'
repl_pattern = r'+7(\2)\4-\5-\6 \7\8'

for person in contacts_list[1:]:
    fio = ' '.join(person[:3])
    person_list = fio.split()
    if len(person_list) < 3:
        for _ in range(3-len(person_list)):
            person_list.append('')

    person_list.append(person[3])
    person_list.append(person[4])

    phone_text = person[5]
    form_phone = re.sub(phone_pattern,repl_pattern, phone_text)
    person_list.append(form_phone.strip())

    person_list.append(person[6])

    new_list.append(person_list)

new_list.sort(key=lambda x:x[0:3])

del_indexes = []
for i in range(2,len(new_list)):
    if new_list[i-1][0] == new_list[i][0] and new_list[i-1][1] == new_list[i][1]:
        if new_list[i-1][2] == '' and new_list[i][2] != '':
            new_list[i-1][2] = new_list[i][2]
        if new_list[i-1][3] == '' and new_list[i][3] != '':
            new_list[i-1][3] = new_list[i][3]
        if new_list[i-1][4] == '' and new_list[i][4] != '':
            new_list[i-1][4] = new_list[i][4]
        if new_list[i-1][5] == '' and new_list[i][5] != '':
            new_list[i-1][5] = new_list[i][5]
        if new_list[i-1][6] == '' and new_list[i][6] != '':
            new_list[i-1][6] = new_list[i][6]
        del_indexes.append(i)

final_list = [l for l in new_list if new_list.index(l) not in del_indexes]

pprint(final_list)

with open("fixed_phonebook.csv", "w", newline='', encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_list)


