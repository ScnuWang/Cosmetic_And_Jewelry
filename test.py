from datetime import datetime
from models import Cj_Model


# product = Cj_Model.Cj_Brand(brand_name='Swarosvki',update_time=datetime.now())
# session = Cj_Model.DBSession()
# session.add(product)
# session.commit()
# session.close()

def disemvowel(string):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    byts_string = bytes(string,encoding='utf-8')
    print(byts_string)
    print(str(byts_string))





disemvowel('This website is for losers LOL!')