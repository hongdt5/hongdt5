# 1
import time
import datetime
from datetime import datetime as dt
def day_diff(release_date, code_complete_day):
    date_1="%d/%m/%Y"
    date_2="Y-%d-%m"
    d1 = dt.strptime(release_date, date_1)
    d2 = dt.strptime(code_complete_day,date_2)
    delta= abs(d1-d2)
    return (delta.days)
# 2
def alpha_num(sentence):
    wordsinsentence = sentence.plit(' ')
    


