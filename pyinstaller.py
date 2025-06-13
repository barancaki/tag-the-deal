import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--name=TagTheDeal',
    '--onefile',
    '--windowed',
    '--noconsole',
    '--icon=sorts.icns',
    '--add-data=driver:driver',
    '--add-data=web_functions:web_functions',
    '--add-data=chromedriver-mac/chromedriver'
])