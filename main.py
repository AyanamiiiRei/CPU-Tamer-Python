"""
CPU-Tamer - Python版本
Author: Your Name
"""
# import String 
CPU_Core_Count=4
CPU_Thread_count=8

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

def cpu_state_checker(core_count:int, thread_count: int):
    if core_count>0 and core_count <=CPU_Core_Count:
        if thread_count>=core_count:
            if thread_count<=CPU_Thread_count:
                return True
    return False

def toggle_cpu_state(on_or_off: int,cpu_index: int):
    if not (cpu_index>0 and cpu_index<=CPU_Thread_count):
        return 0
    path=f"/sys/devices/system/cpu/cpu{cpu_index}/online"
    if on_or_off:
        state=1
    else:
        state=0
    # 错误处理用 try/except
    try:
        with open(path, 'w') as f:
            f.write(str(state))
            print(f"Set CPU {cpu_index} status to:",state)
            return 0
    except OSError as e:
        print(f"toggle_cpu_state cpu{cpu_index} Error: {e}")
        return 1

def set_cpu(core_count: int , thread_count: int):
    if not cpu_state_checker(core_count,thread_count):
        print("Illegal cores and threads parameter:",core_count,thread_count)
        return 1
    vice_threads=thread_count-core_count
    for i in range(1,CPU_Core_Count):
        if (i<core_count):
            # print(f"toggle_cpu_state(1,{i})")
            toggle_cpu_state(1,i)
        else:
            toggle_cpu_state(0,i)
            
    for i in range(CPU_Core_Count,CPU_Thread_count):
        if ((i-CPU_Core_Count)<vice_threads):
            # print(f"toggle_cpu_state(1,{i})")
            toggle_cpu_state(1,i)
        else:
            toggle_cpu_state(0,i)

    return 0



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
                    return set_cpu(core_count,thread_count)
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