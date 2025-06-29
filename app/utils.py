
def load_css(filepath:str) -> str:
    with open(filepath, "r") as f:
        lines = f.readlines()
    return "".join(lines)