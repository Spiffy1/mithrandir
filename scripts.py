from subprocess import check_call


def lint() -> None:
    check_call(["flake8", "mithrandir/"])
    check_call(["pylint", "mithrandir/", "--rcfile=setup.cfg"])
    check_call(["autopep8", "mithrandir/*.py"])


def test() -> None:
    check_call(
        [
            "pytest",
            "tests",
            "--maxfail=1",
            "--verbose",
            "-s",
            # "--fulltrace",
            "--cov-report",
            "html",
            "--cov=mithrandir",
        ]
    )
