#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `database` module."""

import pytest
import os
import sqlite3
from packit_app.database import Database


def test_database_connection():
    db = Database()
    assert type(db.cur) is sqlite3.Cursor
    assert type(db.connection) is sqlite3.Connection
    assert os.path.exists(Database.db_location) is True


def test_database_disconnects():
    db = Database()
    db.close_connection()
    with pytest.raises(sqlite3.ProgrammingError):
        db.cur.execute("CREATE TABLE cannot_not_be_created")
