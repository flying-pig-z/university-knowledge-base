import os
from pathlib import Path

class DocsifySidebarGenerator:
    def __init__(self, docs_dir):
        self.docs_dir = Path(docs_dir)
        self.ignore_files = {'_sidebar.md', '.nojekyll', '_navbar.md', '_404.md', '_coverpage.md'}
        self.indent_spaces = 2

    def is_markdown_file(self, file_path):
        return file_path.suffix.lower() == '.md'

    def get_relative_path(self, file_path):
        return str(file_path.relative_to(self.docs_dir)).replace('\\', '/')

    def get_title_from_file(self, file_path):
        """直接使用文件名作为标题（不包含.md后缀）"""
        return file_path.stem

    def generate_sidebar_content(self, current_dir, level=0):
        content = []
        indent = ' ' * (level * self.indent_spaces)
        
        # 首先处理当前目录的 README.md 或 index.md
        readme_path = current_dir / 'README.md'
        index_path = current_dir / 'index.md'
        if readme_path.exists():
            rel_path = self.get_relative_path(readme_path)
            title = self.get_title_from_file(readme_path)
            content.append(f'{indent}* [{title}](/{rel_path})')
        elif index_path.exists():
            rel_path = self.get_relative_path(index_path)
            title = self.get_title_from_file(index_path)
            content.append(f'{indent}* [{title}](/{rel_path})')

        # 获取所有文件和目录
        items = sorted(current_dir.iterdir())
        
        # 首先处理文件
        for item in items:
            if item.is_file() and self.is_markdown_file(item):
                if item.name not in self.ignore_files and item.name not in ['README.md', 'index.md']:
                    rel_path = self.get_relative_path(item)
                    title = self.get_title_from_file(item)
                    content.append(f'{indent}* [{title}](/{rel_path})')

        # 然后处理子目录
        for item in items:
            if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('_'):
                dir_name = item.name
                content.append(f'{indent}* {dir_name}')
                # 递归处理子目录
                sub_content = self.generate_sidebar_content(item, level + 1)
                content.extend(sub_content)

        return content

    def generate(self):
        """生成 _sidebar.md 文件"""
        sidebar_content = self.generate_sidebar_content(self.docs_dir)
        
        # 写入 _sidebar.md 文件
        sidebar_path = self.docs_dir / '_sidebar.md'
        with open(sidebar_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sidebar_content))
        
        print(f"Successfully generated _sidebar.md at {sidebar_path}")

def main():
    # 获取当前目录下的 docs 文件夹路径
    docs_dir = Path.cwd() / 'docs'
    
    if not docs_dir.exists():
        print(f"Error: {docs_dir} directory not found!")
        return
    
    # 生成 .nojekyll 文件
    nojekyll_path = docs_dir / '.nojekyll'
    if not nojekyll_path.exists():
        nojekyll_path.touch()
        print("Created .nojekyll file")
    
    # 生成侧边栏
    generator = DocsifySidebarGenerator(docs_dir)
    generator.generate()

if __name__ == '__main__':
    main()