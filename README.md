# EzCompiler

## list of languages supported:

- Python 3
- Python 2
- C++
- C
- C#
- .NET
- Ruby
- MySQL
- Java (v8 and v16)
- JavaScript
- jQuery
- HTML and CSS

## resources:

- https://drive.google.com/file/d/1qy4i_7nsEActewD0w1-eTBvkmt9FL5KA/view?usp=sharing
- gdown https://drive.google.com/uc?id=1qy4i_7nsEActewD0w1-eTBvkmt9FL5KA

## INSTALLATION STEPS

- donwload and unzip the resources file in the project root
- Open mysql and specify the username and password in the file:

  - `resources/app_home/db_config/db_config.cnf`
  - You can also sepcify another db/schema if you want and the create it it in the mysql server/workbench
- python manage.py makemigrations app_home
- python manage.py migrate
- Copy the __static one directory above and do:__

  - python manage.py collectstatic and then type __yes__
- python manage.py runserver `<ipaddr>:<port>`
- `http://localhost:<port>`

## REFERENCES

- https://codemirror.net/
- https://github.com/microsoft/monaco-editor
- https://github.com/codex-team/editor.js
- https://ckeditor.com/cke4/addon/pbckcode
- https://ckeditor.com/docs/ckeditor5/latest/installation/index.html
- https://highlightjs.org/
- https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md
