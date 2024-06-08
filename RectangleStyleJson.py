from Json import *
from Icon import *
from RectangleComponent import *
# 全局变量获取输出最长的长度以规整矩形
maxlen=0
# 树形Json，内部含有icon的建造和组合print
class RectangleStyleJson(Json):
    def __init__(self):
        self.icon=None
    # 建立icon
    def build_icon(self,icon):
        self.icon=Icon().setIcon(icon)
    # 建立根
    def build_tree(self,json_data):
        global maxlen
        keys=list(json_data.keys())
        # 第一个节点
        name=keys[0]
        # 子树不是叶子节点
        if type(json_data[name]) is dict: 
            root=RectangleComposite(name)
            length=len(name)
            if length>maxlen:
                maxlen=length
            self.build_subtree(root,json_data[name],2)
        # 子树是叶子节点，但是空值
        elif json_data[name]!=None:
            newname=name+": "+json_data[name]
            root=RectangleComposite(newname)
            length=len(newname)
            if length>maxlen:
                maxlen=length
        # 子树是叶子节点，非空
        else:
            root=RectangleComposite(name)
            length=len(name)
            if length>maxlen:
                maxlen=length
        # 下面代码有未解决的问题:根节点只有一颗子树时如何打印矩形结构?如果只有一行如何打印?
        root.print_tree(1,self.icon,maxlen)
        # 非最后一个节点
        for name in keys[1:-1]:
            # 子树不是叶子节点
            if type(json_data[name]) is dict: 
                root=RectangleComposite(name)
                length=len(name)
                if length>maxlen:
                    maxlen=length
                self.build_subtree(root,json_data[name],2)
            # 子树是叶子节点，但是空值
            elif json_data[name]!=None:
                newname=name+": "+json_data[name]
                root=RectangleComposite(newname)
                length=len(newname)
                if length>maxlen:
                    maxlen=length
            # 子树是叶子节点，非空
            else:
                root=RectangleComposite(name)
                length=len(name)
                if length>maxlen:
                    maxlen=length
            root.print_tree(0,self.icon,maxlen)
        # 最后一个节点
        if len(keys)>1:
            name=keys[-1]
            # 子树不是叶子节点
            if type(json_data[name]) is dict: 
                root=RectangleComposite(name)
                length=len(name)
                if length>maxlen:
                    maxlen=length
                self.build_subtree(root,json_data[name],2)
            # 子树是叶子节点，但是空值
            elif json_data[name]!=None:
                newname=name+": "+json_data[name]
                root=RectangleComposite(newname)
                length=len(newname)
                if length>maxlen:
                    maxlen=length
            # 子树是叶子节点，非空
            else:
                root=RectangleComposite(name)
                length=len(name)
                if length>maxlen:
                    maxlen=length
            root.print_tree(-1,self.icon,maxlen)
    # 建立子树
    def build_subtree(self,parent,children,depth):
        global maxlen
        for name in children.keys():
            # value是字典类型变量，需要继续充当新的根节点
            if type(children[name]) is dict:
                root=RectangleComposite(name)
                self.build_subtree(root,children[name],depth+1)
                parent.add(root)
            # value是一个值，与key一起作为叶节点
            else:
                # 注意空值不打印，计算最长长度
                if children[name]!=None:
                    newname=name+": "+children[name]
                    leaf=RectangleLeaf(newname)
                    length=len(newname)+3*depth
                    if length>maxlen:
                        maxlen=length
                else:
                    leaf=RectangleLeaf(name)
                    length=len(name)+3*depth
                    if length>maxlen:
                        maxlen=length
                parent.add(leaf)
                