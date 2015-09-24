
# Code to repeat the results

Steps to take

    00 data_download
    01 data prepare
    02 data split fold
    03 feature extract
    04 feature processing
    05 feature discovery ...  find 
       feature selection
    06 classifier train
    07 classifier test  -optimize
    08 evaluate model
    09 docs plot results
    10 docs report

   + publish ... in Figshare, 

 see [Kaggle - GettingStartedWithPythonForDataScience](https://www.kaggle.com/wiki/GettingStartedWithPythonForDataScience)


, fold – also known variously as reduce, accumulate, aggregate, compress, or inject – refers to a family of higher-order functions that analyze a recursive data structure and through use of a given combining operation, recombine the results of recursively processing its constituent parts, building up a return value.
https://en.wikipedia.org/wiki/Cross-validation_(statistics)

## Links

Try starting the project using the [python_boilerplate template.](https://pypi.python.org/pypi/python_boilerplate_template)

A sample project that exists for [PyPUG's "Tutorial on Packaging and Distributing Projects"](https://github.com/pypa/sampleproject)

Pattern for Python=
http://libraries.universityofcalifornia.edu/groups/files/about/desmedt12a.pdf
http://www.clips.ua.ac.be/pages/pattern.

https://github.com/ajschumacher/gadsdc
    https://github.com/jseabold/538model

https://github.com/ajschumacher/gadsdc/tree/master/06-python
https://github.com/ajschumacher/gadsdc/tree/master/07-python_viz

### Repeatable Research in Python

!!
http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/


https://github.com/reproducible-research/scipy-tutorial-2014
Emacs + org-mode + python in reproducible research; SciPy 2013 
    https://www.youtube.com/watch?v=1-dUkyn_fZA
    https://github.com/jkitchin/scipy2013

https://www.sitepen.com/blog/2008/06/05/easy-repeatable-buildingdeployment-of-pythondojo-projects/

split/fold 10 -> 10 file list files
train repeat 

http://www.cs.utexas.edu/~mooney/cs391L/project-topics.html


python bootstrap.py


http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application

In particular:
1.Where do you put the source?
2.Where do you put application startup scripts?
3.Where do you put the IDE project cruft?
4.Where do you put the unit/acceptance tests?
5.Where do you put non-Python data such as config files?
6.Where do you put non-Python sources such as C++ for pyd/so binary extension modules?


•/scripts or /bin for that kind of command-line interface stuff
•/tests for your tests
•/lib for your C-language libraries
•/doc for most documentation
•/apidoc for the Epydoc-generated API docs.


 

Doesn't too much matter. Whatever makes you happy will work. There aren't a lot of silly rules because Python projects can be simple.
•/scripts or /bin for that kind of command-line interface stuff
•/tests for your tests
•/lib for your C-language libraries
•/doc for most documentation
•/apidoc for the Epydoc-generated API docs.

And the top-level directory can contain README's, Config's and whatnot.

The hard choice is whether or not to use a /src tree. Python doesn't have a distinction between /src, /lib, and /bin like Java or C has.

Since a top-level /src directory is seen by some as meaningless, your top-level directory can be the top-level architecture of your application.
•/foo
•/bar
•/baz

I recommend putting all of this under the "name-of-my-product" directory. So, if you're writing an application named quux, the directory that contains all this stuff is named /quux.

Another project's PYTHONPATH, then, can include /path/to/quux/foo to reuse the QUUX.foo module. 
 


In my case, since I use Komodo Edit, my IDE cuft is a single .KPF file. I actually put that in the top-level /quux directory, and omit adding it to SVN.


According to [Jean-Paul Calderone's Filesystem structure of a Python project:](http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html)

Project/
|-- bin/
|   |-- project
|
|-- project/
|   |-- test/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |   
|   |-- __init__.py
|   |-- main.py
|
|-- setup.py
|-- README


You install the package! (pip install -e /path/to/Project) 

Check out [Open Sourcing a Python Project the Right Way.](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)

$ tree
.
|- LICENSE
|- README.md
|- TODO.md
|- docs
|   |-- conf.py
|   |-- generated
|   |-- index.rst
|   |-- installation.rst
|   |-- modules.rst
|   |-- quickstart.rst
|   |-- sandman.rst
|- requirements.txt
|- sandman
|   |-- __init__.py
|   |-- exception.py
|   |-- model.py
|   |-- sandman.py
|   |-- test
|       |-- models.py
|       |-- test_sandman.py
|- setup.py


----------
paster create -t python_boilerplate <project_name>

project_name>/
  |
  +-- .gitignore           # Git configuration
  +-- .travis.yml          # Travis-CI configuration
  +-- bootstrap.py         # Buildout bootstrap-script
  +-- buildout.cfg         # Buildout project configuration
  +-- setup.cfg            # Configuration for py.test and other tools
  +-- README.md            # Information on how to use the project
  +-- src/                 # Directory for keeping (possible multiple) project eggs
      |
      +- <egg_name>/       # First egg of the project
         |
         +-- package/      # Python source files
         +-- tests/        # Tests
         +-- .gitignore    # Git configuration
         +-- .travis.yml   # Travis-CI configuration
         +-- setup.cfg     # Configuration for py.test and other tools
         +-- setup.py      # Package metadata
         +-- MANIFEST.in   # Files to include in the package
         +-- README.rst    # Package description
         +-- LICENSE.txt   # License
         +-- CHANGELOG.txt # Changelog



------------

import urllib
import json

destination_file = '/tmp/myimage.jpg'

figshare_id = '1066744'

figshare_url = "http://api.figshare.com/v1/articles/%s" % figshare_id
jsonresponse = urllib.urlopen(figshare_url)
article_info = json.load(jsonresponse)
image_download_url = article_info['items'][0]['files'][0]['download_url']
urllib.urlretrieve(image_download_url, destination_file)
ls  -l    /tmp/myimage.jpg



-------
from sound.effects import echo
...
echo.EchoFilter(input, output, delay=0.7, atten=4)



https://www.youtube.com/watch?v=X47SGnTMZIU
  http://nycdatascience.com/data-science-bootcamp/
    Linear Logistic Regression
    kNN
    Tree based 
        decision trees
        random forest
        Gradient Boost Machine  https://github.com/dmlc/xgboost
    Neural Networks



dmlc-core  A common code-base for Distributed Machine Learning in C++ 
    https://github.com/dmlc/dmlc-core/blob/master/src/data.cc
