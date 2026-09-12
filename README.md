# Sub-Dollar Machine Commerce: A Census-Scale Analysis of Real x402 On-Chain Payments

**Authors:** Oscar Underwood, Roman Kurnovskii

**Artifact repository:** https://github.com/romankurnovskii/rnd-2026-sub-dollar-machine-commerce (private)
**Paper:** Sub-Dollar Machine Commerce: A Census-Scale Analysis of Real x402 On-Chain Payments

## Abstract

Autonomous software agents increasingly pay for API calls and compute over the HTTP 402 (x402) payment protocol, yet the empirical economics of these machine payments remain poorly characterised. We analyse a census-scale extract of real x402 settlement activity assembled from public Dune Analytics tables: 143,785,721 transactions and USD 42,818,828.87 of settled value across Base, Solana and Polygon between May and December 2025. Contrary to the prevailing narrative that machine commerce has migrated to multi-dollar compound transactions, we find that x402 remains micropayment-dominated. The volume-weighted average payment is USD 0.2717, sub-cent payments are 28.50% of all payments, and payments of USD 1 or more are only 7.96% of transaction count (though they carry 72.45% of value). Merchant revenue is highly concentrated: the top 1% of 12,065 merchants receives 93.0% of revenue. Concentration is even more pronounced at the settlement-infrastructure layer, where the monthly facilitator Herfindahl-Hirschman index ranges from 3,426 to 8,994 and a single facilitator accounts for roughly 62% of settled volume. Endpoint list prices are highly dispersed (median USD 0.0100, coefficient of variation 12.91), and a decoded transaction-level source confirms this directly: across 433,694 settled events the median payment is USD 0.001173 and 94.85% are below USD 0.01. This rejects the hypothesis of a tight algorithmic clearing corridor. Settlement is Base-dominant (82.55% of volume) with Solana a persistent minority (17.44%). These results reframe machine commerce as a high-volume, sub-dollar API economy whose principal concentration risk lies in the facilitator layer rather than among merchants.

## Citation

If you use this artifact, please cite the paper and this repository:

`bibtex
@misc{rnd-2026-sub-dollar-machine-commerce,
  title = {Sub-Dollar Machine Commerce: A Census-Scale Analysis of Real x402 On-Chain Payments},
  author = {Oscar Underwood and Roman Kurnovskii},
  year = {2026},
  url = {https://github.com/romankurnovskii/rnd-2026-sub-dollar-machine-commerce}
}
`

Machine-readable metadata: see [CITATION.cff](./CITATION.cff).

## Contents

| Path | Description |
|---|---|
| `code/` | Reproducibility scripts that generate the results |
| `data/` | Input and derived datasets needed to reproduce the results |
| `figures/` | Generated figures |


## Reproducing the results

1. Clone this repository.
2. Run the scripts in `code/` (their headers document the inputs under `data/`).
3. Compare the regenerated tables and figures with those reported in the paper.

## Data

Input and derived datasets are provided under `data/`. Larger raw upstream
extracts, when not redistributed here, are referenced in the paper's Data
Availability statement.

## Licenses

- Code: [MIT](./LICENSE)
- Data and figures: [CC BY 4.0](./LICENSE-DATA)

This repository is **private** until the paper is accepted.
