# LaTeX Word Count
by H. M. Wakeling, inspired by S. Alden

LaTeX Word Count is a quick bash wordcount that uses texcount to count all .tex files in a given directory. The word count is then stored alongside the time the program was run and the data points are available to plot.

## Requirements

* `texcount` (https://app.uio.no/ifi/texcount/howto.html)
* python3, matplotlib, numpy

## Installation
Clone this 

## Usage
`./wordcount.sh` counts all words in all .tex files under current directory. The values are then stored an plotted. Basic implementation has been included to prevent too many data points per day.

![A plot of word count for each date that the program has been run](https://github.com/hmwakeling/LaTeX-word-count/blob/main/wordcount.png)

Fun usage: add ./wordcount.sh to your git hook pre-commit file to keep a detailed progression of your project (i.e. thesis!)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License