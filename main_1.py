from ya_sched import Ya_sched
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
sched_api = Ya_sched(api_key=API_KEY)
print(sched_api.get_city_info
