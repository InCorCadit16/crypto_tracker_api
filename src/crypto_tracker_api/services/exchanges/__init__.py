import sys
from crypto_tracker_api.utils.import_submodules import import_all_modules


class ExchangeMeta(type):
    _subclasses = {}

    def __init__(cls, name, bases, attrs):
        if hasattr(cls, 'EXCHANGE') and cls.EXCHANGE is not None:
            ExchangeMeta._subclasses[cls.EXCHANGE] = cls
        super().__init__(name, bases, attrs)

    @classmethod
    def get_all(cls):
        return cls._subclasses

import_all_modules(sys.modules[__name__])
