from flask_assets import Environment, Bundle


assets = Environment()

css = Bundle('src/css/*.css', filters='cssmin', output='build/styles.min.css')

def init_app(app):
    assets.init_app(app)
    assets.register('main_css', css)
