from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # pindahkan key ke posisi paling belakang (terbaru)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update value dan pindahkan ke belakang
            self.cache.move_to_end(key)
        self.cache[key] = value
        # jika melebihi kapasitas, hapus yang paling depan (terlama)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
