import json
import time
import os
from datetime import datetime

FILE = "data/user_activity.json"

def save_activity(username, role, session_start, dashboard_time):
    os.makedirs("data", exist_ok=True)

    logout_time = time.time()
    total_time = logout_time - session_start

    record = {
        "username": username,
        "role": role,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "login_time": datetime.fromtimestamp(session_start).strftime("%H:%M:%S"),
        "logout_time": datetime.fromtimestamp(logout_time).strftime("%H:%M:%S"),
        "dashboard_time_sec": round(dashboard_time, 2),
        "total_time_sec": round(total_time, 2)
    }

    with open(FILE, "a") as f:
        json.dump(record, f)
        f.write("\n")