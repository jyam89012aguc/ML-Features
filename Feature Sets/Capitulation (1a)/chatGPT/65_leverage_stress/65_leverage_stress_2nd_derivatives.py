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



def lvs_151_lvs_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def lvs_152_lvs_007_interest_coverage_stress_252_roc_42(lvs_007_interest_coverage_stress_252):
    feature = _s(lvs_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def lvs_153_lvs_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def lvs_154_lvs_019_interest_coverage_stress_84_roc_378(lvs_019_interest_coverage_stress_84):
    feature = _s(lvs_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def lvs_155_lvs_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















LEVERAGE_STRESS_REGISTRY_2ND_DERIVATIVES = {
    'lvs_151_lvs_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': lvs_151_lvs_001_netinc_decline_1_roc_1},
    'lvs_152_lvs_007_interest_coverage_stress_252_roc_42': {'inputs': ['lvs_007_interest_coverage_stress_252'], 'func': lvs_152_lvs_007_interest_coverage_stress_252_roc_42},
    'lvs_153_lvs_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': lvs_153_lvs_013_netinc_decline_1_roc_126},
    'lvs_154_lvs_019_interest_coverage_stress_84_roc_378': {'inputs': ['lvs_019_interest_coverage_stress_84'], 'func': lvs_154_lvs_019_interest_coverage_stress_84_roc_378},
    'lvs_155_lvs_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': lvs_155_lvs_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ls_replacement_d2_001(ls_replacement_001):
    feature = _clean(ls_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_001'] = {'inputs': ['ls_replacement_001'], 'func': ls_replacement_d2_001}


def ls_replacement_d2_002(ls_replacement_002):
    feature = _clean(ls_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_002'] = {'inputs': ['ls_replacement_002'], 'func': ls_replacement_d2_002}


def ls_replacement_d2_003(ls_replacement_003):
    feature = _clean(ls_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_003'] = {'inputs': ['ls_replacement_003'], 'func': ls_replacement_d2_003}


def ls_replacement_d2_004(ls_replacement_004):
    feature = _clean(ls_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_004'] = {'inputs': ['ls_replacement_004'], 'func': ls_replacement_d2_004}


def ls_replacement_d2_005(ls_replacement_005):
    feature = _clean(ls_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_005'] = {'inputs': ['ls_replacement_005'], 'func': ls_replacement_d2_005}


def ls_replacement_d2_006(ls_replacement_006):
    feature = _clean(ls_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_006'] = {'inputs': ['ls_replacement_006'], 'func': ls_replacement_d2_006}


def ls_replacement_d2_007(ls_replacement_007):
    feature = _clean(ls_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_007'] = {'inputs': ['ls_replacement_007'], 'func': ls_replacement_d2_007}


def ls_replacement_d2_008(ls_replacement_008):
    feature = _clean(ls_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_008'] = {'inputs': ['ls_replacement_008'], 'func': ls_replacement_d2_008}


def ls_replacement_d2_009(ls_replacement_009):
    feature = _clean(ls_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_009'] = {'inputs': ['ls_replacement_009'], 'func': ls_replacement_d2_009}


def ls_replacement_d2_010(ls_replacement_010):
    feature = _clean(ls_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_010'] = {'inputs': ['ls_replacement_010'], 'func': ls_replacement_d2_010}


def ls_replacement_d2_011(ls_replacement_011):
    feature = _clean(ls_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_011'] = {'inputs': ['ls_replacement_011'], 'func': ls_replacement_d2_011}


def ls_replacement_d2_012(ls_replacement_012):
    feature = _clean(ls_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_012'] = {'inputs': ['ls_replacement_012'], 'func': ls_replacement_d2_012}


def ls_replacement_d2_013(ls_replacement_013):
    feature = _clean(ls_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_013'] = {'inputs': ['ls_replacement_013'], 'func': ls_replacement_d2_013}


def ls_replacement_d2_014(ls_replacement_014):
    feature = _clean(ls_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_014'] = {'inputs': ['ls_replacement_014'], 'func': ls_replacement_d2_014}


def ls_replacement_d2_015(ls_replacement_015):
    feature = _clean(ls_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_015'] = {'inputs': ['ls_replacement_015'], 'func': ls_replacement_d2_015}


def ls_replacement_d2_016(ls_replacement_016):
    feature = _clean(ls_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_016'] = {'inputs': ['ls_replacement_016'], 'func': ls_replacement_d2_016}


def ls_replacement_d2_017(ls_replacement_017):
    feature = _clean(ls_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_017'] = {'inputs': ['ls_replacement_017'], 'func': ls_replacement_d2_017}


def ls_replacement_d2_018(ls_replacement_018):
    feature = _clean(ls_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_018'] = {'inputs': ['ls_replacement_018'], 'func': ls_replacement_d2_018}


def ls_replacement_d2_019(ls_replacement_019):
    feature = _clean(ls_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_019'] = {'inputs': ['ls_replacement_019'], 'func': ls_replacement_d2_019}


def ls_replacement_d2_020(ls_replacement_020):
    feature = _clean(ls_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_020'] = {'inputs': ['ls_replacement_020'], 'func': ls_replacement_d2_020}


def ls_replacement_d2_021(ls_replacement_021):
    feature = _clean(ls_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_021'] = {'inputs': ['ls_replacement_021'], 'func': ls_replacement_d2_021}


def ls_replacement_d2_022(ls_replacement_022):
    feature = _clean(ls_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_022'] = {'inputs': ['ls_replacement_022'], 'func': ls_replacement_d2_022}


def ls_replacement_d2_023(ls_replacement_023):
    feature = _clean(ls_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_023'] = {'inputs': ['ls_replacement_023'], 'func': ls_replacement_d2_023}


def ls_replacement_d2_024(ls_replacement_024):
    feature = _clean(ls_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_024'] = {'inputs': ['ls_replacement_024'], 'func': ls_replacement_d2_024}


def ls_replacement_d2_025(ls_replacement_025):
    feature = _clean(ls_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_025'] = {'inputs': ['ls_replacement_025'], 'func': ls_replacement_d2_025}


def ls_replacement_d2_026(ls_replacement_026):
    feature = _clean(ls_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_026'] = {'inputs': ['ls_replacement_026'], 'func': ls_replacement_d2_026}


def ls_replacement_d2_027(ls_replacement_027):
    feature = _clean(ls_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_027'] = {'inputs': ['ls_replacement_027'], 'func': ls_replacement_d2_027}


def ls_replacement_d2_028(ls_replacement_028):
    feature = _clean(ls_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_028'] = {'inputs': ['ls_replacement_028'], 'func': ls_replacement_d2_028}


def ls_replacement_d2_029(ls_replacement_029):
    feature = _clean(ls_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_029'] = {'inputs': ['ls_replacement_029'], 'func': ls_replacement_d2_029}


def ls_replacement_d2_030(ls_replacement_030):
    feature = _clean(ls_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_030'] = {'inputs': ['ls_replacement_030'], 'func': ls_replacement_d2_030}


def ls_replacement_d2_031(ls_replacement_031):
    feature = _clean(ls_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_031'] = {'inputs': ['ls_replacement_031'], 'func': ls_replacement_d2_031}


def ls_replacement_d2_032(ls_replacement_032):
    feature = _clean(ls_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_032'] = {'inputs': ['ls_replacement_032'], 'func': ls_replacement_d2_032}


def ls_replacement_d2_033(ls_replacement_033):
    feature = _clean(ls_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_033'] = {'inputs': ['ls_replacement_033'], 'func': ls_replacement_d2_033}


def ls_replacement_d2_034(ls_replacement_034):
    feature = _clean(ls_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_034'] = {'inputs': ['ls_replacement_034'], 'func': ls_replacement_d2_034}


def ls_replacement_d2_035(ls_replacement_035):
    feature = _clean(ls_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_035'] = {'inputs': ['ls_replacement_035'], 'func': ls_replacement_d2_035}


def ls_replacement_d2_036(ls_replacement_036):
    feature = _clean(ls_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_036'] = {'inputs': ['ls_replacement_036'], 'func': ls_replacement_d2_036}


def ls_replacement_d2_037(ls_replacement_037):
    feature = _clean(ls_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_037'] = {'inputs': ['ls_replacement_037'], 'func': ls_replacement_d2_037}


def ls_replacement_d2_038(ls_replacement_038):
    feature = _clean(ls_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_038'] = {'inputs': ['ls_replacement_038'], 'func': ls_replacement_d2_038}


def ls_replacement_d2_039(ls_replacement_039):
    feature = _clean(ls_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_039'] = {'inputs': ['ls_replacement_039'], 'func': ls_replacement_d2_039}


def ls_replacement_d2_040(ls_replacement_040):
    feature = _clean(ls_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_040'] = {'inputs': ['ls_replacement_040'], 'func': ls_replacement_d2_040}


def ls_replacement_d2_041(ls_replacement_041):
    feature = _clean(ls_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_041'] = {'inputs': ['ls_replacement_041'], 'func': ls_replacement_d2_041}


def ls_replacement_d2_042(ls_replacement_042):
    feature = _clean(ls_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_042'] = {'inputs': ['ls_replacement_042'], 'func': ls_replacement_d2_042}


def ls_replacement_d2_043(ls_replacement_043):
    feature = _clean(ls_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_043'] = {'inputs': ['ls_replacement_043'], 'func': ls_replacement_d2_043}


def ls_replacement_d2_044(ls_replacement_044):
    feature = _clean(ls_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_044'] = {'inputs': ['ls_replacement_044'], 'func': ls_replacement_d2_044}


def ls_replacement_d2_045(ls_replacement_045):
    feature = _clean(ls_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_045'] = {'inputs': ['ls_replacement_045'], 'func': ls_replacement_d2_045}


def ls_replacement_d2_046(ls_replacement_046):
    feature = _clean(ls_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_046'] = {'inputs': ['ls_replacement_046'], 'func': ls_replacement_d2_046}


def ls_replacement_d2_047(ls_replacement_047):
    feature = _clean(ls_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_047'] = {'inputs': ['ls_replacement_047'], 'func': ls_replacement_d2_047}


def ls_replacement_d2_048(ls_replacement_048):
    feature = _clean(ls_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_048'] = {'inputs': ['ls_replacement_048'], 'func': ls_replacement_d2_048}


def ls_replacement_d2_049(ls_replacement_049):
    feature = _clean(ls_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_049'] = {'inputs': ['ls_replacement_049'], 'func': ls_replacement_d2_049}


def ls_replacement_d2_050(ls_replacement_050):
    feature = _clean(ls_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_050'] = {'inputs': ['ls_replacement_050'], 'func': ls_replacement_d2_050}


def ls_replacement_d2_051(ls_replacement_051):
    feature = _clean(ls_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_051'] = {'inputs': ['ls_replacement_051'], 'func': ls_replacement_d2_051}


def ls_replacement_d2_052(ls_replacement_052):
    feature = _clean(ls_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_052'] = {'inputs': ['ls_replacement_052'], 'func': ls_replacement_d2_052}


def ls_replacement_d2_053(ls_replacement_053):
    feature = _clean(ls_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_053'] = {'inputs': ['ls_replacement_053'], 'func': ls_replacement_d2_053}


def ls_replacement_d2_054(ls_replacement_054):
    feature = _clean(ls_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_054'] = {'inputs': ['ls_replacement_054'], 'func': ls_replacement_d2_054}


def ls_replacement_d2_055(ls_replacement_055):
    feature = _clean(ls_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_055'] = {'inputs': ['ls_replacement_055'], 'func': ls_replacement_d2_055}


def ls_replacement_d2_056(ls_replacement_056):
    feature = _clean(ls_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_056'] = {'inputs': ['ls_replacement_056'], 'func': ls_replacement_d2_056}


def ls_replacement_d2_057(ls_replacement_057):
    feature = _clean(ls_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_057'] = {'inputs': ['ls_replacement_057'], 'func': ls_replacement_d2_057}


def ls_replacement_d2_058(ls_replacement_058):
    feature = _clean(ls_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_058'] = {'inputs': ['ls_replacement_058'], 'func': ls_replacement_d2_058}


def ls_replacement_d2_059(ls_replacement_059):
    feature = _clean(ls_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_059'] = {'inputs': ['ls_replacement_059'], 'func': ls_replacement_d2_059}


def ls_replacement_d2_060(ls_replacement_060):
    feature = _clean(ls_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_060'] = {'inputs': ['ls_replacement_060'], 'func': ls_replacement_d2_060}


def ls_replacement_d2_061(ls_replacement_061):
    feature = _clean(ls_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_061'] = {'inputs': ['ls_replacement_061'], 'func': ls_replacement_d2_061}


def ls_replacement_d2_062(ls_replacement_062):
    feature = _clean(ls_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_062'] = {'inputs': ['ls_replacement_062'], 'func': ls_replacement_d2_062}


def ls_replacement_d2_063(ls_replacement_063):
    feature = _clean(ls_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_063'] = {'inputs': ['ls_replacement_063'], 'func': ls_replacement_d2_063}


def ls_replacement_d2_064(ls_replacement_064):
    feature = _clean(ls_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_064'] = {'inputs': ['ls_replacement_064'], 'func': ls_replacement_d2_064}


def ls_replacement_d2_065(ls_replacement_065):
    feature = _clean(ls_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_065'] = {'inputs': ['ls_replacement_065'], 'func': ls_replacement_d2_065}


def ls_replacement_d2_066(ls_replacement_066):
    feature = _clean(ls_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_066'] = {'inputs': ['ls_replacement_066'], 'func': ls_replacement_d2_066}


def ls_replacement_d2_067(ls_replacement_067):
    feature = _clean(ls_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_067'] = {'inputs': ['ls_replacement_067'], 'func': ls_replacement_d2_067}


def ls_replacement_d2_068(ls_replacement_068):
    feature = _clean(ls_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_068'] = {'inputs': ['ls_replacement_068'], 'func': ls_replacement_d2_068}


def ls_replacement_d2_069(ls_replacement_069):
    feature = _clean(ls_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_069'] = {'inputs': ['ls_replacement_069'], 'func': ls_replacement_d2_069}


def ls_replacement_d2_070(ls_replacement_070):
    feature = _clean(ls_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_070'] = {'inputs': ['ls_replacement_070'], 'func': ls_replacement_d2_070}


def ls_replacement_d2_071(ls_replacement_071):
    feature = _clean(ls_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_071'] = {'inputs': ['ls_replacement_071'], 'func': ls_replacement_d2_071}


def ls_replacement_d2_072(ls_replacement_072):
    feature = _clean(ls_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_072'] = {'inputs': ['ls_replacement_072'], 'func': ls_replacement_d2_072}


def ls_replacement_d2_073(ls_replacement_073):
    feature = _clean(ls_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_073'] = {'inputs': ['ls_replacement_073'], 'func': ls_replacement_d2_073}


def ls_replacement_d2_074(ls_replacement_074):
    feature = _clean(ls_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_074'] = {'inputs': ['ls_replacement_074'], 'func': ls_replacement_d2_074}


def ls_replacement_d2_075(ls_replacement_075):
    feature = _clean(ls_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_075'] = {'inputs': ['ls_replacement_075'], 'func': ls_replacement_d2_075}


def ls_replacement_d2_076(ls_replacement_076):
    feature = _clean(ls_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_076'] = {'inputs': ['ls_replacement_076'], 'func': ls_replacement_d2_076}


def ls_replacement_d2_077(ls_replacement_077):
    feature = _clean(ls_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_077'] = {'inputs': ['ls_replacement_077'], 'func': ls_replacement_d2_077}


def ls_replacement_d2_078(ls_replacement_078):
    feature = _clean(ls_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_078'] = {'inputs': ['ls_replacement_078'], 'func': ls_replacement_d2_078}


def ls_replacement_d2_079(ls_replacement_079):
    feature = _clean(ls_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_079'] = {'inputs': ['ls_replacement_079'], 'func': ls_replacement_d2_079}


def ls_replacement_d2_080(ls_replacement_080):
    feature = _clean(ls_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_080'] = {'inputs': ['ls_replacement_080'], 'func': ls_replacement_d2_080}


def ls_replacement_d2_081(ls_replacement_081):
    feature = _clean(ls_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_081'] = {'inputs': ['ls_replacement_081'], 'func': ls_replacement_d2_081}


def ls_replacement_d2_082(ls_replacement_082):
    feature = _clean(ls_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_082'] = {'inputs': ['ls_replacement_082'], 'func': ls_replacement_d2_082}


def ls_replacement_d2_083(ls_replacement_083):
    feature = _clean(ls_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_083'] = {'inputs': ['ls_replacement_083'], 'func': ls_replacement_d2_083}


def ls_replacement_d2_084(ls_replacement_084):
    feature = _clean(ls_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_084'] = {'inputs': ['ls_replacement_084'], 'func': ls_replacement_d2_084}


def ls_replacement_d2_085(ls_replacement_085):
    feature = _clean(ls_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_085'] = {'inputs': ['ls_replacement_085'], 'func': ls_replacement_d2_085}


def ls_replacement_d2_086(ls_replacement_086):
    feature = _clean(ls_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_086'] = {'inputs': ['ls_replacement_086'], 'func': ls_replacement_d2_086}


def ls_replacement_d2_087(ls_replacement_087):
    feature = _clean(ls_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_087'] = {'inputs': ['ls_replacement_087'], 'func': ls_replacement_d2_087}


def ls_replacement_d2_088(ls_replacement_088):
    feature = _clean(ls_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_088'] = {'inputs': ['ls_replacement_088'], 'func': ls_replacement_d2_088}


def ls_replacement_d2_089(ls_replacement_089):
    feature = _clean(ls_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_089'] = {'inputs': ['ls_replacement_089'], 'func': ls_replacement_d2_089}


def ls_replacement_d2_090(ls_replacement_090):
    feature = _clean(ls_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_090'] = {'inputs': ['ls_replacement_090'], 'func': ls_replacement_d2_090}


def ls_replacement_d2_091(ls_replacement_091):
    feature = _clean(ls_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_091'] = {'inputs': ['ls_replacement_091'], 'func': ls_replacement_d2_091}


def ls_replacement_d2_092(ls_replacement_092):
    feature = _clean(ls_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_092'] = {'inputs': ['ls_replacement_092'], 'func': ls_replacement_d2_092}


def ls_replacement_d2_093(ls_replacement_093):
    feature = _clean(ls_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_093'] = {'inputs': ['ls_replacement_093'], 'func': ls_replacement_d2_093}


def ls_replacement_d2_094(ls_replacement_094):
    feature = _clean(ls_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_094'] = {'inputs': ['ls_replacement_094'], 'func': ls_replacement_d2_094}


def ls_replacement_d2_095(ls_replacement_095):
    feature = _clean(ls_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_095'] = {'inputs': ['ls_replacement_095'], 'func': ls_replacement_d2_095}


def ls_replacement_d2_096(ls_replacement_096):
    feature = _clean(ls_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_096'] = {'inputs': ['ls_replacement_096'], 'func': ls_replacement_d2_096}


def ls_replacement_d2_097(ls_replacement_097):
    feature = _clean(ls_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_097'] = {'inputs': ['ls_replacement_097'], 'func': ls_replacement_d2_097}


def ls_replacement_d2_098(ls_replacement_098):
    feature = _clean(ls_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_098'] = {'inputs': ['ls_replacement_098'], 'func': ls_replacement_d2_098}


def ls_replacement_d2_099(ls_replacement_099):
    feature = _clean(ls_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_099'] = {'inputs': ['ls_replacement_099'], 'func': ls_replacement_d2_099}


def ls_replacement_d2_100(ls_replacement_100):
    feature = _clean(ls_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_100'] = {'inputs': ['ls_replacement_100'], 'func': ls_replacement_d2_100}


def ls_replacement_d2_101(ls_replacement_101):
    feature = _clean(ls_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_101'] = {'inputs': ['ls_replacement_101'], 'func': ls_replacement_d2_101}


def ls_replacement_d2_102(ls_replacement_102):
    feature = _clean(ls_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_102'] = {'inputs': ['ls_replacement_102'], 'func': ls_replacement_d2_102}


def ls_replacement_d2_103(ls_replacement_103):
    feature = _clean(ls_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_103'] = {'inputs': ['ls_replacement_103'], 'func': ls_replacement_d2_103}


def ls_replacement_d2_104(ls_replacement_104):
    feature = _clean(ls_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_104'] = {'inputs': ['ls_replacement_104'], 'func': ls_replacement_d2_104}


def ls_replacement_d2_105(ls_replacement_105):
    feature = _clean(ls_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_105'] = {'inputs': ['ls_replacement_105'], 'func': ls_replacement_d2_105}


def ls_replacement_d2_106(ls_replacement_106):
    feature = _clean(ls_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_106'] = {'inputs': ['ls_replacement_106'], 'func': ls_replacement_d2_106}


def ls_replacement_d2_107(ls_replacement_107):
    feature = _clean(ls_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_107'] = {'inputs': ['ls_replacement_107'], 'func': ls_replacement_d2_107}


def ls_replacement_d2_108(ls_replacement_108):
    feature = _clean(ls_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_108'] = {'inputs': ['ls_replacement_108'], 'func': ls_replacement_d2_108}


def ls_replacement_d2_109(ls_replacement_109):
    feature = _clean(ls_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_109'] = {'inputs': ['ls_replacement_109'], 'func': ls_replacement_d2_109}


def ls_replacement_d2_110(ls_replacement_110):
    feature = _clean(ls_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_110'] = {'inputs': ['ls_replacement_110'], 'func': ls_replacement_d2_110}


def ls_replacement_d2_111(ls_replacement_111):
    feature = _clean(ls_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_111'] = {'inputs': ['ls_replacement_111'], 'func': ls_replacement_d2_111}


def ls_replacement_d2_112(ls_replacement_112):
    feature = _clean(ls_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_112'] = {'inputs': ['ls_replacement_112'], 'func': ls_replacement_d2_112}


def ls_replacement_d2_113(ls_replacement_113):
    feature = _clean(ls_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_113'] = {'inputs': ['ls_replacement_113'], 'func': ls_replacement_d2_113}


def ls_replacement_d2_114(ls_replacement_114):
    feature = _clean(ls_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_114'] = {'inputs': ['ls_replacement_114'], 'func': ls_replacement_d2_114}


def ls_replacement_d2_115(ls_replacement_115):
    feature = _clean(ls_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_115'] = {'inputs': ['ls_replacement_115'], 'func': ls_replacement_d2_115}


def ls_replacement_d2_116(ls_replacement_116):
    feature = _clean(ls_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_116'] = {'inputs': ['ls_replacement_116'], 'func': ls_replacement_d2_116}


def ls_replacement_d2_117(ls_replacement_117):
    feature = _clean(ls_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_117'] = {'inputs': ['ls_replacement_117'], 'func': ls_replacement_d2_117}


def ls_replacement_d2_118(ls_replacement_118):
    feature = _clean(ls_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_118'] = {'inputs': ['ls_replacement_118'], 'func': ls_replacement_d2_118}


def ls_replacement_d2_119(ls_replacement_119):
    feature = _clean(ls_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_119'] = {'inputs': ['ls_replacement_119'], 'func': ls_replacement_d2_119}


def ls_replacement_d2_120(ls_replacement_120):
    feature = _clean(ls_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_120'] = {'inputs': ['ls_replacement_120'], 'func': ls_replacement_d2_120}


def ls_replacement_d2_121(ls_replacement_121):
    feature = _clean(ls_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_121'] = {'inputs': ['ls_replacement_121'], 'func': ls_replacement_d2_121}


def ls_replacement_d2_122(ls_replacement_122):
    feature = _clean(ls_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_122'] = {'inputs': ['ls_replacement_122'], 'func': ls_replacement_d2_122}


def ls_replacement_d2_123(ls_replacement_123):
    feature = _clean(ls_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_123'] = {'inputs': ['ls_replacement_123'], 'func': ls_replacement_d2_123}


def ls_replacement_d2_124(ls_replacement_124):
    feature = _clean(ls_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_124'] = {'inputs': ['ls_replacement_124'], 'func': ls_replacement_d2_124}


def ls_replacement_d2_125(ls_replacement_125):
    feature = _clean(ls_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_125'] = {'inputs': ['ls_replacement_125'], 'func': ls_replacement_d2_125}


def ls_replacement_d2_126(ls_replacement_126):
    feature = _clean(ls_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_126'] = {'inputs': ['ls_replacement_126'], 'func': ls_replacement_d2_126}


def ls_replacement_d2_127(ls_replacement_127):
    feature = _clean(ls_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_127'] = {'inputs': ['ls_replacement_127'], 'func': ls_replacement_d2_127}


def ls_replacement_d2_128(ls_replacement_128):
    feature = _clean(ls_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_128'] = {'inputs': ['ls_replacement_128'], 'func': ls_replacement_d2_128}


def ls_replacement_d2_129(ls_replacement_129):
    feature = _clean(ls_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_129'] = {'inputs': ['ls_replacement_129'], 'func': ls_replacement_d2_129}


def ls_replacement_d2_130(ls_replacement_130):
    feature = _clean(ls_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_130'] = {'inputs': ['ls_replacement_130'], 'func': ls_replacement_d2_130}


def ls_replacement_d2_131(ls_replacement_131):
    feature = _clean(ls_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_131'] = {'inputs': ['ls_replacement_131'], 'func': ls_replacement_d2_131}


def ls_replacement_d2_132(ls_replacement_132):
    feature = _clean(ls_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_132'] = {'inputs': ['ls_replacement_132'], 'func': ls_replacement_d2_132}


def ls_replacement_d2_133(ls_replacement_133):
    feature = _clean(ls_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_133'] = {'inputs': ['ls_replacement_133'], 'func': ls_replacement_d2_133}


def ls_replacement_d2_134(ls_replacement_134):
    feature = _clean(ls_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_134'] = {'inputs': ['ls_replacement_134'], 'func': ls_replacement_d2_134}


def ls_replacement_d2_135(ls_replacement_135):
    feature = _clean(ls_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_135'] = {'inputs': ['ls_replacement_135'], 'func': ls_replacement_d2_135}


def ls_replacement_d2_136(ls_replacement_136):
    feature = _clean(ls_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_136'] = {'inputs': ['ls_replacement_136'], 'func': ls_replacement_d2_136}


def ls_replacement_d2_137(ls_replacement_137):
    feature = _clean(ls_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_137'] = {'inputs': ['ls_replacement_137'], 'func': ls_replacement_d2_137}


def ls_replacement_d2_138(ls_replacement_138):
    feature = _clean(ls_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_138'] = {'inputs': ['ls_replacement_138'], 'func': ls_replacement_d2_138}


def ls_replacement_d2_139(ls_replacement_139):
    feature = _clean(ls_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_139'] = {'inputs': ['ls_replacement_139'], 'func': ls_replacement_d2_139}


def ls_replacement_d2_140(ls_replacement_140):
    feature = _clean(ls_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_140'] = {'inputs': ['ls_replacement_140'], 'func': ls_replacement_d2_140}


def ls_replacement_d2_141(ls_replacement_141):
    feature = _clean(ls_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_141'] = {'inputs': ['ls_replacement_141'], 'func': ls_replacement_d2_141}


def ls_replacement_d2_142(ls_replacement_142):
    feature = _clean(ls_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_142'] = {'inputs': ['ls_replacement_142'], 'func': ls_replacement_d2_142}


def ls_replacement_d2_143(ls_replacement_143):
    feature = _clean(ls_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_143'] = {'inputs': ['ls_replacement_143'], 'func': ls_replacement_d2_143}


def ls_replacement_d2_144(ls_replacement_144):
    feature = _clean(ls_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_144'] = {'inputs': ['ls_replacement_144'], 'func': ls_replacement_d2_144}


def ls_replacement_d2_145(ls_replacement_145):
    feature = _clean(ls_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_145'] = {'inputs': ['ls_replacement_145'], 'func': ls_replacement_d2_145}


def ls_replacement_d2_146(ls_replacement_146):
    feature = _clean(ls_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_146'] = {'inputs': ['ls_replacement_146'], 'func': ls_replacement_d2_146}


def ls_replacement_d2_147(ls_replacement_147):
    feature = _clean(ls_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_147'] = {'inputs': ['ls_replacement_147'], 'func': ls_replacement_d2_147}


def ls_replacement_d2_148(ls_replacement_148):
    feature = _clean(ls_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_148'] = {'inputs': ['ls_replacement_148'], 'func': ls_replacement_d2_148}


def ls_replacement_d2_149(ls_replacement_149):
    feature = _clean(ls_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_149'] = {'inputs': ['ls_replacement_149'], 'func': ls_replacement_d2_149}


def ls_replacement_d2_150(ls_replacement_150):
    feature = _clean(ls_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_150'] = {'inputs': ['ls_replacement_150'], 'func': ls_replacement_d2_150}


def ls_replacement_d2_151(ls_replacement_151):
    feature = _clean(ls_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_151'] = {'inputs': ['ls_replacement_151'], 'func': ls_replacement_d2_151}


def ls_replacement_d2_152(ls_replacement_152):
    feature = _clean(ls_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_152'] = {'inputs': ['ls_replacement_152'], 'func': ls_replacement_d2_152}


def ls_replacement_d2_153(ls_replacement_153):
    feature = _clean(ls_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_153'] = {'inputs': ['ls_replacement_153'], 'func': ls_replacement_d2_153}


def ls_replacement_d2_154(ls_replacement_154):
    feature = _clean(ls_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_154'] = {'inputs': ['ls_replacement_154'], 'func': ls_replacement_d2_154}


def ls_replacement_d2_155(ls_replacement_155):
    feature = _clean(ls_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_155'] = {'inputs': ['ls_replacement_155'], 'func': ls_replacement_d2_155}


def ls_replacement_d2_156(ls_replacement_156):
    feature = _clean(ls_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_156'] = {'inputs': ['ls_replacement_156'], 'func': ls_replacement_d2_156}


def ls_replacement_d2_157(ls_replacement_157):
    feature = _clean(ls_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_157'] = {'inputs': ['ls_replacement_157'], 'func': ls_replacement_d2_157}


def ls_replacement_d2_158(ls_replacement_158):
    feature = _clean(ls_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_158'] = {'inputs': ['ls_replacement_158'], 'func': ls_replacement_d2_158}


def ls_replacement_d2_159(ls_replacement_159):
    feature = _clean(ls_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_159'] = {'inputs': ['ls_replacement_159'], 'func': ls_replacement_d2_159}


def ls_replacement_d2_160(ls_replacement_160):
    feature = _clean(ls_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_160'] = {'inputs': ['ls_replacement_160'], 'func': ls_replacement_d2_160}


def ls_replacement_d2_161(ls_replacement_161):
    feature = _clean(ls_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_161'] = {'inputs': ['ls_replacement_161'], 'func': ls_replacement_d2_161}


def ls_replacement_d2_162(ls_replacement_162):
    feature = _clean(ls_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_162'] = {'inputs': ['ls_replacement_162'], 'func': ls_replacement_d2_162}


def ls_replacement_d2_163(ls_replacement_163):
    feature = _clean(ls_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_163'] = {'inputs': ['ls_replacement_163'], 'func': ls_replacement_d2_163}


def ls_replacement_d2_164(ls_replacement_164):
    feature = _clean(ls_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_164'] = {'inputs': ['ls_replacement_164'], 'func': ls_replacement_d2_164}


def ls_replacement_d2_165(ls_replacement_165):
    feature = _clean(ls_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_165'] = {'inputs': ['ls_replacement_165'], 'func': ls_replacement_d2_165}


def ls_replacement_d2_166(ls_replacement_166):
    feature = _clean(ls_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
LS_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ls_replacement_d2_166'] = {'inputs': ['ls_replacement_166'], 'func': ls_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def lvs_base_universe_d2_001_lvs_003_fcf_burn_to_cash_63(lvs_003_fcf_burn_to_cash_63):
    return _base_universe_d2(lvs_003_fcf_burn_to_cash_63, 1)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_001_lvs_003_fcf_burn_to_cash_63'] = {'inputs': ['lvs_003_fcf_burn_to_cash_63'], 'func': lvs_base_universe_d2_001_lvs_003_fcf_burn_to_cash_63}


def lvs_base_universe_d2_002_lvs_004_debt_to_equity_84(lvs_004_debt_to_equity_84):
    return _base_universe_d2(lvs_004_debt_to_equity_84, 2)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_002_lvs_004_debt_to_equity_84'] = {'inputs': ['lvs_004_debt_to_equity_84'], 'func': lvs_base_universe_d2_002_lvs_004_debt_to_equity_84}


def lvs_base_universe_d2_003_lvs_005_debt_to_assets_126(lvs_005_debt_to_assets_126):
    return _base_universe_d2(lvs_005_debt_to_assets_126, 3)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_003_lvs_005_debt_to_assets_126'] = {'inputs': ['lvs_005_debt_to_assets_126'], 'func': lvs_base_universe_d2_003_lvs_005_debt_to_assets_126}


def lvs_base_universe_d2_004_lvs_012_accrual_gap_1260(lvs_012_accrual_gap_1260):
    return _base_universe_d2(lvs_012_accrual_gap_1260, 4)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_004_lvs_012_accrual_gap_1260'] = {'inputs': ['lvs_012_accrual_gap_1260'], 'func': lvs_base_universe_d2_004_lvs_012_accrual_gap_1260}


def lvs_base_universe_d2_005_lvs_016_debt_to_equity_21(lvs_016_debt_to_equity_21):
    return _base_universe_d2(lvs_016_debt_to_equity_21, 5)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_005_lvs_016_debt_to_equity_21'] = {'inputs': ['lvs_016_debt_to_equity_21'], 'func': lvs_base_universe_d2_005_lvs_016_debt_to_equity_21}


def lvs_base_universe_d2_006_lvs_017_debt_to_assets_42(lvs_017_debt_to_assets_42):
    return _base_universe_d2(lvs_017_debt_to_assets_42, 6)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_006_lvs_017_debt_to_assets_42'] = {'inputs': ['lvs_017_debt_to_assets_42'], 'func': lvs_base_universe_d2_006_lvs_017_debt_to_assets_42}


def lvs_base_universe_d2_007_lvs_024_accrual_gap_504(lvs_024_accrual_gap_504):
    return _base_universe_d2(lvs_024_accrual_gap_504, 7)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_007_lvs_024_accrual_gap_504'] = {'inputs': ['lvs_024_accrual_gap_504'], 'func': lvs_base_universe_d2_007_lvs_024_accrual_gap_504}


def lvs_base_universe_d2_008_lvs_027_fcf_burn_to_cash_1260(lvs_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(lvs_027_fcf_burn_to_cash_1260, 8)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_008_lvs_027_fcf_burn_to_cash_1260'] = {'inputs': ['lvs_027_fcf_burn_to_cash_1260'], 'func': lvs_base_universe_d2_008_lvs_027_fcf_burn_to_cash_1260}


def lvs_base_universe_d2_009_lvs_028_debt_to_equity_1512(lvs_028_debt_to_equity_1512):
    return _base_universe_d2(lvs_028_debt_to_equity_1512, 9)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_009_lvs_028_debt_to_equity_1512'] = {'inputs': ['lvs_028_debt_to_equity_1512'], 'func': lvs_base_universe_d2_009_lvs_028_debt_to_equity_1512}


def lvs_base_universe_d2_010_lvs_029_debt_to_assets_63(lvs_029_debt_to_assets_63):
    return _base_universe_d2(lvs_029_debt_to_assets_63, 10)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_010_lvs_029_debt_to_assets_63'] = {'inputs': ['lvs_029_debt_to_assets_63'], 'func': lvs_base_universe_d2_010_lvs_029_debt_to_assets_63}


def lvs_base_universe_d2_011_lvs_031_interest_coverage_stress_21(lvs_031_interest_coverage_stress_21):
    return _base_universe_d2(lvs_031_interest_coverage_stress_21, 11)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_011_lvs_031_interest_coverage_stress_21'] = {'inputs': ['lvs_031_interest_coverage_stress_21'], 'func': lvs_base_universe_d2_011_lvs_031_interest_coverage_stress_21}


def lvs_base_universe_d2_012_lvs_036_accrual_gap_189(lvs_036_accrual_gap_189):
    return _base_universe_d2(lvs_036_accrual_gap_189, 12)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_012_lvs_036_accrual_gap_189'] = {'inputs': ['lvs_036_accrual_gap_189'], 'func': lvs_base_universe_d2_012_lvs_036_accrual_gap_189}


def lvs_base_universe_d2_013_lvs_039_fcf_burn_to_cash_504(lvs_039_fcf_burn_to_cash_504):
    return _base_universe_d2(lvs_039_fcf_burn_to_cash_504, 13)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_013_lvs_039_fcf_burn_to_cash_504'] = {'inputs': ['lvs_039_fcf_burn_to_cash_504'], 'func': lvs_base_universe_d2_013_lvs_039_fcf_burn_to_cash_504}


def lvs_base_universe_d2_014_lvs_040_debt_to_equity_756(lvs_040_debt_to_equity_756):
    return _base_universe_d2(lvs_040_debt_to_equity_756, 14)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_014_lvs_040_debt_to_equity_756'] = {'inputs': ['lvs_040_debt_to_equity_756'], 'func': lvs_base_universe_d2_014_lvs_040_debt_to_equity_756}


def lvs_base_universe_d2_015_lvs_041_debt_to_assets_1008(lvs_041_debt_to_assets_1008):
    return _base_universe_d2(lvs_041_debt_to_assets_1008, 15)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_015_lvs_041_debt_to_assets_1008'] = {'inputs': ['lvs_041_debt_to_assets_1008'], 'func': lvs_base_universe_d2_015_lvs_041_debt_to_assets_1008}


def lvs_base_universe_d2_016_lvs_043_interest_coverage_stress_1512(lvs_043_interest_coverage_stress_1512):
    return _base_universe_d2(lvs_043_interest_coverage_stress_1512, 16)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_016_lvs_043_interest_coverage_stress_1512'] = {'inputs': ['lvs_043_interest_coverage_stress_1512'], 'func': lvs_base_universe_d2_016_lvs_043_interest_coverage_stress_1512}


def lvs_base_universe_d2_017_lvs_048_accrual_gap_63(lvs_048_accrual_gap_63):
    return _base_universe_d2(lvs_048_accrual_gap_63, 17)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_017_lvs_048_accrual_gap_63'] = {'inputs': ['lvs_048_accrual_gap_63'], 'func': lvs_base_universe_d2_017_lvs_048_accrual_gap_63}


def lvs_base_universe_d2_018_lvs_051_fcf_burn_to_cash_189(lvs_051_fcf_burn_to_cash_189):
    return _base_universe_d2(lvs_051_fcf_burn_to_cash_189, 18)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_018_lvs_051_fcf_burn_to_cash_189'] = {'inputs': ['lvs_051_fcf_burn_to_cash_189'], 'func': lvs_base_universe_d2_018_lvs_051_fcf_burn_to_cash_189}


def lvs_base_universe_d2_019_lvs_052_debt_to_equity_252(lvs_052_debt_to_equity_252):
    return _base_universe_d2(lvs_052_debt_to_equity_252, 19)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_019_lvs_052_debt_to_equity_252'] = {'inputs': ['lvs_052_debt_to_equity_252'], 'func': lvs_base_universe_d2_019_lvs_052_debt_to_equity_252}


def lvs_base_universe_d2_020_lvs_053_debt_to_assets_378(lvs_053_debt_to_assets_378):
    return _base_universe_d2(lvs_053_debt_to_assets_378, 20)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_020_lvs_053_debt_to_assets_378'] = {'inputs': ['lvs_053_debt_to_assets_378'], 'func': lvs_base_universe_d2_020_lvs_053_debt_to_assets_378}


def lvs_base_universe_d2_021_lvs_055_interest_coverage_stress_756(lvs_055_interest_coverage_stress_756):
    return _base_universe_d2(lvs_055_interest_coverage_stress_756, 21)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_021_lvs_055_interest_coverage_stress_756'] = {'inputs': ['lvs_055_interest_coverage_stress_756'], 'func': lvs_base_universe_d2_021_lvs_055_interest_coverage_stress_756}


def lvs_base_universe_d2_022_lvs_060_accrual_gap_252(lvs_060_accrual_gap_252):
    return _base_universe_d2(lvs_060_accrual_gap_252, 22)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_022_lvs_060_accrual_gap_252'] = {'inputs': ['lvs_060_accrual_gap_252'], 'func': lvs_base_universe_d2_022_lvs_060_accrual_gap_252}


def lvs_base_universe_d2_023_lvs_basefill_001(lvs_basefill_001):
    return _base_universe_d2(lvs_basefill_001, 23)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_023_lvs_basefill_001'] = {'inputs': ['lvs_basefill_001'], 'func': lvs_base_universe_d2_023_lvs_basefill_001}


def lvs_base_universe_d2_024_lvs_basefill_002(lvs_basefill_002):
    return _base_universe_d2(lvs_basefill_002, 24)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_024_lvs_basefill_002'] = {'inputs': ['lvs_basefill_002'], 'func': lvs_base_universe_d2_024_lvs_basefill_002}


def lvs_base_universe_d2_025_lvs_basefill_006(lvs_basefill_006):
    return _base_universe_d2(lvs_basefill_006, 25)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_025_lvs_basefill_006'] = {'inputs': ['lvs_basefill_006'], 'func': lvs_base_universe_d2_025_lvs_basefill_006}


def lvs_base_universe_d2_026_lvs_basefill_008(lvs_basefill_008):
    return _base_universe_d2(lvs_basefill_008, 26)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_026_lvs_basefill_008'] = {'inputs': ['lvs_basefill_008'], 'func': lvs_base_universe_d2_026_lvs_basefill_008}


def lvs_base_universe_d2_027_lvs_basefill_009(lvs_basefill_009):
    return _base_universe_d2(lvs_basefill_009, 27)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_027_lvs_basefill_009'] = {'inputs': ['lvs_basefill_009'], 'func': lvs_base_universe_d2_027_lvs_basefill_009}


def lvs_base_universe_d2_028_lvs_basefill_010(lvs_basefill_010):
    return _base_universe_d2(lvs_basefill_010, 28)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_028_lvs_basefill_010'] = {'inputs': ['lvs_basefill_010'], 'func': lvs_base_universe_d2_028_lvs_basefill_010}


def lvs_base_universe_d2_029_lvs_basefill_011(lvs_basefill_011):
    return _base_universe_d2(lvs_basefill_011, 29)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_029_lvs_basefill_011'] = {'inputs': ['lvs_basefill_011'], 'func': lvs_base_universe_d2_029_lvs_basefill_011}


def lvs_base_universe_d2_030_lvs_basefill_013(lvs_basefill_013):
    return _base_universe_d2(lvs_basefill_013, 30)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_030_lvs_basefill_013'] = {'inputs': ['lvs_basefill_013'], 'func': lvs_base_universe_d2_030_lvs_basefill_013}


def lvs_base_universe_d2_031_lvs_basefill_014(lvs_basefill_014):
    return _base_universe_d2(lvs_basefill_014, 31)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_031_lvs_basefill_014'] = {'inputs': ['lvs_basefill_014'], 'func': lvs_base_universe_d2_031_lvs_basefill_014}


def lvs_base_universe_d2_032_lvs_basefill_015(lvs_basefill_015):
    return _base_universe_d2(lvs_basefill_015, 32)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_032_lvs_basefill_015'] = {'inputs': ['lvs_basefill_015'], 'func': lvs_base_universe_d2_032_lvs_basefill_015}


def lvs_base_universe_d2_033_lvs_basefill_018(lvs_basefill_018):
    return _base_universe_d2(lvs_basefill_018, 33)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_033_lvs_basefill_018'] = {'inputs': ['lvs_basefill_018'], 'func': lvs_base_universe_d2_033_lvs_basefill_018}


def lvs_base_universe_d2_034_lvs_basefill_020(lvs_basefill_020):
    return _base_universe_d2(lvs_basefill_020, 34)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_034_lvs_basefill_020'] = {'inputs': ['lvs_basefill_020'], 'func': lvs_base_universe_d2_034_lvs_basefill_020}


def lvs_base_universe_d2_035_lvs_basefill_021(lvs_basefill_021):
    return _base_universe_d2(lvs_basefill_021, 35)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_035_lvs_basefill_021'] = {'inputs': ['lvs_basefill_021'], 'func': lvs_base_universe_d2_035_lvs_basefill_021}


def lvs_base_universe_d2_036_lvs_basefill_022(lvs_basefill_022):
    return _base_universe_d2(lvs_basefill_022, 36)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_036_lvs_basefill_022'] = {'inputs': ['lvs_basefill_022'], 'func': lvs_base_universe_d2_036_lvs_basefill_022}


def lvs_base_universe_d2_037_lvs_basefill_023(lvs_basefill_023):
    return _base_universe_d2(lvs_basefill_023, 37)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_037_lvs_basefill_023'] = {'inputs': ['lvs_basefill_023'], 'func': lvs_base_universe_d2_037_lvs_basefill_023}


def lvs_base_universe_d2_038_lvs_basefill_025(lvs_basefill_025):
    return _base_universe_d2(lvs_basefill_025, 38)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_038_lvs_basefill_025'] = {'inputs': ['lvs_basefill_025'], 'func': lvs_base_universe_d2_038_lvs_basefill_025}


def lvs_base_universe_d2_039_lvs_basefill_026(lvs_basefill_026):
    return _base_universe_d2(lvs_basefill_026, 39)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_039_lvs_basefill_026'] = {'inputs': ['lvs_basefill_026'], 'func': lvs_base_universe_d2_039_lvs_basefill_026}


def lvs_base_universe_d2_040_lvs_basefill_030(lvs_basefill_030):
    return _base_universe_d2(lvs_basefill_030, 40)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_040_lvs_basefill_030'] = {'inputs': ['lvs_basefill_030'], 'func': lvs_base_universe_d2_040_lvs_basefill_030}


def lvs_base_universe_d2_041_lvs_basefill_032(lvs_basefill_032):
    return _base_universe_d2(lvs_basefill_032, 41)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_041_lvs_basefill_032'] = {'inputs': ['lvs_basefill_032'], 'func': lvs_base_universe_d2_041_lvs_basefill_032}


def lvs_base_universe_d2_042_lvs_basefill_033(lvs_basefill_033):
    return _base_universe_d2(lvs_basefill_033, 42)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_042_lvs_basefill_033'] = {'inputs': ['lvs_basefill_033'], 'func': lvs_base_universe_d2_042_lvs_basefill_033}


def lvs_base_universe_d2_043_lvs_basefill_034(lvs_basefill_034):
    return _base_universe_d2(lvs_basefill_034, 43)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_043_lvs_basefill_034'] = {'inputs': ['lvs_basefill_034'], 'func': lvs_base_universe_d2_043_lvs_basefill_034}


def lvs_base_universe_d2_044_lvs_basefill_035(lvs_basefill_035):
    return _base_universe_d2(lvs_basefill_035, 44)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_044_lvs_basefill_035'] = {'inputs': ['lvs_basefill_035'], 'func': lvs_base_universe_d2_044_lvs_basefill_035}


def lvs_base_universe_d2_045_lvs_basefill_037(lvs_basefill_037):
    return _base_universe_d2(lvs_basefill_037, 45)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_045_lvs_basefill_037'] = {'inputs': ['lvs_basefill_037'], 'func': lvs_base_universe_d2_045_lvs_basefill_037}


def lvs_base_universe_d2_046_lvs_basefill_038(lvs_basefill_038):
    return _base_universe_d2(lvs_basefill_038, 46)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_046_lvs_basefill_038'] = {'inputs': ['lvs_basefill_038'], 'func': lvs_base_universe_d2_046_lvs_basefill_038}


def lvs_base_universe_d2_047_lvs_basefill_042(lvs_basefill_042):
    return _base_universe_d2(lvs_basefill_042, 47)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_047_lvs_basefill_042'] = {'inputs': ['lvs_basefill_042'], 'func': lvs_base_universe_d2_047_lvs_basefill_042}


def lvs_base_universe_d2_048_lvs_basefill_044(lvs_basefill_044):
    return _base_universe_d2(lvs_basefill_044, 48)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_048_lvs_basefill_044'] = {'inputs': ['lvs_basefill_044'], 'func': lvs_base_universe_d2_048_lvs_basefill_044}


def lvs_base_universe_d2_049_lvs_basefill_045(lvs_basefill_045):
    return _base_universe_d2(lvs_basefill_045, 49)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_049_lvs_basefill_045'] = {'inputs': ['lvs_basefill_045'], 'func': lvs_base_universe_d2_049_lvs_basefill_045}


def lvs_base_universe_d2_050_lvs_basefill_046(lvs_basefill_046):
    return _base_universe_d2(lvs_basefill_046, 50)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_050_lvs_basefill_046'] = {'inputs': ['lvs_basefill_046'], 'func': lvs_base_universe_d2_050_lvs_basefill_046}


def lvs_base_universe_d2_051_lvs_basefill_047(lvs_basefill_047):
    return _base_universe_d2(lvs_basefill_047, 51)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_051_lvs_basefill_047'] = {'inputs': ['lvs_basefill_047'], 'func': lvs_base_universe_d2_051_lvs_basefill_047}


def lvs_base_universe_d2_052_lvs_basefill_049(lvs_basefill_049):
    return _base_universe_d2(lvs_basefill_049, 52)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_052_lvs_basefill_049'] = {'inputs': ['lvs_basefill_049'], 'func': lvs_base_universe_d2_052_lvs_basefill_049}


def lvs_base_universe_d2_053_lvs_basefill_050(lvs_basefill_050):
    return _base_universe_d2(lvs_basefill_050, 53)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_053_lvs_basefill_050'] = {'inputs': ['lvs_basefill_050'], 'func': lvs_base_universe_d2_053_lvs_basefill_050}


def lvs_base_universe_d2_054_lvs_basefill_054(lvs_basefill_054):
    return _base_universe_d2(lvs_basefill_054, 54)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_054_lvs_basefill_054'] = {'inputs': ['lvs_basefill_054'], 'func': lvs_base_universe_d2_054_lvs_basefill_054}


def lvs_base_universe_d2_055_lvs_basefill_056(lvs_basefill_056):
    return _base_universe_d2(lvs_basefill_056, 55)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_055_lvs_basefill_056'] = {'inputs': ['lvs_basefill_056'], 'func': lvs_base_universe_d2_055_lvs_basefill_056}


def lvs_base_universe_d2_056_lvs_basefill_057(lvs_basefill_057):
    return _base_universe_d2(lvs_basefill_057, 56)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_056_lvs_basefill_057'] = {'inputs': ['lvs_basefill_057'], 'func': lvs_base_universe_d2_056_lvs_basefill_057}


def lvs_base_universe_d2_057_lvs_basefill_058(lvs_basefill_058):
    return _base_universe_d2(lvs_basefill_058, 57)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_057_lvs_basefill_058'] = {'inputs': ['lvs_basefill_058'], 'func': lvs_base_universe_d2_057_lvs_basefill_058}


def lvs_base_universe_d2_058_lvs_basefill_059(lvs_basefill_059):
    return _base_universe_d2(lvs_basefill_059, 58)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_058_lvs_basefill_059'] = {'inputs': ['lvs_basefill_059'], 'func': lvs_base_universe_d2_058_lvs_basefill_059}


def lvs_base_universe_d2_059_lvs_basefill_061(lvs_basefill_061):
    return _base_universe_d2(lvs_basefill_061, 59)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_059_lvs_basefill_061'] = {'inputs': ['lvs_basefill_061'], 'func': lvs_base_universe_d2_059_lvs_basefill_061}


def lvs_base_universe_d2_060_lvs_basefill_062(lvs_basefill_062):
    return _base_universe_d2(lvs_basefill_062, 60)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_060_lvs_basefill_062'] = {'inputs': ['lvs_basefill_062'], 'func': lvs_base_universe_d2_060_lvs_basefill_062}


def lvs_base_universe_d2_061_lvs_basefill_063(lvs_basefill_063):
    return _base_universe_d2(lvs_basefill_063, 61)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_061_lvs_basefill_063'] = {'inputs': ['lvs_basefill_063'], 'func': lvs_base_universe_d2_061_lvs_basefill_063}


def lvs_base_universe_d2_062_lvs_basefill_064(lvs_basefill_064):
    return _base_universe_d2(lvs_basefill_064, 62)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_062_lvs_basefill_064'] = {'inputs': ['lvs_basefill_064'], 'func': lvs_base_universe_d2_062_lvs_basefill_064}


def lvs_base_universe_d2_063_lvs_basefill_065(lvs_basefill_065):
    return _base_universe_d2(lvs_basefill_065, 63)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_063_lvs_basefill_065'] = {'inputs': ['lvs_basefill_065'], 'func': lvs_base_universe_d2_063_lvs_basefill_065}


def lvs_base_universe_d2_064_lvs_basefill_066(lvs_basefill_066):
    return _base_universe_d2(lvs_basefill_066, 64)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_064_lvs_basefill_066'] = {'inputs': ['lvs_basefill_066'], 'func': lvs_base_universe_d2_064_lvs_basefill_066}


def lvs_base_universe_d2_065_lvs_basefill_067(lvs_basefill_067):
    return _base_universe_d2(lvs_basefill_067, 65)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_065_lvs_basefill_067'] = {'inputs': ['lvs_basefill_067'], 'func': lvs_base_universe_d2_065_lvs_basefill_067}


def lvs_base_universe_d2_066_lvs_basefill_068(lvs_basefill_068):
    return _base_universe_d2(lvs_basefill_068, 66)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_066_lvs_basefill_068'] = {'inputs': ['lvs_basefill_068'], 'func': lvs_base_universe_d2_066_lvs_basefill_068}


def lvs_base_universe_d2_067_lvs_basefill_069(lvs_basefill_069):
    return _base_universe_d2(lvs_basefill_069, 67)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_067_lvs_basefill_069'] = {'inputs': ['lvs_basefill_069'], 'func': lvs_base_universe_d2_067_lvs_basefill_069}


def lvs_base_universe_d2_068_lvs_basefill_070(lvs_basefill_070):
    return _base_universe_d2(lvs_basefill_070, 68)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_068_lvs_basefill_070'] = {'inputs': ['lvs_basefill_070'], 'func': lvs_base_universe_d2_068_lvs_basefill_070}


def lvs_base_universe_d2_069_lvs_basefill_071(lvs_basefill_071):
    return _base_universe_d2(lvs_basefill_071, 69)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_069_lvs_basefill_071'] = {'inputs': ['lvs_basefill_071'], 'func': lvs_base_universe_d2_069_lvs_basefill_071}


def lvs_base_universe_d2_070_lvs_basefill_072(lvs_basefill_072):
    return _base_universe_d2(lvs_basefill_072, 70)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_070_lvs_basefill_072'] = {'inputs': ['lvs_basefill_072'], 'func': lvs_base_universe_d2_070_lvs_basefill_072}


def lvs_base_universe_d2_071_lvs_basefill_073(lvs_basefill_073):
    return _base_universe_d2(lvs_basefill_073, 71)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_071_lvs_basefill_073'] = {'inputs': ['lvs_basefill_073'], 'func': lvs_base_universe_d2_071_lvs_basefill_073}


def lvs_base_universe_d2_072_lvs_basefill_074(lvs_basefill_074):
    return _base_universe_d2(lvs_basefill_074, 72)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_072_lvs_basefill_074'] = {'inputs': ['lvs_basefill_074'], 'func': lvs_base_universe_d2_072_lvs_basefill_074}


def lvs_base_universe_d2_073_lvs_basefill_075(lvs_basefill_075):
    return _base_universe_d2(lvs_basefill_075, 73)
LVS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['lvs_base_universe_d2_073_lvs_basefill_075'] = {'inputs': ['lvs_basefill_075'], 'func': lvs_base_universe_d2_073_lvs_basefill_075}
