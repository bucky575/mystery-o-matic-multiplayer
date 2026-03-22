def get_data():
    intro = {}
    intro["en"] = " are transported into <b>a deserted hospital</b> at night!"
    intro["es"] = " han sido transportados a <b>un hospital desierto</b> por la noche!"
    intro["ru"] = " перенеслись в <b>пустую больницу</b> ночью!"

    labels = {}
    labels["en"] = {
        "ER": "emergency room",
        "ICU": "intensive care unit",
        "OPERATING THEATER": "operating theater",
        "PHARMACY": "pharmacy",
        "LOBBY": "lobby",
    }
    labels["es"] = {
        "ER": "la sala de urgencias",
        "ICU": "la unidad de cuidados intensivos",
        "OPERATING THEATER": "el quirófano",
        "PHARMACY": "la farmacia",
        "LOBBY": "el vestíbulo",
    }
    labels["ru"] = {
        "ER": "приёмное отделение",
        "ICU": "реанимация",
        "OPERATING THEATER": "операционная",
        "PHARMACY": "аптека",
        "LOBBY": "вестибюль",
    }
    labels["ru_loc"] = {
        "ER": "приёмном отделении",
        "ICU": "реанимации",
        "OPERATING THEATER": "операционной",
        "PHARMACY": "аптеке",
        "LOBBY": "вестибюле",
    }
    labels["ru_gen"] = {
        "ER": "приёмного отделения",
        "ICU": "реанимации",
        "OPERATING THEATER": "операционной",
        "PHARMACY": "аптеки",
        "LOBBY": "вестибюля",
    }

    representations = {
        "ER": "🚑",
        "ICU": "🛏️",
        "OPERATING THEATER": "🔪",
        "PHARMACY": "💊",
        "LOBBY": "💺",
    }

    activities = {
        "ER": [
            {"en": "heard a voice coming from the emergency room (🚑)", "es": "escuché una voz que venía desde la sala de urgencias (🚑)", "ru": "услышал(а) голос из приёмного отделения (🚑)"}
        ],
        "ICU": [
            {"en": "heard a voice coming from the intensive care unit (🛏️)", "es": "escuché una voz que venía desde la unidad de cuidados intensivos (🛏️)", "ru": "услышал(а) голос из реанимации (🛏️)"},
        ],
        "OPERATING THEATER": [
            {"en": "heard a voice coming from the operating theater (🔪)", "es": "escuché una voz que venía desde el quirófano (🔪)", "ru": "услышал(а) голос из операционной (🔪)"}
        ],
        "PHARMACY": [
            {"en": "heard a voice coming from the pharmacy (💊)", "es": "escuché una voz que venía desde la farmacia (💊)", "ru": "услышал(а) голос из аптеки (💊)"},
            {"en": "saw someone checking the medicine shelves in the pharmacy (💊)", "es": "vi a alguien revisando las estanterías de medicamentos en la farmacia (💊)", "ru": "увидел(а), как кто-то проверяет полки с лекарствами в аптеке (💊)"}
        ],
        "LOBBY": [
            {"en": "heard a voice coming from the lobby (💺)", "es": "escuché una voz que venía desde el vestíbulo (💺)", "ru": "услышал(а) голос из вестибюля (💺)"}
        ],
    }

    return (intro, labels, representations, activities)
