# Installation Guide
This document includes:

1. [Installing methods](#Installing-methods)
2. [Updating blogger-cli](#Updating-blogger-cli)
3. [Uninstalling blogger-cli](#Uninstalling-blogger-cli)
4. [Developing guide](#Developing-guide)

<a id="Installing-methods"></a>
## Installing methods

### Custom installer
```
curl -sSL https://raw.githubusercontent.com/hemanta212/blogger-cli//master/get_blogger.py
```

#### Why?
The custom installer provides an isolated installation for blogger-cli. It is sensible since blogger-cli relies on nbconvert / jupyter-core that have many dependencies and are likely to cause you some trouble.
Even if you install it in a virtual environment yourself, you need to constantly activate it to use the command. This installer solves exactly that; it puts 'blogger' command in the system's path.

### With pip
```
pip install blogger-cli
```
If you already have jupyter in your system python then a pip install will work just fine and you can access blogger without any hassle.


<a id="Updating-blogger-cli"></a>
## Updating blogger-cli
If you have installed through custom installation then,
```
blogger update
```
See blogger update --help for information regarding various options

**For pip installations**:
```
pip install --upgrade blogger-cli
```


<a id="Uninstalling-blogger-cli"></a>
## Uninstalling blogger-cli
```
blogger uninstall
```
If you have installed from custom installer

```
pip uninstall blogger-cli
```
If you have installed through pip

<a id="Developing-guide"></a>
## Developing guide
Clone the repository using,
```
$ git clone https://github.com/hemanta212/blogger-cli
```
change working directory into the blogger-cli folder
```
$ cd blogger-cli
```
Then install it in development mode using pip
```
pip install -e .
```
