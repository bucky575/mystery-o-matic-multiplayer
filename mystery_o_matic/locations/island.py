def get_data():
    intro = {}
    intro["en"] = " are transported to <b>a deserted tropical island</b>!"
    intro["es"] = " han sido transportados a <b>una isla tropical desierta</b>!"
    intro["ru"] = " перенеслись на <b>необитаемый тропический остров</b>!"

    labels = {}
    labels["en"] = {
        "BEACH": "beach",
        "JUNGLE": "jungle",
        "CAVE": "cave",
        "CLIFF": "cliff",
        "VOLCANO": "volcano",
    }
    labels["es"] = {
        "BEACH": "la playa",
        "JUNGLE": "la jungla",
        "CAVE": "la cueva",
        "CLIFF": "el acantilado",
        "VOLCANO": "el volcán",
    }
    labels["ru"] = {
        "BEACH": "пляж",
        "JUNGLE": "джунгли",
        "CAVE": "пещера",
        "CLIFF": "утёс",
        "VOLCANO": "вулкан",
    }
    labels["ru_loc"] = {
        "BEACH": "пляже",
        "JUNGLE": "джунглях",
        "CAVE": "пещере",
        "CLIFF": "утёсе",
        "VOLCANO": "вулкане",
    }
    labels["ru_gen"] = {
        "BEACH": "пляжа",
        "JUNGLE": "джунглей",
        "CAVE": "пещеры",
        "CLIFF": "утёса",
        "VOLCANO": "вулкана",
    }

    representations = {
        "BEACH": "🏖️",
        "JUNGLE": "🌴",
        "CAVE": "🦇",
        "CLIFF": "⛰️",
        "VOLCANO": "🌋",
    }

    activities = {
        "BEACH": [
            {"en": "looked around and saw someone collecting seashells (🏖️)", "es": "miré alrededor y vi a alguien recogiendo conchas marinas (🏖️)", "ru": "осмотрелся(ась) и увидел(а), как кто-то собирает ракушки (🏖️)"},
        ],
        "JUNGLE": [
            {"en": "heard someone chopping wood in the jungle (🌴)", "es": "escuché a alguien cortando leña en la jungla (🌴)", "ru": "услышал(а), как кто-то рубит дрова в джунглях (🌴)"},
        ],
        "CAVE": [
            {"en": "heard a voice coming from the cave (🦇)", "es": "escuché una voz que venía desde la cueva (🦇)", "ru": "услышал(а) голос из пещеры (🦇)"},
        ],
        "CLIFF": [
            {"en": "saw someone climbing the cliff (⛰️)", "es": "vi a alguien escalando el acantilado (⛰️)", "ru": "увидел(а), как кто-то карабкается на утёс (⛰️)"},
        ],
        "VOLCANO": [
            {"en": "saw someone inspecting the volcano summit (🌋)", "es": "vi a alguien inspeccionando la cima del volcán (🌋)", "ru": "увидел(а), как кто-то осматривает кратер вулкана (🌋)"},
        ],
    }

    return (intro, labels, representations, activities)
