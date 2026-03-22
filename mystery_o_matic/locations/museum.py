def get_data():
    intro = {}
    intro["en"] = " are transported into <b>an empty museum at night</b>!"
    intro["es"] = " han sido transportados a <b>un museo vacío por la noche</b>!"
    intro["ru"] = " перенеслись в <b>пустой музей ночью</b>!"

    labels = {}
    labels["en"] = {
        "DINOSAUR EXHIBIT": "dinosaur exhibit",
        "EGYPTIAN EXHIBIT": "egyptian exhibit",
        "MEDIEVAL EXHIBIT": "medieval exhibit",
        "SPACE EXHIBIT": "space exhibit",
        "OCEAN EXHIBIT": "ocean exhibit",
    }
    labels["es"] = {
        "DINOSAUR EXHIBIT": "la exhibición de dinosaurios",
        "EGYPTIAN EXHIBIT": "la exhibición egipcia",
        "MEDIEVAL EXHIBIT": "la exhibición medieval",
        "SPACE EXHIBIT": "la exhibición espacial",
        "OCEAN EXHIBIT": "la exhibición oceánica",
    }
    labels["ru"] = {
        "DINOSAUR EXHIBIT": "зал динозавров",
        "EGYPTIAN EXHIBIT": "египетский зал",
        "MEDIEVAL EXHIBIT": "средневековый зал",
        "SPACE EXHIBIT": "космический зал",
        "OCEAN EXHIBIT": "океанский зал",
    }
    labels["ru_loc"] = {
        "DINOSAUR EXHIBIT": "зале динозавров",
        "EGYPTIAN EXHIBIT": "египетском зале",
        "MEDIEVAL EXHIBIT": "средневековом зале",
        "SPACE EXHIBIT": "космическом зале",
        "OCEAN EXHIBIT": "океанском зале",
    }
    labels["ru_gen"] = {
        "DINOSAUR EXHIBIT": "зала динозавров",
        "EGYPTIAN EXHIBIT": "египетского зала",
        "MEDIEVAL EXHIBIT": "средневекового зала",
        "SPACE EXHIBIT": "космического зала",
        "OCEAN EXHIBIT": "океанского зала",
    }

    representations = {
        "DINOSAUR EXHIBIT": "🦖",
        "EGYPTIAN EXHIBIT": "⚱️",
        "MEDIEVAL EXHIBIT": "🛡️",
        "SPACE EXHIBIT": "🪐",
        "OCEAN EXHIBIT": "🐠",
    }

    activities = {
        "DINOSAUR EXHIBIT": [
            {"en": "heard a voice coming from the dinosaur exhibit (🦖)", "es": "escuché una voz que venía desde la exhibición de dinosaurios (🦖)", "ru": "услышал(а) голос из зала динозавров (🦖)"}
        ],
        "EGYPTIAN EXHIBIT": [
            {"en": "heard a voice coming from the egyptian exhibit (⚱️)", "es": "escuché una voz que venía desde la exhibición egipcia (⚱️)", "ru": "услышал(а) голос из египетского зала (⚱️)"}
        ],
        "MEDIEVAL EXHIBIT": [
            {"en": "heard a voice coming from the medieval exhibit (🛡️)", "es": "escuché una voz que venía desde la exhibición medieval (🛡️)", "ru": "услышал(а) голос из средневекового зала (🛡️)"}
        ],
        "SPACE EXHIBIT": [
            {"en": "heard a voice coming from the space exhibit (🪐)", "es": "escuché una voz que venía desde la exhibición espacial (🪐)", "ru": "услышал(а) голос из космического зала (🪐)"}
        ],
        "OCEAN EXHIBIT": [
            {"en": "heard a voice coming from the ocean exhibit (🐠)", "es": "escuché una voz que venía desde la exhibición oceánica (🐠)", "ru": "услышал(а) голос из океанского зала (🐠)"}
        ],
    }

    return (intro, labels, representations, activities)
