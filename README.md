# List Files Action
[![StepSecurity Maintained Action](https://raw.githubusercontent.com/step-security/maintained-actions-assets/main/assets/maintained-action-banner.png)](https://docs.stepsecurity.io/actions/stepsecurity-maintained-actions)

<p align="center">

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/step-security/list-files-action?label=latest-release)](https://github.com/step-security/list-files-action/releases/latest)

[![Test](https://github.com/step-security/list-files-action/actions/workflows/test.yml/badge.svg)](https://github.com/step-security/list-files-action/actions/workflows/test.yml)

</p>
GitHub action to list path of all files of a particular extension in the folder/directory
specified by the user.

## Inputs
| Input                                    | Description                           |
|------------------------------------------|---------------------------------------|
| `repo` (required)                        | Repository name where to search files |
| `ref`  (optional => default is 'master') | Branch or tag to checkout             |
| `path` (required)                        | Path where searching files            |
| `ext`  (required)                        | File extension to match               |

## Outputs

| Output       | Description                               |
|--------------|-------------------------------------------|
| `paths`      | Paths of all the files with the extension |

## Usage example

```yaml
name: Test

on:
  push:
    tags-ignore:
      - '*'
    branches:
      - 'main'
  pull_request:
  workflow_dispatch:

jobs:
  list-files:
    runs-on: ubuntu-latest
    outputs:
      paths: ${{ steps.list-files.outputs.paths }}
    steps:
      - name: List Files
        id: list-files
        uses: step-security/list-files-action@v3
        with:
          repo: ${{ github.repository }}
          ref: ${{ github.ref }}
          path: "."
          ext: ".yml"
  Test:
    needs: list-files
    strategy:
      matrix:
        paths: ${{ fromJson(needs.list-files.outputs.paths) }}
    runs-on: ubuntu-latest
    steps:
      - name: Output results
        run: |
          echo ${{ matrix.paths }}
```
Output generated for the above yaml file (in this repository):

```shell
github/workflows/test.yml
action.yml
```

## License
[MIT license]

[MIT license]: LICENSE