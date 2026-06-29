"""
Project Autoscribe Engine — Intellectual Property Extension
Module: novelty_assessor.py
Specification Reference: ASC-003 (The Innovation Delta Engine)
Runtime: Pure Python 3.14+ (Zero-Dependency)
"""
import re
from typing import Dict, List, Set

class InnovationDeltaEngine:
    def __init__(self):
        self.established_lexicon: Set[str] = {
            "winmm", "midi", "loopback", "telemetry", "markdown", 
            "parser", "diff", "repository", "thread", "asio"
        }
        self.ip_indicators = [
            r"\b(protocol|framework|engine|matrix|wrapper|daemon|layer|sdk)\b",
            r"\b(polymorphic|autonomous|decoupled|stateless|isolated|sovereign)\b",
            r"\b(arbitrage|cascade|leverage|tier|monetise|licence|proprietary)\b"
        ]
        self.compiled_indicators = [re.compile(p, re.IGNORECASE) for p in self.ip_indicators]

    def _extract_novel_tokens(self, text_payload: str) -> List[str]:
        words = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]{5,}\b", text_payload)
        return [w for w in set(words) if w.lower() not in self.established_lexicon and len(w) > 6 and not w.startswith("__")]

    def evaluate_session_novelty(self, session_diff_text: str) -> Dict:
        score = 0
        detected_indicators = []
        for pattern in self.compiled_indicators:
            matches = pattern.findall(session_diff_text)
            if matches:
                score += len(set(matches)) * 5
                detected_indicators.extend(list(set(matches)))
        novel_tokens = self._extract_novel_tokens(session_diff_text)
        score += len(novel_tokens) * 3
        classification = "INCREMENTAL UPDATE"
        if score > 40: classification = "CORE PROTOCOL BREAKTHROUGH [HIGH PATENT POTENTIAL]"
        elif score > 15: classification = "DERIVATIVE PLATFORM STYLE [PRODUCTISABLE ASSET]"
        return {"innovation_score": score, "asset_classification": classification, "conceptual_tokens": novel_tokens, "structural_markers": list(set(detected_indicators))}

if __name__ == "__main__":
    assessor = InnovationDeltaEngine()
    analysis = assessor.evaluate_session_novelty("+ Initialised the Polymorphic Localisation Layer. + Leveraged a validation cascade to isolate states.")
    print(f"Asset Class: {analysis['asset_classification']} | Score: {analysis['innovation_score']}")
