def get_key_from_value(mapper:dict, value):
    index = list(mapper.values()).index(value)
    return list(mapper.keys())[index]

def load_css(filepath:str) -> str:
    with open(filepath, "r") as f:
        lines = f.readlines()
    return "".join(lines)