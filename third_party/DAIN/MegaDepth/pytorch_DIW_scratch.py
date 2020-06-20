import torch
import torch.nn as nn
from torch.autograd import Variable
from functools import reduce


class LambdaBase(nn.Sequential):
    def __init__(self, fn, *args):
        super(LambdaBase, self).__init__(*args)
        self.lambda_func = fn

    def forward_prepare(self, input):
        output = []
        for module in self._modules.values():
            output.append(module(input))
        return output if output else input


class Lambda(LambdaBase):
    def forward(self, input):
        return self.lambda_func(self.forward_prepare(input))


class LambdaMap(LambdaBase):
    def forward(self, input):
        return list(map(self.lambda_func, self.forward_prepare(input)))


class LambdaReduce(LambdaBase):
    def forward(self, input):
        return reduce(self.lambda_func, self.forward_prepare(input))


pytorch_DIW_scratch = nn.Sequential(  # Sequential,
    nn.Conv2d(3, 128, (7, 7), (1, 1), (3, 3)),
    nn.BatchNorm2d(128),
    nn.ReLU(),
    nn.Sequential(  # Sequential,
        LambdaMap(
            lambda x: x,  # ConcatTable,
            nn.Sequential(  # Sequential,
                nn.MaxPool2d((2, 2), (2, 2)),
                LambdaReduce(
                    lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 32, (3, 3), (1, 1), (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 32, (5, 5), (1, 1), (2, 2)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 32, (7, 7), (1, 1), (3, 3)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                ),
                LambdaReduce(
                    lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 32, (3, 3), (1, 1), (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 32, (5, 5), (1, 1), (2, 2)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 32, (7, 7), (1, 1), (3, 3)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                ),
                nn.Sequential(  # Sequential,
                    LambdaMap(
                        lambda x: x,  # ConcatTable,
                        nn.Sequential(  # Sequential,
                            nn.MaxPool2d((2, 2), (2, 2)),
                            LambdaReduce(
                                lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (3, 3), (1, 1), (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (5, 5), (1, 1), (2, 2)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (7, 7), (1, 1), (3, 3)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                            ),
                            LambdaReduce(
                                lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 64, (1, 1)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 64, (3, 3), (1, 1), (1, 1)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 64, (5, 5), (1, 1), (2, 2)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 64, (7, 7), (1, 1), (3, 3)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                            ),
                            nn.Sequential(  # Sequential,
                                LambdaMap(
                                    lambda x: x,  # ConcatTable,
                                    nn.Sequential(  # Sequential,
                                        LambdaReduce(
                                            lambda x, y, dim=1: torch.cat(
                                                (x, y), dim
                                            ),  # Concat,
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (3, 3), (1, 1), (1, 1)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (5, 5), (1, 1), (2, 2)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (7, 7), (1, 1), (3, 3)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                        ),
                                        LambdaReduce(
                                            lambda x, y, dim=1: torch.cat(
                                                (x, y), dim
                                            ),  # Concat,
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    64, 64, (3, 3), (1, 1), (1, 1)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    64, 64, (7, 7), (1, 1), (3, 3)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    64, 64, (11, 11), (1, 1), (5, 5)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                        ),
                                    ),
                                    nn.Sequential(  # Sequential,
                                        nn.AvgPool2d((2, 2), (2, 2)),
                                        LambdaReduce(
                                            lambda x, y, dim=1: torch.cat(
                                                (x, y), dim
                                            ),  # Concat,
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (3, 3), (1, 1), (1, 1)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (5, 5), (1, 1), (2, 2)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (7, 7), (1, 1), (3, 3)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                        ),
                                        LambdaReduce(
                                            lambda x, y, dim=1: torch.cat(
                                                (x, y), dim
                                            ),  # Concat,
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (3, 3), (1, 1), (1, 1)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (5, 5), (1, 1), (2, 2)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (7, 7), (1, 1), (3, 3)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                        ),
                                        nn.Sequential(  # Sequential,
                                            LambdaMap(
                                                lambda x: x,  # ConcatTable,
                                                nn.Sequential(  # Sequential,
                                                    LambdaReduce(
                                                        lambda x, y, dim=1: torch.cat(
                                                            (x, y), dim
                                                        ),  # Concat,
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 64, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (3, 3),
                                                                (1, 1),
                                                                (1, 1),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (5, 5),
                                                                (1, 1),
                                                                (2, 2),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (7, 7),
                                                                (1, 1),
                                                                (3, 3),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                    ),
                                                    LambdaReduce(
                                                        lambda x, y, dim=1: torch.cat(
                                                            (x, y), dim
                                                        ),  # Concat,
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 64, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (3, 3),
                                                                (1, 1),
                                                                (1, 1),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (5, 5),
                                                                (1, 1),
                                                                (2, 2),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (7, 7),
                                                                (1, 1),
                                                                (3, 3),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                    ),
                                                ),
                                                nn.Sequential(  # Sequential,
                                                    nn.AvgPool2d((2, 2), (2, 2)),
                                                    LambdaReduce(
                                                        lambda x, y, dim=1: torch.cat(
                                                            (x, y), dim
                                                        ),  # Concat,
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 64, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (3, 3),
                                                                (1, 1),
                                                                (1, 1),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (5, 5),
                                                                (1, 1),
                                                                (2, 2),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (7, 7),
                                                                (1, 1),
                                                                (3, 3),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                    ),
                                                    LambdaReduce(
                                                        lambda x, y, dim=1: torch.cat(
                                                            (x, y), dim
                                                        ),  # Concat,
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 64, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (3, 3),
                                                                (1, 1),
                                                                (1, 1),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (5, 5),
                                                                (1, 1),
                                                                (2, 2),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (7, 7),
                                                                (1, 1),
                                                                (3, 3),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                    ),
                                                    LambdaReduce(
                                                        lambda x, y, dim=1: torch.cat(
                                                            (x, y), dim
                                                        ),  # Concat,
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 64, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (3, 3),
                                                                (1, 1),
                                                                (1, 1),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (5, 5),
                                                                (1, 1),
                                                                (2, 2),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                        nn.Sequential(  # Sequential,
                                                            nn.Conv2d(256, 32, (1, 1)),
                                                            nn.BatchNorm2d(
                                                                32, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                            nn.Conv2d(
                                                                32,
                                                                64,
                                                                (7, 7),
                                                                (1, 1),
                                                                (3, 3),
                                                            ),
                                                            nn.BatchNorm2d(
                                                                64, 1e-05, 0.1, False
                                                            ),
                                                            nn.ReLU(),
                                                        ),
                                                    ),
                                                    nn.UpsamplingNearest2d(
                                                        scale_factor=2
                                                    ),
                                                ),
                                            ),
                                            LambdaReduce(
                                                lambda x, y: x + y
                                            ),  # CAddTable,
                                        ),
                                        LambdaReduce(
                                            lambda x, y, dim=1: torch.cat(
                                                (x, y), dim
                                            ),  # Concat,
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (3, 3), (1, 1), (1, 1)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (5, 5), (1, 1), (2, 2)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 32, (1, 1)),
                                                nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    32, 64, (7, 7), (1, 1), (3, 3)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                        ),
                                        LambdaReduce(
                                            lambda x, y, dim=1: torch.cat(
                                                (x, y), dim
                                            ),  # Concat,
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    64, 64, (3, 3), (1, 1), (1, 1)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    64, 64, (7, 7), (1, 1), (3, 3)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                            nn.Sequential(  # Sequential,
                                                nn.Conv2d(256, 64, (1, 1)),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                                nn.Conv2d(
                                                    64, 64, (11, 11), (1, 1), (5, 5)
                                                ),
                                                nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                                nn.ReLU(),
                                            ),
                                        ),
                                        nn.UpsamplingNearest2d(scale_factor=2),
                                    ),
                                ),
                                LambdaReduce(lambda x, y: x + y),  # CAddTable,
                            ),
                            LambdaReduce(
                                lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 64, (1, 1)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 64, (3, 3), (1, 1), (1, 1)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 64, (5, 5), (1, 1), (2, 2)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 64, (7, 7), (1, 1), (3, 3)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                            ),
                            LambdaReduce(
                                lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (3, 3), (1, 1), (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (5, 5), (1, 1), (2, 2)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(256, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (7, 7), (1, 1), (3, 3)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                            ),
                            nn.UpsamplingNearest2d(scale_factor=2),
                        ),
                        nn.Sequential(  # Sequential,
                            LambdaReduce(
                                lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (3, 3), (1, 1), (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (5, 5), (1, 1), (2, 2)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(32, 32, (7, 7), (1, 1), (3, 3)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                            ),
                            LambdaReduce(
                                lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 32, (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 64, (1, 1)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(64, 32, (3, 3), (1, 1), (1, 1)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 64, (1, 1)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(64, 32, (7, 7), (1, 1), (3, 3)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                                nn.Sequential(  # Sequential,
                                    nn.Conv2d(128, 64, (1, 1)),
                                    nn.BatchNorm2d(64, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                    nn.Conv2d(64, 32, (11, 11), (1, 1), (5, 5)),
                                    nn.BatchNorm2d(32, 1e-05, 0.1, False),
                                    nn.ReLU(),
                                ),
                            ),
                        ),
                    ),
                    LambdaReduce(lambda x, y: x + y),  # CAddTable,
                ),
                LambdaReduce(
                    lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 64, (1, 1)),
                        nn.BatchNorm2d(64, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(64, 32, (3, 3), (1, 1), (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 64, (1, 1)),
                        nn.BatchNorm2d(64, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(64, 32, (5, 5), (1, 1), (2, 2)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 64, (1, 1)),
                        nn.BatchNorm2d(64, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(64, 32, (7, 7), (1, 1), (3, 3)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                ),
                LambdaReduce(
                    lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 16, (1, 1)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 16, (3, 3), (1, 1), (1, 1)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 16, (7, 7), (1, 1), (3, 3)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 32, (1, 1)),
                        nn.BatchNorm2d(32, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(32, 16, (11, 11), (1, 1), (5, 5)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                ),
                nn.UpsamplingNearest2d(scale_factor=2),
            ),
            nn.Sequential(  # Sequential,
                LambdaReduce(
                    lambda x, y, dim=1: torch.cat((x, y), dim),  # Concat,
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 16, (1, 1)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 64, (1, 1)),
                        nn.BatchNorm2d(64, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(64, 16, (3, 3), (1, 1), (1, 1)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 64, (1, 1)),
                        nn.BatchNorm2d(64, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(64, 16, (7, 7), (1, 1), (3, 3)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                    nn.Sequential(  # Sequential,
                        nn.Conv2d(128, 64, (1, 1)),
                        nn.BatchNorm2d(64, 1e-05, 0.1, False),
                        nn.ReLU(),
                        nn.Conv2d(64, 16, (11, 11), (1, 1), (5, 5)),
                        nn.BatchNorm2d(16, 1e-05, 0.1, False),
                        nn.ReLU(),
                    ),
                ),
            ),
        ),
        LambdaReduce(lambda x, y: x + y),  # CAddTable,
    ),
    nn.Conv2d(64, 1, (3, 3), (1, 1), (1, 1)),
)
