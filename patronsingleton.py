class soyunico(object):
    __instance = None

    nombre = None

    def __new__(cls):
        if soyunico.__instance is None:
            soyunico.__instance = object.__new__(cls)
        return soyunico.__instance