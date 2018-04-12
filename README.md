# Weekly
Automate weekly work.

# Documentation

Publish the [document](http://weekly.readthedocs.io/en/feature-docs/) onto [readthedoc](https://readthedocs.org/).

# Requirement
1. Python3

# Inclusion
1. Attendee List
2. Announcement
3. Mail
4. Downloader

# Attendee list
The identification is retrieved from Student ID cards by NFC reader and it associates with built-in calendar.

# Announcement
Event register and timeline to announce are covered in this mechanism.

# Mail
It's implemented via gmail with smtp protocol.

# Downloader
A download mechanism for various source. Moreover, It supports Google Drive.

# Unittest
Execute all the test suites via:
```shell=
make check
```
Execute particular test suites via:
```shell=
make XXX_test XXX_test ...
```

# Coding Style
Please follow [PEP8](https://www.python.org/dev/peps/pep-0008/).

# Autotools
Statistic for violenting PEP8:
`make pep8stat`
Print the diff for the fixed sources:
`make pep8diff`
Discipline sources to follow PEP8:
`make pep8replace`

# Contribution
Contributing is welcome, please use GitHub issue and Pull Request to contribute!
Notice that you should follow the `coding style` and send PR to `dev/master branch`.

# For all administrators
Forbid to force push on `master` and `dev/master` branch. Commit messages is such a 
treasure for each project on Github. One of risks of force push is to rearrange all 
commit messages if you use `git rebase`. It's possible to remove the merge notification
message. We could retrieve lots of information from that kind of messages including 
the number of PR merged and branch name for briefly introducing what this PR for.
