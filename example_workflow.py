#!/usr/bin/env python3
"""
Example Workflow for AI-Powered Content Calendar Generator

This script demonstrates comprehensive usage of the content calendar generator
including AI content creation, social media scheduling, analytics tracking,
and team collaboration workflows.

Run this script to see the full capabilities of the system:
    python example_workflow.py
"""

import asyncio
import os
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Any
import json

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from models import (
    db, User, Team, SocialAccount, ContentPost, ContentTemplate,
    Campaign, PostAnalytics, AIGenerationLog, SocialPlatform,
    ContentType, PostStatus, UserRole, CampaignStatus
