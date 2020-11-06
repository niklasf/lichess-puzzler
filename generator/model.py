from chess.pgn import ChildNode
from chess import Move
from chess.engine import Score, Mate, Cp
from dataclasses import dataclass
from typing import List, Optional, Tuple, Literal, Union

Kind = Literal["mate", "material"]

@dataclass
class Puzzle:
    node: ChildNode
    moves: List[Move]
    kind: Kind

@dataclass
class EngineMove:
    move: Move
    score: Score

@dataclass
class NextMovePair:
    node: ChildNode
    best: EngineMove
    second: Optional[EngineMove]
