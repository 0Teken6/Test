class Hello:
    def __init__(self, str):
        self.str = str


class Hello2(Hello):
    def __init__(self, str, compliment):
        Hello.__init__(self, str)
        self.compliment = compliment
