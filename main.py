from common.settings import Settings

settings = Settings()

if settings.mode == "host":
    import host

elif settings.mode == "test":
    import test

