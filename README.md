# LectureUserResearch

Warning! For the conversion to work, you need to use `nbconvert-5.6.1`

    pip install nbconvert==5.6.1

For installing jupyter notebook extensions (nbextensions)

    pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install 
    

Activate the extensions `Collapsible Headings` and `Table of Contents (2)`.
    

For converting a notebook with collapsible headings (CH) and table of contents (TOC) still available in HTML, use this command:

    jupyter nbconvert --to exporter.exporter.CH_TOC <mylecture>.ipynb --output docs/<mylecture>.html
