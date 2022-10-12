from time import asctime


def displayPrint(msg: str, **kwargs):

    outstr = f"[{asctime()}] {msg}"
    if kwargs not in [None, {}]:
        outstr += f", ({', '.join(kwargs.values())})"
    print(outstr)
