#!/usr/bin/env bash

set -e

section "Script section"

export NX_SOURCE=$PWD
export NX_INSTALL=$(pip show cynetworkx | grep Location | awk '{print $2"/cynetworkx"}')

# nose 1.3.0 does not tell coverage to only cover the requested
# package (except during the report).  So to restrict coverage, we must
# inform coverage through the .coveragerc file.
cp .coveragerc $NX_INSTALL
cp setup.cfg $NX_INSTALL

# Move to new directory so that cynetworkx is not imported from repository.
# Why? Because we want the tests to make sure that cyNetworkX was installed
# correctly. Example: setup.py might not have included some submodules.
# Testing from the git repository cannot catch a mistake like that.
#
# Export current directory for logs.
cd $NX_INSTALL
printenv PWD

# Run nosetests.
if [[ "${REPORT_COVERAGE}" == 1 ]]; then
  nosetests --verbosity=2 --with-ignore-docstrings --with-coverage --cover-package=cynetworkx
  cp -a .coverage $NX_SOURCE
else
  nosetests --verbosity=2 --with-ignore-docstrings
fi

cd $NX_SOURCE

section_end "Script section"

set +e
