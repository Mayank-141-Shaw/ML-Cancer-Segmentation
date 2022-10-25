from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import json

from model_definition import SegmentationModel