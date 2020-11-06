from dataclasses import dataclass, field
import chess
from chess.pgn import Game, ChildNode
from chess import Move, Color
from typing import List, Optional, Tuple, Literal, Union

PuzzleKind = Literal["mate", "material"]  # Literal["mate", "other"]

TagKind = Literal[
    "advancedPawn",
    "attraction",
    "blocking",
    "capturingDefender",
    "clearance",
    "coercion",
    "defensiveMove",
    "discoveredAttack",
    "deflection",
    "doubleCheck",
    "exposedKing",
    "fork",
    "hangingPiece",
    "interference",
    "long",
    "mateIn6+",
    "mateIn5",
    "mateIn4",
    "mateIn3",
    "mateIn2",
    "mateIn1",
    "oneMove",
    "overloading",
    "pin",
    "quietMove",
    "sacrifice",
    "short",
    "simplification",
    "skewer",
    "trappedPiece",
    "zugzwang"
]

@dataclass
class Puzzle:
    id: str
    game: Game
    pov: Color = field(init=False)
    mainline: List[ChildNode] = field(init=False)

    def __post_init__(self) -> None:
        self.pov = not self.game.turn()
        self.mainline = list(self.game.mainline())
