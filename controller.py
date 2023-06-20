from view import menu, show_contacts, print_message, input_contact, input_return, input_index
import model
from view import text

def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                #1. Открыть файл
                model.open_file()
                print_message(text.open_successful)
            case 2:
                #2. Сохранить файл
                model.save_file(model.encoding())
                print_message(text.file_saved)
            case 3:
                #3. Показать все файлы
                show_contacts(model.phone_book)
            case 4:
                #4. Создать новый контакт
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                #5. Найти контакт
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                #6. Изменить контакт
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index)-1].get('name')
                print_message(text.contact_change(new.get('name') if new.get('name') else old_name))
            case 7:
                #7. Удалить контакт
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index_delete)
                delete_name = model.phone_book[int(index)-1].get('name')
                check = int(input(text.check_delete_contact(delete_name)))
                if(check == 1):
                    model.delete(int(index))
                    print_message(text.delete_contact(delete_name))
                else:
                    print_message(text.delete_error)
            case 8:
                #8. Выход
                with open(model.path, 'r', encoding='UTF-8') as file:
                    data = file.readlines()
                    temp = model.encoding()
                    if data != temp:
                        check = int(input(text.check_exit))
                        if(check == 1):
                            model.save_file(temp)
                            print_message(f'{text.file_saved}\n{text.file_close}')
                        else:
                            file.close()
                            print_message(text.file_close)
                    else:
                        print_message(text.file_close)
                break