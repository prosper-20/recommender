from faker import Faker
import csv
from django.conf import settings
from pprint import pprint


MOVIES_MEDTDATA_CSV = settings.DATA_DIR / "movies_metadata.csv"

def load_movie_data(limit=10):
    with open(MOVIES_MEDTDATA_CSV, newline="", encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            pprint(row)
            if i + 1> limit:
                break


def get_fake_profiles(count=10):
    fake = Faker()

    for _ in range(count):
        user_data = []
        profile = fake.profile()
        data = {
            "username": profile.get('username'),
            "email": profile.get('mail'),
            # "password": make_password(fake.password(length=15)),
            "is_active": True
        }
        if 'name' in profile:
            fname, lname = profile.get("name").split(" ")[:2]
            data['first_name'] = fname
            data['last_name']   = lname
        user_data.append(data)
        return user_data
        