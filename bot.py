import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from assistant import Assistant  

bot = Bot(token='7619488688:AAEczfDybXXdDa0_1NriSA99VN3MEEYlkLs')  
dp = Dispatcher(storage=MemoryStorage())
assistant = Assistant()

# Стан машини
class AddNoteState(StatesGroup):
    waiting_for_note = State()

class SearchNoteState(StatesGroup):
    waiting_for_keyword = State()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привіт! Я асистент. Використай /add, /list або /search.")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Команди:\n/add — додати нотатку\n/list — показати всі\n/search — знайти нотатки")

@dp.message(Command("add"))
async def cmd_add(message: Message, state: FSMContext):
    await message.answer("Введіть текст нотатки:")
    await state.set_state(AddNoteState.waiting_for_note)

@dp.message(AddNoteState.waiting_for_note)
async def process_add_note(message: Message, state: FSMContext):
    assistant.add_note(message.text)
    await message.answer("Нотатку додано ✅")
    await state.clear()

@dp.message(Command("list"))
async def cmd_list(message: Message):
    notes = assistant.notes
    if not notes:
        await message.answer("Список нотаток порожній.")
    else:
        text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(notes)])
        await message.answer("Нотатки:\n" + text)

@dp.message(Command("search"))
async def cmd_search(message: Message, state: FSMContext):
    await message.answer("Введіть ключове слово для пошуку:")
    await state.set_state(SearchNoteState.waiting_for_keyword)

@dp.message(SearchNoteState.waiting_for_keyword)
async def process_search(message: Message, state: FSMContext):
    keyword = message.text
    found = [note for note in assistant.notes if keyword.lower() in note.lower()]
    if not found:
        await message.answer("Нічого не знайдено.")
    else:
        text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(found)])
        await message.answer("Результати пошуку:\n" + text)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
