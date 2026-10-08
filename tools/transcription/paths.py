"""Shared paths for the transcription tools.
Text (transcript/, verify/, final) lives in git under transcriptions/<name>/;
images are derived files and live in cache/transcription_<name>/images (not in git).
Select the transcription with the environment variable PQ_TRANSCRIPTION (default 1567)."""
import os
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAME = os.environ.get("PQ_TRANSCRIPTION", "1567")
TEXT = os.path.join(REPO, "transcriptions", NAME)
IMAGES = os.path.join(REPO, "cache", f"transcription_{NAME}", "images")
ZOOM = os.path.join(REPO, "cache", "zoom")
