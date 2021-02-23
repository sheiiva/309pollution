############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 309pollution         #
#                                          #
############################################

import pytest

from sources.Pollution import Pollution


def test_normal_case(capsys):

    # Set
    argv = ['./309pollution', '3', 'tests/deps/file.csv', '0', '2']
    # Run
    argman = Pollution().run(argv)
    # Test
    redir = capsys.readouterr()
    assert redir.out == "0.00\n"


def test_normal_case2(capsys):

    # Set
    argv = ['./309pollution', '3', 'tests/deps/file.csv', '0.6', '2']
    # Run
    argman = Pollution().run(argv)
    # Test
    redir = capsys.readouterr()
    assert redir.out == "28.20\n"


def test_normal_case3(capsys):

    # Set
    argv = ['./309pollution', '3', 'tests/deps/file.csv', '1.3', '2']
    # Run
    argman = Pollution().run(argv)
    # Test
    redir = capsys.readouterr()
    assert redir.out == "56.55\n"


def test_normal_case4(capsys):

    # Set
    argv = ['./309pollution', '3', 'tests/deps/file.csv', '1', '1.5']
    # Run
    argman = Pollution().run(argv)
    # Test
    redir = capsys.readouterr()
    assert redir.out == "33.94\n"


def test_normal_case5(capsys):

    # Set
    argv = ['./309pollution', '3', 'tests/deps/file.csv', '0.8', '0.8']
    # Run
    argman = Pollution().run(argv)
    # Test
    redir = capsys.readouterr()
    assert redir.out == "26.11\n"
