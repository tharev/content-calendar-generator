#!/usr/bin/env python3
"""
Content Calendar Generator - Configuration Management
====================================================
Comprehensive configuration management for the AI-powered content calendar
generator application with environment-based settings, security configurations,
and external service integrations.

Author: Content Calendar Generator Team
Version: 1.0.0
License: MIT
"""

import os
import logging
from datetime import timedelta
from typing import Dict, Any, Optional
from dataclasses import dataclass
from pathlib import Path

# Base directory for the application
BASE_DIR = Path(__file__).parent.absolute()


@dataclass
class DatabaseConfig:
    """Database configuration settings"""
