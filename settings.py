import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ETH = os.environ.get("ETH_KEY")
POL = os.environ.get("POL_KEY")
GNO = os.environ.get("GNO_KEY")
SDN = os.environ.get("SDN_KEY")
