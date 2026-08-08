#!/usr/bin/env node

interface ReputationInput {
  profile: string;
  profileType: string;
  reputationRisk: number;
  contentDiscovery: number;
  searchVisibility: number;
  urlAnalysis: number;
  removalFeasibility: number;
  monitoringCoverage: number;
}

interface ReputationOutput {
  profile: string;
  profileType: string;
  reputationRiskScore: number;
  contentDiscoveryScore: number;
  searchVisibilityScore: number;
  urlAnalysisScore: number;
  removalFeasibilityScore: number;
  monitoringCoverageScore: number;
  overallReputationIndex: number;
  priorityAction: string;
  reputationChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    reputationRisk: "Reputation Risk",
    contentDiscovery: "Content Discovery",
    searchVisibility: "Search Visibility",
    urlAnalysis: "URL Analysis",
    removalFeasibility: "Removal Feasibility",
    monitoringCoverage: "Monitoring Coverage",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getReputationChannels(search: number, content: number, monitor: number, url: number): Record<string, number> {
  return {
    "Google Search": Math.min(100, Math.round(search * 1.0)),
    "News & Media": Math.min(100, Math.round(content * 1.0)),
    "Social Platforms": Math.min(100, Math.round(monitor * 1.0)),
    "Review Sites": Math.min(100, Math.round(url * 1.0)),
  };
}

export function analyzeReputation(input: ReputationInput): ReputationOutput {
  const scores = {
    reputationRisk: input.reputationRisk,
    contentDiscovery: input.contentDiscovery,
    searchVisibility: input.searchVisibility,
    urlAnalysis: input.urlAnalysis,
    removalFeasibility: input.removalFeasibility,
    monitoringCoverage: input.monitoringCoverage,
  };
  const overallReputationIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    profile: input.profile,
    profileType: input.profileType.charAt(0).toUpperCase() + input.profileType.slice(1),
    reputationRiskScore: input.reputationRisk,
    contentDiscoveryScore: input.contentDiscovery,
    searchVisibilityScore: input.searchVisibility,
    urlAnalysisScore: input.urlAnalysis,
    removalFeasibilityScore: input.removalFeasibility,
    monitoringCoverageScore: input.monitoringCoverage,
    overallReputationIndex,
    priorityAction: getPriorityAction(scores),
    reputationChannels: getReputationChannels(input.searchVisibility, input.contentDiscovery, input.monitoringCoverage, input.urlAnalysis),
  };
}

const args = process.argv.slice(2);
const profile = args[0] || "brand-name";
const profileType = args[1] || "business";
const reputationRisk = parseInt(args[2]) || 85;
const contentDiscovery = parseInt(args[3]) || 78;
const searchVisibility = parseInt(args[4]) || 82;
const urlAnalysis = parseInt(args[5]) || 74;
const removalFeasibility = parseInt(args[6]) || 88;
const monitoringCoverage = parseInt(args[7]) || 80;

const result = analyzeReputation({
  profile, profileType, reputationRisk, contentDiscovery,
  searchVisibility, urlAnalysis, removalFeasibility, monitoringCoverage,
});

console.log(`Profile: ${result.profile}`);
console.log(`Profile Type: ${result.profileType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Reputation Risk Score:         ${result.reputationRiskScore}/100  [${getStatus(result.reputationRiskScore)}]`);
console.log(`Content Discovery Score:       ${result.contentDiscoveryScore}/100  [${getStatus(result.contentDiscoveryScore)}]`);
console.log(`Search Visibility Score:       ${result.searchVisibilityScore}/100  [${getStatus(result.searchVisibilityScore)}]`);
console.log(`URL Analysis Score:            ${result.urlAnalysisScore}/100  [${getStatus(result.urlAnalysisScore)}]`);
console.log(`Removal Feasibility Score:     ${result.removalFeasibilityScore}/100  [${getStatus(result.removalFeasibilityScore)}]`);
console.log(`Monitoring Coverage Score:     ${result.monitoringCoverageScore}/100  [${getStatus(result.monitoringCoverageScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Reputation Index:      ${result.overallReputationIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nReputation Channels:");
Object.entries(result.reputationChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(22)} ${score}/100`);
});
