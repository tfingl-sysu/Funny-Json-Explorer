import argparse
import json
from Factory import *
if __name__ == '__main__':
    # 创建参数解析器
    parser=argparse.ArgumentParser(description='这是一个简单的命令行工具示例')
    # 添加命令行参数
    parser.add_argument('-f','--filename')
    parser.add_argument('-s','--style',default='tree')
    parser.add_argument('-i','--icon_family',default='none')
    # 解析命令行参数
    args=parser.parse_args()
    # 处理命令行参数并输出结果
    with open(args.filename) as f:
        json_data=json.load(f)
    # print(type(json_data))
    # print(json_data['oranges'])
    factory=AbstractFactory().createfactory(args.style)
    product=factory.create(args.icon_family)
    product.build_tree(json_data)