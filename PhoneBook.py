# 1. Создать файл
#     - Открыть файл на дозапись
# 2. Запись контакта в файл
#     - Открыть файл на дозапись
#     - Получить данные нового контакта
#     - Записать эти данные в файл
# 3. Вывод данных на экран
#     - Открыть файл на чтение
#     - Получить данные из файла
#     - Вывести данные на экран
# 4. Поиск контакта по данным
#     - Получить данные для поиска
#     - Выбрать вариант поиска
#     - Открыть файл на чтение
#     - Получить данные из файла
#     - Осуществить поиск
#     - Вывести данные на экран
# 5. Копирование строки в другой файл
#     - Получить номер строки
#     - Скопировать данные по номеру строки из текущего файла
#     - Создать новый файл
#     - Открыть файл на дозапись
#     - Записать данные в новый файл
# 6. Создать пользовательский интерфейс (UI)
#     - Вывод на экран пользовательского меню
#     - Получение запроса от пользователя
#     - Запуск соответствующей функции
#     - Выход из программы
################################################

def input_name():
    return input("Введите имя: ")

def input_patronumic():
    return input("Введите отчество: ")

def input_surname():
    return input("Введите фамилию: ")

def input_phone():
    return input("Введите телефон: ")

def input_address():
    return input("Введите адрес: ")

def create_contact():
    name = input_name()
    patronumic = input_patronumic()
    surname = input_surname()
    phone = input_phone()
    address = input_address()
    return f"{name} {patronumic} {surname}\n{phone}\n{address}\n\n"
   

def add_contact():
    contact = create_contact()
    with open("phonebook.txt","a",encoding = "UTF-8") as f_w:
        f_w.write(contact)
   
def print_phonebook():
    with open("phonebook.txt","r",encoding = "UTF-8") as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split("\n\n")
    for i, contact in enumerate(list_contacts, 1):
        print(i, contact + "\n" )    


def find_contact():
    search = input("Введите данные для поиска: ")
    print(

        "Возможные варианты поиска:\n"
        "1. По имени\n"
        "2. По отчеству\n"
        "3. По фамилии\n"
        "4. По телефону\n"
        "5. По адресу\n"
    )
    var = input("Выберите вариант поиска 1,2,3,4 или 5: ")
    while var not in ("1","2","3","4","5"):
        print("Некорректный ввод")
        var = input("Выберите вариант поиска 1,2,3,4 или 5: ")
    i_var = int(var) - 1
    with open("phonebook.txt","r",encoding = "UTF-8") as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split("\n\n")
    for contact in list_contacts:
        contact_lst = contact.split()
        if search in contact_lst[i_var]:
            print(contact)

def copy_contact():
    with open("phonebook.txt","r",encoding = "UTF-8") as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split("\n\n")
    number_contact = input("Введите номер строки (контакта) для копирования: ")
   
    numbers = []
       
    for i, contact in enumerate(list_contacts, 1): 
        numbers.append(int(i))  
        if int(number_contact) == i:
            with open("copy_phonebook.txt","a",encoding = "UTF-8") as f_w:
                f_w.write(contact + "\n\n")
                print(" !! Копирование проведено !! ")   
    if int(number_contact) not in numbers:
             print(" !! Такого номера нет в списке !! ")

# UI

def ui():
    with open("phonebook.txt","a", encoding = "UTF-8"):
        pass
    choise = "0"
    while choise != "5":
        print(

            "Возможные варианты запроса:\n"
            "1. Добавление нового контакта\n"
            "2. Вывод данных на экран\n"
            "3. Поиск контакта по данным\n"
            "4. Скопировать контакт в другой файл\n"
            "5. Выход из программы\n"
            )
        choise = input("Выберите вариант действия 1,2,3,4 или 5: ")
        while choise not in ("1","2","3","4","5"):
            print("Некорректный ввод")
            choise = input("Выберите вариант действия 1,2,3,4 или 5: ")
        match choise:
            case "1":
                add_contact()
            case "2":
                print_phonebook()
            case "3":
                find_contact()
            case "4":
                copy_contact()
            case "5":
                print("Всего хорошего!")


ui()




    