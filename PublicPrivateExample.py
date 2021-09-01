class PublicPrivateExample:
    def __init__(self):
        self.public = "sage"
        self._unsafe = "unsafe"

    def public_method(self):
        pass

    def _unsage_method(self):

        pass
