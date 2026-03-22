def get_data():
    intro = {}
    intro["en"] = " are transported into <b>an abandoned school</b> at night!"
    intro["es"] = " han sido transportados a <b>una escuela abandonada</b> por la noche!"
    intro["ru"] = " перенеслись в <b>заброшенную школу</b> ночью!"

    labels = {}
    labels["en"] = {
        "ART CLASSROOM": "art classroom",
        "SCIENCE LAB": "science lab",
        "GYM": "gym",
        "LIBRARY": "library",
        "CAFETERIA": "cafeteria",
    }
    labels["es"] = {
        "ART CLASSROOM": "el aula de arte",
        "SCIENCE LAB": "el laboratorio de ciencias",
        "GYM": "el gimnasio",
        "LIBRARY": "la biblioteca",
        "CAFETERIA": "la cafetería",
    }
    labels["ru"] = {
        "ART CLASSROOM": "класс рисования",
        "SCIENCE LAB": "лаборатория",
        "GYM": "спортзал",
        "LIBRARY": "библиотека",
        "CAFETERIA": "столовая",
    }
    labels["ru_loc"] = {
        "ART CLASSROOM": "классе рисования",
        "SCIENCE LAB": "лаборатории",
        "GYM": "спортзале",
        "LIBRARY": "библиотеке",
        "CAFETERIA": "столовой",
    }
    labels["ru_gen"] = {
        "ART CLASSROOM": "класса рисования",
        "SCIENCE LAB": "лаборатории",
        "GYM": "спортзала",
        "LIBRARY": "библиотеки",
        "CAFETERIA": "столовой",
    }

    representations = {
        "ART CLASSROOM": "🎨",
        "SCIENCE LAB": "🔬",
        "GYM": "💪",
        "LIBRARY": "📚",
        "CAFETERIA": "🍽️",
    }

    activities = {
        "ART CLASSROOM": [
            {"en": "heard a voice coming from the art classroom (🎨)", "es": "escuché una voz que venía desde el aula de arte (🎨)", "ru": "услышал(а) голос из класса рисования (🎨)"}
        ],
        "SCIENCE LAB": [
            {"en": "heard a voice coming from the science lab (🔬)", "es": "escuché una voz que venía desde el laboratorio de ciencias (🔬)", "ru": "услышал(а) голос из лаборатории (🔬)"}
        ],
        "GYM": [
            {"en": "heard a voice coming from the gym (💪)", "es": "escuché una voz que venía desde el gimnasio (💪)", "ru": "услышал(а) голос из спортзала (💪)"}
        ],
        "LIBRARY": [
            {"en": "heard a voice coming from the library (📚)", "es": "escuché una voz que venía desde la biblioteca (📚)", "ru": "услышал(а) голос из библиотеки (📚)"}
        ],
        "CAFETERIA": [
            {"en": "heard a voice coming from the cafeteria (🍽️)", "es": "escuché una voz que venía desde la cafetería (🍽️)", "ru": "услышал(а) голос из столовой (🍽️)"}
        ],
    }

    return (intro, labels, representations, activities)
