Last login: Tue Sep 11 14:33:35 on ttys001
cd%                                                                             ➜  ~ cd Program/tensorflow-project 
➜  tensorflow-project git:(master) ✗ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	deleted:    face/data/Aaron_Eckhart/Aaron_Eckhart_0001.jpg
	deleted:    face/data/Aaron_Guiel/Aaron_Guiel_0001.jpg
	deleted:    face/data/Aaron_Patterson/Aaron_Patterson_0001.jpg
	deleted:    face/data/Aaron_Peirsol/Aaron_Peirsol_0001.jpg
	deleted:    face/data/Aaron_Peirsol/Aaron_Peirsol_0002.jpg
	deleted:    face/data/Aaron_Peirsol/Aaron_Peirsol_0003.jpg
	deleted:    face/data/Aaron_Peirsol/Aaron_Peirsol_0004.jpg
	deleted:    face/data/Aaron_Pena/Aaron_Pena_0001.jpg
	deleted:    face/data/Aaron_Sorkin/Aaron_Sorkin_0001.jpg
	deleted:    face/data/Aaron_Sorkin/Aaron_Sorkin_0002.jpg
	deleted:    face/data/Aaron_Tippin/Aaron_Tippin_0001.jpg
	deleted:    face/data/Abba_Eban/Abba_Eban_0001.jpg

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    catdogs/__init__.py
	deleted:    catdogs/train.py
	deleted:    catdogs/utils.py
	deleted:    cifar10/README.md
	deleted:    cifar10/__init__.py
	deleted:    cifar10/base.py
	deleted:    cifar10/eval.py
	deleted:    cifar10/train.py
	deleted:    cifar10/train_test_split.py
	deleted:    face/load_data.py
	deleted:    face/prediction.py
	deleted:    face/resize.py
	deleted:    face/train.py
	deleted:    keras/example/cifar10_cnn.py
	deleted:    keras/example/mnist_cnn.py
	deleted:    keras/example/mnist_sample.py
	deleted:    mnist/data/2.png
	deleted:    mnist/new/__init__.py
	deleted:    mnist/new/mnist.py
	deleted:    mnist/old/__init__.py
	deleted:    mnist/old/base.py
	deleted:    mnist/old/test.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	ANIMALS/
	CIFAR/
	MNIST/mnist/
	keras/cifar10_cnn.py
	keras/mnist_cnn.py
	keras/mnist_sample.py

➜  tensorflow-project git:(master) ✗ git add --A
error: unknown option `A'
usage: git add [<options>] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose

    -i, --interactive     interactive picking
    -p, --patch           select hunks interactively
    -e, --edit            edit current diff and apply
    -f, --force           allow adding otherwise ignored files
    -u, --update          update tracked files
    -N, --intent-to-add   record only the fact that the path will be added later
    -A, --all             add changes from all tracked and untracked files
    --ignore-removal      ignore paths removed in the working tree (same as --no-all)
    --refresh             don't add, only refresh the index
    --ignore-errors       just skip files which cannot be added because of errors
    --ignore-missing      check if - even missing - files are ignored in dry run
    --chmod <(+/-)x>      override the executable bit of the listed files

➜  tensorflow-project git:(master) ✗ git add -A 
➜  tensorflow-project git:(master) ✗ git commit -m "Change all file structures to increase the number of papers"
[master 3eae6de] Change all file structures to increase the number of papers
 34 files changed, 733 deletions(-)
 rename {catdogs => ANIMALS/catdogs}/train.py (100%)
 rename {catdogs => ANIMALS/catdogs}/utils.py (100%)
 rename {cifar10 => CIFAR/cifar10}/README.md (100%)
 rename {cifar10 => CIFAR/cifar10}/base.py (100%)
 rename {cifar10 => CIFAR/cifar10}/eval.py (100%)
 rename {cifar10 => CIFAR/cifar10}/train.py (100%)
 rename {cifar10 => CIFAR/cifar10}/train_test_split.py (100%)
 rename {mnist => MNIST/mnist}/new/mnist.py (100%)
 rename {mnist/data => MNIST/mnist/test}/2.png (100%)
 delete mode 100644 catdogs/__init__.py
 delete mode 100644 cifar10/__init__.py
 delete mode 100644 face/data/Aaron_Eckhart/Aaron_Eckhart_0001.jpg
 delete mode 100644 face/data/Aaron_Guiel/Aaron_Guiel_0001.jpg
 delete mode 100644 face/data/Aaron_Patterson/Aaron_Patterson_0001.jpg
 delete mode 100644 face/data/Aaron_Peirsol/Aaron_Peirsol_0001.jpg
 delete mode 100644 face/data/Aaron_Peirsol/Aaron_Peirsol_0002.jpg
 delete mode 100644 face/data/Aaron_Peirsol/Aaron_Peirsol_0003.jpg
 delete mode 100644 face/data/Aaron_Peirsol/Aaron_Peirsol_0004.jpg
 delete mode 100644 face/data/Aaron_Pena/Aaron_Pena_0001.jpg
 delete mode 100644 face/data/Aaron_Sorkin/Aaron_Sorkin_0001.jpg
 delete mode 100644 face/data/Aaron_Sorkin/Aaron_Sorkin_0002.jpg
 delete mode 100644 face/data/Aaron_Tippin/Aaron_Tippin_0001.jpg
 delete mode 100644 face/data/Abba_Eban/Abba_Eban_0001.jpg
 delete mode 100644 face/load_data.py
 delete mode 100644 face/prediction.py
 delete mode 100644 face/resize.py
 delete mode 100644 face/train.py
 rename keras/{example => }/cifar10_cnn.py (100%)
 rename keras/{example => }/mnist_cnn.py (100%)
 rename keras/{example => }/mnist_sample.py (100%)
 delete mode 100644 mnist/new/__init__.py
 delete mode 100644 mnist/old/__init__.py
 delete mode 100644 mnist/old/base.py
 delete mode 100644 mnist/old/test.py
➜  tensorflow-project git:(master) git push origin master 
Counting objects: 211, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (189/189), done.
Writing objects: 100% (211/211), 197.77 KiB | 6.82 MiB/s, done.
Total 211 (delta 88), reused 5 (delta 3)
remote: Resolving deltas: 100% (88/88), completed with 4 local objects.
To https://github.com/shiyipaisizuo/tensorflow-project.git
 ! [remote rejected] master -> master (permission denied)
error: failed to push some refs to 'https://github.com/shiyipaisizuo/tensorflow-project.git'
➜  tensorflow-project git:(master) git remote rm origin 
➜  tensorflow-project git:(master) git remote add origin https://github.com/lornatang/tensorflow-project.git
➜  tensorflow-project git:(master) git push origin master 
Counting objects: 9, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (9/9), 983 bytes | 983.00 KiB/s, done.
Total 9 (delta 0), reused 0 (delta 0)
To https://github.com/lornatang/tensorflow-project.git
   0cf5d4b..3eae6de  master -> master
➜  tensorflow-project git:(master) conda update --all
Solving environment: done

## Package Plan ##

  environment location: /anaconda3


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    zope-1.0                   |           py36_1           3 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyterlab_launcher-0.13.1 |           py36_0          36 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    beautifulsoup4-4.6.3       |           py36_0         139 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libsodium-1.0.16           |       h3efe00b_0         324 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    contextlib2-0.5.5          |   py36hd66e5e7_0          15 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sqlite-3.24.0              |       ha441bb4_0         2.2 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    click-6.7                  |   py36hec950be_0         104 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mpmath-1.0.0               |           py36_2         893 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    attrs-18.2.0               |   py36h28b3542_0          50 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipywidgets-7.4.1           |           py36_0         148 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libgfortran-3.0.1          |       h93005f0_2         495 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    flask-cors-3.0.6           |           py36_0          20 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyodbc-4.0.24              |   py36h0a44026_0          60 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sqlalchemy-1.2.11          |   py36h1de35cc_0         1.6 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ruamel_yaml-0.15.46        |   py36h1de35cc_0         228 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    dask-0.19.1                |           py36_0           3 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numba-0.39.0               |   py36h6440ff4_0         2.4 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlsxwriter-1.1.0           |           py36_0         210 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    expat-2.2.6                |       h0a44026_0         129 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytz-2018.5                |           py36_0         231 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cloudpickle-0.5.5          |           py36_0          26 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    dbus-1.13.2                |       h760590f_1         540 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nbconvert-5.3.1            |           py36_0         405 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    backports-1.0              |           py36_1           4 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    h5py-2.8.0                 |   py36h878fce3_3         913 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qtawesome-0.4.4            |   py36h468c6fb_0         159 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    appscript-1.0.1            |   py36h1de35cc_1         129 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl-service-1.1.2          |   py36h6b9c3cc_4          10 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nltk-3.3.0                 |           py36_0         2.0 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    kiwisolver-1.0.1           |   py36h0a44026_0          56 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    typing-3.6.4               |           py36_0          44 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gettext-0.19.8.1           |       h15daf44_3         3.4 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    heapdict-1.0.0             |           py36_2           7 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    parso-0.3.1                |           py36_0         114 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    wrapt-1.10.11              |   py36h1de35cc_2          41 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl_fft-1.0.4              |   py36h5d10147_1         137 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pickleshare-0.7.4          |   py36hf512f8e_0          12 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bottleneck-1.2.1           |   py36h1d22016_1         113 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    traitlets-4.3.2            |   py36h65bd3ce_0         131 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libssh2-1.8.0              |       h322a93b_4         218 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    atomicwrites-1.2.1         |           py36_0          11 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    snappy-1.1.7               |       he62c110_3          40 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    conda-build-3.14.2         |           py36_0         463 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyflakes-2.0.0             |           py36_0          87 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    itsdangerous-0.24          |           py36_1          21 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nose-1.3.7                 |           py36_2         214 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pywavelets-1.0.0           |   py36h1d22016_0         4.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyasn1-0.4.4               |   py36h28b3542_0         101 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    webencodings-0.5.1         |           py36_1          19 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter-1.0.0              |           py36_4           5 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    markupsafe-1.0             |   py36h1de35cc_1          23 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libxslt-1.1.32             |       hb819dd2_0         491 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    idna-2.7                   |           py36_0         132 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter_console-5.2.0      |           py36_1          36 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-arraydiff-0.2       |   py36h39e3cac_0          14 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python-3.6.6               |       hc167b69_0        15.4 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    multipledispatch-0.6.0     |           py36_0          21 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    anaconda-client-1.7.2      |           py36_0         141 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-doctestplus-0.1.3   |           py36_0          19 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    et_xmlfile-1.0.1           |   py36h1315bdc_0          20 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    appnope-0.1.0              |   py36hf537a9a_0           8 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    imagesize-1.1.0            |           py36_0           9 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pluggy-0.7.1               |   py36h28b3542_0          25 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipython-6.5.0              |           py36_0         1.0 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    spyder-3.3.1               |           py36_1         2.6 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libpng-1.6.34              |       he12f830_0         319 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    keyring-13.2.1             |           py36_0          46 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libedit-3.1.20170329       |       hb402a30_2         154 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    conda-env-2.6.0            |                1           3 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    filelock-3.0.6             |           py36_0          12 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    urllib3-1.23               |           py36_0         152 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    wcwidth-0.1.7              |   py36h8c6ec74_0          25 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl-2018.0.3               |                1       149.2 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bitarray-0.8.3             |   py36h1de35cc_0          54 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sympy-1.2                  |           py36_0         8.8 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycodestyle-2.4.0          |           py36_0          59 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter_client-5.2.3       |           py36_0         124 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python.app-2               |           py36_8         1.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    incremental-17.5.0         |           py36_0          25 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    flask-1.0.2                |           py36_1         119 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jbig-2.1                   |       h4d881f8_0          42 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter_core-4.4.0         |           py36_0          63 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    anaconda-project-0.8.2     |           py36_0         478 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycosat-0.6.3              |   py36h1de35cc_0         107 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    greenlet-0.4.14            |   py36h1de35cc_0          18 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-remotedata-0.3.0    |           py36_0          12 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-openfiles-0.3.0     |           py36_0           9 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    alabaster-0.7.11           |           py36_0          16 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sortedcollections-1.0.1    |           py36_0          15 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    packaging-17.1             |           py36_0          33 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    notebook-5.6.0             |           py36_0         7.4 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    tk-8.6.8                   |       ha441bb4_0         3.2 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlwings-0.11.8             |           py36_0         428 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    yaml-0.1.7                 |       hc338f04_2          80 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    openpyxl-2.5.6             |           py36_0         330 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    readline-7.0               |       h1de35cc_5         393 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cytoolz-0.9.0.1            |   py36h1de35cc_1         350 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    llvmlite-0.24.0            |   py36hc454e04_0        10.6 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    lxml-4.2.4                 |   py36hef8c89e_0         1.5 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyzmq-17.1.2               |   py36h1de35cc_0         407 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    send2trash-1.5.0           |           py36_0          16 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyasn1-modules-0.2.2       |           py36_0          86 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qtpy-1.5.0                 |           py36_0          50 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    scipy-1.1.0                |   py36h28f7352_1        15.4 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pep8-1.7.1                 |           py36_0          51 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pillow-5.2.0               |   py36hb68e598_0         543 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    testpath-0.3.1             |   py36h625a49b_0          90 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    spyder-kernels-0.2.6       |           py36_0          69 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    glib-2.56.2                |       hd9629dc_0         4.7 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qt-5.9.6                   |       h45cd832_2        78.1 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libiconv-1.15              |       hdd342a3_7         1.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    py-1.6.0                   |           py36_0         136 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    boto-2.49.0                |           py36_0         1.5 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    patsy-0.5.0                |           py36_0         322 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipykernel-4.9.0            |           py36_0         146 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pexpect-4.6.0              |           py36_0          77 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ncurses-6.1                |       h0a44026_0         888 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    automat-0.7.0              |           py36_0          52 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bleach-2.1.4               |           py36_0          33 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    fastcache-1.0.2            |   py36h1de35cc_2          28 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sip-4.19.12                |   py36h0a44026_0         253 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    get_terminal_size-1.0.0    |       h7520d66_0           3 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libcxxabi-4.0.1            |       hebd6815_0         149 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    asn1crypto-0.24.0          |           py36_0         154 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    conda-verify-3.1.0         |           py36_0          32 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cycler-0.10.0              |   py36hfc81398_0          13 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycrypto-2.6.1             |   py36h1de35cc_9         452 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-astropy-0.4.0       |           py36_0           5 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    future-0.16.0              |           py36_2         668 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    glob2-0.6                  |           py36_0          17 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlwt-1.2.0                 |   py36h5ad1178_0         163 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bzip2-1.0.6                |       h1de35cc_5         149 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mistune-0.8.3              |   py36h1de35cc_1         244 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    intel-openmp-2018.0.3      |                0        1004 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    psutil-5.4.7               |   py36h1de35cc_0         314 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    networkx-2.1               |           py36_0         1.8 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pysocks-1.6.8              |           py36_0          22 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pygments-2.2.0             |   py36h240cd3f_0         1.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    setuptools-40.2.0          |           py36_0         554 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    astropy-3.0.4              |   py36h1de35cc_0         6.7 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python-dateutil-2.7.3      |           py36_0         260 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jpeg-9b                    |       he5867d9_2         236 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bokeh-0.13.0               |           py36_0         5.0 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    blas-1.0                   |              mkl           5 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numexpr-2.6.8              |   py36h1dc9127_0         126 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jdcal-1.4                  |           py36_0          11 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    typed-ast-1.1.0            |   py36h1de35cc_0         183 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nbformat-4.4.0             |   py36h827af21_0         138 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    more-itertools-4.3.0       |           py36_0          83 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gmp-6.1.2                  |       hb37e062_1         734 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mccabe-0.6.1               |           py36_1          14 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xz-5.2.4                   |       h1de35cc_4         269 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libxml2-2.9.8              |       hab757c2_1         1.9 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numpy-1.15.1               |   py36h6a91979_0          37 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sphinxcontrib-websupport-1.1.0|           py36_1          36 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyterlab-0.34.7          |           py36_0        10.0 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mpc-1.1.0                  |       h6ef4df4_1          90 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sphinx-1.7.8               |           py36_0         1.6 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mpfr-4.0.1                 |       h3018a27_3         526 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipython_genutils-0.2.0     |   py36h241746c_0          39 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    partd-0.3.8                |   py36hf5c4cb8_0          31 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bkcharts-0.2               |   py36h073222e_0         127 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    hyperlink-18.0.0           |           py36_0          62 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    curl-7.61.0                |       ha441bb4_0         134 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numpy-base-1.15.1          |   py36h8a80b8c_0         4.0 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pip-10.0.1                 |           py36_0         1.8 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    freetype-2.9.1             |       hb4e5f40_0         864 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    unixodbc-2.3.7             |       h1de35cc_0         271 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    decorator-4.3.0            |           py36_0          15 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    odo-0.5.1                  |   py36hc1af34a_0         193 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    snowballstemmer-1.2.1      |   py36h6c7b616_0          85 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    werkzeug-0.14.1            |           py36_0         423 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    rope-0.11.0                |           py36_0         282 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zict-0.1.3                 |           py36_0          18 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlrd-1.1.0                 |           py36_1         194 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ptyprocess-0.6.0           |           py36_0          23 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    unicodecsv-0.14.1          |   py36he531d66_0          25 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    blaze-0.11.3               |           py36_0         603 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libcurl-7.61.0             |       hf30b1f0_0         456 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytables-3.4.4             |   py36h13cba08_0         1.4 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    chardet-3.0.4              |           py36_1         189 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cryptography-2.3.1         |   py36hdbc3d79_0         540 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    olefile-0.45.1             |           py36_0          47 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    entrypoints-0.2.3          |           py36_2           9 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libcxx-4.0.1               |       h579ed51_0         957 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    six-1.11.0                 |           py36_1          21 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    distributed-1.23.1         |           py36_0         828 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    colorama-0.3.9             |   py36hd29a30c_0          23 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    lzo-2.10                   |       h362108e_2         190 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    path.py-11.1.0             |           py36_0          53 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    lazy-object-proxy-1.3.1    |   py36h1de35cc_2          29 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    astroid-2.0.4              |           py36_0         247 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    clyent-1.2.2               |           py36_1          19 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyparsing-2.2.0            |           py36_1          96 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pkginfo-1.4.2              |           py36_1          39 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    widgetsnbextension-3.4.1   |           py36_0         1.7 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cython-0.28.5              |   py36h0a44026_0         3.0 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    prompt_toolkit-1.0.15      |   py36haeda067_0         339 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    prometheus_client-0.3.1    |   py36h28b3542_0          52 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pcre-8.42                  |       h378b8a2_0         224 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    hdf5-1.10.2                |       hfa1e0ec_1         4.5 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    babel-2.6.0                |           py36_0         5.7 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zope.interface-4.5.0       |   py36h1de35cc_0         198 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    terminado-0.8.1            |           py36_1          21 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jinja2-2.10                |           py36_0         184 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    anaconda-navigator-1.8.7   |           py36_0         4.9 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jsonschema-2.6.0           |   py36hb385e00_0          62 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    locket-0.2.0               |   py36hca03003_1           8 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    isort-4.3.4                |           py36_0          58 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    twisted-18.7.0             |   py36h1de35cc_1         4.9 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    _ipyw_jlab_nb_ext_conf-0.1.0|           py36_0           4 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    seaborn-0.9.0              |           py36_0         379 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    html5lib-1.0.1             |           py36_0         184 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qtconsole-4.4.1            |           py36_0         156 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libffi-3.2.1               |       h475c297_4          40 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycurl-7.43.0.2            |   py36hdbc3d79_0          62 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    backports.shutil_get_terminal_size-1.0.0|           py36_2           8 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    requests-2.19.1            |           py36_0          96 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jedi-0.12.1                |           py36_0         225 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    imageio-2.3.0              |           py36_0         3.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    constantly-15.1.0          |   py36h28b3542_0          13 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    statsmodels-0.9.0          |   py36h1d22016_0         8.5 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    toolz-0.9.0                |           py36_0          91 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gevent-1.3.6               |   py36h1de35cc_0         1.7 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    blosc-1.14.4               |       hd9629dc_0         317 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyyaml-3.13                |   py36h1de35cc_0         160 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    dask-core-0.19.1           |           py36_0         1.1 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zeromq-4.2.5               |       h0a44026_1         495 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    navigator-updater-0.2.1    |           py36_0         1.2 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    icu-58.2                   |       h4b95b61_1        22.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    singledispatch-3.4.0.3     |   py36hf20db9d_0          15 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numpydoc-0.8.0             |           py36_0          42 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sphinxcontrib-1.0          |           py36_1           3 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zlib-1.2.11                |       hf3cbc9b_2         101 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    appdirs-1.4.3              |   py36h28b3542_0          16 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    msgpack-python-0.5.6       |   py36h04f5b5a_1          89 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    matplotlib-2.2.3           |   py36h54f8f79_0         6.7 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    wheel-0.31.1               |           py36_0          62 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ply-3.11                   |           py36_0          79 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl_random-1.0.1           |   py36h5d10147_1         349 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pandas-0.23.4              |   py36h6440ff4_0         9.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    tornado-5.1                |   py36h1de35cc_0         665 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pylint-2.1.1               |           py36_0         795 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    service_identity-17.0.0    |   py36h28b3542_0          18 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cffi-1.11.5                |   py36h6174b99_1         205 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    datashape-0.5.4            |           py36_1         100 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    tblib-1.3.2                |   py36hda67792_0          16 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pandoc-2.2.3.2             |                0        13.8 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pathlib2-2.3.2             |           py36_0          32 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libtiff-4.0.9              |       hcb84e12_2         544 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pandocfilters-1.4.2        |           py36_1          13 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sortedcontainers-2.0.5     |           py36_0          42 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyopenssl-18.0.0           |           py36_0          82 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-3.7.4               |           py36_0         309 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    scikit-image-0.14.0        |   py36h0a44026_1        23.4 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    simplegeneric-0.8.1        |           py36_2           9 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gmpy2-2.0.8                |   py36h6ef4df4_2         162 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    docutils-0.14              |   py36hbfde631_0         689 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycparser-2.18             |           py36_1         169 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyqt-5.9.2                 |   py36h655552a_0         4.7 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    backcall-0.1.0             |           py36_0          19 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    scikit-learn-0.19.1        |   py36hf9f1f73_0         4.8 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ------------------------------------------------------------
                                           Total:       514.5 MB

The following NEW packages will be INSTALLED:

    appdirs:                            1.4.3-py36h28b3542_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    atomicwrites:                       1.2.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    automat:                            0.7.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    constantly:                         15.1.0-py36h28b3542_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    future:                             0.16.0-py36_2           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    hyperlink:                          18.0.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    incremental:                        17.5.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    keyring:                            13.2.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    prometheus_client:                  0.3.1-py36h28b3542_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyasn1:                             0.4.4-py36h28b3542_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyasn1-modules:                     0.2.2-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    service_identity:                   17.0.0-py36h28b3542_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    spyder-kernels:                     0.2.6-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    twisted:                            18.7.0-py36h1de35cc_1   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    typed-ast:                          1.1.0-py36h1de35cc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zope:                               1.0-py36_1              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zope.interface:                     4.5.0-py36h1de35cc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main

The following packages will be UPDATED:

    _ipyw_jlab_nb_ext_conf:             0.1.0-py36h2fc01ae_0    defaults                                                --> 0.1.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    alabaster:                          0.7.10-py36h174008c_0   defaults                                                --> 0.7.11-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    anaconda-client:                    1.6.14-py36_0           defaults                                                --> 1.7.2-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    anaconda-navigator:                 1.8.7-py36_0            defaults                                                --> 1.8.7-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    anaconda-project:                   0.8.2-py36h9ee5d53_0    defaults                                                --> 0.8.2-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    appnope:                            0.1.0-py36hf537a9a_0    defaults                                                --> 0.1.0-py36hf537a9a_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    appscript:                          1.0.1-py36h9e71e49_1    defaults                                                --> 1.0.1-py36h1de35cc_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    asn1crypto:                         0.24.0-py36_0           defaults                                                --> 0.24.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    astroid:                            1.6.3-py36_0            defaults                                                --> 2.0.4-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    astropy:                            3.0.2-py36h917ab60_1    defaults                                                --> 3.0.4-py36h1de35cc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    attrs:                              18.1.0-py36_0           defaults                                                --> 18.2.0-py36h28b3542_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    babel:                              2.5.3-py36_0            defaults                                                --> 2.6.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    backcall:                           0.1.0-py36_0            defaults                                                --> 0.1.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    backports:                          1.0-py36ha3c1827_1      defaults                                                --> 1.0-py36_1              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    backports.shutil_get_terminal_size: 1.0.0-py36hd7a2ee4_2    defaults                                                --> 1.0.0-py36_2            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    beautifulsoup4:                     4.6.0-py36h72d3c9f_1    defaults                                                --> 4.6.3-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bitarray:                           0.8.1-py36h1de35cc_1    defaults                                                --> 0.8.3-py36h1de35cc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bkcharts:                           0.2-py36h073222e_0      defaults                                                --> 0.2-py36h073222e_0      https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    blas:                               1.0-mkl                 defaults                                                --> 1.0-mkl                 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    blaze:                              0.11.3-py36h02e7a37_0   defaults                                                --> 0.11.3-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bleach:                             2.1.3-py36_0            defaults                                                --> 2.1.4-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    blosc:                              1.14.3-hd9629dc_0       defaults                                                --> 1.14.4-hd9629dc_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bokeh:                              0.12.16-py36_0          defaults                                                --> 0.13.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    boto:                               2.48.0-py36hdbc59ac_1   defaults                                                --> 2.49.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bottleneck:                         1.2.1-py36hbd380ad_0    defaults                                                --> 1.2.1-py36h1d22016_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    bzip2:                              1.0.6-h1de35cc_5        defaults                                                --> 1.0.6-h1de35cc_5        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cffi:                               1.11.5-py36h342bebf_0   defaults                                                --> 1.11.5-py36h6174b99_1   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    chardet:                            3.0.4-py36h96c241c_1    defaults                                                --> 3.0.4-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    click:                              6.7-py36hec950be_0      defaults                                                --> 6.7-py36hec950be_0      https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cloudpickle:                        0.5.3-py36_0            defaults                                                --> 0.5.5-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    clyent:                             1.2.2-py36hae3ad88_0    defaults                                                --> 1.2.2-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    colorama:                           0.3.9-py36hd29a30c_0    defaults                                                --> 0.3.9-py36hd29a30c_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    conda-build:                        3.10.5-py36_0           defaults                                                --> 3.14.2-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    conda-env:                          2.6.0-h36134e3_0        defaults                                                --> 2.6.0-1                 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    conda-verify:                       2.0.0-py36he837df3_0    defaults                                                --> 3.1.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    contextlib2:                        0.5.5-py36hd66e5e7_0    defaults                                                --> 0.5.5-py36hd66e5e7_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cryptography:                       2.2.2-py36h1de35cc_0    defaults                                                --> 2.3.1-py36hdbc3d79_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    curl:                               7.60.0-ha441bb4_0       defaults                                                --> 7.61.0-ha441bb4_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cycler:                             0.10.0-py36hfc81398_0   defaults                                                --> 0.10.0-py36hfc81398_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cython:                             0.28.2-py36h1de35cc_0   defaults                                                --> 0.28.5-py36h0a44026_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    cytoolz:                            0.9.0.1-py36h1de35cc_0  defaults                                                --> 0.9.0.1-py36h1de35cc_1  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    dask:                               0.17.5-py36_0           defaults                                                --> 0.19.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    dask-core:                          0.17.5-py36_0           defaults                                                --> 0.19.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    datashape:                          0.5.4-py36hfb22df8_0    defaults                                                --> 0.5.4-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    dbus:                               1.13.2-h760590f_1       defaults                                                --> 1.13.2-h760590f_1       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    decorator:                          4.3.0-py36_0            defaults                                                --> 4.3.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    distributed:                        1.21.8-py36_0           defaults                                                --> 1.23.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    docutils:                           0.14-py36hbfde631_0     defaults                                                --> 0.14-py36hbfde631_0     https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    entrypoints:                        0.2.3-py36hd81d71f_2    defaults                                                --> 0.2.3-py36_2            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    et_xmlfile:                         1.0.1-py36h1315bdc_0    defaults                                                --> 1.0.1-py36h1315bdc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    expat:                              2.2.5-hb8e80ba_0        defaults                                                --> 2.2.6-h0a44026_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    fastcache:                          1.0.2-py36h1de35cc_2    defaults                                                --> 1.0.2-py36h1de35cc_2    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    filelock:                           3.0.4-py36_0            defaults                                                --> 3.0.6-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    flask:                              1.0.2-py36_1            defaults                                                --> 1.0.2-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    flask-cors:                         3.0.4-py36_0            defaults                                                --> 3.0.6-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    freetype:                           2.8-h12048fb_1          defaults                                                --> 2.9.1-hb4e5f40_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    get_terminal_size:                  1.0.0-h7520d66_0        defaults                                                --> 1.0.0-h7520d66_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gettext:                            0.19.8.1-h15daf44_3     defaults                                                --> 0.19.8.1-h15daf44_3     https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gevent:                             1.3.0-py36h1de35cc_0    defaults                                                --> 1.3.6-py36h1de35cc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    glib:                               2.56.1-h35bc53a_0       defaults                                                --> 2.56.2-hd9629dc_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    glob2:                              0.6-py36h94c9186_0      defaults                                                --> 0.6-py36_0              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gmp:                                6.1.2-hb37e062_1        defaults                                                --> 6.1.2-hb37e062_1        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    gmpy2:                              2.0.8-py36hf9c35bd_2    defaults                                                --> 2.0.8-py36h6ef4df4_2    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    greenlet:                           0.4.13-py36h1de35cc_0   defaults                                                --> 0.4.14-py36h1de35cc_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    h5py:                               2.7.1-py36ha8ecd60_2    defaults                                                --> 2.8.0-py36h878fce3_3    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    hdf5:                               1.10.2-hfa1e0ec_1       defaults                                                --> 1.10.2-hfa1e0ec_1       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    heapdict:                           1.0.0-py36_2            defaults                                                --> 1.0.0-py36_2            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    html5lib:                           1.0.1-py36h2f9c1c0_0    defaults                                                --> 1.0.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    icu:                                58.2-h4b95b61_1         defaults                                                --> 58.2-h4b95b61_1         https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    idna:                               2.6-py36h8628d0a_1      defaults                                                --> 2.7-py36_0              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    imageio:                            2.3.0-py36_0            defaults                                                --> 2.3.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    imagesize:                          1.0.0-py36_0            defaults                                                --> 1.1.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    intel-openmp:                       2018.0.0-8              defaults                                                --> 2018.0.3-0              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipykernel:                          4.8.2-py36_0            defaults                                                --> 4.9.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipython:                            6.4.0-py36_0            defaults                                                --> 6.5.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipython_genutils:                   0.2.0-py36h241746c_0    defaults                                                --> 0.2.0-py36h241746c_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ipywidgets:                         7.2.1-py36_0            defaults                                                --> 7.4.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    isort:                              4.3.4-py36_0            defaults                                                --> 4.3.4-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    itsdangerous:                       0.24-py36h49fbb8d_1     defaults                                                --> 0.24-py36_1             https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jbig:                               2.1-h4d881f8_0          defaults                                                --> 2.1-h4d881f8_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jdcal:                              1.4-py36_0              defaults                                                --> 1.4-py36_0              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jedi:                               0.12.0-py36_1           defaults                                                --> 0.12.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jinja2:                             2.10-py36hd36f9c5_0     defaults                                                --> 2.10-py36_0             https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jpeg:                               9b-he5867d9_2           defaults                                                --> 9b-he5867d9_2           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jsonschema:                         2.6.0-py36hb385e00_0    defaults                                                --> 2.6.0-py36hb385e00_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter:                            1.0.0-py36_4            defaults                                                --> 1.0.0-py36_4            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter_client:                     5.2.3-py36_0            defaults                                                --> 5.2.3-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter_console:                    5.2.0-py36hccf5b1c_1    defaults                                                --> 5.2.0-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyter_core:                       4.4.0-py36h79cf704_0    defaults                                                --> 4.4.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyterlab:                         0.32.1-py36_0           defaults                                                --> 0.34.7-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    jupyterlab_launcher:                0.10.5-py36_0           defaults                                                --> 0.13.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    kiwisolver:                         1.0.1-py36h792292d_0    defaults                                                --> 1.0.1-py36h0a44026_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    lazy-object-proxy:                  1.3.1-py36h2fbbe47_0    defaults                                                --> 1.3.1-py36h1de35cc_2    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libcurl:                            7.60.0-hf30b1f0_0       defaults                                                --> 7.61.0-hf30b1f0_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libcxx:                             4.0.1-h579ed51_0        defaults                                                --> 4.0.1-h579ed51_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libcxxabi:                          4.0.1-hebd6815_0        defaults                                                --> 4.0.1-hebd6815_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libedit:                            3.1.20170329-hb402a30_2 defaults                                                --> 3.1.20170329-hb402a30_2 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libffi:                             3.2.1-h475c297_4        defaults                                                --> 3.2.1-h475c297_4        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libgfortran:                        3.0.1-h93005f0_2        defaults                                                --> 3.0.1-h93005f0_2        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libiconv:                           1.15-hdd342a3_7         defaults                                                --> 1.15-hdd342a3_7         https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libpng:                             1.6.34-he12f830_0       defaults                                                --> 1.6.34-he12f830_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libsodium:                          1.0.16-h3efe00b_0       defaults                                                --> 1.0.16-h3efe00b_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libssh2:                            1.8.0-h322a93b_4        defaults                                                --> 1.8.0-h322a93b_4        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libtiff:                            4.0.9-hcb84e12_1        defaults                                                --> 4.0.9-hcb84e12_2        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libxml2:                            2.9.8-hab757c2_1        defaults                                                --> 2.9.8-hab757c2_1        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    libxslt:                            1.1.32-hb819dd2_0       defaults                                                --> 1.1.32-hb819dd2_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    llvmlite:                           0.23.1-py36hc454e04_0   defaults                                                --> 0.24.0-py36hc454e04_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    locket:                             0.2.0-py36hca03003_1    defaults                                                --> 0.2.0-py36hca03003_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    lxml:                               4.2.1-py36h7166777_0    defaults                                                --> 4.2.4-py36hef8c89e_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    lzo:                                2.10-h362108e_2         defaults                                                --> 2.10-h362108e_2         https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    markupsafe:                         1.0-py36h3a1e703_1      defaults                                                --> 1.0-py36h1de35cc_1      https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    matplotlib:                         2.2.2-py36ha7267d0_0    defaults                                                --> 2.2.3-py36h54f8f79_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mccabe:                             0.6.1-py36hdaeb55d_0    defaults                                                --> 0.6.1-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mistune:                            0.8.3-py36h1de35cc_1    defaults                                                --> 0.8.3-py36h1de35cc_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl:                                2018.0.2-1              defaults                                                --> 2018.0.3-1              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl-service:                        1.1.2-py36h7ea6df4_4    defaults                                                --> 1.1.2-py36h6b9c3cc_4    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl_fft:                            1.0.1-py36h917ab60_0    defaults                                                --> 1.0.4-py36h5d10147_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mkl_random:                         1.0.1-py36h78cc56f_0    defaults                                                --> 1.0.1-py36h5d10147_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    more-itertools:                     4.1.0-py36_0            defaults                                                --> 4.3.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mpc:                                1.0.3-h7a72875_5        defaults                                                --> 1.1.0-h6ef4df4_1        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mpfr:                               3.1.5-h711e7fd_2        defaults                                                --> 4.0.1-h3018a27_3        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    mpmath:                             1.0.0-py36hf1b8295_2    defaults                                                --> 1.0.0-py36_2            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    msgpack-python:                     0.5.6-py36h04f5b5a_0    defaults                                                --> 0.5.6-py36h04f5b5a_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    multipledispatch:                   0.5.0-py36_0            defaults                                                --> 0.6.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    navigator-updater:                  0.2.1-py36_0            defaults                                                --> 0.2.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nbconvert:                          5.3.1-py36h810822e_0    defaults                                                --> 5.3.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nbformat:                           4.4.0-py36h827af21_0    defaults                                                --> 4.4.0-py36h827af21_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ncurses:                            6.1-h0a44026_0          defaults                                                --> 6.1-h0a44026_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    networkx:                           2.1-py36_0              defaults                                                --> 2.1-py36_0              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nltk:                               3.3.0-py36_0            defaults                                                --> 3.3.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    nose:                               1.3.7-py36h73fae2b_2    defaults                                                --> 1.3.7-py36_2            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    notebook:                           5.5.0-py36_0            defaults                                                --> 5.6.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numba:                              0.38.0-py36h1702cab_0   defaults                                                --> 0.39.0-py36h6440ff4_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numexpr:                            2.6.5-py36h057f876_0    defaults                                                --> 2.6.8-py36h1dc9127_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numpy:                              1.14.3-py36h9bb19eb_1   defaults                                                --> 1.15.1-py36h6a91979_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numpy-base:                         1.14.3-py36h479e554_1   defaults                                                --> 1.15.1-py36h8a80b8c_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    numpydoc:                           0.8.0-py36_0            defaults                                                --> 0.8.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    odo:                                0.5.1-py36hc1af34a_0    defaults                                                --> 0.5.1-py36hc1af34a_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    olefile:                            0.45.1-py36_0           defaults                                                --> 0.45.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    openpyxl:                           2.5.3-py36_0            defaults                                                --> 2.5.6-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    packaging:                          17.1-py36_0             defaults                                                --> 17.1-py36_0             https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pandas:                             0.23.0-py36h1702cab_0   defaults                                                --> 0.23.4-py36h6440ff4_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pandoc:                             1.19.2.1-ha5e8f32_1     defaults                                                --> 2.2.3.2-0               https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pandocfilters:                      1.4.2-py36h3b0b094_1    defaults                                                --> 1.4.2-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    parso:                              0.2.0-py36_0            defaults                                                --> 0.3.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    partd:                              0.3.8-py36hf5c4cb8_0    defaults                                                --> 0.3.8-py36hf5c4cb8_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    path.py:                            11.0.1-py36_0           defaults                                                --> 11.1.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pathlib2:                           2.3.2-py36_0            defaults                                                --> 2.3.2-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    patsy:                              0.5.0-py36_0            defaults                                                --> 0.5.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pcre:                               8.42-h378b8a2_0         defaults                                                --> 8.42-h378b8a2_0         https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pep8:                               1.7.1-py36_0            defaults                                                --> 1.7.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pexpect:                            4.5.0-py36_0            defaults                                                --> 4.6.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pickleshare:                        0.7.4-py36hf512f8e_0    defaults                                                --> 0.7.4-py36hf512f8e_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pillow:                             5.1.0-py36hfcce615_0    defaults                                                --> 5.2.0-py36hb68e598_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pip:                                10.0.1-py36_0           defaults                                                --> 10.0.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pkginfo:                            1.4.2-py36_1            defaults                                                --> 1.4.2-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pluggy:                             0.6.0-py36hb1d0581_0    defaults                                                --> 0.7.1-py36h28b3542_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ply:                                3.11-py36_0             defaults                                                --> 3.11-py36_0             https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    prompt_toolkit:                     1.0.15-py36haeda067_0   defaults                                                --> 1.0.15-py36haeda067_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    psutil:                             5.4.5-py36h1de35cc_0    defaults                                                --> 5.4.7-py36h1de35cc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ptyprocess:                         0.5.2-py36he6521c3_0    defaults                                                --> 0.6.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    py:                                 1.5.3-py36_0            defaults                                                --> 1.6.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycodestyle:                        2.4.0-py36_0            defaults                                                --> 2.4.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycosat:                            0.6.3-py36hee92d8f_0    defaults                                                --> 0.6.3-py36h1de35cc_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycparser:                          2.18-py36h724b2fc_1     defaults                                                --> 2.18-py36_1             https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycrypto:                           2.6.1-py36h1de35cc_8    defaults                                                --> 2.6.1-py36h1de35cc_9    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pycurl:                             7.43.0.1-py36hdbc3d79_0 defaults                                                --> 7.43.0.2-py36hdbc3d79_0 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyflakes:                           1.6.0-py36hea45e83_0    defaults                                                --> 2.0.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pygments:                           2.2.0-py36h240cd3f_0    defaults                                                --> 2.2.0-py36h240cd3f_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pylint:                             1.8.4-py36_0            defaults                                                --> 2.1.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyodbc:                             4.0.23-py36h0a44026_0   defaults                                                --> 4.0.24-py36h0a44026_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyopenssl:                          18.0.0-py36_0           defaults                                                --> 18.0.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyparsing:                          2.2.0-py36hb281f35_0    defaults                                                --> 2.2.0-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyqt:                               5.9.2-py36h11d3b92_0    defaults                                                --> 5.9.2-py36h655552a_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pysocks:                            1.6.8-py36_0            defaults                                                --> 1.6.8-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytables:                           3.4.3-py36h5ca999c_2    defaults                                                --> 3.4.4-py36h13cba08_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest:                             3.5.1-py36_0            defaults                                                --> 3.7.4-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-arraydiff:                   0.2-py36_0              defaults                                                --> 0.2-py36h39e3cac_0      https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-astropy:                     0.3.0-py36_0            defaults                                                --> 0.4.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-doctestplus:                 0.1.3-py36_0            defaults                                                --> 0.1.3-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-openfiles:                   0.3.0-py36_0            defaults                                                --> 0.3.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytest-remotedata:                  0.2.1-py36_0            defaults                                                --> 0.3.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python:                             3.6.5-hc167b69_1        defaults                                                --> 3.6.6-hc167b69_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python-dateutil:                    2.7.3-py36_0            defaults                                                --> 2.7.3-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python.app:                         2-py36_8                defaults                                                --> 2-py36_8                https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pytz:                               2018.4-py36_0           defaults                                                --> 2018.5-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pywavelets:                         0.5.2-py36h2710a04_0    defaults                                                --> 1.0.0-py36h1d22016_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyyaml:                             3.12-py36h2ba1e63_1     defaults                                                --> 3.13-py36h1de35cc_0     https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    pyzmq:                              17.0.0-py36h1de35cc_1   defaults                                                --> 17.1.2-py36h1de35cc_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qt:                                 5.9.5-h02808f3_0        defaults                                                --> 5.9.6-h45cd832_2        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qtawesome:                          0.4.4-py36h468c6fb_0    defaults                                                --> 0.4.4-py36h468c6fb_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qtconsole:                          4.3.1-py36hd96c0ff_0    defaults                                                --> 4.4.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    qtpy:                               1.4.1-py36_0            defaults                                                --> 1.5.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    readline:                           7.0-hc1231fa_4          defaults                                                --> 7.0-h1de35cc_5          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    requests:                           2.18.4-py36h4516966_1   defaults                                                --> 2.19.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    rope:                               0.10.7-py36h68959ac_0   defaults                                                --> 0.11.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ruamel_yaml:                        0.15.35-py36h1de35cc_1  defaults                                                --> 0.15.46-py36h1de35cc_0  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    scikit-image:                       0.13.1-py36h1de35cc_1   defaults                                                --> 0.14.0-py36h0a44026_1   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    scikit-learn:                       0.19.1-py36hffbff8c_0   defaults                                                --> 0.19.1-py36hf9f1f73_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    scipy:                              1.1.0-py36hcaad992_0    defaults                                                --> 1.1.0-py36h28f7352_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    seaborn:                            0.8.1-py36h595ecd9_0    defaults                                                --> 0.9.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    send2trash:                         1.5.0-py36_0            defaults                                                --> 1.5.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    setuptools:                         39.1.0-py36_0           defaults                                                --> 40.2.0-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    simplegeneric:                      0.8.1-py36_2            defaults                                                --> 0.8.1-py36_2            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    singledispatch:                     3.4.0.3-py36hf20db9d_0  defaults                                                --> 3.4.0.3-py36hf20db9d_0  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sip:                                4.19.8-py36h0a44026_0   defaults                                                --> 4.19.12-py36h0a44026_0  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    six:                                1.11.0-py36h0e22d5e_1   defaults                                                --> 1.11.0-py36_1           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    snappy:                             1.1.7-he62c110_3        defaults                                                --> 1.1.7-he62c110_3        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    snowballstemmer:                    1.2.1-py36h6c7b616_0    defaults                                                --> 1.2.1-py36h6c7b616_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sortedcollections:                  0.6.1-py36_0            defaults                                                --> 1.0.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sortedcontainers:                   1.5.10-py36_0           defaults                                                --> 2.0.5-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sphinx:                             1.7.4-py36_0            defaults                                                --> 1.7.8-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sphinxcontrib:                      1.0-py36h9364dc8_1      defaults                                                --> 1.0-py36_1              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sphinxcontrib-websupport:           1.0.1-py36h92f4a7a_1    defaults                                                --> 1.1.0-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    spyder:                             3.2.8-py36_0            defaults                                                --> 3.3.1-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sqlalchemy:                         1.2.7-py36hb402a30_0    defaults                                                --> 1.2.11-py36h1de35cc_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sqlite:                             3.23.1-hf1716c9_0       defaults                                                --> 3.24.0-ha441bb4_0       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    statsmodels:                        0.9.0-py36h917ab60_0    defaults                                                --> 0.9.0-py36h1d22016_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    sympy:                              1.1.1-py36h7f3cf04_0    defaults                                                --> 1.2-py36_0              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    tblib:                              1.3.2-py36hda67792_0    defaults                                                --> 1.3.2-py36hda67792_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    terminado:                          0.8.1-py36_1            defaults                                                --> 0.8.1-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    testpath:                           0.3.1-py36h625a49b_0    defaults                                                --> 0.3.1-py36h625a49b_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    tk:                                 8.6.7-h35a86e2_3        defaults                                                --> 8.6.8-ha441bb4_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    toolz:                              0.9.0-py36_0            defaults                                                --> 0.9.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    tornado:                            5.0.2-py36_0            defaults                                                --> 5.1-py36h1de35cc_0      https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    traitlets:                          4.3.2-py36h65bd3ce_0    defaults                                                --> 4.3.2-py36h65bd3ce_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    typing:                             3.6.4-py36_0            defaults                                                --> 3.6.4-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    unicodecsv:                         0.14.1-py36he531d66_0   defaults                                                --> 0.14.1-py36he531d66_0   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    unixodbc:                           2.3.6-h3efe00b_0        defaults                                                --> 2.3.7-h1de35cc_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    urllib3:                            1.22-py36h68b9469_0     defaults                                                --> 1.23-py36_0             https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    wcwidth:                            0.1.7-py36h8c6ec74_0    defaults                                                --> 0.1.7-py36h8c6ec74_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    webencodings:                       0.5.1-py36h3b9701d_1    defaults                                                --> 0.5.1-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    werkzeug:                           0.14.1-py36_0           defaults                                                --> 0.14.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    wheel:                              0.31.1-py36_0           defaults                                                --> 0.31.1-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    widgetsnbextension:                 3.2.1-py36_0            defaults                                                --> 3.4.1-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    wrapt:                              1.10.11-py36hc29e774_0  defaults                                                --> 1.10.11-py36h1de35cc_2  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlrd:                               1.1.0-py36h336f4a2_1    defaults                                                --> 1.1.0-py36_1            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlsxwriter:                         1.0.4-py36_0            defaults                                                --> 1.1.0-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlwings:                            0.11.8-py36_0           defaults                                                --> 0.11.8-py36_0           https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xlwt:                               1.2.0-py36h5ad1178_0    defaults                                                --> 1.2.0-py36h5ad1178_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    xz:                                 5.2.4-h1de35cc_4        defaults                                                --> 5.2.4-h1de35cc_4        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    yaml:                               0.1.7-hc338f04_2        defaults                                                --> 0.1.7-hc338f04_2        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zeromq:                             4.2.5-h378b8a2_0        defaults                                                --> 4.2.5-h0a44026_1        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zict:                               0.1.3-py36h71da714_0    defaults                                                --> 0.1.3-py36_0            https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    zlib:                               1.2.11-hf3cbc9b_2       defaults                                                --> 1.2.11-hf3cbc9b_2       https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main

Proceed ([y]/n)? y


Downloading and Extracting Packages
zope-1.0             | 3 KB      | ##################################### | 100% 
jupyterlab_launcher- | 36 KB     | ##################################### | 100% 
beautifulsoup4-4.6.3 | 139 KB    | ##################################### | 100% 
libsodium-1.0.16     | 324 KB    | ##################################### | 100% 
contextlib2-0.5.5    | 15 KB     | ##################################### | 100% 
sqlite-3.24.0        | 2.2 MB    | ##################################### | 100% 
click-6.7            | 104 KB    | ##################################### | 100% 
mpmath-1.0.0         | 893 KB    | ##################################### | 100% 
attrs-18.2.0         | 50 KB     | ##################################### | 100% 
ipywidgets-7.4.1     | 148 KB    | ##################################### | 100% 
libgfortran-3.0.1    | 495 KB    | ##################################### | 100% 
flask-cors-3.0.6     | 20 KB     | ##################################### | 100% 
pyodbc-4.0.24        | 60 KB     | ##################################### | 100% 
sqlalchemy-1.2.11    | 1.6 MB    | ##################################### | 100% 
ruamel_yaml-0.15.46  | 228 KB    | ##################################### | 100% 
dask-0.19.1          | 3 KB      | ##################################### | 100% 
numba-0.39.0         | 2.4 MB    | ##################################### | 100% 
xlsxwriter-1.1.0     | 210 KB    | ##################################### | 100% 
expat-2.2.6          | 129 KB    | ##################################### | 100% 
pytz-2018.5          | 231 KB    | ##################################### | 100% 
cloudpickle-0.5.5    | 26 KB     | ##################################### | 100% 
dbus-1.13.2          | 540 KB    | ##################################### | 100% 
nbconvert-5.3.1      | 405 KB    | ##################################### | 100% 
backports-1.0        | 4 KB      | ##################################### | 100% 
h5py-2.8.0           | 913 KB    | ##################################### | 100% 
qtawesome-0.4.4      | 159 KB    | ##################################### | 100% 
appscript-1.0.1      | 129 KB    | ##################################### | 100% 
mkl-service-1.1.2    | 10 KB     | ##################################### | 100% 
nltk-3.3.0           | 2.0 MB    | ##################################### | 100% 
kiwisolver-1.0.1     | 56 KB     | ##################################### | 100% 
typing-3.6.4         | 44 KB     | ##################################### | 100% 
gettext-0.19.8.1     | 3.4 MB    | ##################################### | 100% 
heapdict-1.0.0       | 7 KB      | ##################################### | 100% 
parso-0.3.1          | 114 KB    | ##################################### | 100% 
wrapt-1.10.11        | 41 KB     | ##################################### | 100% 
mkl_fft-1.0.4        | 137 KB    | ##################################### | 100% 
pickleshare-0.7.4    | 12 KB     | ##################################### | 100% 
bottleneck-1.2.1     | 113 KB    | ##################################### | 100% 
traitlets-4.3.2      | 131 KB    | ##################################### | 100% 
libssh2-1.8.0        | 218 KB    | ##################################### | 100% 
atomicwrites-1.2.1   | 11 KB     | ##################################### | 100% 
snappy-1.1.7         | 40 KB     | ##################################### | 100% 
conda-build-3.14.2   | 463 KB    | ##################################### | 100% 
pyflakes-2.0.0       | 87 KB     | ##################################### | 100% 
itsdangerous-0.24    | 21 KB     | ##################################### | 100% 
nose-1.3.7           | 214 KB    | ##################################### | 100% 
pywavelets-1.0.0     | 4.3 MB    | ##################################### | 100% 
pyasn1-0.4.4         | 101 KB    | ##################################### | 100% 
webencodings-0.5.1   | 19 KB     | ##################################### | 100% 
jupyter-1.0.0        | 5 KB      | ##################################### | 100% 
markupsafe-1.0       | 23 KB     | ##################################### | 100% 
libxslt-1.1.32       | 491 KB    | ##################################### | 100% 
idna-2.7             | 132 KB    | ##################################### | 100% 
jupyter_console-5.2. | 36 KB     | ##################################### | 100% 
pytest-arraydiff-0.2 | 14 KB     | ##################################### | 100% 
python-3.6.6         | 15.4 MB   | ##################################### | 100% 
multipledispatch-0.6 | 21 KB     | ##################################### | 100% 
anaconda-client-1.7. | 141 KB    | ##################################### | 100% 
pytest-doctestplus-0 | 19 KB     | ##################################### | 100% 
et_xmlfile-1.0.1     | 20 KB     | ##################################### | 100% 
appnope-0.1.0        | 8 KB      | ##################################### | 100% 
imagesize-1.1.0      | 9 KB      | ##################################### | 100% 
pluggy-0.7.1         | 25 KB     | ##################################### | 100% 
ipython-6.5.0        | 1.0 MB    | ##################################### | 100% 
spyder-3.3.1         | 2.6 MB    | ##################################### | 100% 
libpng-1.6.34        | 319 KB    | ##################################### | 100% 
keyring-13.2.1       | 46 KB     | ##################################### | 100% 
libedit-3.1.20170329 | 154 KB    | ##################################### | 100% 
conda-env-2.6.0      | 3 KB      | ##################################### | 100% 
filelock-3.0.6       | 12 KB     | ##################################### | 100% 
urllib3-1.23         | 152 KB    | ##################################### | 100% 
wcwidth-0.1.7        | 25 KB     | ##################################### | 100% 
mkl-2018.0.3         | 149.2 MB  | ##################################### | 100% 
bitarray-0.8.3       | 54 KB     | ##################################### | 100% 
sympy-1.2            | 8.8 MB    | ##################################### | 100% 
pycodestyle-2.4.0    | 59 KB     | ##################################### | 100% 
jupyter_client-5.2.3 | 124 KB    | ##################################### | 100% 
python.app-2         | 1.3 MB    | ##################################### | 100% 
incremental-17.5.0   | 25 KB     | ##################################### | 100% 
flask-1.0.2          | 119 KB    | ##################################### | 100% 
jbig-2.1             | 42 KB     | ##################################### | 100% 
jupyter_core-4.4.0   | 63 KB     | ##################################### | 100% 
anaconda-project-0.8 | 478 KB    | ##################################### | 100% 
pycosat-0.6.3        | 107 KB    | ##################################### | 100% 
greenlet-0.4.14      | 18 KB     | ##################################### | 100% 
pytest-remotedata-0. | 12 KB     | ##################################### | 100% 
pytest-openfiles-0.3 | 9 KB      | ##################################### | 100% 
alabaster-0.7.11     | 16 KB     | ##################################### | 100% 
sortedcollections-1. | 15 KB     | ##################################### | 100% 
packaging-17.1       | 33 KB     | ##################################### | 100% 
notebook-5.6.0       | 7.4 MB    | ##################################### | 100% 
tk-8.6.8             | 3.2 MB    | ##################################### | 100% 
xlwings-0.11.8       | 428 KB    | ##################################### | 100% 
yaml-0.1.7           | 80 KB     | ##################################### | 100% 
openpyxl-2.5.6       | 330 KB    | ##################################### | 100% 
readline-7.0         | 393 KB    | ##################################### | 100% 
cytoolz-0.9.0.1      | 350 KB    | ##################################### | 100% 
llvmlite-0.24.0      | 10.6 MB   | ##################################### | 100% 
lxml-4.2.4           | 1.5 MB    | ##################################### | 100% 
pyzmq-17.1.2         | 407 KB    | ##################################### | 100% 
send2trash-1.5.0     | 16 KB     | ##################################### | 100% 
pyasn1-modules-0.2.2 | 86 KB     | ##################################### | 100% 
qtpy-1.5.0           | 50 KB     | ##################################### | 100% 
scipy-1.1.0          | 15.4 MB   | ##################################### | 100% 
pep8-1.7.1           | 51 KB     | ##################################### | 100% 
pillow-5.2.0         | 543 KB    | ##################################### | 100% 
testpath-0.3.1       | 90 KB     | ##################################### | 100% 
spyder-kernels-0.2.6 | 69 KB     | ##################################### | 100% 
glib-2.56.2          | 4.7 MB    | ##################################### | 100% 
qt-5.9.6             | 78.1 MB   | ##################################### | 100% 
libiconv-1.15        | 1.3 MB    | ##################################### | 100% 
py-1.6.0             | 136 KB    | ##################################### | 100% 
boto-2.49.0          | 1.5 MB    | ##################################### | 100% 
patsy-0.5.0          | 322 KB    | ##################################### | 100% 
ipykernel-4.9.0      | 146 KB    | ##################################### | 100% 
pexpect-4.6.0        | 77 KB     | ##################################### | 100% 
ncurses-6.1          | 888 KB    | ##################################### | 100% 
automat-0.7.0        | 52 KB     | ##################################### | 100% 
bleach-2.1.4         | 33 KB     | ##################################### | 100% 
fastcache-1.0.2      | 28 KB     | ##################################### | 100% 
sip-4.19.12          | 253 KB    | ##################################### | 100% 
get_terminal_size-1. | 3 KB      | ##################################### | 100% 
libcxxabi-4.0.1      | 149 KB    | ##################################### | 100% 
asn1crypto-0.24.0    | 154 KB    | ##################################### | 100% 
conda-verify-3.1.0   | 32 KB     | ##################################### | 100% 
cycler-0.10.0        | 13 KB     | ##################################### | 100% 
pycrypto-2.6.1       | 452 KB    | ##################################### | 100% 
pytest-astropy-0.4.0 | 5 KB      | ##################################### | 100% 
future-0.16.0        | 668 KB    | ##################################### | 100% 
glob2-0.6            | 17 KB     | ##################################### | 100% 
xlwt-1.2.0           | 163 KB    | ##################################### | 100% 
bzip2-1.0.6          | 149 KB    | ##################################### | 100% 
mistune-0.8.3        | 244 KB    | ##################################### | 100% 
intel-openmp-2018.0. | 1004 KB   | ##################################### | 100% 
psutil-5.4.7         | 314 KB    | ##################################### | 100% 
networkx-2.1         | 1.8 MB    | ##################################### | 100% 
pysocks-1.6.8        | 22 KB     | ##################################### | 100% 
pygments-2.2.0       | 1.3 MB    | ##################################### | 100% 
setuptools-40.2.0    | 554 KB    | ##################################### | 100% 
astropy-3.0.4        | 6.7 MB    | ##################################### | 100% 
python-dateutil-2.7. | 260 KB    | ##################################### | 100% 
jpeg-9b              | 236 KB    | ##################################### | 100% 
bokeh-0.13.0         | 5.0 MB    | ##################################### | 100% 
blas-1.0             | 5 KB      | ##################################### | 100% 
numexpr-2.6.8        | 126 KB    | ##################################### | 100% 
jdcal-1.4            | 11 KB     | ##################################### | 100% 
typed-ast-1.1.0      | 183 KB    | ##################################### | 100% 
nbformat-4.4.0       | 138 KB    | ##################################### | 100% 
more-itertools-4.3.0 | 83 KB     | ##################################### | 100% 
gmp-6.1.2            | 734 KB    | ##################################### | 100% 
mccabe-0.6.1         | 14 KB     | ##################################### | 100% 
xz-5.2.4             | 269 KB    | ##################################### | 100% 
libxml2-2.9.8        | 1.9 MB    | ##################################### | 100% 
numpy-1.15.1         | 37 KB     | ##################################### | 100% 
sphinxcontrib-websup | 36 KB     | ##################################### | 100% 
jupyterlab-0.34.7    | 10.0 MB   | ##################################### | 100% 
mpc-1.1.0            | 90 KB     | ##################################### | 100% 
sphinx-1.7.8         | 1.6 MB    | ##################################### | 100% 
mpfr-4.0.1           | 526 KB    | ##################################### | 100% 
ipython_genutils-0.2 | 39 KB     | ##################################### | 100% 
partd-0.3.8          | 31 KB     | ##################################### | 100% 
bkcharts-0.2         | 127 KB    | ##################################### | 100% 
hyperlink-18.0.0     | 62 KB     | ##################################### | 100% 
curl-7.61.0          | 134 KB    | ##################################### | 100% 
numpy-base-1.15.1    | 4.0 MB    | ##################################### | 100% 
pip-10.0.1           | 1.8 MB    | ##################################### | 100% 
freetype-2.9.1       | 864 KB    | ##################################### | 100% 
unixodbc-2.3.7       | 271 KB    | ##################################### | 100% 
decorator-4.3.0      | 15 KB     | ##################################### | 100% 
odo-0.5.1            | 193 KB    | ##################################### | 100% 
snowballstemmer-1.2. | 85 KB     | ##################################### | 100% 
werkzeug-0.14.1      | 423 KB    | ##################################### | 100% 
rope-0.11.0          | 282 KB    | ##################################### | 100% 
zict-0.1.3           | 18 KB     | ##################################### | 100% 
xlrd-1.1.0           | 194 KB    | ##################################### | 100% 
ptyprocess-0.6.0     | 23 KB     | ##################################### | 100% 
unicodecsv-0.14.1    | 25 KB     | ##################################### | 100% 
blaze-0.11.3         | 603 KB    | ##################################### | 100% 
libcurl-7.61.0       | 456 KB    | ##################################### | 100% 
pytables-3.4.4       | 1.4 MB    | ##################################### | 100% 
chardet-3.0.4        | 189 KB    | ##################################### | 100% 
cryptography-2.3.1   | 540 KB    | ##################################### | 100% 
olefile-0.45.1       | 47 KB     | ##################################### | 100% 
entrypoints-0.2.3    | 9 KB      | ##################################### | 100% 
libcxx-4.0.1         | 957 KB    | ##################################### | 100% 
six-1.11.0           | 21 KB     | ##################################### | 100% 
distributed-1.23.1   | 828 KB    | ##################################### | 100% 
colorama-0.3.9       | 23 KB     | ##################################### | 100% 
lzo-2.10             | 190 KB    | ##################################### | 100% 
path.py-11.1.0       | 53 KB     | ##################################### | 100% 
lazy-object-proxy-1. | 29 KB     | ##################################### | 100% 
astroid-2.0.4        | 247 KB    | ##################################### | 100% 
clyent-1.2.2         | 19 KB     | ##################################### | 100% 
pyparsing-2.2.0      | 96 KB     | ##################################### | 100% 
pkginfo-1.4.2        | 39 KB     | ##################################### | 100% 
widgetsnbextension-3 | 1.7 MB    | ##################################### | 100% 
cython-0.28.5        | 3.0 MB    | ##################################### | 100% 
prompt_toolkit-1.0.1 | 339 KB    | ##################################### | 100% 
prometheus_client-0. | 52 KB     | ##################################### | 100% 
pcre-8.42            | 224 KB    | ##################################### | 100% 
hdf5-1.10.2          | 4.5 MB    | ##################################### | 100% 
babel-2.6.0          | 5.7 MB    | ##################################### | 100% 
zope.interface-4.5.0 | 198 KB    | ##################################### | 100% 
terminado-0.8.1      | 21 KB     | ##################################### | 100% 
jinja2-2.10          | 184 KB    | ##################################### | 100% 
anaconda-navigator-1 | 4.9 MB    | ##################################### | 100% 
jsonschema-2.6.0     | 62 KB     | ##################################### | 100% 
locket-0.2.0         | 8 KB      | ##################################### | 100% 
isort-4.3.4          | 58 KB     | ##################################### | 100% 
twisted-18.7.0       | 4.9 MB    | ##################################### | 100% 
_ipyw_jlab_nb_ext_co | 4 KB      | ##################################### | 100% 
seaborn-0.9.0        | 379 KB    | ##################################### | 100% 
html5lib-1.0.1       | 184 KB    | ##################################### | 100% 
qtconsole-4.4.1      | 156 KB    | ##################################### | 100% 
libffi-3.2.1         | 40 KB     | ##################################### | 100% 
pycurl-7.43.0.2      | 62 KB     | ##################################### | 100% 
backports.shutil_get | 8 KB      | ##################################### | 100% 
requests-2.19.1      | 96 KB     | ##################################### | 100% 
jedi-0.12.1          | 225 KB    | ##################################### | 100% 
imageio-2.3.0        | 3.3 MB    | ##################################### | 100% 
constantly-15.1.0    | 13 KB     | ##################################### | 100% 
statsmodels-0.9.0    | 8.5 MB    | ##################################### | 100% 
toolz-0.9.0          | 91 KB     | ##################################### | 100% 
gevent-1.3.6         | 1.7 MB    | ##################################### | 100% 
blosc-1.14.4         | 317 KB    | ##################################### | 100% 
pyyaml-3.13          | 160 KB    | ##################################### | 100% 
dask-core-0.19.1     | 1.1 MB    | ##################################### | 100% 
zeromq-4.2.5         | 495 KB    | ##################################### | 100% 
navigator-updater-0. | 1.2 MB    | ##################################### | 100% 
icu-58.2             | 22.3 MB   | ##################################### | 100% 
singledispatch-3.4.0 | 15 KB     | ##################################### | 100% 
numpydoc-0.8.0       | 42 KB     | ##################################### | 100% 
sphinxcontrib-1.0    | 3 KB      | ##################################### | 100% 
zlib-1.2.11          | 101 KB    | ##################################### | 100% 
appdirs-1.4.3        | 16 KB     | ##################################### | 100% 
msgpack-python-0.5.6 | 89 KB     | ##################################### | 100% 
matplotlib-2.2.3     | 6.7 MB    | ##################################### | 100% 
wheel-0.31.1         | 62 KB     | ##################################### | 100% 
ply-3.11             | 79 KB     | ##################################### | 100% 
mkl_random-1.0.1     | 349 KB    | ##################################### | 100% 
pandas-0.23.4        | 9.3 MB    | ##################################### | 100% 
tornado-5.1          | 665 KB    | ##################################### | 100% 
pylint-2.1.1         | 795 KB    | ##################################### | 100% 
service_identity-17. | 18 KB     | ##################################### | 100% 
cffi-1.11.5          | 205 KB    | ##################################### | 100% 
datashape-0.5.4      | 100 KB    | ##################################### | 100% 
tblib-1.3.2          | 16 KB     | ##################################### | 100% 
pandoc-2.2.3.2       | 13.8 MB   | ##################################### | 100% 
pathlib2-2.3.2       | 32 KB     | ##################################### | 100% 
libtiff-4.0.9        | 544 KB    | ##################################### | 100% 
pandocfilters-1.4.2  | 13 KB     | ##################################### | 100% 
sortedcontainers-2.0 | 42 KB     | ##################################### | 100% 
pyopenssl-18.0.0     | 82 KB     | ##################################### | 100% 
pytest-3.7.4         | 309 KB    | ##################################### | 100% 
scikit-image-0.14.0  | 23.4 MB   | ##################################### | 100% 
simplegeneric-0.8.1  | 9 KB      | ##################################### | 100% 
gmpy2-2.0.8          | 162 KB    | ##################################### | 100% 
docutils-0.14        | 689 KB    | ##################################### | 100% 
pycparser-2.18       | 169 KB    | ##################################### | 100% 
pyqt-5.9.2           | 4.7 MB    | ##################################### | 100% 
backcall-0.1.0       | 19 KB     | ##################################### | 100% 
scikit-learn-0.19.1  | 4.8 MB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
➜  tensorflow-project git:(master) conda install autopep8
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - autopep8

Current channels:

  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/osx-64
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/osx-64
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
  - https://repo.anaconda.com/pkgs/main/osx-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/free/osx-64
  - https://repo.anaconda.com/pkgs/free/noarch
  - https://repo.anaconda.com/pkgs/r/osx-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/pro/osx-64
  - https://repo.anaconda.com/pkgs/pro/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


➜  tensorflow-project git:(master) ✗ pip install autopep8
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting autopep8
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/cf/30/9efc988f92f41e2ba51211e3d317ee82260d563ae84dceb53f7021a1bdfe/autopep8-1.4.tar.gz (107kB)
    100% |████████████████████████████████| 112kB 9.5MB/s 
Requirement already satisfied: pycodestyle>=2.3 in /anaconda3/lib/python3.6/site-packages (from autopep8) (2.4.0)
Building wheels for collected packages: autopep8
  Running setup.py bdist_wheel for autopep8 ... done
  Stored in directory: /Users/mac/Library/Caches/pip/wheels/f4/c4/0d/f316fd4e09a3c728a658ca96167546f5c69ed9ed2491432de4
Successfully built autopep8
twisted 18.7.0 requires PyHamcrest>=1.9.0, which is not installed.
tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.15.1 which is incompatible.
tensorflow 1.10.0 has requirement setuptools<=39.1.0, but you'll have setuptools 40.2.0 which is incompatible.
Installing collected packages: autopep8
Successfully installed autopep8-1.4
You are using pip version 10.0.1, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
➜  tensorflow-project git:(master) ✗ pip doctor
ERROR: unknown command "doctor"
➜  tensorflow-project git:(master) ✗ pip check 
twisted 18.7.0 requires pyhamcrest, which is not installed.
tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you have numpy 1.15.1.
tensorflow 1.10.0 has requirement setuptools<=39.1.0, but you have setuptools 40.2.0.
You are using pip version 10.0.1, however version 18.0 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
➜  tensorflow-project git:(master) ✗ conda check

CommandNotFoundError: No command 'conda check'.

➜  tensorflow-project git:(master) ✗ conda -h    
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean        Remove unused packages and caches.
    config       Modify configuration values in .condarc. This is modeled
                 after the git config command. Writes to the user .condarc
                 file (/Users/mac/.condarc) by default.
    create       Create a new conda environment from a list of specified
                 packages.
    help         Displays a list of available conda commands and their help
                 strings.
    info         Display information about current conda install.
    install      Installs a list of packages into a specified conda
                 environment.
    list         List linked packages in a conda environment.
    package      Low-level conda package utility. (EXPERIMENTAL)
    remove       Remove a list of packages from a specified conda environment.
    uninstall    Alias for conda remove. See conda remove --help.
    search       Search for packages and display associated information. The
                 input is a MatchSpec, a query language for conda packages.
                 See examples below.
    update       Updates conda packages to the latest compatible version. This
                 command accepts a list of package names and updates them to
                 the latest versions that are compatible with all other
                 packages in the environment. Conda attempts to install the
                 newest versions of the requested packages. To accomplish
                 this, it may update some packages that are already installed,
                 or install additional packages. To prevent existing packages
                 from updating, use the --no-update-deps option. This may
                 force conda to install older versions of the requested
                 packages, and it does not prevent additional dependency
                 packages from being installed. If you wish to skip dependency
                 checking altogether, use the '--force' option. This may
                 result in an environment with incompatible packages, so this
                 option must be used with great caution.
    upgrade      Alias for conda update. See conda update --help.

optional arguments:
  -h, --help     Show this help message and exit.
  -V, --version  Show the conda version number and exit.

conda commands available from other packages:
  build
  convert
  develop
  env
  index
  inspect
  metapackage
  render
  server
  skeleton
  verify
➜  tensorflow-project git:(master) ✗ conda clean --all
Cache location: /anaconda3/pkgs
Will remove the following tarballs:

/anaconda3/pkgs
---------------
simplegeneric-0.8.1-py36_2.tar.bz2             9 KB
mpc-1.1.0-h6ef4df4_1.tar.bz2                  90 KB
odo-0.5.1-py36hc1af34a_0.tar.bz2             193 KB
nose-1.3.7-py36_2.tar.bz2                    214 KB
libedit-3.1.20170329-hb402a30_2.tar.bz2      154 KB
pip-10.0.1-py36_0.tar.bz2                    1.8 MB
backports.shutil_get_terminal_size-1.0.0-py36_2.tar.bz2       8 KB
bzip2-1.0.6-h1de35cc_5.tar.bz2               149 KB
atomicwrites-1.2.1-py36_0.tar.bz2             11 KB
pyzmq-17.1.2-py36h1de35cc_0.tar.bz2          407 KB
markdown-2.6.11-py36_0.tar.bz2               103 KB
zope-1.0-py36_1.tar.bz2                        3 KB
bottleneck-1.2.1-py36h1d22016_1.tar.bz2      113 KB
babel-2.6.0-py36_0.tar.bz2                   5.7 MB
libcxxabi-4.0.1-hebd6815_0.tar.bz2           149 KB
mistune-0.8.3-py36h1de35cc_1.tar.bz2         244 KB
conda-build-3.14.2-py36_0.tar.bz2            463 KB
twisted-18.7.0-py36h1de35cc_1.tar.bz2        4.9 MB
tensorboard-1.10.0-py36hdc36e2c_0.tar.bz2     3.3 MB
jedi-0.12.1-py36_0.tar.bz2                   225 KB
send2trash-1.5.0-py36_0.tar.bz2               16 KB
sphinxcontrib-websupport-1.1.0-py36_1.tar.bz2      36 KB
requests-2.19.1-py36_0.tar.bz2                96 KB
zict-0.1.3-py36_0.tar.bz2                     18 KB
python-dateutil-2.7.3-py36_0.tar.bz2         260 KB
lxml-4.2.4-py36hef8c89e_0.tar.bz2            1.5 MB
jinja2-2.10-py36_0.tar.bz2                   184 KB
pytest-3.7.4-py36_0.tar.bz2                  309 KB
sympy-1.2-py36_0.tar.bz2                     8.8 MB
pyflakes-2.0.0-py36_0.tar.bz2                 87 KB
anaconda-project-0.8.2-py36_0.tar.bz2        478 KB
spyder-3.3.1-py36_1.tar.bz2                  2.6 MB
protobuf-3.6.0-py36h0a44026_0.tar.bz2        604 KB
scikit-learn-0.19.1-py36hf9f1f73_0.tar.bz2     4.8 MB
xlsxwriter-1.1.0-py36_0.tar.bz2              210 KB
pytz-2018.5-py36_0.tar.bz2                   231 KB
hyperlink-18.0.0-py36_0.tar.bz2               62 KB
fastcache-1.0.2-py36h1de35cc_2.tar.bz2        28 KB
readline-7.0-h1de35cc_5.tar.bz2              393 KB
pcre-8.42-h378b8a2_0.tar.bz2                 224 KB
libcurl-7.61.0-hf30b1f0_0.tar.bz2            456 KB
colorama-0.3.9-py36hd29a30c_0.tar.bz2         23 KB
get_terminal_size-1.0.0-h7520d66_0.tar.bz2       3 KB
jupyterlab_launcher-0.13.1-py36_0.tar.bz2      36 KB
jupyter-1.0.0-py36_4.tar.bz2                   5 KB
markupsafe-1.0-py36h1de35cc_1.tar.bz2         23 KB
urllib3-1.23-py36_0.tar.bz2                  152 KB
ply-3.11-py36_0.tar.bz2                       79 KB
glob2-0.6-py36_0.tar.bz2                      17 KB
cycler-0.10.0-py36hfc81398_0.tar.bz2          13 KB
nltk-3.3.0-py36_0.tar.bz2                    2.0 MB
seaborn-0.9.0-py36_0.tar.bz2                 379 KB
prometheus_client-0.3.1-py36h28b3542_0.tar.bz2      52 KB
grpcio-1.12.1-py36hd9629dc_0.tar.bz2         1.5 MB
entrypoints-0.2.3-py36_2.tar.bz2               9 KB
appnope-0.1.0-py36hf537a9a_0.tar.bz2           8 KB
future-0.16.0-py36_2.tar.bz2                 668 KB
libxml2-2.9.8-hab757c2_1.tar.bz2             1.9 MB
ncurses-6.1-h0a44026_0.tar.bz2               888 KB
asn1crypto-0.24.0-py36_0.tar.bz2             154 KB
blaze-0.11.3-py36_0.tar.bz2                  603 KB
gast-0.2.0-py36_0.tar.bz2                     15 KB
mkl_random-1.0.1-py36h5d10147_1.tar.bz2      349 KB
imageio-2.3.0-py36_0.tar.bz2                 3.3 MB
scikit-image-0.14.0-py36h0a44026_1.tar.bz2    23.4 MB
isort-4.3.4-py36_0.tar.bz2                    58 KB
ipython-6.5.0-py36_0.tar.bz2                 1.0 MB
prompt_toolkit-1.0.15-py36haeda067_0.tar.bz2     339 KB
unixodbc-2.3.7-h1de35cc_0.tar.bz2            271 KB
unicodecsv-0.14.1-py36he531d66_0.tar.bz2      25 KB
snowballstemmer-1.2.1-py36h6c7b616_0.tar.bz2      85 KB
jdcal-1.4-py36_0.tar.bz2                      11 KB
pexpect-4.6.0-py36_0.tar.bz2                  77 KB
docutils-0.14-py36hbfde631_0.tar.bz2         689 KB
libssh2-1.8.0-h322a93b_4.tar.bz2             218 KB
heapdict-1.0.0-py36_2.tar.bz2                  7 KB
numpy-1.15.1-py36h6a91979_0.tar.bz2           37 KB
setuptools-40.2.0-py36_0.tar.bz2             554 KB
numba-0.39.0-py36h6440ff4_0.tar.bz2          2.4 MB
conda-env-2.6.0-1.tar.bz2                      3 KB
gevent-1.3.6-py36h1de35cc_0.tar.bz2          1.7 MB
ipykernel-4.9.0-py36_0.tar.bz2               146 KB
dask-0.19.1-py36_0.tar.bz2                     3 KB
sphinx-1.7.8-py36_0.tar.bz2                  1.6 MB
networkx-2.1-py36_0.tar.bz2                  1.8 MB
numpy-base-1.15.1-py36h8a80b8c_0.tar.bz2     4.0 MB
python.app-2-py36_8.tar.bz2                  1.3 MB
cloudpickle-0.5.5-py36_0.tar.bz2              26 KB
ruamel_yaml-0.15.46-py36h1de35cc_0.tar.bz2     228 KB
absl-py-0.4.1-py36_0.tar.bz2                 144 KB
anaconda-client-1.7.2-py36_0.tar.bz2         141 KB
dask-core-0.19.1-py36_0.tar.bz2              1.1 MB
yaml-0.1.7-hc338f04_2.tar.bz2                 80 KB
typing-3.6.4-py36_0.tar.bz2                   44 KB
boto-2.49.0-py36_0.tar.bz2                   1.5 MB
locket-0.2.0-py36hca03003_1.tar.bz2            8 KB
werkzeug-0.14.1-py36_0.tar.bz2               423 KB
olefile-0.45.1-py36_0.tar.bz2                 47 KB
intel-openmp-2018.0.3-0.tar.bz2             1004 KB
multipledispatch-0.6.0-py36_0.tar.bz2         21 KB
pkginfo-1.4.2-py36_1.tar.bz2                  39 KB
idna-2.7-py36_0.tar.bz2                      132 KB
pycrypto-2.6.1-py36h1de35cc_9.tar.bz2        452 KB
bkcharts-0.2-py36h073222e_0.tar.bz2          127 KB
xlrd-1.1.0-py36_1.tar.bz2                    194 KB
pandoc-2.2.3.2-0.tar.bz2                    13.8 MB
widgetsnbextension-3.4.1-py36_0.tar.bz2      1.7 MB
_ipyw_jlab_nb_ext_conf-0.1.0-py36_0.tar.bz2       4 KB
cryptography-2.3.1-py36hdbc3d79_0.tar.bz2     540 KB
xz-5.2.4-h1de35cc_4.tar.bz2                  269 KB
attrs-18.2.0-py36h28b3542_0.tar.bz2           50 KB
pytest-openfiles-0.3.0-py36_0.tar.bz2          9 KB
pep8-1.7.1-py36_0.tar.bz2                     51 KB
blas-1.0-mkl.tar.bz2                           5 KB
pytest-remotedata-0.3.0-py36_0.tar.bz2        12 KB
flask-1.0.2-py36_1.tar.bz2                   119 KB
conda-verify-3.1.0-py36_0.tar.bz2             32 KB
zope.interface-4.5.0-py36h1de35cc_0.tar.bz2     198 KB
clyent-1.2.2-py36_1.tar.bz2                   19 KB
pluggy-0.7.1-py36h28b3542_0.tar.bz2           25 KB
click-6.7-py36hec950be_0.tar.bz2             104 KB
astroid-2.0.4-py36_0.tar.bz2                 247 KB
jpeg-9b-he5867d9_2.tar.bz2                   236 KB
testpath-0.3.1-py36h625a49b_0.tar.bz2         90 KB
pyodbc-4.0.24-py36h0a44026_0.tar.bz2          60 KB
mkl_fft-1.0.4-py36h5d10147_1.tar.bz2         137 KB
qtawesome-0.4.4-py36h468c6fb_0.tar.bz2       159 KB
pycodestyle-2.4.0-py36_0.tar.bz2              59 KB
chardet-3.0.4-py36_1.tar.bz2                 189 KB
more-itertools-4.3.0-py36_0.tar.bz2           83 KB
mkl-service-1.1.2-py36h6b9c3cc_4.tar.bz2      10 KB
nbformat-4.4.0-py36h827af21_0.tar.bz2        138 KB
h5py-2.8.0-py36h878fce3_3.tar.bz2            913 KB
glib-2.56.2-hd9629dc_0.tar.bz2               4.7 MB
incremental-17.5.0-py36_0.tar.bz2             25 KB
pickleshare-0.7.4-py36hf512f8e_0.tar.bz2      12 KB
ipywidgets-7.4.1-py36_0.tar.bz2              148 KB
sortedcontainers-2.0.5-py36_0.tar.bz2         42 KB
pyyaml-3.13-py36h1de35cc_0.tar.bz2           160 KB
libsodium-1.0.16-h3efe00b_0.tar.bz2          324 KB
astor-0.7.1-py36_0.tar.bz2                    43 KB
et_xmlfile-1.0.1-py36h1315bdc_0.tar.bz2       20 KB
llvmlite-0.24.0-py36hc454e04_0.tar.bz2      10.6 MB
tornado-5.1-py36h1de35cc_0.tar.bz2           665 KB
libxslt-1.1.32-hb819dd2_0.tar.bz2            491 KB
py-1.6.0-py36_0.tar.bz2                      136 KB
libcxx-4.0.1-h579ed51_0.tar.bz2              957 KB
pywavelets-1.0.0-py36h1d22016_0.tar.bz2      4.3 MB
hdf5-1.10.2-hfa1e0ec_1.tar.bz2               4.5 MB
libgfortran-3.0.1-h93005f0_2.tar.bz2         495 KB
pytest-doctestplus-0.1.3-py36_0.tar.bz2       19 KB
libiconv-1.15-hdd342a3_7.tar.bz2             1.3 MB
pyopenssl-18.0.0-py36_0.tar.bz2               82 KB
bitarray-0.8.3-py36h1de35cc_0.tar.bz2         54 KB
psutil-5.4.7-py36h1de35cc_0.tar.bz2          314 KB
statsmodels-0.9.0-py36h1d22016_0.tar.bz2     8.5 MB
cytoolz-0.9.0.1-py36h1de35cc_1.tar.bz2       350 KB
freetype-2.9.1-hb4e5f40_0.tar.bz2            864 KB
automat-0.7.0-py36_0.tar.bz2                  52 KB
pycosat-0.6.3-py36h1de35cc_0.tar.bz2         107 KB
scipy-1.1.0-py36h28f7352_1.tar.bz2          15.4 MB
beautifulsoup4-4.6.3-py36_0.tar.bz2          139 KB
jupyterlab-0.34.7-py36_0.tar.bz2            10.0 MB
zeromq-4.2.5-h0a44026_1.tar.bz2              495 KB
dbus-1.13.2-h760590f_1.tar.bz2               540 KB
libprotobuf-3.6.0-hd9629dc_0.tar.bz2         3.8 MB
navigator-updater-0.2.1-py36_0.tar.bz2       1.2 MB
patsy-0.5.0-py36_0.tar.bz2                   322 KB
appdirs-1.4.3-py36h28b3542_0.tar.bz2          16 KB
icu-58.2-h4b95b61_1.tar.bz2                 22.3 MB
pandas-0.23.4-py36h6440ff4_0.tar.bz2         9.3 MB
pyqt-5.9.2-py36h655552a_0.tar.bz2            4.7 MB
greenlet-0.4.14-py36h1de35cc_0.tar.bz2        18 KB
sqlalchemy-1.2.11-py36h1de35cc_0.tar.bz2     1.6 MB
toolz-0.9.0-py36_0.tar.bz2                    91 KB
openpyxl-2.5.6-py36_0.tar.bz2                330 KB
six-1.11.0-py36_1.tar.bz2                     21 KB
distributed-1.23.1-py36_0.tar.bz2            828 KB
notebook-5.6.0-py36_0.tar.bz2                7.4 MB
termcolor-1.1.0-py36_1.tar.bz2                 7 KB
mpmath-1.0.0-py36_2.tar.bz2                  893 KB
msgpack-python-0.5.6-py36h04f5b5a_1.tar.bz2      89 KB
numpydoc-0.8.0-py36_0.tar.bz2                 42 KB
contextlib2-0.5.5-py36hd66e5e7_0.tar.bz2      15 KB
partd-0.3.8-py36hf5c4cb8_0.tar.bz2            31 KB
mpfr-4.0.1-h3018a27_3.tar.bz2                526 KB
gettext-0.19.8.1-h15daf44_3.tar.bz2          3.4 MB
alabaster-0.7.11-py36_0.tar.bz2               16 KB
rope-0.11.0-py36_0.tar.bz2                   282 KB
pathlib2-2.3.2-py36_0.tar.bz2                 32 KB
wheel-0.31.1-py36_0.tar.bz2                   62 KB
datashape-0.5.4-py36_1.tar.bz2               100 KB
sip-4.19.12-py36h0a44026_0.tar.bz2           253 KB
pycparser-2.18-py36_1.tar.bz2                169 KB
libtiff-4.0.9-hcb84e12_2.tar.bz2             544 KB
singledispatch-3.4.0.3-py36hf20db9d_0.tar.bz2      15 KB
packaging-17.1-py36_0.tar.bz2                 33 KB
pandocfilters-1.4.2-py36_1.tar.bz2            13 KB
blosc-1.14.4-hd9629dc_0.tar.bz2              317 KB
anaconda-navigator-1.8.7-py36_0.tar.bz2      4.9 MB
libffi-3.2.1-h475c297_4.tar.bz2               40 KB
qtpy-1.5.0-py36_0.tar.bz2                     50 KB
expat-2.2.6-h0a44026_0.tar.bz2               129 KB
decorator-4.3.0-py36_0.tar.bz2                15 KB
spyder-kernels-0.2.6-py36_0.tar.bz2           69 KB
mkl-2018.0.3-1.tar.bz2                     149.2 MB
html5lib-1.0.1-py36_0.tar.bz2                184 KB
qtconsole-4.4.1-py36_0.tar.bz2               156 KB
itsdangerous-0.24-py36_1.tar.bz2              21 KB
webencodings-0.5.1-py36_1.tar.bz2             19 KB
keyring-13.2.1-py36_0.tar.bz2                 46 KB
bleach-2.1.4-py36_0.tar.bz2                   33 KB
wcwidth-0.1.7-py36h8c6ec74_0.tar.bz2          25 KB
sqlite-3.24.0-ha441bb4_0.tar.bz2             2.2 MB
pytables-3.4.4-py36h13cba08_0.tar.bz2        1.4 MB
ipython_genutils-0.2.0-py36h241746c_0.tar.bz2      39 KB
filelock-3.0.6-py36_0.tar.bz2                 12 KB
sphinxcontrib-1.0-py36_1.tar.bz2               3 KB
gmpy2-2.0.8-py36h6ef4df4_2.tar.bz2           162 KB
typed-ast-1.1.0-py36h1de35cc_0.tar.bz2       183 KB
jsonschema-2.6.0-py36hb385e00_0.tar.bz2       62 KB
constantly-15.1.0-py36h28b3542_0.tar.bz2      13 KB
bokeh-0.13.0-py36_0.tar.bz2                  5.0 MB
pygments-2.2.0-py36h240cd3f_0.tar.bz2        1.3 MB
qt-5.9.6-h45cd832_2.tar.bz2                 78.1 MB
xlwings-0.11.8-py36_0.tar.bz2                428 KB
xlwt-1.2.0-py36h5ad1178_0.tar.bz2            163 KB
curl-7.61.0-ha441bb4_0.tar.bz2               134 KB
lazy-object-proxy-1.3.1-py36h1de35cc_2.tar.bz2      29 KB
kiwisolver-1.0.1-py36h0a44026_0.tar.bz2       56 KB
backcall-0.1.0-py36_0.tar.bz2                 19 KB
cffi-1.11.5-py36h6174b99_1.tar.bz2           205 KB
tk-8.6.8-ha441bb4_0.tar.bz2                  3.2 MB
_tflow_1100_select-0.0.2-eigen.tar.bz2         3 KB
jupyter_core-4.4.0-py36_0.tar.bz2             63 KB
pyasn1-modules-0.2.2-py36_0.tar.bz2           86 KB
pytest-arraydiff-0.2-py36h39e3cac_0.tar.bz2      14 KB
jupyter_console-5.2.0-py36_1.tar.bz2          36 KB
cython-0.28.5-py36h0a44026_0.tar.bz2         3.0 MB
backports-1.0-py36_1.tar.bz2                   4 KB
sortedcollections-1.0.1-py36_0.tar.bz2        15 KB
flask-cors-3.0.6-py36_0.tar.bz2               20 KB
imagesize-1.1.0-py36_0.tar.bz2                 9 KB
tensorflow-1.10.0-eigen_py36h0906837_0.tar.bz2       4 KB
pylint-2.1.1-py36_0.tar.bz2                  795 KB
astropy-3.0.4-py36h1de35cc_0.tar.bz2         6.7 MB
traitlets-4.3.2-py36h65bd3ce_0.tar.bz2       131 KB
path.py-11.1.0-py36_0.tar.bz2                 53 KB
numexpr-2.6.8-py36h1dc9127_0.tar.bz2         126 KB
parso-0.3.1-py36_0.tar.bz2                   114 KB
tensorflow-base-1.10.0-eigen_py36h4f0eeca_0.tar.bz2    55.3 MB
libpng-1.6.34-he12f830_0.tar.bz2             319 KB
lzo-2.10-h362108e_2.tar.bz2                  190 KB
gmp-6.1.2-hb37e062_1.tar.bz2                 734 KB
tblib-1.3.2-py36hda67792_0.tar.bz2            16 KB
jupyter_client-5.2.3-py36_0.tar.bz2          124 KB
pysocks-1.6.8-py36_0.tar.bz2                  22 KB
service_identity-17.0.0-py36h28b3542_0.tar.bz2      18 KB
snappy-1.1.7-he62c110_3.tar.bz2               40 KB
pillow-5.2.0-py36hb68e598_0.tar.bz2          543 KB
pytest-astropy-0.4.0-py36_0.tar.bz2            5 KB
wrapt-1.10.11-py36h1de35cc_2.tar.bz2          41 KB
mccabe-0.6.1-py36_1.tar.bz2                   14 KB
pycurl-7.43.0.2-py36hdbc3d79_0.tar.bz2        62 KB
pyparsing-2.2.0-py36_1.tar.bz2                96 KB
appscript-1.0.1-py36h1de35cc_1.tar.bz2       129 KB
zlib-1.2.11-hf3cbc9b_2.tar.bz2               101 KB
matplotlib-2.2.3-py36h54f8f79_0.tar.bz2      6.7 MB
pyasn1-0.4.4-py36h28b3542_0.tar.bz2          101 KB
ptyprocess-0.6.0-py36_0.tar.bz2               23 KB
nbconvert-5.3.1-py36_0.tar.bz2               405 KB
python-3.6.6-hc167b69_0.tar.bz2             15.4 MB
jbig-2.1-h4d881f8_0.tar.bz2                   42 KB
terminado-0.8.1-py36_1.tar.bz2                21 KB

---------------------------------------------------
Total:                                     579.4 MB

Proceed ([y]/n)? y

Removed simplegeneric-0.8.1-py36_2.tar.bz2
Removed mpc-1.1.0-h6ef4df4_1.tar.bz2
Removed odo-0.5.1-py36hc1af34a_0.tar.bz2
Removed nose-1.3.7-py36_2.tar.bz2
Removed libedit-3.1.20170329-hb402a30_2.tar.bz2
Removed pip-10.0.1-py36_0.tar.bz2
Removed backports.shutil_get_terminal_size-1.0.0-py36_2.tar.bz2
Removed bzip2-1.0.6-h1de35cc_5.tar.bz2
Removed atomicwrites-1.2.1-py36_0.tar.bz2
Removed pyzmq-17.1.2-py36h1de35cc_0.tar.bz2
Removed markdown-2.6.11-py36_0.tar.bz2
Removed zope-1.0-py36_1.tar.bz2
Removed bottleneck-1.2.1-py36h1d22016_1.tar.bz2
Removed babel-2.6.0-py36_0.tar.bz2
Removed libcxxabi-4.0.1-hebd6815_0.tar.bz2
Removed mistune-0.8.3-py36h1de35cc_1.tar.bz2
Removed conda-build-3.14.2-py36_0.tar.bz2
Removed twisted-18.7.0-py36h1de35cc_1.tar.bz2
Removed tensorboard-1.10.0-py36hdc36e2c_0.tar.bz2
Removed jedi-0.12.1-py36_0.tar.bz2
Removed send2trash-1.5.0-py36_0.tar.bz2
Removed sphinxcontrib-websupport-1.1.0-py36_1.tar.bz2
Removed requests-2.19.1-py36_0.tar.bz2
Removed zict-0.1.3-py36_0.tar.bz2
Removed python-dateutil-2.7.3-py36_0.tar.bz2
Removed lxml-4.2.4-py36hef8c89e_0.tar.bz2
Removed jinja2-2.10-py36_0.tar.bz2
Removed pytest-3.7.4-py36_0.tar.bz2
Removed sympy-1.2-py36_0.tar.bz2
Removed pyflakes-2.0.0-py36_0.tar.bz2
Removed anaconda-project-0.8.2-py36_0.tar.bz2
Removed spyder-3.3.1-py36_1.tar.bz2
Removed protobuf-3.6.0-py36h0a44026_0.tar.bz2
Removed scikit-learn-0.19.1-py36hf9f1f73_0.tar.bz2
Removed xlsxwriter-1.1.0-py36_0.tar.bz2
Removed pytz-2018.5-py36_0.tar.bz2
Removed hyperlink-18.0.0-py36_0.tar.bz2
Removed fastcache-1.0.2-py36h1de35cc_2.tar.bz2
Removed readline-7.0-h1de35cc_5.tar.bz2
Removed pcre-8.42-h378b8a2_0.tar.bz2
Removed libcurl-7.61.0-hf30b1f0_0.tar.bz2
Removed colorama-0.3.9-py36hd29a30c_0.tar.bz2
Removed get_terminal_size-1.0.0-h7520d66_0.tar.bz2
Removed jupyterlab_launcher-0.13.1-py36_0.tar.bz2
Removed jupyter-1.0.0-py36_4.tar.bz2
Removed markupsafe-1.0-py36h1de35cc_1.tar.bz2
Removed urllib3-1.23-py36_0.tar.bz2
Removed ply-3.11-py36_0.tar.bz2
Removed glob2-0.6-py36_0.tar.bz2
Removed cycler-0.10.0-py36hfc81398_0.tar.bz2
Removed nltk-3.3.0-py36_0.tar.bz2
Removed seaborn-0.9.0-py36_0.tar.bz2
Removed prometheus_client-0.3.1-py36h28b3542_0.tar.bz2
Removed grpcio-1.12.1-py36hd9629dc_0.tar.bz2
Removed entrypoints-0.2.3-py36_2.tar.bz2
Removed appnope-0.1.0-py36hf537a9a_0.tar.bz2
Removed future-0.16.0-py36_2.tar.bz2
Removed libxml2-2.9.8-hab757c2_1.tar.bz2
Removed ncurses-6.1-h0a44026_0.tar.bz2
Removed asn1crypto-0.24.0-py36_0.tar.bz2
Removed blaze-0.11.3-py36_0.tar.bz2
Removed gast-0.2.0-py36_0.tar.bz2
Removed mkl_random-1.0.1-py36h5d10147_1.tar.bz2
Removed imageio-2.3.0-py36_0.tar.bz2
Removed scikit-image-0.14.0-py36h0a44026_1.tar.bz2
Removed isort-4.3.4-py36_0.tar.bz2
Removed ipython-6.5.0-py36_0.tar.bz2
Removed prompt_toolkit-1.0.15-py36haeda067_0.tar.bz2
Removed unixodbc-2.3.7-h1de35cc_0.tar.bz2
Removed unicodecsv-0.14.1-py36he531d66_0.tar.bz2
Removed snowballstemmer-1.2.1-py36h6c7b616_0.tar.bz2
Removed jdcal-1.4-py36_0.tar.bz2
Removed pexpect-4.6.0-py36_0.tar.bz2
Removed docutils-0.14-py36hbfde631_0.tar.bz2
Removed libssh2-1.8.0-h322a93b_4.tar.bz2
Removed heapdict-1.0.0-py36_2.tar.bz2
Removed numpy-1.15.1-py36h6a91979_0.tar.bz2
Removed setuptools-40.2.0-py36_0.tar.bz2
Removed numba-0.39.0-py36h6440ff4_0.tar.bz2
Removed conda-env-2.6.0-1.tar.bz2
Removed gevent-1.3.6-py36h1de35cc_0.tar.bz2
Removed ipykernel-4.9.0-py36_0.tar.bz2
Removed dask-0.19.1-py36_0.tar.bz2
Removed sphinx-1.7.8-py36_0.tar.bz2
Removed networkx-2.1-py36_0.tar.bz2
Removed numpy-base-1.15.1-py36h8a80b8c_0.tar.bz2
Removed python.app-2-py36_8.tar.bz2
Removed cloudpickle-0.5.5-py36_0.tar.bz2
Removed ruamel_yaml-0.15.46-py36h1de35cc_0.tar.bz2
Removed absl-py-0.4.1-py36_0.tar.bz2
Removed anaconda-client-1.7.2-py36_0.tar.bz2
Removed dask-core-0.19.1-py36_0.tar.bz2
Removed yaml-0.1.7-hc338f04_2.tar.bz2
Removed typing-3.6.4-py36_0.tar.bz2
Removed boto-2.49.0-py36_0.tar.bz2
Removed locket-0.2.0-py36hca03003_1.tar.bz2
Removed werkzeug-0.14.1-py36_0.tar.bz2
Removed olefile-0.45.1-py36_0.tar.bz2
Removed intel-openmp-2018.0.3-0.tar.bz2
Removed multipledispatch-0.6.0-py36_0.tar.bz2
Removed pkginfo-1.4.2-py36_1.tar.bz2
Removed idna-2.7-py36_0.tar.bz2
Removed pycrypto-2.6.1-py36h1de35cc_9.tar.bz2
Removed bkcharts-0.2-py36h073222e_0.tar.bz2
Removed xlrd-1.1.0-py36_1.tar.bz2
Removed pandoc-2.2.3.2-0.tar.bz2
Removed widgetsnbextension-3.4.1-py36_0.tar.bz2
Removed _ipyw_jlab_nb_ext_conf-0.1.0-py36_0.tar.bz2
Removed cryptography-2.3.1-py36hdbc3d79_0.tar.bz2
Removed xz-5.2.4-h1de35cc_4.tar.bz2
Removed attrs-18.2.0-py36h28b3542_0.tar.bz2
Removed pytest-openfiles-0.3.0-py36_0.tar.bz2
Removed pep8-1.7.1-py36_0.tar.bz2
Removed blas-1.0-mkl.tar.bz2
Removed pytest-remotedata-0.3.0-py36_0.tar.bz2
Removed flask-1.0.2-py36_1.tar.bz2
Removed conda-verify-3.1.0-py36_0.tar.bz2
Removed zope.interface-4.5.0-py36h1de35cc_0.tar.bz2
Removed clyent-1.2.2-py36_1.tar.bz2
Removed pluggy-0.7.1-py36h28b3542_0.tar.bz2
Removed click-6.7-py36hec950be_0.tar.bz2
Removed astroid-2.0.4-py36_0.tar.bz2
Removed jpeg-9b-he5867d9_2.tar.bz2
Removed testpath-0.3.1-py36h625a49b_0.tar.bz2
Removed pyodbc-4.0.24-py36h0a44026_0.tar.bz2
Removed mkl_fft-1.0.4-py36h5d10147_1.tar.bz2
Removed qtawesome-0.4.4-py36h468c6fb_0.tar.bz2
Removed pycodestyle-2.4.0-py36_0.tar.bz2
Removed chardet-3.0.4-py36_1.tar.bz2
Removed more-itertools-4.3.0-py36_0.tar.bz2
Removed mkl-service-1.1.2-py36h6b9c3cc_4.tar.bz2
Removed nbformat-4.4.0-py36h827af21_0.tar.bz2
Removed h5py-2.8.0-py36h878fce3_3.tar.bz2
Removed glib-2.56.2-hd9629dc_0.tar.bz2
Removed incremental-17.5.0-py36_0.tar.bz2
Removed pickleshare-0.7.4-py36hf512f8e_0.tar.bz2
Removed ipywidgets-7.4.1-py36_0.tar.bz2
Removed sortedcontainers-2.0.5-py36_0.tar.bz2
Removed pyyaml-3.13-py36h1de35cc_0.tar.bz2
Removed libsodium-1.0.16-h3efe00b_0.tar.bz2
Removed astor-0.7.1-py36_0.tar.bz2
Removed et_xmlfile-1.0.1-py36h1315bdc_0.tar.bz2
Removed llvmlite-0.24.0-py36hc454e04_0.tar.bz2
Removed tornado-5.1-py36h1de35cc_0.tar.bz2
Removed libxslt-1.1.32-hb819dd2_0.tar.bz2
Removed py-1.6.0-py36_0.tar.bz2
Removed libcxx-4.0.1-h579ed51_0.tar.bz2
Removed pywavelets-1.0.0-py36h1d22016_0.tar.bz2
Removed hdf5-1.10.2-hfa1e0ec_1.tar.bz2
Removed libgfortran-3.0.1-h93005f0_2.tar.bz2
Removed pytest-doctestplus-0.1.3-py36_0.tar.bz2
Removed libiconv-1.15-hdd342a3_7.tar.bz2
Removed pyopenssl-18.0.0-py36_0.tar.bz2
Removed bitarray-0.8.3-py36h1de35cc_0.tar.bz2
Removed psutil-5.4.7-py36h1de35cc_0.tar.bz2
Removed statsmodels-0.9.0-py36h1d22016_0.tar.bz2
Removed cytoolz-0.9.0.1-py36h1de35cc_1.tar.bz2
Removed freetype-2.9.1-hb4e5f40_0.tar.bz2
Removed automat-0.7.0-py36_0.tar.bz2
Removed pycosat-0.6.3-py36h1de35cc_0.tar.bz2
Removed scipy-1.1.0-py36h28f7352_1.tar.bz2
Removed beautifulsoup4-4.6.3-py36_0.tar.bz2
Removed jupyterlab-0.34.7-py36_0.tar.bz2
Removed zeromq-4.2.5-h0a44026_1.tar.bz2
Removed dbus-1.13.2-h760590f_1.tar.bz2
Removed libprotobuf-3.6.0-hd9629dc_0.tar.bz2
Removed navigator-updater-0.2.1-py36_0.tar.bz2
Removed patsy-0.5.0-py36_0.tar.bz2
Removed appdirs-1.4.3-py36h28b3542_0.tar.bz2
Removed icu-58.2-h4b95b61_1.tar.bz2
Removed pandas-0.23.4-py36h6440ff4_0.tar.bz2
Removed pyqt-5.9.2-py36h655552a_0.tar.bz2
Removed greenlet-0.4.14-py36h1de35cc_0.tar.bz2
Removed sqlalchemy-1.2.11-py36h1de35cc_0.tar.bz2
Removed toolz-0.9.0-py36_0.tar.bz2
Removed openpyxl-2.5.6-py36_0.tar.bz2
Removed six-1.11.0-py36_1.tar.bz2
Removed distributed-1.23.1-py36_0.tar.bz2
Removed notebook-5.6.0-py36_0.tar.bz2
Removed termcolor-1.1.0-py36_1.tar.bz2
Removed mpmath-1.0.0-py36_2.tar.bz2
Removed msgpack-python-0.5.6-py36h04f5b5a_1.tar.bz2
Removed numpydoc-0.8.0-py36_0.tar.bz2
Removed contextlib2-0.5.5-py36hd66e5e7_0.tar.bz2
Removed partd-0.3.8-py36hf5c4cb8_0.tar.bz2
Removed mpfr-4.0.1-h3018a27_3.tar.bz2
Removed gettext-0.19.8.1-h15daf44_3.tar.bz2
Removed alabaster-0.7.11-py36_0.tar.bz2
Removed rope-0.11.0-py36_0.tar.bz2
Removed pathlib2-2.3.2-py36_0.tar.bz2
Removed wheel-0.31.1-py36_0.tar.bz2
Removed datashape-0.5.4-py36_1.tar.bz2
Removed sip-4.19.12-py36h0a44026_0.tar.bz2
Removed pycparser-2.18-py36_1.tar.bz2
Removed libtiff-4.0.9-hcb84e12_2.tar.bz2
Removed singledispatch-3.4.0.3-py36hf20db9d_0.tar.bz2
Removed packaging-17.1-py36_0.tar.bz2
Removed pandocfilters-1.4.2-py36_1.tar.bz2
Removed blosc-1.14.4-hd9629dc_0.tar.bz2
Removed anaconda-navigator-1.8.7-py36_0.tar.bz2
Removed libffi-3.2.1-h475c297_4.tar.bz2
Removed qtpy-1.5.0-py36_0.tar.bz2
Removed expat-2.2.6-h0a44026_0.tar.bz2
Removed decorator-4.3.0-py36_0.tar.bz2
Removed spyder-kernels-0.2.6-py36_0.tar.bz2
Removed mkl-2018.0.3-1.tar.bz2
Removed html5lib-1.0.1-py36_0.tar.bz2
Removed qtconsole-4.4.1-py36_0.tar.bz2
Removed itsdangerous-0.24-py36_1.tar.bz2
Removed webencodings-0.5.1-py36_1.tar.bz2
Removed keyring-13.2.1-py36_0.tar.bz2
Removed bleach-2.1.4-py36_0.tar.bz2
Removed wcwidth-0.1.7-py36h8c6ec74_0.tar.bz2
Removed sqlite-3.24.0-ha441bb4_0.tar.bz2
Removed pytables-3.4.4-py36h13cba08_0.tar.bz2
Removed ipython_genutils-0.2.0-py36h241746c_0.tar.bz2
Removed filelock-3.0.6-py36_0.tar.bz2
Removed sphinxcontrib-1.0-py36_1.tar.bz2
Removed gmpy2-2.0.8-py36h6ef4df4_2.tar.bz2
Removed typed-ast-1.1.0-py36h1de35cc_0.tar.bz2
Removed jsonschema-2.6.0-py36hb385e00_0.tar.bz2
Removed constantly-15.1.0-py36h28b3542_0.tar.bz2
Removed bokeh-0.13.0-py36_0.tar.bz2
Removed pygments-2.2.0-py36h240cd3f_0.tar.bz2
Removed qt-5.9.6-h45cd832_2.tar.bz2
Removed xlwings-0.11.8-py36_0.tar.bz2
Removed xlwt-1.2.0-py36h5ad1178_0.tar.bz2
Removed curl-7.61.0-ha441bb4_0.tar.bz2
Removed lazy-object-proxy-1.3.1-py36h1de35cc_2.tar.bz2
Removed kiwisolver-1.0.1-py36h0a44026_0.tar.bz2
Removed backcall-0.1.0-py36_0.tar.bz2
Removed cffi-1.11.5-py36h6174b99_1.tar.bz2
Removed tk-8.6.8-ha441bb4_0.tar.bz2
Removed _tflow_1100_select-0.0.2-eigen.tar.bz2
Removed jupyter_core-4.4.0-py36_0.tar.bz2
Removed pyasn1-modules-0.2.2-py36_0.tar.bz2
Removed pytest-arraydiff-0.2-py36h39e3cac_0.tar.bz2
Removed jupyter_console-5.2.0-py36_1.tar.bz2
Removed cython-0.28.5-py36h0a44026_0.tar.bz2
Removed backports-1.0-py36_1.tar.bz2
Removed sortedcollections-1.0.1-py36_0.tar.bz2
Removed flask-cors-3.0.6-py36_0.tar.bz2
Removed imagesize-1.1.0-py36_0.tar.bz2
Removed tensorflow-1.10.0-eigen_py36h0906837_0.tar.bz2
Removed pylint-2.1.1-py36_0.tar.bz2
Removed astropy-3.0.4-py36h1de35cc_0.tar.bz2
Removed traitlets-4.3.2-py36h65bd3ce_0.tar.bz2
Removed path.py-11.1.0-py36_0.tar.bz2
Removed numexpr-2.6.8-py36h1dc9127_0.tar.bz2
Removed parso-0.3.1-py36_0.tar.bz2
Removed tensorflow-base-1.10.0-eigen_py36h4f0eeca_0.tar.bz2
Removed libpng-1.6.34-he12f830_0.tar.bz2
Removed lzo-2.10-h362108e_2.tar.bz2
Removed gmp-6.1.2-hb37e062_1.tar.bz2
Removed tblib-1.3.2-py36hda67792_0.tar.bz2
Removed jupyter_client-5.2.3-py36_0.tar.bz2
Removed pysocks-1.6.8-py36_0.tar.bz2
Removed service_identity-17.0.0-py36h28b3542_0.tar.bz2
Removed snappy-1.1.7-he62c110_3.tar.bz2
Removed pillow-5.2.0-py36hb68e598_0.tar.bz2
Removed pytest-astropy-0.4.0-py36_0.tar.bz2
Removed wrapt-1.10.11-py36h1de35cc_2.tar.bz2
Removed mccabe-0.6.1-py36_1.tar.bz2
Removed pycurl-7.43.0.2-py36hdbc3d79_0.tar.bz2
Removed pyparsing-2.2.0-py36_1.tar.bz2
Removed appscript-1.0.1-py36h1de35cc_1.tar.bz2
Removed zlib-1.2.11-hf3cbc9b_2.tar.bz2
Removed matplotlib-2.2.3-py36h54f8f79_0.tar.bz2
Removed pyasn1-0.4.4-py36h28b3542_0.tar.bz2
Removed ptyprocess-0.6.0-py36_0.tar.bz2
Removed nbconvert-5.3.1-py36_0.tar.bz2
Removed python-3.6.6-hc167b69_0.tar.bz2
Removed jbig-2.1-h4d881f8_0.tar.bz2
Removed terminado-0.8.1-py36_1.tar.bz2
Cache location: /anaconda3/pkgs
Will remove the following packages:
/anaconda3/pkgs
---------------

mkl-service-1.1.2-py36h7ea6df4_4              30 KB
ipywidgets-7.2.1-py36_0                      520 KB
msgpack-python-0.5.6-py36h04f5b5a_0          263 KB
sortedcontainers-1.5.10-py36_0               244 KB
kiwisolver-1.0.1-py36h792292d_0              167 KB
alabaster-0.7.10-py36h174008c_0               49 KB
libcurl-7.60.0-hf30b1f0_0                    1.4 MB
zeromq-4.2.5-h378b8a2_0                      2.0 MB
wrapt-1.10.11-py36hc29e774_0                 159 KB
_tflow_1100_select-0.0.2-eigen                 6 KB
pycurl-7.43.0.1-py36hdbc3d79_0               166 KB
attrs-18.1.0-py36_0                          173 KB
distributed-1.21.8-py36_0                    3.2 MB
clyent-1.2.2-py36hae3ad88_0                   59 KB
cryptography-2.2.2-py36h1de35cc_0            2.8 MB
ruamel_yaml-0.15.35-py36h1de35cc_1           955 KB
_ipyw_jlab_nb_ext_conf-0.1.0-py36h2fc01ae_0      10 KB
bitarray-0.8.1-py36h1de35cc_1                232 KB
intel-openmp-2018.0.0-8                      2.4 MB
pyflakes-1.6.0-py36hea45e83_0                463 KB
pillow-5.1.0-py36hfcce615_0                  1.8 MB
conda-build-3.10.5-py36_0                    1.6 MB
pytest-remotedata-0.2.1-py36_0                33 KB
freetype-2.8-h12048fb_1                      2.7 MB
blas-1.0-mkl                                  14 KB
flask-cors-3.0.4-py36_0                       69 KB
pytest-arraydiff-0.2-py36_0                   41 KB
conda-env-2.6.0-1                              7 KB
openpyxl-2.5.3-py36_0                        1.6 MB
h5py-2.7.1-py36ha8ecd60_2                    3.2 MB
anaconda-client-1.6.14-py36_0                621 KB
cytoolz-0.9.0.1-py36h1de35cc_0               1.2 MB
parso-0.2.0-py36_0                           499 KB
requests-2.18.4-py36h4516966_1               379 KB
pycrypto-2.6.1-py36h1de35cc_8                1.9 MB
ipykernel-4.8.2-py36_0                       600 KB
setuptools-39.1.0-py36_0                     2.6 MB
gevent-1.3.0-py36h1de35cc_0                 11.0 MB
spyder-3.2.8-py36_0                          9.2 MB
boto-2.48.0-py36hdbc59ac_1                   8.8 MB
qt-5.9.5-h02808f3_0                        257.4 MB
pytest-astropy-0.3.0-py36_0                   15 KB
notebook-5.5.0-py36_0                       28.0 MB
glib-2.56.1-h35bc53a_0                      33.4 MB
numpy-base-1.14.3-py36h479e554_1            17.2 MB
pycparser-2.18-py36h724b2fc_1                916 KB
pluggy-0.6.0-py36hb1d0581_0                   78 KB
numba-0.38.0-py36h1702cab_0                 10.5 MB
babel-2.5.3-py36_0                          20.1 MB
lazy-object-proxy-1.3.1-py36h2fbbe47_0       131 KB
readline-7.0-hc1231fa_4                      1.4 MB
jupyterlab_launcher-0.10.5-py36_0             79 KB
mccabe-0.6.1-py36hdaeb55d_0                   38 KB
mpfr-3.1.5-h711e7fd_2                        1.4 MB
nbconvert-5.3.1-py36h810822e_0               1.4 MB
pylint-1.8.4-py36_0                          4.0 MB
dask-core-0.17.5-py36_0                      4.5 MB
markupsafe-1.0-py36h3a1e703_1                 75 KB
cloudpickle-0.5.3-py36_0                      80 KB
lxml-4.2.1-py36h7166777_0                    4.3 MB
cffi-1.11.5-py36h342bebf_0                   765 KB
pytables-3.4.3-py36h5ca999c_2                7.0 MB
zict-0.1.3-py36h71da714_0                     66 KB
statsmodels-0.9.0-py36h917ab60_0            31.6 MB
blosc-1.14.3-hd9629dc_0                     1002 KB
backports-1.0-py36ha3c1827_1                   8 KB
tensorflow-1.10.0-eigen_py36h0906837_0        12 KB
html5lib-1.0.1-py36h2f9c1c0_0                896 KB
pandocfilters-1.4.2-py36h3b0b094_1            37 KB
greenlet-0.4.13-py36h1de35cc_0                48 KB
pyqt-5.9.2-py36h11d3b92_0                   24.4 MB
anaconda-project-0.8.2-py36h9ee5d53_0        2.8 MB
pandas-0.23.0-py36h1702cab_0                51.7 MB
llvmlite-0.23.1-py36hc454e04_0              32.8 MB
widgetsnbextension-3.2.1-py36_0             10.3 MB
dask-0.19.1-py36_0                             9 KB
scikit-learn-0.19.1-py36hffbff8c_0          17.8 MB
numpy-1.15.1-py36h6a91979_0                  212 KB
jupyterlab-0.32.1-py36_0                    46.5 MB
bottleneck-1.2.1-py36hbd380ad_0              494 KB
imagesize-1.0.0-py36_0                        23 KB
xlrd-1.1.0-py36h336f4a2_1                    732 KB
unixodbc-2.3.6-h3efe00b_0                    963 KB
jedi-0.12.0-py36_1                           983 KB
sqlalchemy-1.2.7-py36hb402a30_0              7.8 MB
scikit-image-0.13.1-py36h1de35cc_1          33.8 MB
sip-4.19.8-py36h0a44026_0                    701 KB
sortedcollections-0.6.1-py36_0                52 KB
get_terminal_size-1.0.0-h7520d66_0             7 KB
numexpr-2.6.5-py36h057f876_0                 423 KB
astropy-3.0.2-py36h917ab60_1                27.8 MB
mkl-2018.0.2-1                             526.2 MB
tk-8.6.7-h35a86e2_3                          9.4 MB
blaze-0.11.3-py36h02e7a37_0                  2.7 MB
sqlite-3.23.1-hf1716c9_0                     4.6 MB
bokeh-0.12.16-py36_0                        24.9 MB
py-1.5.3-py36_0                              537 KB
qtconsole-4.3.1-py36hd96c0ff_0               681 KB
pytz-2018.4-py36_0                           1.2 MB
beautifulsoup4-4.6.0-py36h72d3c9f_1          608 KB
pycosat-0.6.3-py36hee92d8f_0                 424 KB
pywavelets-0.5.2-py36h2710a04_0              6.3 MB
mpmath-1.0.0-py36hf1b8295_2                  3.6 MB
curl-7.61.0-ha441bb4_0                       227 KB
glob2-0.6-py36h94c9186_0                      50 KB
cython-0.28.2-py36h1de35cc_0                11.1 MB
mpc-1.0.3-h7a72875_5                         358 KB
filelock-3.0.4-py36_0                         38 KB
conda-verify-2.0.0-py36he837df3_0             60 KB
pandoc-1.19.2.1-ha5e8f32_1                 216.8 MB
bleach-2.1.3-py36_0                          117 KB
pytest-3.5.1-py36_0                          1.2 MB
sympy-1.1.1-py36h7f3cf04_0                  30.2 MB
multipledispatch-0.5.0-py36_0                 58 KB
scipy-1.1.0-py36hcaad992_0                  50.2 MB
appscript-1.0.1-py36h9e71e49_1               480 KB
sphinx-1.7.4-py36_0                          8.7 MB
ptyprocess-0.5.2-py36he6521c3_0               73 KB
expat-2.2.5-hb8e80ba_0                       480 KB
gmpy2-2.0.8-py36hf9c35bd_2                   498 KB
backports.shutil_get_terminal_size-1.0.0-py36hd7a2ee4_2      21 KB
pyodbc-4.0.23-py36h0a44026_0                 155 KB
itsdangerous-0.24-py36h49fbb8d_1              73 KB
rope-0.10.7-py36h68959ac_0                   1.4 MB
idna-2.6-py36h8628d0a_1                      517 KB
path.py-11.0.1-py36_0                        209 KB
pexpect-4.5.0-py36_0                         326 KB
psutil-5.4.5-py36h1de35cc_0                  1.4 MB
jinja2-2.10-py36hd36f9c5_0                   831 KB
sphinxcontrib-1.0-py36h9364dc8_1               7 KB
urllib3-1.22-py36h68b9469_0                  672 KB
entrypoints-0.2.3-py36hd81d71f_2              24 KB
mkl_fft-1.0.1-py36h917ab60_0                 419 KB
python-3.6.5-hc167b69_1                     41.8 MB
libtiff-4.0.9-hcb84e12_1                     1.7 MB
nose-1.3.7-py36h73fae2b_2                    948 KB
seaborn-0.8.1-py36h595ecd9_0                 1.5 MB
xlsxwriter-1.0.4-py36_0                      1.1 MB
tornado-5.0.2-py36_0                         3.0 MB
mkl_random-1.0.1-py36h78cc56f_0              1.1 MB
jupyter_console-5.2.0-py36hccf5b1c_1         118 KB
pyparsing-2.2.0-py36hb281f35_0               440 KB
jupyter_core-4.4.0-py36h79cf704_0            322 KB
six-1.11.0-py36h0e22d5e_1                     68 KB
chardet-3.0.4-py36h96c241c_1                 937 KB
matplotlib-2.2.2-py36ha7267d0_0             19.1 MB
ipython-6.4.0-py36_0                         4.1 MB
pyzmq-17.0.0-py36h1de35cc_1                  1.7 MB
qtpy-1.4.1-py36_0                            184 KB
astroid-1.6.3-py36_0                        64.2 MB
webencodings-0.5.1-py36h3b9701d_1             70 KB
datashape-0.5.4-py36hfb22df8_0               435 KB
sphinxcontrib-websupport-1.0.1-py36h92f4a7a_1     145 KB
pyyaml-3.12-py36h2ba1e63_1                   534 KB
more-itertools-4.1.0-py36_0                  365 KB

---------------------------------------------------
Total:                                      1.76 GB

Proceed ([y]/n)? y

removing mkl-service-1.1.2-py36h7ea6df4_4
removing ipywidgets-7.2.1-py36_0
removing msgpack-python-0.5.6-py36h04f5b5a_0
removing sortedcontainers-1.5.10-py36_0
removing kiwisolver-1.0.1-py36h792292d_0
removing alabaster-0.7.10-py36h174008c_0
removing libcurl-7.60.0-hf30b1f0_0
removing zeromq-4.2.5-h378b8a2_0
removing wrapt-1.10.11-py36hc29e774_0
removing _tflow_1100_select-0.0.2-eigen
removing pycurl-7.43.0.1-py36hdbc3d79_0
removing attrs-18.1.0-py36_0
removing distributed-1.21.8-py36_0
removing clyent-1.2.2-py36hae3ad88_0
removing cryptography-2.2.2-py36h1de35cc_0
removing ruamel_yaml-0.15.35-py36h1de35cc_1
removing _ipyw_jlab_nb_ext_conf-0.1.0-py36h2fc01ae_0
removing bitarray-0.8.1-py36h1de35cc_1
removing intel-openmp-2018.0.0-8
removing pyflakes-1.6.0-py36hea45e83_0
removing pillow-5.1.0-py36hfcce615_0
removing conda-build-3.10.5-py36_0
removing pytest-remotedata-0.2.1-py36_0
removing freetype-2.8-h12048fb_1
removing blas-1.0-mkl
removing flask-cors-3.0.4-py36_0
removing pytest-arraydiff-0.2-py36_0
removing conda-env-2.6.0-1
removing openpyxl-2.5.3-py36_0
removing h5py-2.7.1-py36ha8ecd60_2
removing anaconda-client-1.6.14-py36_0
removing cytoolz-0.9.0.1-py36h1de35cc_0
removing parso-0.2.0-py36_0
removing requests-2.18.4-py36h4516966_1
removing pycrypto-2.6.1-py36h1de35cc_8
removing ipykernel-4.8.2-py36_0
removing setuptools-39.1.0-py36_0
removing gevent-1.3.0-py36h1de35cc_0
removing spyder-3.2.8-py36_0
removing boto-2.48.0-py36hdbc59ac_1
removing qt-5.9.5-h02808f3_0
removing pytest-astropy-0.3.0-py36_0
removing notebook-5.5.0-py36_0
removing glib-2.56.1-h35bc53a_0
removing numpy-base-1.14.3-py36h479e554_1
removing pycparser-2.18-py36h724b2fc_1
removing pluggy-0.6.0-py36hb1d0581_0
removing numba-0.38.0-py36h1702cab_0
removing babel-2.5.3-py36_0
removing lazy-object-proxy-1.3.1-py36h2fbbe47_0
removing readline-7.0-hc1231fa_4
removing jupyterlab_launcher-0.10.5-py36_0
removing mccabe-0.6.1-py36hdaeb55d_0
removing mpfr-3.1.5-h711e7fd_2
removing nbconvert-5.3.1-py36h810822e_0
removing pylint-1.8.4-py36_0
removing dask-core-0.17.5-py36_0
removing markupsafe-1.0-py36h3a1e703_1
removing cloudpickle-0.5.3-py36_0
removing lxml-4.2.1-py36h7166777_0
removing cffi-1.11.5-py36h342bebf_0
removing pytables-3.4.3-py36h5ca999c_2
removing zict-0.1.3-py36h71da714_0
removing statsmodels-0.9.0-py36h917ab60_0
removing blosc-1.14.3-hd9629dc_0
removing backports-1.0-py36ha3c1827_1
removing tensorflow-1.10.0-eigen_py36h0906837_0
removing html5lib-1.0.1-py36h2f9c1c0_0
removing pandocfilters-1.4.2-py36h3b0b094_1
removing greenlet-0.4.13-py36h1de35cc_0
removing pyqt-5.9.2-py36h11d3b92_0
removing anaconda-project-0.8.2-py36h9ee5d53_0
removing pandas-0.23.0-py36h1702cab_0
removing llvmlite-0.23.1-py36hc454e04_0
removing widgetsnbextension-3.2.1-py36_0
removing dask-0.19.1-py36_0
removing scikit-learn-0.19.1-py36hffbff8c_0
removing numpy-1.15.1-py36h6a91979_0
removing jupyterlab-0.32.1-py36_0
removing bottleneck-1.2.1-py36hbd380ad_0
removing imagesize-1.0.0-py36_0
removing xlrd-1.1.0-py36h336f4a2_1
removing unixodbc-2.3.6-h3efe00b_0
removing jedi-0.12.0-py36_1
removing sqlalchemy-1.2.7-py36hb402a30_0
removing scikit-image-0.13.1-py36h1de35cc_1
removing sip-4.19.8-py36h0a44026_0
removing sortedcollections-0.6.1-py36_0
removing get_terminal_size-1.0.0-h7520d66_0
removing numexpr-2.6.5-py36h057f876_0
removing astropy-3.0.2-py36h917ab60_1
removing mkl-2018.0.2-1
removing tk-8.6.7-h35a86e2_3
removing blaze-0.11.3-py36h02e7a37_0
removing sqlite-3.23.1-hf1716c9_0
removing bokeh-0.12.16-py36_0
removing py-1.5.3-py36_0
removing qtconsole-4.3.1-py36hd96c0ff_0
removing pytz-2018.4-py36_0
removing beautifulsoup4-4.6.0-py36h72d3c9f_1
removing pycosat-0.6.3-py36hee92d8f_0
removing pywavelets-0.5.2-py36h2710a04_0
removing mpmath-1.0.0-py36hf1b8295_2
removing curl-7.61.0-ha441bb4_0
removing glob2-0.6-py36h94c9186_0
removing cython-0.28.2-py36h1de35cc_0
removing mpc-1.0.3-h7a72875_5
removing filelock-3.0.4-py36_0
removing conda-verify-2.0.0-py36he837df3_0
removing pandoc-1.19.2.1-ha5e8f32_1
removing bleach-2.1.3-py36_0
removing pytest-3.5.1-py36_0
removing sympy-1.1.1-py36h7f3cf04_0
removing multipledispatch-0.5.0-py36_0
removing scipy-1.1.0-py36hcaad992_0
removing appscript-1.0.1-py36h9e71e49_1
removing sphinx-1.7.4-py36_0
removing ptyprocess-0.5.2-py36he6521c3_0
removing expat-2.2.5-hb8e80ba_0
removing gmpy2-2.0.8-py36hf9c35bd_2
removing backports.shutil_get_terminal_size-1.0.0-py36hd7a2ee4_2
removing pyodbc-4.0.23-py36h0a44026_0
removing itsdangerous-0.24-py36h49fbb8d_1
removing rope-0.10.7-py36h68959ac_0
removing idna-2.6-py36h8628d0a_1
removing path.py-11.0.1-py36_0
removing pexpect-4.5.0-py36_0
removing psutil-5.4.5-py36h1de35cc_0
removing jinja2-2.10-py36hd36f9c5_0
removing sphinxcontrib-1.0-py36h9364dc8_1
removing urllib3-1.22-py36h68b9469_0
removing entrypoints-0.2.3-py36hd81d71f_2
removing mkl_fft-1.0.1-py36h917ab60_0
removing python-3.6.5-hc167b69_1
removing libtiff-4.0.9-hcb84e12_1
removing nose-1.3.7-py36h73fae2b_2
removing seaborn-0.8.1-py36h595ecd9_0
removing xlsxwriter-1.0.4-py36_0
removing tornado-5.0.2-py36_0
removing mkl_random-1.0.1-py36h78cc56f_0
removing jupyter_console-5.2.0-py36hccf5b1c_1
removing pyparsing-2.2.0-py36hb281f35_0
removing jupyter_core-4.4.0-py36h79cf704_0
removing six-1.11.0-py36h0e22d5e_1
removing chardet-3.0.4-py36h96c241c_1
removing matplotlib-2.2.2-py36ha7267d0_0
removing ipython-6.4.0-py36_0
removing pyzmq-17.0.0-py36h1de35cc_1
removing qtpy-1.4.1-py36_0
removing astroid-1.6.3-py36_0
removing webencodings-0.5.1-py36h3b9701d_1
removing datashape-0.5.4-py36hfb22df8_0
removing sphinxcontrib-websupport-1.0.1-py36h92f4a7a_1
removing pyyaml-3.12-py36h2ba1e63_1
removing more-itertools-4.1.0-py36_0
source cache (/anaconda3/conda-bld/src_cache)
Size:                                           0 B

git cache (/anaconda3/conda-bld/git_cache)
Size:                                           0 B

hg cache (/anaconda3/conda-bld/hg_cache)
Size:                                           0 B

svn cache (/anaconda3/conda-bld/svn_cache)
Size:                                           0 B

Total:                                          0 B
Proceed ([y]/n)? y

Removing /anaconda3/conda-bld/src_cache
Removing /anaconda3/conda-bld/git_cache
Removing /anaconda3/conda-bld/hg_cache
Removing /anaconda3/conda-bld/svn_cache
➜  tensorflow-project git:(master) ✗ git commit -m "Change all file structures to increase the number of papers"
On branch master
Changes not staged for commit:
	modified:   MNIST/fashionMnist.py

no changes added to commit
➜  tensorflow-project git:(master) ✗ git add -A
➜  tensorflow-project git:(master) ✗ git commit -m "Change all file structures to increase the number of papers"
[master fff4a34] Change all file structures to increase the number of papers
 1 file changed, 92 insertions(+), 10 deletions(-)
➜  tensorflow-project git:(master) git push origin master 
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.73 KiB | 1.73 MiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/lornatang/tensorflow-project.git
   2ca6abe..fff4a34  master -> master
➜  tensorflow-project git:(master) git add -A
➜  tensorflow-project git:(master) ✗ git commit -m "Change all file structures to increase the number of papers"
[master 04242a7] Change all file structures to increase the number of papers
 2 files changed, 15 insertions(+), 13 deletions(-)
➜  tensorflow-project git:(master) git push origin master
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 674 bytes | 674.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/lornatang/tensorflow-project.git
   fff4a34..04242a7  master -> master
➜  tensorflow-project git:(master) git add -A
➜  tensorflow-project git:(master) ✗ git commit -m "Change all file structures to increase the number of papers"
[master 701bd70] Change all file structures to increase the number of papers
 1 file changed, 8 insertions(+), 7 deletions(-)
➜  tensorflow-project git:(master) git add -A
➜  tensorflow-project git:(master) ✗ git commit -m "Change all file structures to increase the number of papers"
[master 66e8873] Change all file structures to increase the number of papers
 1 file changed, 6 insertions(+), 1 deletion(-)
➜  tensorflow-project git:(master) git push origin master
Counting objects: 8, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.00 KiB | 1.00 MiB/s, done.
Total 8 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/lornatang/tensorflow-project.git
   04242a7..66e8873  master -> master
➜  tensorflow-project git:(master) git add -A
➜  tensorflow-project git:(master) ✗ git commit -m "Change all file structures to increase the number of papers"
[master 65c1e12] Change all file structures to increase the number of papers
 1 file changed, 10 insertions(+), 9 deletions(-)
➜  tensorflow-project git:(master) git push origin master
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 517 bytes | 517.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/lornatang/tensorflow-project.git
   66e8873..65c1e12  master -> master
➜  tensorflow-project git:(master) git add -A
➜  tensorflow-project git:(master) ✗ git commit -m "Rewrite most of the code to use the argparse parameter format"
[master 8929059] Rewrite most of the code to use the argparse parameter format
 1 file changed, 49 insertions(+), 32 deletions(-)
➜  tensorflow-project git:(master) git push origin master 
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.07 KiB | 1.07 MiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/lornatang/tensorflow-project.git
   65c1e12..8929059  master -> master
➜  tensorflow-project git:(master) cd ..
➜  Program git clone https://github.com/lornatang/tfmodels
Cloning into 'tfmodels'...
remote: Counting objects: 21746, done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 21746 (delta 1), reused 2 (delta 0), pack-reused 21733
Receiving objects: 100% (21746/21746), 558.61 MiB | 2.49 MiB/s, done.
Resolving deltas: 100% (12813/12813), done.
➜  Program cd tfmodels 
➜  tfmodels git:(master) conda install official/requirements.txt 
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - official/requirements.txt

Current channels:

  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/osx-64
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/osx-64
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
  - https://repo.anaconda.com/pkgs/main/osx-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/free/osx-64
  - https://repo.anaconda.com/pkgs/free/noarch
  - https://repo.anaconda.com/pkgs/r/osx-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/pro/osx-64
  - https://repo.anaconda.com/pkgs/pro/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


➜  tfmodels git:(master) cd ~
➜  ~ cd Desktop 
➜  Desktop vim test.py
➜  Desktop python test.py 
  File "test.py", line 12
    new_image.paste(image, (0, int((new_image_length - height) / 2)))
    ^
IndentationError: unexpected indent
➜  Desktop vim test.py   
➜  Desktop vim test.py +12
➜  Desktop python test.py 
297 447
447
9
Traceback (most recent call last):
  File "test.py", line 51, in <module>
    save_images(image_list)
  File "test.py", line 40, in save_images
    image.save('result/'+str(index)+'.png')
  File "/anaconda3/lib/python3.6/site-packages/PIL/Image.py", line 1947, in save
    fp = builtins.open(filename, "w+b")
FileNotFoundError: [Errno 2] No such file or directory: 'result/1.png'
➜  Desktop python test.py
297 447
447
9
➜  Desktop cd ~/Program/tensorflow-project 
➜  tensorflow-project git:(master) ✗ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   MNIST/validation.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   MNIST/mnist.py
	modified:   MNIST/validation.py

➜  tensorflow-project git:(master) ✗ git add -A
➜  tensorflow-project git:(master) ✗ git commit -m "New verification file"
[master 100688f] New verification file
 2 files changed, 131 insertions(+), 2 deletions(-)
 create mode 100644 MNIST/validation.py
➜  tensorflow-project git:(master) git push origin master 
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.26 KiB | 1.26 MiB/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
To https://github.com/lornatang/tensorflow-project.git
   8929059..100688f  master -> master
➜  tensorflow-project git:(master) git add -A                           
➜  tensorflow-project git:(master) ✗ git commit -m "change other file line"
[master f873f1e] change other file line
 1 file changed, 5 insertions(+), 5 deletions(-)
➜  tensorflow-project git:(master) git push origin master 
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 443 bytes | 443.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/lornatang/tensorflow-project.git
   100688f..f873f1e  master -> master
➜  tensorflow-project git:(master) git add -A                            
➜  tensorflow-project git:(master) ✗ git commit -m "change other file line"
[master 26fd56a] change other file line
 1 file changed, 3 insertions(+), 3 deletions(-)
➜  tensorflow-project git:(master) git push origin master                
\fatal: unable to access 'https://github.com/lornatang/tensorflow-project.git/': Couldn't connect to server
➜  tensorflow-project git:(master) git push origin master
fatal: unable to access 'https://github.com/lornatang/tensorflow-project.git/': Couldn't connect to server
➜  tensorflow-project git:(master) git push origin master
fatal: unable to access 'https://github.com/lornatang/tensorflow-project.git/': Couldn't connect to server
➜  tensorflow-project git:(master) git push origin master
fatal: unable to access 'https://github.com/lornatang/tensorflow-project.git/': Couldn't connect to server
➜  tensorflow-project git:(master) git push origin master
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 437 bytes | 437.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/lornatang/tensorflow-project.git
   f873f1e..26fd56a  master -> master
➜  tensorflow-project git:(master) git add -A                            
➜  tensorflow-project git:(master) ✗ git commit -m "change other file line"
[master 91119c7] change other file line
 2 files changed, 6 insertions(+), 6 deletions(-)
➜  tensorflow-project git:(master) git push origin master                
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 493 bytes | 493.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/lornatang/tensorflow-project.git
   26fd56a..91119c7  master -> master
➜  tensorflow-project git:(master) conda upgrade --all
Solving environment: | 
- 
done

## Package Plan ##

  environment location: /anaconda3


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    tqdm-4.25.0                |   py36h28b3542_0          58 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    twisted-17.5.0             |           py36_0         4.3 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
    conda-build-3.14.4         |           py36_0         452 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ------------------------------------------------------------
                                           Total:         4.8 MB

The following NEW packages will be INSTALLED:

    tqdm:        4.25.0-py36h28b3542_0 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main

The following packages will be UPDATED:

    conda-build: 3.14.2-py36_0         https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main --> 3.14.4-py36_0 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main

The following packages will be DOWNGRADED:

    twisted:     18.7.0-py36h1de35cc_1 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main --> 17.5.0-py36_0 https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free

Proceed ([y]/n)? 

Downloading and Extracting Packages
tqdm-4.25.0          | 58 KB     | ##################################### | 100% 
twisted-17.5.0       | 4.3 MB    | ##################################### | 100% 
conda-build-3.14.4   | 452 KB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
➜  tensorflow-project git:(master) 
➜  tensorflow-project git:(master) conda clean --all
Cache location: /anaconda3/pkgs
Will remove the following tarballs:

/anaconda3/pkgs
---------------
tqdm-4.25.0-py36h28b3542_0.tar.bz2            58 KB
conda-build-3.14.4-py36_0.tar.bz2            452 KB
twisted-17.5.0-py36_0.tar.bz2                4.3 MB

---------------------------------------------------
Total:                                       4.8 MB

Proceed ([y]/n)? y

Removed tqdm-4.25.0-py36h28b3542_0.tar.bz2
Removed conda-build-3.14.4-py36_0.tar.bz2
Removed twisted-17.5.0-py36_0.tar.bz2
Cache location: /anaconda3/pkgs
Will remove the following packages:
/anaconda3/pkgs
---------------

conda-build-3.14.2-py36_0                    1.7 MB
twisted-18.7.0-py36h1de35cc_1               23.4 MB

---------------------------------------------------
Total:                                      25.1 MB

Proceed ([y]/n)? y

removing conda-build-3.14.2-py36_0
removing twisted-18.7.0-py36h1de35cc_1
source cache (/anaconda3/conda-bld/src_cache)
Size:                                           0 B

git cache (/anaconda3/conda-bld/git_cache)
Size:                                           0 B

hg cache (/anaconda3/conda-bld/hg_cache)
Size:                                           0 B

svn cache (/anaconda3/conda-bld/svn_cache)
Size:                                           0 B

Total:                                          0 B
Proceed ([y]/n)? y

Removing /anaconda3/conda-bld/src_cache
Removing /anaconda3/conda-bld/git_cache
Removing /anaconda3/conda-bld/hg_cache
Removing /anaconda3/conda-bld/svn_cache
➜  tensorflow-project git:(master) cd ..
➜  Program ll
total 0
drwxr-xr-x  14 mac  staff   448B  9 11 17:35 100-Days-Of-ML-Code
drwxr-xr-x  11 mac  staff   352B  9 11 11:48 Extend_data
drwxr-xr-x  10 mac  staff   320B  9 11 15:35 models
drwxr-xr-x  16 mac  staff   512B  9 10 18:30 pytorch-project
drwxr-xr-x   9 mac  staff   288B  8 23 23:06 target_detection
drwxr-xr-x  14 mac  staff   448B  9 11 15:23 tensorflow-project
drwxr-xr-x  16 mac  staff   512B  9 11 17:27 tfmodels
➜  Program cd tfmodels 
➜  tfmodels git:(master) ll
total 64
-rw-r--r--   1 mac  staff   337B  9 11 17:27 AUTHORS
-rw-r--r--   1 mac  staff   2.5K  9 11 17:27 CODEOWNERS
-rw-r--r--   1 mac  staff   1.3K  9 11 17:27 CONTRIBUTING.md
-rw-r--r--   1 mac  staff   2.0K  9 11 17:27 ISSUE_TEMPLATE.md
-rw-r--r--   1 mac  staff    11K  9 11 17:27 LICENSE
-rw-r--r--   1 mac  staff   1.3K  9 11 17:27 README.md
-rw-r--r--   1 mac  staff     0B  9 11 17:27 WORKSPACE
drwxr-xr-x  18 mac  staff   576B  9 11 17:27 official
drwxr-xr-x  66 mac  staff   2.1K  9 11 17:27 research
drwxr-xr-x   6 mac  staff   192B  9 11 17:27 samples
drwxr-xr-x   7 mac  staff   224B  9 11 17:27 tutorials
➜  tfmodels git:(master) cd tutorials 
➜  tutorials git:(master) ll
total 8
-rw-r--r--   1 mac  staff   133B  9 11 17:27 README.md
-rw-r--r--   1 mac  staff     0B  9 11 17:27 __init__.py
drwxr-xr-x  10 mac  staff   320B  9 11 17:27 embedding
drwxr-xr-x   8 mac  staff   256B  9 11 17:27 image
drwxr-xr-x   7 mac  staff   224B  9 11 17:27 rnn
➜  tutorials git:(master) cd image 
➜  image git:(master) ll
total 0
-rw-r--r--   1 mac  staff     0B  9 11 17:27 __init__.py
drwxr-xr-x   5 mac  staff   160B  9 11 17:27 alexnet
drwxr-xr-x  11 mac  staff   352B  9 11 17:27 cifar10
drwxr-xr-x  11 mac  staff   352B  9 11 17:27 cifar10_estimator
drwxr-xr-x   4 mac  staff   128B  9 11 17:27 imagenet
drwxr-xr-x   5 mac  staff   160B  9 11 17:27 mnist
➜  image git:(master) cd alexnet 
➜  alexnet git:(master) ll
total 32
-rw-r--r--  1 mac  staff   504B  9 11 17:27 BUILD
-rw-r--r--  1 mac  staff     0B  9 11 17:27 __init__.py
-rw-r--r--  1 mac  staff   8.9K  9 11 17:27 alexnet_benchmark.py
➜  alexnet git:(master) vim alexnet_benchmark.py 
➜  alexnet git:(master) cd ..
➜  image git:(master) ll
total 0
-rw-r--r--   1 mac  staff     0B  9 11 17:27 __init__.py
drwxr-xr-x   5 mac  staff   160B  9 12 21:43 alexnet
drwxr-xr-x  11 mac  staff   352B  9 11 17:27 cifar10
drwxr-xr-x  11 mac  staff   352B  9 11 17:27 cifar10_estimator
drwxr-xr-x   4 mac  staff   128B  9 11 17:27 imagenet
drwxr-xr-x   5 mac  staff   160B  9 11 17:27 mnist
➜  image git:(master) cd cifar10_estimator 
➜  cifar10_estimator git:(master) ll
total 160
-rw-r--r--  1 mac  staff    26K  9 11 17:27 README.md
-rw-r--r--  1 mac  staff     0B  9 11 17:27 __init__.py
-rw-r--r--  1 mac  staff   3.7K  9 11 17:27 cifar10.py
-rw-r--r--  1 mac  staff    18K  9 11 17:27 cifar10_main.py
-rw-r--r--  1 mac  staff   2.7K  9 11 17:27 cifar10_model.py
-rw-r--r--  1 mac  staff   5.3K  9 11 17:27 cifar10_utils.py
-rw-r--r--  1 mac  staff   159B  9 11 17:27 cmle_config.yaml
-rw-r--r--  1 mac  staff   3.9K  9 11 17:27 generate_cifar10_tfrecords.py
-rw-r--r--  1 mac  staff   6.9K  9 11 17:27 model_base.py
➜  cifar10_estimator git:(master) vim README.md 
➜  cifar10_estimator git:(master) ll
total 160
-rw-r--r--  1 mac  staff    26K  9 12 21:45 README.md
-rw-r--r--  1 mac  staff     0B  9 11 17:27 __init__.py
-rw-r--r--  1 mac  staff   3.7K  9 11 17:27 cifar10.py
-rw-r--r--  1 mac  staff    18K  9 11 17:27 cifar10_main.py
-rw-r--r--  1 mac  staff   2.7K  9 11 17:27 cifar10_model.py
-rw-r--r--  1 mac  staff   5.3K  9 11 17:27 cifar10_utils.py
-rw-r--r--  1 mac  staff   159B  9 11 17:27 cmle_config.yaml
-rw-r--r--  1 mac  staff   3.9K  9 11 17:27 generate_cifar10_tfrecords.py
-rw-r--r--  1 mac  staff   6.9K  9 11 17:27 model_base.py
➜  cifar10_estimator git:(master) vim cifar10.py 
➜  cifar10_estimator git:(master) ll
total 160
-rw-r--r--  1 mac  staff    26K  9 12 21:45 README.md
-rw-r--r--  1 mac  staff     0B  9 11 17:27 __init__.py
-rw-r--r--  1 mac  staff   3.7K  9 12 21:46 cifar10.py
-rw-r--r--  1 mac  staff    18K  9 11 17:27 cifar10_main.py
-rw-r--r--  1 mac  staff   2.7K  9 11 17:27 cifar10_model.py
-rw-r--r--  1 mac  staff   5.3K  9 11 17:27 cifar10_utils.py
-rw-r--r--  1 mac  staff   159B  9 11 17:27 cmle_config.yaml
-rw-r--r--  1 mac  staff   3.9K  9 11 17:27 generate_cifar10_tfrecords.py
-rw-r--r--  1 mac  staff   6.9K  9 11 17:27 model_base.py
➜  cifar10_estimator git:(master) vim README.md 

  1 CIFAR-10 is a common benchmark in machine learning for image recognition.
  2 
  3 http://www.cs.toronto.edu/~kriz/cifar.html
  4 
  5 Code in this directory focuses on how to use TensorFlow Estimators to train     and
  6 evaluate a CIFAR-10 ResNet model on:
  7 
  8 * A single host with one CPU;
  9 * A single host with multiple GPUs;
 10 * Multiple hosts with CPU or multiple GPUs;
 11 
 12 Before trying to run the model we highly encourage you to read all the READM    E.
 13 
 14 ## Prerequisite
 15 
 16 1. [Install](https://www.tensorflow.org/install/) TensorFlow version 1.9.0 o    r
 17 later.
 18 
 19 2. Download the CIFAR-10 dataset and generate TFRecord files using the provi    ded
523 lines yanked
