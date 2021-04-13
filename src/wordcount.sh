a="$(find . -name '*.tex' | xargs texcount -1 -sum *.tex)"
count_dt="$(date "+%Y-%m-%d %H:00")"
tag=$( tail -n 1 wordcount.txt )
if [ "$tag" != "${count_dt}|${a}|" ]; then echo "${count_dt} | ${a} |" >> wordcount.txt; fi
python3 wordcount.py
