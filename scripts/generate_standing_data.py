from format_dataset import read_json


import fire
import yaml


def generate_yaml(name):
    dataset = read_json(name)

    age_list = []
    type_list = []

    for i in dataset:
        age_list.append(i["age"])
        type_list.append(i["type"])

    create_json(
        {
            "ages": sorted(list(set(age_list))),
            "types": sorted(list(set(type_list))),
        }
    )


def create_json(datalist):
    f = open(f"../backend/core/lib/yamls/standing_data.yml", "a")

    f.write(yaml.dump(datalist, indent=2))
    f.close()


if __name__ == "__main__":
    fire.Fire(generate_yaml)
