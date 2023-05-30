from colorama import Fore, Back, Style, init

init(autoreset=True)

def highlight_terminal(message, start_index, end_index, color_text=Fore.RED, color_back=Back.BLACK):
    print(message[:start_index], end="")
    print(color_text + color_back + message[start_index:end_index + 1] + Style.RESET_ALL, end="")
    print(message[end_index + 1:])

if __name__ == "__main__":
    highlight_terminal("Hello, can I help you?", 0, 4)