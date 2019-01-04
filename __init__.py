import os
class pysh:
    def __getatrribute__(attr):
        class cmd:
            def __init__(self,command):
                self.cmd=command
            def __call__(self,*args):
                if self.cmd=='cd':
                    return os.chdir(*args[0])
                return os.system(self.cmd+' '+' '.join(args))
        return cmd(attr)
