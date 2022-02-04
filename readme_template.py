import sys

if len(sys.argv) > 3:
    print("You have specified too many arguments")
    sys.exit()

if len(sys.argv) < 3:
    print(
        "Missing arguements.\n usage: python readme_template.py [github_username] [repository_name]"
    )
    sys.exit()

github_username = sys.argv[1]
repo_name = sys.argv[2]

short_repo_url = f"https://github.com/{github_username}/{repo_name}"
repo_url = f"https://github.com/{github_username}/{repo_name}"
with open("README.md", "w") as f:
    f.write(
        f"""
<p align="center">
  <img src="product icon" />
</p>
<h1 align="center">{repo_name}</h1>
<h4 align="center">
1 Line Description.</h1>
<br>
<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0"> <img src="https://img.shields.io/github/license/{github_username}/{repo_name}"> <img src="https://img.shields.io/tokei/lines/github/{github_username}/{repo_name}?label=lines%20of%20code"> <img src="https://img.shields.io/github/languages/top/{github_username}/{repo_name}">
  <img src="https://img.shields.io/github/repo-size/{github_username}/{repo_name}">
</p>
<br>

![Doing something cool through my software. Check it out!](A cool gif here)

3 Line Description

**Note**: Bugs or early-project related notes.
<br>

# :zap: Installation

Any steps you need to run before installation or important notes.
<br>

## Build From Source
Prerequisites: **Git**, **Language Dependencies**

1. Clone the github repository using the Github CLI.
```sh
git clone {repo_url}
```

2. Change to the project directory.
```sh
cd repo_name
```

3. Installation commands
```sh
```

5. What you can do to verify successful installation.
<br>

## :test_tube: Testing

First, make sure you [**Build From Source**](link to build from source tag).

Run this command to run the tests for electric
```sh
command you can use to run project tests.
```
<br>

## :clap: Supporters
[![Stargazers repo roster for {short_repo_url}](https://reporoster.com/stars/{github_username}/{repo_name})](https://github.com/{short_repo_url}/stargazers)

[![Forkers repo roster for {short_repo_url}](https://reporoster.com/forks/{github_username}/{repo_name})](https://github.com/{short_repo_url}/network/members)

<br>

## :hammer: Build Status
## :hammer: Build Status
| Feature                            | Build Status   |
|------------------------------------|----------------|
| Installation                       | ‚úÖ             |
| Portable Installation              | ‚úÖ             |
| Uninstallation                     | ‚úÖ             |
| Update                             | ‚úÖ             |
| Show                               | ‚úÖ             |
| List                               | ‚úÖ             |
| Search                             | ‚úÖ             |
| Code Editor Extension Installation | ‚úÖ             |
| Python Package Installation        | ‚úÖ             |
| NodeJS Package Installation        | ‚úÖ             |
| Configuration Management           | ‚úÖ             |
| Cleanup                            | ‚úÖ             |
| Tab Completion                     | ‚úÖ             |

<br>

## Authors
[{github_username}](https://github.com/{github_username}) - Role in the project.

See also the list of [contributors](https://github.com/{repo_name}/contributors) who contributed to this.

Special thanks to:
[SomeUser](https://www.github.com/linktotheirgithub) what they did.

## Built With
* [Name Of Technology](Link to Homepage)
* [Name of library](Link to library)

## Versioning

We use [type of versioning](details about the versioning with a link) for versioning. For the versions available, see the [tags on this repository](https://github.com/{repo_name}/tags). 

## License

This project is licensed under yourlicense - see the [LICENSE.md](LICENSE) file for details.
"""
    )
