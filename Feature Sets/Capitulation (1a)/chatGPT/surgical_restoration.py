import os
import re

def fix_family(family_dir):
    files = [f for f in os.listdir(family_dir) if f.endswith('.py') and ('derivatives' in f)]
    for file in files:
        path = os.path.join(family_dir, file)
        with open(path, 'r') as f:
            content = f.read()

        # Find all function definitions in derivatives
        # def name(input1, input2):
        # We look for inputs that look like polluted base functions: [a-z]{2,4}_[0-9]{3}_.*_[0-9]{3}
        
        def replacement(match):
            func_name = match.group(1)
            inputs_str = match.group(2)
            inputs = [i.strip() for i in inputs_str.split(',')]
            new_inputs = []
            for inp in inputs:
                # Check if it matches the polluted pattern
                # iex_001_holder_exit_1_001
                # dstk_001_amihud_illiquidity_5_001
                m = re.match(r'^([a-z]{2,4}_[0-9]{3}_)(.*)(_[0-9]+_[0-9]{3})$', inp)
                if m:
                    raw_input = m.group(2)
                    # Handle some common cases where raw_input might still have a window
                    # e.g. amihud_illiquidity_5 -> amihud_illiquidity
                    raw_input = re.sub(r'_[0-9]+$', '', raw_input)
                    new_inputs.append(raw_input)
                else:
                    new_inputs.append(inp)
            
            return f"def {func_name}({', '.join(new_inputs)}):"

        # Update function signatures
        new_content = re.sub(r'def\s+([a-zA-Z0-9_]+)\(([^)]+)\):', replacement, content)
        
        # Update function bodies where the old inputs were used
        # feature = _s(dstk_001_amihud_illiquidity_5_001)
        def body_replacement(match):
            old_inp = match.group(1)
            m = re.match(r'^([a-z]{2,4}_[0-9]{3}_)(.*)(_[0-9]+_[0-9]{3})$', old_inp)
            if m:
                raw_input = m.group(2)
                raw_input = re.sub(r'_[0-9]+$', '', raw_input)
                return raw_input
            return old_inp

        new_content = re.sub(r'([a-z]{2,4}_[0-9]{3}_[a-zA-Z0-9_]+_[0-9]{3})', body_replacement, new_content)

        # Update _REGISTRY
        # 'inputs': ['dstk_001_amihud_illiquidity_5_001']
        def registry_replacement(match):
            old_inp = match.group(1)
            m = re.match(r'^([a-z]{2,4}_[0-9]{3}_)(.*)(_[0-9]+_[0-9]{3})$', old_inp)
            if m:
                raw_input = m.group(2)
                raw_input = re.sub(r'_[0-9]+$', '', raw_input)
                return f"'{raw_input}'"
            return f"'{old_inp}'"

        new_content = re.sub(r"'([a-z]{2,4}_[0-9]{3}_[a-zA-Z0-9_]+_[0-9]{3})'", registry_replacement, new_content)

        if new_content != content:
            with open(path, 'w') as f:
                f.write(new_content)
            print(f"Updated {path}")

# List of families from audit report with errors
families_with_errors = [
    "08_decline_streaks", "09_price_compression", "10_trough_clustering", "11_decline_path_entropy",
    "25_momentum_decay", "26_rsi_extremes", "27_momentum_exhaustion", "28_return_distribution",
    "29_consecutive_loss", "30_relative_strength", "31_oscillator_extremes", "32_momentum_divergence",
    "33_trend_breakdown", "34_velocity_inflection", "35_capitulation_thrust", "36_volatility_spike",
    "37_range_expansion", "38_volatility_regime", "39_intraday_range", "40_close_location",
    "41_range_compression", "42_volatility_of_volatility", "43_downside_deviation", "44_atr_normalized_move",
    "45_panic_bar_signatures", "53_liquidity_collapse", "54_turnover_ratio", "55_price_level_distress",
    "56_zero_volume_days", "57_spread_proxy", "58_trading_intensity", "59_market_impact_proxy",
    "60_earnings_collapse", "61_revenue_deterioration", "62_margin_compression", "63_cash_burn",
    "64_liquidity_distress", "65_leverage_stress", "66_interest_coverage", "67_working_capital_drain",
    "68_asset_quality", "69_equity_erosion", "70_dilution_acceleration", "71_accruals_quality",
    "72_solvency_scores", "73_earnings_volatility", "74_fundamental_momentum", "75_guidance_distress",
    "76_balance_sheet_decay", "83_insider_buy_cluster", "84_insider_buy_size", "85_insider_role_weight",
    "86_insider_buy_sell_ratio", "87_insider_timing", "88_insider_transaction_freq", "89_insider_conviction",
    "90_insider_silence", "91_institutional_exit", "92_ownership_concentration", "93_institutional_bottom_fish",
    "95_forced_selling_proxy", "96_dividend_distress", "97_reverse_split_signal", "98_corporate_event_density",
    "99_going_concern_flags", "100_listing_status_risk"
]

for family in families_with_errors:
    if os.path.isdir(family):
        fix_family(family)
