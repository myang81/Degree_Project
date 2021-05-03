from flask import Blueprint, render_template, session, flash, redirect, request, url_for
from src.extension import db
from src.Models.Houses import House
from src.Utility import enumMachine
import math
import re
from time import time
import os
import json
from backend.src.Models.Targets import Targets

