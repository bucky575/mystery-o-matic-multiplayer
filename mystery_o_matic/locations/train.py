def get_data():
    intro = {}
    intro["en"] = " are transported back in time to <b>the famous Orient Express</b> during its last voyage!"
    intro["es"] = " han sido transportados en el tiempo al <b>famoso Orient Express</b> durante su último viaje!"
    intro["ru"] = " перенеслись в прошлое на <b>знаменитый Восточный экспресс</b> во время его последнего рейса!"

    labels = {}
    labels["en"] = {
        "LOCOMOTIVE": "locomotive",
        "LUGGAGE": "luggage carriage",
        "DINING": "dining carriage",
        "SLEEPING": "sleeping carriage",
        "LOUNGE": "lounge carriage",
    }
    labels["es"] = {
        "LOCOMOTIVE": "la locomotora",
        "LUGGAGE": "el vagón de equipaje",
        "DINING": "el vagón comedor",
        "SLEEPING": "el vagón dormitorio",
        "LOUNGE": "el vagón salón",
    }
    labels["ru"] = {
        "LOCOMOTIVE": "локомотив",
        "LUGGAGE": "багажный вагон",
        "DINING": "вагон-ресторан",
        "SLEEPING": "спальный вагон",
        "LOUNGE": "салон-вагон",
    }
    labels["ru_loc"] = {
        "LOCOMOTIVE": "локомотиве",
        "LUGGAGE": "багажном вагоне",
        "DINING": "вагоне-ресторане",
        "SLEEPING": "спальном вагоне",
        "LOUNGE": "салоне-вагоне",
    }
    labels["ru_gen"] = {
        "LOCOMOTIVE": "локомотива",
        "LUGGAGE": "багажного вагона",
        "DINING": "вагона-ресторана",
        "SLEEPING": "спального вагона",
        "LOUNGE": "салона-вагона",
    }

    representations = {
        "LOCOMOTIVE": "🚂",
        "LUGGAGE": "🧳",
        "DINING": "🍽️",
        "SLEEPING": "🛌",
        "LOUNGE": "🪑",
    }

    activities = {
        "LOCOMOTIVE": [
            {"en": "glanced out the window and saw someone shoveling coal into the locomotive's furnace (🚂)", "es": "miré por la ventana y vi a alguien echando carbón al horno de la locomotora (🚂)", "ru": "взглянул(а) в окно и увидел(а), как кто-то бросает уголь в топку локомотива (🚂)"},
            {"en": "heard a loud clang of tools in the locomotive (🚂)", "es": "escuché un golpe fuerte de herramientas en la locomotora (🚂)", "ru": "услышал(а) громкий лязг инструментов в локомотиве (🚂)"},
            {"en": "heard the whistle of the locomotive", "es": "escuché el silbido de la locomotora", "ru": "услышал(а) свисток локомотива"},
            {"en": "heard a voice coming from the locomotive (🚂)", "es": "escuché una voz que venía desde la locomotora (🚂)", "ru": "услышал(а) голос из локомотива (🚂)"},
        ],
        "LUGGAGE": [
            {"en": "heard someone rummaging in luggage carriage (🧳)", "es": "escuché a alguien revisando el vagón de carga (🧳)", "ru": "услышал(а), как кто-то роется в багажном вагоне (🧳)"},
            {"en": "heard a voice coming from the luggage carriage (🧳)", "es": "escuché una voz que venía desde el vagón de carga (🧳)", "ru": "услышал(а) голос из багажного вагона (🧳)"},
        ],
        "DINING": [
            {"en": "glanced out my window and saw someone eating in the dining carriage (🍽️)", "es": "miré por la ventana y vi a alguien comiendo en el vagón comedor (🍽️)", "ru": "взглянул(а) в окно и увидел(а), как кто-то ест в вагоне-ресторане (🍽️)"},
            {"en": "saw someone pouring wine in the dining carriage (🍽️)", "es": "vi a alguien sirviendose vino en el vagón comedor (🍽️)", "ru": "увидел(а), как кто-то наливает вино в вагоне-ресторане (🍽️)"},
            {"en": "heard someone playing the piano in the dining carriage (🍽️)", "es": "escuché a alguien tocando el piano en el vagón comedor (🍽️)", "ru": "услышал(а), как кто-то играет на пианино в вагоне-ресторане (🍽️)"},
            {"en": "heard a voice coming from the dining carriage (🍽️)", "es": "escuché una voz que venía desde el vagón comedor (🍽️)", "ru": "услышал(а) голос из вагона-ресторана (🍽️)"},
        ],
        "SLEEPING": [
            {"en": "heard someone snoring in the sleeping carriage (🛌)", "es": "escuché a alguien roncando en el vagón dormitorio (🛌)", "ru": "услышал(а) чей-то храп в спальном вагоне (🛌)"},
            {"en": "saw someone adjusting the curtains in the sleeping carriage (🛌)", "es": "vi a alguien ajustando las cortinas en el vagón dormitorio (🛌)", "ru": "увидел(а), как кто-то поправляет шторы в спальном вагоне (🛌)"},
            {"en": "heard a voice coming from the sleeping carriage (🛌)", "es": "escuché una voz que venía desde el vagón dormitorio (🛌)", "ru": "услышал(а) голос из спального вагона (🛌)"},
        ],
        "LOUNGE": [
            {"en": "glanced out my window and saw someone reading in the lounge carriage (🪑)", "es": "miré por la ventana y vi a alguien leyendo en el vagón salón (🪑)", "ru": "взглянул(а) в окно и увидел(а), как кто-то читает в салон-вагоне (🪑)"},
            {"en": "heard a voice coming from the lounge carriage (🪑)", "es": "escuché una voz que venía desde el vagón salón (🪑)", "ru": "услышал(а) голос из салон-вагона (🪑)"},
        ],
    }

    return (intro, labels, representations, activities)
