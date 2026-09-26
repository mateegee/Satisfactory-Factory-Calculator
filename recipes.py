# Power Output Variables #
ASSEMBLER = 15
BLENDER = 75
CONSTRUCTOR = 4
FOUNDRY = 16
MANUFACTURER = 55
PACKAGER = 10
REFINERY = 30
SMELTER = 4

raw_inputs = [
    "Bauxite", 
    "Caterium Ore", 
    "Coal", 
    "Copper Ore", 
    "Crude Oil", 
    "Iron Ore", 
    "Limestone", 
    "Nitrogen Gas", 
    "Raw Quartz", 
    "Sam", 
    "Sulfur", 
    "Uranium", 
    "Water"]

recipes = {
    "Iron Ingots": {
        "machine": "Smelter",
        "materials": ["Iron Ore"],
        "by-product": None,
        "input": [30],
        "output": 30,
        "power": SMELTER,
        "is alt": False,
        "alts": True,
        "output material": "Iron Ingots",
    },
    "Iron Plates": {
        "machine": "Constructor",
        "materials": ["Iron Ingots"],
        "by-product": None,
        "input": [30],
        "output": 20,
        "power": CONSTRUCTOR,
        "is alt": False,
        "alts": True,
        "output material": "Iron Plates",
    },
    "Screws": {
        "machine": "Constructor",
        "materials": ["Iron Rods"],
        "by-product": None,
        "input": [10],
        "output": 40,
        "power": CONSTRUCTOR,
        "is alt": False,
        "alts": True,
        "output material": "Screws",
    },
    "Reinforced Iron Plates": {
        "machine": "Assembler",
        "materials": ["Iron Plates", "Screws"],
        "by-product": None,
        "input": [30, 60],
        "output": 5,
        "power": ASSEMBLER,
        "is alt": False,
        "alts": True,
        "output material": "Reinforced Iron Plates", 
    },
    "Cast Screws": {
        "machine": "Constructor",
        "materials": ["Iron Ingots"],
        "by-product": None,
        "input": [12.5],
        "output": 50,
        "power": CONSTRUCTOR,
        "is alt": True,
        "alts": False,
        "output material": "Screws",
    },
    "Iron Rods": {
        "machine": "Constructor",
        "materials": ["Iron Ingots"],
        "by-product": None,
        "input": [15],
        "output": 15,
        "power": CONSTRUCTOR,
        "is alt": False,
        "alts": True,
        "output material": "Iron Rods",
    }
}
