class WinException(Exception):
    def __init__(self, *args: object, winning_board) -> None:
        super().__init__(*args)
        self.winning_board = winning_board


class LoseException(Exception):
    pass


