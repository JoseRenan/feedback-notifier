from fnotifier.factory import create_app

if __name__ == '__main__':
    app = create_app(__name__).run()
