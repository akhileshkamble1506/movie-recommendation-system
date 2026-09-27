import pickle
import numpy as np
import os

print("Loading similarity.pkl...")

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

similarity = np.asarray(similarity)

print("Original shape:", similarity.shape)
print("Original dtype:", similarity.dtype)

# Convert float64 -> float32
similarity = similarity.astype(np.float32)

with open("similarity.pkl", "wb") as f:
    pickle.dump(
        similarity,
        f,
        protocol=pickle.HIGHEST_PROTOCOL
    )

size_mb = os.path.getsize("similarity.pkl") / (1024 * 1024)

print("New dtype:", similarity.dtype)
print(f"New file size: {size_mb:.2f} MB")
print("Done!")