#!/usr/bin/env bash
set -e

OPENAPI_GENERATOR_VERSION=7.18.0
OPENAPI_JSON=openapi.json
OPENAPI_CLIENT_DIR=GENERATED_API
ASYNC_LIB="asyncio"

# Detect flavor
sed --version >/dev/null 2>&1 && SED_FLAVOR="GNU" || SED_FLAVOR="BSD"

# Set flags based on flavor
if [[ "$SED_FLAVOR" == "BSD" ]]; then
	SED_FLAGS=(-i '')
else
	SED_FLAGS=(-i)
fi

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

	sed "${SED_FLAGS[@]}" "s/packageVersion: \"$current_version\"/packageVersion: \"$new_version\"/" "$PYTHON_GENERATOR_YAML"

	echo "SDK Version bumped to $new_version"
}

pre_generation_process() {
	clean
	get_openapi_spec
	bump_patch
}

# Post-Generation Steps #######################################################

# Update the project license
update_license() {
	local PYPROJECT_TOML="./pyproject.toml"

	if [[ ! -f "$PYPROJECT_TOML" ]]; then
		echo "Error: File '$PYPROJECT_TOML' does not exist."
		return 1
	fi

	sed "${SED_FLAGS[@]}" 's/^license = .*/license = "Apache-2.0"/' "$PYPROJECT_TOML"

	echo "Updated license in pyproject.toml to Apache-2.0"
}

# Remove unused dependencies
remove_dependencies() {

	if poetry remove --group=dev tox >/dev/null 2>&1; then
		echo "removing tox dependencies"
	else
		echo "skipping tox"
	fi
}

# Fix the setupfiles
fix_setupfiles() {
    local LIBRARY=$1
    local TARGET_FILE="setup.py"
	local PYPROJECT_FILE="vulncheck_sdk/aio/pyproject.toml"

    if [[ ! -f "$TARGET_FILE" ]]; then
        echo "Error: $TARGET_FILE not found."
        return 1
    fi

    if [[ ! -f "$PYPROJECT_FILE" ]]; then
        echo "Warning: $PYPROJECT_FILE not found. Using defaults."
        AIOHTTP_VERSION="3.13.2"
        AIOHTTPRETRY_VERSION="2.9.1"
        return
    fi

    # Extract versions: 
    AIOHTTP_VERSION=$(grep "aiohttp " "$PYPROJECT_FILE" | sed -E 's/.*>=([^")]+).*/\1/')
    AIOHTTPRETRY_VERSION=$(grep "aiohttp-retry" "$PYPROJECT_FILE" | sed -E 's/.*>=([^")]+).*/\1/')

    echo "--- Updating dependencies for: $LIBRARY ---"

    case "$LIBRARY" in
        "asyncio")
            # Update package managers
            poetry add "aiohttp>=$AIOHTTP_VERSION" "aiohttp_retry>=$AIOHTTPRETRY_VERSION"
            echo "aiohttp>=$AIOHTTP_VERSION" >> requirements.txt
            echo "aiohttp_retry>=$AIOHTTPRETRY_VERSION" >> requirements.txt

            # Update setup.py
            if [[ "$SED_FLAVOR" == "GNU" ]]; then
                sed "${SED_FLAGS[@]}" "/REQUIRES = \[/a \    \"aiohttp >= $AIOHTTP_VERSION\"," "$TARGET_FILE"
                sed "${SED_FLAGS[@]}" "/REQUIRES = \[/a \    \"aiohttp_retry >= $AIOHTTPRETRY_VERSION\"," "$TARGET_FILE"
            else
                # BSD sed is very picky about the newline after 'a\'
                sed "${SED_FLAGS[@]}" "/REQUIRES = \[/a\\
    \"aiohttp >= $AIOHTTP_VERSION\"," "$TARGET_FILE"
                sed "${SED_FLAGS[@]}" "/REQUIRES = \[/a\\
    \"aiohttp_retry >= $AIOHTTPRETRY_VERSION\"," "$TARGET_FILE"
            fi
            ;;
        *)
            echo "Error: Unsupported library '$LIBRARY'. Use 'asyncio'."
            return 1
            ;;
    esac

	rm -rf vulncheck_sdk/aio/pyproject.toml
}

generate_readme() {
	echo "Hydrating README.template"
	cog -d -o README.md ./README.template
}

post_generation_process() {
	local LIBRARY=$1
	post_build_cleanup
	generate_readme
	update_license
	remove_dependencies
	fix_setupfiles "$LIBRARY"
}

# Generation ##################################################################

generate_sdk() {
	# Variable Verification
	if [[ -z "$OPENAPI_JSON" || -z "$OPENAPI_GENERATOR_VERSION" ]]; then
		echo "Error: Ensure OPENAPI_JSON, and OPENAPI_GENERATOR_VERSION are set."
		return 1
	fi

	local PACKAGE_NAME="vulncheck_sdk"
	local SYNC_LIB="urllib3"

	echo "--- Generating Sync Client (Default) ---"
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
		-o /local/"$OPENAPI_CLIENT_DIR" \
		--additional-properties=packageName=$PACKAGE_NAME,library=$SYNC_LIB,extraDependencies="httpx >= 0.24.0;urllib3 >=2.1.0"

	echo "--- Generating Async Client Namespace ---"
	# generate directly into the aio subfolder.
	# packageName is set to .aio to fix internal relative imports.
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
		-o /local/"$OPENAPI_CLIENT_DIR/$PACKAGE_NAME/aio" \
		--additional-properties=packageName=$PACKAGE_NAME.aio,library=$ASYNC_LIB,extraDependencies="httpx >= 0.24.0;urllib3 >=2.1.0"

	echo "--- Cleaning up and flattening Async structure ---"
	local AIO_PATH="$OPENAPI_CLIENT_DIR/$PACKAGE_NAME/aio"
	local NESTED_CODE_PATH="$AIO_PATH/$PACKAGE_NAME/aio"

	rm -rf "$AIO_PATH/api" "$AIO_PATH/models" "$AIO_PATH/docs"

	if [ -d "$NESTED_CODE_PATH" ]; then
		mv "$NESTED_CODE_PATH/"* "$AIO_PATH/"
	fi

	echo "--- moving tests ---"
	mv "$AIO_PATH/test" "$AIO_PATH/aiotest"

	echo "Success: SDK generated"
}

# Helpers #####################################################################

post_build_cleanup() {
	echo "--- post build cleanup ---"
	rm -rf test
	mkdir test
	mv $OPENAPI_CLIENT_DIR/test test/blocking
	mv $OPENAPI_CLIENT_DIR/vulncheck_sdk/aio/aiotest test/aio
	mv $OPENAPI_CLIENT_DIR/* .

	rm -rf $OPENAPI_CLIENT_DIR

	rm -rf git_push.sh
	rm -rf vulncheck_sdk.egg-info
	rm -rf vulncheck_sdk/aio/requirements.txt vulncheck_sdk/aio/setup.py vulncheck_sdk/aio/setup.cfg poetry.lock
	rm -rf vulncheck_sdk/aio/.github vulncheck_sdk/aio/.gitignore vulncheck_sdk/aio/.gitlab-ci.yml vulncheck_sdk/aio/.openapi-generator
	rm -rf vulncheck_sdk/aio/.openapi-generator-ignore vulncheck_sdk/aio/.travis.yml vulncheck_sdk/aio/README.md vulncheck_sdk/aio/git_push.sh
	rm -rf vulncheck_sdk/aio/tox.ini vulncheck_sdk/aio/test-requirements.txt
	rm -rf vulncheck_sdk/aio/vulncheck_sdk tox.ini
}

check_git_status() {
    # Define the paths we care about
    local WATCHED_PATHS="vulncheck_sdk/ pyproject.toml"

    # Check if there are any changes in the specific paths
    if [ -n "$(git --no-pager status --porcelain $WATCHED_PATHS)" ]; then
        echo "Changes detected in core SDK or pyproject.toml!"
        
        echo "::group::Stats"
        git --no-pager diff --stat $WATCHED_PATHS
        echo "::endGroup::"
        
        echo "::group::Full Diff"
        git --no-pager diff $WATCHED_PATHS
        echo "::endGroup::"
    else
        echo "No relevant changes detected in: $WATCHED_PATHS. Exiting."
        exit 0
    fi
}

# Main #########################################################################

main() {
	# First we'll check if there are new changes, by skipping the bump_patch step
	# (otherwise check_git_status would always see a new change, i.e. the version)
	echo "::group::Clean"
	clean
	echo "::endGroup::"

	echo "::group::Get openapi spec"
	get_openapi_spec
	echo "::endGroup::"

	echo "::group::Generate SDK"
	generate_sdk
	echo "::endGroup::"

	echo "::group::Post Generate Process"
	post_generation_process $ASYNC_LIB
	echo "::endGroup::"

	echo "::group::Check Git Status"
	check_git_status # If there's no new changes, we exit here
	echo "::endGroup::"
	# If there's new changes, let's bump the version and prepare for a new PR

	echo "::group::Changed Detected Pre Generate Process"
	pre_generation_process
	echo "::endGroup::"

	echo "::group::Changes Detected Generate SDK"
	generate_sdk
	echo "::endGroup::"

	echo "::group::Changes Detected Post Generate Process"
	post_generation_process $ASYNC_LIB
	echo "::endGroup::"

	echo "Done"
}

main
