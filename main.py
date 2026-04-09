"""
CPU-Tamer - Python版本
Author: Your Name
"""
import String 

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

def SMT(int on_or_off)

def set_cpu(int core_count, int thread_count)

def parser(user_input):
    inputs_list=user_input.strip().split()
    command=inputs_list[0]
    if command is not None:
        args=inputs_list[1:]
    match command:
        case 'q':
            return -1
        case 'set':
            if args[0] is None:
                print("No argument for command: set")
                return 0
            else:
                arg=args[0]
                if (arg[1]=='c' and arg[3]=='t') and (arg[0].isdigit() and arg[2].isdigit):
                    core_count=int (arg[0]), thread_count=int (arg[2])
                else:
                    print("Illegal argument",args[0:],"for command set")
        case 'smt':        
            if args[0] is None:
                print("No argument for command: smt")
                return 0
            else:
                arg=args[0]
                match arg:
                    case 'on':
                        SMT(1)
                    case 'off':
                        SMT(0)
                    case _:
                        print("Illegal argument for comand smt:",arg)
                        return 0

    

def main():
    greetings()
    user_input = CLI()
    if(user_input==None):
        return
    
    
if __name__ == "__main__":
    main()