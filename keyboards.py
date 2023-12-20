from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------- Navigation inline keyboard ---------------------------------------------------------
navigation = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='Про коледж',
                          callback_data='about')
b2 = InlineKeyboardButton(text='Студенту',
                          callback_data='For student')
b3 = InlineKeyboardButton(text='Абітурієнту',
                          callback_data='For abiturient')
b4 = InlineKeyboardButton(text='Різне',
                          callback_data='Random shit')
b5 = InlineKeyboardButton(text='Контакти',
                          callback_data='Contacts')

navigation.add(b1, b2, b3, b4, b5)


# ------------------------------- Navigation inline keyboard ---------------------------------------------------------

# ------------------------------- Back to MainMenu inline keyboard ---------------------------------------------------
main_menu = InlineKeyboardMarkup()
goBack = InlineKeyboardButton(text='На головну',
                              callback_data='MainMenu')
main_menu.add(goBack)

# ------------------------------- Back to MainMenu inline keyboard ---------------------------------------------------

#-------------------------------- Contacts Area ----------------------------------------------------------------------
Contacts_text = """
Директор - (03-236) 3-40-90 \n 
Заступник директора з виховної роботи, Зав відділення - (03-236) 3-40-91 \n
Заступник директора з навчальної роботи - (03-236) 3-22-46 \n
Відділ кадрів - (03-236) 6-06-07 \n
Учительська - (03-236) 3-40-88 \n
Заочне відділення - (03-236) 3-44-50 \n
Факультет прикладного програмного забезпечення </b> - (03-236) 3-30-97 \n
Бухгалтерія - (03-236) 3-35-84 \n
Гуртожиток - (03-236) 3-31-50 \n
Прохідна - (03-236) 3-21-63 \n
Email - steti@ua.fm \n
Адреса - Львівська обл. м. Самбір, вул. С.Крушельницької, 7 \n
Питання на рахунок бота(Писати з приміткою "#бот) - @Vova_ss \n
"""

# ------------------------------------------------- For student area --------------------------------------------------

for_student_keyboard1 = InlineKeyboardMarkup(row_width=3)
schedule = InlineKeyboardButton(text='Розклад занять', callback_data='schedule')
timetable = InlineKeyboardButton(text='Розклад дзвінків', url='https://drive.google.com/file/d/1CPWb0brHLXRRBLwpo_Ugy1zmQRd-I402/view')
rating = InlineKeyboardButton(text='Рейтинг студентів', url='https://drive.google.com/drive/folders/1J5S3Q2JYWVuUgyIIvPdEvpGhI_wZILat')
changes = InlineKeyboardButton(text='Заміни', url='https://drive.google.com/file/d/13i5QaEs_eXXcDV7ouxCv3ndPWmFUr7_Z/view')
library = InlineKeyboardButton(text='Електронна бібліотека', callback_data='library')
for_student_keyboard1.add(schedule, timetable, rating, changes, library).add(goBack)

pick_cycle_keyboard = InlineKeyboardMarkup()
t_k_e = InlineKeyboardButton(text='Економіка/комерція/туризм', url='https://docs.google.com/spreadsheets/d/1yR46hj7_xAEXB9xIQ9DTr823Y7C7LkKY/edit#gid=1490852171')
programming = InlineKeyboardButton(text='Інженерія ПЗ', url='https://docs.google.com/spreadsheets/d/1kgEcnSjVD1yHkB8R6l-YcqemdKxlOKtM/edit#gid=183795053')
pick_cycle_keyboard.add(t_k_e, programming).add(goBack)

rating_tables = InlineKeyboardMarkup()
rating_link = InlineKeyboardButton(text='Рейтинг студентів', url='https://drive.google.com/drive/folders/1J5S3Q2JYWVuUgyIIvPdEvpGhI_wZILat')
rating_tables.add(rating_link)


cycle_comision_keyboard_part1 = InlineKeyboardMarkup(row_width=1)
economic_and_tourism = InlineKeyboardButton(text='Циклова комісія економіки та туризму', url='https://drive.google.com/drive/folders/1vTJF5NNcw4r_6i9OWL1KVt0CMaqufxP1')
commercial = InlineKeyboardButton(text='Циклова комісія комерційних дисциплін', url='https://drive.google.com/drive/folders/1ddd3QeVhpDKdUYbWiIF-YS4fMO1hpthv?usp=sharing')
maths = InlineKeyboardButton(text='Циклова комісія природничо-математичних дисциплін', url='https://drive.google.com/drive/folders/1YYjDz7acNgkMvWzBamK5ko9OPUmPN9AF?usp=sharing')
lang = InlineKeyboardButton(text='Циклова комісія мови та літератури', url='https://drive.google.com/drive/folders/1mREWfv4mHr1HQ433gCMVmZS5s8J7VrjJ?usp=sharing')
next_page = InlineKeyboardButton(text='▶️', callback_data='next page')
cycle_comision_keyboard_part1.add(economic_and_tourism, commercial, maths, lang, next_page)

cycle_comision_keyboard_part2 = InlineKeyboardMarkup(row_width=1)
engineering = InlineKeyboardButton(text='Циклова комісія інженерії програмного забезпечення', url='https://drive.google.com/drive/folders/1nEO6K0xrZEAzrUoLI4HVt7KaaUIUOQa5?usp=sharing')
PE = InlineKeyboardButton(text='Циклова комісія соціально-гуманітарних дисциплін та фізичного виховання', url='https://drive.google.com/drive/folders/1Af5xg2HM9xn3ypr79jcJOi_4mO3m9bv5?usp=sharing')
books_10grade = InlineKeyboardButton(text='Електронні підручники 10 клас', url='https://drive.google.com/drive/folders/1AenLeqh7cfA4-XChHWKOO9vsGAYrxspz?usp=sharing')
other_links = InlineKeyboardButton(text='Перелік електронних ресурсів та посилань', url='https://docs.google.com/document/d/1790Rjyr842S6xU4syum80tPaZmtPIUbP/edit?usp=sharing&ouid=106641847566370597167&rtpof=true&sd=true')
cycle_comision_keyboard_part2.add(engineering, PE, books_10grade, other_links)

# ----------------------------------------------- End of For student area ---------------------------------------------

# ----------------------------------------------- For abiturient area ------------------------------------------------
for_abiturient_keyboard = InlineKeyboardMarkup()
commision = InlineKeyboardButton(text='Приймальна комісія', url='https://saceit.org.ua/seclection-committee/')
ab_rating = InlineKeyboardButton(text='Рейтинг вступників', url='https://vstup.osvita.ua/r14/742/')
specialities = InlineKeyboardButton(text='Спеціальності', url='https://saceit.org.ua/specialities/')
courses = InlineKeyboardButton(text='Підготовчі курси', url='https://saceit.org.ua/courses/')
price = InlineKeyboardButton(text='Розмір оплати', url='https://drive.google.com/file/d/1kINoU2S2JsnRyMgOgTQcvprOcZA7NzL5/view')
for_abiturient_keyboard.add(commision, ab_rating, specialities, courses, price).add(goBack)
# ---------------------------------------------------------------------------------------------------------------------
