import os

def add_meta_to_md_files(docs_dir):
    # meta标签内容
    meta_content = '<meta name="referrer" content="no-referrer"/>\n\n'
    
    # 遍历docs目录下的所有文件
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            # 检查是否为md文件
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 检查文件开头是否已经有meta标签
                if not content.startswith('<meta name="referrer"'):
                    # 写入新内容
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(meta_content + content)
                    print(f'已添加meta标签到文件: {file_path}')
                else:
                    print(f'文件已包含meta标签,跳过: {file_path}')

if __name__ == '__main__':
    # 指定docs目录的路径
    docs_directory = './docs'
    
    # 检查目录是否存在
    if os.path.exists(docs_directory):
        add_meta_to_md_files(docs_directory)
        print('处理完成!')
    else:
        print('错误: docs目录不存在!')