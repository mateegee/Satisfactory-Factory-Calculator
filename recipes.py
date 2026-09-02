# Power Output Variables #
ASSEMBLER = 15
BLENDER = 75
CONSTRUCTOR = 4
FOUNDRY = 16
MANUFACTURER = 55
PACKAGER = 10
REFINERY = 30
SMELTER = 4

raw_materials = {
    "Iron Ingots": {
            "machine": "Smelter",
            "materials": ["Iron Ore"],
            "by-product": None,
            "input": [30],
            "output": 30,
            "power": SMELTER,
            "alt": True,
            "output material": "Iron Ingots",
        }
}

recipes = {
    "Iron Plates": {
        "machine": "Constructor",
        "materials": ["Iron Ingots"],
        "by-product": None,
        "input": [30],
        "output": 20,
        "power": CONSTRUCTOR,
        "alt": True,
        "output material": "Iron Plates",
    },
    "Screws": {
        "machine": "Constructor",
        "materials": ["Iron Rods"],
        "by-product": None,
        "input": [10],
        "output": 40,
        "power": CONSTRUCTOR,
        "alt": True,
        "output material": "Screws",
    },
    "Reinforced Iron Plates": {
        "machine": "Assembler",
        "materials": ["Iron Plates", "Screws"],
        "by-product": None,
        "input": [30, 60],
        "output": 5,
        "power": ASSEMBLER,
        "alt": True,
        "output material": "Reinforced Iron Plates", 
    }
}
