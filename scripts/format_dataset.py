# Formats the dataset for seeding

from datetime import date, datetime
from dotenv import load_dotenv


import fire
import json
import os
import re
import uuid


load_dotenv(".env")

def format(name):
    dataset = read_json(name)

    formatted = [
        {
            "id": str(uuid.uuid4()),
            "model": "db.Poem",
            "fields": {
                "age": i["age"],
                "author": i["author"],
                "content": i["content"],
                "title": i["poem name"],
                "type": i["type"],
                "user_id": os.getenv("SUPERUSER_ID"),
                "created_on": str(date.today()),
                "updated_on": str(date.today()),
            },
        }
        for i in dataset
    ]

    create_json(formatted)

    return "Successfully created seed file"

def create_json(datalist):
    timestamp = str(datetime.now())
    pattern = "[" + "".join([":", " ", "-", "."]) + "]"
    clean_timestamp = re.sub(pattern, "", timestamp)

    f = open(f"../backend/core/poem_seed_{clean_timestamp}.json", "a")

    f.write(json.dumps(datalist, indent=2))
    f.close()

def read_json(name):
    f = open(f"{name}.json")
    data = json.load(f)

    f.close()

    return data


if __name__ == "__main__":
    fire.Fire(format)
