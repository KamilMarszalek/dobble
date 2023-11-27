import select
import sys
import termios


def input_with_timeout(prompt, timeout):
    print(prompt, end="", flush=True)
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
