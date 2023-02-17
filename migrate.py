from settings import engine, Base
import crud.models


def main():
    if not Base.metadata.tables.keys():
        Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
