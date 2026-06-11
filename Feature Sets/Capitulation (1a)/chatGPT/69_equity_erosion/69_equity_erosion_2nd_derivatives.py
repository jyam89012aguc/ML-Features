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



def eqe_151_eqe_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def eqe_152_eqe_007_interest_coverage_stress_252_roc_42(eqe_007_interest_coverage_stress_252):
    feature = _s(eqe_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def eqe_153_eqe_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def eqe_154_eqe_019_interest_coverage_stress_84_roc_378(eqe_019_interest_coverage_stress_84):
    feature = _s(eqe_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def eqe_155_eqe_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















EQUITY_EROSION_REGISTRY_2ND_DERIVATIVES = {
    'eqe_151_eqe_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': eqe_151_eqe_001_netinc_decline_1_roc_1},
    'eqe_152_eqe_007_interest_coverage_stress_252_roc_42': {'inputs': ['eqe_007_interest_coverage_stress_252'], 'func': eqe_152_eqe_007_interest_coverage_stress_252_roc_42},
    'eqe_153_eqe_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': eqe_153_eqe_013_netinc_decline_1_roc_126},
    'eqe_154_eqe_019_interest_coverage_stress_84_roc_378': {'inputs': ['eqe_019_interest_coverage_stress_84'], 'func': eqe_154_eqe_019_interest_coverage_stress_84_roc_378},
    'eqe_155_eqe_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': eqe_155_eqe_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ee_replacement_d2_001(ee_replacement_001):
    feature = _clean(ee_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_001'] = {'inputs': ['ee_replacement_001'], 'func': ee_replacement_d2_001}


def ee_replacement_d2_002(ee_replacement_002):
    feature = _clean(ee_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_002'] = {'inputs': ['ee_replacement_002'], 'func': ee_replacement_d2_002}


def ee_replacement_d2_003(ee_replacement_003):
    feature = _clean(ee_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_003'] = {'inputs': ['ee_replacement_003'], 'func': ee_replacement_d2_003}


def ee_replacement_d2_004(ee_replacement_004):
    feature = _clean(ee_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_004'] = {'inputs': ['ee_replacement_004'], 'func': ee_replacement_d2_004}


def ee_replacement_d2_005(ee_replacement_005):
    feature = _clean(ee_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_005'] = {'inputs': ['ee_replacement_005'], 'func': ee_replacement_d2_005}


def ee_replacement_d2_006(ee_replacement_006):
    feature = _clean(ee_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_006'] = {'inputs': ['ee_replacement_006'], 'func': ee_replacement_d2_006}


def ee_replacement_d2_007(ee_replacement_007):
    feature = _clean(ee_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_007'] = {'inputs': ['ee_replacement_007'], 'func': ee_replacement_d2_007}


def ee_replacement_d2_008(ee_replacement_008):
    feature = _clean(ee_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_008'] = {'inputs': ['ee_replacement_008'], 'func': ee_replacement_d2_008}


def ee_replacement_d2_009(ee_replacement_009):
    feature = _clean(ee_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_009'] = {'inputs': ['ee_replacement_009'], 'func': ee_replacement_d2_009}


def ee_replacement_d2_010(ee_replacement_010):
    feature = _clean(ee_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_010'] = {'inputs': ['ee_replacement_010'], 'func': ee_replacement_d2_010}


def ee_replacement_d2_011(ee_replacement_011):
    feature = _clean(ee_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_011'] = {'inputs': ['ee_replacement_011'], 'func': ee_replacement_d2_011}


def ee_replacement_d2_012(ee_replacement_012):
    feature = _clean(ee_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_012'] = {'inputs': ['ee_replacement_012'], 'func': ee_replacement_d2_012}


def ee_replacement_d2_013(ee_replacement_013):
    feature = _clean(ee_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_013'] = {'inputs': ['ee_replacement_013'], 'func': ee_replacement_d2_013}


def ee_replacement_d2_014(ee_replacement_014):
    feature = _clean(ee_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_014'] = {'inputs': ['ee_replacement_014'], 'func': ee_replacement_d2_014}


def ee_replacement_d2_015(ee_replacement_015):
    feature = _clean(ee_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_015'] = {'inputs': ['ee_replacement_015'], 'func': ee_replacement_d2_015}


def ee_replacement_d2_016(ee_replacement_016):
    feature = _clean(ee_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_016'] = {'inputs': ['ee_replacement_016'], 'func': ee_replacement_d2_016}


def ee_replacement_d2_017(ee_replacement_017):
    feature = _clean(ee_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_017'] = {'inputs': ['ee_replacement_017'], 'func': ee_replacement_d2_017}


def ee_replacement_d2_018(ee_replacement_018):
    feature = _clean(ee_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_018'] = {'inputs': ['ee_replacement_018'], 'func': ee_replacement_d2_018}


def ee_replacement_d2_019(ee_replacement_019):
    feature = _clean(ee_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_019'] = {'inputs': ['ee_replacement_019'], 'func': ee_replacement_d2_019}


def ee_replacement_d2_020(ee_replacement_020):
    feature = _clean(ee_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_020'] = {'inputs': ['ee_replacement_020'], 'func': ee_replacement_d2_020}


def ee_replacement_d2_021(ee_replacement_021):
    feature = _clean(ee_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_021'] = {'inputs': ['ee_replacement_021'], 'func': ee_replacement_d2_021}


def ee_replacement_d2_022(ee_replacement_022):
    feature = _clean(ee_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_022'] = {'inputs': ['ee_replacement_022'], 'func': ee_replacement_d2_022}


def ee_replacement_d2_023(ee_replacement_023):
    feature = _clean(ee_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_023'] = {'inputs': ['ee_replacement_023'], 'func': ee_replacement_d2_023}


def ee_replacement_d2_024(ee_replacement_024):
    feature = _clean(ee_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_024'] = {'inputs': ['ee_replacement_024'], 'func': ee_replacement_d2_024}


def ee_replacement_d2_025(ee_replacement_025):
    feature = _clean(ee_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_025'] = {'inputs': ['ee_replacement_025'], 'func': ee_replacement_d2_025}


def ee_replacement_d2_026(ee_replacement_026):
    feature = _clean(ee_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_026'] = {'inputs': ['ee_replacement_026'], 'func': ee_replacement_d2_026}


def ee_replacement_d2_027(ee_replacement_027):
    feature = _clean(ee_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_027'] = {'inputs': ['ee_replacement_027'], 'func': ee_replacement_d2_027}


def ee_replacement_d2_028(ee_replacement_028):
    feature = _clean(ee_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_028'] = {'inputs': ['ee_replacement_028'], 'func': ee_replacement_d2_028}


def ee_replacement_d2_029(ee_replacement_029):
    feature = _clean(ee_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_029'] = {'inputs': ['ee_replacement_029'], 'func': ee_replacement_d2_029}


def ee_replacement_d2_030(ee_replacement_030):
    feature = _clean(ee_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_030'] = {'inputs': ['ee_replacement_030'], 'func': ee_replacement_d2_030}


def ee_replacement_d2_031(ee_replacement_031):
    feature = _clean(ee_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_031'] = {'inputs': ['ee_replacement_031'], 'func': ee_replacement_d2_031}


def ee_replacement_d2_032(ee_replacement_032):
    feature = _clean(ee_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_032'] = {'inputs': ['ee_replacement_032'], 'func': ee_replacement_d2_032}


def ee_replacement_d2_033(ee_replacement_033):
    feature = _clean(ee_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_033'] = {'inputs': ['ee_replacement_033'], 'func': ee_replacement_d2_033}


def ee_replacement_d2_034(ee_replacement_034):
    feature = _clean(ee_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_034'] = {'inputs': ['ee_replacement_034'], 'func': ee_replacement_d2_034}


def ee_replacement_d2_035(ee_replacement_035):
    feature = _clean(ee_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_035'] = {'inputs': ['ee_replacement_035'], 'func': ee_replacement_d2_035}


def ee_replacement_d2_036(ee_replacement_036):
    feature = _clean(ee_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_036'] = {'inputs': ['ee_replacement_036'], 'func': ee_replacement_d2_036}


def ee_replacement_d2_037(ee_replacement_037):
    feature = _clean(ee_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_037'] = {'inputs': ['ee_replacement_037'], 'func': ee_replacement_d2_037}


def ee_replacement_d2_038(ee_replacement_038):
    feature = _clean(ee_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_038'] = {'inputs': ['ee_replacement_038'], 'func': ee_replacement_d2_038}


def ee_replacement_d2_039(ee_replacement_039):
    feature = _clean(ee_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_039'] = {'inputs': ['ee_replacement_039'], 'func': ee_replacement_d2_039}


def ee_replacement_d2_040(ee_replacement_040):
    feature = _clean(ee_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_040'] = {'inputs': ['ee_replacement_040'], 'func': ee_replacement_d2_040}


def ee_replacement_d2_041(ee_replacement_041):
    feature = _clean(ee_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_041'] = {'inputs': ['ee_replacement_041'], 'func': ee_replacement_d2_041}


def ee_replacement_d2_042(ee_replacement_042):
    feature = _clean(ee_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_042'] = {'inputs': ['ee_replacement_042'], 'func': ee_replacement_d2_042}


def ee_replacement_d2_043(ee_replacement_043):
    feature = _clean(ee_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_043'] = {'inputs': ['ee_replacement_043'], 'func': ee_replacement_d2_043}


def ee_replacement_d2_044(ee_replacement_044):
    feature = _clean(ee_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_044'] = {'inputs': ['ee_replacement_044'], 'func': ee_replacement_d2_044}


def ee_replacement_d2_045(ee_replacement_045):
    feature = _clean(ee_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_045'] = {'inputs': ['ee_replacement_045'], 'func': ee_replacement_d2_045}


def ee_replacement_d2_046(ee_replacement_046):
    feature = _clean(ee_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_046'] = {'inputs': ['ee_replacement_046'], 'func': ee_replacement_d2_046}


def ee_replacement_d2_047(ee_replacement_047):
    feature = _clean(ee_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_047'] = {'inputs': ['ee_replacement_047'], 'func': ee_replacement_d2_047}


def ee_replacement_d2_048(ee_replacement_048):
    feature = _clean(ee_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_048'] = {'inputs': ['ee_replacement_048'], 'func': ee_replacement_d2_048}


def ee_replacement_d2_049(ee_replacement_049):
    feature = _clean(ee_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_049'] = {'inputs': ['ee_replacement_049'], 'func': ee_replacement_d2_049}


def ee_replacement_d2_050(ee_replacement_050):
    feature = _clean(ee_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_050'] = {'inputs': ['ee_replacement_050'], 'func': ee_replacement_d2_050}


def ee_replacement_d2_051(ee_replacement_051):
    feature = _clean(ee_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_051'] = {'inputs': ['ee_replacement_051'], 'func': ee_replacement_d2_051}


def ee_replacement_d2_052(ee_replacement_052):
    feature = _clean(ee_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_052'] = {'inputs': ['ee_replacement_052'], 'func': ee_replacement_d2_052}


def ee_replacement_d2_053(ee_replacement_053):
    feature = _clean(ee_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_053'] = {'inputs': ['ee_replacement_053'], 'func': ee_replacement_d2_053}


def ee_replacement_d2_054(ee_replacement_054):
    feature = _clean(ee_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_054'] = {'inputs': ['ee_replacement_054'], 'func': ee_replacement_d2_054}


def ee_replacement_d2_055(ee_replacement_055):
    feature = _clean(ee_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_055'] = {'inputs': ['ee_replacement_055'], 'func': ee_replacement_d2_055}


def ee_replacement_d2_056(ee_replacement_056):
    feature = _clean(ee_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_056'] = {'inputs': ['ee_replacement_056'], 'func': ee_replacement_d2_056}


def ee_replacement_d2_057(ee_replacement_057):
    feature = _clean(ee_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_057'] = {'inputs': ['ee_replacement_057'], 'func': ee_replacement_d2_057}


def ee_replacement_d2_058(ee_replacement_058):
    feature = _clean(ee_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_058'] = {'inputs': ['ee_replacement_058'], 'func': ee_replacement_d2_058}


def ee_replacement_d2_059(ee_replacement_059):
    feature = _clean(ee_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_059'] = {'inputs': ['ee_replacement_059'], 'func': ee_replacement_d2_059}


def ee_replacement_d2_060(ee_replacement_060):
    feature = _clean(ee_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_060'] = {'inputs': ['ee_replacement_060'], 'func': ee_replacement_d2_060}


def ee_replacement_d2_061(ee_replacement_061):
    feature = _clean(ee_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_061'] = {'inputs': ['ee_replacement_061'], 'func': ee_replacement_d2_061}


def ee_replacement_d2_062(ee_replacement_062):
    feature = _clean(ee_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_062'] = {'inputs': ['ee_replacement_062'], 'func': ee_replacement_d2_062}


def ee_replacement_d2_063(ee_replacement_063):
    feature = _clean(ee_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_063'] = {'inputs': ['ee_replacement_063'], 'func': ee_replacement_d2_063}


def ee_replacement_d2_064(ee_replacement_064):
    feature = _clean(ee_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_064'] = {'inputs': ['ee_replacement_064'], 'func': ee_replacement_d2_064}


def ee_replacement_d2_065(ee_replacement_065):
    feature = _clean(ee_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_065'] = {'inputs': ['ee_replacement_065'], 'func': ee_replacement_d2_065}


def ee_replacement_d2_066(ee_replacement_066):
    feature = _clean(ee_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_066'] = {'inputs': ['ee_replacement_066'], 'func': ee_replacement_d2_066}


def ee_replacement_d2_067(ee_replacement_067):
    feature = _clean(ee_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_067'] = {'inputs': ['ee_replacement_067'], 'func': ee_replacement_d2_067}


def ee_replacement_d2_068(ee_replacement_068):
    feature = _clean(ee_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_068'] = {'inputs': ['ee_replacement_068'], 'func': ee_replacement_d2_068}


def ee_replacement_d2_069(ee_replacement_069):
    feature = _clean(ee_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_069'] = {'inputs': ['ee_replacement_069'], 'func': ee_replacement_d2_069}


def ee_replacement_d2_070(ee_replacement_070):
    feature = _clean(ee_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_070'] = {'inputs': ['ee_replacement_070'], 'func': ee_replacement_d2_070}


def ee_replacement_d2_071(ee_replacement_071):
    feature = _clean(ee_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_071'] = {'inputs': ['ee_replacement_071'], 'func': ee_replacement_d2_071}


def ee_replacement_d2_072(ee_replacement_072):
    feature = _clean(ee_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_072'] = {'inputs': ['ee_replacement_072'], 'func': ee_replacement_d2_072}


def ee_replacement_d2_073(ee_replacement_073):
    feature = _clean(ee_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_073'] = {'inputs': ['ee_replacement_073'], 'func': ee_replacement_d2_073}


def ee_replacement_d2_074(ee_replacement_074):
    feature = _clean(ee_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_074'] = {'inputs': ['ee_replacement_074'], 'func': ee_replacement_d2_074}


def ee_replacement_d2_075(ee_replacement_075):
    feature = _clean(ee_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_075'] = {'inputs': ['ee_replacement_075'], 'func': ee_replacement_d2_075}


def ee_replacement_d2_076(ee_replacement_076):
    feature = _clean(ee_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_076'] = {'inputs': ['ee_replacement_076'], 'func': ee_replacement_d2_076}


def ee_replacement_d2_077(ee_replacement_077):
    feature = _clean(ee_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_077'] = {'inputs': ['ee_replacement_077'], 'func': ee_replacement_d2_077}


def ee_replacement_d2_078(ee_replacement_078):
    feature = _clean(ee_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_078'] = {'inputs': ['ee_replacement_078'], 'func': ee_replacement_d2_078}


def ee_replacement_d2_079(ee_replacement_079):
    feature = _clean(ee_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_079'] = {'inputs': ['ee_replacement_079'], 'func': ee_replacement_d2_079}


def ee_replacement_d2_080(ee_replacement_080):
    feature = _clean(ee_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_080'] = {'inputs': ['ee_replacement_080'], 'func': ee_replacement_d2_080}


def ee_replacement_d2_081(ee_replacement_081):
    feature = _clean(ee_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_081'] = {'inputs': ['ee_replacement_081'], 'func': ee_replacement_d2_081}


def ee_replacement_d2_082(ee_replacement_082):
    feature = _clean(ee_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_082'] = {'inputs': ['ee_replacement_082'], 'func': ee_replacement_d2_082}


def ee_replacement_d2_083(ee_replacement_083):
    feature = _clean(ee_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_083'] = {'inputs': ['ee_replacement_083'], 'func': ee_replacement_d2_083}


def ee_replacement_d2_084(ee_replacement_084):
    feature = _clean(ee_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_084'] = {'inputs': ['ee_replacement_084'], 'func': ee_replacement_d2_084}


def ee_replacement_d2_085(ee_replacement_085):
    feature = _clean(ee_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_085'] = {'inputs': ['ee_replacement_085'], 'func': ee_replacement_d2_085}


def ee_replacement_d2_086(ee_replacement_086):
    feature = _clean(ee_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_086'] = {'inputs': ['ee_replacement_086'], 'func': ee_replacement_d2_086}


def ee_replacement_d2_087(ee_replacement_087):
    feature = _clean(ee_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_087'] = {'inputs': ['ee_replacement_087'], 'func': ee_replacement_d2_087}


def ee_replacement_d2_088(ee_replacement_088):
    feature = _clean(ee_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_088'] = {'inputs': ['ee_replacement_088'], 'func': ee_replacement_d2_088}


def ee_replacement_d2_089(ee_replacement_089):
    feature = _clean(ee_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_089'] = {'inputs': ['ee_replacement_089'], 'func': ee_replacement_d2_089}


def ee_replacement_d2_090(ee_replacement_090):
    feature = _clean(ee_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_090'] = {'inputs': ['ee_replacement_090'], 'func': ee_replacement_d2_090}


def ee_replacement_d2_091(ee_replacement_091):
    feature = _clean(ee_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_091'] = {'inputs': ['ee_replacement_091'], 'func': ee_replacement_d2_091}


def ee_replacement_d2_092(ee_replacement_092):
    feature = _clean(ee_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_092'] = {'inputs': ['ee_replacement_092'], 'func': ee_replacement_d2_092}


def ee_replacement_d2_093(ee_replacement_093):
    feature = _clean(ee_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_093'] = {'inputs': ['ee_replacement_093'], 'func': ee_replacement_d2_093}


def ee_replacement_d2_094(ee_replacement_094):
    feature = _clean(ee_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_094'] = {'inputs': ['ee_replacement_094'], 'func': ee_replacement_d2_094}


def ee_replacement_d2_095(ee_replacement_095):
    feature = _clean(ee_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_095'] = {'inputs': ['ee_replacement_095'], 'func': ee_replacement_d2_095}


def ee_replacement_d2_096(ee_replacement_096):
    feature = _clean(ee_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_096'] = {'inputs': ['ee_replacement_096'], 'func': ee_replacement_d2_096}


def ee_replacement_d2_097(ee_replacement_097):
    feature = _clean(ee_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_097'] = {'inputs': ['ee_replacement_097'], 'func': ee_replacement_d2_097}


def ee_replacement_d2_098(ee_replacement_098):
    feature = _clean(ee_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_098'] = {'inputs': ['ee_replacement_098'], 'func': ee_replacement_d2_098}


def ee_replacement_d2_099(ee_replacement_099):
    feature = _clean(ee_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_099'] = {'inputs': ['ee_replacement_099'], 'func': ee_replacement_d2_099}


def ee_replacement_d2_100(ee_replacement_100):
    feature = _clean(ee_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_100'] = {'inputs': ['ee_replacement_100'], 'func': ee_replacement_d2_100}


def ee_replacement_d2_101(ee_replacement_101):
    feature = _clean(ee_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_101'] = {'inputs': ['ee_replacement_101'], 'func': ee_replacement_d2_101}


def ee_replacement_d2_102(ee_replacement_102):
    feature = _clean(ee_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_102'] = {'inputs': ['ee_replacement_102'], 'func': ee_replacement_d2_102}


def ee_replacement_d2_103(ee_replacement_103):
    feature = _clean(ee_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_103'] = {'inputs': ['ee_replacement_103'], 'func': ee_replacement_d2_103}


def ee_replacement_d2_104(ee_replacement_104):
    feature = _clean(ee_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_104'] = {'inputs': ['ee_replacement_104'], 'func': ee_replacement_d2_104}


def ee_replacement_d2_105(ee_replacement_105):
    feature = _clean(ee_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_105'] = {'inputs': ['ee_replacement_105'], 'func': ee_replacement_d2_105}


def ee_replacement_d2_106(ee_replacement_106):
    feature = _clean(ee_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_106'] = {'inputs': ['ee_replacement_106'], 'func': ee_replacement_d2_106}


def ee_replacement_d2_107(ee_replacement_107):
    feature = _clean(ee_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_107'] = {'inputs': ['ee_replacement_107'], 'func': ee_replacement_d2_107}


def ee_replacement_d2_108(ee_replacement_108):
    feature = _clean(ee_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_108'] = {'inputs': ['ee_replacement_108'], 'func': ee_replacement_d2_108}


def ee_replacement_d2_109(ee_replacement_109):
    feature = _clean(ee_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_109'] = {'inputs': ['ee_replacement_109'], 'func': ee_replacement_d2_109}


def ee_replacement_d2_110(ee_replacement_110):
    feature = _clean(ee_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_110'] = {'inputs': ['ee_replacement_110'], 'func': ee_replacement_d2_110}


def ee_replacement_d2_111(ee_replacement_111):
    feature = _clean(ee_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_111'] = {'inputs': ['ee_replacement_111'], 'func': ee_replacement_d2_111}


def ee_replacement_d2_112(ee_replacement_112):
    feature = _clean(ee_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_112'] = {'inputs': ['ee_replacement_112'], 'func': ee_replacement_d2_112}


def ee_replacement_d2_113(ee_replacement_113):
    feature = _clean(ee_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_113'] = {'inputs': ['ee_replacement_113'], 'func': ee_replacement_d2_113}


def ee_replacement_d2_114(ee_replacement_114):
    feature = _clean(ee_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_114'] = {'inputs': ['ee_replacement_114'], 'func': ee_replacement_d2_114}


def ee_replacement_d2_115(ee_replacement_115):
    feature = _clean(ee_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_115'] = {'inputs': ['ee_replacement_115'], 'func': ee_replacement_d2_115}


def ee_replacement_d2_116(ee_replacement_116):
    feature = _clean(ee_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_116'] = {'inputs': ['ee_replacement_116'], 'func': ee_replacement_d2_116}


def ee_replacement_d2_117(ee_replacement_117):
    feature = _clean(ee_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_117'] = {'inputs': ['ee_replacement_117'], 'func': ee_replacement_d2_117}


def ee_replacement_d2_118(ee_replacement_118):
    feature = _clean(ee_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_118'] = {'inputs': ['ee_replacement_118'], 'func': ee_replacement_d2_118}


def ee_replacement_d2_119(ee_replacement_119):
    feature = _clean(ee_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_119'] = {'inputs': ['ee_replacement_119'], 'func': ee_replacement_d2_119}


def ee_replacement_d2_120(ee_replacement_120):
    feature = _clean(ee_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_120'] = {'inputs': ['ee_replacement_120'], 'func': ee_replacement_d2_120}


def ee_replacement_d2_121(ee_replacement_121):
    feature = _clean(ee_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_121'] = {'inputs': ['ee_replacement_121'], 'func': ee_replacement_d2_121}


def ee_replacement_d2_122(ee_replacement_122):
    feature = _clean(ee_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_122'] = {'inputs': ['ee_replacement_122'], 'func': ee_replacement_d2_122}


def ee_replacement_d2_123(ee_replacement_123):
    feature = _clean(ee_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_123'] = {'inputs': ['ee_replacement_123'], 'func': ee_replacement_d2_123}


def ee_replacement_d2_124(ee_replacement_124):
    feature = _clean(ee_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_124'] = {'inputs': ['ee_replacement_124'], 'func': ee_replacement_d2_124}


def ee_replacement_d2_125(ee_replacement_125):
    feature = _clean(ee_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_125'] = {'inputs': ['ee_replacement_125'], 'func': ee_replacement_d2_125}


def ee_replacement_d2_126(ee_replacement_126):
    feature = _clean(ee_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_126'] = {'inputs': ['ee_replacement_126'], 'func': ee_replacement_d2_126}


def ee_replacement_d2_127(ee_replacement_127):
    feature = _clean(ee_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_127'] = {'inputs': ['ee_replacement_127'], 'func': ee_replacement_d2_127}


def ee_replacement_d2_128(ee_replacement_128):
    feature = _clean(ee_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_128'] = {'inputs': ['ee_replacement_128'], 'func': ee_replacement_d2_128}


def ee_replacement_d2_129(ee_replacement_129):
    feature = _clean(ee_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_129'] = {'inputs': ['ee_replacement_129'], 'func': ee_replacement_d2_129}


def ee_replacement_d2_130(ee_replacement_130):
    feature = _clean(ee_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_130'] = {'inputs': ['ee_replacement_130'], 'func': ee_replacement_d2_130}


def ee_replacement_d2_131(ee_replacement_131):
    feature = _clean(ee_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_131'] = {'inputs': ['ee_replacement_131'], 'func': ee_replacement_d2_131}


def ee_replacement_d2_132(ee_replacement_132):
    feature = _clean(ee_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_132'] = {'inputs': ['ee_replacement_132'], 'func': ee_replacement_d2_132}


def ee_replacement_d2_133(ee_replacement_133):
    feature = _clean(ee_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_133'] = {'inputs': ['ee_replacement_133'], 'func': ee_replacement_d2_133}


def ee_replacement_d2_134(ee_replacement_134):
    feature = _clean(ee_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_134'] = {'inputs': ['ee_replacement_134'], 'func': ee_replacement_d2_134}


def ee_replacement_d2_135(ee_replacement_135):
    feature = _clean(ee_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_135'] = {'inputs': ['ee_replacement_135'], 'func': ee_replacement_d2_135}


def ee_replacement_d2_136(ee_replacement_136):
    feature = _clean(ee_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_136'] = {'inputs': ['ee_replacement_136'], 'func': ee_replacement_d2_136}


def ee_replacement_d2_137(ee_replacement_137):
    feature = _clean(ee_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_137'] = {'inputs': ['ee_replacement_137'], 'func': ee_replacement_d2_137}


def ee_replacement_d2_138(ee_replacement_138):
    feature = _clean(ee_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_138'] = {'inputs': ['ee_replacement_138'], 'func': ee_replacement_d2_138}


def ee_replacement_d2_139(ee_replacement_139):
    feature = _clean(ee_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_139'] = {'inputs': ['ee_replacement_139'], 'func': ee_replacement_d2_139}


def ee_replacement_d2_140(ee_replacement_140):
    feature = _clean(ee_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_140'] = {'inputs': ['ee_replacement_140'], 'func': ee_replacement_d2_140}


def ee_replacement_d2_141(ee_replacement_141):
    feature = _clean(ee_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_141'] = {'inputs': ['ee_replacement_141'], 'func': ee_replacement_d2_141}


def ee_replacement_d2_142(ee_replacement_142):
    feature = _clean(ee_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_142'] = {'inputs': ['ee_replacement_142'], 'func': ee_replacement_d2_142}


def ee_replacement_d2_143(ee_replacement_143):
    feature = _clean(ee_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_143'] = {'inputs': ['ee_replacement_143'], 'func': ee_replacement_d2_143}


def ee_replacement_d2_144(ee_replacement_144):
    feature = _clean(ee_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_144'] = {'inputs': ['ee_replacement_144'], 'func': ee_replacement_d2_144}


def ee_replacement_d2_145(ee_replacement_145):
    feature = _clean(ee_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_145'] = {'inputs': ['ee_replacement_145'], 'func': ee_replacement_d2_145}


def ee_replacement_d2_146(ee_replacement_146):
    feature = _clean(ee_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_146'] = {'inputs': ['ee_replacement_146'], 'func': ee_replacement_d2_146}


def ee_replacement_d2_147(ee_replacement_147):
    feature = _clean(ee_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_147'] = {'inputs': ['ee_replacement_147'], 'func': ee_replacement_d2_147}


def ee_replacement_d2_148(ee_replacement_148):
    feature = _clean(ee_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_148'] = {'inputs': ['ee_replacement_148'], 'func': ee_replacement_d2_148}


def ee_replacement_d2_149(ee_replacement_149):
    feature = _clean(ee_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_149'] = {'inputs': ['ee_replacement_149'], 'func': ee_replacement_d2_149}


def ee_replacement_d2_150(ee_replacement_150):
    feature = _clean(ee_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_150'] = {'inputs': ['ee_replacement_150'], 'func': ee_replacement_d2_150}


def ee_replacement_d2_151(ee_replacement_151):
    feature = _clean(ee_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_151'] = {'inputs': ['ee_replacement_151'], 'func': ee_replacement_d2_151}


def ee_replacement_d2_152(ee_replacement_152):
    feature = _clean(ee_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_152'] = {'inputs': ['ee_replacement_152'], 'func': ee_replacement_d2_152}


def ee_replacement_d2_153(ee_replacement_153):
    feature = _clean(ee_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_153'] = {'inputs': ['ee_replacement_153'], 'func': ee_replacement_d2_153}


def ee_replacement_d2_154(ee_replacement_154):
    feature = _clean(ee_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_154'] = {'inputs': ['ee_replacement_154'], 'func': ee_replacement_d2_154}


def ee_replacement_d2_155(ee_replacement_155):
    feature = _clean(ee_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_155'] = {'inputs': ['ee_replacement_155'], 'func': ee_replacement_d2_155}


def ee_replacement_d2_156(ee_replacement_156):
    feature = _clean(ee_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_156'] = {'inputs': ['ee_replacement_156'], 'func': ee_replacement_d2_156}


def ee_replacement_d2_157(ee_replacement_157):
    feature = _clean(ee_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_157'] = {'inputs': ['ee_replacement_157'], 'func': ee_replacement_d2_157}


def ee_replacement_d2_158(ee_replacement_158):
    feature = _clean(ee_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_158'] = {'inputs': ['ee_replacement_158'], 'func': ee_replacement_d2_158}


def ee_replacement_d2_159(ee_replacement_159):
    feature = _clean(ee_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_159'] = {'inputs': ['ee_replacement_159'], 'func': ee_replacement_d2_159}


def ee_replacement_d2_160(ee_replacement_160):
    feature = _clean(ee_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_160'] = {'inputs': ['ee_replacement_160'], 'func': ee_replacement_d2_160}


def ee_replacement_d2_161(ee_replacement_161):
    feature = _clean(ee_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_161'] = {'inputs': ['ee_replacement_161'], 'func': ee_replacement_d2_161}


def ee_replacement_d2_162(ee_replacement_162):
    feature = _clean(ee_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_162'] = {'inputs': ['ee_replacement_162'], 'func': ee_replacement_d2_162}


def ee_replacement_d2_163(ee_replacement_163):
    feature = _clean(ee_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_163'] = {'inputs': ['ee_replacement_163'], 'func': ee_replacement_d2_163}


def ee_replacement_d2_164(ee_replacement_164):
    feature = _clean(ee_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_164'] = {'inputs': ['ee_replacement_164'], 'func': ee_replacement_d2_164}


def ee_replacement_d2_165(ee_replacement_165):
    feature = _clean(ee_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_165'] = {'inputs': ['ee_replacement_165'], 'func': ee_replacement_d2_165}


def ee_replacement_d2_166(ee_replacement_166):
    feature = _clean(ee_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
EE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ee_replacement_d2_166'] = {'inputs': ['ee_replacement_166'], 'func': ee_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def eqe_base_universe_d2_001_eqe_003_fcf_burn_to_cash_63(eqe_003_fcf_burn_to_cash_63):
    return _base_universe_d2(eqe_003_fcf_burn_to_cash_63, 1)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_001_eqe_003_fcf_burn_to_cash_63'] = {'inputs': ['eqe_003_fcf_burn_to_cash_63'], 'func': eqe_base_universe_d2_001_eqe_003_fcf_burn_to_cash_63}


def eqe_base_universe_d2_002_eqe_004_debt_to_equity_84(eqe_004_debt_to_equity_84):
    return _base_universe_d2(eqe_004_debt_to_equity_84, 2)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_002_eqe_004_debt_to_equity_84'] = {'inputs': ['eqe_004_debt_to_equity_84'], 'func': eqe_base_universe_d2_002_eqe_004_debt_to_equity_84}


def eqe_base_universe_d2_003_eqe_005_debt_to_assets_126(eqe_005_debt_to_assets_126):
    return _base_universe_d2(eqe_005_debt_to_assets_126, 3)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_003_eqe_005_debt_to_assets_126'] = {'inputs': ['eqe_005_debt_to_assets_126'], 'func': eqe_base_universe_d2_003_eqe_005_debt_to_assets_126}


def eqe_base_universe_d2_004_eqe_012_accrual_gap_1260(eqe_012_accrual_gap_1260):
    return _base_universe_d2(eqe_012_accrual_gap_1260, 4)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_004_eqe_012_accrual_gap_1260'] = {'inputs': ['eqe_012_accrual_gap_1260'], 'func': eqe_base_universe_d2_004_eqe_012_accrual_gap_1260}


def eqe_base_universe_d2_005_eqe_016_debt_to_equity_21(eqe_016_debt_to_equity_21):
    return _base_universe_d2(eqe_016_debt_to_equity_21, 5)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_005_eqe_016_debt_to_equity_21'] = {'inputs': ['eqe_016_debt_to_equity_21'], 'func': eqe_base_universe_d2_005_eqe_016_debt_to_equity_21}


def eqe_base_universe_d2_006_eqe_017_debt_to_assets_42(eqe_017_debt_to_assets_42):
    return _base_universe_d2(eqe_017_debt_to_assets_42, 6)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_006_eqe_017_debt_to_assets_42'] = {'inputs': ['eqe_017_debt_to_assets_42'], 'func': eqe_base_universe_d2_006_eqe_017_debt_to_assets_42}


def eqe_base_universe_d2_007_eqe_024_accrual_gap_504(eqe_024_accrual_gap_504):
    return _base_universe_d2(eqe_024_accrual_gap_504, 7)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_007_eqe_024_accrual_gap_504'] = {'inputs': ['eqe_024_accrual_gap_504'], 'func': eqe_base_universe_d2_007_eqe_024_accrual_gap_504}


def eqe_base_universe_d2_008_eqe_027_fcf_burn_to_cash_1260(eqe_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(eqe_027_fcf_burn_to_cash_1260, 8)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_008_eqe_027_fcf_burn_to_cash_1260'] = {'inputs': ['eqe_027_fcf_burn_to_cash_1260'], 'func': eqe_base_universe_d2_008_eqe_027_fcf_burn_to_cash_1260}


def eqe_base_universe_d2_009_eqe_028_debt_to_equity_1512(eqe_028_debt_to_equity_1512):
    return _base_universe_d2(eqe_028_debt_to_equity_1512, 9)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_009_eqe_028_debt_to_equity_1512'] = {'inputs': ['eqe_028_debt_to_equity_1512'], 'func': eqe_base_universe_d2_009_eqe_028_debt_to_equity_1512}


def eqe_base_universe_d2_010_eqe_029_debt_to_assets_63(eqe_029_debt_to_assets_63):
    return _base_universe_d2(eqe_029_debt_to_assets_63, 10)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_010_eqe_029_debt_to_assets_63'] = {'inputs': ['eqe_029_debt_to_assets_63'], 'func': eqe_base_universe_d2_010_eqe_029_debt_to_assets_63}


def eqe_base_universe_d2_011_eqe_031_interest_coverage_stress_21(eqe_031_interest_coverage_stress_21):
    return _base_universe_d2(eqe_031_interest_coverage_stress_21, 11)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_011_eqe_031_interest_coverage_stress_21'] = {'inputs': ['eqe_031_interest_coverage_stress_21'], 'func': eqe_base_universe_d2_011_eqe_031_interest_coverage_stress_21}


def eqe_base_universe_d2_012_eqe_036_accrual_gap_189(eqe_036_accrual_gap_189):
    return _base_universe_d2(eqe_036_accrual_gap_189, 12)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_012_eqe_036_accrual_gap_189'] = {'inputs': ['eqe_036_accrual_gap_189'], 'func': eqe_base_universe_d2_012_eqe_036_accrual_gap_189}


def eqe_base_universe_d2_013_eqe_039_fcf_burn_to_cash_504(eqe_039_fcf_burn_to_cash_504):
    return _base_universe_d2(eqe_039_fcf_burn_to_cash_504, 13)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_013_eqe_039_fcf_burn_to_cash_504'] = {'inputs': ['eqe_039_fcf_burn_to_cash_504'], 'func': eqe_base_universe_d2_013_eqe_039_fcf_burn_to_cash_504}


def eqe_base_universe_d2_014_eqe_040_debt_to_equity_756(eqe_040_debt_to_equity_756):
    return _base_universe_d2(eqe_040_debt_to_equity_756, 14)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_014_eqe_040_debt_to_equity_756'] = {'inputs': ['eqe_040_debt_to_equity_756'], 'func': eqe_base_universe_d2_014_eqe_040_debt_to_equity_756}


def eqe_base_universe_d2_015_eqe_041_debt_to_assets_1008(eqe_041_debt_to_assets_1008):
    return _base_universe_d2(eqe_041_debt_to_assets_1008, 15)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_015_eqe_041_debt_to_assets_1008'] = {'inputs': ['eqe_041_debt_to_assets_1008'], 'func': eqe_base_universe_d2_015_eqe_041_debt_to_assets_1008}


def eqe_base_universe_d2_016_eqe_043_interest_coverage_stress_1512(eqe_043_interest_coverage_stress_1512):
    return _base_universe_d2(eqe_043_interest_coverage_stress_1512, 16)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_016_eqe_043_interest_coverage_stress_1512'] = {'inputs': ['eqe_043_interest_coverage_stress_1512'], 'func': eqe_base_universe_d2_016_eqe_043_interest_coverage_stress_1512}


def eqe_base_universe_d2_017_eqe_048_accrual_gap_63(eqe_048_accrual_gap_63):
    return _base_universe_d2(eqe_048_accrual_gap_63, 17)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_017_eqe_048_accrual_gap_63'] = {'inputs': ['eqe_048_accrual_gap_63'], 'func': eqe_base_universe_d2_017_eqe_048_accrual_gap_63}


def eqe_base_universe_d2_018_eqe_051_fcf_burn_to_cash_189(eqe_051_fcf_burn_to_cash_189):
    return _base_universe_d2(eqe_051_fcf_burn_to_cash_189, 18)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_018_eqe_051_fcf_burn_to_cash_189'] = {'inputs': ['eqe_051_fcf_burn_to_cash_189'], 'func': eqe_base_universe_d2_018_eqe_051_fcf_burn_to_cash_189}


def eqe_base_universe_d2_019_eqe_052_debt_to_equity_252(eqe_052_debt_to_equity_252):
    return _base_universe_d2(eqe_052_debt_to_equity_252, 19)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_019_eqe_052_debt_to_equity_252'] = {'inputs': ['eqe_052_debt_to_equity_252'], 'func': eqe_base_universe_d2_019_eqe_052_debt_to_equity_252}


def eqe_base_universe_d2_020_eqe_053_debt_to_assets_378(eqe_053_debt_to_assets_378):
    return _base_universe_d2(eqe_053_debt_to_assets_378, 20)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_020_eqe_053_debt_to_assets_378'] = {'inputs': ['eqe_053_debt_to_assets_378'], 'func': eqe_base_universe_d2_020_eqe_053_debt_to_assets_378}


def eqe_base_universe_d2_021_eqe_055_interest_coverage_stress_756(eqe_055_interest_coverage_stress_756):
    return _base_universe_d2(eqe_055_interest_coverage_stress_756, 21)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_021_eqe_055_interest_coverage_stress_756'] = {'inputs': ['eqe_055_interest_coverage_stress_756'], 'func': eqe_base_universe_d2_021_eqe_055_interest_coverage_stress_756}


def eqe_base_universe_d2_022_eqe_060_accrual_gap_252(eqe_060_accrual_gap_252):
    return _base_universe_d2(eqe_060_accrual_gap_252, 22)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_022_eqe_060_accrual_gap_252'] = {'inputs': ['eqe_060_accrual_gap_252'], 'func': eqe_base_universe_d2_022_eqe_060_accrual_gap_252}


def eqe_base_universe_d2_023_eqe_basefill_001(eqe_basefill_001):
    return _base_universe_d2(eqe_basefill_001, 23)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_023_eqe_basefill_001'] = {'inputs': ['eqe_basefill_001'], 'func': eqe_base_universe_d2_023_eqe_basefill_001}


def eqe_base_universe_d2_024_eqe_basefill_002(eqe_basefill_002):
    return _base_universe_d2(eqe_basefill_002, 24)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_024_eqe_basefill_002'] = {'inputs': ['eqe_basefill_002'], 'func': eqe_base_universe_d2_024_eqe_basefill_002}


def eqe_base_universe_d2_025_eqe_basefill_006(eqe_basefill_006):
    return _base_universe_d2(eqe_basefill_006, 25)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_025_eqe_basefill_006'] = {'inputs': ['eqe_basefill_006'], 'func': eqe_base_universe_d2_025_eqe_basefill_006}


def eqe_base_universe_d2_026_eqe_basefill_008(eqe_basefill_008):
    return _base_universe_d2(eqe_basefill_008, 26)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_026_eqe_basefill_008'] = {'inputs': ['eqe_basefill_008'], 'func': eqe_base_universe_d2_026_eqe_basefill_008}


def eqe_base_universe_d2_027_eqe_basefill_009(eqe_basefill_009):
    return _base_universe_d2(eqe_basefill_009, 27)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_027_eqe_basefill_009'] = {'inputs': ['eqe_basefill_009'], 'func': eqe_base_universe_d2_027_eqe_basefill_009}


def eqe_base_universe_d2_028_eqe_basefill_010(eqe_basefill_010):
    return _base_universe_d2(eqe_basefill_010, 28)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_028_eqe_basefill_010'] = {'inputs': ['eqe_basefill_010'], 'func': eqe_base_universe_d2_028_eqe_basefill_010}


def eqe_base_universe_d2_029_eqe_basefill_011(eqe_basefill_011):
    return _base_universe_d2(eqe_basefill_011, 29)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_029_eqe_basefill_011'] = {'inputs': ['eqe_basefill_011'], 'func': eqe_base_universe_d2_029_eqe_basefill_011}


def eqe_base_universe_d2_030_eqe_basefill_013(eqe_basefill_013):
    return _base_universe_d2(eqe_basefill_013, 30)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_030_eqe_basefill_013'] = {'inputs': ['eqe_basefill_013'], 'func': eqe_base_universe_d2_030_eqe_basefill_013}


def eqe_base_universe_d2_031_eqe_basefill_014(eqe_basefill_014):
    return _base_universe_d2(eqe_basefill_014, 31)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_031_eqe_basefill_014'] = {'inputs': ['eqe_basefill_014'], 'func': eqe_base_universe_d2_031_eqe_basefill_014}


def eqe_base_universe_d2_032_eqe_basefill_015(eqe_basefill_015):
    return _base_universe_d2(eqe_basefill_015, 32)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_032_eqe_basefill_015'] = {'inputs': ['eqe_basefill_015'], 'func': eqe_base_universe_d2_032_eqe_basefill_015}


def eqe_base_universe_d2_033_eqe_basefill_018(eqe_basefill_018):
    return _base_universe_d2(eqe_basefill_018, 33)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_033_eqe_basefill_018'] = {'inputs': ['eqe_basefill_018'], 'func': eqe_base_universe_d2_033_eqe_basefill_018}


def eqe_base_universe_d2_034_eqe_basefill_020(eqe_basefill_020):
    return _base_universe_d2(eqe_basefill_020, 34)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_034_eqe_basefill_020'] = {'inputs': ['eqe_basefill_020'], 'func': eqe_base_universe_d2_034_eqe_basefill_020}


def eqe_base_universe_d2_035_eqe_basefill_021(eqe_basefill_021):
    return _base_universe_d2(eqe_basefill_021, 35)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_035_eqe_basefill_021'] = {'inputs': ['eqe_basefill_021'], 'func': eqe_base_universe_d2_035_eqe_basefill_021}


def eqe_base_universe_d2_036_eqe_basefill_022(eqe_basefill_022):
    return _base_universe_d2(eqe_basefill_022, 36)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_036_eqe_basefill_022'] = {'inputs': ['eqe_basefill_022'], 'func': eqe_base_universe_d2_036_eqe_basefill_022}


def eqe_base_universe_d2_037_eqe_basefill_023(eqe_basefill_023):
    return _base_universe_d2(eqe_basefill_023, 37)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_037_eqe_basefill_023'] = {'inputs': ['eqe_basefill_023'], 'func': eqe_base_universe_d2_037_eqe_basefill_023}


def eqe_base_universe_d2_038_eqe_basefill_025(eqe_basefill_025):
    return _base_universe_d2(eqe_basefill_025, 38)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_038_eqe_basefill_025'] = {'inputs': ['eqe_basefill_025'], 'func': eqe_base_universe_d2_038_eqe_basefill_025}


def eqe_base_universe_d2_039_eqe_basefill_026(eqe_basefill_026):
    return _base_universe_d2(eqe_basefill_026, 39)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_039_eqe_basefill_026'] = {'inputs': ['eqe_basefill_026'], 'func': eqe_base_universe_d2_039_eqe_basefill_026}


def eqe_base_universe_d2_040_eqe_basefill_030(eqe_basefill_030):
    return _base_universe_d2(eqe_basefill_030, 40)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_040_eqe_basefill_030'] = {'inputs': ['eqe_basefill_030'], 'func': eqe_base_universe_d2_040_eqe_basefill_030}


def eqe_base_universe_d2_041_eqe_basefill_032(eqe_basefill_032):
    return _base_universe_d2(eqe_basefill_032, 41)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_041_eqe_basefill_032'] = {'inputs': ['eqe_basefill_032'], 'func': eqe_base_universe_d2_041_eqe_basefill_032}


def eqe_base_universe_d2_042_eqe_basefill_033(eqe_basefill_033):
    return _base_universe_d2(eqe_basefill_033, 42)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_042_eqe_basefill_033'] = {'inputs': ['eqe_basefill_033'], 'func': eqe_base_universe_d2_042_eqe_basefill_033}


def eqe_base_universe_d2_043_eqe_basefill_034(eqe_basefill_034):
    return _base_universe_d2(eqe_basefill_034, 43)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_043_eqe_basefill_034'] = {'inputs': ['eqe_basefill_034'], 'func': eqe_base_universe_d2_043_eqe_basefill_034}


def eqe_base_universe_d2_044_eqe_basefill_035(eqe_basefill_035):
    return _base_universe_d2(eqe_basefill_035, 44)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_044_eqe_basefill_035'] = {'inputs': ['eqe_basefill_035'], 'func': eqe_base_universe_d2_044_eqe_basefill_035}


def eqe_base_universe_d2_045_eqe_basefill_037(eqe_basefill_037):
    return _base_universe_d2(eqe_basefill_037, 45)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_045_eqe_basefill_037'] = {'inputs': ['eqe_basefill_037'], 'func': eqe_base_universe_d2_045_eqe_basefill_037}


def eqe_base_universe_d2_046_eqe_basefill_038(eqe_basefill_038):
    return _base_universe_d2(eqe_basefill_038, 46)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_046_eqe_basefill_038'] = {'inputs': ['eqe_basefill_038'], 'func': eqe_base_universe_d2_046_eqe_basefill_038}


def eqe_base_universe_d2_047_eqe_basefill_042(eqe_basefill_042):
    return _base_universe_d2(eqe_basefill_042, 47)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_047_eqe_basefill_042'] = {'inputs': ['eqe_basefill_042'], 'func': eqe_base_universe_d2_047_eqe_basefill_042}


def eqe_base_universe_d2_048_eqe_basefill_044(eqe_basefill_044):
    return _base_universe_d2(eqe_basefill_044, 48)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_048_eqe_basefill_044'] = {'inputs': ['eqe_basefill_044'], 'func': eqe_base_universe_d2_048_eqe_basefill_044}


def eqe_base_universe_d2_049_eqe_basefill_045(eqe_basefill_045):
    return _base_universe_d2(eqe_basefill_045, 49)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_049_eqe_basefill_045'] = {'inputs': ['eqe_basefill_045'], 'func': eqe_base_universe_d2_049_eqe_basefill_045}


def eqe_base_universe_d2_050_eqe_basefill_046(eqe_basefill_046):
    return _base_universe_d2(eqe_basefill_046, 50)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_050_eqe_basefill_046'] = {'inputs': ['eqe_basefill_046'], 'func': eqe_base_universe_d2_050_eqe_basefill_046}


def eqe_base_universe_d2_051_eqe_basefill_047(eqe_basefill_047):
    return _base_universe_d2(eqe_basefill_047, 51)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_051_eqe_basefill_047'] = {'inputs': ['eqe_basefill_047'], 'func': eqe_base_universe_d2_051_eqe_basefill_047}


def eqe_base_universe_d2_052_eqe_basefill_049(eqe_basefill_049):
    return _base_universe_d2(eqe_basefill_049, 52)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_052_eqe_basefill_049'] = {'inputs': ['eqe_basefill_049'], 'func': eqe_base_universe_d2_052_eqe_basefill_049}


def eqe_base_universe_d2_053_eqe_basefill_050(eqe_basefill_050):
    return _base_universe_d2(eqe_basefill_050, 53)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_053_eqe_basefill_050'] = {'inputs': ['eqe_basefill_050'], 'func': eqe_base_universe_d2_053_eqe_basefill_050}


def eqe_base_universe_d2_054_eqe_basefill_054(eqe_basefill_054):
    return _base_universe_d2(eqe_basefill_054, 54)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_054_eqe_basefill_054'] = {'inputs': ['eqe_basefill_054'], 'func': eqe_base_universe_d2_054_eqe_basefill_054}


def eqe_base_universe_d2_055_eqe_basefill_056(eqe_basefill_056):
    return _base_universe_d2(eqe_basefill_056, 55)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_055_eqe_basefill_056'] = {'inputs': ['eqe_basefill_056'], 'func': eqe_base_universe_d2_055_eqe_basefill_056}


def eqe_base_universe_d2_056_eqe_basefill_057(eqe_basefill_057):
    return _base_universe_d2(eqe_basefill_057, 56)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_056_eqe_basefill_057'] = {'inputs': ['eqe_basefill_057'], 'func': eqe_base_universe_d2_056_eqe_basefill_057}


def eqe_base_universe_d2_057_eqe_basefill_058(eqe_basefill_058):
    return _base_universe_d2(eqe_basefill_058, 57)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_057_eqe_basefill_058'] = {'inputs': ['eqe_basefill_058'], 'func': eqe_base_universe_d2_057_eqe_basefill_058}


def eqe_base_universe_d2_058_eqe_basefill_059(eqe_basefill_059):
    return _base_universe_d2(eqe_basefill_059, 58)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_058_eqe_basefill_059'] = {'inputs': ['eqe_basefill_059'], 'func': eqe_base_universe_d2_058_eqe_basefill_059}


def eqe_base_universe_d2_059_eqe_basefill_061(eqe_basefill_061):
    return _base_universe_d2(eqe_basefill_061, 59)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_059_eqe_basefill_061'] = {'inputs': ['eqe_basefill_061'], 'func': eqe_base_universe_d2_059_eqe_basefill_061}


def eqe_base_universe_d2_060_eqe_basefill_062(eqe_basefill_062):
    return _base_universe_d2(eqe_basefill_062, 60)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_060_eqe_basefill_062'] = {'inputs': ['eqe_basefill_062'], 'func': eqe_base_universe_d2_060_eqe_basefill_062}


def eqe_base_universe_d2_061_eqe_basefill_063(eqe_basefill_063):
    return _base_universe_d2(eqe_basefill_063, 61)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_061_eqe_basefill_063'] = {'inputs': ['eqe_basefill_063'], 'func': eqe_base_universe_d2_061_eqe_basefill_063}


def eqe_base_universe_d2_062_eqe_basefill_064(eqe_basefill_064):
    return _base_universe_d2(eqe_basefill_064, 62)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_062_eqe_basefill_064'] = {'inputs': ['eqe_basefill_064'], 'func': eqe_base_universe_d2_062_eqe_basefill_064}


def eqe_base_universe_d2_063_eqe_basefill_065(eqe_basefill_065):
    return _base_universe_d2(eqe_basefill_065, 63)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_063_eqe_basefill_065'] = {'inputs': ['eqe_basefill_065'], 'func': eqe_base_universe_d2_063_eqe_basefill_065}


def eqe_base_universe_d2_064_eqe_basefill_066(eqe_basefill_066):
    return _base_universe_d2(eqe_basefill_066, 64)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_064_eqe_basefill_066'] = {'inputs': ['eqe_basefill_066'], 'func': eqe_base_universe_d2_064_eqe_basefill_066}


def eqe_base_universe_d2_065_eqe_basefill_067(eqe_basefill_067):
    return _base_universe_d2(eqe_basefill_067, 65)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_065_eqe_basefill_067'] = {'inputs': ['eqe_basefill_067'], 'func': eqe_base_universe_d2_065_eqe_basefill_067}


def eqe_base_universe_d2_066_eqe_basefill_068(eqe_basefill_068):
    return _base_universe_d2(eqe_basefill_068, 66)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_066_eqe_basefill_068'] = {'inputs': ['eqe_basefill_068'], 'func': eqe_base_universe_d2_066_eqe_basefill_068}


def eqe_base_universe_d2_067_eqe_basefill_069(eqe_basefill_069):
    return _base_universe_d2(eqe_basefill_069, 67)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_067_eqe_basefill_069'] = {'inputs': ['eqe_basefill_069'], 'func': eqe_base_universe_d2_067_eqe_basefill_069}


def eqe_base_universe_d2_068_eqe_basefill_070(eqe_basefill_070):
    return _base_universe_d2(eqe_basefill_070, 68)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_068_eqe_basefill_070'] = {'inputs': ['eqe_basefill_070'], 'func': eqe_base_universe_d2_068_eqe_basefill_070}


def eqe_base_universe_d2_069_eqe_basefill_071(eqe_basefill_071):
    return _base_universe_d2(eqe_basefill_071, 69)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_069_eqe_basefill_071'] = {'inputs': ['eqe_basefill_071'], 'func': eqe_base_universe_d2_069_eqe_basefill_071}


def eqe_base_universe_d2_070_eqe_basefill_072(eqe_basefill_072):
    return _base_universe_d2(eqe_basefill_072, 70)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_070_eqe_basefill_072'] = {'inputs': ['eqe_basefill_072'], 'func': eqe_base_universe_d2_070_eqe_basefill_072}


def eqe_base_universe_d2_071_eqe_basefill_073(eqe_basefill_073):
    return _base_universe_d2(eqe_basefill_073, 71)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_071_eqe_basefill_073'] = {'inputs': ['eqe_basefill_073'], 'func': eqe_base_universe_d2_071_eqe_basefill_073}


def eqe_base_universe_d2_072_eqe_basefill_074(eqe_basefill_074):
    return _base_universe_d2(eqe_basefill_074, 72)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_072_eqe_basefill_074'] = {'inputs': ['eqe_basefill_074'], 'func': eqe_base_universe_d2_072_eqe_basefill_074}


def eqe_base_universe_d2_073_eqe_basefill_075(eqe_basefill_075):
    return _base_universe_d2(eqe_basefill_075, 73)
EQE_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['eqe_base_universe_d2_073_eqe_basefill_075'] = {'inputs': ['eqe_basefill_075'], 'func': eqe_base_universe_d2_073_eqe_basefill_075}
