# Logo 资源

本目录用于存放公司、学校的本地 logo 图片。

当前已包含学校 logo（来自官网）：
- `bjtu.png` - 北京交通大学
- `suda.png` - 苏州大学

## 公司 Logo

在 `personal_page.py` 的 EXPERIENCE 中为对应公司添加 `"logo": "文件名.png"`：

```python
{
    "org": "美团",
    "logo": "meituan.png",  # 使用 logos/meituan.png
    ...
}
```

## 学校 Logo

在 `personal_page.py` 的 EDUCATION 中为对应学校添加 `"logo": "文件名.png"`：

```python
{
    "school": "北京交通大学",
    "logo": "bjtu.png",  # 使用 logos/bjtu.png
    ...
}
```

建议尺寸：64×64 或 128×128 像素，支持 PNG、JPG、SVG 格式。
