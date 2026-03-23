import os

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# decorator
def log_typing(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        if self: Logger.ison = self.typing
        Logger.log()
        
        return result
    return wrapper

# decorator
def log_mode(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        if self: Logger.mode = self.mode
        Logger.log()
        
        return result
    return wrapper

class Logger:
    ison = False
    mode = True

    @classmethod
    def _init(cls):
        print("https://github.com/amature0000/engkor_converter")
        print("EKconverter ver 4.0.0")

    @classmethod
    def log(cls):
        os.system('cls')
        cls._init()
        print()

        ison = f"{GREEN}ON{RESET}" if cls.ison else f"{RED}OFF{RESET}"
        mode = f"{YELLOW}한{RESET}" if cls.mode else f"{CYAN}영{RESET}"

        print(f"채팅창 상태\t{ison}")
        print(f"한/영 모드\t{mode}")

    @classmethod
    def update(cls, ison = None, mode = None):
        if ison: cls.ison = ison
        if mode: cls.mode = mode
        cls.log()
