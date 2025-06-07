import json
import os

class Assistant:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.notes = json.load(f)
        else:
            self.notes = []

    def save_notes(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.notes, f, indent=2, ensure_ascii=False)

    def add_note(self, note: str):
        self.notes.append(note)
        self.save_notes()
        print("Нотатку додано.")

    def list_notes(self):
        if not self.notes:
            print("Список нотаток порожній.")
        else:
            print("Нотатки:")
            for i, note in enumerate(self.notes, 1):
                print(f"{i}. {note}")

    def search_notes(self, keyword: str):
        found = [note for note in self.notes if keyword.lower() in note.lower()]
        if not found:
            print("Нічого не знайдено.")
        else:
            print("Результати пошуку:")
            for i, note in enumerate(found, 1):
                print(f"{i}. {note}")
