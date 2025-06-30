# https://github.com/ful1e5/Bibata_Cursor/releases/tag/v2.0.7

import os
import shutil

# 根据install.inf文件中的映射关系
mapping = {
    "Pointer.cur": "Arrow.cur",
    "Help.cur": "Help.cur",
    "Work.ani": "AppStarting.ani",
    "Busy.ani": "Wait.ani",
    "Cross.cur": "Cross.cur",
    "Text.cur": "IBeam.cur",
    "Handwriting.cur": "Pen.cur",
    "Unavailable.cur": "No.cur",
    "Vert.cur": "SizeNS.cur",
    "Horz.cur": "SizeWE.cur",
    "Dgn1.cur": "SizeNWSE.cur",
    "Dgn2.cur": "SizeNESW.cur",
    "Move.cur": "SizeAll.cur",
    "Alternate.cur": "UpArrow.cur",
    "Link.cur": "Hand.cur",
    "Pin.cur": "Pin.cur",
    "Person.cur": "Person.cur",
    "Pan.cur": "Pan.cur",
    "Grabbing.cur": "Grabbing.cur",
    "Zoom-in.cur": "Zoom-in.cur",
    "Zoom-out.cur": "Zoom-out.cur"
}

src_dir = "Bibata-Modern-Ice-Regular-Windows"
dst_dir = "EN"

replaced = []
not_found = []

for bibata_file, cn_file in mapping.items():
    bibata_path = os.path.join(src_dir, bibata_file)
    cn_path = os.path.join(dst_dir, cn_file)

    if os.path.exists(bibata_path) and os.path.exists(cn_path):
        shutil.copy2(bibata_path, cn_path)
        replaced.append(f"{bibata_file} -> {cn_file}")
    else:
        missing_files = []
        if not os.path.exists(bibata_path):
            missing_files.append(f"源文件: {bibata_file}")
        if not os.path.exists(cn_path):
            missing_files.append(f"目标文件: {cn_file}")
        not_found.append(f"{bibata_file} -> {cn_file} ({', '.join(missing_files)})")

print("=" * 60)
print("文件替换结果报告")
print("=" * 60)

if replaced:
    print(f"\n✅ 成功替换了 {len(replaced)} 个文件：")
    for i, file in enumerate(replaced, 1):
        print(f"  {i:2d}. {file}")
else:
    print("\n❌ 没有成功替换任何文件")

if not_found:
    print(f"\n⚠️  有 {len(not_found)} 个文件未找到对应关系：")
    for i, file in enumerate(not_found, 1):
        print(f"  {i:2d}. {file}")

print(f"\n📊 总结：")
print(f"   - 总映射数量：{len(mapping)}")
print(f"   - 成功替换：{len(replaced)}")
print(f"   - 未找到：{len(not_found)}")

if len(replaced) == len(mapping):
    print(f"\n🎉 所有文件都已成功替换！")
elif len(replaced) > 0:
    print(f"\n⚠️  部分文件替换成功，请检查未找到的文件")
else:
    print(f"\n❌ 没有文件被替换，请检查文件路径和映射关系")

print("=" * 60)
