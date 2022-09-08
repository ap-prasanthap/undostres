#!/bin/bash

# run pytest website test - step2
echo "Run UnDosTres tests"
py.test
echo "UnDosTres tests complete"

allure generate reports/allure-results/ --clean
