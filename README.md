# FOIAnalyser

A proof of concept to look at how to provide analysis of a document and suggest words to be redacted.

## Implementation Notes

The core analysis engine being used is [Presidio](https://github.com/microsoft/presidio), which includes a Python analyser service and therefore this project is using Python to make the integration easier at this stage.

## Running the script

Set up a Python environment. Presidio requires Python >= 3.6. The steps I tool were to create an Ubuntu 18.04 VM from the Azure marketplace and then:

- SSH into the VM:

    `ssh -i keyfile.pem username@ipaddress`

- Install PIP:

    `sudo apt install python3-pip`

- Install [python-docx] (https://python-docx.readthedocs.io/en/latest/) for working with Word documents:

    `pip3 install python-docx`

- Install the Presidio analyser:

    `pip3 install presidio_analyzer`

- Install the analyser dependency on ML Model web_lg:

    `python3 -m spacy download en_core_web_lg`

- Upload the script e.g.:

    `scp -i keyfile.pem ./foianalyser.py username@ipaddress:/path/to/dir`

- Test the script (with a word document) e.g.:

    `python3 foianalyser wordoc.docx profilename`