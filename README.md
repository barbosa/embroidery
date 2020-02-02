# Embroidery

[![Build Status](https://travis-ci.com/barbosa/embroidery.svg?branch=master)](https://travis-ci.com/barbosa/embroidery)

## Motivation

TODO

## Requirements

Make sure you have both ImageMagick (for image rendering) and GhostScript (for custom text rendering) installed:

On macOS:

```
brew install imagemagick
brew install gs
```

_NOTE: This library was tested only using ImageMagick version >7. It's not guaranteed it will work with older versions._

## Installation

```
pip install embroidery
```

## Usage

### Basic

```
embroidery --file icon.png --text BETA
```

=> Output image here

### Advanced

#### Custom color

```
embroidery --file icon.png \
    --color 33cc60 \
    --text BETA
```

=> Output image here

#### Gradient color

```
embroidery --file icon.png \
    --color FF00FF-FFFF00 \
    --text BETA
```

=> Output image here

#### Custom text color

```
embroidery --file icon.png \
    --color FF00FF-FFFF00 \
    --text BETA \
    --text-color 333
```

=> Output image here

#### Custom position

```
embroidery --file icon.png \
    --color FF00FF-FFFF00 \
    --text BETA \
    --position TL
```

=> Output image here

### Full list of options

```
$ embroidery --help

Usage: embroidery [OPTIONS]

Options:
  -f, --file PATH               Image to apply embroidery.  [required]
  -c, --color TEXT              Background color. Defaults to black.
  -t, --text TEXT               Text on top of embroidery. Defaults to None.
  -k, --text-color TEXT         Defaults to white.
  -p, --position [TL|TR|BL|BR]  Top Left, Top Right (default), Bottom Left,
                                Bottom Right.
  -o, --output TEXT             Path for result image. Defaults to image name
                                + '_embroidered'.
  --help                        Show this message and exit.
```

## Contributing

Coming soon

## License

This project is distributed under the [MIT License](https://github.com/barbosa/embroidery/blob/master/LICENSE).
