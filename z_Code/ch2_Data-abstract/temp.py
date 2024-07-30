def connector(name=None):
    """限制条件之间的连接器"""
    informant = None
    constraints = []

    def set_value(source, value):
        nonlocal informant
        val = connector["val"]
        if val is None:
            informant, connector["val"] = source, value
            if name is not None:
                print(name, "=", value)
            inform_all_except(source, "new_val", constraints)
        else:
            if val != value:
                print("Contradiction detected:", val, "vs", value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector["val"] = None, None
            if name is not None:
                print(name, "is forgotten")
            inform_all_except(source, "forget", constraints)

    connector = {
        "val": None,
        "set_val": set_value,
        "forget": forget_value,
        "has_val": lambda: connector["val"] is not None,
        "connect": lambda source: constraints.append(source),
    }
    return connector
