#!/bin/bash

# Submit script for assignments
#
# BEFORE YOU RUN THIS: check assignment 0 for the invite link,
# which will create a private submission repo linked to your GitHub username.
#
# Usage: ./submit.sh -u my_github_username
#
# Options:
#   -f : force submit, overwrites target branch
#   -a <number> : specify assignment number

GITHUB_USERNAME="${USER}"
DEFAULT_ASSIGNMENT="0"
FORCE="false"
TARGET_BRANCH="master"

# Change to assignment dir
dir=$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
pushd $dir



function validate_assignment() {
  grep -F -q -x "$1" <<EOF
0
1
2
3
4
5
6
EOF
}

while getopts "u:a:f" opt; do
  case $opt in
    u)
      GITHUB_USERNAME="${OPTARG}"
      ;;
    a)
      ASSIGNMENT="${OPTARG}"
      validate_assignment "${ASSIGNMENT}" \
        || (echo "Invalid assignment number '$ASSIGNMENT'."; exit 1)
      ;;
    f)
      FORCE="true"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

set -e

###############################
# Verify assignment to submit #
###############################
if [[ -z "$ASSIGNMENT" ]]; then
  echo "No assignment number specified."
  echo "./submit.sh -a <assignment#>"
  exit
fi
TARGET_BRANCH="a${ASSIGNMENT}-submit"
echo "=== Submitting assignment ${ASSIGNMENT} ==="
echo "Note: this will submit your whole repository to branch '${TARGET_BRANCH}'"

#############################################
# Run anaswers_test.py for pre-submit tests #
#############################################
echo "=== Running presubmit tests ==="
pushd a$ASSIGNMENT
if ! python answers_test.py; then
  echo "== Warning! Presubmits failed.  Submit anyways?"
  select mode in "Yes" "No"; do
    case $mode in
      "Yes" ) break;;
      "No" ) exit;;
    esac
  done
fi
popd

#################################
# Check for uncommitted changes #
#################################
CHANGED=$(git diff-index --name-only HEAD --)
if [[ ! -z "$CHANGED" ]]; then
  echo "== Warning! You have uncommitted changes in this repository: =="
  git diff --stat
  echo "Commit before submitting? (submit.sh will only push commited changes)"
  select mode in "Yes" "No" "(cancel)"; do
    case $mode in
      "Yes" ) git commit -a; break;;
      "No" ) break;;
      "(cancel)" ) echo "Submit cancelled."; exit;;
    esac
  done
fi

###############################
# Select github access method #
###############################
REPO_NAME="datasci-w266/2022-fall-assignment-$GITHUB_USERNAME"
WEB_URL="https://github.com/$REPO_NAME/tree/${TARGET_BRANCH}"
echo "== Select GitHub access protocol =="
echo "HTTPS is default, but SSH may be needed if you use two-factor auth."
select mode in "HTTPS" "SSH" "(cancel)"; do
  case $mode in
    "HTTPS" ) REMOTE_URL="https://github.com/$REPO_NAME.git"; break;;
    "SSH" ) REMOTE_URL="git@github.com:$REPO_NAME.git"; break;;
    "(cancel)" ) echo "Submit cancelled."; exit;;
  esac
done

###########################
# Set up git remote alias #
###########################
REMOTE_ALIAS="2022-fall-assignment-submit"
echo "== Pushing to submission repo $REPO_NAME, branch '${TARGET_BRANCH}'"
echo "== Latest commit: $(git rev-parse HEAD)"
echo "== Check submission status at ${WEB_URL}"
if [[ $(git remote | grep "$REMOTE_ALIAS") ]]; then
  git remote -v remove "$REMOTE_ALIAS"
fi
git remote -v add "$REMOTE_ALIAS" "${REMOTE_URL}"
if [[ ${FORCE} == true ]]; then
  echo "Warning! Force-submit will overwrite remote history. Proceed?"
  select mode in "Force submit" "(cancel)"; do
    case $mode in
      "Force submit" ) echo "Proceeding with submission!"; break;;
      "(cancel)"  ) echo "Submit cancelled."; exit;;
    esac
  done
  git push "$REMOTE_ALIAS" "+HEAD:${TARGET_BRANCH}"
else
  git push "$REMOTE_ALIAS" "HEAD:${TARGET_BRANCH}"
fi

###############################
# Verify submission succeeded #
###############################
echo "=== Verifying submission ==="
git fetch "$REMOTE_ALIAS"
if [[ $(git rev-parse HEAD) == $(git ls-remote "$REMOTE_ALIAS" "${TARGET_BRANCH}" | cut -f1) ]]; then
  echo "=== Submission successful! ==="
  echo "You can view your submission at ${WEB_URL}"
else
  echo "=== ERROR: Submission failed. Manually push to $REPO_NAME:${TARGET_BRANCH}, or contact the course staff for help."
  echo "=== Alternatively, re-run this script in force-mode:"
  echo "=== ./submit.sh -u your-github-username -f"
fi

echo "== As always, you are responsible for double checking that the assignment you want us to grade is in the a#-submit branch of your repo (this can probably be found at ${WEB_URL})."
