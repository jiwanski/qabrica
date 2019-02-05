# Is 'Codewars for testers' possible?

After playing with codewars.com for some time I noticed lack of similar resource for QA. So I built some basic testing assignments and inquired whether a QA-flavoured spinoff would be possible.

The conclusion is "no" and main reasons are:

- a typical Codewars problem is way easier to solve in online editor than testing solution
- some QA frameworks tend to involve boilerplate code
- validating a test would require a human code review, unlike predefined tests in Codewars
- complexity will increase with dependencies like unit test frameworks or BDD support
- clever few-liners are hardly possible (not a required feature, but highly educative)

However, there was some residue left after this failed inquiry. I named it QAbrica and put on GitHub - https://github.com/jiwanski/qabrica.

# What is QAbrica?

It is a flat collection of QA tasks and solutions. The assignments posted so far, five in total, were created when trying to envisage _Codewars for testers_.

## tasks

Current testing tasks are of two types:

1. trivial math problems, implemented as simple Python code
2. web tasks, best solved using Selenium

Due to my juniority, only few solutions are available and some might need refactoring. Current statuses are:

- **solved** (&#9745;), using Python with testing frameworks or Robot Framework or pure Python
- **irrelevant** (-), for example, non-BDD task won't require _behave_ or _lettuce_
- **not implemented** (x), like Robot Framework not supporting Gherkin data tables
- **waiting to be solved** (&#9744;)

| source | feature | task | Python | Robot Framework | Python + pytest | Python + unittest | Python + behave | Python + lettuce |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| web | scroll with execute script | count flags in eBay popup | &#9744; | &#9744; | &#9744; | &#9745; | - | - |
| Python | parameterization | harshad numbers | &#9744; | &#9744; | &#9745; | &#9744; | - | - |
| Python | BDD (scenario outline) | multiples of 3 and 5 | - | &#9745; | - | - | &#9745; | &#9744; |
| web | string with HTML entity | title with HTML entity | &#9745; | &#9745; | &#9745; | &#9744; | - | - |
| Python | BDD (data tables) | validate triangle | - | x | - | - | &#9744; | &#9745; |

## single task structure

A generic structure is more or less like this:

| path | feature | 
| --- | --- |
| task.md | task description |
| [robot] | Robot Framework solution |
| robot/docs.md | how to run test, sample output, notes |
| robot/test/solution.robot | actual Robot test |
| [python_selenium] | Python solution (no framework) |
| python_selenium/docs.md | how to run test, sample output, notes |
| python_selenium/test/solution.py | actual Python test |
| [python_pytest] | Python solution (pytest) |
| python_pytest/docs.md | how to run test, sample output, notes |
| python_pytest/test/conftest.py | pytest configuration script |
| python_pytest/test/test.py | actual test |
| python_pytest/test/pytest.ini | pytest INI file |

## typical workflow

| step | action | 
| --- | --- |
| examine problem | read **problem/**_task.md_ |
| examine chosen solution | read **problem/some solution/**_docs.md_ |
| run test | execute command from _docs.md_ |
| examine test code, refactor, etc. | analyze **problem/some solution/**_test_ |
| (optional) create own solution | develop test code and docs in **problem/**_my solution_ |



## what's next

Current structure is enough to populate with hundreds of examples and extend with other frameworks/languages.

Unfortunately, I am too busy finding a job now to guarantee steady growth of this collection, unless my next occupation is somehow related to introductory test automation.
