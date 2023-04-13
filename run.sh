#!/bin/bash

echo ">Initiating servers..."
echo ">Loading ICE..."
echo ">Welcome to HAAS-Bioroid internal servers."

#> generate template files from master json file (from netrunnerDB)
#args: 'json','card','card_tests','card_implement_list','deck_types'
#note: destructive, will overwrite all your hard work!
function generate(){
	python dev_utils/generate_templates.py $1
}

#> run unittests
#> args: 'all','games','cards'
function tests(){
	if [[ "$1" == "all" ]]; then
		echo "run all tests"
		python -m unittest discover -v generic_lib
	elif [[ "$1" == "games" ]]; then
		echo "run games tests"
		python -m unittest discover generic_lib/tests
	elif [[ "$1" == "cards" ]]; then
		echo "run card tests"
		python -m unittest discover generic_lib/cards/tests
	else
		echo "invalid tests params $@"
	fi
}

#use function name as CLI param
"$@"
