#!/usr/bin/env python
import os
import sys
import subprocess
import shutil

pwd = os.path.abspath(os.path.dirname(__file__))
vedir = os.path.abspath(os.path.join(pwd, "ve"))
templatetests = os.path.abspath(os.path.join(pwd, "run_template_tests.sh"))

if os.path.exists(vedir):
    shutil.rmtree(vedir)

if os.path.exists(templatetests):
    os.remove(templatetests)

virtualenv_support_dir = os.path.abspath(
    os.path.join(
        pwd, "requirements", "virtualenv_support"))

ret = subprocess.call(["python", "virtualenv.py",
                       "--extra-search-dir=%s" % virtualenv_support_dir,
                       "--never-download",
                       vedir])
if ret:
    exit(ret)

ret = subprocess.call(
    [os.path.join(vedir, 'bin', 'pip'), "install",
     "--use-wheel",
     "--no-deps",
     "--index-url=https://pypi.ccnmtl.columbia.edu/",
     "--requirement", os.path.join(pwd, "requirements.txt")])

if ret:
    exit(ret)

ret = subprocess.call(["python", "virtualenv.py", "--relocatable", vedir])
# --relocatable always complains about activate.csh, which we don't really
# care about. but it means we need to ignore its error messages
