from datetime import date, datetime
from dotenv import load_dotenv
import fire
import json
import os
import re
import uuid


load_dotenv(".env")


def process(name):
    dataset = read_json(name)

    author_fixture = format_author_fixture(dataset)
    poem_fixture = format_poem_fixture(author_fixture, dataset)

    create_json(author_fixture, "author_fixture_")
    create_json(poem_fixture, "poem_fixture_")

    return "Successfully created fixtures."


def format_author_fixture(dataset):
    temp_author_list = sorted(list(set([i["author"] for i in dataset])))

    return [
        {
            "pk": str(uuid.uuid4()),
            "model": "db.Author",
            "fields": {
                "name": i,
                "user_id": os.getenv("SUPERUSER_ID"),
                "created_on": str(date.today()),
                "updated_on": str(date.today()),
            },
        }
        for i in temp_author_list
    ]


def format_poem_fixture(author_fixture, dataset):
    poem_list = []

    index = 0
    for i in dataset:
        matched_author = [
            x["pk"] if x["fields"]["name"] == i["author"] else None
            for x in author_fixture
        ]

        author_id = list(filter(None, matched_author))[0]

        poem_list.append(
            {
                "pk": str(uuid.uuid4()),
                "model": "db.Poem",
                "fields": {
                    "age": i["age"],
                    "author_id": author_id,
                    "content": i["content"],
                    "title": i["poem name"],
                    "type": i["type"],
                    "user_id": os.getenv("SUPERUSER_ID"),
                    "created_on": str(date.today()),
                    "updated_on": str(date.today()),
                },
            }
        )

        index += 1

    return poem_list


def create_json(datalist, prefix):
    timestamp = str(datetime.now())
    pattern = "[" + "".join([":", " ", "-", "."]) + "]"
    clean_timestamp = re.sub(pattern, "", timestamp)

    f = open(f"../backend/core/{prefix}{clean_timestamp}.json", "a")

    f.write(json.dumps(datalist, indent=2))
    f.close()


def read_json(name):
    f = open(f"{name}.json")
    data = json.load(f)

    f.close()

    return data


if __name__ == "__main__":
    fire.Fire(process)
