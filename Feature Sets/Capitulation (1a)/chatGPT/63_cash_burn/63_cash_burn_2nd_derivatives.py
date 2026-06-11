import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)



def cbr_151_cbr_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def cbr_152_cbr_007_interest_coverage_stress_252_roc_42(cbr_007_interest_coverage_stress_252):
    feature = _s(cbr_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def cbr_153_cbr_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def cbr_154_cbr_019_interest_coverage_stress_84_roc_378(cbr_019_interest_coverage_stress_84):
    feature = _s(cbr_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def cbr_155_cbr_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















CASH_BURN_REGISTRY_2ND_DERIVATIVES = {
    'cbr_151_cbr_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': cbr_151_cbr_001_netinc_decline_1_roc_1},
    'cbr_152_cbr_007_interest_coverage_stress_252_roc_42': {'inputs': ['cbr_007_interest_coverage_stress_252'], 'func': cbr_152_cbr_007_interest_coverage_stress_252_roc_42},
    'cbr_153_cbr_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': cbr_153_cbr_013_netinc_decline_1_roc_126},
    'cbr_154_cbr_019_interest_coverage_stress_84_roc_378': {'inputs': ['cbr_019_interest_coverage_stress_84'], 'func': cbr_154_cbr_019_interest_coverage_stress_84_roc_378},
    'cbr_155_cbr_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': cbr_155_cbr_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def cb_replacement_d2_001(cb_replacement_001):
    feature = _clean(cb_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_001'] = {'inputs': ['cb_replacement_001'], 'func': cb_replacement_d2_001}


def cb_replacement_d2_002(cb_replacement_002):
    feature = _clean(cb_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_002'] = {'inputs': ['cb_replacement_002'], 'func': cb_replacement_d2_002}


def cb_replacement_d2_003(cb_replacement_003):
    feature = _clean(cb_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_003'] = {'inputs': ['cb_replacement_003'], 'func': cb_replacement_d2_003}


def cb_replacement_d2_004(cb_replacement_004):
    feature = _clean(cb_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_004'] = {'inputs': ['cb_replacement_004'], 'func': cb_replacement_d2_004}


def cb_replacement_d2_005(cb_replacement_005):
    feature = _clean(cb_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_005'] = {'inputs': ['cb_replacement_005'], 'func': cb_replacement_d2_005}


def cb_replacement_d2_006(cb_replacement_006):
    feature = _clean(cb_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_006'] = {'inputs': ['cb_replacement_006'], 'func': cb_replacement_d2_006}


def cb_replacement_d2_007(cb_replacement_007):
    feature = _clean(cb_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_007'] = {'inputs': ['cb_replacement_007'], 'func': cb_replacement_d2_007}


def cb_replacement_d2_008(cb_replacement_008):
    feature = _clean(cb_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_008'] = {'inputs': ['cb_replacement_008'], 'func': cb_replacement_d2_008}


def cb_replacement_d2_009(cb_replacement_009):
    feature = _clean(cb_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_009'] = {'inputs': ['cb_replacement_009'], 'func': cb_replacement_d2_009}


def cb_replacement_d2_010(cb_replacement_010):
    feature = _clean(cb_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_010'] = {'inputs': ['cb_replacement_010'], 'func': cb_replacement_d2_010}


def cb_replacement_d2_011(cb_replacement_011):
    feature = _clean(cb_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_011'] = {'inputs': ['cb_replacement_011'], 'func': cb_replacement_d2_011}


def cb_replacement_d2_012(cb_replacement_012):
    feature = _clean(cb_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_012'] = {'inputs': ['cb_replacement_012'], 'func': cb_replacement_d2_012}


def cb_replacement_d2_013(cb_replacement_013):
    feature = _clean(cb_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_013'] = {'inputs': ['cb_replacement_013'], 'func': cb_replacement_d2_013}


def cb_replacement_d2_014(cb_replacement_014):
    feature = _clean(cb_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_014'] = {'inputs': ['cb_replacement_014'], 'func': cb_replacement_d2_014}


def cb_replacement_d2_015(cb_replacement_015):
    feature = _clean(cb_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_015'] = {'inputs': ['cb_replacement_015'], 'func': cb_replacement_d2_015}


def cb_replacement_d2_016(cb_replacement_016):
    feature = _clean(cb_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_016'] = {'inputs': ['cb_replacement_016'], 'func': cb_replacement_d2_016}


def cb_replacement_d2_017(cb_replacement_017):
    feature = _clean(cb_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_017'] = {'inputs': ['cb_replacement_017'], 'func': cb_replacement_d2_017}


def cb_replacement_d2_018(cb_replacement_018):
    feature = _clean(cb_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_018'] = {'inputs': ['cb_replacement_018'], 'func': cb_replacement_d2_018}


def cb_replacement_d2_019(cb_replacement_019):
    feature = _clean(cb_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_019'] = {'inputs': ['cb_replacement_019'], 'func': cb_replacement_d2_019}


def cb_replacement_d2_020(cb_replacement_020):
    feature = _clean(cb_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_020'] = {'inputs': ['cb_replacement_020'], 'func': cb_replacement_d2_020}


def cb_replacement_d2_021(cb_replacement_021):
    feature = _clean(cb_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_021'] = {'inputs': ['cb_replacement_021'], 'func': cb_replacement_d2_021}


def cb_replacement_d2_022(cb_replacement_022):
    feature = _clean(cb_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_022'] = {'inputs': ['cb_replacement_022'], 'func': cb_replacement_d2_022}


def cb_replacement_d2_023(cb_replacement_023):
    feature = _clean(cb_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_023'] = {'inputs': ['cb_replacement_023'], 'func': cb_replacement_d2_023}


def cb_replacement_d2_024(cb_replacement_024):
    feature = _clean(cb_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_024'] = {'inputs': ['cb_replacement_024'], 'func': cb_replacement_d2_024}


def cb_replacement_d2_025(cb_replacement_025):
    feature = _clean(cb_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_025'] = {'inputs': ['cb_replacement_025'], 'func': cb_replacement_d2_025}


def cb_replacement_d2_026(cb_replacement_026):
    feature = _clean(cb_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_026'] = {'inputs': ['cb_replacement_026'], 'func': cb_replacement_d2_026}


def cb_replacement_d2_027(cb_replacement_027):
    feature = _clean(cb_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_027'] = {'inputs': ['cb_replacement_027'], 'func': cb_replacement_d2_027}


def cb_replacement_d2_028(cb_replacement_028):
    feature = _clean(cb_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_028'] = {'inputs': ['cb_replacement_028'], 'func': cb_replacement_d2_028}


def cb_replacement_d2_029(cb_replacement_029):
    feature = _clean(cb_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_029'] = {'inputs': ['cb_replacement_029'], 'func': cb_replacement_d2_029}


def cb_replacement_d2_030(cb_replacement_030):
    feature = _clean(cb_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_030'] = {'inputs': ['cb_replacement_030'], 'func': cb_replacement_d2_030}


def cb_replacement_d2_031(cb_replacement_031):
    feature = _clean(cb_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_031'] = {'inputs': ['cb_replacement_031'], 'func': cb_replacement_d2_031}


def cb_replacement_d2_032(cb_replacement_032):
    feature = _clean(cb_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_032'] = {'inputs': ['cb_replacement_032'], 'func': cb_replacement_d2_032}


def cb_replacement_d2_033(cb_replacement_033):
    feature = _clean(cb_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_033'] = {'inputs': ['cb_replacement_033'], 'func': cb_replacement_d2_033}


def cb_replacement_d2_034(cb_replacement_034):
    feature = _clean(cb_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_034'] = {'inputs': ['cb_replacement_034'], 'func': cb_replacement_d2_034}


def cb_replacement_d2_035(cb_replacement_035):
    feature = _clean(cb_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_035'] = {'inputs': ['cb_replacement_035'], 'func': cb_replacement_d2_035}


def cb_replacement_d2_036(cb_replacement_036):
    feature = _clean(cb_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_036'] = {'inputs': ['cb_replacement_036'], 'func': cb_replacement_d2_036}


def cb_replacement_d2_037(cb_replacement_037):
    feature = _clean(cb_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_037'] = {'inputs': ['cb_replacement_037'], 'func': cb_replacement_d2_037}


def cb_replacement_d2_038(cb_replacement_038):
    feature = _clean(cb_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_038'] = {'inputs': ['cb_replacement_038'], 'func': cb_replacement_d2_038}


def cb_replacement_d2_039(cb_replacement_039):
    feature = _clean(cb_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_039'] = {'inputs': ['cb_replacement_039'], 'func': cb_replacement_d2_039}


def cb_replacement_d2_040(cb_replacement_040):
    feature = _clean(cb_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_040'] = {'inputs': ['cb_replacement_040'], 'func': cb_replacement_d2_040}


def cb_replacement_d2_041(cb_replacement_041):
    feature = _clean(cb_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_041'] = {'inputs': ['cb_replacement_041'], 'func': cb_replacement_d2_041}


def cb_replacement_d2_042(cb_replacement_042):
    feature = _clean(cb_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_042'] = {'inputs': ['cb_replacement_042'], 'func': cb_replacement_d2_042}


def cb_replacement_d2_043(cb_replacement_043):
    feature = _clean(cb_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_043'] = {'inputs': ['cb_replacement_043'], 'func': cb_replacement_d2_043}


def cb_replacement_d2_044(cb_replacement_044):
    feature = _clean(cb_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_044'] = {'inputs': ['cb_replacement_044'], 'func': cb_replacement_d2_044}


def cb_replacement_d2_045(cb_replacement_045):
    feature = _clean(cb_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_045'] = {'inputs': ['cb_replacement_045'], 'func': cb_replacement_d2_045}


def cb_replacement_d2_046(cb_replacement_046):
    feature = _clean(cb_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_046'] = {'inputs': ['cb_replacement_046'], 'func': cb_replacement_d2_046}


def cb_replacement_d2_047(cb_replacement_047):
    feature = _clean(cb_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_047'] = {'inputs': ['cb_replacement_047'], 'func': cb_replacement_d2_047}


def cb_replacement_d2_048(cb_replacement_048):
    feature = _clean(cb_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_048'] = {'inputs': ['cb_replacement_048'], 'func': cb_replacement_d2_048}


def cb_replacement_d2_049(cb_replacement_049):
    feature = _clean(cb_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_049'] = {'inputs': ['cb_replacement_049'], 'func': cb_replacement_d2_049}


def cb_replacement_d2_050(cb_replacement_050):
    feature = _clean(cb_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_050'] = {'inputs': ['cb_replacement_050'], 'func': cb_replacement_d2_050}


def cb_replacement_d2_051(cb_replacement_051):
    feature = _clean(cb_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_051'] = {'inputs': ['cb_replacement_051'], 'func': cb_replacement_d2_051}


def cb_replacement_d2_052(cb_replacement_052):
    feature = _clean(cb_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_052'] = {'inputs': ['cb_replacement_052'], 'func': cb_replacement_d2_052}


def cb_replacement_d2_053(cb_replacement_053):
    feature = _clean(cb_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_053'] = {'inputs': ['cb_replacement_053'], 'func': cb_replacement_d2_053}


def cb_replacement_d2_054(cb_replacement_054):
    feature = _clean(cb_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_054'] = {'inputs': ['cb_replacement_054'], 'func': cb_replacement_d2_054}


def cb_replacement_d2_055(cb_replacement_055):
    feature = _clean(cb_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_055'] = {'inputs': ['cb_replacement_055'], 'func': cb_replacement_d2_055}


def cb_replacement_d2_056(cb_replacement_056):
    feature = _clean(cb_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_056'] = {'inputs': ['cb_replacement_056'], 'func': cb_replacement_d2_056}


def cb_replacement_d2_057(cb_replacement_057):
    feature = _clean(cb_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_057'] = {'inputs': ['cb_replacement_057'], 'func': cb_replacement_d2_057}


def cb_replacement_d2_058(cb_replacement_058):
    feature = _clean(cb_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_058'] = {'inputs': ['cb_replacement_058'], 'func': cb_replacement_d2_058}


def cb_replacement_d2_059(cb_replacement_059):
    feature = _clean(cb_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_059'] = {'inputs': ['cb_replacement_059'], 'func': cb_replacement_d2_059}


def cb_replacement_d2_060(cb_replacement_060):
    feature = _clean(cb_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_060'] = {'inputs': ['cb_replacement_060'], 'func': cb_replacement_d2_060}


def cb_replacement_d2_061(cb_replacement_061):
    feature = _clean(cb_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_061'] = {'inputs': ['cb_replacement_061'], 'func': cb_replacement_d2_061}


def cb_replacement_d2_062(cb_replacement_062):
    feature = _clean(cb_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_062'] = {'inputs': ['cb_replacement_062'], 'func': cb_replacement_d2_062}


def cb_replacement_d2_063(cb_replacement_063):
    feature = _clean(cb_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_063'] = {'inputs': ['cb_replacement_063'], 'func': cb_replacement_d2_063}


def cb_replacement_d2_064(cb_replacement_064):
    feature = _clean(cb_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_064'] = {'inputs': ['cb_replacement_064'], 'func': cb_replacement_d2_064}


def cb_replacement_d2_065(cb_replacement_065):
    feature = _clean(cb_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_065'] = {'inputs': ['cb_replacement_065'], 'func': cb_replacement_d2_065}


def cb_replacement_d2_066(cb_replacement_066):
    feature = _clean(cb_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_066'] = {'inputs': ['cb_replacement_066'], 'func': cb_replacement_d2_066}


def cb_replacement_d2_067(cb_replacement_067):
    feature = _clean(cb_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_067'] = {'inputs': ['cb_replacement_067'], 'func': cb_replacement_d2_067}


def cb_replacement_d2_068(cb_replacement_068):
    feature = _clean(cb_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_068'] = {'inputs': ['cb_replacement_068'], 'func': cb_replacement_d2_068}


def cb_replacement_d2_069(cb_replacement_069):
    feature = _clean(cb_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_069'] = {'inputs': ['cb_replacement_069'], 'func': cb_replacement_d2_069}


def cb_replacement_d2_070(cb_replacement_070):
    feature = _clean(cb_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_070'] = {'inputs': ['cb_replacement_070'], 'func': cb_replacement_d2_070}


def cb_replacement_d2_071(cb_replacement_071):
    feature = _clean(cb_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_071'] = {'inputs': ['cb_replacement_071'], 'func': cb_replacement_d2_071}


def cb_replacement_d2_072(cb_replacement_072):
    feature = _clean(cb_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_072'] = {'inputs': ['cb_replacement_072'], 'func': cb_replacement_d2_072}


def cb_replacement_d2_073(cb_replacement_073):
    feature = _clean(cb_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_073'] = {'inputs': ['cb_replacement_073'], 'func': cb_replacement_d2_073}


def cb_replacement_d2_074(cb_replacement_074):
    feature = _clean(cb_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_074'] = {'inputs': ['cb_replacement_074'], 'func': cb_replacement_d2_074}


def cb_replacement_d2_075(cb_replacement_075):
    feature = _clean(cb_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_075'] = {'inputs': ['cb_replacement_075'], 'func': cb_replacement_d2_075}


def cb_replacement_d2_076(cb_replacement_076):
    feature = _clean(cb_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_076'] = {'inputs': ['cb_replacement_076'], 'func': cb_replacement_d2_076}


def cb_replacement_d2_077(cb_replacement_077):
    feature = _clean(cb_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_077'] = {'inputs': ['cb_replacement_077'], 'func': cb_replacement_d2_077}


def cb_replacement_d2_078(cb_replacement_078):
    feature = _clean(cb_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_078'] = {'inputs': ['cb_replacement_078'], 'func': cb_replacement_d2_078}


def cb_replacement_d2_079(cb_replacement_079):
    feature = _clean(cb_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_079'] = {'inputs': ['cb_replacement_079'], 'func': cb_replacement_d2_079}


def cb_replacement_d2_080(cb_replacement_080):
    feature = _clean(cb_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_080'] = {'inputs': ['cb_replacement_080'], 'func': cb_replacement_d2_080}


def cb_replacement_d2_081(cb_replacement_081):
    feature = _clean(cb_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_081'] = {'inputs': ['cb_replacement_081'], 'func': cb_replacement_d2_081}


def cb_replacement_d2_082(cb_replacement_082):
    feature = _clean(cb_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_082'] = {'inputs': ['cb_replacement_082'], 'func': cb_replacement_d2_082}


def cb_replacement_d2_083(cb_replacement_083):
    feature = _clean(cb_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_083'] = {'inputs': ['cb_replacement_083'], 'func': cb_replacement_d2_083}


def cb_replacement_d2_084(cb_replacement_084):
    feature = _clean(cb_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_084'] = {'inputs': ['cb_replacement_084'], 'func': cb_replacement_d2_084}


def cb_replacement_d2_085(cb_replacement_085):
    feature = _clean(cb_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_085'] = {'inputs': ['cb_replacement_085'], 'func': cb_replacement_d2_085}


def cb_replacement_d2_086(cb_replacement_086):
    feature = _clean(cb_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_086'] = {'inputs': ['cb_replacement_086'], 'func': cb_replacement_d2_086}


def cb_replacement_d2_087(cb_replacement_087):
    feature = _clean(cb_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_087'] = {'inputs': ['cb_replacement_087'], 'func': cb_replacement_d2_087}


def cb_replacement_d2_088(cb_replacement_088):
    feature = _clean(cb_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_088'] = {'inputs': ['cb_replacement_088'], 'func': cb_replacement_d2_088}


def cb_replacement_d2_089(cb_replacement_089):
    feature = _clean(cb_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_089'] = {'inputs': ['cb_replacement_089'], 'func': cb_replacement_d2_089}


def cb_replacement_d2_090(cb_replacement_090):
    feature = _clean(cb_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_090'] = {'inputs': ['cb_replacement_090'], 'func': cb_replacement_d2_090}


def cb_replacement_d2_091(cb_replacement_091):
    feature = _clean(cb_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_091'] = {'inputs': ['cb_replacement_091'], 'func': cb_replacement_d2_091}


def cb_replacement_d2_092(cb_replacement_092):
    feature = _clean(cb_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_092'] = {'inputs': ['cb_replacement_092'], 'func': cb_replacement_d2_092}


def cb_replacement_d2_093(cb_replacement_093):
    feature = _clean(cb_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_093'] = {'inputs': ['cb_replacement_093'], 'func': cb_replacement_d2_093}


def cb_replacement_d2_094(cb_replacement_094):
    feature = _clean(cb_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_094'] = {'inputs': ['cb_replacement_094'], 'func': cb_replacement_d2_094}


def cb_replacement_d2_095(cb_replacement_095):
    feature = _clean(cb_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_095'] = {'inputs': ['cb_replacement_095'], 'func': cb_replacement_d2_095}


def cb_replacement_d2_096(cb_replacement_096):
    feature = _clean(cb_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_096'] = {'inputs': ['cb_replacement_096'], 'func': cb_replacement_d2_096}


def cb_replacement_d2_097(cb_replacement_097):
    feature = _clean(cb_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_097'] = {'inputs': ['cb_replacement_097'], 'func': cb_replacement_d2_097}


def cb_replacement_d2_098(cb_replacement_098):
    feature = _clean(cb_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_098'] = {'inputs': ['cb_replacement_098'], 'func': cb_replacement_d2_098}


def cb_replacement_d2_099(cb_replacement_099):
    feature = _clean(cb_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_099'] = {'inputs': ['cb_replacement_099'], 'func': cb_replacement_d2_099}


def cb_replacement_d2_100(cb_replacement_100):
    feature = _clean(cb_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_100'] = {'inputs': ['cb_replacement_100'], 'func': cb_replacement_d2_100}


def cb_replacement_d2_101(cb_replacement_101):
    feature = _clean(cb_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_101'] = {'inputs': ['cb_replacement_101'], 'func': cb_replacement_d2_101}


def cb_replacement_d2_102(cb_replacement_102):
    feature = _clean(cb_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_102'] = {'inputs': ['cb_replacement_102'], 'func': cb_replacement_d2_102}


def cb_replacement_d2_103(cb_replacement_103):
    feature = _clean(cb_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_103'] = {'inputs': ['cb_replacement_103'], 'func': cb_replacement_d2_103}


def cb_replacement_d2_104(cb_replacement_104):
    feature = _clean(cb_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_104'] = {'inputs': ['cb_replacement_104'], 'func': cb_replacement_d2_104}


def cb_replacement_d2_105(cb_replacement_105):
    feature = _clean(cb_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_105'] = {'inputs': ['cb_replacement_105'], 'func': cb_replacement_d2_105}


def cb_replacement_d2_106(cb_replacement_106):
    feature = _clean(cb_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_106'] = {'inputs': ['cb_replacement_106'], 'func': cb_replacement_d2_106}


def cb_replacement_d2_107(cb_replacement_107):
    feature = _clean(cb_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_107'] = {'inputs': ['cb_replacement_107'], 'func': cb_replacement_d2_107}


def cb_replacement_d2_108(cb_replacement_108):
    feature = _clean(cb_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_108'] = {'inputs': ['cb_replacement_108'], 'func': cb_replacement_d2_108}


def cb_replacement_d2_109(cb_replacement_109):
    feature = _clean(cb_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_109'] = {'inputs': ['cb_replacement_109'], 'func': cb_replacement_d2_109}


def cb_replacement_d2_110(cb_replacement_110):
    feature = _clean(cb_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_110'] = {'inputs': ['cb_replacement_110'], 'func': cb_replacement_d2_110}


def cb_replacement_d2_111(cb_replacement_111):
    feature = _clean(cb_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_111'] = {'inputs': ['cb_replacement_111'], 'func': cb_replacement_d2_111}


def cb_replacement_d2_112(cb_replacement_112):
    feature = _clean(cb_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_112'] = {'inputs': ['cb_replacement_112'], 'func': cb_replacement_d2_112}


def cb_replacement_d2_113(cb_replacement_113):
    feature = _clean(cb_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_113'] = {'inputs': ['cb_replacement_113'], 'func': cb_replacement_d2_113}


def cb_replacement_d2_114(cb_replacement_114):
    feature = _clean(cb_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_114'] = {'inputs': ['cb_replacement_114'], 'func': cb_replacement_d2_114}


def cb_replacement_d2_115(cb_replacement_115):
    feature = _clean(cb_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_115'] = {'inputs': ['cb_replacement_115'], 'func': cb_replacement_d2_115}


def cb_replacement_d2_116(cb_replacement_116):
    feature = _clean(cb_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_116'] = {'inputs': ['cb_replacement_116'], 'func': cb_replacement_d2_116}


def cb_replacement_d2_117(cb_replacement_117):
    feature = _clean(cb_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_117'] = {'inputs': ['cb_replacement_117'], 'func': cb_replacement_d2_117}


def cb_replacement_d2_118(cb_replacement_118):
    feature = _clean(cb_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_118'] = {'inputs': ['cb_replacement_118'], 'func': cb_replacement_d2_118}


def cb_replacement_d2_119(cb_replacement_119):
    feature = _clean(cb_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_119'] = {'inputs': ['cb_replacement_119'], 'func': cb_replacement_d2_119}


def cb_replacement_d2_120(cb_replacement_120):
    feature = _clean(cb_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_120'] = {'inputs': ['cb_replacement_120'], 'func': cb_replacement_d2_120}


def cb_replacement_d2_121(cb_replacement_121):
    feature = _clean(cb_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_121'] = {'inputs': ['cb_replacement_121'], 'func': cb_replacement_d2_121}


def cb_replacement_d2_122(cb_replacement_122):
    feature = _clean(cb_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_122'] = {'inputs': ['cb_replacement_122'], 'func': cb_replacement_d2_122}


def cb_replacement_d2_123(cb_replacement_123):
    feature = _clean(cb_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_123'] = {'inputs': ['cb_replacement_123'], 'func': cb_replacement_d2_123}


def cb_replacement_d2_124(cb_replacement_124):
    feature = _clean(cb_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_124'] = {'inputs': ['cb_replacement_124'], 'func': cb_replacement_d2_124}


def cb_replacement_d2_125(cb_replacement_125):
    feature = _clean(cb_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_125'] = {'inputs': ['cb_replacement_125'], 'func': cb_replacement_d2_125}


def cb_replacement_d2_126(cb_replacement_126):
    feature = _clean(cb_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_126'] = {'inputs': ['cb_replacement_126'], 'func': cb_replacement_d2_126}


def cb_replacement_d2_127(cb_replacement_127):
    feature = _clean(cb_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_127'] = {'inputs': ['cb_replacement_127'], 'func': cb_replacement_d2_127}


def cb_replacement_d2_128(cb_replacement_128):
    feature = _clean(cb_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_128'] = {'inputs': ['cb_replacement_128'], 'func': cb_replacement_d2_128}


def cb_replacement_d2_129(cb_replacement_129):
    feature = _clean(cb_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_129'] = {'inputs': ['cb_replacement_129'], 'func': cb_replacement_d2_129}


def cb_replacement_d2_130(cb_replacement_130):
    feature = _clean(cb_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_130'] = {'inputs': ['cb_replacement_130'], 'func': cb_replacement_d2_130}


def cb_replacement_d2_131(cb_replacement_131):
    feature = _clean(cb_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_131'] = {'inputs': ['cb_replacement_131'], 'func': cb_replacement_d2_131}


def cb_replacement_d2_132(cb_replacement_132):
    feature = _clean(cb_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_132'] = {'inputs': ['cb_replacement_132'], 'func': cb_replacement_d2_132}


def cb_replacement_d2_133(cb_replacement_133):
    feature = _clean(cb_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_133'] = {'inputs': ['cb_replacement_133'], 'func': cb_replacement_d2_133}


def cb_replacement_d2_134(cb_replacement_134):
    feature = _clean(cb_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_134'] = {'inputs': ['cb_replacement_134'], 'func': cb_replacement_d2_134}


def cb_replacement_d2_135(cb_replacement_135):
    feature = _clean(cb_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_135'] = {'inputs': ['cb_replacement_135'], 'func': cb_replacement_d2_135}


def cb_replacement_d2_136(cb_replacement_136):
    feature = _clean(cb_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_136'] = {'inputs': ['cb_replacement_136'], 'func': cb_replacement_d2_136}


def cb_replacement_d2_137(cb_replacement_137):
    feature = _clean(cb_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_137'] = {'inputs': ['cb_replacement_137'], 'func': cb_replacement_d2_137}


def cb_replacement_d2_138(cb_replacement_138):
    feature = _clean(cb_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_138'] = {'inputs': ['cb_replacement_138'], 'func': cb_replacement_d2_138}


def cb_replacement_d2_139(cb_replacement_139):
    feature = _clean(cb_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_139'] = {'inputs': ['cb_replacement_139'], 'func': cb_replacement_d2_139}


def cb_replacement_d2_140(cb_replacement_140):
    feature = _clean(cb_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_140'] = {'inputs': ['cb_replacement_140'], 'func': cb_replacement_d2_140}


def cb_replacement_d2_141(cb_replacement_141):
    feature = _clean(cb_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_141'] = {'inputs': ['cb_replacement_141'], 'func': cb_replacement_d2_141}


def cb_replacement_d2_142(cb_replacement_142):
    feature = _clean(cb_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_142'] = {'inputs': ['cb_replacement_142'], 'func': cb_replacement_d2_142}


def cb_replacement_d2_143(cb_replacement_143):
    feature = _clean(cb_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_143'] = {'inputs': ['cb_replacement_143'], 'func': cb_replacement_d2_143}


def cb_replacement_d2_144(cb_replacement_144):
    feature = _clean(cb_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_144'] = {'inputs': ['cb_replacement_144'], 'func': cb_replacement_d2_144}


def cb_replacement_d2_145(cb_replacement_145):
    feature = _clean(cb_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_145'] = {'inputs': ['cb_replacement_145'], 'func': cb_replacement_d2_145}


def cb_replacement_d2_146(cb_replacement_146):
    feature = _clean(cb_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_146'] = {'inputs': ['cb_replacement_146'], 'func': cb_replacement_d2_146}


def cb_replacement_d2_147(cb_replacement_147):
    feature = _clean(cb_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_147'] = {'inputs': ['cb_replacement_147'], 'func': cb_replacement_d2_147}


def cb_replacement_d2_148(cb_replacement_148):
    feature = _clean(cb_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_148'] = {'inputs': ['cb_replacement_148'], 'func': cb_replacement_d2_148}


def cb_replacement_d2_149(cb_replacement_149):
    feature = _clean(cb_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_149'] = {'inputs': ['cb_replacement_149'], 'func': cb_replacement_d2_149}


def cb_replacement_d2_150(cb_replacement_150):
    feature = _clean(cb_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_150'] = {'inputs': ['cb_replacement_150'], 'func': cb_replacement_d2_150}


def cb_replacement_d2_151(cb_replacement_151):
    feature = _clean(cb_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_151'] = {'inputs': ['cb_replacement_151'], 'func': cb_replacement_d2_151}


def cb_replacement_d2_152(cb_replacement_152):
    feature = _clean(cb_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_152'] = {'inputs': ['cb_replacement_152'], 'func': cb_replacement_d2_152}


def cb_replacement_d2_153(cb_replacement_153):
    feature = _clean(cb_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_153'] = {'inputs': ['cb_replacement_153'], 'func': cb_replacement_d2_153}


def cb_replacement_d2_154(cb_replacement_154):
    feature = _clean(cb_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_154'] = {'inputs': ['cb_replacement_154'], 'func': cb_replacement_d2_154}


def cb_replacement_d2_155(cb_replacement_155):
    feature = _clean(cb_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_155'] = {'inputs': ['cb_replacement_155'], 'func': cb_replacement_d2_155}


def cb_replacement_d2_156(cb_replacement_156):
    feature = _clean(cb_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_156'] = {'inputs': ['cb_replacement_156'], 'func': cb_replacement_d2_156}


def cb_replacement_d2_157(cb_replacement_157):
    feature = _clean(cb_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_157'] = {'inputs': ['cb_replacement_157'], 'func': cb_replacement_d2_157}


def cb_replacement_d2_158(cb_replacement_158):
    feature = _clean(cb_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_158'] = {'inputs': ['cb_replacement_158'], 'func': cb_replacement_d2_158}


def cb_replacement_d2_159(cb_replacement_159):
    feature = _clean(cb_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_159'] = {'inputs': ['cb_replacement_159'], 'func': cb_replacement_d2_159}


def cb_replacement_d2_160(cb_replacement_160):
    feature = _clean(cb_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_160'] = {'inputs': ['cb_replacement_160'], 'func': cb_replacement_d2_160}


def cb_replacement_d2_161(cb_replacement_161):
    feature = _clean(cb_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_161'] = {'inputs': ['cb_replacement_161'], 'func': cb_replacement_d2_161}


def cb_replacement_d2_162(cb_replacement_162):
    feature = _clean(cb_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_162'] = {'inputs': ['cb_replacement_162'], 'func': cb_replacement_d2_162}


def cb_replacement_d2_163(cb_replacement_163):
    feature = _clean(cb_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_163'] = {'inputs': ['cb_replacement_163'], 'func': cb_replacement_d2_163}


def cb_replacement_d2_164(cb_replacement_164):
    feature = _clean(cb_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_164'] = {'inputs': ['cb_replacement_164'], 'func': cb_replacement_d2_164}


def cb_replacement_d2_165(cb_replacement_165):
    feature = _clean(cb_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_165'] = {'inputs': ['cb_replacement_165'], 'func': cb_replacement_d2_165}


def cb_replacement_d2_166(cb_replacement_166):
    feature = _clean(cb_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
CB_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['cb_replacement_d2_166'] = {'inputs': ['cb_replacement_166'], 'func': cb_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def cbr_base_universe_d2_001_cbr_003_fcf_burn_to_cash_63(cbr_003_fcf_burn_to_cash_63):
    return _base_universe_d2(cbr_003_fcf_burn_to_cash_63, 1)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_001_cbr_003_fcf_burn_to_cash_63'] = {'inputs': ['cbr_003_fcf_burn_to_cash_63'], 'func': cbr_base_universe_d2_001_cbr_003_fcf_burn_to_cash_63}


def cbr_base_universe_d2_002_cbr_004_debt_to_equity_84(cbr_004_debt_to_equity_84):
    return _base_universe_d2(cbr_004_debt_to_equity_84, 2)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_002_cbr_004_debt_to_equity_84'] = {'inputs': ['cbr_004_debt_to_equity_84'], 'func': cbr_base_universe_d2_002_cbr_004_debt_to_equity_84}


def cbr_base_universe_d2_003_cbr_005_debt_to_assets_126(cbr_005_debt_to_assets_126):
    return _base_universe_d2(cbr_005_debt_to_assets_126, 3)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_003_cbr_005_debt_to_assets_126'] = {'inputs': ['cbr_005_debt_to_assets_126'], 'func': cbr_base_universe_d2_003_cbr_005_debt_to_assets_126}


def cbr_base_universe_d2_004_cbr_012_accrual_gap_1260(cbr_012_accrual_gap_1260):
    return _base_universe_d2(cbr_012_accrual_gap_1260, 4)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_004_cbr_012_accrual_gap_1260'] = {'inputs': ['cbr_012_accrual_gap_1260'], 'func': cbr_base_universe_d2_004_cbr_012_accrual_gap_1260}


def cbr_base_universe_d2_005_cbr_016_debt_to_equity_21(cbr_016_debt_to_equity_21):
    return _base_universe_d2(cbr_016_debt_to_equity_21, 5)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_005_cbr_016_debt_to_equity_21'] = {'inputs': ['cbr_016_debt_to_equity_21'], 'func': cbr_base_universe_d2_005_cbr_016_debt_to_equity_21}


def cbr_base_universe_d2_006_cbr_017_debt_to_assets_42(cbr_017_debt_to_assets_42):
    return _base_universe_d2(cbr_017_debt_to_assets_42, 6)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_006_cbr_017_debt_to_assets_42'] = {'inputs': ['cbr_017_debt_to_assets_42'], 'func': cbr_base_universe_d2_006_cbr_017_debt_to_assets_42}


def cbr_base_universe_d2_007_cbr_024_accrual_gap_504(cbr_024_accrual_gap_504):
    return _base_universe_d2(cbr_024_accrual_gap_504, 7)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_007_cbr_024_accrual_gap_504'] = {'inputs': ['cbr_024_accrual_gap_504'], 'func': cbr_base_universe_d2_007_cbr_024_accrual_gap_504}


def cbr_base_universe_d2_008_cbr_027_fcf_burn_to_cash_1260(cbr_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(cbr_027_fcf_burn_to_cash_1260, 8)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_008_cbr_027_fcf_burn_to_cash_1260'] = {'inputs': ['cbr_027_fcf_burn_to_cash_1260'], 'func': cbr_base_universe_d2_008_cbr_027_fcf_burn_to_cash_1260}


def cbr_base_universe_d2_009_cbr_028_debt_to_equity_1512(cbr_028_debt_to_equity_1512):
    return _base_universe_d2(cbr_028_debt_to_equity_1512, 9)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_009_cbr_028_debt_to_equity_1512'] = {'inputs': ['cbr_028_debt_to_equity_1512'], 'func': cbr_base_universe_d2_009_cbr_028_debt_to_equity_1512}


def cbr_base_universe_d2_010_cbr_029_debt_to_assets_63(cbr_029_debt_to_assets_63):
    return _base_universe_d2(cbr_029_debt_to_assets_63, 10)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_010_cbr_029_debt_to_assets_63'] = {'inputs': ['cbr_029_debt_to_assets_63'], 'func': cbr_base_universe_d2_010_cbr_029_debt_to_assets_63}


def cbr_base_universe_d2_011_cbr_031_interest_coverage_stress_21(cbr_031_interest_coverage_stress_21):
    return _base_universe_d2(cbr_031_interest_coverage_stress_21, 11)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_011_cbr_031_interest_coverage_stress_21'] = {'inputs': ['cbr_031_interest_coverage_stress_21'], 'func': cbr_base_universe_d2_011_cbr_031_interest_coverage_stress_21}


def cbr_base_universe_d2_012_cbr_036_accrual_gap_189(cbr_036_accrual_gap_189):
    return _base_universe_d2(cbr_036_accrual_gap_189, 12)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_012_cbr_036_accrual_gap_189'] = {'inputs': ['cbr_036_accrual_gap_189'], 'func': cbr_base_universe_d2_012_cbr_036_accrual_gap_189}


def cbr_base_universe_d2_013_cbr_039_fcf_burn_to_cash_504(cbr_039_fcf_burn_to_cash_504):
    return _base_universe_d2(cbr_039_fcf_burn_to_cash_504, 13)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_013_cbr_039_fcf_burn_to_cash_504'] = {'inputs': ['cbr_039_fcf_burn_to_cash_504'], 'func': cbr_base_universe_d2_013_cbr_039_fcf_burn_to_cash_504}


def cbr_base_universe_d2_014_cbr_040_debt_to_equity_756(cbr_040_debt_to_equity_756):
    return _base_universe_d2(cbr_040_debt_to_equity_756, 14)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_014_cbr_040_debt_to_equity_756'] = {'inputs': ['cbr_040_debt_to_equity_756'], 'func': cbr_base_universe_d2_014_cbr_040_debt_to_equity_756}


def cbr_base_universe_d2_015_cbr_041_debt_to_assets_1008(cbr_041_debt_to_assets_1008):
    return _base_universe_d2(cbr_041_debt_to_assets_1008, 15)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_015_cbr_041_debt_to_assets_1008'] = {'inputs': ['cbr_041_debt_to_assets_1008'], 'func': cbr_base_universe_d2_015_cbr_041_debt_to_assets_1008}


def cbr_base_universe_d2_016_cbr_043_interest_coverage_stress_1512(cbr_043_interest_coverage_stress_1512):
    return _base_universe_d2(cbr_043_interest_coverage_stress_1512, 16)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_016_cbr_043_interest_coverage_stress_1512'] = {'inputs': ['cbr_043_interest_coverage_stress_1512'], 'func': cbr_base_universe_d2_016_cbr_043_interest_coverage_stress_1512}


def cbr_base_universe_d2_017_cbr_048_accrual_gap_63(cbr_048_accrual_gap_63):
    return _base_universe_d2(cbr_048_accrual_gap_63, 17)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_017_cbr_048_accrual_gap_63'] = {'inputs': ['cbr_048_accrual_gap_63'], 'func': cbr_base_universe_d2_017_cbr_048_accrual_gap_63}


def cbr_base_universe_d2_018_cbr_051_fcf_burn_to_cash_189(cbr_051_fcf_burn_to_cash_189):
    return _base_universe_d2(cbr_051_fcf_burn_to_cash_189, 18)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_018_cbr_051_fcf_burn_to_cash_189'] = {'inputs': ['cbr_051_fcf_burn_to_cash_189'], 'func': cbr_base_universe_d2_018_cbr_051_fcf_burn_to_cash_189}


def cbr_base_universe_d2_019_cbr_052_debt_to_equity_252(cbr_052_debt_to_equity_252):
    return _base_universe_d2(cbr_052_debt_to_equity_252, 19)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_019_cbr_052_debt_to_equity_252'] = {'inputs': ['cbr_052_debt_to_equity_252'], 'func': cbr_base_universe_d2_019_cbr_052_debt_to_equity_252}


def cbr_base_universe_d2_020_cbr_053_debt_to_assets_378(cbr_053_debt_to_assets_378):
    return _base_universe_d2(cbr_053_debt_to_assets_378, 20)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_020_cbr_053_debt_to_assets_378'] = {'inputs': ['cbr_053_debt_to_assets_378'], 'func': cbr_base_universe_d2_020_cbr_053_debt_to_assets_378}


def cbr_base_universe_d2_021_cbr_055_interest_coverage_stress_756(cbr_055_interest_coverage_stress_756):
    return _base_universe_d2(cbr_055_interest_coverage_stress_756, 21)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_021_cbr_055_interest_coverage_stress_756'] = {'inputs': ['cbr_055_interest_coverage_stress_756'], 'func': cbr_base_universe_d2_021_cbr_055_interest_coverage_stress_756}


def cbr_base_universe_d2_022_cbr_060_accrual_gap_252(cbr_060_accrual_gap_252):
    return _base_universe_d2(cbr_060_accrual_gap_252, 22)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_022_cbr_060_accrual_gap_252'] = {'inputs': ['cbr_060_accrual_gap_252'], 'func': cbr_base_universe_d2_022_cbr_060_accrual_gap_252}


def cbr_base_universe_d2_023_cbr_basefill_001(cbr_basefill_001):
    return _base_universe_d2(cbr_basefill_001, 23)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_023_cbr_basefill_001'] = {'inputs': ['cbr_basefill_001'], 'func': cbr_base_universe_d2_023_cbr_basefill_001}


def cbr_base_universe_d2_024_cbr_basefill_002(cbr_basefill_002):
    return _base_universe_d2(cbr_basefill_002, 24)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_024_cbr_basefill_002'] = {'inputs': ['cbr_basefill_002'], 'func': cbr_base_universe_d2_024_cbr_basefill_002}


def cbr_base_universe_d2_025_cbr_basefill_006(cbr_basefill_006):
    return _base_universe_d2(cbr_basefill_006, 25)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_025_cbr_basefill_006'] = {'inputs': ['cbr_basefill_006'], 'func': cbr_base_universe_d2_025_cbr_basefill_006}


def cbr_base_universe_d2_026_cbr_basefill_008(cbr_basefill_008):
    return _base_universe_d2(cbr_basefill_008, 26)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_026_cbr_basefill_008'] = {'inputs': ['cbr_basefill_008'], 'func': cbr_base_universe_d2_026_cbr_basefill_008}


def cbr_base_universe_d2_027_cbr_basefill_009(cbr_basefill_009):
    return _base_universe_d2(cbr_basefill_009, 27)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_027_cbr_basefill_009'] = {'inputs': ['cbr_basefill_009'], 'func': cbr_base_universe_d2_027_cbr_basefill_009}


def cbr_base_universe_d2_028_cbr_basefill_010(cbr_basefill_010):
    return _base_universe_d2(cbr_basefill_010, 28)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_028_cbr_basefill_010'] = {'inputs': ['cbr_basefill_010'], 'func': cbr_base_universe_d2_028_cbr_basefill_010}


def cbr_base_universe_d2_029_cbr_basefill_011(cbr_basefill_011):
    return _base_universe_d2(cbr_basefill_011, 29)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_029_cbr_basefill_011'] = {'inputs': ['cbr_basefill_011'], 'func': cbr_base_universe_d2_029_cbr_basefill_011}


def cbr_base_universe_d2_030_cbr_basefill_013(cbr_basefill_013):
    return _base_universe_d2(cbr_basefill_013, 30)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_030_cbr_basefill_013'] = {'inputs': ['cbr_basefill_013'], 'func': cbr_base_universe_d2_030_cbr_basefill_013}


def cbr_base_universe_d2_031_cbr_basefill_014(cbr_basefill_014):
    return _base_universe_d2(cbr_basefill_014, 31)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_031_cbr_basefill_014'] = {'inputs': ['cbr_basefill_014'], 'func': cbr_base_universe_d2_031_cbr_basefill_014}


def cbr_base_universe_d2_032_cbr_basefill_015(cbr_basefill_015):
    return _base_universe_d2(cbr_basefill_015, 32)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_032_cbr_basefill_015'] = {'inputs': ['cbr_basefill_015'], 'func': cbr_base_universe_d2_032_cbr_basefill_015}


def cbr_base_universe_d2_033_cbr_basefill_018(cbr_basefill_018):
    return _base_universe_d2(cbr_basefill_018, 33)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_033_cbr_basefill_018'] = {'inputs': ['cbr_basefill_018'], 'func': cbr_base_universe_d2_033_cbr_basefill_018}


def cbr_base_universe_d2_034_cbr_basefill_020(cbr_basefill_020):
    return _base_universe_d2(cbr_basefill_020, 34)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_034_cbr_basefill_020'] = {'inputs': ['cbr_basefill_020'], 'func': cbr_base_universe_d2_034_cbr_basefill_020}


def cbr_base_universe_d2_035_cbr_basefill_021(cbr_basefill_021):
    return _base_universe_d2(cbr_basefill_021, 35)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_035_cbr_basefill_021'] = {'inputs': ['cbr_basefill_021'], 'func': cbr_base_universe_d2_035_cbr_basefill_021}


def cbr_base_universe_d2_036_cbr_basefill_022(cbr_basefill_022):
    return _base_universe_d2(cbr_basefill_022, 36)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_036_cbr_basefill_022'] = {'inputs': ['cbr_basefill_022'], 'func': cbr_base_universe_d2_036_cbr_basefill_022}


def cbr_base_universe_d2_037_cbr_basefill_023(cbr_basefill_023):
    return _base_universe_d2(cbr_basefill_023, 37)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_037_cbr_basefill_023'] = {'inputs': ['cbr_basefill_023'], 'func': cbr_base_universe_d2_037_cbr_basefill_023}


def cbr_base_universe_d2_038_cbr_basefill_025(cbr_basefill_025):
    return _base_universe_d2(cbr_basefill_025, 38)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_038_cbr_basefill_025'] = {'inputs': ['cbr_basefill_025'], 'func': cbr_base_universe_d2_038_cbr_basefill_025}


def cbr_base_universe_d2_039_cbr_basefill_026(cbr_basefill_026):
    return _base_universe_d2(cbr_basefill_026, 39)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_039_cbr_basefill_026'] = {'inputs': ['cbr_basefill_026'], 'func': cbr_base_universe_d2_039_cbr_basefill_026}


def cbr_base_universe_d2_040_cbr_basefill_030(cbr_basefill_030):
    return _base_universe_d2(cbr_basefill_030, 40)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_040_cbr_basefill_030'] = {'inputs': ['cbr_basefill_030'], 'func': cbr_base_universe_d2_040_cbr_basefill_030}


def cbr_base_universe_d2_041_cbr_basefill_032(cbr_basefill_032):
    return _base_universe_d2(cbr_basefill_032, 41)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_041_cbr_basefill_032'] = {'inputs': ['cbr_basefill_032'], 'func': cbr_base_universe_d2_041_cbr_basefill_032}


def cbr_base_universe_d2_042_cbr_basefill_033(cbr_basefill_033):
    return _base_universe_d2(cbr_basefill_033, 42)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_042_cbr_basefill_033'] = {'inputs': ['cbr_basefill_033'], 'func': cbr_base_universe_d2_042_cbr_basefill_033}


def cbr_base_universe_d2_043_cbr_basefill_034(cbr_basefill_034):
    return _base_universe_d2(cbr_basefill_034, 43)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_043_cbr_basefill_034'] = {'inputs': ['cbr_basefill_034'], 'func': cbr_base_universe_d2_043_cbr_basefill_034}


def cbr_base_universe_d2_044_cbr_basefill_035(cbr_basefill_035):
    return _base_universe_d2(cbr_basefill_035, 44)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_044_cbr_basefill_035'] = {'inputs': ['cbr_basefill_035'], 'func': cbr_base_universe_d2_044_cbr_basefill_035}


def cbr_base_universe_d2_045_cbr_basefill_037(cbr_basefill_037):
    return _base_universe_d2(cbr_basefill_037, 45)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_045_cbr_basefill_037'] = {'inputs': ['cbr_basefill_037'], 'func': cbr_base_universe_d2_045_cbr_basefill_037}


def cbr_base_universe_d2_046_cbr_basefill_038(cbr_basefill_038):
    return _base_universe_d2(cbr_basefill_038, 46)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_046_cbr_basefill_038'] = {'inputs': ['cbr_basefill_038'], 'func': cbr_base_universe_d2_046_cbr_basefill_038}


def cbr_base_universe_d2_047_cbr_basefill_042(cbr_basefill_042):
    return _base_universe_d2(cbr_basefill_042, 47)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_047_cbr_basefill_042'] = {'inputs': ['cbr_basefill_042'], 'func': cbr_base_universe_d2_047_cbr_basefill_042}


def cbr_base_universe_d2_048_cbr_basefill_044(cbr_basefill_044):
    return _base_universe_d2(cbr_basefill_044, 48)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_048_cbr_basefill_044'] = {'inputs': ['cbr_basefill_044'], 'func': cbr_base_universe_d2_048_cbr_basefill_044}


def cbr_base_universe_d2_049_cbr_basefill_045(cbr_basefill_045):
    return _base_universe_d2(cbr_basefill_045, 49)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_049_cbr_basefill_045'] = {'inputs': ['cbr_basefill_045'], 'func': cbr_base_universe_d2_049_cbr_basefill_045}


def cbr_base_universe_d2_050_cbr_basefill_046(cbr_basefill_046):
    return _base_universe_d2(cbr_basefill_046, 50)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_050_cbr_basefill_046'] = {'inputs': ['cbr_basefill_046'], 'func': cbr_base_universe_d2_050_cbr_basefill_046}


def cbr_base_universe_d2_051_cbr_basefill_047(cbr_basefill_047):
    return _base_universe_d2(cbr_basefill_047, 51)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_051_cbr_basefill_047'] = {'inputs': ['cbr_basefill_047'], 'func': cbr_base_universe_d2_051_cbr_basefill_047}


def cbr_base_universe_d2_052_cbr_basefill_049(cbr_basefill_049):
    return _base_universe_d2(cbr_basefill_049, 52)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_052_cbr_basefill_049'] = {'inputs': ['cbr_basefill_049'], 'func': cbr_base_universe_d2_052_cbr_basefill_049}


def cbr_base_universe_d2_053_cbr_basefill_050(cbr_basefill_050):
    return _base_universe_d2(cbr_basefill_050, 53)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_053_cbr_basefill_050'] = {'inputs': ['cbr_basefill_050'], 'func': cbr_base_universe_d2_053_cbr_basefill_050}


def cbr_base_universe_d2_054_cbr_basefill_054(cbr_basefill_054):
    return _base_universe_d2(cbr_basefill_054, 54)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_054_cbr_basefill_054'] = {'inputs': ['cbr_basefill_054'], 'func': cbr_base_universe_d2_054_cbr_basefill_054}


def cbr_base_universe_d2_055_cbr_basefill_056(cbr_basefill_056):
    return _base_universe_d2(cbr_basefill_056, 55)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_055_cbr_basefill_056'] = {'inputs': ['cbr_basefill_056'], 'func': cbr_base_universe_d2_055_cbr_basefill_056}


def cbr_base_universe_d2_056_cbr_basefill_057(cbr_basefill_057):
    return _base_universe_d2(cbr_basefill_057, 56)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_056_cbr_basefill_057'] = {'inputs': ['cbr_basefill_057'], 'func': cbr_base_universe_d2_056_cbr_basefill_057}


def cbr_base_universe_d2_057_cbr_basefill_058(cbr_basefill_058):
    return _base_universe_d2(cbr_basefill_058, 57)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_057_cbr_basefill_058'] = {'inputs': ['cbr_basefill_058'], 'func': cbr_base_universe_d2_057_cbr_basefill_058}


def cbr_base_universe_d2_058_cbr_basefill_059(cbr_basefill_059):
    return _base_universe_d2(cbr_basefill_059, 58)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_058_cbr_basefill_059'] = {'inputs': ['cbr_basefill_059'], 'func': cbr_base_universe_d2_058_cbr_basefill_059}


def cbr_base_universe_d2_059_cbr_basefill_061(cbr_basefill_061):
    return _base_universe_d2(cbr_basefill_061, 59)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_059_cbr_basefill_061'] = {'inputs': ['cbr_basefill_061'], 'func': cbr_base_universe_d2_059_cbr_basefill_061}


def cbr_base_universe_d2_060_cbr_basefill_062(cbr_basefill_062):
    return _base_universe_d2(cbr_basefill_062, 60)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_060_cbr_basefill_062'] = {'inputs': ['cbr_basefill_062'], 'func': cbr_base_universe_d2_060_cbr_basefill_062}


def cbr_base_universe_d2_061_cbr_basefill_063(cbr_basefill_063):
    return _base_universe_d2(cbr_basefill_063, 61)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_061_cbr_basefill_063'] = {'inputs': ['cbr_basefill_063'], 'func': cbr_base_universe_d2_061_cbr_basefill_063}


def cbr_base_universe_d2_062_cbr_basefill_064(cbr_basefill_064):
    return _base_universe_d2(cbr_basefill_064, 62)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_062_cbr_basefill_064'] = {'inputs': ['cbr_basefill_064'], 'func': cbr_base_universe_d2_062_cbr_basefill_064}


def cbr_base_universe_d2_063_cbr_basefill_065(cbr_basefill_065):
    return _base_universe_d2(cbr_basefill_065, 63)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_063_cbr_basefill_065'] = {'inputs': ['cbr_basefill_065'], 'func': cbr_base_universe_d2_063_cbr_basefill_065}


def cbr_base_universe_d2_064_cbr_basefill_066(cbr_basefill_066):
    return _base_universe_d2(cbr_basefill_066, 64)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_064_cbr_basefill_066'] = {'inputs': ['cbr_basefill_066'], 'func': cbr_base_universe_d2_064_cbr_basefill_066}


def cbr_base_universe_d2_065_cbr_basefill_067(cbr_basefill_067):
    return _base_universe_d2(cbr_basefill_067, 65)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_065_cbr_basefill_067'] = {'inputs': ['cbr_basefill_067'], 'func': cbr_base_universe_d2_065_cbr_basefill_067}


def cbr_base_universe_d2_066_cbr_basefill_068(cbr_basefill_068):
    return _base_universe_d2(cbr_basefill_068, 66)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_066_cbr_basefill_068'] = {'inputs': ['cbr_basefill_068'], 'func': cbr_base_universe_d2_066_cbr_basefill_068}


def cbr_base_universe_d2_067_cbr_basefill_069(cbr_basefill_069):
    return _base_universe_d2(cbr_basefill_069, 67)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_067_cbr_basefill_069'] = {'inputs': ['cbr_basefill_069'], 'func': cbr_base_universe_d2_067_cbr_basefill_069}


def cbr_base_universe_d2_068_cbr_basefill_070(cbr_basefill_070):
    return _base_universe_d2(cbr_basefill_070, 68)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_068_cbr_basefill_070'] = {'inputs': ['cbr_basefill_070'], 'func': cbr_base_universe_d2_068_cbr_basefill_070}


def cbr_base_universe_d2_069_cbr_basefill_071(cbr_basefill_071):
    return _base_universe_d2(cbr_basefill_071, 69)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_069_cbr_basefill_071'] = {'inputs': ['cbr_basefill_071'], 'func': cbr_base_universe_d2_069_cbr_basefill_071}


def cbr_base_universe_d2_070_cbr_basefill_072(cbr_basefill_072):
    return _base_universe_d2(cbr_basefill_072, 70)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_070_cbr_basefill_072'] = {'inputs': ['cbr_basefill_072'], 'func': cbr_base_universe_d2_070_cbr_basefill_072}


def cbr_base_universe_d2_071_cbr_basefill_073(cbr_basefill_073):
    return _base_universe_d2(cbr_basefill_073, 71)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_071_cbr_basefill_073'] = {'inputs': ['cbr_basefill_073'], 'func': cbr_base_universe_d2_071_cbr_basefill_073}


def cbr_base_universe_d2_072_cbr_basefill_074(cbr_basefill_074):
    return _base_universe_d2(cbr_basefill_074, 72)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_072_cbr_basefill_074'] = {'inputs': ['cbr_basefill_074'], 'func': cbr_base_universe_d2_072_cbr_basefill_074}


def cbr_base_universe_d2_073_cbr_basefill_075(cbr_basefill_075):
    return _base_universe_d2(cbr_basefill_075, 73)
CBR_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['cbr_base_universe_d2_073_cbr_basefill_075'] = {'inputs': ['cbr_basefill_075'], 'func': cbr_base_universe_d2_073_cbr_basefill_075}
