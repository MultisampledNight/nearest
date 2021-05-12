# nearest
Finds the nearest color in the colortable at https://github.com/meodai/color-names and returns it in a pretty format, along with name and distance.

## Images
![A picture of nearest how it outputs the found colors](https://user-images.githubusercontent.com/80128916/117981742-9fc41b00-b335-11eb-80cc-e29592decf08.png)

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
