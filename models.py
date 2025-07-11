"""
Database models for AI-powered Content Calendar Generator

This module defines comprehensive SQLAlchemy models for managing:
- Users and authentication
- Content calendar and posts
- Social media accounts and platforms
- AI-generated content and templates
- Analytics and performance tracking
- Team collaboration and workflows
- Campaign management
"""

from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, Dict, Any
import json

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import text
import uuid

db = SQLAlchemy()
