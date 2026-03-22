def get_data():
    intro = {}
    intro["en"] = " are back into <b>the mansion where everything started</b>!"
    intro["es"] = " han vuelto a <b>la mansión donde todo comenzó</b>!"
    intro["ru"] = " снова в <b>особняке, где всё началось</b>!"

    labels = {}
    labels["en"] = {
        "KITCHEN": "kitchen",
        "DINING": "dining room",
        "BEDROOM": "bedroom",
        "BATHROOM": "bathroom",
        "GARDEN": "garden",
    }
    labels["es"] = {
        "KITCHEN": "la cocina",
        "DINING": "el comedor",
        "BEDROOM": "el dormitorio",
        "BATHROOM": "el baño",
        "GARDEN": "el jardín",
    }
    labels["ru"] = {
        "KITCHEN": "кухня",
        "DINING": "столовая",
        "BEDROOM": "спальня",
        "BATHROOM": "ванная",
        "GARDEN": "сад",
    }
    labels["ru_loc"] = {
        "KITCHEN": "кухне",
        "DINING": "столовой",
        "BEDROOM": "спальне",
        "BATHROOM": "ванной",
        "GARDEN": "саду",
    }
    labels["ru_gen"] = {
        "KITCHEN": "кухни",
        "DINING": "столовой",
        "BEDROOM": "спальни",
        "BATHROOM": "ванной",
        "GARDEN": "сада",
    }

    representations = {
        "KITCHEN": "🍲",
        "DINING": "🪑",
        "BEDROOM": "🛏️",
        "BATHROOM": "🚽",
        "GARDEN": "🌳",
    }

    activities = {
        "KITCHEN": [
            {"en": "noticed someone cooking", "es": "noté a alguien cocinando", "ru": "заметил(а), как кто-то готовит"},
            {"en": "heard someone washing the dishes", "es": "escuché a alguien lavando los platos", "ru": "услышал(а), как кто-то моет посуду"},
            {"en": "heard the clatter of pots in the kitchen (🍲)", "es": "escuché el ruido de ollas en la cocina (🍲)", "ru": "услышал(а) стук кастрюль на кухне (🍲)"},
            {"en": "heard a voice coming from the kitchen (🍲)", "es": "escuché una voz que venía desde la cocina (🍲)", "ru": "услышал(а) голос с кухни (🍲)"},
        ],
        "BATHROOM": [
            {"en": "heard someone brushing their teeth", "es": "escuché a alguien cepillándose los dientes", "ru": "услышал(а), как кто-то чистит зубы"},
            {"en": "heard someone flushing the toilet", "es": "escuché a alguien tirando de la cadena", "ru": "услышал(а), как кто-то спускает воду"},
            {"en": "heard the splash of shower in the bathroom (🚽)", "es": "escuché el chapoteo de la ducha en el baño (🚽)", "ru": "услышал(а) шум душа в ванной (🚽)"},
            {"en": "heard a voice coming from the bathroom (🚽)", "es": "escuché una voz que venía desde el baño (🚽)", "ru": "услышал(а) голос из ванной (🚽)"},
        ],
        "GARDEN": [
            {"en": "heard someone whistling in the garden (🌳)", "es": "escuché a alguien silbando en el jardín (🌳)", "ru": "услышал(а), как кто-то насвистывает в саду (🌳)"},
            {"en": "looked outside and saw someone pruning the bushes", "es": "miré afuera y vi a alguien podando los arbustos", "ru": "выглянул(а) наружу и увидел(а), как кто-то подстригает кусты"},
            {"en": "heard a voice coming from the garden (🌳)", "es": "escuché una voz que venía desde el jardín (🌳)", "ru": "услышал(а) голос из сада (🌳)"},
        ],
        "BEDROOM": [
            {"en": "heard someone snoring in the bedroom (🛏️)", "es": "escuché a alguien roncando en el dormitorio (🛏️)", "ru": "услышал(а) чей-то храп в спальне (🛏️)"},
            {"en": "heard a voice coming from the bedroom (🛏️)", "es": "escuché una voz que venía desde el dormitorio (🛏️)", "ru": "услышал(а) голос из спальни (🛏️)"},
        ],
        "DINING": [
            {"en": "heard someone playing the piano in the dining room (🪑)", "es": "escuché a alguien tocando el piano en el comedor (🪑)", "ru": "услышал(а), как кто-то играет на пианино в столовой (🪑)"},
            {"en": "heard a voice coming from the dining room (🪑)", "es": "escuché una voz que venía desde el comedor (🪑)", "ru": "услышал(а) голос из столовой (🪑)"},
        ],
    }

    return (intro, labels, representations, activities)
