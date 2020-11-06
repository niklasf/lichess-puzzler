from typing import List, Optional, Tuple, Literal, Union
import chess
from chess import square_rank, Move, Color, Board, Square, Piece
from chess.pgn import Game, ChildNode

def moved_piece_type(node: ChildNode) -> chess.PieceType:
    piece_type = node.board().piece_type_at(node.move.to_square)
    assert piece_type is not None, "did not find moved piece"
    return piece_type

def is_pawn_move(node: ChildNode) -> bool:
    return moved_piece_type(node) == chess.PAWN

def is_advanced_pawn_move(node: ChildNode) -> bool:
    if node.move.promotion:
        return True
    if not is_pawn_move(node):
        return False
    to_rank = square_rank(node.move.to_square)
    return to_rank < 5 if node.turn() else to_rank > 4

def is_king_move(node: ChildNode) -> bool:
    return moved_piece_type(node) == chess.KING

def is_capture(node: ChildNode) -> bool:
    return node.parent.board().is_capture(node.move)

def next_next_node(node: ChildNode) -> Optional[ChildNode]:
    nn = node.next()
    return nn.next() if nn else None

values = { chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9 }

def piece_value(piece_type: chess.PieceType) -> int:
    return values[piece_type]

def material_count(board: Board, side: Color) -> int:
    return sum(len(board.pieces(piece_type, side)) * value for piece_type, value in values.items())

def material_diff(board: Board, side: Color) -> int:
    return material_count(board, side) - material_count(board, not side)

def attacked_opponent_pieces(board: Board, from_square: Square, pov: Color) -> List[Piece]:
    return [piece for (piece, square) in attacked_opponent_squares(board, from_square, pov)]

def attacked_opponent_squares(board: Board, from_square: Square, pov: Color) -> List[Tuple[Piece, Square]]:
    pieces = []
    for attacked_square in board.attacks(from_square):
        attacked_piece = board.piece_at(attacked_square)
        if attacked_piece and attacked_piece.color != pov:
            pieces.append((attacked_piece, attacked_square))
    return pieces

def is_hanging(board: Board, piece: Piece, square: Square) -> bool:
    return not board.attackers(piece.color, square)
