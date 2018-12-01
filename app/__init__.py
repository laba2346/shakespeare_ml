from flask import Flask

app = (__name__, instance_relative_config=True)

from app import routes

app.config.from_object('config')
