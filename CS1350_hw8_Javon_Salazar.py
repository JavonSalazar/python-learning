# Homework 8
# Name: Javon Salazar
# Date: 4/24/26
#Description: This homework covers over lecture 12 and 14 lecture 1 unit 1-3.

#lecture 1 unit 1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def safe_get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Not found"


def convert_to_number(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            return None
#lecture 1 unit 2
def access_data(data_structure, key):
    try:
        return data_structure[key]
    except LookupError:   # handles IndexError + KeyError
        return None


def parse_value(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            return str(value)
#lecture 1 unit 3
def process_file(filename):
    file = None
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print("File not found")
        return None
    except PermissionError:
        print("Permission denied")
        return None
    else:
        content = file.read()
        return content.upper()
    finally:
        if file:
            file.close()
class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None

    def acquire(self):
        print(f"Acquiring {self.name}")
        self.resource = True

    def release(self):
        print(f"Releasing {self.name}")
        self.resource = None

    def use(self):
        if not self.resource:
            raise RuntimeError("Resource not acquired")
        print(f"Using {self.name}")


rm = ResourceManager("Database")

try:
    rm.acquire()
except RuntimeError as e:
    print(e)
else:
    rm.use()
finally:
    rm.release()
#lecture 2 unit 2
def practice_2_custom_exceptions():
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    #  Custom Exceptions
    class GameError(Exception):
        pass

    class InvalidMoveError(GameError):
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"Move {position} invalid: {reason}")

    class GameOverError(GameError):
        def __init__(self, winner):
            self.winner = winner
            super().__init__(f"Game over! Winner: {winner}")

    #  Game Logic
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):
            if self.game_over:
                raise GameOverError("X or O")

            if row < 0 or row >= 3 or col < 0 or col >= 3:
                raise InvalidMoveError((row, col), "Out of bounds")

            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "Position already taken")

            self.board[row][col] = self.current_player

    #  Test
    game = TicTacToe()
    test_moves = [(0, 0), (0, 0), (5, 5)]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"ok Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"invalid Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")
#lecture 2 unit 3
def practice_3_complete_system():
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)

    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            file = None
            try:
                file = open(filename, 'r')
                content = file.read()

            except FileNotFoundError:
                print(f"invalid File not found: {filename}")
                self.failed_files.append(filename)

            except PermissionError:
                print(f"invalid Permission denied: {filename}")
                self.failed_files.append(filename)

            except Exception as e:
                print(f"invalid Unexpected error: {e}")
                self.failed_files.append(filename)

            else:
                print(f"ok Processed: {filename}")
                self.processed_files.append(filename)

            finally:
                if file:
                    file.close()

        def process_directory(self, files):
            for file in files:
                self.process_file(file)

        def get_report(self):
            return {
                "processed": len(self.processed_files),
                "failed": len(self.failed_files),
                "success_files": self.processed_files,
                "failed_files": self.failed_files
            }

    #  Test
    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    processor.process_directory(test_files)

    report = processor.get_report()
    print(f"Report: {report}")