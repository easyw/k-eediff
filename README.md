# k-eediff

Visual diff tool for KiCAD eeschema:
![icon](./k-eediff-svg.svg)

1) plot as svg the two eeschema pages to compare in BW i.e. sheet_1.svg sheet_2.svg
2) usage: ```python3 k-eediff-svg.py sheet_1.svg sheet_2.svg```
3) the result will be displayed in ```sheet_1-diff-sheet_2.svg```

note: any modern browser should show correctly the diff file as colored svg

![screenshot](./k-eediff-example.png)