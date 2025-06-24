#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件处理脚本：在指定文件开头和末尾添加 "happy code"
"""

import os
import sys
import argparse


def add_happy_code_to_file(file_path):
    """
    在指定文件的开头和末尾添加 "happy code"
    
    Args:
        file_path (str): 要处理的文件路径
    """
    if not os.path.exists(file_path):
        print(f"错误：文件 '{file_path}' 不存在！")
        return False
    
    try:
        # 读取原文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        # 在开头和末尾添加 "happy code"
        new_content = "happy code\n" + original_content + "\nhappy code"
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"成功在文件 '{file_path}' 的开头和末尾添加了 'happy code'！")
        return True
        
    except Exception as e:
        print(f"处理文件时发生错误：{e}")
        return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='在指定文件开头和末尾添加 "happy code"')
    parser.add_argument('file_path', help='要处理的文件路径')
    
    args = parser.parse_args()
    
    # 处理文件
    success = add_happy_code_to_file(args.file_path)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
