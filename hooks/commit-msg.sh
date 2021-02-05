#!/bin/sh

RETURN_CODE=0
INVALID_RETURN_CODE=255

COMMIT_MSG_PATH="$1"
COMMIT_MSG_HEADER=$(head -n 1 "$COMMIT_MSG_PATH")
COMMIT_MSG_HEADER_LINE_N="1"
COMMIT_MSG_BODY=$(tail -n +2 "$COMMIT_MSG_PATH")
COMMIT_MSG_BODY_START_LINE=2

COMMIT_MSG_HEADER_MAX_LEN=50
COMMIT_MSG_BODY_MAX_LEN=72
COMMIT_MSG_HEADER_REGEX="^(revert: )?(feat|fix|build|ci|docs|style|refactor|perf|test)(\(.+\))?: .*$"
INVALID_COMMIT_MESSAGE_HEADER="This commit message header does not match our standard, take a look at our COMMIT_CONVETION.md."
INVALID_COMMIT_MESSAGE_COLUMN_SIZE="Line %s should be at most %s characters long.\n"
EDIT_HELP_MESSAGE="In order to edit yout previous commit messate simply run: git commit --edit --file=.git/COMMIT_EDITMSG."

check_line_len()
{
    LINE=$1
    MAX_LEN=$2
    LINE_N=$3
    if [ ${#LINE} -gt "$MAX_LEN" ]
    then
        printf "$INVALID_COMMIT_MESSAGE_COLUMN_SIZE" "$LINE_N" "$MAX_LEN"
        RETURN_CODE=$((INVALID_RETURN_CODE))
    fi
}

if ! echo "$COMMIT_MSG_HEADER" | grep -Eq "$COMMIT_MSG_HEADER_REGEX"; then
    printf "%s\n" "$INVALID_COMMIT_MESSAGE_HEADER"
    RETURN_CODE=$((INVALID_RETURN_CODE))
fi

check_line_len "$COMMIT_MSG_HEADER" "$COMMIT_MSG_HEADER_MAX_LEN" "$COMMIT_MSG_HEADER_LINE_N"

line_n=$COMMIT_MSG_BODY_START_LINE
while IFS= read -r COMMIT_MSG_BODY_LINE; do
    check_line_len "$COMMIT_MSG_BODY_LINE" "$COMMIT_MSG_BODY_MAX_LEN" "$line_n"
    line_n=$((line_n+1))
done < <(printf '%s\n' "$COMMIT_MSG_BODY")

if [ "$RETURN_CODE" -eq "$INVALID_RETURN_CODE" ]; then
    printf "%s\n" "$EDIT_HELP_MESSAGE"
fi

exit $RETURN_CODE
