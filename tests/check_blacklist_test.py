from pre_commit_hook.check_blacklist import check_blacklist

test_dir = '~/tests/'


def test_empty_blacklist():
    filepath = test_dir.join('test.txt')
    retv = check_blacklist([filepath])
    assert retv == 0


def test_single_file_equals_blacklist():
    """
    The one file being modified is the one file
    in the blacklist
    """
    filepath = test_dir.join('test.txt')
    retv = check_blacklist([filepath])
    assert retv == 1


def test_single_file_in_blacklist():
    """
    The single modified file is one of the several files
    specified in the blacklist
    """
    filepath = test_dir.join('test.txt')
    retv = check_blacklist([filepath])
    assert retv == 1


def test_partial_file_in_blacklist():
    """
    One of the modified files is listed in the
    blacklist
    """
    filepath = test_dir.join('test.txt')
    retv = check_blacklist([filepath])
    assert retv == 1
