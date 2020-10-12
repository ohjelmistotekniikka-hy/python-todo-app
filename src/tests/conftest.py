from build import build


def pytest_configure():
    build()
