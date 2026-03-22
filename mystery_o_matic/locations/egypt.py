def get_data():
    intro = {}
    intro["en"] = " are transported back in time to <b>a pyramid in Ancient Egypt</b>!"
    intro["es"] = " han sido transportados en el tiempo a <b>una pirámide en el Antiguo Egipto</b>!"
    intro["ru"] = " перенеслись в прошлое в <b>пирамиду Древнего Египта</b>!"

    labels = {}
    labels["en"] = {
        "THRONE ROOM": "throne room",
        "BURIAL PLACE": "burial chamber",
        "TEMPLE": "temple",
        "DESERT": "desert",
        "GARDEN": "garden",
    }
    labels["es"] = {
        "THRONE ROOM": "el cuarto del trono",
        "BURIAL PLACE": "la cámara funeraria",
        "TEMPLE": "el templo",
        "DESERT": "el desierto",
        "GARDEN": "el jardín",
    }
    labels["ru"] = {
        "THRONE ROOM": "тронный зал",
        "BURIAL PLACE": "погребальная камера",
        "TEMPLE": "храм",
        "DESERT": "пустыня",
        "GARDEN": "сад",
    }
    labels["ru_loc"] = {
        "THRONE ROOM": "тронном зале",
        "BURIAL PLACE": "погребальной камере",
        "TEMPLE": "храме",
        "DESERT": "пустыне",
        "GARDEN": "саду",
    }
    labels["ru_gen"] = {
        "THRONE ROOM": "тронного зала",
        "BURIAL PLACE": "погребальной камеры",
        "TEMPLE": "храма",
        "DESERT": "пустыни",
        "GARDEN": "сада",
    }

    representations = {
        "THRONE ROOM": "👑",
        "BURIAL PLACE": "⚱️",
        "TEMPLE": "📿",
        "DESERT": "🏜️",
        "GARDEN": "🌳",
    }

    activities = {
        "THRONE ROOM": [
            {"en": "saw someone from a distance sitting on the throne", "es": "vi a alguien sentado en el trono a lo lejos", "ru": "издалека увидел(а), как кто-то сидит на троне"},
            {"en": "saw someone from afar polishing the throne", "es": "vi a alguien puliendo el trono a lo lejos", "ru": "издалека увидел(а), как кто-то полирует трон"},
            {"en": "heard a voice coming from the throne room (👑)", "es": "escuché una voz que venía desde el cuarto del trono (👑)", "ru": "услышал(а) голос из тронного зала (👑)"},
        ],
        "BURIAL PLACE": [
            {"en": "saw someone at a distance praying in the burial chamber (⚱️)", "es": "vi a alguien rezando en la cámara funeraria a lo lejos (⚱️)", "ru": "издалека увидел(а), как кто-то молится в погребальной камере (⚱️)"},
            {"en": "heard a voice coming from the burial chamber (⚱️)", "es": "escuché una voz que venía desde la cámara funeraria (⚱️)", "ru": "услышал(а) голос из погребальной камеры (⚱️)"},
        ],
        "TEMPLE": [
            {"en": "saw someone at a distance praying in the temple (📿)", "es": "vi a alguien a la distancia rezando en el templo (📿)", "ru": "издалека увидел(а), как кто-то молится в храме (📿)"},
            {"en": "saw someone from afar lighting candles in the temple (📿)", "es": "vi a alguien a la distancia encendiendo velas en el templo (📿)", "ru": "издалека увидел(а), как кто-то зажигает свечи в храме (📿)"},
            {"en": "heard a voice coming from the temple (📿)", "es": "escuché una voz que venía desde el templo (📿)", "ru": "услышал(а) голос из храма (📿)"},
        ],
        "DESERT": [
            {"en": "looked outside and saw someone riding a camel in the desert (🏜️)", "es": "miré afuera y vi a alguien montando un camello en el desierto (🏜️)", "ru": "выглянул(а) наружу и увидел(а), как кто-то едет на верблюде в пустыне (🏜️)"},
        ],
        "GARDEN": [
            {"en": "heard someone whistling in the garden (🌳)", "es": "escuché a alguien silbando en el jardín (🌳)", "ru": "услышал(а), как кто-то насвистывает в саду (🌳)"},
            {"en": "looked outside and saw someone pruning the bushes", "es": "miré afuera y vi a alguien podando los arbustos", "ru": "выглянул(а) наружу и увидел(а), как кто-то подстригает кусты"},
            {"en": "heard a voice coming from the garden (🌳)", "es": "escuché una voz que venía desde el jardín (🌳)", "ru": "услышал(а) голос из сада (🌳)"},
        ],
    }

    return (intro, labels, representations, activities)
