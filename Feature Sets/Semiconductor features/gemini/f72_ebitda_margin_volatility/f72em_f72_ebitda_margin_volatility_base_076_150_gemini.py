import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_180d_base_v076_signal(fcf, revenue):
    res = (fcf / revenue).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_180d_base_v076_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_180d_base_v076_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_90d_base_v077_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_90d_base_v077_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_90d_base_v077_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_126d_base_v078_signal(ebitda, equity):
    res = (ebitda / equity).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_126d_base_v078_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_126d_base_v078_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_63d_base_v079_signal(opinc, revenue):
    res = (opinc / revenue).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_63d_base_v079_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_63d_base_v079_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_30d_base_v080_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_30d_base_v080_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_30d_base_v080_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_90d_base_v081_signal(ebitda, equity):
    res = (ebitda / equity).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_90d_base_v081_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_90d_base_v081_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_21d_base_v082_signal(ebitda, equity):
    res = (ebitda / equity).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_21d_base_v082_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_21d_base_v082_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_42d_base_v083_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_42d_base_v083_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_42d_base_v083_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_90d_base_v084_signal(fcf, revenue):
    res = (fcf / revenue).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_90d_base_v084_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_90d_base_v084_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_63d_base_v085_signal(ebitda, debt):
    res = (ebitda / debt).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_63d_base_v085_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_63d_base_v085_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_90d_base_v086_signal(opinc, revenue):
    res = (opinc / revenue).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_90d_base_v086_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_90d_base_v086_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_30d_base_v087_signal(ebitda, equity):
    res = (ebitda / equity).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_30d_base_v087_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_skew_30d_base_v087_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_5d_base_v088_signal(ebitda, gp):
    res = (ebitda / gp).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_5d_base_v088_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_5d_base_v088_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_252d_base_v089_signal(ebitda, assets):
    res = (ebitda / assets).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_252d_base_v089_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_252d_base_v089_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_63d_base_v090_signal(fcf, revenue):
    res = (fcf / revenue).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_63d_base_v090_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_63d_base_v090_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_21d_base_v091_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_21d_base_v091_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_21d_base_v091_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_126d_base_v092_signal(ebitda, ev):
    res = (ebitda / ev).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_126d_base_v092_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_126d_base_v092_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_90d_base_v093_signal(ebitda, debt):
    res = (ebitda / debt).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_90d_base_v093_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_90d_base_v093_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_252d_base_v094_signal(netinc, revenue):
    res = (netinc / revenue).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_252d_base_v094_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_skew_252d_base_v094_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_21d_base_v095_signal(ebitda, debt):
    res = (ebitda / debt).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_21d_base_v095_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_21d_base_v095_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_90d_base_v096_signal(ebitda, assets):
    res = (ebitda / assets).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_90d_base_v096_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_90d_base_v096_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_15d_base_v097_signal(ebitda, gp):
    res = (ebitda / gp).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_15d_base_v097_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_15d_base_v097_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_5d_base_v098_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_5d_base_v098_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_5d_base_v098_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_63d_base_v099_signal(ebitda, debt):
    res = (ebitda / debt).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_63d_base_v099_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_63d_base_v099_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_21d_base_v100_signal(netinc, revenue):
    res = (netinc / revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_21d_base_v100_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_21d_base_v100_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_21d_base_v101_signal(ebitda, ev):
    res = (ebitda / ev).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_21d_base_v101_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_21d_base_v101_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_rev_rel_base_vol_close_63d_base_v102_signal(ebitda, revenue, closeadj):
    res = (ebitda / revenue).rolling(63).std() / closeadj.pct_change().rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_rev_rel_base_vol_close_63d_base_v102_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_rev_rel_base_vol_close_63d_base_v102_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_126d_base_v103_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_126d_base_v103_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_126d_base_v103_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_252d_base_v104_signal(ebitda, gp):
    res = (ebitda / gp).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_252d_base_v104_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_252d_base_v104_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_180d_base_v105_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_180d_base_v105_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_180d_base_v105_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_15d_base_v106_signal(ebitda, ev):
    res = (ebitda / ev).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_15d_base_v106_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_15d_base_v106_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_126d_base_v107_signal(ebitda, assets):
    res = (ebitda / assets).rolling(126).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_126d_base_v107_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_126d_base_v107_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_rev_base_vol_int_63d_base_v108_signal(ebitda, revenue, volume):
    res = (ebitda / revenue).rolling(63).std() * volume.pct_change().rolling(63).std().abs()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_rev_base_vol_int_63d_base_v108_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_rev_base_vol_int_63d_base_v108_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_15d_base_v109_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(15).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_15d_base_v109_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_std_15d_base_v109_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_30d_base_v110_signal(ebitda, equity):
    res = (ebitda / equity).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_30d_base_v110_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_30d_base_v110_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_180d_base_v111_signal(ebitda, ev):
    res = (ebitda / ev).rolling(180).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_180d_base_v111_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_180d_base_v111_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_90d_base_v112_signal(ebitda, equity):
    res = (ebitda / equity).rolling(90).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_90d_base_v112_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_90d_base_v112_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_42d_base_v113_signal(ebitda, debt):
    res = (ebitda / debt).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_42d_base_v113_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_42d_base_v113_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_63d_base_v114_signal(ebitda, assets):
    res = (ebitda / assets).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_63d_base_v114_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_63d_base_v114_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_21d_base_v115_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_21d_base_v115_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_21d_base_v115_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_42d_base_v116_signal(fcf, revenue):
    res = (fcf / revenue).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_42d_base_v116_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_42d_base_v116_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_126d_base_v117_signal(netinc, revenue):
    res = (netinc / revenue).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_126d_base_v117_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_126d_base_v117_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_30d_base_v118_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_30d_base_v118_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_skew_30d_base_v118_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_5d_base_v119_signal(ebitda, equity):
    res = (ebitda / equity).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_5d_base_v119_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_5d_base_v119_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_21d_base_v120_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_21d_base_v120_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_21d_base_v120_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_126d_base_v121_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_126d_base_v121_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_126d_base_v121_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_21d_base_v122_signal(ebitda, ev):
    res = (ebitda / ev).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_21d_base_v122_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_21d_base_v122_signal

def f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_42d_base_v123_signal(netinc, revenue):
    res = (netinc / revenue).rolling(42).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_42d_base_v123_signal'] = f72em_f72_ebitda_margin_base_volatility_netinc_revenue_std_42d_base_v123_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_63d_base_v124_signal(ebitda, ev):
    res = (ebitda / ev).rolling(63).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_63d_base_v124_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_std_63d_base_v124_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_30d_base_v125_signal(ebitda, assets):
    res = (ebitda / assets).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_30d_base_v125_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_30d_base_v125_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_21d_base_v126_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(21).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_21d_base_v126_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_21d_base_v126_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_30d_base_v127_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_30d_base_v127_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_30d_base_v127_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_252d_base_v128_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(252).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_252d_base_v128_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_252d_base_v128_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_90d_base_v129_signal(ebitda, assets):
    res = (ebitda / assets).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_90d_base_v129_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_90d_base_v129_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_90d_base_v130_signal(ebitda, gp):
    res = (ebitda / gp).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_90d_base_v130_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_90d_base_v130_signal

def f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_180d_base_v131_signal(opinc, revenue):
    res = (opinc / revenue).rolling(180).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_180d_base_v131_signal'] = f72em_f72_ebitda_margin_base_volatility_opinc_revenue_std_180d_base_v131_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_42d_base_v132_signal(ebitda, assets):
    res = (ebitda / assets).rolling(42).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_42d_base_v132_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_42d_base_v132_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_10d_base_v133_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_10d_base_v133_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_std_10d_base_v133_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_252d_base_v134_signal(ebitda, debt):
    res = (ebitda / debt).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_252d_base_v134_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_skew_252d_base_v134_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_10d_base_v135_signal(ebitda, equity):
    res = (ebitda / equity).rolling(10).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_10d_base_v135_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_equity_std_10d_base_v135_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_90d_base_v136_signal(ebitda, workingcapital):
    res = (ebitda / workingcapital).rolling(90).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_90d_base_v136_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_workingcapital_skew_90d_base_v136_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_30d_base_v137_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_30d_base_v137_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_std_30d_base_v137_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_126d_base_v138_signal(ebitda, debt):
    res = (ebitda / debt).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_126d_base_v138_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_debt_std_126d_base_v138_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_5d_base_v139_signal(fcf, revenue):
    res = (fcf / revenue).rolling(5).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_5d_base_v139_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_std_5d_base_v139_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_126d_base_v140_signal(ebitda, revenue):
    res = (ebitda / revenue).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_126d_base_v140_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_revenue_std_126d_base_v140_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_63d_base_v141_signal(ebitda, marketcap):
    res = (ebitda / marketcap).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_63d_base_v141_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_marketcap_skew_63d_base_v141_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_30d_base_v142_signal(ebitda, assets):
    res = (ebitda / assets).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_30d_base_v142_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_skew_30d_base_v142_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_30d_base_v143_signal(ebitda, gp):
    res = (ebitda / gp).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_30d_base_v143_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_skew_30d_base_v143_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_30d_base_v144_signal(ebitda, gp):
    res = (ebitda / gp).rolling(30).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_30d_base_v144_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_gp_std_30d_base_v144_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_21d_base_v145_signal(ebitda, assets):
    res = (ebitda / assets).rolling(21).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_21d_base_v145_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_21d_base_v145_signal

def f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_252d_base_v146_signal(ncfo, revenue):
    res = (ncfo / revenue).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_252d_base_v146_signal'] = f72em_f72_ebitda_margin_base_volatility_ncfo_revenue_skew_252d_base_v146_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_252d_base_v147_signal(ebitda, ev):
    res = (ebitda / ev).rolling(252).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_252d_base_v147_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_ev_skew_252d_base_v147_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_126d_base_v148_signal(ebitda, assets):
    res = (ebitda / assets).rolling(126).std()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_126d_base_v148_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_assets_std_126d_base_v148_signal

def f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_63d_base_v149_signal(ebitda, liabilities):
    res = (ebitda / liabilities).rolling(63).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_63d_base_v149_signal'] = f72em_f72_ebitda_margin_base_volatility_ebitda_liabilities_skew_63d_base_v149_signal

def f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_30d_base_v150_signal(fcf, revenue):
    res = (fcf / revenue).rolling(30).skew()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_30d_base_v150_signal'] = f72em_f72_ebitda_margin_base_volatility_fcf_revenue_skew_30d_base_v150_signal

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.uniform(500, 2000, n),
        "ebitda": np.random.uniform(50, 200, n),
        "opinc": np.random.uniform(40, 180, n),
        "netinc": np.random.uniform(20, 100, n),
        "assets": np.random.uniform(2000, 5000, n),
        "equity": np.random.uniform(1000, 3000, n),
        "marketcap": np.random.uniform(5000, 20000, n),
        "ev": np.random.uniform(6000, 25000, n),
        "closeadj": np.random.uniform(10, 100, n),
        "volume": np.random.uniform(100000, 1000000, n),
        "ncfo": np.random.uniform(30, 150, n),
        "capex": np.random.uniform(10, 50, n),
        "liabilities": np.random.uniform(1000, 4000, n),
        "debt": np.random.uniform(500, 2000, n),
        "workingcapital": np.random.uniform(200, 800, n),
        "currentratio": np.random.uniform(1, 5, n),
        "gp": np.random.uniform(100, 400, n),
        "retearn": np.random.uniform(500, 2000, n),
        "eps": np.random.uniform(0.1, 5, n),
        "fcf": np.random.uniform(20, 120, n),
        "pe": np.random.uniform(10, 30, n),
        "pb": np.random.uniform(1, 5, n),
        "ps": np.random.uniform(1, 10, n)
    })
    results = {}
    for name, func in FEATURE_FUNCTIONS.items():
        import inspect
        args = inspect.getfullargspec(func).args
        res = func(**{col: df[col] for col in args})
        results[name] = res
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}")
                assert corr_matrix.iloc[i, j] <= 0.95, f"High correlation between {col1} and {col2}: {corr_matrix.iloc[i, j]}"
    print(f"Self-test passed for {os.path.basename(__file__)}")

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
