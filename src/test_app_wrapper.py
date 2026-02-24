"""Wrapper to run app with mongomock"""
import sys
import mongomock

# Patch pymongo with mongomock
sys.modules['pymongo'] = mongomock

# Now import the real app
from app import app

# Export the app so uvicorn can use it
__all__ = ['app']
