cli_string="CPU-Tamer>>"
global user_input

def CLI():
    while true:
            try:
                user_input=input(cli_string)
            except EOFError: # Ctrl+D
                user_input=None
            except KeyboardInterrupt:# Ctrl+C
                user_input=None
            return user_input
