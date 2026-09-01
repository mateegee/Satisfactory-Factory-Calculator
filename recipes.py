# Power Output Variables #
ASSEMBLER = 15
BLENDER = 75
CONSTRUCTOR = 4
FOUNDRY = 16
MANUFACTURER = 55
PACKAGER = 10
REFINERY = 30
SMELTER = 4

recipes = {
    "Iron Plates": {
        "machine": "Constructor",
        "materials": ["Iron Ingots"],
        "by-product": None,
        "input": [30],
        "output": 20,
        "power": CONSTRUCTOR,
    },
    "Screws": {
        "machine": "Constructor",
        "materials": ["Iron Rods"],
        "by-product": None,
        "input": [10],
        "output": 40,
        "power": CONSTRUCTOR,
    },
    "Reinforced Iron Plates": {
        "machine": "Assembler",
        "materials": ["Iron Plates", "Screws"],
        "by-product": None,
        "input": [30, 60],
        "output": 5,
        "power": ASSEMBLER
    }
}
