import json

def generate_id(data: dict) -> int:
    new_id = 1
    if data:
        return max([data[i]['id'] for i in data]) + 1
    return new_id

def save_data(data: dict) -> None:
    with open('library.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_book(data: dict) -> None:
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    while True:
        try:
            year = int(input('Введите год написания книги: '))
            break
        except ValueError:
            print('Значение некорректно. Введите число.')
    id = generate_id(data)
    new_book = {
        'id': id,
        'title': title,
        'author': author,
        'year': year,
        'status': 'в наличии'
    }
    data[f'book_{id}'] = new_book
    save_data(data)
    print('Книга добавлена.')

def remove_book(data: dict) -> None:
    #print([(data[i],data[i]['id']) for i in data])
    while True:
        try:
            id = int(input('Введите id книги для удаления: '))
            break
        except ValueError:
            print('Значение некорректно. Введите число.')
    if id not in [data[i]['id'] for i in data]:
        print('Введите корректное значение id.')
        return remove_book(data)
    for i in data:
        if data[i]['id'] == id:
            del data[i]
        save_data(data)
        print('Книга удалена.')
        return None

def case_for_search(data: dict, field_: str) -> None:
    if field_ == 'year':
        while True:
            try:
                field = int(input(f'Введите {field_}: '))
                break
            except ValueError:
                print('Значение некорректно.')
        array = [int(data[i][field_]) for i in data]
    else:
        field = input(f'Введите {field_}: ')
        array = [data[i][field_] for i in data]
    if field not in array:
        print('Значение некорректно.')
        case_for_search(data, field_)
    else:
        for i in data:
            if data[i][field_] == field:
                print(f'id: {data[i]["id"]}, Название: {data[i]["title"]}, Автор: {data[i]["author"]}, Год: {data[i]["year"]}, Статус: {data[i]["status"]}')

def search_book(data: dict) -> None:
    while True:
        try:
            value = int(input('1 - Название, 2 - Автор, 3 - Год. Выберите параметр поиска: '))
            break
        except ValueError:
            print('Значение некорректно. Введите число.')
    if value not in [i for i in range(1, 4)]:
        print("Значение некорректно")
        return search_book(data)
    else:
        match value:
            case 1:
                case_for_search(data, field_='title')
            case 2:
                case_for_search(data, field_='author')
            case 3:
                case_for_search(data, field_='year')

def display_books(data: dict) -> None:
    if data:
        print('Cписок всех книг: ', end='\n\n')
        for i in data:
            print(
                f'id: {data[i]["id"]}, Название: {data[i]["title"]}, Автор: {data[i]["author"]}, Год: {data[i]["year"]}, Статус: {data[i]["status"]}')
    else:
        print('В библиотеке ни одной книги.')
def change_book_status(data: dict) -> None:
    while True:
        try:
            id = int(input('Введите id книги для обновления статуса: '))
            break
        except ValueError:
            print('Значение некорректно. Введите число.')
    if id not in [data[i]['id'] for i in data]:
        print('Введите корректное значение id.')
        return change_book_status(data)
    while True:
        status = input('Введите статус книги: ')
        if status.lower() in ['в наличии', 'выдана']:
            break
        else:
            print("Значение некорректно")
    for i in data:
        if data[i]['id'] == id:
            data[i]['status'] = status.lower()
            save_data(data)

def menu() -> None:
    try:
        with open('library.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = {}
    while True:
        print('Меню:\n1. Добавить книгу\n2. Удалить книгу\n3. Найти книгу.\n4. Показать все книги\n5. Изменить статус книги.\n6. Закончить программу')
        value = input('Выберите действие: ').strip()
        if value == '1': add_book(data)
        elif value == '2': remove_book(data)
        elif value == '3': search_book(data)
        elif value == '4': display_books(data)
        elif value == '5': change_book_status(data)
        elif value == '6': exit()
        else: print('Значение некорректно.')

if __name__ == '__main__':
    menu()