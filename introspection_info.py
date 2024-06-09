import inspect


class Inspect_object():

    def __init__(self, *args):
        if args: self.obj = args[0]


    def introspection_info(self, *args):
        if args: self.obj = args[0]
        if len(args) > 1: print("Can only inspect the first parametr!")

        t = type(self.obj)
        a = dir(self.obj)
        m_ = []
        for m in a:
            if callable(m):
                m_.append(m_)

        d = inspect.getmodule(self.introspection_info)
        s = None
        try:
            s = [y for y in inspect.signature(self.obj).parameters.items()][0]
        except:
            pass

        return {"type": t, "attributes": a, "methods": m_, "module": d.__name__, "signature": s}


introspection_info = Inspect_object().introspection_info

number_info = introspection_info(42)
print(number_info)
