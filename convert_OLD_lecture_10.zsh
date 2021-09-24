jupyter nbconvert OLD_lecture10.ipynb --output docs/lecture10.html
echo "copying images..."
rm -r docs/img
cp -r img docs
echo "done!"