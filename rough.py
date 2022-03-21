# Imports
import time
from azure.storage.blob import BlockBlobService, BlobPermissions
import os
import time
import sys

import itertools
import json
import csv
import numpy as np
import re
import requests
import subprocess as sp
import pandas as pd
import pathlib
import hashlib
import traceback
from datetime import date, datetime, timedelta

from pyspark.ml.linalg import SparseVector, VectorUDT, Vectors, DenseVector 
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col
from pyspark.sql import functions as F, types as T, Row
from itertools import chain