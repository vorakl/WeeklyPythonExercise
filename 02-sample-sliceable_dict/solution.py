class SliceableDict(dict):
    def __getitem__(self, key):
        try:
            value = super().__getitem__(key)
        except KeyError:
            try:
                # check if it is iterable
                _ = iter(key)
            except TypeError:
                raise KeyError(key)
            else:
                value = []
                for k in key:
                    value.append(super().__getitem__(k))
        return value
