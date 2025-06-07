from assistant import Assistant

def main():
    assistant = Assistant()

    print("Консольний асистент. Команди: /add, /list, /search, /exit")

    while True:
        command = input(">>> ").strip()

        if command == "/add":
            note = input("Введіть нотатку: ")
            assistant.add_note(note)

        elif command == "/list":
            assistant.list_notes()

        elif command == "/search":
            keyword = input("Ключове слово для пошуку: ")
            assistant.search_notes(keyword)

        elif command == "/exit":
            print("До побачення!")
            break

        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
