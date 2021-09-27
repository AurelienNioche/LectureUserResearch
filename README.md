# LectureUserResearch

For installing jupyter notebook extensions (nbextensions)

    pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install 
    

Activate the extensions `Collapsible Headings` and `Table of Contents (2)`.
    

For converting a notebook with collapsible headings (CH) and table of contents (TOC) still available in HTML, use this command:

    jupyter nbconvert --to exporter.exporter.CH_TOC <mylecture>.ipynb --output docs/<mylecture>.html



