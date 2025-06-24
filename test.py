#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件处理脚本：在指定文件开头和末尾添加 "happy code"，并打包为tar文件
"""

import os
import sys
import argparse
import tarfile
import datetime


def add_happy_code_to_file(file_path):
    """
    在指定文件的开头和末尾添加 "happy code"
    
    Args:
        file_path (str): 要处理的文件路径
        
    Returns:
        bool: 处理是否成功
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


def create_tar_archive(file_path):
    """
    将处理过的文件打包为tar文件
    
    Args:
        file_path (str): 要打包的文件路径
        
    Returns:
        str: tar文件路径，如果失败返回None
    """
    try:
        # 生成tar文件名（基于原文件名和时间戳）
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        tar_filename = f"{base_name}_happy_code_{timestamp}.tar"
        
        # 创建tar文件
        with tarfile.open(tar_filename, 'w') as tar:
            # 添加文件到tar包中，使用原始文件名作为归档名
            tar.add(file_path, arcname=os.path.basename(file_path))
        
        print(f"成功创建tar文件：'{tar_filename}'")
        return tar_filename
        
    except Exception as e:
        print(f"创建tar文件时发生错误：{e}")
        return None


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='在指定文件开头和末尾添加 "happy code" 并打包为tar文件')
    parser.add_argument('file_path', help='要处理的文件路径')
    parser.add_argument('--no-tar', action='store_true', help='不创建tar文件，只处理文件内容')
    
    args = parser.parse_args()
    
    # 处理文件
    success = add_happy_code_to_file(args.file_path)
    
    if not success:
        sys.exit(1)
    
    # 如果处理成功且用户没有指定--no-tar，则创建tar文件
    if not args.no_tar:
        tar_file = create_tar_archive(args.file_path)
        if tar_file:
            print(f"任务完成！处理后的文件已打包为：'{tar_file}'")
        else:
            print("文件处理成功，但tar打包失败！")
            sys.exit(1)
    else:
        print("任务完成！文件已处理（未创建tar包）")


if __name__ == "__main__":
    main()
