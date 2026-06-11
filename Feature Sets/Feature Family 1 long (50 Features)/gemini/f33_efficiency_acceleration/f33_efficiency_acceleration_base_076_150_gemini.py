import pandas as pd
import numpy as np

def _ea_ratio(num, den):
    return num / den.replace(0, np.nan)

def _ea_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _ea_z(s, w):
    return (s - s.rolling(w, min_periods=min(w, 10)).mean()) / s.rolling(w, min_periods=min(w, 10)).std().replace(0, np.nan)

# F33 Efficiency Acceleration - Base v076 to v150

def f33_efficiency_acceleration_op_margin_accel_5d_21d_base_v076_signal(opinc, revenue) -> pd.Series:
    """Acceleration of Operating Margin over 5d and 21d."""
    ratio = _ea_ratio(opinc, revenue)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_21d_63d_base_v077_signal(opinc, revenue) -> pd.Series:
    """Acceleration of Operating Margin over 21d and 63d."""
    ratio = _ea_ratio(opinc, revenue)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_5d_21d_base_v078_signal(revenue, cogs) -> pd.Series:
    """Acceleration of Gross Margin (approx Rev/Cogs) over 5d and 21d."""
    ratio = _ea_ratio(revenue, cogs)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_21d_63d_base_v079_signal(revenue, cogs) -> pd.Series:
    """Acceleration of Gross Margin over 21d and 63d."""
    ratio = _ea_ratio(revenue, cogs)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_5d_21d_base_v080_signal(inventory, cogs) -> pd.Series:
    """Acceleration of Days Sales in Inventory (Inv/Cogs) over 5d and 21d."""
    ratio = _ea_ratio(inventory, cogs)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_21d_63d_base_v081_signal(inventory, cogs) -> pd.Series:
    """Acceleration of Days Sales in Inventory over 21d and 63d."""
    ratio = _ea_ratio(inventory, cogs)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_5d_21d_base_v082_signal(receivables, revenue) -> pd.Series:
    """Acceleration of Days Sales Outstanding (Rec/Rev) over 5d and 21d."""
    ratio = _ea_ratio(receivables, revenue)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_21d_63d_base_v083_signal(receivables, revenue) -> pd.Series:
    """Acceleration of Days Sales Outstanding over 21d and 63d."""
    ratio = _ea_ratio(receivables, revenue)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_5d_21d_base_v084_signal(payables, cogs) -> pd.Series:
    """Acceleration of Days Payables Outstanding (Pay/Cogs) over 5d and 21d."""
    ratio = _ea_ratio(payables, cogs)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_21d_63d_base_v085_signal(payables, cogs) -> pd.Series:
    """Acceleration of Days Payables Outstanding over 21d and 63d."""
    ratio = _ea_ratio(payables, cogs)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_5d_21d_base_v086_signal(assets, equity) -> pd.Series:
    """Acceleration of Asset/Equity Leverage over 5d and 21d."""
    ratio = _ea_ratio(assets, equity)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_21d_63d_base_v087_signal(assets, equity) -> pd.Series:
    """Acceleration of Asset/Equity Leverage over 21d and 63d."""
    ratio = _ea_ratio(assets, equity)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_5d_21d_base_v088_signal(revenue, assets, liabilities) -> pd.Series:
    """Acceleration of Net Asset Turnover (Rev/(Assets-Liab)) over 5d and 21d."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_21d_63d_base_v089_signal(revenue, assets, liabilities) -> pd.Series:
    """Acceleration of Net Asset Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_5d_21d_base_v090_signal(capex, assets) -> pd.Series:
    """Acceleration of CAPEX Intensity (Capex/Assets) over 5d and 21d."""
    ratio = _ea_ratio(capex, assets)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_21d_63d_base_v091_signal(capex, assets) -> pd.Series:
    """Acceleration of CAPEX Intensity over 21d and 63d."""
    ratio = _ea_ratio(capex, assets)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_5d_21d_base_v092_signal(revenue, employees) -> pd.Series:
    """Acceleration of Revenue per Employee over 5d and 21d."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 5, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_21d_63d_base_v093_signal(revenue, employees) -> pd.Series:
    """Acceleration of Revenue per Employee over 21d and 63d."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 21, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_z_5d_21d_base_v094_signal(opinc, revenue) -> pd.Series:
    """Z-score of Acceleration of Operating Margin over 5d and 21d."""
    ratio = _ea_ratio(opinc, revenue)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_z_21d_63d_base_v095_signal(opinc, revenue) -> pd.Series:
    """Z-score of Acceleration of Operating Margin over 21d and 63d."""
    ratio = _ea_ratio(opinc, revenue)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_z_5d_21d_base_v096_signal(revenue, cogs) -> pd.Series:
    """Z-score of Acceleration of Gross Margin over 5d and 21d."""
    ratio = _ea_ratio(revenue, cogs)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_z_21d_63d_base_v097_signal(revenue, cogs) -> pd.Series:
    """Z-score of Acceleration of Gross Margin over 21d and 63d."""
    ratio = _ea_ratio(revenue, cogs)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_z_5d_21d_base_v098_signal(inventory, cogs) -> pd.Series:
    """Z-score of Acceleration of Days Sales in Inventory over 5d and 21d."""
    ratio = _ea_ratio(inventory, cogs)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_z_21d_63d_base_v099_signal(inventory, cogs) -> pd.Series:
    """Z-score of Acceleration of Days Sales in Inventory over 21d and 63d."""
    ratio = _ea_ratio(inventory, cogs)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_z_5d_21d_base_v100_signal(receivables, revenue) -> pd.Series:
    """Z-score of Acceleration of Days Sales Outstanding over 5d and 21d."""
    ratio = _ea_ratio(receivables, revenue)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_z_21d_63d_base_v101_signal(receivables, revenue) -> pd.Series:
    """Z-score of Acceleration of Days Sales Outstanding over 21d and 63d."""
    ratio = _ea_ratio(receivables, revenue)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_z_5d_21d_base_v102_signal(payables, cogs) -> pd.Series:
    """Z-score of Acceleration of Days Payables Outstanding over 5d and 21d."""
    ratio = _ea_ratio(payables, cogs)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_z_21d_63d_base_v103_signal(payables, cogs) -> pd.Series:
    """Z-score of Acceleration of Days Payables Outstanding over 21d and 63d."""
    ratio = _ea_ratio(payables, cogs)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_z_5d_21d_base_v104_signal(assets, equity) -> pd.Series:
    """Z-score of Acceleration of Leverage over 5d and 21d."""
    ratio = _ea_ratio(assets, equity)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_z_21d_63d_base_v105_signal(assets, equity) -> pd.Series:
    """Z-score of Acceleration of Leverage over 21d and 63d."""
    ratio = _ea_ratio(assets, equity)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_z_5d_21d_base_v106_signal(revenue, assets, liabilities) -> pd.Series:
    """Z-score of Acceleration of Net Asset Turnover over 5d and 21d."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_z_21d_63d_base_v107_signal(revenue, assets, liabilities) -> pd.Series:
    """Z-score of Acceleration of Net Asset Turnover over 21d and 63d."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_z_5d_21d_base_v108_signal(capex, assets) -> pd.Series:
    """Z-score of Acceleration of CAPEX Intensity over 5d and 21d."""
    ratio = _ea_ratio(capex, assets)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_z_21d_63d_base_v109_signal(capex, assets) -> pd.Series:
    """Z-score of Acceleration of CAPEX Intensity over 21d and 63d."""
    ratio = _ea_ratio(capex, assets)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_z_5d_21d_base_v110_signal(revenue, employees) -> pd.Series:
    """Z-score of Acceleration of Revenue per Employee over 5d and 21d."""
    ratio = _ea_ratio(revenue, employees)
    accel = _ea_accel(ratio, 5, 21)
    res = _ea_z(accel, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_z_21d_63d_base_v111_signal(revenue, employees) -> pd.Series:
    """Z-score of Acceleration of Revenue per Employee over 21d and 63d."""
    ratio = _ea_ratio(revenue, employees)
    accel = _ea_accel(ratio, 21, 63)
    res = _ea_z(accel, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_126d_252d_base_v112_signal(opinc, revenue) -> pd.Series:
    """Long window Acceleration of Operating Margin."""
    ratio = _ea_ratio(opinc, revenue)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_126d_252d_base_v113_signal(revenue, cogs) -> pd.Series:
    """Long window Acceleration of Gross Margin."""
    ratio = _ea_ratio(revenue, cogs)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_126d_252d_base_v114_signal(inventory, cogs) -> pd.Series:
    """Long window Acceleration of Days Sales in Inventory."""
    ratio = _ea_ratio(inventory, cogs)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_126d_252d_base_v115_signal(receivables, revenue) -> pd.Series:
    """Long window Acceleration of Days Sales Outstanding."""
    ratio = _ea_ratio(receivables, revenue)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_126d_252d_base_v116_signal(payables, cogs) -> pd.Series:
    """Long window Acceleration of Days Payables Outstanding."""
    ratio = _ea_ratio(payables, cogs)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_126d_252d_base_v117_signal(assets, equity) -> pd.Series:
    """Long window Acceleration of Leverage."""
    ratio = _ea_ratio(assets, equity)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_126d_252d_base_v118_signal(revenue, assets, liabilities) -> pd.Series:
    """Long window Acceleration of Net Asset Turnover."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_126d_252d_base_v119_signal(capex, assets) -> pd.Series:
    """Long window Acceleration of CAPEX Intensity."""
    ratio = _ea_ratio(capex, assets)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_126d_252d_base_v120_signal(revenue, employees) -> pd.Series:
    """Long window Acceleration of Revenue per Employee."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 126, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_3d_10d_base_v121_signal(opinc, revenue) -> pd.Series:
    """Short window Acceleration of Operating Margin."""
    ratio = _ea_ratio(opinc, revenue)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_3d_10d_base_v122_signal(revenue, cogs) -> pd.Series:
    """Short window Acceleration of Gross Margin."""
    ratio = _ea_ratio(revenue, cogs)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_3d_10d_base_v123_signal(inventory, cogs) -> pd.Series:
    """Short window Acceleration of Days Sales in Inventory."""
    ratio = _ea_ratio(inventory, cogs)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_3d_10d_base_v124_signal(receivables, revenue) -> pd.Series:
    """Short window Acceleration of Days Sales Outstanding."""
    ratio = _ea_ratio(receivables, revenue)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_3d_10d_base_v125_signal(payables, cogs) -> pd.Series:
    """Short window Acceleration of Days Payables Outstanding."""
    ratio = _ea_ratio(payables, cogs)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_3d_10d_base_v126_signal(assets, equity) -> pd.Series:
    """Short window Acceleration of Leverage."""
    ratio = _ea_ratio(assets, equity)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_3d_10d_base_v127_signal(revenue, assets, liabilities) -> pd.Series:
    """Short window Acceleration of Net Asset Turnover."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_3d_10d_base_v128_signal(capex, assets) -> pd.Series:
    """Short window Acceleration of CAPEX Intensity."""
    ratio = _ea_ratio(capex, assets)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_3d_10d_base_v129_signal(revenue, employees) -> pd.Series:
    """Short window Acceleration of Revenue per Employee."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 3, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_10d_63d_base_v130_signal(opinc, revenue) -> pd.Series:
    """Acceleration of Operating Margin over 10d and 63d."""
    ratio = _ea_ratio(opinc, revenue)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_10d_63d_base_v131_signal(revenue, cogs) -> pd.Series:
    """Acceleration of Gross Margin over 10d and 63d."""
    ratio = _ea_ratio(revenue, cogs)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_10d_63d_base_v132_signal(inventory, cogs) -> pd.Series:
    """Acceleration of Days Sales in Inventory over 10d and 63d."""
    ratio = _ea_ratio(inventory, cogs)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_10d_63d_base_v133_signal(receivables, revenue) -> pd.Series:
    """Acceleration of Days Sales Outstanding over 10d and 63d."""
    ratio = _ea_ratio(receivables, revenue)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_10d_63d_base_v134_signal(payables, cogs) -> pd.Series:
    """Acceleration of Days Payables Outstanding over 10d and 63d."""
    ratio = _ea_ratio(payables, cogs)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_10d_63d_base_v135_signal(assets, equity) -> pd.Series:
    """Acceleration of Leverage over 10d and 63d."""
    ratio = _ea_ratio(assets, equity)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_10d_63d_base_v136_signal(revenue, assets, liabilities) -> pd.Series:
    """Acceleration of Net Asset Turnover over 10d and 63d."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_10d_63d_base_v137_signal(capex, assets) -> pd.Series:
    """Acceleration of CAPEX Intensity over 10d and 63d."""
    ratio = _ea_ratio(capex, assets)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_10d_63d_base_v138_signal(revenue, employees) -> pd.Series:
    """Acceleration of Revenue per Employee over 10d and 63d."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 10, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_margin_accel_63d_252d_base_v139_signal(opinc, revenue) -> pd.Series:
    """Acceleration of Operating Margin over 63d and 252d."""
    ratio = _ea_ratio(opinc, revenue)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_gross_margin_accel_63d_252d_base_v140_signal(revenue, cogs) -> pd.Series:
    """Acceleration of Gross Margin over 63d and 252d."""
    ratio = _ea_ratio(revenue, cogs)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dsi_accel_63d_252d_base_v141_signal(inventory, cogs) -> pd.Series:
    """Acceleration of Days Sales in Inventory over 63d and 252d."""
    ratio = _ea_ratio(inventory, cogs)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dso_accel_63d_252d_base_v142_signal(receivables, revenue) -> pd.Series:
    """Acceleration of Days Sales Outstanding over 63d and 252d."""
    ratio = _ea_ratio(receivables, revenue)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_dpo_accel_63d_252d_base_v143_signal(payables, cogs) -> pd.Series:
    """Acceleration of Days Payables Outstanding over 63d and 252d."""
    ratio = _ea_ratio(payables, cogs)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_leverage_accel_63d_252d_base_v144_signal(assets, equity) -> pd.Series:
    """Acceleration of Leverage over 63d and 252d."""
    ratio = _ea_ratio(assets, equity)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_net_asset_turn_accel_63d_252d_base_v145_signal(revenue, assets, liabilities) -> pd.Series:
    """Acceleration of Net Asset Turnover over 63d and 252d."""
    ratio = _ea_ratio(revenue, assets - liabilities)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_capex_intensity_accel_63d_252d_base_v146_signal(capex, assets) -> pd.Series:
    """Acceleration of CAPEX Intensity over 63d and 252d."""
    ratio = _ea_ratio(capex, assets)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_rev_per_emp_accel_63d_252d_base_v147_signal(revenue, employees) -> pd.Series:
    """Acceleration of Revenue per Employee over 63d and 252d."""
    ratio = _ea_ratio(revenue, employees)
    res = _ea_accel(ratio, 63, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_asset_turn_accel_21d_252d_base_v148_signal(revenue, assets) -> pd.Series:
    """Acceleration of Asset Turnover over 21d and 252d."""
    ratio = _ea_ratio(revenue, assets)
    res = _ea_accel(ratio, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_wc_turn_accel_21d_252d_base_v149_signal(revenue, workingcapital) -> pd.Series:
    """Acceleration of Working Capital Turnover over 21d and 252d."""
    ratio = _ea_ratio(revenue, workingcapital)
    res = _ea_accel(ratio, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f33_efficiency_acceleration_op_eff_accel_21d_252d_base_v150_signal(opinc, assets) -> pd.Series:
    """Acceleration of Operating Efficiency over 21d and 252d."""
    ratio = _ea_ratio(opinc, assets)
    res = _ea_accel(ratio, 21, 252)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1000
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum(),
        "assets": np.random.normal(5000, 500, n).cumsum(),
        "workingcapital": np.random.normal(100, 20, n).cumsum(),
        "opinc": np.random.normal(100, 20, n).cumsum(),
        "inventory": np.random.normal(200, 40, n).cumsum(),
        "receivables": np.random.normal(150, 30, n).cumsum(),
        "payables": np.random.normal(120, 25, n).cumsum(),
        "capex": np.random.normal(50, 10, n).cumsum(),
        "equity": np.random.normal(3000, 300, n).cumsum(),
        "liabilities": np.random.normal(2000, 200, n).cumsum(),
        "employees": np.random.normal(100, 10, n).cumsum() + 100,
        "cogs": np.random.normal(700, 70, n).cumsum(),
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f33_"))]
    
    print(f"Testing {len(funcs)} functions...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        # Test non-triviality
        q = y1.dropna()
        if len(q) > 0:
            assert q.nunique() > 10, f"Function {func.__name__} has too few unique values"
        
    print("All tests passed!")
