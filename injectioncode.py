import requests
from payloads import payloads
from colorama import Fore, Style

def check_command_injection(url, parameter):
    print(f"{Fore.GREEN}{'Payload':<50} {'Result'}{Style.RESET_ALL}")
    print("="*70)

    for payload in payloads:
        response = requests.get(url, params={parameter: payload}, timeout=5)

        if response.status_code == 200:
            result = f"{Fore.RED}[Vulnerable]{Style.RESET_ALL}"
        else:
            result = f"{Fore.YELLOW}[Failed: Status Code {response.status_code}]{Style.RESET_ALL}"

        print(f"{payload:<50} {result}")

if __name__ == "__main__":
    print(f"{Fore.CYAN}{'██╗   ██╗ ███████╗ ██████╗  ██████╗ ██╗   ██╗███████╗':^70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'██║   ██║ ██╔════╝██╔═══██╗██╔═══██╗██║   ██║██╔════╝':^70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'██║   ██║ ███████╗██║   ██║██║   ██║██║   ██║█████╗  ':^70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'██║   ██║ ╚════██║██║   ██║██║   ██║╚██╗ ██╔╝██╔══╝  ':^70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'╚██████╔╝ ███████║╚██████╔╝╚██████╔╝ ╚████╔╝ ███████╗':^70}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{' ╚═════╝  ╚══════╝ ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝':^70}{Style.RESET_ALL}")

    target_url = input(f"{Fore.MAGENTA}Enter the target URL: {Style.RESET_ALL}")
    target_parameter = input(f"{Fore.MAGENTA}Enter the target parameter: {Style.RESET_ALL}")
    check_command_injection(target_url, target_parameter)
