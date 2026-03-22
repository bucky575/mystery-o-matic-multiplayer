def get_data():
    intro = {}
    intro["en"] = " are transported into <b>an abandoned zoo</b> at night!"
    intro["es"] = " han sido transportados a <b>un zoológico abandonado</b> por la noche!"
    intro["ru"] = " перенеслись в <b>заброшенный зоопарк</b> ночью!"

    labels = {}
    labels["en"] = {
        "LION ENCLOSURE": "lion enclosure",
        "REPTILE HOUSE": "reptile house",
        "AVIARY": "aviary",
        "MONKEY ISLAND": "monkey island",
        "AQUARIUM": "aquarium",
    }
    labels["es"] = {
        "LION ENCLOSURE": "el recinto de leones",
        "REPTILE HOUSE": "la casa de reptiles",
        "AVIARY": "el aviario",
        "MONKEY ISLAND": "la isla de monos",
        "AQUARIUM": "el acuario",
    }
    labels["ru"] = {
        "LION ENCLOSURE": "вольер львов",
        "REPTILE HOUSE": "террариум",
        "AVIARY": "вольер птиц",
        "MONKEY ISLAND": "остров обезьян",
        "AQUARIUM": "аквариум",
    }
    labels["ru_loc"] = {
        "LION ENCLOSURE": "вольере львов",
        "REPTILE HOUSE": "террариуме",
        "AVIARY": "вольере птиц",
        "MONKEY ISLAND": "острове обезьян",
        "AQUARIUM": "аквариуме",
    }
    labels["ru_gen"] = {
        "LION ENCLOSURE": "вольера львов",
        "REPTILE HOUSE": "террариума",
        "AVIARY": "вольера птиц",
        "MONKEY ISLAND": "острова обезьян",
        "AQUARIUM": "аквариума",
    }

    representations = {
        "LION ENCLOSURE": "🦁",
        "REPTILE HOUSE": "🦎",
        "AVIARY": "🦜",
        "MONKEY ISLAND": "🐒",
        "AQUARIUM": "🐠",
    }

    activities = {}

    return (intro, labels, representations, activities)
