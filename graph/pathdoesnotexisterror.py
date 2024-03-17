class PathDoesNotExistError(Exception):
    def __init__(self, start, target):
        msg = f"No path found between {start} and {target}!"
        super().__init__(msg)