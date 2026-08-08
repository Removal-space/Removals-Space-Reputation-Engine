#!/usr/bin/env python3
"""
Removals Space Reputation Engine
A digital reputation management and online content analysis tool designed
to help individuals, businesses, and digital professionals better understand
and manage their online visibility.

Framework: Discover → Analyse → Assess → Resolve → Monitor

https://removals.space
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "reputation_risk": "Reputation Risk",
        "content_discovery": "Content Discovery",
        "search_visibility": "Search Visibility",
        "url_analysis": "URL Analysis",
        "removal_feasibility": "Removal Feasibility",
        "monitoring_coverage": "Monitoring Coverage",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_reputation_channels(search: int, content: int, monitor: int, url: int) -> dict:
    return {
        "Google Search": min(100, round(search * 1.0)),
        "News & Media": min(100, round(content * 1.0)),
        "Social Platforms": min(100, round(monitor * 1.0)),
        "Review Sites": min(100, round(url * 1.0)),
    }


def analyze_reputation(
    profile: str,
    profile_type: str = "business",
    reputation_risk: int = 85,
    content_discovery: int = 78,
    search_visibility: int = 82,
    url_analysis: int = 74,
    removal_feasibility: int = 88,
    monitoring_coverage: int = 80,
) -> dict:
    """
    Analyze digital reputation management signals.

    Framework: Discover → Analyse → Assess → Resolve → Monitor

    Args:
        profile: Profile name or brand identifier
        profile_type: Type of profile being assessed
        reputation_risk: Reputation risk score (0-100)
        content_discovery: Content discovery score (0-100)
        search_visibility: Search visibility score (0-100)
        url_analysis: URL analysis score (0-100)
        removal_feasibility: Removal feasibility score (0-100)
        monitoring_coverage: Monitoring coverage score (0-100)

    Returns:
        dict with individual signal scores, overall reputation index,
        and reputation channel breakdown
    """
    scores = {
        "reputation_risk": reputation_risk,
        "content_discovery": content_discovery,
        "search_visibility": search_visibility,
        "url_analysis": url_analysis,
        "removal_feasibility": removal_feasibility,
        "monitoring_coverage": monitoring_coverage,
    }
    overall_reputation_index = round(sum(scores.values()) / 6)

    return {
        "profile": profile,
        "profile_type": profile_type.capitalize(),
        "reputation_risk_score": reputation_risk,
        "content_discovery_score": content_discovery,
        "search_visibility_score": search_visibility,
        "url_analysis_score": url_analysis,
        "removal_feasibility_score": removal_feasibility,
        "monitoring_coverage_score": monitoring_coverage,
        "overall_reputation_index": overall_reputation_index,
        "priority_action": get_priority_action(scores),
        "reputation_channels": get_reputation_channels(search_visibility, content_discovery, monitoring_coverage, url_analysis),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    profile = args[0] if len(args) > 0 else "brand-name"
    profile_type = args[1] if len(args) > 1 else "business"
    reputation_risk = int(args[2]) if len(args) > 2 else 85
    content_discovery = int(args[3]) if len(args) > 3 else 78
    search_visibility = int(args[4]) if len(args) > 4 else 82
    url_analysis = int(args[5]) if len(args) > 5 else 74
    removal_feasibility = int(args[6]) if len(args) > 6 else 88
    monitoring_coverage = int(args[7]) if len(args) > 7 else 80

    result = analyze_reputation(
        profile, profile_type, reputation_risk, content_discovery,
        search_visibility, url_analysis, removal_feasibility, monitoring_coverage
    )

    print(f"Profile: {result['profile']}")
    print(f"Profile Type: {result['profile_type']}")
    print("=" * 45)
    print(f"Reputation Risk Score:         {result['reputation_risk_score']}/100  [{get_status(result['reputation_risk_score'])}]")
    print(f"Content Discovery Score:       {result['content_discovery_score']}/100  [{get_status(result['content_discovery_score'])}]")
    print(f"Search Visibility Score:       {result['search_visibility_score']}/100  [{get_status(result['search_visibility_score'])}]")
    print(f"URL Analysis Score:            {result['url_analysis_score']}/100  [{get_status(result['url_analysis_score'])}]")
    print(f"Removal Feasibility Score:     {result['removal_feasibility_score']}/100  [{get_status(result['removal_feasibility_score'])}]")
    print(f"Monitoring Coverage Score:     {result['monitoring_coverage_score']}/100  [{get_status(result['monitoring_coverage_score'])}]")
    print("=" * 45)
    print(f"Overall Reputation Index:      {result['overall_reputation_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nReputation Channels:")
    for channel, score in result['reputation_channels'].items():
        print(f"  {channel:<24} {score}/100")


if __name__ == "__main__":
    main()
