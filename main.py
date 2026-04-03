"""
CPU-Tamer - Python版本
Author: Your Name
"""

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

def parser(user_input):
    inputs_list=user_input.split()
    for input in inputs_list:
        if input is 'q':
            return -1
        
        
    

def main():
    greetings()
    user_input = CLI()
    if(user_input==None):
        return
    
    
if __name__ == "__main__":
    main()