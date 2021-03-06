# Keypirinha Plugin: Command

This is Command, a plugin for the
[Keypirinha](http://keypirinha.com) launcher.

This plugin provides an easy way to execute simple commands from Keypirinha.

| ![Command usage](./images/demo.gif "Command usage") |
| :-: |
| *Command demo* |

## Install:

There are two ways to install:

1. Using **[PackageControl](https://github.com/ueffel/Keypirinha-PackageControl)**:

    - Invoke Keypirinha and type `install package`.
    - Click enter.
    - Now search for package `Keypirinha-Command`.
    - Again press enter.

2. Manual:

    Download the latest plugin file from [here](https://github.com/bantya/Keypirinha-Command/releases/latest).

    Once the `Command.keypirinha-package` file is downloaded,
    move it to the `InstalledPackage` folder located at:

    - `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**
    - **Or** `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** (the
    final path would look like
    `C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`)

**NOTE:** You may have to manually restart Keypirinha to see the package activated.


## Configuration:

0. NO configuration is required.


## Usage:

Invoke Keypirinha and put the command to be executed in following format:
```
[>] [command (can contain spaces)]
-OR-
[>>] [command (can contain spaces)]

e.g.

> echo 'Hello World'
>> ping google.com
```

| ![Command usage](./images/usage.png "Command usage") |
| :-: |
| *Command usage* |


### Difference between > and >>:

Running any command with `>>` will close the CMD after completion of the command.

In case of `>`, CMD will be kept open!


### Actions

There are two actions available irrespective of the configuration.

| ![Command actions](./images/actions.png "Command actions") |
| :-: |
| *Command actions* |

- **Keep Open**: Do not close the prompt after running the command.
- **Close CMD**: Close the prompt after running the command.

*NOTE: These actions have first preference, if applied with a command.*


## Change Log:

### v1.1.0

- Added >> (CMD close keyword).
- Updated README.
- Updated config file.

### v1.0.1

- Added PackageControl section in README.
- Updated config file.

### v1.0.0

- Initial release.
- Added actions.


## License

MIT, that's it.


## Credits

*Waiting for the first name to appear here.*


## Contribute

Here is how to contribute:

1. Check for open issues or open a fresh issue to start a discussion around a
   feature idea or a bug.
2. Fork this repository on GitHub to start making your changes to the **dev**
   branch.
3. Send a pull request.
4. Add yourself to the *Contributors* section below (or create it if needed)!


## Anything else?
No, Thanks to all.
