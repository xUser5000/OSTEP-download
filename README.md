# Description
A python script that downloads all online chapters of the free textbook Operating System: Three Easy Pieces (OSTEP for short).

# Run
```bash
git clone https://github.com/xUser5000/OSTEP-download.git  # clone the repo
cd OSTEP-download
pip install -r requirements.txt  # install the script dependencies (BeautifulSoup and Requests)
python script.py
```

# How it works
1. Scrapes https://pages.cs.wisc.edu/~remzi/OSTEP/
2. Finds all `<a>`s whose `href` end with `.pdf`
3. For each pdf file, makes a new thread and downloads the file on disk
