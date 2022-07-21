from format_dataset import create_json, read_json


from datetime import date
from dotenv import load_dotenv
import fire
import os
import uuid


load_dotenv(".env")


def format(name):
    dataset = read_json(name)

    dataset_authors = [i["author"] for i in dataset]

    author_list = sorted(list(set(dataset_authors)))

    formatted = [
        {
            "id": str(uuid.uuid4()),
            "model": "db.Author",
            "fields": {
                "name": i,
                "user_id": os.getenv("SUPERUSER_ID"),
                "created_on": str(date.today()),
                "updated_on": str(date.today()),
            },
        }
        for i in author_list
    ]

    create_json(formatted, "author_seed_")

    return "Successfully created seed file"


if __name__ == "__main__":
    fire.Fire(format)
