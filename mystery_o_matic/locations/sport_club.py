def get_data():
    intro = {}
    intro["en"] = " are transported into <b>an empty sport club</b> at night!"
    intro["es"] = " han sido transportados a <b>un club deportivo desierto</b> por la noche!"
    intro["ru"] = " перенеслись в <b>пустой спортивный клуб</b> ночью!"

    labels = {}
    labels["en"] = {
        "GYM": "gym",
        "POOL": "swimming pool",
        "SAUNA": "sauna",
        "COURT": "sports court",
        "LOUNGE": "lounge",
    }
    labels["es"] = {
        "GYM": "el gimnasio",
        "POOL": "la piscina",
        "SAUNA": "la sauna",
        "COURT": "la cancha deportiva",
        "LOUNGE": "el salón",
    }
    labels["ru"] = {
        "GYM": "тренажёрный зал",
        "POOL": "бассейн",
        "SAUNA": "сауна",
        "COURT": "спортивная площадка",
        "LOUNGE": "зал отдыха",
    }
    labels["ru_loc"] = {
        "GYM": "тренажёрном зале",
        "POOL": "бассейне",
        "SAUNA": "сауне",
        "COURT": "спортивной площадке",
        "LOUNGE": "зале отдыха",
    }
    labels["ru_gen"] = {
        "GYM": "тренажёрного зала",
        "POOL": "бассейна",
        "SAUNA": "сауны",
        "COURT": "спортивной площадки",
        "LOUNGE": "зала отдыха",
    }

    representations = {
        "GYM": "💪",
        "POOL": "🏊",
        "SAUNA": "🧖",
        "COURT": "🏀",
        "LOUNGE": "🛋️",
    }

    activities = {
        "GYM": [
            {"en": "heard a voice coming from the gym (💪)", "es": "escuché una voz que venía desde el gimnasio (💪)", "ru": "услышал(а) голос из тренажёрного зала (💪)"}
        ],
        "POOL": [
            {"en": "heard a voice coming from the swimming pool (🏊)", "es": "escuché una voz que venía desde la piscina (🏊)", "ru": "услышал(а) голос из бассейна (🏊)"}
        ],
        "SAUNA": [
            {"en": "heard a voice coming from the sauna (🧖)", "es": "escuché una voz que venía desde la sauna (🧖)", "ru": "услышал(а) голос из сауны (🧖)"}
        ],
        "COURT": [
            {"en": "heard a voice coming from the sports court (🏀)", "es": "escuché una voz que venía desde la cancha deportiva (🏀)", "ru": "услышал(а) голос со спортивной площадки (🏀)"}
        ],
        "LOUNGE": [
            {"en": "heard a voice coming from the lounge (🛋️)", "es": "escuché una voz que venía desde el salón (🛋️)", "ru": "услышал(а) голос из зала отдыха (🛋️)"}
        ],
    }

    return (intro, labels, representations, activities)
