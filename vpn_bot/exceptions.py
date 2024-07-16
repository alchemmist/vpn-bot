import logging


class MyBaseException(Exception):
    def __init__(self, *args):
        if args[0]:
            logging.error(args[0])
        super().__init__(*args)


class UpdateHaventMessage(MyBaseException): ...

class UpdateHaventQuery(MyBaseException): ...

class CallbackUndefined(MyBaseException): ...

class CallbackIncorrectFormat(MyBaseException): ...

