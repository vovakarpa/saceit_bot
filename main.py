from aiogram import Bot, Dispatcher, types, executor
import keyboards as kb
from config import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бота запущено')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://scontent.flwo3-1.fna.fbcdn.net/v/t39.30808-6/274607137_1315462545638395_5905418142003772471_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=I0BHuAFEBvoAX8s4kjm&_nc_ht=scontent.flwo3-1.fna&oh=00_AfATz89j4u4qMBk1ejktjNTe9ti7DmNBKrJQb7TSVa4YBA&oe=63ED6783',
                         caption='Вас вітає бот СФКЕтІТ')
    await bot.send_message(chat_id=message.chat.id,
                           text='Виберіть категорію',
                           reply_markup=kb.navigation)

# ------------------------------- About area --------------------------------------------------------------

@dp.callback_query_handler(text='about')
async def about_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                            text='Самбірський фаховий коледж економіки та інформаційних технологій – державний навчальний заклад, який готує фахівців освітньо-кваліфікаційного рівня «молодший спеціаліст» та «фаховий молодший бакалавр» відповідно до  потреб ринку праці. Це сучасний навчальний заклад, який крокує в ногу з життям.',
                            reply_markup=kb.main_menu)

# ------------------------------- End of about area --------------------------------------------------------------

# ------------------------------------------- Main Menu area -------------------------------------------------------

@dp.callback_query_handler(text='MainMenu')
async def go_to_mainMenu(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Виберіть куди перейти',
                           reply_markup=kb.navigation)

# ------------------------------------------- End of Main Menu area -------------------------------------------------

# ------------------------------------------------Contacts area-------------------------------------------------------

@dp.callback_query_handler(text='Contacts')
async def contacts_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text=kb.Contacts_text,
                           reply_markup=kb.main_menu)

# ------------------------------------------End of contacts area-------------------------------------------------------

# ------------------------------------------- For student area ------------------------------------------------------

@dp.callback_query_handler(text='For student')
async def forStudent_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Виберіть категорію',
                           reply_markup=kb.for_student_keyboard1)

@dp.callback_query_handler(text='schedule')
async def schedule_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Виберіть вашу категорію',
                           reply_markup=kb.pick_cycle_keyboard)

@dp.callback_query_handler(text='rating')
async def rating_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Ви можете переглянути актуальний рейтинг студентів за посиланням',
                           reply_markup=kb.rating_tables)


@dp.callback_query_handler(text='library')
async def library_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Виберіть циклову комісію',
                           reply_markup=kb.cycle_comision_keyboard_part1)

@dp.callback_query_handler(text='next page')
async def next_page_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Виберіть циклову комісію',
                           reply_markup=kb.cycle_comision_keyboard_part2)



# ------------------------------------------ End of for student area --------------------------------------------------

# -------------------------------------------- For abiturient area ---------------------------------------------------

@dp.callback_query_handler(text='For abiturient')
async def abiturient_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Виберіть підкатегорію',
                           reply_markup=kb.for_abiturient_keyboard)

# --------------------------------------------- End of For abiturient area --------------------------------------------


# -------------------------------------------- Others area -----------------------------------------------------------
@dp.callback_query_handler(text='Random shit')
async def others_command(callback: types.CallbackQuery):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Функція в процесі розробки. Променів добра вам ❤️',
                           reply_markup=kb.main_menu)

# ------------------------------------------- End of Others area ------------------------------------------------------
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)