
import json

tasks_dict = {
    
    "Kitchen": {
        "Demolition":[
            "Cabinets", "Countertops", "Walls", "Flooring", "Faucet", "Sink", "Disposal", "Refrigerator", "Microwave", "Range",
            "Dishwasher", "Lights", "Outlets"
        ],
        "Rebuild":["Cabinets", "Countertops"],
        "Cosmetic":["Ceilings", "Walls", "Baseboards"]
    },
    
    "Bathroom": {
        "Demolition":["Toilet", "Sink", "Shower", "Walls", "Flooring"],
        "Rebuild":["Walls", "Floor", "Shower"],
        "Cosmetic":["Walls", "Baseboard", "Tiling"]
    },

    "Bedroom":{
        "Demolition":["Walls"],
        "Rebuild":[],
        "Cosmetic":[]
    },

    "Multiple Room":{
        "Demolition":[],
        "Rebuild":[],
        "Cosmetic":[]
    },
    
    "Addition":{
        "Demolition":[],
        "Rebuild":[],
        "Cosmetic":[]
    },

    "Other":{
        "Demolition":[],
        "Rebuild":[],
        "Cosmetic":[]
    }
}

with open("tasks_kw.json", "w") as f:
    json.dump(tasks_dict, f)

# with open("tasks_kw.json", "r") as f:
#     json_file = json.load(f)

# print(json_file)