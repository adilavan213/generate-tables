import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('he_IL')

def generate_fake_hrp1001_data_option2(num_rows=100):
    data = []

    for i in range(num_rows):
        object_id = 6813000 + random.randint(0, 999)
        pv = "01"
        s1 = random.choice(["A", "B"])
        rel = f"{random.randint(1, 999):03}"
        s2 = "1"
        pr = "S"
        start_date = datetime.today() - timedelta(days=random.randint(1000, 5000))
        end_date = start_date + timedelta(days=random.randint(100, 1500))
        variation_field = f"0{random.randint(22500000, 22599999)}"
        rno = f"0 {random.randint(22500000, 22599999)}"
        infotype = 1001
        objT_objID = f"S 0{object_id}"
        subtype = random.choice(["A003", "A002", "A008", "B001"])
        changed_on = end_date + timedelta(days=random.randint(1, 200))
        user_name = fake.user_name().upper()

        row = [
            "S",                  # Ob
            object_id,            # Object ID
            pv,                   # PV
            s1,                   # iStat
            rel,                  # Rel
            pr,                   # Pr
            start_date.strftime("%d.%m.%Y"),  # Start Date
            end_date.strftime("%d.%m.%Y"),    # End Date
            variation_field,      # Variation field
            infotype,             # Infoty.
            objT_objID,           # ObjT/objID
            subtype,              # Subtyp
            changed_on.strftime("%d.%m.%Y"),  # Changed On
            user_name ,            # User Name
            "s"                     # rel_object_type
        ]
        data.append(row)

    columns = [
        "Ob", "Object ID", "PV", "ISTAT", "Rel", "Pr",
        "Start Date", "End Date", "Variation field",
        "Infoty.", "ObjT/objID", "Subtyp", "Changed On", "User Name","rel_object_type"
    ]

    df = pd.DataFrame(data, columns=columns)

    # יצירת עמודת SOBID בפורמט "S 0{object_id}"
    object_ids = df["Object ID"].tolist()
    sobid_list = []
    for oid in object_ids:
        possible_links = [x for x in object_ids if x != oid and abs(x - oid) <= 10]
        if possible_links:
            linked_oid = random.choice(possible_links)
            sobid = f" {linked_oid}"
        else:
            sobid = None
        sobid_list.append(sobid)

    df["SOBID"] = sobid_list

    return df

# יצירת הנתונים
df_option2 = generate_fake_hrp1001_data_option2(100)

# הדפסת דוגמה
print(df_option2.head(10))

# שמירה לקובץ אם רוצים
df_option2.to_csv(r"C:\Users\use\Desktop\hrp1001_fake_data_option2.csv", index=False, sep='\t')
