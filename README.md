# README
<h1 align="center">
  <br>
  <a href="https://openpecha.org"><img src="https://avatars.githubusercontent.com/u/82142807?s=400&u=19e108a15566f3a1449bafb03b8dd706a72aebcd&v=4" alt="OpenPecha" width="150"></a>
  <br>
</h1>

## format-otr
## Owner(s)

- [@spsither](https://github.com/spsither)

## RFXs

Requests for work (RFWs) and requests for comments (RFCs) associated with this project:

- [RFW0026](https://github.com/OpenPecha/Requests/issues/70)
- [RFC0026](https://github.com/OpenPecha/Format-otr/issues/4)

## Table of contents

<p align="center">
  <a href="#project-description">Project description</a> •
  <a href="#who-this-project-is-for">Who this project is for</a> •
  <a href="#project-dependencies">Project dependencies</a> •
  <a href="#instructions-for-use">Instructions for use</a> •
  <a href="#contributing-guidelines">Contributing guidelines</a> •
  <a href="#additional-documentation">Additional documentation</a> •
  <a href="#how-to-get-help">How to get help</a> •
  <a href="#terms-of-use">Terms of use</a>
</p>
<hr>

## Project description

This package is for formatting .otr file and Exporting it to other file types.

## Who this project is for

This project is for .otr reviewers and validator. This project is used to create the workflow for the [STT000 template](https://github.com/MonlamAI/STT000)

## Project dependencies

Before using _OpenPecha Project Template_, ensure you have:

- _python>=3.8_
- _pip>=23.0_

## Instructions for use
### Install format-otr

1.  install format-otr
  - `pip install git+https://github.com/OpenPecha/format-otr.git`

### Run format-otr

1. to export a txt file from an otr file with syllable count per-line
  >`export-txt <path to otr file>`
2. format an otr file
  >`format-otr <path to otr file>`
3. get total syllable count of an otr file
  >`summary-otr <path to otr file>`

## Contributing guidelines

If you'd like to help out, check out our [contributing guidelines](/CONTRIBUTING.md).



## How to get help

- File an issue.
- Email us at openpecha[at]gmail.com.
- Join our [discord](https://discord.com/invite/7GFpPFSTeA).

## Terms of use

format_otr is licensed under the [MIT License](/LICENSE.md).
