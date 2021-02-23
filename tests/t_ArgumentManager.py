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

from sources.ArgumentManager import ArgumentManager


def test_needHelp_h_case():

    argman = ArgumentManager()

    argv = ['binary', '-h']

    assert argman.needHelp(argv) is True


def test_needHelp_help_case():

    argman = ArgumentManager()

    argv = ['binary', '--help']

    assert argman.needHelp(argv) is True


def test_needHelp_wrong_case():

    argman = ArgumentManager()

    argv = ['binary', 'no']

    assert argman.needHelp(argv) is False


def test_normal_case():

    argman = ArgumentManager()

    argv = ['./309pollution', '3', 'tests/deps/file.csv', '0', '2']

    assert argman.checkArgs(argv) != 84


def test_wrong_number_args(capsys):

    argman = ArgumentManager()

    argv = ['./309pollution', '3', 'tests/deps/file.csv', '0',]

    assert argman.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR - Wrong number of arguments.\n"


def test_n_not_int(capsys):

    argman = ArgumentManager()

    argv = ['./309pollution', 'a', 'tests/deps/file.csv', '0', '1']

    assert argman.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR - Wrong arguments type.\n"


def test_not_a_file(capsys):

    argman = ArgumentManager()

    argv = ['./309pollution', '0', 'WRONG FILE', '0', '0']

    assert argman.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR - WRONG FILE no such file.\n"


def test_x_not_int(capsys):

    argman = ArgumentManager()

    argv = ['./309pollution', '0', 'tests/deps/file.csv', 'a', '1']

    assert argman.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR - Wrong arguments type.\n"


def test_y_not_int(capsys):

    argman = ArgumentManager()

    argv = ['./309pollution', '0', 'tests/deps/file.csv', '0', 'a']

    assert argman.checkArgs(argv) == 84

    redir = capsys.readouterr()
    assert redir.out == "ERROR - Wrong arguments type.\n"
