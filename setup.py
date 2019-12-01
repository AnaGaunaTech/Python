$ pip wheel --global-option bdist_ext --global-option -DFOO wheel
$ pip install --no-index --find-links=/tmp/wheelhouse SomePackage

# write the file
(shiny_new_env)$ pip freeze > requirements.txt

# show the contents
(shiny_new_env)$ cat requirements.txt

certifi==2018.10.15
chardet==3.0.4
Click==7.0
dash==0.30.0
dash-core-components==0.38.0
dash-html-components==0.13.2
dash-renderer==0.15.0
decorator==4.3.0
Flask==1.0.2
Flask-Compress==1.4.0
Flask-SQLAlchemy==2.3.2
idna==2.7
ipython-genutils==0.2.0
itsdangerous==1.1.0
Jinja2==2.10
jsonschema==2.6.0
jupyter-core==4.4.0
MarkupSafe==1.1.0
nbformat==4.4.0
numpy==1.15.4
pandas==0.22.0
plotly==3.4.1
python-dateutil==2.7.5
pytz==2018.7
requests==2.20.1
retrying==1.3.3
six==1.11.0
SQLAlchemy==1.2.14
traitlets==4.3.2
urllib3==1.24.1
Werkzeug==0.14.1
