import numpy as np
import os
from backend.utils.common import shannon_entropy

class AttachmentFeatureExtractor:
    def extract(self, filenames):
        features = []
        for f in filenames:
            features.append(self._extract_single(f))
        return np.array(features)

    def _extract_single(self, filename):
        return [
            len(filename),
            filename.count('.'),
            shannon_entropy(filename),
            self._is_suspicious_extension(filename)
        ]

    def _is_suspicious_extension(self, filename):
        suspicious = ['exe', 'js', 'bat', 'scr', 'vbs', 'zip']
        ext = filename.split('.')[-1].lower()
        return int(ext in suspicious)