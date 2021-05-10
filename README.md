# nearest
Finds the nearest color in the colortable at https://github.com/meodai/color-names and returns it in a pretty format, along with name and distance.

## Images
![A picture of nearest how it outputs the found colors](https://user-images.githubusercontent.com/80128916/117614699-fb8d7900-b168-11eb-8f22-5945f3b60c3c.png)

## Installation
```sh
?git clone https://github.com/MultisampledNight/nearest
?pip install -r nearest/requirements.txt
```

## Usage
```sh
?python nearest/main.py '#5f00ff'
?./nearest/main.py --help
```

You have to put the color in quotes, else your shell will probably interpret it.
It doesn't matter whether you use `./` or `python`, this allows you to simply symlink the main.py from somewhere on PATH.
