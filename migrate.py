from config.settings import engine, Base
import config.models


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
