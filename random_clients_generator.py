#!/usr/bin/env python
# coding: utf-8

# In[42]:




def rand_house(city): # Func that generates random house num or house + apt num depends where it is located 

    import random          
    if 'город' in city.lower():
        house = 'д. ' + str(random.randint(1,100)) +' кв. '+ str(random.randint(1,100))
    else:
        house = 'дом номер ' + str(random.randint(1,100)) +' '
    return house

def rand_dob(): # Func for creating a single random date of birth

    import datetime
    import random
    d1, d2 = datetime.date(1950,1,1), datetime.date(2006,1,1)
    delta = (d2-d1).days   
    return d1+ datetime.timedelta(days = random.randint(0, delta))

def rand_phone(): # Func that returns random phone number

    import random
    phone = '+7 ('
    for i in range(10):
        phone += str(random.randint(0,9))
        if i == 2:
            phone += ') '
        elif i in (5, 7):
            phone += '-'
    return phone

def rand_email(name, dob): # Func for creating random email based on family name and date of birth  
  
    from dicts import translit_dict
    import random
    email = ''
    name1 = name.split()[0].lower()
    for num in range(random.randint(len(name1)//2, len(name1))):
        if name1[num] in translit_dict:
            email += translit_dict[name1[num]]
    email += str(dob.year)[2:] + '@' + random.choice([
        'bk.ru', 'gmail.com', 'mail.ru', 'yandex.ry', 'inbox.ru', 'hotmail.com', 'live.com'])       
    return email

def accounts_generator(): # Func generates savigs and check acc   
 
    import random
    savings_acc = random.randint(10**4, 10**random.randint(5,9))/100*random.randint(0,1)
    check_acc = random.randint(10**4, 10**random.randint(5,9))/100
    return savings_acc, check_acc

def random_client(): # Func for generating multiple client data items
    
    import dicts
    import random
    import datetime
    
    # Generating gender and selecting name dictionaries
    gen=random.choice([ 
        [dicts.male_names_list, dicts.male_father_names_list, dicts.male_family_names_list], 
        [dicts.female_names_list, dicts.female_father_names_list, dicts.female_family_names_list]])
    
    # Generating full name
    name =random.choice(gen[2]) + ' ' + random.choice(gen[0]) + ' ' + random.choice(gen[1]) 
    
    # Generating city, region and index
    index = random.choice(list(dicts.city_dict.keys()))
    city = ' '.join(dicts.city_dict[index][0:2])
    region = ' '.join(dicts.city_dict[index][2:])
                          
    # Generating street name
    street = random.choice(dicts.strt_dict)
    
    # Generating street address
    house = rand_house(city)
    
    # Generating date of birth
    dob = rand_dob()
    dob_str = dob.strftime('%d.%m.%Y')                      
    # Generating phone number
    phone = rand_phone()
                          
    # Generating email    
    email = rand_email(name, dob)
    
    # Generating accounts
    savings_acc, check_acc = accounts_generator()
    total = savings_acc + check_acc
                          
    return {'name': name, 'street': street, 'house': house, 'city': city, 'region': region, 'index': index, 'dob_dt': dob, 'dob_str': dob_str, 'phone': phone, 'email': email, 'savings_acc': savings_acc, 'check_acc': check_acc, 'total': total}


if __name__ == "__main__":
    client = random_client()
    print(client)