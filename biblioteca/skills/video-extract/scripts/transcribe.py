#!/usr/bin/env python3
"""Transcribe an audio/video file locally with faster-whisper. Offline, free, no API key.

Run it through uv so the dependency is fetched on demand and pinned to a Python
that has ctranslate2 wheels (3.12 is safe; 3.13/3.14 may not have wheels yet):

  uv run --python 3.12 --with faster-whisper python transcribe.py INPUT [opts]

INPUT can be anything ffmpeg can read (wav, mp3, webm, m4a, mp4, mkv ...). For best
speed give it a 16k mono wav, but it will decode other formats fine too.

Output: one timestamped phrase per line -> `[   start-     end] text`
Written to --out (default transcript.txt), and mirrored to stderr so you can watch
progress live (faster-whisper transcribes lazily as the generator is consumed).

For long or large files, launch this in the BACKGROUND and read the output file as it
grows -- transcription of ~11 min audio with the `small` model is a couple of minutes
on CPU, `medium` is several, `large-v3` can be 10+.
"""
import argparse
import sys

from faster_whisper import WhisperModel


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", help="audio or video file")
    ap.add_argument(
        "--model",
        default="small",
        help="tiny|base|small|medium|large-v3 . Bigger = more accurate but slower. "
        "small is a good default for understanding content; bump to medium/large-v3 "
        "when exact wording matters (names, numbers, non-English).",
    )
    ap.add_argument(
        "--lang",
        default=None,
        help="ISO code (tr, pt, en, es ...). Omit to auto-detect (printed to stderr).",
    )
    ap.add_argument("--out", default="transcript.txt")
    ap.add_argument(
        "--compute",
        default="int8",
        help="int8 for CPU (default), float16 for GPU.",
    )
    ap.add_argument("--device", default="cpu", help="cpu (default) or cuda")
    args = ap.parse_args()

    model = WhisperModel(args.model, device=args.device, compute_type=args.compute)
    segments, info = model.transcribe(
        args.input,
        language=args.lang,
        vad_filter=True,  # drop long silences -> cleaner segments, fewer hallucinations
        vad_parameters=dict(min_silence_duration_ms=500),
    )
    print(
        f"lang={info.language} prob={info.language_probability:.2f} model={args.model}",
        file=sys.stderr,
        flush=True,
    )
    with open(args.out, "w", encoding="utf-8") as f:
        for s in segments:
            line = f"[{s.start:8.2f}-{s.end:8.2f}] {s.text.strip()}"
            f.write(line + "\n")
            f.flush()
            print(line, file=sys.stderr, flush=True)
    print("DONE", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
