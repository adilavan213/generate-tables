import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('he_IL')

# הגדרות
num_objects = 100  # מספר מזהי אובייקט
max_rows_per_object = 5  # כמה תתי-סוגים לכל אובייקט

rows = []

for i in range(num_objects):
    object_id = 6817000 + i
    subtypes = random.sample(range(1, 50), random.randint(2, max_rows_per_object))

    for sub in subtypes:
        # תאריכים מדורגים לפי מזהה האובייקט
        base_date = datetime(2010, 1, 1) + timedelta(days=i*30 + sub*15)
        end_date = base_date + timedelta(days=random.randint(180, 2000))
        
        row = [
            "01",                                # PV
            "S",                                 # Ob
            object_id,                           # Object ID
            f"{sub:04}",                         # STy.
            1,                                   # istat
            base_date.strftime("%d.%m.%Y"),      # Start Date
            end_date.strftime("%d.%m.%Y"),       # End Date                         # Var.field, RNo
            9500,                                # Infoty.
            f"S {object_id}",                    # ObjT/objID
            fake.date_between(start_date='-2y', end_date='today').strftime("%d.%m.%Y"),  # Changed On
            fake.user_name()                     # User Name
        ]
        rows.append(row)

columns = [
    "PV", "Ob", "Object ID", "STy.", "istat", "Start Date", "End Date",
     "Infoty.", "ObjT/objID", "Changed On", "User Name"
]

df = pd.DataFrame(rows, columns=columns)

# הצגה
print(df.head(13))

# שמירה כ־CSV
df.to_csv(r"C:\Users\use\Desktop\hrp9500_fake_data2.xlsx", index=False, sep='\t')

