# Word finder

Pass a word or phrase to get the whole sentence in any number of text files.



## Description

This is a CLI python script. Runs by default on the directory of the word-finder.py if not changed by the CLI argument (runs only on one directory at a time). Scans all files or a list of them when the names are provided as arguments in the CLI.
There are 3 supported extensions(.txt, .doc, .docx). Can return a specified number of sentences after the one with the searched word or phrase if the optional argument is specified.



## Getting Started

### Dependencies

* Python 3.x. Runs only on pre-installed python packages.
* Packages: re, os, argparse, glob.

### Installing

```
git clone https://github.com/galudSla/word-finder.git
```


### CLI Arguments

`-h --help`       HELP\
`-w --word`       Word or phrase to search\
`-a --all`        Specify only if you want all the text files to be searched\
`-e --extensions` Extensions to be searched\
`-n --names`      Specify names of text files to be searched. Include the extensions\
`-s --sentences`  Number of sentences that come after the sentence that contains the word or phrase


### Executing program

* Place all the text files you want to search in the same folder or organize them in one directory. 

*Search 'foo' in the same directory on all the text files*
```
word-finder.py -w foo -a
```
*Search 'foo' in the same directory on all files with .docx extension*
```
word-finder.py -w foo -a -e .docx
```
*Search 'foo' in the same directory on specific text files*
```
word-finder.py -w foo -a -n bar.txt foobar.txt
```
*Search 'foo bar' in another directory on all text files*
```
word-finder.py -w foo bar -d <your-path> -a
```



## Help

CLI argument format:
```
[-h] [-d DIRECTORY] [-w [WORD [WORD ...]]] [-a] [-n [NAMES [NAMES ...]]] [-e [EXTENSIONS [EXTENSIONS ...]]] [-s SENTENCES]
```


## Authors

@galudSla\
email: tedgiann@gmail.com
