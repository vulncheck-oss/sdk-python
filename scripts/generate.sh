#!/usr/bin/env bash
set -e

OPENAPI_GENERATOR_VERSION=7.14.0
OPENAPI_JSON=openapi.json

# Pre-Generation Steps ########################################################

clean() {
  rm $OPENAPI_JSON || true
  rm -rf vulncheck_sdk/ dist/ docs/ test/ vulncheck_sdk_README.md || true
}

get_openapi_spec() {
  curl --request GET \
    --url https://api.vulncheck.com/v3/openapi \
    --verbose \
    --header "Accept: application/json" >$OPENAPI_JSON
}

bump_patch() {
  PYTHON_GENERATOR_YAML=./python-generator-config.yaml

  current_version=$(grep "packageVersion" "$PYTHON_GENERATOR_YAML" | awk -F': ' '{print $2}' | tr -d '"')
  IFS='.' read -r major minor patch <<<"$current_version"
  patch=$((patch + 1))
  new_version="${major}.${minor}.${patch}"

  sed -i "s/packageVersion: \"$current_version\"/packageVersion: \"$new_version\"/" "$PYTHON_GENERATOR_YAML"

  echo "SDK Version bumped to $new_version"
}

pre_generation_process() {
  clean
  get_openapi_spec
  bump_patch
}

# Post-Generation Steps #######################################################

# Revert readme
revert_readme() {
  mv README.md vulncheck_sdk_README.md
  git checkout -- README.md
}

# Update the project license
update_license() {
  PYPROJECT_TOML=./pyproject.toml
  if [[ ! -f "$PYPROJECT_TOML" ]]; then
    echo "File '$PYPROJECT_TOML' does not exist."
    exit 1
  fi
  sed -i 's/^\(license = \)"[^"]*"/\1"Apache-2.0"/' "$PYPROJECT_TOML"
  echo "Updated license in pyproject.toml"
}

# Remove unused dependencies
remove_dependencies() {
  poetry remove --group=dev tox
  echo "Removed tox from dev dependencies"
}

post_generation_process() {
  revert_readme
  update_license
  remove_dependencies
}

# Generation ##################################################################

generate_sdk() {
  docker run \
    --rm \
    --user "$(id -u):$(id -g)" \
    -v "${PWD}":/local \
    openapitools/openapi-generator-cli:v$OPENAPI_GENERATOR_VERSION generate \
    -i /local/"$OPENAPI_JSON" \
    -g python \
    --git-user-id "vulncheck-oss" \
    --git-repo-id "sdk-python" \
    -c /local/python-generator-config.yaml \
    -o /local/"$OPENAPI_CLIENT_DIR"
}

# Helpers #####################################################################

check_git_status() {
  if [ -n "$(git status --porcelain)" ]; then
    echo "New API changes!"
  else
    echo "No changes detected."
    exit 0
  fi
}

# Main #########################################################################

main() {
  # First we'll check if there are new changes, by skipping the bump_patch step
  # (otherwise check_git_status would always see a new change, i.e. the version)
  clean
  get_openapi_spec
  generate_sdk
  post_generation_process
  check_git_status # If there's no new changes, we exit here
  # If there's new changes, let's bump the version and prepare for a new PR
  pre_generation_process
  generate_sdk
  post_generation_process
}

main
