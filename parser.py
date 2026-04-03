class Parser:
    """命令解析器"""
    
    def __init__(self):
        self.COMMAND_COUNT = 64
        self.defined_commands = ["set", "q", "smt"]
        self.commands = []
        self.matched_command = None
    
    def get_commands(self, buffer):
        """分割输入字符串"""
        self.commands = buffer.split()
        
        if not self.commands:
            return False  # Python常用True/False
        
        # 限制命令数量
        if len(self.commands) > self.COMMAND_COUNT - 1:
            self.commands = self.commands[:self.COMMAND_COUNT - 1]
        
        return True
    
    def match_first_cmd(self):
        """匹配第一个命令"""
        if not self.commands:
            return False
        
        first_cmd = self.commands[0]
        if first_cmd in self.defined_commands:
            self.matched_command = first_cmd
            return True
        
        return False
    
    def parse_input(self, buffer):
        """解析输入"""
        if not self.get_commands(buffer):
            print("No valid command found")
            return False
        
        if not self.match_first_cmd():
            print(f"{self.commands[0]}: Not a command")
            return False
        
        return True