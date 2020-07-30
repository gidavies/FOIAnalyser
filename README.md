# FOIAnalyser

A proof of concept to look at how to provide analysis of a document and suggest words to be redacted.

## Implementation Notes

The core analysis engine being used is [Presidio](https://github.com/microsoft/presidio), which includes a Python analyser service and therefore this project is using Python to make the integration easier at this stage.