Rep consists of 2 files - file (dicts.py) with dictionaries and lists of possible particles of names and addreses and file (random_clients_generator.py) with functions, gathering and randomising data from the first file.

You can launch file No 2 (random_clients_generator.py) from terminal and get a sample of random client personal data in form of a dictionary.
You also can import random_clients_generator.py and use it's main function (random_client()) along with i.e. a SQL client to generate a client data base.
Here is what the client data consists of:

{
'name': 'Ларионов Кузьма Самуилович', 
'street': 'улица Прибрежная', 
'house': 'д. 59 кв. 53', 
'city': 'город Нытва', 
'region': 'Пермский край Приволжский Федеральный округ', 
'index': '979025', 
'dob_dt': datetime.date(1959, 2, 6), 
'dob_str': '06.02.1959', 
'phone': '+7 (034) 053-65-99', 
'email': 'lari59@bk.ru', 
'savings_acc': 9787955.14, 
'check_acc': 779.14, 
'total': 9788734.280000001
}

A few notes here - I put 2 types of date of birth data here - one in str and one in datetime format, so its possible to use it as it is as well as pull day, month, etc from it.
Last 3 items in dictionary are bank account data.

Enjoy.
