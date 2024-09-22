class Chip:
    """Attempt detection of current chip / CPU."""

    def __init__(self, detector) -> None:
        self.detector = detector
        self._chip_id = "SG2002"
    
    @property
    def sg2002(self) -> bool:
        return True

class Board:
    """Attempt to detect specific boards."""

    def __init__(self, detector) -> None:
        self.detector = detector
        self._board_id = "LICHEE_RV_NANO"
        
    @property
    def id(self):
        self._board_id

    @property
    def lichee_rv_nano(self) -> bool:
        return True

class Detector:
    """Wrap various platform detection functions."""

    def __init__(self) -> None:
        self.board = Board(self)
        self.chip = Chip(self)