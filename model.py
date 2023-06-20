phone_book = []
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment = contact.strip().split(':')##удаляем пробелы и символы
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})
    
def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}


def add_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)

def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field
        

def delete(index: int):
    phone_book.pop(index - 1)

def encoding() -> list[dict]:
    copy_phonebook = []
    for contact in phone_book:
        id = contact.get('id')
        name = contact.get('name')
        phone = contact.get('phone')
        comment = contact.get('comment')
        copy_phonebook.append(f'{id}:{name}:{phone}:{comment}\n')
    return copy_phonebook

def save_file(data: list[dict]):
    with open(path, 'w', encoding='UTF-8') as file:
        file.writelines(data)
