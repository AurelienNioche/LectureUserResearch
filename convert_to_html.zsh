#!/bin/zsh 
echo "converting notebook into html..."
jupyter nbconvert --to exporter.exporter.CH_TOC lecture02-user-study-design.ipynb --output docs/lecture2.html
jupyter nbconvert --to exporter.exporter.CH_TOC lecture02-user-study-design.ipynb --output docs/lecture02.html
jupyter nbconvert --to exporter.exporter.CH_TOC lecture03-inference.ipynb --output docs/lecture03.html
jupyter nbconvert --to exporter.exporter.CH_TOC lecture04-data-visualization.ipynb --output docs/lecture04.html
jupyter nbconvert --to exporter.exporter.CH_TOC lecture08-developing-brain-computer-interfaces.ipynb --output docs/lecture08.html
echo "copying images..."
rm -r docs/img
cp -r img docs
echo "done!"