#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown文件纯文本字数统计工具
统计指定目录及其子目录下所有.md文件的纯文本字数
去除markdown格式标记、图片链接等格式化内容
"""

import os
import re
import argparse
from pathlib import Path


def clean_markdown_text(content):
    """
    清理markdown内容，去除格式标记，保留纯文本
    
    Args:
        content (str): 原始markdown内容
        
    Returns:
        str: 清理后的纯文本
    """
    text = content
    
    # 去除代码块 (```)
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # 去除行内代码 (`)
    text = re.sub(r'`[^`]*`', '', text)
    
    # 去除图片链接 ![alt](url)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    
    # 去除链接，保留链接文本 [text](url)
    text = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', text)
    
    # 去除引用链接定义 [id]: url
    text = re.sub(r'^\[.*?\]:.*$', '', text, flags=re.MULTILINE)
    
    # 去除HTML标签
    text = re.sub(r'<[^>]*>', '', text)
    
    # 去除标题标记 (#)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    
    # 去除加粗标记 (**text** 或 __text__)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    
    # 去除斜体标记 (*text* 或 _text_)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    
    # 去除删除线标记 (~~text~~)
    text = re.sub(r'~~(.*?)~~', r'\1', text)
    
    # 去除列表标记 (-, *, +, 1.)
    text = re.sub(r'^\s*[-\*\+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    
    # 去除引用标记 (>)
    text = re.sub(r'^\s*>\s*', '', text, flags=re.MULTILINE)
    
    # 去除水平分割线 (--- 或 ***)
    text = re.sub(r'^[-\*]{3,}\s*$', '', text, flags=re.MULTILINE)
    
    # 去除表格分隔符
    text = re.sub(r'^\|.*\|\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*[-\|:\s]+\s*$', '', text, flags=re.MULTILINE)
    
    # 清理多余的空白字符
    text = re.sub(r'\n\s*\n', '\n\n', text)  # 多个空行合并为两个
    text = re.sub(r'[ \t]+', ' ', text)      # 多个空格合并为一个
    text = text.strip()
    
    return text


def count_chinese_chars(text):
    """
    统计中文字符数量
    
    Args:
        text (str): 输入文本
        
    Returns:
        int: 中文字符数量
    """
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    chinese_chars = ''.join(chinese_pattern.findall(text))
    return len(chinese_chars)


def count_english_words(text):
    """
    统计英文单词数量
    
    Args:
        text (str): 输入文本
        
    Returns:
        int: 英文单词数量
    """
    # 移除中文字符
    text_no_chinese = re.sub(r'[\u4e00-\u9fff]', ' ', text)
    # 提取英文单词
    english_words = re.findall(r'\b[a-zA-Z]+\b', text_no_chinese)
    return len(english_words)


def process_md_file(file_path):
    """
    处理单个markdown文件
    
    Args:
        file_path (Path): 文件路径
        
    Returns:
        dict: 包含文件统计信息的字典
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 清理markdown格式
        clean_text = clean_markdown_text(content)
        
        # 统计字符和单词
        total_chars = len(clean_text)
        chinese_chars = count_chinese_chars(clean_text)
        english_words = count_english_words(clean_text)
        
        return {
            'file': file_path,
            'original_size': len(content),
            'clean_text_size': total_chars,
            'chinese_chars': chinese_chars,
            'english_words': english_words,
            'success': True,
            'error': None
        }
        
    except Exception as e:
        return {
            'file': file_path,
            'original_size': 0,
            'clean_text_size': 0,
            'chinese_chars': 0,
            'english_words': 0,
            'success': False,
            'error': str(e)
        }


def find_md_files(directory):
    """
    查找目录下所有的markdown文件
    
    Args:
        directory (str): 目录路径
        
    Returns:
        list: markdown文件路径列表
    """
    md_files = []
    directory_path = Path(directory)
    
    if not directory_path.exists():
        raise ValueError(f"目录不存在: {directory}")
    
    # 递归查找所有.md文件
    md_files = list(directory_path.rglob("*.md"))
    
    return md_files


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='统计目录下所有Markdown文件的纯文本字数')
    parser.add_argument('directory', nargs='?', default='.', 
                       help='要统计的目录路径 (默认为当前目录)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='显示详细信息')
    
    args = parser.parse_args()
    
    try:
        # 查找所有markdown文件
        print(f"正在扫描目录: {os.path.abspath(args.directory)}")
        md_files = find_md_files(args.directory)
        
        if not md_files:
            print("未找到任何.md文件")
            return
        
        print(f"找到 {len(md_files)} 个markdown文件")
        print("=" * 50)
        
        # 统计信息
        total_stats = {
            'files_processed': 0,
            'files_failed': 0,
            'total_original_chars': 0,
            'total_clean_chars': 0,
            'total_chinese_chars': 0,
            'total_english_words': 0
        }
        
        failed_files = []
        
        # 处理每个文件
        for md_file in md_files:
            result = process_md_file(md_file)
            
            if result['success']:
                total_stats['files_processed'] += 1
                total_stats['total_original_chars'] += result['original_size']
                total_stats['total_clean_chars'] += result['clean_text_size']
                total_stats['total_chinese_chars'] += result['chinese_chars']
                total_stats['total_english_words'] += result['english_words']
                
                if args.verbose:
                    rel_path = os.path.relpath(result['file'])
                    print(f"文件: {rel_path}")
                    print(f"  原始字符数: {result['original_size']:,}")
                    print(f"  纯文本字符数: {result['clean_text_size']:,}")
                    print(f"  中文字符数: {result['chinese_chars']:,}")
                    print(f"  英文单词数: {result['english_words']:,}")
                    print()
            else:
                total_stats['files_failed'] += 1
                failed_files.append((result['file'], result['error']))
                if args.verbose:
                    print(f"处理失败: {result['file']} - {result['error']}")
        
        # 显示总结
        print("=" * 50)
        print("统计结果:")
        print(f"成功处理文件数: {total_stats['files_processed']}")
        if total_stats['files_failed'] > 0:
            print(f"处理失败文件数: {total_stats['files_failed']}")
        print()
        print(f"所有文件原始字符总数: {total_stats['total_original_chars']:,}")
        print(f"去除Markdown格式之后字符总数: {total_stats['total_clean_chars']:,}")
        
        # 显示失败的文件
        if failed_files and args.verbose:
            print("\n处理失败的文件:")
            for file_path, error in failed_files:
                print(f"  {file_path}: {error}")
                
        # 计算压缩比
        if total_stats['total_original_chars'] > 0:
            compression_ratio = (1 - total_stats['total_clean_chars'] / total_stats['total_original_chars']) * 100
            print(f"\nMarkdown格式去除比例: {compression_ratio:.1f}%")
        
    except Exception as e:
        print(f"错误: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
