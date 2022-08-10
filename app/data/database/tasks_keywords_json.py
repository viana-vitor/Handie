
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

   "Living Room":{
       "Demolition": [],
       "Rebuild": [],
       "Cosmetic": []
   },

   "Exterior":{
       "Demolition":[],
       "Rebuild":[],
       "Cosmetic":[]
   },

   "Landscape":{
       "Demolition":[],
       "Rebuild":[],
       "Cosmetic":[]

   }
}

def main():
    
    with open("app/data/database/tasks_kw.json", "w") as f:
        json.dump(tasks_dict, f)

