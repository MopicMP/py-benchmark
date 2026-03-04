"""Tests for py-benchmark."""

import pytest
from py_benchmark import benchmark


class TestBenchmark:
    """Test suite for benchmark."""

    def test_basic(self):
        """Test basic usage."""
        result = benchmark("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            benchmark("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = benchmark(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
