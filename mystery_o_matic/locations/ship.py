def get_data():
    intro = {}
    intro["en"] = " are transported back in time to <b>a pirate ship</b>!"
    intro["es"] = " han sido transportados en el tiempo a <b>un barco pirata</b>!"
    intro["ru"] = " перенеслись в прошлое на <b>пиратский корабль</b>!"

    labels = {}
    labels["en"] = {
        "GALLEY": "galley",
        "NAVIGATION ROOM": "navigation room",
        "CAPTAIN CABIN": "captain cabin",
        "MAIN DECK": "main deck",
        "CARGO HOLD": "cargo hold",
    }
    labels["es"] = {
        "GALLEY": "la cocina",
        "NAVIGATION ROOM": "la sala de navegación",
        "CAPTAIN CABIN": "la cabina del capitán",
        "MAIN DECK": "la cubierta principal",
        "CARGO HOLD": "la bodega de carga",
    }
    labels["ru"] = {
        "GALLEY": "камбуз",
        "NAVIGATION ROOM": "штурманская рубка",
        "CAPTAIN CABIN": "капитанская каюта",
        "MAIN DECK": "главная палуба",
        "CARGO HOLD": "грузовой трюм",
    }
    labels["ru_loc"] = {
        "GALLEY": "камбузе",
        "NAVIGATION ROOM": "штурманской рубке",
        "CAPTAIN CABIN": "капитанской каюте",
        "MAIN DECK": "главной палубе",
        "CARGO HOLD": "грузовом трюме",
    }
    labels["ru_gen"] = {
        "GALLEY": "камбуза",
        "NAVIGATION ROOM": "штурманской рубки",
        "CAPTAIN CABIN": "капитанской каюты",
        "MAIN DECK": "главной палубы",
        "CARGO HOLD": "грузового трюма",
    }

    representations = {
        "GALLEY": "🍲",
        "NAVIGATION ROOM": "🧭",
        "CAPTAIN CABIN": "🛏️",
        "MAIN DECK": "⚓",
        "CARGO HOLD": "📦",
    }

    activities = {
        "GALLEY": [
            {"en": "noticed someone cooking", "es": "noté a alguien cocinando", "ru": "заметил(а), как кто-то готовит"},
            {"en": "heard someone washing the dishes", "es": "escuché a alguien lavando los platos", "ru": "услышал(а), как кто-то моет посуду"},
            {"en": "heard a voice coming from the galley (🍲)", "es": "escuché una voz que venía desde la cocina (🍲)", "ru": "услышал(а) голос с камбуза (🍲)"},
        ],
        "NAVIGATION ROOM": [
            {"en": "saw someone studying a map", "es": "vi a alguien mirando un mapa", "ru": "увидел(а), как кто-то изучает карту"},
            {"en": "heard a voice coming from the navigation room (🧭)", "es": "escuché una voz que venía desde la sala de navegación (🧭)", "ru": "услышал(а) голос из штурманской рубки (🧭)"},
        ],
        "MAIN DECK": [
            {"en": "heard someone loading a cannon", "es": "escuché a alguien cargando un cañón", "ru": "услышал(а), как кто-то заряжает пушку"},
            {"en": "heard someone adjusting the sails", "es": "escuché a alguien ajustando las velas", "ru": "услышал(а), как кто-то поправляет паруса"},
            {"en": "heard a voice coming from the main deck (⚓)", "es": "escuché una voz que venía desde la cubierta principal (⚓)", "ru": "услышал(а) голос с главной палубы (⚓)"},
        ],
        "CAPTAIN CABIN": [
            {"en": "heard someone snoring in the captain cabin (🛏️)", "es": "escuché a alguien roncando en la cabina del capitán (🛏️)", "ru": "услышал(а) чей-то храп в капитанской каюте (🛏️)"},
            {"en": "heard a voice coming from the captain cabin (🛏️)", "es": "escuché una voz que venía desde la cabina del capitán (🛏️)", "ru": "услышал(а) голос из капитанской каюты (🛏️)"},
        ],
        "CARGO HOLD": [
            {"en": "heard someone rummaging in the cargo hold (📦)", "es": "escuché a alguien revisando la bodega de carga (📦)", "ru": "услышал(а), как кто-то роется в грузовом трюме (📦)"},
            {"en": "heard a voice coming from the cargo hold (📦)", "es": "escuché una voz que venía desde la bodega de carga (📦)", "ru": "услышал(а) голос из грузового трюма (📦)"},
        ],
    }

    return (intro, labels, representations, activities)
