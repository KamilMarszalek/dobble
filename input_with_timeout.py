import select
import sys
import termios
from typing import Optional


def input_with_timeout(prompt: str, timeout: int) -> Optional[str]:
    """Enables inputs with set timeout"""
    print(prompt, end="\n", flush=True)
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return sys.stdin.readline().rstrip()
        else:
            return None
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)