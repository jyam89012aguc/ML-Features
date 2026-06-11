# Financial Features — Feature Family Plan

## Sector context
Database: `C:\Users\jyama\Desktop\silver db\trading.duckdb`
- `sep` — daily OHLCV (closeadj, volume).
- `fundamentals` — quarterly financials. Note: `revenue` = interest+fee income for banks;
  `ebitda` less meaningful; `deposits` is bank-specific; `equity` = book value; `intangibles`
  = goodwill from M&A; `de` = leverage ratio; `bvps`/`fcfps`/`eps` standard.
- `tickers` — `sector='Financial Services'` covers Regional Banks (3,109), Asset Mgmt (595),
  Capital Markets (397), P&C Insurance (388), Credit Services (323), Life Insurance (220),
  Diversified Banks (188), Mortgage Finance (136), Specialty Insurance (114), Insurance
  Brokers (101), Reinsurance (47), Savings & Coop Banks (18). 5,751 tickers total.

## Investment thesis
Banks compound at 3–5x cycles; rare 10x outcomes. **Small banks & thrifts** are M&A-driven —
intangibles growth, asset acceleration, and tangible-book compounding are key signals.
**Specialty lenders** show occasional 10x via yield + asset growth on small base.
**Insurance** compounders are float-growth + underwriting durability + investment income.

50 families to maximize coverage across the heterogeneous financial sub-industries.

## File structure (mirrors other claude folders)
Per family folder `f##_<slug>/`:
1. `f##_<slug>_base_001_075_claude.py`  — 75 base features (v001…v075).
2. `f##_<slug>_base_076_150_claude.py`  — 75 base features (v076…v150).
3. `f##_<slug>_2nd_derivatives_001_150_claude.py` — 150 slope features.
4. `f##_<slug>_3rd_derivatives_001_150_claude.py` — 150 jerk features.

Total per family: 450. Grand total: 50 × 450 = **22,500 features**.

## 50 Financial feature families

### Bank fundamentals (1–10)
- f01 bank_asset_growth — loan-book / asset growth trajectory.
- f02 deposit_franchise_growth — deposit-base growth (via `deposits` column).
- f03 net_interest_margin_proxy — revenue / earning-asset proxy (revenue/assets).
- f04 bank_efficiency_ratio — sg&a / revenue dynamics.
- f05 loan_to_deposit_dynamics — debt / deposits cycle.
- f06 bank_capital_adequacy — equity / assets dynamics.
- f07 tangible_book_compound — (equity − intangibles) / shares trajectory.
- f08 bank_roe_compounding — ROE trajectory + persistence.
- f09 bank_credit_quality — earnings volatility (provisions proxy).
- f10 net_charge_off_proxy — netinc dispersion vs revenue.

### M&A / small-bank consolidation (11–15)
- f11 small_bank_acquisition_signature — intangibles + asset growth pulse.
- f12 ma_target_signature — undervaluation + small size composite.
- f13 ma_acquirer_signature — intangibles growth + asset jerk.
- f14 goodwill_intensity_cycle — intangibles / assets ratio cycle.
- f15 ma_consolidation_premium — sector consolidation pricing signal.

### Insurance — P&C / reinsurance (16–20)
- f16 insurance_float_growth — liabilities / equity (float proxy).
- f17 insurance_combined_ratio_proxy — opex / revenue.
- f18 insurance_investment_income — netinc vs revenue divergence.
- f19 insurance_underwriting_quality — margin durability.
- f20 reinsurance_cycle — cyclical pricing signal.

### Specialty lenders / credit (21–25)
- f21 specialty_lender_yield — revenue / assets for specialty finance.
- f22 consumer_finance_growth — asset growth signature.
- f23 commercial_lending_dynamics — debt cycle in commercial lending.
- f24 specialty_finance_quality — return durability for specialty.
- f25 nonbank_lender_signature — high growth + lighter regulation.

### Bank cycle / rate / credit (26–30)
- f26 interest_rate_sensitivity — revenue / assets dynamics through cycles.
- f27 credit_cycle_position — revenue vs provisions cycle.
- f28 deposit_beta_signature — funding-cost sensitivity proxy.
- f29 bank_loan_growth_cycle — asset acceleration cycle.
- f30 bank_distress_signature — leverage + ROA collapse risk.

### Capital allocation (31–35)
- f31 dividend_growth_bank — dividend compounding signal.
- f32 buyback_efficiency_bank — share count vs price dynamics.
- f33 capital_return_quality — dividend + buyback consistency.
- f34 reinvestment_to_growth — retained earnings deployment.
- f35 bank_payout_durability — payout ratio sustainability.

### Compounders & quality (36–40)
- f36 quiet_bank_compounder — low vol + steady book value growth.
- f37 community_bank_compounder — small bank + steady growth.
- f38 hidden_financial_compounder — undervalued financial signal.
- f39 specialty_finance_compounder — specialty lender quality.
- f40 financial_terminal_compounder — aggregate quality.

### Risk & earnings quality (41–45)
- f41 bank_earnings_quality — cash earnings vs accrual.
- f42 bank_balance_sheet_strength — equity coverage of liabilities.
- f43 leverage_risk_bank — asset / equity ratio dynamics.
- f44 nim_durability — revenue / asset stability.
- f45 fee_income_growth — revenue mix change (fee vs interest).

### Insurance & specialty extension (46–50)
- f46 insurance_premium_growth — revenue growth.
- f47 insurance_reserve_quality — liabilities / revenue.
- f48 insurance_market_cycle — cyclical underwriting signal.
- f49 financial_sector_relative — relative momentum.
- f50 financial_compounder_idiosyncratic — aggregate idiosyncratic composite.

## Parallel build plan
10 sub-agents (Batch A–J), each owns 5 families.
- A f01–f05, B f06–f10, C f11–f15, D f16–f20, E f21–f25,
- F f26–f30, G f31–f35, H f36–f40, I f41–f45, J f46–f50.

10 × 5 × 4 = **200 files**. 50 × 450 = **22,500 features**.
