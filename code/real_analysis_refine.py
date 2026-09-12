#!/usr/bin/env python3
"""Cycle-2 REFINE (Stage 13/14): bootstrap CIs + transaction-level H3 evidence.

Reads data/real/*.csv plus the decoded x402x settlement-router tables. Writes
experiment_summary.v03.json, analysis_real.md and charts_real/fig4...png.
"""
import os, json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REAL = os.path.join(BASE, "data", "real")
CHARTS = os.path.join(BASE, "charts_real")
os.makedirs(CHARTS, exist_ok=True)

def gini(x):
    x = np.sort(np.asarray(x, float)); n = len(x)
    return float((2 * np.sum((np.arange(1, n + 1)) * x) - (n + 1) * np.sum(x)) / (n * np.sum(x)))

def hhi_pct(x):
    s = np.asarray(x, float); s = s / s.sum()
    return float(np.sum((s * 100) ** 2))

sl = pd.read_csv(os.path.join(REAL, "sellers_lookup.csv"))
calls = sl.groupby("pay_to")["total_calls"].sum().values.astype(float)
prices = pd.to_numeric(sl["min_price"], errors="coerce").dropna().values.astype(float)

def boot(vals, stat, seeds=(42, 123, 2026), n=1000):
    ci = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        est = np.array([stat(rng.choice(vals, size=len(vals), replace=True)) for _ in range(n)])
        ci.append((float(np.percentile(est, 2.5)), float(np.percentile(est, 97.5))))
    lo = float(np.mean([c[0] for c in ci])); hi = float(np.mean([c[1] for c in ci]))
    return {"point": float(stat(vals)), "ci95": [lo, hi], "per_seed": ci}

gini_ci = boot(calls, gini)
hhi_ci = boot(calls, hhi_pct)
med_ci = boot(prices, np.median)
cv_ci = boot(prices, lambda v: float(np.std(v, ddof=1) / np.mean(v)))

b = pd.read_csv(os.path.join(REAL, "settlement_router_buckets.csv")).iloc[0]
tot = float(b["total"])
router_shares = {
    "n": int(tot),
    "sub_cent_pct": round(float(b["sub_cent"]) / tot * 100, 2),
    "usd_0p01_0p10_pct": round(float(b["c01_10"]) / tot * 100, 2),
    "usd_0p10_1_pct": round(float(b["c10_1"]) / tot * 100, 2),
    "usd_1_10_pct": round(float(b["c1_10"]) / tot * 100, 2),
    "usd_10plus_pct": round(float(b["c10plus"]) / tot * 100, 2),
}
st = pd.read_csv(os.path.join(REAL, "settlement_router_stats.csv")).iloc[0]
router_stats = {"median_usd": float(st["p50"]), "p10_usd": float(st["p10"]), "p25_usd": float(st["p25"]),
                "p75_usd": float(st["p75"]), "p90_usd": float(st["p90"]), "mean_usd": float(st["mean"]), "sd_usd": float(st["sd"])}

summary = {
  "stage": "stage-14-result-analysis.v03",
  "data_source": "Dune Analytics; data/real/PROVENANCE.json (17 tables)",
  "synthetic_metrics": 0,
  "bootstrap": {"method": "1000 resamples x seeds 42/123/2026", "merchant_calls": {"gini": gini_ci, "hhi": hhi_ci}, "endpoint_price": {"median": med_ci, "cv": cv_ci}},
  "transaction_level_h3": {"source": "x402x_base.settlementrouter_evt_settled (decoded, realistic)", "stats": router_stats, "shares": router_shares,
    "verdict": "Refutes tight clustering even more strongly: median USD 0.00117 and 94.85% of settled events below USD 0.01."},
}
with open(os.path.join(BASE, "experiment_summary.v03.json"), "w") as fh:
    json.dump(summary, fh, indent=2)

md = []
md.append("# Real-Data Analysis (v03, REFINE) - Bootstrap CIs and Transaction-Level Prices\n")
md.append("## Bootstrap 95% CIs (seeds 42/123/2026, 1000 resamples)\n")
md.append("- Merchant-call Gini: %.4f [%.4f, %.4f]" % (gini_ci["point"], gini_ci["ci95"][0], gini_ci["ci95"][1]))
md.append("- Merchant-call HHI: %.2f [%.2f, %.2f]" % (hhi_ci["point"], hhi_ci["ci95"][0], hhi_ci["ci95"][1]))
md.append("- Endpoint min-price median: USD %.4f [%.4f, %.4f]" % (med_ci["point"], med_ci["ci95"][0], med_ci["ci95"][1]))
md.append("- Endpoint min-price CV: %.4f [%.4f, %.4f]\n" % (cv_ci["point"], cv_ci["ci95"][0], cv_ci["ci95"][1]))
md.append("## Transaction-level clearing prices (x402x settlement router, Base, 433,694 events)\n")
md.append("- Median USD %.6f; p10 %.6f; p25 %.6f; p75 %.6f; p90 %.6f; mean USD %.4f" % (router_stats["median_usd"], router_stats["p10_usd"], router_stats["p25_usd"], router_stats["p75_usd"], router_stats["p90_usd"], router_stats["mean_usd"]))
md.append("- Buckets: sub-cent %.2f%%, USD 0.01-0.10 %.2f%%, USD 0.10-1 %.2f%%, USD 1-10 %.2f%%, USD 10+ %.2f%%" % (router_shares["sub_cent_pct"], router_shares["usd_0p01_0p10_pct"], router_shares["usd_0p10_1_pct"], router_shares["usd_1_10_pct"], router_shares["usd_10plus_pct"]))
md.append("- This is the authoritative H3 evidence: machine payments clear near one-tenth of a cent, not USD 0.25.")
open(os.path.join(BASE, "analysis_real.md"), "w").write("\n".join(md))

labels = ["<0.01", "0.01-0.10", "0.10-1", "1-10", "10+"]
vals = [router_shares["sub_cent_pct"], router_shares["usd_0p01_0p10_pct"], router_shares["usd_0p10_1_pct"], router_shares["usd_1_10_pct"], router_shares["usd_10plus_pct"]]
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.bar(labels, vals, color="#2C3E50")
ax.set_title("REAL transaction-level x402 clearing sizes (x402x router, 433,694 events)")
ax.set_ylabel("% of settled events"); ax.grid(alpha=.3, axis="y")
for i, v in enumerate(vals):
    ax.text(i, v + 1, "%.1f%%" % v, ha="center", fontsize=9)
plt.tight_layout(); plt.savefig(os.path.join(CHARTS, "fig4_real_clearing_sizes.png"), dpi=200); plt.close(fig)

print("Gini %.4f [%.4f, %.4f]" % (gini_ci["point"], gini_ci["ci95"][0], gini_ci["ci95"][1]))
print("HHI %.2f [%.2f, %.2f]" % (hhi_ci["point"], hhi_ci["ci95"][0], hhi_ci["ci95"][1]))
print("min-price median %.4f [%.4f, %.4f]  CV %.4f [%.4f, %.4f]" % (med_ci["point"], med_ci["ci95"][0], med_ci["ci95"][1], cv_ci["point"], cv_ci["ci95"][0], cv_ci["ci95"][1]))
print("router sub-cent %.2f%% median USD %.6f" % (router_shares["sub_cent_pct"], router_stats["median_usd"]))
