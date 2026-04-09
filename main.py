"""
CPU-Tamer - Python版本
Author: Your Name
"""
# import String 

def main():
    """主函数 - 相当于C的int main()"""
    print("Hello from Python!")
    return 0  # 可以返回，但通常不需要

def greetings():
    print("Welcome using CPU Tamer\nThis is a version written in Python\n"
    "Reminder: You need to run this program with root privilges!!!\n")

def CLI():
    try:
        user_input=input("CPU-Tamer>>")
    except EOFError: # Ctrl+D
        user_input=None
    except KeyboardInterrupt:# Ctrl+C
        user_input=None
    return user_input

def SMT(on_or_off: int):
    path="/sys/devices/system/cpu/smt/control"
    if on_or_off:
        state="on"
    else:
        state="off"
    # 错误处理用 try/except
    try:
        with open(path, 'w') as f:
            f.write(str(state))
            print("Set SMT status to:",state)
    except OSError as e:
        print(f"Error: {e}")

def set_cpu(core_count: int , thread_count: int):
    vice_threads=thread_count-core_count
    

def parser(user_input):
    inputs_list=user_input.strip().split()
    command=inputs_list[0]
    if command is not None:
        args=inputs_list[1:]
        # print("Debug - args:",args)
    match command:
        case 'q':
            return -1
        case 'set':
            if args == []:
                print("No argument for command: set")
                return 1
            else:
                arg=args[0]
                if len(arg)!=4:
                    print("Illegal argument(",arg,") for set")
                    # print("Illegal argument",arg," for set")
                    return 1
                if (arg[1]=='c' and arg[3]=='t') and (arg[0].isdigit() and arg[2].isdigit()):
                    core_count = int (arg[0])
                    thread_count = int (arg[2])
                    #implement
                    return 0
                else:
                    print("Illegal argument",arg,"for command set")
        case 'smt':       
            if args == []:
                print("No argument for command: smt")
                return 1
            else:
                arg=args[0]
                match arg:
                    case 'on':
                        SMT(1)
                        return 0
                    case 'off':
                        SMT(0)
                        return 0
                    case _:
                        print("Illegal argument for comand smt:",arg)
                        return 1
        case _:
            print("No command found for:",user_input)
            return 1

    
def main():
    greetings()
    while True:
        user_input = CLI()
        if(user_input==None):
            print("You've entered nothing")
            return
        exit_code=parser(user_input)
        match exit_code:
            case -1:
                print("Exit...")
                return
            case _:
                continue
    
    
if __name__ == "__main__":
    main()
    # return