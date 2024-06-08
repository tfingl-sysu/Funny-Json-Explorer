from Json import *
from Icon import *
from TreeComponent import *
# 树形Json，内部含有icon的建造和组合print
class TreeStyleJson(Json):
    def __init__(self):
        self.icon=None
    def build_icon(self,icon):
        self.icon=Icon().setIcon(icon)
    # 建立根
    def build_tree(self,json_data):
        keys=list(json_data.keys())
        # 非最后一个节点
        for name in keys[:-1]:
            # 子树不是叶子节点
            if type(json_data[name]) is dict: 
                root=TreeComposite(name)
                self.build_subtree(root,json_data[name])
            # 子树是叶子节点，但是空值
            elif json_data[name]!=None:
                root=TreeComposite(name+": "+json_data[name])
            # 子树是叶子节点，非空
            else:
                root=TreeComposite(name)
            root.print_tree([False],self.icon)
        # 最后一个节点
        name=keys[-1]
        # 子树不是叶子节点
        if type(json_data[name]) is dict: 
            root=TreeComposite(name)
            self.build_subtree(root,json_data[name])
        # 子树是叶子节点，但是空值
        elif json_data[name]!=None:
            root=TreeComposite(name+": "+json_data[name])
        # 子树是叶子节点，非空
        else:
            root=TreeComposite(name)
        root.print_tree([True],self.icon)
    # 建立子树
    def build_subtree(self,parent,children):
        for name in children.keys():
            # value是字典类型变量，需要继续充当新的根节点
            if type(children[name]) is dict:
                root=TreeComposite(name)
                self.build_subtree(root,children[name])
                parent.add(root)
            # value是一个值，与key一起作为叶节点
            else:
                # 注意空值不打印
                if children[name]!=None:
                    leaf=TreeLeaf(name+": "+children[name])
                else:
                    leaf=TreeLeaf(name)
                parent.add(leaf)
                