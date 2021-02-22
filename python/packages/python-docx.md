# python-docx

```python
document = Document()
styles = document.styles
style = styles.add_style('Citation', WD_STYLE_TYPE.PARAGRAPH)
style.base_style = styles['Normal']
styles['Citation'].delete()
```

## table 表格

默认格式
`table.style = 'LightShading-Accent1'`

### Table styles in default template

- Table Normal
- Colorful Grid
- Colorful Grid Accent 1
- Colorful Grid Accent 2
- Colorful Grid Accent 3
- Colorful Grid Accent 4
- Colorful Grid Accent 5
- Colorful Grid Accent 6
- Colorful List
- Colorful List Accent 1
- Colorful List Accent 2
- Colorful List Accent 3
- Colorful List Accent 4
- Colorful List Accent 5
- Colorful List Accent 6
- Colorful Shading
- Colorful Shading Accent 1
- Colorful Shading Accent 2
- Colorful Shading Accent 3
- Colorful Shading Accent 4
- Colorful Shading Accent 5
- Colorful Shading Accent 6
- Dark List
- Dark List Accent 1
- Dark List Accent 2
- Dark List Accent 3
- Dark List Accent 4
- Dark List Accent 5
- Dark List Accent 6
- Light Grid
- Light Grid Accent 1
- Light Grid Accent 2
- Light Grid Accent 3
- Light Grid Accent 4
- Light Grid Accent 5
- Light Grid Accent 6
- Light List
- Light List Accent 1
- Light List Accent 2
- Light List Accent 3
- Light List Accent 4
- Light List Accent 5
- Light List Accent 6
- Light Shading
- Light Shading Accent 1
- Light Shading Accent 2
- Light Shading Accent 3
- Light Shading Accent 4
- Light Shading Accent 5
- Light Shading Accent 6
- Medium Grid 1
- Medium Grid 1 Accent 1
- Medium Grid 1 Accent 2
- Medium Grid 1 Accent 3
- Medium Grid 1 Accent 4
- Medium Grid 1 Accent 5
- Medium Grid 1 Accent 6
- Medium Grid 2
- Medium Grid 2 Accent 1
- Medium Grid 2 Accent 2
- Medium Grid 2 Accent 3
- Medium Grid 2 Accent 4
- Medium Grid 2 Accent 5
- Medium Grid 2 Accent 6
- Medium Grid 3
- Medium Grid 3 Accent 1
- Medium Grid 3 Accent 2
- Medium Grid 3 Accent 3
- Medium Grid 3 Accent 4
- Medium Grid 3 Accent 5
- Medium Grid 3 Accent 6
- Medium List 1
- Medium List 1 Accent 1
- Medium List 1 Accent 2
- Medium List 1 Accent 3
- Medium List 1 Accent 4
- Medium List 1 Accent 5
- Medium List 1 Accent 6
- Medium List 2
- Medium List 2 Accent 1
- Medium List 2 Accent 2
- Medium List 2 Accent 3
- Medium List 2 Accent 4
- Medium List 2 Accent 5
- Medium List 2 Accent 6
- Medium Shading 1
- Medium Shading 1 Accent 1
- Medium Shading 1 Accent 2
- Medium Shading 1 Accent 3
- Medium Shading 1 Accent 4
- Medium Shading 1 Accent 5
- Medium Shading 1 Accent 6
- Medium Shading 2
- Medium Shading 2 Accent 1
- Medium Shading 2 Accent 2
- Medium Shading 2 Accent 3
- Medium Shading 2 Accent 4
- Medium Shading 2 Accent 5
- Medium Shading 2 Accent 6
- Table Grid

## paragraph 段落

`document.add_paragraph('Lorem ipsum dolor sit amet.', style='ListBullet')`

`paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
paragraph.style = 'List Bullet'`

一个段落里面的字符需要单独设置格式，拼接各部分，使用add_run()

```python
paragraph = document.add_paragraph('Lorem ipsum ')
run = paragraph.add_run('dolor')
run.bold = True
paragraph.add_run(' sit amet.')
#单独设置一个格式
paragraph.add_run('dolor').bold = True
paragraph_format = paragraph.paragraph_format
# margin
#paragraph_format.left_indent=Cm(1)
# paragraph_format.right_indent=Inches(0.5)
#paragraph_format.first_line_indent = Inches(-0.25)

#段落间距
# paragraph_format.space_before, paragraph_format.space_after

#行间距
# paragraph_format.line_spacing = Pt(18)
# paragraph_format.line_spacing = 1.75
```

### Paragraph styles in default template[¶](https://python-docx.readthedocs.io/en/latest/user/styles-understanding.html#paragraph-styles-in-default-template)

- Normal
- Body Text
- Body Text 2
- Body Text 3
- Caption
- Heading 1
- Heading 2
- Heading 3
- Heading 4
- Heading 5
- Heading 6
- Heading 7
- Heading 8
- Heading 9
- Intense Quote
- List
- List 2
- List 3
- List Bullet
- List Bullet 2
- List Bullet 3
- List Continue
- List Continue 2
- List Continue 3
- List Number
- List Number 2
- List Number 3
- List Paragraph
- Macro Text
- No Spacing
- Quote
- Subtitle
- TOCHeading
- Title

## character字符

- True means the property is “on”
- False means it is “off”
- None means “inherit”

```python
from docx import Document
from docx.shared import Pt
from docx.shared import RGBColor
document = Document()
run = document.add_paragraph().add_run()
font = run.font
font.name = 'Calibri'
font.size = Pt(12)
# font.bold, font.italic
# True  None WD_UNDERLINE
# font.underline = WD_UNDERLINE.DOT_DASH
font.color.rgb = RGBColor(0x42, 0x24, 0xE9)
```

### Character styles in default template

- Body Text Char
- Body Text 2 Char
- Body Text 3 Char
- Book Title
- Default Paragraph Font
- Emphasis
- Heading 1 Char
- Heading 2 Char
- Heading 3 Char
- Heading 4 Char
- Heading 5 Char
- Heading 6 Char
- Heading 7 Char
- Heading 8 Char
- Heading 9 Char
- Intense Emphasis
- Intense Quote Char
- Intense Reference
- Macro Text Char
- Quote Char
- Strong
- Subtitle Char
- Subtle Emphasis
- Subtle Reference
- Title Char

## section 节

```python
from docx import Document
from docx.enum.section import WD_SECTION
from docx.shared import Inches
document = Document()
sections = document.sections
section = sections[0]
current_section = document.sections[-1]  # last section in document
new_section = document.add_section(WD_SECTION.ODD_PAGE)
# section.orientation, section.page_width, section.page_height
# ection.left_margin, section.right_margin
# section.top_margin, section.bottom_margin
# section.header_distance, section.footer_distance
```

## header and footer 页眉页脚

```python
from docx import Document
document = Document()
section = document.sections[0]
header = section.header
# header.is_linked_to_previous
#header  edited just like a Document object
paragraph = header.paragraphs[0]
paragraph.text = "Title of my document"
# 通过tab stops实现header的布局
paragraph.text = "Left Text\tCenter Text\tRight Text"
# 默认设置 paragraph.style = document.styles["Header"]
```
