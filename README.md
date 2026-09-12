# Sub-Dollar Machine Commerce: A Census-Scale Analysis of Real x402 On-Chain Payments

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22726373.svg)](https://doi.org/10.5281/zenodo.22726373)

**Authors:** Oscar Underwood, Roman Kurnovskii

**Artifact repository:** https://github.com/romankurnovskii/rnd-2026-sub-dollar-machine-commerce (private)  
**Zenodo Permanent Record:** https://doi.org/10.5281/zenodo.22726373  
**Paper:** Sub-Dollar Machine Commerce: A Census-Scale Analysis of Real x402 On-Chain Payments

## Abstract

Autonomous software agents are increasingly transacting over the HTTP 402 (x402) protocol, yet the empirical economics of machine-to-machine commerce remain largely uncharacterized. The prevailing industry narrative assumes a migration toward multi-dollar, compound transactions. To test this, we analyzed a census-scale dataset of 143.8 million x402 settlements—totaling $42.8M across Base, Solana, and Polygon (May–Dec 2025)—and found the exact opposite.

Our analysis reveals three structural realities of the machine economy:

- **The Sub-Dollar Reality:** Machine commerce is overwhelmingly micropayment-driven. The volume-weighted average payment is just $0.27, and 28.5% of all transactions are sub-cent. Payments ≥$1 carry 72.5% of the total value but represent less than 8% of network traffic.
- **Extreme Centralization:** The top 1% of merchants capture 93.0% of all revenue. This bottleneck is even more pronounced at the settlement infrastructure layer, where a single facilitator controls ~62% of the total settled volume.
- **Wild Price Dispersion & Network Dominance:** Endpoint list prices are highly erratic (median $0.01, CV 12.91), decisively rejecting the hypothesis of a tight, efficient algorithmic clearing corridor. Furthermore, settlement is highly skewed toward Base (82.5% of volume), with Solana holding a persistent minority (17.4%).

These findings dismantle the myth of complex machine commerce, reframing the x402 ecosystem as a high-volume, sub-dollar API economy where the true concentration risk lies in settlement infrastructure, rather than among merchants.

## Citation

If you use this artifact, please cite the paper and this repository:

```bibtex
@misc{underwood2026subdollar,
  title = {Sub-Dollar Machine Commerce: A Census-Scale Analysis of Real x402 On-Chain Payments},
  author = {Oscar Underwood and Roman Kurnovskii},
  year = {2026},
  doi = {10.5281/zenodo.22726373},
  url = {https://doi.org/10.5281/zenodo.22726373}
}
```

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
