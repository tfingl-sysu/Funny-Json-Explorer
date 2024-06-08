from Icon import *
# maxlen=0
# def set_maxlen(value):
#     global maxlen
#     maxlen=value
class RectangleComponent:
    def print_tree(self,endflag,icon,depth=0):
       pass
# 叶子节点
class RectangleLeaf(RectangleComponent):
    def __init__(self,name):
        self.name=name
    def print_tree(self,lineflag,icon,maxlen,depth=0):
        startflag=True
        for _ in range(depth):
            if lineflag==-1 and startflag:
                print('└──',end='')
                startflag=False
            elif lineflag==-1:
                print('┴──',end='')
            else:
                print('│  ',end='')
        if lineflag==-1 and startflag:
            print('└─',end='')
            startflag=False
        elif lineflag==-1:
            print('┴─',end='')
        else:
            print('├─',end='')
        # print(' ',end='')
        icon.print_leaf()
        print(self.name,end='')
        length=(depth+1)*3+len(self.name)
        while length<maxlen+4:
            print('─',end='')
            length+=1
        if lineflag==-1:
            print('┘')
        else:
            print('┤')
# 组合节点
class RectangleComposite(RectangleComponent):
    def __init__(self,name):
        self.name=name
        self.children=[]
    def add(self,child):
        self.children.append(child)
    def remove(self,child):
        self.children.remove(child)
    def print_tree(self,lineflag,icon,maxlen,depth=0):
        size=len(self.children)
        for _ in range(depth):
            if size or lineflag!=-1:
                print('│  ',end='')
            else:
                print('└──',end='')
        if lineflag==1:
            print('┌─',end='')
        elif lineflag==-1 and size==0:
            if depth==0:
                print('└─',end='')
            else:
                print('┴─',end='')
        else:
            print('├─',end='')
        # print(' ',end='')
        icon.print_node()
        print(self.name,end='')
        length=(depth+1)*3+len(self.name)
        while length<maxlen+4:
            print('─',end='')
            length+=1
        if lineflag==1:
            print('┐')
        elif lineflag==-1 and size==0:
            print('┘')
        else:
            print('┤')
        for i in range(size-1):
            self.children[i].print_tree(0,icon,maxlen,depth+1)
        if size:
            if lineflag==-1:
                self.children[-1].print_tree(lineflag,icon,maxlen,depth+1)
            else:
                self.children[-1].print_tree(0,icon,maxlen,depth+1)