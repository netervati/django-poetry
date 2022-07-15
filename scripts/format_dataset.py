# Formats the dataset for seeding

from datetime import datetime

import fire
import json
import re
import uuid


def format(name):
    dataset = read_json(name)

    formatted = [
        {
            "id": str(uuid.uuid4()),
            "model": "",
            "fields": {
                "age": i["age"],
                "author": i["author"],
                "content": i["content"],
                "title": i["poem name"],
                "type": i["type"],
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

    f = open(f"poem_seed_{clean_timestamp}.json", "a")

    f.write(json.dumps(datalist, indent=2))
    f.close()

def read_json(name):
    f = open(f"{name}.json")
    data = json.load(f)

    f.close()

    return data


if __name__ == "__main__":
    fire.Fire(format)
