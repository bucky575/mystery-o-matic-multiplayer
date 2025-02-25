from random import shuffle, choice

from networkx import (
    gnp_random_graph,
    relabel_nodes,
    Graph,
    is_planar,
    is_connected,
    planar_layout,
)
from networkx.drawing.nx_agraph import to_agraph

locations = ["egypt", "castle", "train", "ship", "space station", "mansion"]

mansions_labels = {}
mansions_labels["en"] = {
    "KITCHEN": "kitchen",
    "DINING": "dining room",
    "BEDROOM": "bedroom",
    "BATHROOM": "bathroom",
    "GARDEN": "garden",
}

mansions_labels["es"] = {
    "KITCHEN": "la cocina",
    "DINING": "el comedor",
    "BEDROOM": "el dormitorio",
    "BATHROOM": "el baño",
    "GARDEN": "el jardín",
}

mansion_intro = {}
mansion_intro["en"] = " are back into <b>the mansion where everything started</b>!"
mansion_intro["es"] = " han vuelto a <b>la mansión donde todo comenzó</b>!"

mansion_representations = {
    "KITCHEN": "🍲",
    "DINING": "🪑",
    "BEDROOM": "🛏️",
    "BATHROOM": "🚽",
    "GARDEN": "🌳",
}

mansion_activities = {
    "KITCHEN": [
        {"en": "noticed someone cooking", "es": "noté a alguien cocinando"},
        {
            "en": "heard someone washing the dishes",
            "es": "escuché a alguien lavando los platos",
        },
        {"en": "heard a voice coming from the kitchen (🍲)", "es": "escuché una voz que venía desde la cocina (🍲)"},
    ],
    "BATHROOM": [
        {
            "en": "heard someone brushing their teeth",
            "es": "escuché a alguien cepillándose los dientes",
        },
        {
            "en": "heard someone flushing the toilet",
            "es": "escuché a alguien tirando de la cadena",
        },
        {"en": "heard a voice coming from the bathroom (🚽)", "es": "escuché una voz que venía desde el baño (🚽)"},
    ],
    "GARDEN": [
        {
            "en": "heard someone whistling in the garden (🌳)",
            "es": "escuché a alguien silbando en el jardín (🌳)",
        },
        {
            "en": "looked outside and saw someone pruning the bushes",
            "es": "miré afuera y vi a alguien podando los arbustos",
        },
        {"en": "heard a voice coming from the garden (🌳)", "es": "escuché una voz que venía desde el jardín (🌳)"},
    ],
    "BEDROOM": [
        {
            "en": "heard someone snoring in the bedroom (🛏️)",
            "es": "escuché a alguien roncando en el dormitorio (🛏️)"
        },
        {"en": "heard a voice coming from the bedroom (🛏️)", "es": "escuché una voz que venía desde el dormitorio (🛏️)"},
    ],
    "DINING": [
        {
            "en": "heard someone playing the piano in the dining room (🪑)",
            "es": "escuché a alguien tocando el piano en el comedor (🪑)",
        },
        {"en": "heard a voice coming from the dining room (🪑)", "es": "escuché una voz que venía desde el comedor (🪑)"},
    ],
}

ship_intro = {}
ship_intro["en"] = " are transported back in time to <b>a pirate ship</b>!"
ship_intro["es"] = " han sido transportados en el tiempo a <b>un barco pirata</b>!"

ship_labels = {}
ship_labels["en"] = {
    "GALLEY": "galley",
    "NAVIGATION ROOM": "navigation room",
    "CAPTAIN CABIN": "captain cabin",
    "MAIN DECK": "main deck",
    "CARGO HOLD": "cargo hold",
}

ship_labels["es"] = {
    "GALLEY": "la cocina",
    "NAVIGATION ROOM": "la sala de navegación",
    "CAPTAIN CABIN": "la cabina del capitán",
    "MAIN DECK": "la cubierta principal",
    "CARGO HOLD": "la bodega de carga",
}

ship_representations = {
    "GALLEY": "🍲",
    "NAVIGATION ROOM": "🧭",
    "CAPTAIN CABIN": "🛏️",
    "MAIN DECK": "⚓",
    "CARGO HOLD": "📦",
}

ship_activities = {
    "GALLEY": [
        {"en": "noticed someone cooking", "es": "noté a alguien cocinando"},
        {
            "en": "heard someone washing the dishes",
            "es": "escuché a alguien lavando los platos",
        },
        {"en": "heard a voice coming from the galley (🍲)", "es": "escuché una voz que venía desde la cocina (🍲)"},
    ],
    "NAVIGATION ROOM": [
        {"en": "saw someone studying a map", "es": "vi a alguien mirando un mapa"},
        {
            "en": "heard a voice coming from the navigation room (🧭)",
            "es": "escuché una voz que venía desde la sala de navegación (🧭)",
        },
    ],
    "MAIN DECK": [
        {
            "en": "heard someone loading a cannon",
            "es": "escuché a alguien cargando un cañón",
        },
        {
            "en": "heard someone adjusting the sails",
            "es": "escuché a alguien ajustando las velas",
        },
        {"en": "heard a voice coming from the main deck (⚓)", "es": "escuché una voz que venía desde la cubierta principal (⚓)"},
    ],
    "CAPTAIN CABIN": [
        {
            "en": "heard someone snoring in the captain cabin (🛏️)",
            "es": "escuché a alguien roncando en la cabina del capitán (🛏️)"
        },
        {"en": "heard a voice coming from the captain cabin (🛏️)", "es": "escuché una voz que venía desde la cabina del capitán (🛏️)"},
    ],
    "CARGO HOLD": [
        {
            "en": "heard someone rummaging in the cargo hold (📦)",
            "es": "escuché a alguien revisando la bodega de carga (📦)",
        },
        {"en": "heard a voice coming from the cargo hold (📦)", "es": "escuché una voz que venía desde la bodega de carga (📦)"},
    ],
}

egypt_intro = {}
egypt_intro["en"] = (
    " are transported back in time to <b>a pyramid in Ancient Egypt</b>!"
)
egypt_intro["es"] = (
    " han sido transportados en el tiempo a <b>una pirámide en el Antiguo Egipto</b>!"
)

egypt_labels = {}
egypt_labels["en"] = {
    "THRONE ROOM": "throne room",
    "BURIAL PLACE": "burial chamber",
    "TEMPLE": "temple",
    "DESERT": "desert",
    "GARDEN": "garden",
}

egypt_labels["es"] = {
    "THRONE ROOM": "el cuarto del trono",
    "BURIAL PLACE": "la cámara funeraria",
    "TEMPLE": "el templo",
    "DESERT": "el desierto",
    "GARDEN": "el jardín",
}

egypt_representations = {
    "THRONE ROOM": "👑",
    "BURIAL PLACE": "⚰️",
    "TEMPLE": "📿",
    "DESERT": "🏜️",
    "GARDEN": "🌳",
}

egypt_activities = {
    "THRONE ROOM": [
        {
            "en": "saw someone from a distance sitting on the throne",
            "es": "vi a alguien sentado en el trono a lo lejos",
        },
        {
            "en": "saw someone from afar polishing the throne",
            "es": "vi a alguien puliendo el trono a lo lejos",
        },
        {"en": "heard a voice coming from the throne room (👑)", "es": "escuché una voz que venía desde el cuarto del trono (👑)"},
    ],
    "BURIAL PLACE": [
        {
            "en": "saw someone at a distance praying in the burial chamber (⚰️)",
            "es": "vi a alguien rezando en la cámara funeraria a lo lejos (⚰️)",
        },
        {"en": "heard a voice coming from the burial chamber (⚰️)", "es": "escuché una voz que venía desde la cámara funeraria (⚰️)"},
    ],
    "TEMPLE": [
        {
            "en": "saw someone at a distance praying in the temple (📿)",
            "es": "vi a alguien a la distancia rezando en el templo (📿)",
        },
        {
            "en": "saw someone from afar lighting candles in the temple (📿)",
            "es": "vi a alguien a la distancia encendiendo velas en el templo (📿)",
        },
        {"en": "heard a voice coming from the temple (📿)", "es": "escuché una voz que venía desde el templo (📿)"},
    ],
    "DESERT": [
        {
            "en": "looked outside and saw someone riding a camel in the desert (🏜️)",
            "es": "miré afuera y vi a alguien montando un camello en el desierto (🏜️)",
        },
    ],
    "GARDEN": [
        {
            "en": "heard someone whistling in the garden (🌳)",
            "es": "escuché a alguien silbando en el jardín (🌳)",
        },
        {
            "en": "looked outside and saw someone pruning the bushes",
            "es": "miré afuera y vi a alguien podando los arbustos",
        },
        {"en": "heard a voice coming from the garden (🌳)", "es": "escuché una voz que venía desde el jardín (🌳)"},
    ],
}

medieval_castle_intro = {}
medieval_castle_intro["en"] = (
    " are transported back in time to <b>a castle in the Middle Ages</b>!"
)
medieval_castle_intro["es"] = (
    " han sido transportados en el tiempo a <b>un castillo en la Edad Media</b>!"
)

medieval_castle_labels = {}
medieval_castle_labels["en"] = {
    "GREAT HALL": "great hall",
    "BED CHAMBER": "bed chamber",
    "DUNGEON": "dungeon",
    "ARMORY": "armory",
    "GARDEN": "garden",
}

medieval_castle_labels["es"] = {
    "GREAT HALL": "el gran salón",
    "BED CHAMBER": "el dormitorio principal",
    "DUNGEON": "la mazmorra",
    "ARMORY": "la armería",
    "GARDEN": "el jardín",
}

medieval_castle_representations = {
    "GREAT HALL": "🍷",
    "BED CHAMBER": "🛏️",
    "DUNGEON": "🔒",
    "ARMORY": "🛡️",
    "GARDEN": "🌳",
}

medieval_castle_activities = {
    "GREAT HALL": [
        {
            "en": "heard someone playing the harp in the great hall (🍷)",
            "es": "escuché a alguien tocando el arpa en el gran salón (🍷)",
        },
        {
            "en": "saw someone from a distance dancing in the great hall (🍷)",
            "es": "vi a alguien bailando en el gran salón (🍷) a lo lejos",
        },
        {"en": "heard a voice coming from the great hall (🍷)", "es": "escuché una voz que venía desde el gran salón (🍷)"},
    ],
    "ARMORY": [
        {
            "en": "saw someone from afar sharpening a sword in the armory (🛡️)",
            "es": "vi a alguien afilando una espada en la armería (🛡️) a lo lejos ",
        },
        {
            "en": "saw someone at a distance polishing a shield in the armory (🛡️)",
            "es": "vi a alguien puliendo un escudo en la armería (🛡️) a lo lejos",
        },
        {"en": "heard a voice coming from the armory (🛡️)", "es": "escuché una voz que venía desde la armería (🛡️)"},
    ],
    "DUNGEON": [
        {
            "en": "heard someone screaming in the dungeon (🔒)",
            "es": "escuché a alguien gritando en la mazmorra (🔒)",
        },
        {"en": "heard a voice coming from the dungeon (🔒)", "es": "escuché una voz que venía desde la mazmorra (🔒)"},
    ],
    "BED CHAMBER": [
        {
            "en": "heard someone snoring in the bed chamber (🛏️)",
            "es": "escuché a alguien roncando en el dormitorio principal (🛏️)",
        },
        {"en": "heard a voice coming from the bed chamber (🛏️)", "es": "escuché una voz que venía desde el dormitorio principal (🛏️)"},
    ],
    "GARDEN": [
        {
            "en": "heard someone whistling in the garden (🌳)",
            "es": "escuché a alguien silbando en el jardín (🌳)",
        },
        {
            "en": "looked outside and saw someone pruning the bushes",
            "es": "miré afuera y vi a alguien podando los arbustos",
        },
        {"en": "heard a voice coming from the garden (🌳)", "es": "escuché una voz que venía desde el jardín (🌳)"},
    ],
}

train_intro = {}
train_intro["en"] = (
    " are transported back in time to <b>the famous Orient Express</b> during its last voyage!"
)
train_intro["es"] = (
    " han sido transportados en el tiempo al <b>famoso Orient Express</b> durante su último viaje!"
)

train_labels = {}
train_labels["en"] = {
    "LOCOMOTIVE": "locomotive",
    "LUGGAGE": "luggage carriage",
    "DINING": "dining carriage",
    "SLEEPING": "sleeping carriage",
    "LOUNGE": "lounge carriage",
}

train_labels["es"] = {
    "LOCOMOTIVE": "la locomotora",
    "LUGGAGE": "el vagón de equipaje",
    "DINING": "el vagón comedor",
    "SLEEPING": "el vagón dormitorio",
    "LOUNGE": "el vagón salón",
}

train_representations = {
    "LOCOMOTIVE": "🚂",
    "LUGGAGE": "🧳",
    "DINING": "🍽️",
    "SLEEPING": "🛌",
    "LOUNGE": "🪑",
}

train_activities = {
    "LOCOMOTIVE": [
        {
            "en": "glanced out the window and saw someone fueling the locomotive (🚂)",
            "es": "miré por la ventana y vi a alguien repostando la locomotora (🚂)",
        },
        {
            "en": "heard the whistle of the locomotive",
            "es": "escuché el silbido de la locomotora",
        },
        {"en": "heard a voice coming from the locomotive (🚂)", "es": "escuché una voz que venía desde la locomotora (🚂)"},
    ],
    "LUGGAGE": [
        {
            "en": "heard someone rummaging in luggage carriage (🧳)",
            "es": "escuché a alguien revisando el vagón de carga (🧳)",
        },
        {"en": "heard a voice coming from the luggage carriage (🧳)", "es": "escuché una voz que venía desde el vagón de carga (🧳)"},
    ],
    "DINING": [
        {
            "en": "glanced out my window and saw someone eating in the dining carriage (🍽️)",
            "es": "miré por la ventana y vi a alguien comiendo en el vagón comedor (🍽️)",
        },
        {
            "en": "heard someone playing the piano in the dining carriage (🍽️)",
            "es": "escuché a alguien tocando el piano en el vagón comedor (🍽️)",
        },
        {"en": "heard a voice coming from the dining carriage (🍽️)", "es": "escuché una voz que venía desde el vagón comedor (🍽️)"},
    ],
    "SLEEPING": [
        {
            "en": "heard someone snoring in the sleeping carriage (🛌)",
            "es": "escuché a alguien roncando en el vagón dormitorio (🛌)",
        },
        {"en": "heard a voice coming from the sleeping carriage (🛌)", "es": "escuché una voz que venía desde el vagón dormitorio (🛌)"},
    ],
    "LOUNGE": [
        {
            "en": "glanced out my window and saw someone reading in the lounge carriage (🪑)",
            "es": "miré por la ventana y vi a alguien leyendo en el vagón salón (🪑)",
        },
        {"en": "heard a voice coming from the lounge carriage (🪑)", "es": "escuché una voz que venía desde el vagón salón (🪑)"},
    ],
}

space_station_intro = {}
space_station_intro["en"] = (
    " are transported into the future to <b>a high-tech space station</b> orbiting an unknown planet!"
)
space_station_intro["es"] = (
    " han sido transportados al futuro a <b>una estación espacial de alta tecnología</b> orbitando un planeta desconocido!"
)

space_station_labels = {}
space_station_labels["en"] = {
    "COMMAND": "command module",
    "LAB": "lab module",
    "AIRLOCK": "airlock module",
    "SLEEPING": "sleeping module",
    "GARDEN": "garden module",
}

space_station_labels["es"] = {
    "COMMAND": "el módulo de comando",
    "LAB": "el módulo de laboratorio",
    "AIRLOCK": "el módulo de esclusa",
    "SLEEPING": "el módulo de descanso",
    "GARDEN": "el módulo de jardín",
}

space_station_representations = {
    "COMMAND": "🕹️",
    "LAB": "🔬",
    "AIRLOCK": "🔒",
    "SLEEPING": "🛌",
    "GARDEN": "🥔",
}

space_station_activities = {
    "COMMAND": [
        {
            "en": "saw someone in the command module (🕹️) piloting the station",
            "es": "vi a alguien pilotando la estación espacial a lo lejos"
        },
        {"en": "heard a voice coming from the command module (🕹️)", "es": "escuché una voz que venía desde el módulo de comando (🕹️)"},
    ],
    "LAB": [
        {
            "en": "saw someone conducting experiments in the lab module (🔬)",
            "es": "vi a alguien realizando experimentos en el módulo de laboratorio (🔬)",
        },
        {"en": "heard a voice coming from the lab module (🔬)", "es": "escuché una voz que venía desde el módulo de laboratorio (🔬)"},
    ],
    "AIRLOCK": [
        {
            "en": "heard someone entering through the airlock module (🔒)",
            "es": "escuché a alguien entrando por el módulo de esclusa (🔒)",
        },
        {"en": "heard a voice coming from the airlock module (🔒)", "es": "escuché una voz que venía desde el módulo de esclusa (🔒)"},
    ],
    "SLEEPING": [
        {
            "en": "heard someone snoring in the sleeping module (🛌)",
            "es": "escuché a alguien roncando en el módulo de descanso (🛌)",
        },
        {"en": "heard a voice coming from the sleeping module (🛌)", "es": "escuché una voz que venía desde el módulo de descanso (🛌)"}
    ],
    "GARDEN": [
        {
            "en": "saw someone harvesting potatoes",
            "es": "vi a alguien cosechando patatas",
        },
        {"en": "heard a voice coming from the garden module (🥔)", "es": "escuché una voz que venía desde el módulo de jardín (🥔)"},
    ]
}


def get_location_data(selected_location):
    if selected_location is None:
        location_name = choice(locations)
    else:
        location_name = selected_location
    location_data = None

    if location_name == "mansion":
        location_data = (
            mansion_intro,
            mansions_labels,
            mansion_representations,
            mansion_activities,
        )
    elif location_name == "ship":
        location_data = (
            ship_intro,
            ship_labels,
            ship_representations,
            ship_activities,
        )
    elif location_name == "egypt":
        location_data = (
            egypt_intro,
            egypt_labels,
            egypt_representations,
            egypt_activities,
        )
    elif location_name == "castle":
        location_data = (
            medieval_castle_intro,
            medieval_castle_labels,
            medieval_castle_representations,
            medieval_castle_activities,
        )
    elif location_name == "train":
        location_data = (
            train_intro,
            train_labels,
            train_representations,
            train_activities,
        )
    elif location_name == "space station":
        location_data = (
            space_station_intro,
            space_station_labels,
            space_station_representations,
            space_station_activities,
        )
    else:
        raise ValueError("Unknown location name: " + location_name)

    return (location_name, location_data)


class Locations:
    """
    A class representing locations in a mystery game.

    Attributes:
    - graph: The graph representing the connections between locations.
    - map: A dictionary mapping generic node names to concrete location names.
    - indices: A dictionary mapping generic node names to concrete location indices.
    - names: A dictionary mapping generic node names to concrete location names.
    - representations: A dictionary mapping generic node names to concrete location representations.
    - weapons: A list of weapons available in the game.
    - weapon_locations: A dictionary mapping location names to weapons.
    """

    def __init__(self, location_name, number_places, location_data, weapons):
        """
        Initializes a Locations object.

        Parameters:
        - number_places: The number of locations in the game.
        - location_data: A tuple containing:
            + intro: A short sentence to introduce the location.
            + names: A dictionary mapping concrete location names to generic node names.
            + representations: A dictionary mapping concrete location names to their representations.
        - weapons: A list of weapons available in the game.
        """

        self.name = location_name
        intro, names, representations, activities = location_data
        self.intro = intro
        self.activities = activities
        self.number_places = number_places
        nodes = {}
        for n in range(number_places):
            nodes[n] = "ROOM" + str(n)

        self.map = nodes
        self.number_places = len(nodes)

        nodes_list = list(nodes.values())
        shuffle(nodes_list)
        names_list = list(names["en"].keys())

        self.names = names
        self.indices = {}
        # self.names = {}
        self.representations = {}

        if location_name == "train":
            self.indices["ROOM0"] = "LOCOMOTIVE"
            # self.names["ROOM0"] = names["LOCOMOTIVE"]
            self.representations["ROOM0"] = representations["LOCOMOTIVE"]

            names_list = [x for x in names_list if x != "LOCOMOTIVE"]
            nodes_list = [x for x in nodes_list if x != "ROOM0"]

        for generic, concrete in zip(nodes_list, names_list):
            self.indices[generic] = concrete
            # self.names[generic] = names[concrete]
            self.representations[generic] = representations[concrete]

        self.rindices = {v: k for k, v in self.indices.items()}
        self.weapons = weapons
        self.graph = self.create_locations_graph(nodes)
        self.weapon_locations = self.create_locations_weapons(weapons)

    def create_locations_graph(self, nodes):
        """
        Creates a graph representing the connections between locations.

        Parameters:
        - nodes: A dictionary mapping node indices to location names.

        Returns:
        - graph: The created graph.
        """
        keepGenerating = True

        while keepGenerating:
            if self.name == "train":
                graph = Graph()
                for n in range(self.number_places - 1):
                    graph.add_edge("ROOM" + str(n), "ROOM" + str(n + 1))
            else:
                graph = gnp_random_graph(self.number_places, 0.5)

            keepGenerating = not (is_planar(graph) and is_connected(graph))

        graph = relabel_nodes(graph, nodes)
        return graph

    def create_locations_weapons(self, weapons):
        """
        Creates a dictionary mapping location names to weapons.

        Parameters:
        - weapons: A list of weapons available in the game.

        Returns:
        - weapon_locations: The created dictionary.
        """
        weapon_locations = {}
        shuffled_weapons = list(weapons)
        shuffle(shuffled_weapons)

        for loc, weapon in zip(self.map.values(), shuffled_weapons):
            weapon_locations[loc] = weapon

        return weapon_locations

    def render_locations(self, outdir):
        for language in self.names.keys():
            self.render_locations_language(language, outdir)

    def render_locations_language(self, language, outdir):
        """
        Renders the locations graph and saves it as images.

        Parameters:
        - outdir: The directory where the images will be saved.
        """
        names = {}
        for index, place in self.indices.items():
            names[index] = self.names[language][place]

        labels = {}
        for place, name in names.items():
            labels[place] = name + " " + self.representations[place]

        relabeled_graph = relabel_nodes(self.graph, labels)
        g = to_agraph(relabeled_graph)

        if g.number_of_nodes() > 3:
            pos = planar_layout(g)

            # Apply the planar layout to the PyGraphviz graph
            for node, (x, y) in pos.items():
                n = g.get_node(node)
                n.attr["pos"] = f"{x},{y}"

        g.graph_attr.update(bgcolor="transparent")
        g.node_attr.update(
            fontname="Raleway", color="lightblue2", style="filled", shape="Mrecord"
        )
        g.layout(prog="dot")
        g.edge_attr.update(color="gray")
        g.draw(outdir + f"/{language}/locations_big.svg")
        g.graph_attr.update(dpi="200")
        g.draw(outdir + f"/{language}/locations_big.png")

        labels = {}
        for place, name in names.items():
            labels[place] = self.representations[place]

        relabeled_graph = relabel_nodes(self.graph, labels)
        g = to_agraph(relabeled_graph)

        if g.number_of_nodes() > 3:
            pos = planar_layout(g)

            # Apply the planar layout to the PyGraphviz graph
            for node, (x, y) in pos.items():
                n = g.get_node(node)
                n.attr["pos"] = f"{x},{y}"

        g.graph_attr.update(
            bgcolor="transparent", nodesep="0.1", ranksep="0.1", margin="0"
        )
        g.edge_attr.update(color="dimgrey", labeldistance="0.05")

        g.node_attr.update(
            fontname="Raleway", shape="plaintext", width="0.2", fixedsize="true"
        )
        g.layout(prog="dot")
        g.draw(outdir + f"/{language}/locations_small.svg")
        g.graph_attr.update(dpi="200")
        g.draw(outdir + f"/{language}/locations_small.png")

    def get_activities(self):
        """
        Returns the activities associated with each location.

        Returns:
        - activities: A dictionary mapping location names to activities.
        """
        activities = {}
        for generic, concrete in self.indices.items():
            if concrete in self.activities:
                activities[generic] = self.activities[concrete]

        return activities


class TutorialLocations(Locations):
    def __init__(self, location_data):
        self.name = "tutorial"
        _, names, representations, _ = location_data
        self.number_places = 4
        nodes = {}
        for n in range(self.number_places):
            nodes[n] = "ROOM" + str(n)

        self.map = nodes
        self.number_places = len(nodes)

        nodes_list = list(nodes.values())
        shuffle(nodes_list)

        self.names = names
        self.indices = {}
        # self.names = {}
        self.representations = {}

        self.indices["ROOM0"] = "KITCHEN"
        self.representations["ROOM0"] = representations["KITCHEN"]

        self.indices["ROOM1"] = "DINING"
        self.representations["ROOM1"] = representations["DINING"]

        self.indices["ROOM2"] = "BEDROOM"
        self.representations["ROOM2"] = representations["BEDROOM"]

        self.indices["ROOM3"] = "BATHROOM"
        self.representations["ROOM3"] = representations["BATHROOM"]

        self.rindices = {v: k for k, v in self.indices.items()}
        self.graph = self.create_locations_graph(nodes)

    def create_locations_graph(self, nodes):
        """
        Creates a graph representing the connections between locations.

        Parameters:
        - nodes: A dictionary mapping node indices to location names.

        Returns:
        - graph: The created graph.
        """
        graph = Graph()
        graph.add_edge("ROOM0", "ROOM1")
        graph.add_edge("ROOM0", "ROOM2")
        graph.add_edge("ROOM2", "ROOM3")
        graph = relabel_nodes(graph, nodes)
        return graph
