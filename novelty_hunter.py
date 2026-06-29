"""
Project Autoscribe Engine — External Market Radar
Module: novelty_hunter.py
Specification Reference: ASC-005 (The Novelty Hunter Engine)
Runtime Environment: Pure Python 3.14+ (Zero-Dependency)
"""
import re
from typing import List, Dict

class NoveltyHunterEngine:
    def __init__(self):
        self.frustration_lexicon = {
            r"\b(bottleneck|overhead|starvation|stutter|jitter|crackling)\b": 8,
            r"\b(gdpr|compliance|minimisation|violation|audit|regulatory)\b": 10,
            r"\b(dependency|bloat|compilation|nightmare|failed|pip)\b": 6,
            r"\b(is there a way|how do i|why is there no|any workaround)\b": 4
        }
        self.compiled_lexicon = {re.compile(k, re.IGNORECASE): v for k, v in self.frustration_lexicon.items()}
        self.internal_capabilities = {
            "ASC-001": ["zero-dependency", "parser", "telemetry", "markdown"],
            "ASC-002": ["gdpr", "minimisation", "british english", "localisation", "normalisation"],
            "ASC-004": ["gap-analysis", "blind spot", "socratic", "omission"]
        }

    def generate_theia_request_headers(self) -> Dict[str, str]:
        return {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Accept": "application/json"}

    def format_target_url(self, base_forum_url: str) -> str:
        if not base_forum_url.endswith(".json") and "reddit.com" in base_forum_url:
            return f"{base_forum_url.rstrip('/')}/.json"
        return base_forum_url

    def ingest_and_score_signal(self, feed_source: str, raw_payload: str) -> Dict:
        velocity_score = 0
        triggered_markers = []
        suggested_assets = set()
        for pattern, points in self.compiled_lexicon.items():
            matches = pattern.findall(raw_payload)
            if matches:
                velocity_score += len(set(matches)) * points
                triggered_markers.extend(list(set(matches)))
        payload_lower = raw_payload.lower()
        for asset_id, keyword_list in self.internal_capabilities.items():
            for keyword in keyword_list:
                if keyword in payload_lower:
                    suggested_assets.add(asset_id)
                    velocity_score += 5
        classification = "LOW MARKET VELOCITY"
        if velocity_score > 35: classification = "HIGH MARKET PULL [DEPLOY DEFENSIVE PRIOR ART]"
        elif velocity_score > 15: classification = "VALIDATED PRODUCTISATION VECTOR"
        return {"source": feed_source, "velocity_score": velocity_score, "market_classification": classification, "detected_markers": list(set(triggered_markers)), "matched_capabilities": list(suggested_assets)}

if __name__ == "__main__":
    hunter = NoveltyHunterEngine()
    report = hunter.ingest_and_score_signal("Simulated_Feed", "Compilation nightmare with logging packages causing thread starvation.")
    print(f"Market Status: {report['market_classification']} | Score: {report['velocity_score']}")
