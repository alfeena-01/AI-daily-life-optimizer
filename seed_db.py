import datetime
from utils.db_manager import insert_activity

for i in range(10):
    d = datetime.date.today() - datetime.timedelta(days=i)
    insert_activity(d, 7 + (i % 3)*0.5, 5000 + i*300, 6 + (i % 2)*0.5)
from utils.db_manager import get_all_activity
print(get_all_activity())
