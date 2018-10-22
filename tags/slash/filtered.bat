REM no tests
slash run -k "tag:simple and not simple" tests

REM one test
slash run tests -k "tag:simple and smoke"

REM two tests
slash run -k "REGRESSION and not simple" tests