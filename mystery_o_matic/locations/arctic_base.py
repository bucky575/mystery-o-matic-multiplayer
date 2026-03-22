def get_data():
    intro = {}
    intro["en"] = " are stranded in <b>an abandoned arctic military base</b> during a blizzard!"
    intro["es"] = " han quedado atrapados en <b>una base militar ártica abandonada</b> durante una tormenta de nieve!"
    intro["ru"] = " оказались в <b>заброшенной арктической военной базе</b> во время метели!"

    labels = {}
    labels["en"] = {
        "COMMAND CENTER": "command center",
        "ARMORY": "armory",
        "BARRACKS": "barracks",
        "RADIO ROOM": "radio room",
        "MESS HALL": "mess hall",
    }
    labels["es"] = {
        "COMMAND CENTER": "el centro de mando",
        "ARMORY": "la armería",
        "BARRACKS": "los barracones",
        "RADIO ROOM": "la sala de radio",
        "MESS HALL": "el comedor",
    }
    labels["ru"] = {
        "COMMAND CENTER": "командный центр",
        "ARMORY": "оружейная",
        "BARRACKS": "казарма",
        "RADIO ROOM": "радиорубка",
        "MESS HALL": "столовая",
    }
    labels["ru_loc"] = {
        "COMMAND CENTER": "командном центре",
        "ARMORY": "оружейной",
        "BARRACKS": "казарме",
        "RADIO ROOM": "радиорубке",
        "MESS HALL": "столовой",
    }
    labels["ru_gen"] = {
        "COMMAND CENTER": "командного центра",
        "ARMORY": "оружейной",
        "BARRACKS": "казармы",
        "RADIO ROOM": "радиорубки",
        "MESS HALL": "столовой",
    }

    representations = {
        "COMMAND CENTER": "🖥️",
        "ARMORY": "🔒",
        "BARRACKS": "🛏️",
        "RADIO ROOM": "📡",
        "MESS HALL": "🍽️",
    }

    activities = {
        "COMMAND CENTER": [
            {"en": "heard someone typing on an old keyboard (🖥️)", "es": "escuché a alguien tecleando en un viejo teclado (🖥️)", "ru": "услышал(а), как кто-то печатает на старой клавиатуре (🖥️)"},
            {"en": "heard a voice coming from the command center (🖥️)", "es": "escuché una voz que venía desde el centro de mando (🖥️)", "ru": "услышал(а) голос из командного центра (🖥️)"},
        ],
        "ARMORY": [
            {"en": "heard the clinking of metal in the armory (🔒)", "es": "escuché el tintineo de metal en la armería (🔒)", "ru": "услышал(а) звон металла в оружейной (🔒)"},
            {"en": "heard a voice coming from the armory (🔒)", "es": "escuché una voz que venía desde la armería (🔒)", "ru": "услышал(а) голос из оружейной (🔒)"},
        ],
        "BARRACKS": [
            {"en": "heard footsteps echoing in the barracks (🛏️)", "es": "escuché pasos resonando en los barracones (🛏️)", "ru": "услышал(а) шаги, эхом разносящиеся по казарме (🛏️)"},
            {"en": "heard a voice coming from the barracks (🛏️)", "es": "escuché una voz que venía desde los barracones (🛏️)", "ru": "услышал(а) голос из казармы (🛏️)"},
        ],
        "RADIO ROOM": [
            {"en": "heard the crackle of static from the radio room (📡)", "es": "escuché el crepitar de la estática desde la sala de radio (📡)", "ru": "услышал(а) треск статики из радиорубки (📡)"},
            {"en": "heard a voice coming from the radio room (📡)", "es": "escuché una voz que venía desde la sala de radio (📡)", "ru": "услышал(а) голос из радиорубки (📡)"},
        ],
        "MESS HALL": [
            {"en": "heard the clatter of tin trays in the mess hall (🍽️)", "es": "escuché el ruido de bandejas de metal en el comedor (🍽️)", "ru": "услышал(а) грохот металлических подносов в столовой (🍽️)"},
            {"en": "heard a voice coming from the mess hall (🍽️)", "es": "escuché una voz que venía desde el comedor (🍽️)", "ru": "услышал(а) голос из столовой (🍽️)"},
        ],
    }

    return (intro, labels, representations, activities)
