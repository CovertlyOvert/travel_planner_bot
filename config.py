# config.py
import os

# Prefer a lighter, highly-available model; override per env when needed.
GENAI_MODEL_PRIMARY = os.getenv("GENAI_MODEL_PRIMARY", "gemini-2.0-flash-lite")
GENAI_MODEL_FALLBACK = os.getenv("GENAI_MODEL_FALLBACK", "gemini-2.0-flash")
