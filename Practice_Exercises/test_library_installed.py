
libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "scipy",
    "sklearn",
    "jupyter",
    "torch",
    "torchvision",
    "torchaudio",
    "transformers",
    "datasets",
    "sentence_transformers",
    "umap",
]

for library in libraries:
    try:
        __import__(library)
        print(f"✅ {library}")
    except Exception as e:
        print(f"❌ {library}: {e}")