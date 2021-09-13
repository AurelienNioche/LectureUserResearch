#!/bin/zsh 
echo "converting notebook into html..."
jupyter-nbconvert --to exporter.exporter.CH_TOC lecture.ipynb --output docs/lecture.html
echo "copying images..."
cp -r img docs
echo "done!"