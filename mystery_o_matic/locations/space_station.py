def get_data():
    intro = {}
    intro["en"] = " are transported into the future to <b>a high-tech space station</b> orbiting an unknown planet!"
    intro["es"] = " han sido transportados al futuro a <b>una estación espacial de alta tecnología</b> orbitando un planeta desconocido!"
    intro["ru"] = " перенеслись в будущее на <b>высокотехнологичную космическую станцию</b>, вращающуюся вокруг неизвестной планеты!"

    labels = {}
    labels["en"] = {
        "COMMAND": "command module",
        "LAB": "lab module",
        "AIRLOCK": "airlock module",
        "SLEEPING": "sleeping module",
        "GARDEN": "garden module",
    }
    labels["es"] = {
        "COMMAND": "el módulo de comando",
        "LAB": "el módulo de laboratorio",
        "AIRLOCK": "el módulo de esclusa",
        "SLEEPING": "el módulo de descanso",
        "GARDEN": "el módulo de jardín",
    }
    labels["ru"] = {
        "COMMAND": "командный модуль",
        "LAB": "лабораторный модуль",
        "AIRLOCK": "шлюзовой модуль",
        "SLEEPING": "жилой модуль",
        "GARDEN": "садовый модуль",
    }
    labels["ru_loc"] = {
        "COMMAND": "командном модуле",
        "LAB": "лабораторном модуле",
        "AIRLOCK": "шлюзовом модуле",
        "SLEEPING": "жилом модуле",
        "GARDEN": "садовом модуле",
    }
    labels["ru_gen"] = {
        "COMMAND": "командного модуля",
        "LAB": "лабораторного модуля",
        "AIRLOCK": "шлюзового модуля",
        "SLEEPING": "жилого модуля",
        "GARDEN": "садового модуля",
    }

    representations = {
        "COMMAND": "🕹️",
        "LAB": "🔬",
        "AIRLOCK": "🔒",
        "SLEEPING": "🛌",
        "GARDEN": "🥔",
    }

    activities = {
        "COMMAND": [
            {"en": "saw someone adjusting the station's orbit on the command module's screens", "es": "vi a alguien ajustando la órbita de la estación en las pantallas del módulo de comando (🕹️)", "ru": "увидел(а), как кто-то корректирует орбиту станции на экранах командного модуля (🕹️)"},
            {"en": "heard a voice coming from the command module (🕹️)", "es": "escuché una voz que venía desde el módulo de comando (🕹️)", "ru": "услышал(а) голос из командного модуля (🕹️)"},
        ],
        "LAB": [
            {"en": "saw someone mixing glowing chemicals in the lab module (🔬)", "es": "vi a alguien mezclando químicos brillantes en el módulo de laboratorio (🔬)", "ru": "увидел(а), как кто-то смешивает светящиеся химикаты в лабораторном модуле (🔬)"},
            {"en": "heard a voice coming from the lab module (🔬)", "es": "escuché una voz que venía desde el módulo de laboratorio (🔬)", "ru": "услышал(а) голос из лабораторного модуля (🔬)"},
        ],
        "AIRLOCK": [
            {"en": "heard a hiss of depressurization from the airlock module (🔒)", "es": "escuché un silbido de despresurización desde el módulo de esclusa (🔒)", "ru": "услышал(а) шипение декомпрессии из шлюзового модуля (🔒)"},
            {"en": "heard a voice coming from the airlock module (🔒)", "es": "escuché una voz que venía desde el módulo de esclusa (🔒)", "ru": "услышал(а) голос из шлюзового модуля (🔒)"},
        ],
        "SLEEPING": [
            {"en": "heard someone snoring in the sleeping module (🛌)", "es": "escuché a alguien roncando en el módulo de descanso (🛌)", "ru": "услышал(а) чей-то храп в жилом модуле (🛌)"},
            {"en": "heard a metallic clank from the sleeping module's lockers (🛌)", "es": "escuché un golpe metálico proveniente de los armarios del módulo de descanso (🛌)", "ru": "услышал(а) металлический лязг из шкафчиков жилого модуля (🛌)"},
            {"en": "heard a voice coming from the sleeping module (🛌)", "es": "escuché una voz que venía desde el módulo de descanso (🛌)", "ru": "услышал(а) голос из жилого модуля (🛌)"},
        ],
        "GARDEN": [
            {"en": "saw someone harvesting potatoes", "es": "vi a alguien cosechando patatas", "ru": "увидел(а), как кто-то собирает картофель"},
            {"en": "saw someone watering the hydroponic vines in the garden module (🥔)", "es": "vi a alguien regando las enredaderas hidropónicas en el módulo de jardín (🥔)", "ru": "увидел(а), как кто-то поливает гидропонные растения в садовом модуле (🥔)"},
            {"en": "heard a voice coming from the garden module (🥔)", "es": "escuché una voz que venía desde el módulo de jardín (🥔)", "ru": "услышал(а) голос из садового модуля (🥔)"},
        ],
    }

    return (intro, labels, representations, activities)
