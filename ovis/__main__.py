'''
Workaround for running Streamlit app as a console script from python package

Adopted from https://github.com/streamlit/streamlit/issues/5471#issuecomment-1341051365
'''

import sys, os, runpy
from ovis import app


def main() -> None:
    streamlit_script_path = os.path.join(os.path.dirname(app.__file__), 'main.py')
    sys.argv = ['streamlit', 'run', streamlit_script_path]
    runpy.run_module('streamlit', run_name = '__main__')


if __name__ == '__main__':
    
    main()


