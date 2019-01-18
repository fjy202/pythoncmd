import os,sys
class __main__:
    def __getattribute__(self,attr):
        class _cmd:
            def __init__(self,command):
                self.cmd=command
            def __call__(self,*args):
                if self.cmd=='cd':
                    return os.chdir(*args[0])
                return os.system(self.cmd+' '+(' '.join(args)))
            def __repr__(self):
                return '<cmd object command='+self.cmd+'>'
        return _cmd(attr)
sys.modules[__name__]=__main__()

