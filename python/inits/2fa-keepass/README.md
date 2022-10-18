# 2FA-keepass

---



![tag](https://img.shields.io/badge/tag-testing-red.svg?github/tag-pre/aszadzinski/2fa-keepass.svg)
![commit](https://img.shields.io/github/last-commit/aszadzinski/2fa-keepass.svg)
![license](https://img.shields.io/github/license/aszadzinski/2fa-keepass.svg)

![status](https://img.shields.io/badge/build-falling-red.svg?style=flat&logo=Linux) ![status](https://img.shields.io/badge/build-falling-red.svg?style=flat&logo=Windows)

2fa-keepass is a password manager program that provides GUI application written in PyQt with some features like:

* reading .kdbx database
* 2FA support
* PGP/GPG keys manager

and many more in future.

**Nowadays, an application is unstable. Tested on lastest ArchLinux with Python 3.7.3.**

---

## Table of Contents

- [More about 2FAK](#More)
- [Installation](#Installation)
- [Features](#Features)
- [Getting started](#Getting-started)
  * [Import data](#Import-data)
  * [Export data](#Export-data)
  * [Integrations](#Integrations)
    - [gnupg](#gnupg)
    - [andOTP](#andOTP)
    - [Syncthing](#Syncthing)
    - [Jabber/XMPP](#Jabber)
  * [Command line](#Command-line)
  * [Workflow](#Workflow)
- [Contribute](#Contribute)

## More

XXX

## Installation

**Depedencies:**

- libkeepass
- sleekxmpp
- python-gnupg
- syncthing
- oathtool

### Linux

`git clone https://github.com/aszdzinski/2fa-keepass.git`

`cd 2fa-keepass/`

`python3 setup.py install`

### Using pip

`pip3 install 2fa-keepass`

### AUR

`makepkg XXX`  

## Features

* password manager in keepass format
  - [ ] compatible with [keepassx](https://github.com/keepassx/keepassx)
  - [ ] multiaccounts managements
  - [ ] sorted groups
  - [ ] generating secure and random passwords
  - [ ] AES or GPG encryption
* 2-factory-authentication
  - [ ] TOTP and HOTP support
  - [ ] compatible with [andOTP](https://github.com/andOTP/andOTP) for Android
  - [ ] possibility of storing keys in kdbx
  - [ ] exporting as QR code
* PGP/GPG
  - [ ] compatibile with gnupg
  - [ ] possibility of storing keys in kdbx
  - [ ] encrypting and decrypting message with sign and verification
  - [ ] symmetric encryption
* Integrations
  - [ ] synchronization using E2E from [Syncthing](https://github.com/syncthing/syncthing)
  - [ ] communications with app using Jabber/XMPP protocol
* dev
  - [ ] autoupdate

## Getting started

### Import data

### Export data

### Integrations

#### gnupg
### andOTP
#### Syncthing
#### Jabber

### Command line

### Workflow

## Contribute

* __Translations:__ : If you want to help translate 2FAK edit this file XXX .
* __Bug reports and feature requests:__ You can report bugs and request features in the Issue section on GitHub.

**Developers:**

* [Albert Szadzinski](https://github.com/aszadzinski/)
---
