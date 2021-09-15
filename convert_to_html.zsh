#!/bin/zsh 
echo "converting notebook into html..."
jupyter nbconvert --to exporter.exporter.CH_TOC lecture02-user-study-design.ipynb --output docs/lecture2.html
echo "copying images..."
cp -r img docs
echo "done!"