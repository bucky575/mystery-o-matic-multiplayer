def get_data():
    intro = {}
    intro["en"] = " are transported back in time to <b>a castle in the Middle Ages</b>!"
    intro["es"] = " han sido transportados en el tiempo a <b>un castillo en la Edad Media</b>!"
    intro["ru"] = " перенеслись в прошлое в <b>замок Средневековья</b>!"

    labels = {}
    labels["en"] = {
        "GREAT HALL": "great hall",
        "BED CHAMBER": "bed chamber",
        "DUNGEON": "dungeon",
        "ARMORY": "armory",
        "GARDEN": "garden",
    }
    labels["es"] = {
        "GREAT HALL": "el gran salón",
        "BED CHAMBER": "el dormitorio principal",
        "DUNGEON": "la mazmorra",
        "ARMORY": "la armería",
        "GARDEN": "el jardín",
    }
    labels["ru"] = {
        "GREAT HALL": "большой зал",
        "BED CHAMBER": "опочивальня",
        "DUNGEON": "темница",
        "ARMORY": "оружейная",
        "GARDEN": "сад",
    }
    labels["ru_loc"] = {
        "GREAT HALL": "большом зале",
        "BED CHAMBER": "опочивальне",
        "DUNGEON": "темнице",
        "ARMORY": "оружейной",
        "GARDEN": "саду",
    }
    labels["ru_gen"] = {
        "GREAT HALL": "большого зала",
        "BED CHAMBER": "опочивальни",
        "DUNGEON": "темницы",
        "ARMORY": "оружейной",
        "GARDEN": "сада",
    }

    representations = {
        "GREAT HALL": "🍷",
        "BED CHAMBER": "🛏️",
        "DUNGEON": "🔒",
        "ARMORY": "🛡️",
        "GARDEN": "🌳",
    }

    activities = {
        "GREAT HALL": [
            {"en": "heard someone playing the harp in the great hall (🍷)", "es": "escuché a alguien tocando el arpa en el gran salón (🍷)", "ru": "услышал(а), как кто-то играет на арфе в большом зале (🍷)"},
            {"en": "saw someone from a distance dancing in the great hall (🍷)", "es": "vi a alguien bailando en el gran salón (🍷) a lo lejos", "ru": "издалека увидел(а), как кто-то танцует в большом зале (🍷)"},
            {"en": "heard a voice coming from the great hall (🍷)", "es": "escuché una voz que venía desde el gran salón (🍷)", "ru": "услышал(а) голос из большого зала (🍷)"},
        ],
        "ARMORY": [
            {"en": "saw someone from afar sharpening a sword in the armory (🛡️)", "es": "vi a alguien afilando una espada en la armería (🛡️) a lo lejos ", "ru": "издалека увидел(а), как кто-то точит меч в оружейной (🛡️)"},
            {"en": "saw someone at a distance polishing a shield in the armory (🛡️)", "es": "vi a alguien puliendo un escudo en la armería (🛡️) a lo lejos", "ru": "издалека увидел(а), как кто-то полирует щит в оружейной (🛡️)"},
            {"en": "heard a voice coming from the armory (🛡️)", "es": "escuché una voz que venía desde la armería (🛡️)", "ru": "услышал(а) голос из оружейной (🛡️)"},
        ],
        "DUNGEON": [
            {"en": "heard someone screaming in the dungeon (🔒)", "es": "escuché a alguien gritando en la mazmorra (🔒)", "ru": "услышал(а) чей-то крик из темницы (🔒)"},
            {"en": "heard a voice coming from the dungeon (🔒)", "es": "escuché una voz que venía desde la mazmorra (🔒)", "ru": "услышал(а) голос из темницы (🔒)"},
        ],
        "BED CHAMBER": [
            {"en": "heard someone snoring in the bed chamber (🛏️)", "es": "escuché a alguien roncando en el dormitorio principal (🛏️)", "ru": "услышал(а) чей-то храп в опочивальне (🛏️)"},
            {"en": "heard a voice coming from the bed chamber (🛏️)", "es": "escuché una voz que venía desde el dormitorio principal (🛏️)", "ru": "услышал(а) голос из опочивальни (🛏️)"},
        ],
        "GARDEN": [
            {"en": "heard someone whistling in the garden (🌳)", "es": "escuché a alguien silbando en el jardín (🌳)", "ru": "услышал(а), как кто-то насвистывает в саду (🌳)"},
            {"en": "looked outside and saw someone pruning the bushes", "es": "miré afuera y vi a alguien podando los arbustos", "ru": "выглянул(а) наружу и увидел(а), как кто-то подстригает кусты"},
            {"en": "heard a voice coming from the garden (🌳)", "es": "escuché una voz que venía desde el jardín (🌳)", "ru": "услышал(а) голос из сада (🌳)"},
        ],
    }

    return (intro, labels, representations, activities)
