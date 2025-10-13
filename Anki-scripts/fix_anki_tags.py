#!/usr/bin/env python3
"""
将 Anki CSV 文件中标签列（示例为第三列）中引号内的逗号替换为空格。
用法: python fix_anki_tags.py "c:\\Users\\ZJHSteven\\Desktop\\AnkiTemp.csv"
会在同目录生成一个备份文件 AnkiTemp.csv.bak
"""
import csv
import sys
import shutil
import os


def fix_tags_in_csv(path):
    if not os.path.exists(path):
        print('file not found:', path)
        return 1

    backup = path + '.bak'
    shutil.copy2(path, backup)
    print('backup created at', backup)

    # 读取文件所有行，使用 csv.reader 保持解析正确
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print('empty file')
        return 1

    # 假设标签在最后一列（或者第三列，示例为第3），我们将尝试找到匹配的列数量并处理第三列（index 2）
    fixed_rows = []
    for r in rows:
        # 如果行列少于3，则不处理
        if len(r) >= 3:
            # 将第三列中的逗号替换为空格
            r[2] = r[2].replace(',', ' ')
        fixed_rows.append(r)

    # 写回文件（覆盖）
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(fixed_rows)

    print('file updated:', path)
    return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python fix_anki_tags.py <path-to-csv>')
        sys.exit(1)
    sys.exit(fix_tags_in_csv(sys.argv[1]))
