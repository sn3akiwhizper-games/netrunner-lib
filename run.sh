#!/bin/bash

echo ">Initiating servers..."
echo ">Loading ICE..."
echo ">Welcome to HAAS-Bioroid internal servers."

#> generate template files from master json file (from netrunnerDB)
#args: 'json','card','card_tests','card_implement_list','deck_types'
#note: destructive, will overwrite all your hard work!
function generate_templates(){
	python dev_utils/generate_templates.py $1
}

#> run unittests
#> args: 'all','games','cards'
function tests(){
	TESTS_DIR=netrunner_lib/netrunner_lib/tests
	if [[ "$1" == "all" ]]; then
		echo "run all tests"
		python -m unittest discover -v $TESTS_DIR
	elif [[ "$1" == "games" ]]; then
		echo "run games tests"
		python -m unittest discover $TESTS_DIR/gameplay_tests
	elif [[ "$1" == "players" ]]; then
		echo "run player tests"
		python -m unittest $TESTS_DIR/test_players.py
	elif [[ "$1" == "cards" ]]; then
		echo "run card tests"
		python -m unittest discover $TESTS_DIR/card_tests
	else
		echo "invalid tests params $@"
	fi
}

function generate_docs(){
	PKG_DIR=netrunner_lib/netrunner_lib
	CODE_DOCS_DIR=wiki/CodeDocs
	source $PKG_DIR/.env
	PROJECT_REPO_PATH=$PROJECT_REPO_PATH pdoc --html --force --output-dir $CODE_DOCS_DIR $PKG_DIR/*.py
}

#use function name as CLI param
"$@"
