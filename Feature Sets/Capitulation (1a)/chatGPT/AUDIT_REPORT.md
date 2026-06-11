# Comprehensive Feature Audit Report

## Summary Table

| Family Name | Total Fns | Duplicates | Errors | Constants | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 01_drawdown_depth | 200 | 160 | 0 | 0 | Success |
| 02_drawdown_duration | 200 | 160 | 0 | 0 | Success |
| 03_drawdown_shape | 200 | 160 | 0 | 0 | Success |
| 04_drawdown_velocity | 200 | 160 | 0 | 0 | Success |
| 05_underwater_curve | 200 | 160 | 0 | 0 | Success |
| 06_low_proximity | 200 | 160 | 0 | 0 | Success |
| 07_peak_to_trough | 200 | 160 | 0 | 0 | Success |
| 08_decline_streaks | 200 | 164 | 0 | 25 | Success |
| 09_price_compression | 200 | 164 | 0 | 25 | Success |
| 100_listing_status_risk | 200 | 79 | 0 | 3 | Success |
| 10_trough_clustering | 200 | 164 | 0 | 25 | Success |
| 11_decline_path_entropy | 200 | 164 | 0 | 25 | Success |
| 12_high_water_distance | 200 | 160 | 0 | 0 | Success |
| 13_drawdown_acceleration | 200 | 160 | 0 | 0 | Success |
| 14_recovery_failure | 200 | 160 | 0 | 0 | Success |
| 15_volume_blowoff | 200 | 160 | 0 | 0 | Success |
| 16_volume_persistence | 200 | 160 | 0 | 0 | Success |
| 17_volume_climax | 200 | 160 | 0 | 0 | Success |
| 18_volume_dryup | 200 | 160 | 0 | 0 | Success |
| 19_volume_trend | 200 | 160 | 0 | 0 | Success |
| 20_up_down_volume | 200 | 160 | 0 | 0 | Success |
| 21_volume_concentration | 200 | 160 | 0 | 0 | Success |
| 22_volume_price_divergence | 200 | 160 | 0 | 0 | Success |
| 23_dollar_volume_shock | 200 | 160 | 0 | 0 | Success |
| 24_volume_distribution | 200 | 160 | 0 | 0 | Success |
| 25_momentum_decay | 200 | 160 | 0 | 0 | Success |
| 26_rsi_extremes | 200 | 160 | 0 | 0 | Success |
| 27_momentum_exhaustion | 200 | 160 | 0 | 0 | Success |
| 28_return_distribution | 200 | 160 | 0 | 0 | Success |
| 29_consecutive_loss | 200 | 160 | 0 | 0 | Success |
| 30_relative_strength | 200 | 160 | 0 | 0 | Success |
| 31_oscillator_extremes | 200 | 160 | 0 | 0 | Success |
| 32_momentum_divergence | 200 | 160 | 0 | 0 | Success |
| 33_trend_breakdown | 200 | 160 | 0 | 0 | Success |
| 34_velocity_inflection | 200 | 160 | 0 | 0 | Success |
| 35_capitulation_thrust | 200 | 160 | 0 | 0 | Success |
| 36_volatility_spike | 200 | 160 | 0 | 0 | Success |
| 37_range_expansion | 200 | 160 | 0 | 0 | Success |
| 38_volatility_regime | 200 | 160 | 0 | 0 | Success |
| 39_intraday_range | 200 | 160 | 0 | 0 | Success |
| 40_close_location | 200 | 160 | 0 | 0 | Success |
| 41_range_compression | 200 | 160 | 0 | 0 | Success |
| 42_volatility_of_volatility | 200 | 160 | 0 | 0 | Success |
| 43_downside_deviation | 200 | 160 | 0 | 0 | Success |
| 44_atr_normalized_move | 200 | 160 | 0 | 0 | Success |
| 45_panic_bar_signatures | 200 | 160 | 0 | 0 | Success |
| 46_gap_structure | 200 | 160 | 0 | 0 | Success |
| 47_gap_down_clustering | 200 | 160 | 0 | 0 | Success |
| 48_open_close_dynamics | 200 | 160 | 0 | 0 | Success |
| 49_reversal_patterns | 200 | 160 | 0 | 0 | Success |
| 50_failed_breakdown | 200 | 160 | 0 | 0 | Success |
| 51_shadow_wick_analysis | 200 | 160 | 0 | 0 | Success |
| 52_bar_morphology | 200 | 160 | 0 | 0 | Success |
| 53_liquidity_collapse | 200 | 164 | 0 | 25 | Success |
| 54_turnover_ratio | 200 | 164 | 0 | 25 | Success |
| 55_price_level_distress | 200 | 164 | 0 | 25 | Success |
| 56_zero_volume_days | 200 | 164 | 0 | 25 | Success |
| 57_spread_proxy | 200 | 164 | 0 | 25 | Success |
| 58_trading_intensity | 200 | 164 | 0 | 25 | Success |
| 59_market_impact_proxy | 200 | 164 | 0 | 25 | Success |
| 60_earnings_collapse | 200 | 148 | 0 | 12 | Success |
| 61_revenue_deterioration | 200 | 148 | 0 | 12 | Success |
| 62_margin_compression | 200 | 148 | 0 | 12 | Success |
| 63_cash_burn | 200 | 148 | 0 | 12 | Success |
| 64_liquidity_distress | 200 | 148 | 0 | 12 | Success |
| 65_leverage_stress | 200 | 148 | 0 | 12 | Success |
| 66_interest_coverage | 200 | 148 | 0 | 12 | Success |
| 67_working_capital_drain | 200 | 148 | 0 | 12 | Success |
| 68_asset_quality | 200 | 148 | 0 | 12 | Success |
| 69_equity_erosion | 200 | 148 | 0 | 12 | Success |
| 70_dilution_acceleration | 200 | 148 | 0 | 12 | Success |
| 71_accruals_quality | 200 | 148 | 0 | 12 | Success |
| 72_solvency_scores | 200 | 148 | 0 | 12 | Success |
| 73_earnings_volatility | 200 | 148 | 0 | 12 | Success |
| 74_fundamental_momentum | 200 | 148 | 0 | 12 | Success |
| 75_guidance_distress | 200 | 148 | 0 | 12 | Success |
| 76_balance_sheet_decay | 200 | 148 | 0 | 12 | Success |
| 77_valuation_collapse | 200 | 66 | 0 | 0 | Success |
| 78_marketcap_destruction | 200 | 66 | 0 | 0 | Success |
| 79_ev_distortion | 200 | 66 | 0 | 0 | Success |
| 80_yield_distress | 200 | 66 | 0 | 0 | Success |
| 81_valuation_vs_history | 200 | 66 | 0 | 0 | Success |
| 82_valuation_vs_peers | 200 | 176 | 0 | 0 | Success |
| 83_insider_buy_cluster | 200 | 84 | 0 | 6 | Success |
| 84_insider_buy_size | 200 | 84 | 0 | 6 | Success |
| 85_insider_role_weight | 200 | 84 | 0 | 6 | Success |
| 86_insider_buy_sell_ratio | 200 | 84 | 0 | 6 | Success |
| 87_insider_timing | 200 | 84 | 0 | 6 | Success |
| 88_insider_transaction_freq | 200 | 84 | 0 | 6 | Success |
| 89_insider_conviction | 200 | 84 | 0 | 6 | Success |
| 90_insider_silence | 200 | 84 | 0 | 6 | Success |
| 91_institutional_exit | 200 | 0 | 200 | 0 | Success |
| 92_ownership_concentration | 200 | 0 | 200 | 0 | Success |
| 93_institutional_bottom_fish | 200 | 0 | 200 | 0 | Success |
| 94_holder_count_dynamics | 200 | 0 | 200 | 0 | Success |
| 95_forced_selling_proxy | 200 | 0 | 200 | 0 | Success |
| 96_dividend_distress | 200 | 79 | 0 | 3 | Success |
| 97_reverse_split_signal | 200 | 79 | 0 | 3 | Success |
| 98_corporate_event_density | 200 | 79 | 0 | 3 | Success |
| 99_going_concern_flags | 200 | 79 | 0 | 3 | Success |

## System-Wide Findings

- **Total Functions Audited**: 20000
- **Average Redundancy Rate**: 67.86%
- **Total Errors**: 1000
- **Total All-NaN Functions**: 0
- **Total Constant Functions**: 542
- **Families with Errors**: 91_institutional_exit, 92_ownership_concentration, 93_institutional_bottom_fish, 94_holder_count_dynamics, 95_forced_selling_proxy

## Actionable Recommendations

### Clean Families (Ready for deployment)
- None

### Mass-Bomb Redundant Families (Need consolidation)
- 01_drawdown_depth
- 02_drawdown_duration
- 03_drawdown_shape
- 04_drawdown_velocity
- 05_underwater_curve
- 06_low_proximity
- 07_peak_to_trough
- 08_decline_streaks
- 09_price_compression
- 10_trough_clustering
- 11_decline_path_entropy
- 12_high_water_distance
- 13_drawdown_acceleration
- 14_recovery_failure
- 15_volume_blowoff
- 16_volume_persistence
- 17_volume_climax
- 18_volume_dryup
- 19_volume_trend
- 20_up_down_volume
- 21_volume_concentration
- 22_volume_price_divergence
- 23_dollar_volume_shock
- 24_volume_distribution
- 25_momentum_decay
- 26_rsi_extremes
- 27_momentum_exhaustion
- 28_return_distribution
- 29_consecutive_loss
- 30_relative_strength
- 31_oscillator_extremes
- 32_momentum_divergence
- 33_trend_breakdown
- 34_velocity_inflection
- 35_capitulation_thrust
- 36_volatility_spike
- 37_range_expansion
- 38_volatility_regime
- 39_intraday_range
- 40_close_location
- 41_range_compression
- 42_volatility_of_volatility
- 43_downside_deviation
- 44_atr_normalized_move
- 45_panic_bar_signatures
- 46_gap_structure
- 47_gap_down_clustering
- 48_open_close_dynamics
- 49_reversal_patterns
- 50_failed_breakdown
- 51_shadow_wick_analysis
- 52_bar_morphology
- 53_liquidity_collapse
- 54_turnover_ratio
- 55_price_level_distress
- 56_zero_volume_days
- 57_spread_proxy
- 58_trading_intensity
- 59_market_impact_proxy
- 60_earnings_collapse
- 61_revenue_deterioration
- 62_margin_compression
- 63_cash_burn
- 64_liquidity_distress
- 65_leverage_stress
- 66_interest_coverage
- 67_working_capital_drain
- 68_asset_quality
- 69_equity_erosion
- 70_dilution_acceleration
- 71_accruals_quality
- 72_solvency_scores
- 73_earnings_volatility
- 74_fundamental_momentum
- 75_guidance_distress
- 76_balance_sheet_decay
- 82_valuation_vs_peers

### Surgical Fix Needed (Contain errors)
- 91_institutional_exit
- 92_ownership_concentration
- 93_institutional_bottom_fish
- 94_holder_count_dynamics
- 95_forced_selling_proxy
