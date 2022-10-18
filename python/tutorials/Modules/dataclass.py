from dataclasses import dataclass, field
'''
dataclasses.replace(Class, Arg=X)
'''

@dataclass(frozen=False, order=True)
class Comments:
    index: int = field(init=False)
    cid: int
    data: str
    a: list[int] = field(default_factory=list, compare=False, hash=False, repr=False)

    def __post_init__(self):
        self.index = self.cid
        # if Frozen use:
        # object.__setattr__(self, 'index', self.cid)

if __name__ == '__main__':
    c = Comments(1, 'test')
    print(c)
