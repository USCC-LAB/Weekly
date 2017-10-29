.. _intro

Welcome
*******

**Weekly** is a project which aims to automate all boring stuff in python script
without human involved. The primary scenario is about daily life of
graduated students in laboratory. Professor asks elder students to
do attendance list every week, and sending each member in laboratory mail
to inform recent matters and meeting records and so on. That's only
interesting for computers ;-)

This project is started by a misanthrope who found life is tough especially
in laboratory. All right. Let me change the aim of this project with higher
purpose. Make life easy(at least for me).

Here is also a training place for new members who access to our laboratory
(unfortunately :-( ). We request basic level of coding skills and commit
messages style. Don't be worry about that. Just send us a patch.
We don't bite :)

Documentation
=============

The current implementation is in pure python3.

(... work in progress)

Learn Python
============

Python
------

As I mentioned before, the primary implementation is in Python. So if you want to fix some bugs or work on new features,
you should grasp basic operation of python. Here is a tutorial, `The Python Tutorial <https://docs.python.org/3/tutorial/>`_,
written(mostly) by the author of the Python programming language, *Guido van Rossum*.

If you're a non-native English reader and familiar with Traditional Chinese. You could start it by
reading the slides or tutorials. As follows:

- Tutorials
    1. `Python 教學 <https://docs.python.org.tw/3/tutorial/>`_
    2. `Python tutorial - CodeData <http://www.codedata.com.tw/python/python-tutorial-the-1st-class-1-preface>`_
- Slides
    1. 《Python 3.5 技術手冊》投影片系列 `第 1 章 - Python 起步走 <https://www.slideshare.net/JustinSDK/python-65068620>`_

Despite all materials above, if you suggest others, please use **issues** or **PRs** to contribute.

Nevertheless, the way to practice Python is important. It's convenient to examine your assume via
`interactive shell of python interpreter <https://docs.python.org/2/tutorial/interpreter.html>`_.
However, in order to enhance efficiency, it's really powerful to use IPython and associate with Jupyter_ kernel as a note system which allows you execute python script commands in place. More details could be refered below.

.. _IPython
IPython
-------
    (... unfinished)

.. _Jupyter:
Jupyter
-------
    (... hang on the air)


Contributor Guide
=================

Sorry for my chatter. I have to present a guide like a teaching material for
variety of people.

Github and Git
--------------

There are three ways to contribute projects on Github. No one is beter, and
no one is worst. All of them are necessary for every open source project.
As following:

1. Post a message via `Issues <https://github.com/USCC-LAB/Weekly/issues>`_.
This feature, **Issues**, is similiar with other project's trackers. It's
useful to keep track of issues you focus on.
    - Bug report
    - Feature request
    - Ask questions
    - More details about **Issues**: `Mastering Issues <https://guides.github.com/features/issues/>`_
2. Submit a patch via `Pull Requests <https://github.com/USCC-LAB/Weekly/pulls>`_. The name of **"Pull Request"**
may confuse novices for a while. It's shorted for **Send a Pull Request**!
    - Fix bugs
    - Introduce new features
    - Refactor current implementation
    - Help documentation
    - Learn more about **Pull Request**: `About Pull Requests <https://help.github.com/articles/about-pull-requests/>`_
3. **Participate in discussion and give some feedbacks**.  The two ways I mentioned above, let you take part
in conversations and give your opinions.
    - Code review
    - Answer questions
    - Discuss the dis/advantages of features

Moreover, if you want to ask something, please note that asking a good questions is not as easy as you though.
There is a great material, `How To Ask Questions The Smart Way <http://www.catb.org/esr/faqs/smart-questions.html>`_,
for you to grasp key points of how to ask a question which might be more possible to get replies.
There is the Traditional Chinese translation, `提問的智慧  <https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way>`_.

In addition to asking questions, if you want to send PRs, writing clear and meaningful git commit messages are necessary.
Please refer to `How to Write a Git Commit Message <https://chris.beams.io/posts/git-commit/>`_. That's really helpful.
Thank *louis lu* for Traditional Chinese translation,
`如何寫一個 Git Commit Message <https://blog.louie.lu/2017/03/21/%E5%A6%82%E4%BD%95%E5%AF%AB%E4%B8%80%E5%80%8B-git-commit-message/>`_.


Coding style
============

Follow `PEP 8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_.

Moreover, there are some built-in tools to check coding style, analyse inconsistent terms with PEP8
and format Python code to comform to PEP8 in place.

By the way, we are pleasure to accept any features which could improve code quality.

Contact us
==========
- Current maintainer
    - Yen-Kuan Wu <yenwu.tw@gmail.com>
