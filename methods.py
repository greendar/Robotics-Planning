


class Expectation:
    def __init__(self, code, category, specific, basic, intermediate, advanced):
        self.code = code
        self.category = category
        self.specific = specific
        self.basic = basic
        self.intermediate = intermediate
        self.advanced = advanced

    def __str__(self):
        outString = f"""{self.code}: {self.category} - {self.specific}\n\n
        Basic: {self.basic}\n
        Intermediate: {self.intermediate}\n
        Advanced: {self.advanced}\n\n\n"""
        return outString
