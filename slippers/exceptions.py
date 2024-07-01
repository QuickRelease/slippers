class SlippersError(Exception):
    def __init__(self, msg: str, argument: str, component: str):
        self.msg = msg
        self.argument = argument
        self.component = component
        super().__init__(msg)

    def __str__(self):
        return f'{self.msg} ("{self.component}.{self.argument}")'
