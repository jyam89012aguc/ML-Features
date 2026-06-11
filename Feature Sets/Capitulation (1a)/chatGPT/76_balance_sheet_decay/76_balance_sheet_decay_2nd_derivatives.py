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



def bsd_151_bsd_001_netinc_decline_1_roc_1(netinc):
    feature = _s(netinc)
    return (_roc(feature, 1)).reindex(feature.index)

def bsd_152_bsd_007_interest_coverage_stress_252_roc_42(bsd_007_interest_coverage_stress_252):
    feature = _s(bsd_007_interest_coverage_stress_252)
    return (_roc(feature, 42)).reindex(feature.index)

def bsd_153_bsd_013_netinc_decline_1_roc_126(netinc):
    feature = _s(netinc)
    return (_roc(feature, 126)).reindex(feature.index)

def bsd_154_bsd_019_interest_coverage_stress_84_roc_378(bsd_019_interest_coverage_stress_84):
    feature = _s(bsd_019_interest_coverage_stress_84)
    return (_roc(feature, 378)).reindex(feature.index)

def bsd_155_bsd_025_netinc_decline_1_roc_4(netinc):
    feature = _s(netinc)
    return (_roc(feature, 4)).reindex(feature.index)






















BALANCE_SHEET_DECAY_REGISTRY_2ND_DERIVATIVES = {
    'bsd_151_bsd_001_netinc_decline_1_roc_1': {'inputs': ['netinc'], 'func': bsd_151_bsd_001_netinc_decline_1_roc_1},
    'bsd_152_bsd_007_interest_coverage_stress_252_roc_42': {'inputs': ['bsd_007_interest_coverage_stress_252'], 'func': bsd_152_bsd_007_interest_coverage_stress_252_roc_42},
    'bsd_153_bsd_013_netinc_decline_1_roc_126': {'inputs': ['netinc'], 'func': bsd_153_bsd_013_netinc_decline_1_roc_126},
    'bsd_154_bsd_019_interest_coverage_stress_84_roc_378': {'inputs': ['bsd_019_interest_coverage_stress_84'], 'func': bsd_154_bsd_019_interest_coverage_stress_84_roc_378},
    'bsd_155_bsd_025_netinc_decline_1_roc_4': {'inputs': ['netinc'], 'func': bsd_155_bsd_025_netinc_decline_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def bsd_replacement_d2_001(bsd_replacement_001):
    feature = _clean(bsd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_001'] = {'inputs': ['bsd_replacement_001'], 'func': bsd_replacement_d2_001}


def bsd_replacement_d2_002(bsd_replacement_002):
    feature = _clean(bsd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_002'] = {'inputs': ['bsd_replacement_002'], 'func': bsd_replacement_d2_002}


def bsd_replacement_d2_003(bsd_replacement_003):
    feature = _clean(bsd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_003'] = {'inputs': ['bsd_replacement_003'], 'func': bsd_replacement_d2_003}


def bsd_replacement_d2_004(bsd_replacement_004):
    feature = _clean(bsd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_004'] = {'inputs': ['bsd_replacement_004'], 'func': bsd_replacement_d2_004}


def bsd_replacement_d2_005(bsd_replacement_005):
    feature = _clean(bsd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_005'] = {'inputs': ['bsd_replacement_005'], 'func': bsd_replacement_d2_005}


def bsd_replacement_d2_006(bsd_replacement_006):
    feature = _clean(bsd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_006'] = {'inputs': ['bsd_replacement_006'], 'func': bsd_replacement_d2_006}


def bsd_replacement_d2_007(bsd_replacement_007):
    feature = _clean(bsd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_007'] = {'inputs': ['bsd_replacement_007'], 'func': bsd_replacement_d2_007}


def bsd_replacement_d2_008(bsd_replacement_008):
    feature = _clean(bsd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_008'] = {'inputs': ['bsd_replacement_008'], 'func': bsd_replacement_d2_008}


def bsd_replacement_d2_009(bsd_replacement_009):
    feature = _clean(bsd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_009'] = {'inputs': ['bsd_replacement_009'], 'func': bsd_replacement_d2_009}


def bsd_replacement_d2_010(bsd_replacement_010):
    feature = _clean(bsd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_010'] = {'inputs': ['bsd_replacement_010'], 'func': bsd_replacement_d2_010}


def bsd_replacement_d2_011(bsd_replacement_011):
    feature = _clean(bsd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_011'] = {'inputs': ['bsd_replacement_011'], 'func': bsd_replacement_d2_011}


def bsd_replacement_d2_012(bsd_replacement_012):
    feature = _clean(bsd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_012'] = {'inputs': ['bsd_replacement_012'], 'func': bsd_replacement_d2_012}


def bsd_replacement_d2_013(bsd_replacement_013):
    feature = _clean(bsd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_013'] = {'inputs': ['bsd_replacement_013'], 'func': bsd_replacement_d2_013}


def bsd_replacement_d2_014(bsd_replacement_014):
    feature = _clean(bsd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_014'] = {'inputs': ['bsd_replacement_014'], 'func': bsd_replacement_d2_014}


def bsd_replacement_d2_015(bsd_replacement_015):
    feature = _clean(bsd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_015'] = {'inputs': ['bsd_replacement_015'], 'func': bsd_replacement_d2_015}


def bsd_replacement_d2_016(bsd_replacement_016):
    feature = _clean(bsd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_016'] = {'inputs': ['bsd_replacement_016'], 'func': bsd_replacement_d2_016}


def bsd_replacement_d2_017(bsd_replacement_017):
    feature = _clean(bsd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_017'] = {'inputs': ['bsd_replacement_017'], 'func': bsd_replacement_d2_017}


def bsd_replacement_d2_018(bsd_replacement_018):
    feature = _clean(bsd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_018'] = {'inputs': ['bsd_replacement_018'], 'func': bsd_replacement_d2_018}


def bsd_replacement_d2_019(bsd_replacement_019):
    feature = _clean(bsd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_019'] = {'inputs': ['bsd_replacement_019'], 'func': bsd_replacement_d2_019}


def bsd_replacement_d2_020(bsd_replacement_020):
    feature = _clean(bsd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_020'] = {'inputs': ['bsd_replacement_020'], 'func': bsd_replacement_d2_020}


def bsd_replacement_d2_021(bsd_replacement_021):
    feature = _clean(bsd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_021'] = {'inputs': ['bsd_replacement_021'], 'func': bsd_replacement_d2_021}


def bsd_replacement_d2_022(bsd_replacement_022):
    feature = _clean(bsd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_022'] = {'inputs': ['bsd_replacement_022'], 'func': bsd_replacement_d2_022}


def bsd_replacement_d2_023(bsd_replacement_023):
    feature = _clean(bsd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_023'] = {'inputs': ['bsd_replacement_023'], 'func': bsd_replacement_d2_023}


def bsd_replacement_d2_024(bsd_replacement_024):
    feature = _clean(bsd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_024'] = {'inputs': ['bsd_replacement_024'], 'func': bsd_replacement_d2_024}


def bsd_replacement_d2_025(bsd_replacement_025):
    feature = _clean(bsd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_025'] = {'inputs': ['bsd_replacement_025'], 'func': bsd_replacement_d2_025}


def bsd_replacement_d2_026(bsd_replacement_026):
    feature = _clean(bsd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_026'] = {'inputs': ['bsd_replacement_026'], 'func': bsd_replacement_d2_026}


def bsd_replacement_d2_027(bsd_replacement_027):
    feature = _clean(bsd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_027'] = {'inputs': ['bsd_replacement_027'], 'func': bsd_replacement_d2_027}


def bsd_replacement_d2_028(bsd_replacement_028):
    feature = _clean(bsd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_028'] = {'inputs': ['bsd_replacement_028'], 'func': bsd_replacement_d2_028}


def bsd_replacement_d2_029(bsd_replacement_029):
    feature = _clean(bsd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_029'] = {'inputs': ['bsd_replacement_029'], 'func': bsd_replacement_d2_029}


def bsd_replacement_d2_030(bsd_replacement_030):
    feature = _clean(bsd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_030'] = {'inputs': ['bsd_replacement_030'], 'func': bsd_replacement_d2_030}


def bsd_replacement_d2_031(bsd_replacement_031):
    feature = _clean(bsd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_031'] = {'inputs': ['bsd_replacement_031'], 'func': bsd_replacement_d2_031}


def bsd_replacement_d2_032(bsd_replacement_032):
    feature = _clean(bsd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_032'] = {'inputs': ['bsd_replacement_032'], 'func': bsd_replacement_d2_032}


def bsd_replacement_d2_033(bsd_replacement_033):
    feature = _clean(bsd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_033'] = {'inputs': ['bsd_replacement_033'], 'func': bsd_replacement_d2_033}


def bsd_replacement_d2_034(bsd_replacement_034):
    feature = _clean(bsd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_034'] = {'inputs': ['bsd_replacement_034'], 'func': bsd_replacement_d2_034}


def bsd_replacement_d2_035(bsd_replacement_035):
    feature = _clean(bsd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_035'] = {'inputs': ['bsd_replacement_035'], 'func': bsd_replacement_d2_035}


def bsd_replacement_d2_036(bsd_replacement_036):
    feature = _clean(bsd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_036'] = {'inputs': ['bsd_replacement_036'], 'func': bsd_replacement_d2_036}


def bsd_replacement_d2_037(bsd_replacement_037):
    feature = _clean(bsd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_037'] = {'inputs': ['bsd_replacement_037'], 'func': bsd_replacement_d2_037}


def bsd_replacement_d2_038(bsd_replacement_038):
    feature = _clean(bsd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_038'] = {'inputs': ['bsd_replacement_038'], 'func': bsd_replacement_d2_038}


def bsd_replacement_d2_039(bsd_replacement_039):
    feature = _clean(bsd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_039'] = {'inputs': ['bsd_replacement_039'], 'func': bsd_replacement_d2_039}


def bsd_replacement_d2_040(bsd_replacement_040):
    feature = _clean(bsd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_040'] = {'inputs': ['bsd_replacement_040'], 'func': bsd_replacement_d2_040}


def bsd_replacement_d2_041(bsd_replacement_041):
    feature = _clean(bsd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_041'] = {'inputs': ['bsd_replacement_041'], 'func': bsd_replacement_d2_041}


def bsd_replacement_d2_042(bsd_replacement_042):
    feature = _clean(bsd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_042'] = {'inputs': ['bsd_replacement_042'], 'func': bsd_replacement_d2_042}


def bsd_replacement_d2_043(bsd_replacement_043):
    feature = _clean(bsd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_043'] = {'inputs': ['bsd_replacement_043'], 'func': bsd_replacement_d2_043}


def bsd_replacement_d2_044(bsd_replacement_044):
    feature = _clean(bsd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_044'] = {'inputs': ['bsd_replacement_044'], 'func': bsd_replacement_d2_044}


def bsd_replacement_d2_045(bsd_replacement_045):
    feature = _clean(bsd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_045'] = {'inputs': ['bsd_replacement_045'], 'func': bsd_replacement_d2_045}


def bsd_replacement_d2_046(bsd_replacement_046):
    feature = _clean(bsd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_046'] = {'inputs': ['bsd_replacement_046'], 'func': bsd_replacement_d2_046}


def bsd_replacement_d2_047(bsd_replacement_047):
    feature = _clean(bsd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_047'] = {'inputs': ['bsd_replacement_047'], 'func': bsd_replacement_d2_047}


def bsd_replacement_d2_048(bsd_replacement_048):
    feature = _clean(bsd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_048'] = {'inputs': ['bsd_replacement_048'], 'func': bsd_replacement_d2_048}


def bsd_replacement_d2_049(bsd_replacement_049):
    feature = _clean(bsd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_049'] = {'inputs': ['bsd_replacement_049'], 'func': bsd_replacement_d2_049}


def bsd_replacement_d2_050(bsd_replacement_050):
    feature = _clean(bsd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_050'] = {'inputs': ['bsd_replacement_050'], 'func': bsd_replacement_d2_050}


def bsd_replacement_d2_051(bsd_replacement_051):
    feature = _clean(bsd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_051'] = {'inputs': ['bsd_replacement_051'], 'func': bsd_replacement_d2_051}


def bsd_replacement_d2_052(bsd_replacement_052):
    feature = _clean(bsd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_052'] = {'inputs': ['bsd_replacement_052'], 'func': bsd_replacement_d2_052}


def bsd_replacement_d2_053(bsd_replacement_053):
    feature = _clean(bsd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_053'] = {'inputs': ['bsd_replacement_053'], 'func': bsd_replacement_d2_053}


def bsd_replacement_d2_054(bsd_replacement_054):
    feature = _clean(bsd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_054'] = {'inputs': ['bsd_replacement_054'], 'func': bsd_replacement_d2_054}


def bsd_replacement_d2_055(bsd_replacement_055):
    feature = _clean(bsd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_055'] = {'inputs': ['bsd_replacement_055'], 'func': bsd_replacement_d2_055}


def bsd_replacement_d2_056(bsd_replacement_056):
    feature = _clean(bsd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_056'] = {'inputs': ['bsd_replacement_056'], 'func': bsd_replacement_d2_056}


def bsd_replacement_d2_057(bsd_replacement_057):
    feature = _clean(bsd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_057'] = {'inputs': ['bsd_replacement_057'], 'func': bsd_replacement_d2_057}


def bsd_replacement_d2_058(bsd_replacement_058):
    feature = _clean(bsd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_058'] = {'inputs': ['bsd_replacement_058'], 'func': bsd_replacement_d2_058}


def bsd_replacement_d2_059(bsd_replacement_059):
    feature = _clean(bsd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_059'] = {'inputs': ['bsd_replacement_059'], 'func': bsd_replacement_d2_059}


def bsd_replacement_d2_060(bsd_replacement_060):
    feature = _clean(bsd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_060'] = {'inputs': ['bsd_replacement_060'], 'func': bsd_replacement_d2_060}


def bsd_replacement_d2_061(bsd_replacement_061):
    feature = _clean(bsd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_061'] = {'inputs': ['bsd_replacement_061'], 'func': bsd_replacement_d2_061}


def bsd_replacement_d2_062(bsd_replacement_062):
    feature = _clean(bsd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_062'] = {'inputs': ['bsd_replacement_062'], 'func': bsd_replacement_d2_062}


def bsd_replacement_d2_063(bsd_replacement_063):
    feature = _clean(bsd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_063'] = {'inputs': ['bsd_replacement_063'], 'func': bsd_replacement_d2_063}


def bsd_replacement_d2_064(bsd_replacement_064):
    feature = _clean(bsd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_064'] = {'inputs': ['bsd_replacement_064'], 'func': bsd_replacement_d2_064}


def bsd_replacement_d2_065(bsd_replacement_065):
    feature = _clean(bsd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_065'] = {'inputs': ['bsd_replacement_065'], 'func': bsd_replacement_d2_065}


def bsd_replacement_d2_066(bsd_replacement_066):
    feature = _clean(bsd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_066'] = {'inputs': ['bsd_replacement_066'], 'func': bsd_replacement_d2_066}


def bsd_replacement_d2_067(bsd_replacement_067):
    feature = _clean(bsd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_067'] = {'inputs': ['bsd_replacement_067'], 'func': bsd_replacement_d2_067}


def bsd_replacement_d2_068(bsd_replacement_068):
    feature = _clean(bsd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_068'] = {'inputs': ['bsd_replacement_068'], 'func': bsd_replacement_d2_068}


def bsd_replacement_d2_069(bsd_replacement_069):
    feature = _clean(bsd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_069'] = {'inputs': ['bsd_replacement_069'], 'func': bsd_replacement_d2_069}


def bsd_replacement_d2_070(bsd_replacement_070):
    feature = _clean(bsd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_070'] = {'inputs': ['bsd_replacement_070'], 'func': bsd_replacement_d2_070}


def bsd_replacement_d2_071(bsd_replacement_071):
    feature = _clean(bsd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_071'] = {'inputs': ['bsd_replacement_071'], 'func': bsd_replacement_d2_071}


def bsd_replacement_d2_072(bsd_replacement_072):
    feature = _clean(bsd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_072'] = {'inputs': ['bsd_replacement_072'], 'func': bsd_replacement_d2_072}


def bsd_replacement_d2_073(bsd_replacement_073):
    feature = _clean(bsd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_073'] = {'inputs': ['bsd_replacement_073'], 'func': bsd_replacement_d2_073}


def bsd_replacement_d2_074(bsd_replacement_074):
    feature = _clean(bsd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_074'] = {'inputs': ['bsd_replacement_074'], 'func': bsd_replacement_d2_074}


def bsd_replacement_d2_075(bsd_replacement_075):
    feature = _clean(bsd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_075'] = {'inputs': ['bsd_replacement_075'], 'func': bsd_replacement_d2_075}


def bsd_replacement_d2_076(bsd_replacement_076):
    feature = _clean(bsd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_076'] = {'inputs': ['bsd_replacement_076'], 'func': bsd_replacement_d2_076}


def bsd_replacement_d2_077(bsd_replacement_077):
    feature = _clean(bsd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_077'] = {'inputs': ['bsd_replacement_077'], 'func': bsd_replacement_d2_077}


def bsd_replacement_d2_078(bsd_replacement_078):
    feature = _clean(bsd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_078'] = {'inputs': ['bsd_replacement_078'], 'func': bsd_replacement_d2_078}


def bsd_replacement_d2_079(bsd_replacement_079):
    feature = _clean(bsd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_079'] = {'inputs': ['bsd_replacement_079'], 'func': bsd_replacement_d2_079}


def bsd_replacement_d2_080(bsd_replacement_080):
    feature = _clean(bsd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_080'] = {'inputs': ['bsd_replacement_080'], 'func': bsd_replacement_d2_080}


def bsd_replacement_d2_081(bsd_replacement_081):
    feature = _clean(bsd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_081'] = {'inputs': ['bsd_replacement_081'], 'func': bsd_replacement_d2_081}


def bsd_replacement_d2_082(bsd_replacement_082):
    feature = _clean(bsd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_082'] = {'inputs': ['bsd_replacement_082'], 'func': bsd_replacement_d2_082}


def bsd_replacement_d2_083(bsd_replacement_083):
    feature = _clean(bsd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_083'] = {'inputs': ['bsd_replacement_083'], 'func': bsd_replacement_d2_083}


def bsd_replacement_d2_084(bsd_replacement_084):
    feature = _clean(bsd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_084'] = {'inputs': ['bsd_replacement_084'], 'func': bsd_replacement_d2_084}


def bsd_replacement_d2_085(bsd_replacement_085):
    feature = _clean(bsd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_085'] = {'inputs': ['bsd_replacement_085'], 'func': bsd_replacement_d2_085}


def bsd_replacement_d2_086(bsd_replacement_086):
    feature = _clean(bsd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_086'] = {'inputs': ['bsd_replacement_086'], 'func': bsd_replacement_d2_086}


def bsd_replacement_d2_087(bsd_replacement_087):
    feature = _clean(bsd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_087'] = {'inputs': ['bsd_replacement_087'], 'func': bsd_replacement_d2_087}


def bsd_replacement_d2_088(bsd_replacement_088):
    feature = _clean(bsd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_088'] = {'inputs': ['bsd_replacement_088'], 'func': bsd_replacement_d2_088}


def bsd_replacement_d2_089(bsd_replacement_089):
    feature = _clean(bsd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_089'] = {'inputs': ['bsd_replacement_089'], 'func': bsd_replacement_d2_089}


def bsd_replacement_d2_090(bsd_replacement_090):
    feature = _clean(bsd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_090'] = {'inputs': ['bsd_replacement_090'], 'func': bsd_replacement_d2_090}


def bsd_replacement_d2_091(bsd_replacement_091):
    feature = _clean(bsd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_091'] = {'inputs': ['bsd_replacement_091'], 'func': bsd_replacement_d2_091}


def bsd_replacement_d2_092(bsd_replacement_092):
    feature = _clean(bsd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_092'] = {'inputs': ['bsd_replacement_092'], 'func': bsd_replacement_d2_092}


def bsd_replacement_d2_093(bsd_replacement_093):
    feature = _clean(bsd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_093'] = {'inputs': ['bsd_replacement_093'], 'func': bsd_replacement_d2_093}


def bsd_replacement_d2_094(bsd_replacement_094):
    feature = _clean(bsd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_094'] = {'inputs': ['bsd_replacement_094'], 'func': bsd_replacement_d2_094}


def bsd_replacement_d2_095(bsd_replacement_095):
    feature = _clean(bsd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_095'] = {'inputs': ['bsd_replacement_095'], 'func': bsd_replacement_d2_095}


def bsd_replacement_d2_096(bsd_replacement_096):
    feature = _clean(bsd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_096'] = {'inputs': ['bsd_replacement_096'], 'func': bsd_replacement_d2_096}


def bsd_replacement_d2_097(bsd_replacement_097):
    feature = _clean(bsd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_097'] = {'inputs': ['bsd_replacement_097'], 'func': bsd_replacement_d2_097}


def bsd_replacement_d2_098(bsd_replacement_098):
    feature = _clean(bsd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_098'] = {'inputs': ['bsd_replacement_098'], 'func': bsd_replacement_d2_098}


def bsd_replacement_d2_099(bsd_replacement_099):
    feature = _clean(bsd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_099'] = {'inputs': ['bsd_replacement_099'], 'func': bsd_replacement_d2_099}


def bsd_replacement_d2_100(bsd_replacement_100):
    feature = _clean(bsd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_100'] = {'inputs': ['bsd_replacement_100'], 'func': bsd_replacement_d2_100}


def bsd_replacement_d2_101(bsd_replacement_101):
    feature = _clean(bsd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_101'] = {'inputs': ['bsd_replacement_101'], 'func': bsd_replacement_d2_101}


def bsd_replacement_d2_102(bsd_replacement_102):
    feature = _clean(bsd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_102'] = {'inputs': ['bsd_replacement_102'], 'func': bsd_replacement_d2_102}


def bsd_replacement_d2_103(bsd_replacement_103):
    feature = _clean(bsd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_103'] = {'inputs': ['bsd_replacement_103'], 'func': bsd_replacement_d2_103}


def bsd_replacement_d2_104(bsd_replacement_104):
    feature = _clean(bsd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_104'] = {'inputs': ['bsd_replacement_104'], 'func': bsd_replacement_d2_104}


def bsd_replacement_d2_105(bsd_replacement_105):
    feature = _clean(bsd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_105'] = {'inputs': ['bsd_replacement_105'], 'func': bsd_replacement_d2_105}


def bsd_replacement_d2_106(bsd_replacement_106):
    feature = _clean(bsd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_106'] = {'inputs': ['bsd_replacement_106'], 'func': bsd_replacement_d2_106}


def bsd_replacement_d2_107(bsd_replacement_107):
    feature = _clean(bsd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_107'] = {'inputs': ['bsd_replacement_107'], 'func': bsd_replacement_d2_107}


def bsd_replacement_d2_108(bsd_replacement_108):
    feature = _clean(bsd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_108'] = {'inputs': ['bsd_replacement_108'], 'func': bsd_replacement_d2_108}


def bsd_replacement_d2_109(bsd_replacement_109):
    feature = _clean(bsd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_109'] = {'inputs': ['bsd_replacement_109'], 'func': bsd_replacement_d2_109}


def bsd_replacement_d2_110(bsd_replacement_110):
    feature = _clean(bsd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_110'] = {'inputs': ['bsd_replacement_110'], 'func': bsd_replacement_d2_110}


def bsd_replacement_d2_111(bsd_replacement_111):
    feature = _clean(bsd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_111'] = {'inputs': ['bsd_replacement_111'], 'func': bsd_replacement_d2_111}


def bsd_replacement_d2_112(bsd_replacement_112):
    feature = _clean(bsd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_112'] = {'inputs': ['bsd_replacement_112'], 'func': bsd_replacement_d2_112}


def bsd_replacement_d2_113(bsd_replacement_113):
    feature = _clean(bsd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_113'] = {'inputs': ['bsd_replacement_113'], 'func': bsd_replacement_d2_113}


def bsd_replacement_d2_114(bsd_replacement_114):
    feature = _clean(bsd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_114'] = {'inputs': ['bsd_replacement_114'], 'func': bsd_replacement_d2_114}


def bsd_replacement_d2_115(bsd_replacement_115):
    feature = _clean(bsd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_115'] = {'inputs': ['bsd_replacement_115'], 'func': bsd_replacement_d2_115}


def bsd_replacement_d2_116(bsd_replacement_116):
    feature = _clean(bsd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_116'] = {'inputs': ['bsd_replacement_116'], 'func': bsd_replacement_d2_116}


def bsd_replacement_d2_117(bsd_replacement_117):
    feature = _clean(bsd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_117'] = {'inputs': ['bsd_replacement_117'], 'func': bsd_replacement_d2_117}


def bsd_replacement_d2_118(bsd_replacement_118):
    feature = _clean(bsd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_118'] = {'inputs': ['bsd_replacement_118'], 'func': bsd_replacement_d2_118}


def bsd_replacement_d2_119(bsd_replacement_119):
    feature = _clean(bsd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_119'] = {'inputs': ['bsd_replacement_119'], 'func': bsd_replacement_d2_119}


def bsd_replacement_d2_120(bsd_replacement_120):
    feature = _clean(bsd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_120'] = {'inputs': ['bsd_replacement_120'], 'func': bsd_replacement_d2_120}


def bsd_replacement_d2_121(bsd_replacement_121):
    feature = _clean(bsd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_121'] = {'inputs': ['bsd_replacement_121'], 'func': bsd_replacement_d2_121}


def bsd_replacement_d2_122(bsd_replacement_122):
    feature = _clean(bsd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_122'] = {'inputs': ['bsd_replacement_122'], 'func': bsd_replacement_d2_122}


def bsd_replacement_d2_123(bsd_replacement_123):
    feature = _clean(bsd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_123'] = {'inputs': ['bsd_replacement_123'], 'func': bsd_replacement_d2_123}


def bsd_replacement_d2_124(bsd_replacement_124):
    feature = _clean(bsd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_124'] = {'inputs': ['bsd_replacement_124'], 'func': bsd_replacement_d2_124}


def bsd_replacement_d2_125(bsd_replacement_125):
    feature = _clean(bsd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_125'] = {'inputs': ['bsd_replacement_125'], 'func': bsd_replacement_d2_125}


def bsd_replacement_d2_126(bsd_replacement_126):
    feature = _clean(bsd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_126'] = {'inputs': ['bsd_replacement_126'], 'func': bsd_replacement_d2_126}


def bsd_replacement_d2_127(bsd_replacement_127):
    feature = _clean(bsd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_127'] = {'inputs': ['bsd_replacement_127'], 'func': bsd_replacement_d2_127}


def bsd_replacement_d2_128(bsd_replacement_128):
    feature = _clean(bsd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_128'] = {'inputs': ['bsd_replacement_128'], 'func': bsd_replacement_d2_128}


def bsd_replacement_d2_129(bsd_replacement_129):
    feature = _clean(bsd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_129'] = {'inputs': ['bsd_replacement_129'], 'func': bsd_replacement_d2_129}


def bsd_replacement_d2_130(bsd_replacement_130):
    feature = _clean(bsd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_130'] = {'inputs': ['bsd_replacement_130'], 'func': bsd_replacement_d2_130}


def bsd_replacement_d2_131(bsd_replacement_131):
    feature = _clean(bsd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_131'] = {'inputs': ['bsd_replacement_131'], 'func': bsd_replacement_d2_131}


def bsd_replacement_d2_132(bsd_replacement_132):
    feature = _clean(bsd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_132'] = {'inputs': ['bsd_replacement_132'], 'func': bsd_replacement_d2_132}


def bsd_replacement_d2_133(bsd_replacement_133):
    feature = _clean(bsd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_133'] = {'inputs': ['bsd_replacement_133'], 'func': bsd_replacement_d2_133}


def bsd_replacement_d2_134(bsd_replacement_134):
    feature = _clean(bsd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_134'] = {'inputs': ['bsd_replacement_134'], 'func': bsd_replacement_d2_134}


def bsd_replacement_d2_135(bsd_replacement_135):
    feature = _clean(bsd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_135'] = {'inputs': ['bsd_replacement_135'], 'func': bsd_replacement_d2_135}


def bsd_replacement_d2_136(bsd_replacement_136):
    feature = _clean(bsd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_136'] = {'inputs': ['bsd_replacement_136'], 'func': bsd_replacement_d2_136}


def bsd_replacement_d2_137(bsd_replacement_137):
    feature = _clean(bsd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_137'] = {'inputs': ['bsd_replacement_137'], 'func': bsd_replacement_d2_137}


def bsd_replacement_d2_138(bsd_replacement_138):
    feature = _clean(bsd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_138'] = {'inputs': ['bsd_replacement_138'], 'func': bsd_replacement_d2_138}


def bsd_replacement_d2_139(bsd_replacement_139):
    feature = _clean(bsd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_139'] = {'inputs': ['bsd_replacement_139'], 'func': bsd_replacement_d2_139}


def bsd_replacement_d2_140(bsd_replacement_140):
    feature = _clean(bsd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_140'] = {'inputs': ['bsd_replacement_140'], 'func': bsd_replacement_d2_140}


def bsd_replacement_d2_141(bsd_replacement_141):
    feature = _clean(bsd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_141'] = {'inputs': ['bsd_replacement_141'], 'func': bsd_replacement_d2_141}


def bsd_replacement_d2_142(bsd_replacement_142):
    feature = _clean(bsd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_142'] = {'inputs': ['bsd_replacement_142'], 'func': bsd_replacement_d2_142}


def bsd_replacement_d2_143(bsd_replacement_143):
    feature = _clean(bsd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_143'] = {'inputs': ['bsd_replacement_143'], 'func': bsd_replacement_d2_143}


def bsd_replacement_d2_144(bsd_replacement_144):
    feature = _clean(bsd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_144'] = {'inputs': ['bsd_replacement_144'], 'func': bsd_replacement_d2_144}


def bsd_replacement_d2_145(bsd_replacement_145):
    feature = _clean(bsd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_145'] = {'inputs': ['bsd_replacement_145'], 'func': bsd_replacement_d2_145}


def bsd_replacement_d2_146(bsd_replacement_146):
    feature = _clean(bsd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_146'] = {'inputs': ['bsd_replacement_146'], 'func': bsd_replacement_d2_146}


def bsd_replacement_d2_147(bsd_replacement_147):
    feature = _clean(bsd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_147'] = {'inputs': ['bsd_replacement_147'], 'func': bsd_replacement_d2_147}


def bsd_replacement_d2_148(bsd_replacement_148):
    feature = _clean(bsd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_148'] = {'inputs': ['bsd_replacement_148'], 'func': bsd_replacement_d2_148}


def bsd_replacement_d2_149(bsd_replacement_149):
    feature = _clean(bsd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_149'] = {'inputs': ['bsd_replacement_149'], 'func': bsd_replacement_d2_149}


def bsd_replacement_d2_150(bsd_replacement_150):
    feature = _clean(bsd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_150'] = {'inputs': ['bsd_replacement_150'], 'func': bsd_replacement_d2_150}


def bsd_replacement_d2_151(bsd_replacement_151):
    feature = _clean(bsd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_151'] = {'inputs': ['bsd_replacement_151'], 'func': bsd_replacement_d2_151}


def bsd_replacement_d2_152(bsd_replacement_152):
    feature = _clean(bsd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_152'] = {'inputs': ['bsd_replacement_152'], 'func': bsd_replacement_d2_152}


def bsd_replacement_d2_153(bsd_replacement_153):
    feature = _clean(bsd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_153'] = {'inputs': ['bsd_replacement_153'], 'func': bsd_replacement_d2_153}


def bsd_replacement_d2_154(bsd_replacement_154):
    feature = _clean(bsd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_154'] = {'inputs': ['bsd_replacement_154'], 'func': bsd_replacement_d2_154}


def bsd_replacement_d2_155(bsd_replacement_155):
    feature = _clean(bsd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_155'] = {'inputs': ['bsd_replacement_155'], 'func': bsd_replacement_d2_155}


def bsd_replacement_d2_156(bsd_replacement_156):
    feature = _clean(bsd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_156'] = {'inputs': ['bsd_replacement_156'], 'func': bsd_replacement_d2_156}


def bsd_replacement_d2_157(bsd_replacement_157):
    feature = _clean(bsd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_157'] = {'inputs': ['bsd_replacement_157'], 'func': bsd_replacement_d2_157}


def bsd_replacement_d2_158(bsd_replacement_158):
    feature = _clean(bsd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_158'] = {'inputs': ['bsd_replacement_158'], 'func': bsd_replacement_d2_158}


def bsd_replacement_d2_159(bsd_replacement_159):
    feature = _clean(bsd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_159'] = {'inputs': ['bsd_replacement_159'], 'func': bsd_replacement_d2_159}


def bsd_replacement_d2_160(bsd_replacement_160):
    feature = _clean(bsd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_160'] = {'inputs': ['bsd_replacement_160'], 'func': bsd_replacement_d2_160}


def bsd_replacement_d2_161(bsd_replacement_161):
    feature = _clean(bsd_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_161'] = {'inputs': ['bsd_replacement_161'], 'func': bsd_replacement_d2_161}


def bsd_replacement_d2_162(bsd_replacement_162):
    feature = _clean(bsd_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_162'] = {'inputs': ['bsd_replacement_162'], 'func': bsd_replacement_d2_162}


def bsd_replacement_d2_163(bsd_replacement_163):
    feature = _clean(bsd_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_163'] = {'inputs': ['bsd_replacement_163'], 'func': bsd_replacement_d2_163}


def bsd_replacement_d2_164(bsd_replacement_164):
    feature = _clean(bsd_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_164'] = {'inputs': ['bsd_replacement_164'], 'func': bsd_replacement_d2_164}


def bsd_replacement_d2_165(bsd_replacement_165):
    feature = _clean(bsd_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_165'] = {'inputs': ['bsd_replacement_165'], 'func': bsd_replacement_d2_165}


def bsd_replacement_d2_166(bsd_replacement_166):
    feature = _clean(bsd_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
BSD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['bsd_replacement_d2_166'] = {'inputs': ['bsd_replacement_166'], 'func': bsd_replacement_d2_166}


# Base-universe derivative extensions for repaired first-base features.
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def bsd_base_universe_d2_001_bsd_003_fcf_burn_to_cash_63(bsd_003_fcf_burn_to_cash_63):
    return _base_universe_d2(bsd_003_fcf_burn_to_cash_63, 1)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_001_bsd_003_fcf_burn_to_cash_63'] = {'inputs': ['bsd_003_fcf_burn_to_cash_63'], 'func': bsd_base_universe_d2_001_bsd_003_fcf_burn_to_cash_63}


def bsd_base_universe_d2_002_bsd_004_debt_to_equity_84(bsd_004_debt_to_equity_84):
    return _base_universe_d2(bsd_004_debt_to_equity_84, 2)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_002_bsd_004_debt_to_equity_84'] = {'inputs': ['bsd_004_debt_to_equity_84'], 'func': bsd_base_universe_d2_002_bsd_004_debt_to_equity_84}


def bsd_base_universe_d2_003_bsd_005_debt_to_assets_126(bsd_005_debt_to_assets_126):
    return _base_universe_d2(bsd_005_debt_to_assets_126, 3)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_003_bsd_005_debt_to_assets_126'] = {'inputs': ['bsd_005_debt_to_assets_126'], 'func': bsd_base_universe_d2_003_bsd_005_debt_to_assets_126}


def bsd_base_universe_d2_004_bsd_012_accrual_gap_1260(bsd_012_accrual_gap_1260):
    return _base_universe_d2(bsd_012_accrual_gap_1260, 4)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_004_bsd_012_accrual_gap_1260'] = {'inputs': ['bsd_012_accrual_gap_1260'], 'func': bsd_base_universe_d2_004_bsd_012_accrual_gap_1260}


def bsd_base_universe_d2_005_bsd_016_debt_to_equity_21(bsd_016_debt_to_equity_21):
    return _base_universe_d2(bsd_016_debt_to_equity_21, 5)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_005_bsd_016_debt_to_equity_21'] = {'inputs': ['bsd_016_debt_to_equity_21'], 'func': bsd_base_universe_d2_005_bsd_016_debt_to_equity_21}


def bsd_base_universe_d2_006_bsd_017_debt_to_assets_42(bsd_017_debt_to_assets_42):
    return _base_universe_d2(bsd_017_debt_to_assets_42, 6)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_006_bsd_017_debt_to_assets_42'] = {'inputs': ['bsd_017_debt_to_assets_42'], 'func': bsd_base_universe_d2_006_bsd_017_debt_to_assets_42}


def bsd_base_universe_d2_007_bsd_024_accrual_gap_504(bsd_024_accrual_gap_504):
    return _base_universe_d2(bsd_024_accrual_gap_504, 7)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_007_bsd_024_accrual_gap_504'] = {'inputs': ['bsd_024_accrual_gap_504'], 'func': bsd_base_universe_d2_007_bsd_024_accrual_gap_504}


def bsd_base_universe_d2_008_bsd_027_fcf_burn_to_cash_1260(bsd_027_fcf_burn_to_cash_1260):
    return _base_universe_d2(bsd_027_fcf_burn_to_cash_1260, 8)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_008_bsd_027_fcf_burn_to_cash_1260'] = {'inputs': ['bsd_027_fcf_burn_to_cash_1260'], 'func': bsd_base_universe_d2_008_bsd_027_fcf_burn_to_cash_1260}


def bsd_base_universe_d2_009_bsd_028_debt_to_equity_1512(bsd_028_debt_to_equity_1512):
    return _base_universe_d2(bsd_028_debt_to_equity_1512, 9)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_009_bsd_028_debt_to_equity_1512'] = {'inputs': ['bsd_028_debt_to_equity_1512'], 'func': bsd_base_universe_d2_009_bsd_028_debt_to_equity_1512}


def bsd_base_universe_d2_010_bsd_029_debt_to_assets_63(bsd_029_debt_to_assets_63):
    return _base_universe_d2(bsd_029_debt_to_assets_63, 10)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_010_bsd_029_debt_to_assets_63'] = {'inputs': ['bsd_029_debt_to_assets_63'], 'func': bsd_base_universe_d2_010_bsd_029_debt_to_assets_63}


def bsd_base_universe_d2_011_bsd_031_interest_coverage_stress_21(bsd_031_interest_coverage_stress_21):
    return _base_universe_d2(bsd_031_interest_coverage_stress_21, 11)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_011_bsd_031_interest_coverage_stress_21'] = {'inputs': ['bsd_031_interest_coverage_stress_21'], 'func': bsd_base_universe_d2_011_bsd_031_interest_coverage_stress_21}


def bsd_base_universe_d2_012_bsd_036_accrual_gap_189(bsd_036_accrual_gap_189):
    return _base_universe_d2(bsd_036_accrual_gap_189, 12)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_012_bsd_036_accrual_gap_189'] = {'inputs': ['bsd_036_accrual_gap_189'], 'func': bsd_base_universe_d2_012_bsd_036_accrual_gap_189}


def bsd_base_universe_d2_013_bsd_039_fcf_burn_to_cash_504(bsd_039_fcf_burn_to_cash_504):
    return _base_universe_d2(bsd_039_fcf_burn_to_cash_504, 13)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_013_bsd_039_fcf_burn_to_cash_504'] = {'inputs': ['bsd_039_fcf_burn_to_cash_504'], 'func': bsd_base_universe_d2_013_bsd_039_fcf_burn_to_cash_504}


def bsd_base_universe_d2_014_bsd_040_debt_to_equity_756(bsd_040_debt_to_equity_756):
    return _base_universe_d2(bsd_040_debt_to_equity_756, 14)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_014_bsd_040_debt_to_equity_756'] = {'inputs': ['bsd_040_debt_to_equity_756'], 'func': bsd_base_universe_d2_014_bsd_040_debt_to_equity_756}


def bsd_base_universe_d2_015_bsd_041_debt_to_assets_1008(bsd_041_debt_to_assets_1008):
    return _base_universe_d2(bsd_041_debt_to_assets_1008, 15)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_015_bsd_041_debt_to_assets_1008'] = {'inputs': ['bsd_041_debt_to_assets_1008'], 'func': bsd_base_universe_d2_015_bsd_041_debt_to_assets_1008}


def bsd_base_universe_d2_016_bsd_043_interest_coverage_stress_1512(bsd_043_interest_coverage_stress_1512):
    return _base_universe_d2(bsd_043_interest_coverage_stress_1512, 16)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_016_bsd_043_interest_coverage_stress_1512'] = {'inputs': ['bsd_043_interest_coverage_stress_1512'], 'func': bsd_base_universe_d2_016_bsd_043_interest_coverage_stress_1512}


def bsd_base_universe_d2_017_bsd_048_accrual_gap_63(bsd_048_accrual_gap_63):
    return _base_universe_d2(bsd_048_accrual_gap_63, 17)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_017_bsd_048_accrual_gap_63'] = {'inputs': ['bsd_048_accrual_gap_63'], 'func': bsd_base_universe_d2_017_bsd_048_accrual_gap_63}


def bsd_base_universe_d2_018_bsd_051_fcf_burn_to_cash_189(bsd_051_fcf_burn_to_cash_189):
    return _base_universe_d2(bsd_051_fcf_burn_to_cash_189, 18)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_018_bsd_051_fcf_burn_to_cash_189'] = {'inputs': ['bsd_051_fcf_burn_to_cash_189'], 'func': bsd_base_universe_d2_018_bsd_051_fcf_burn_to_cash_189}


def bsd_base_universe_d2_019_bsd_052_debt_to_equity_252(bsd_052_debt_to_equity_252):
    return _base_universe_d2(bsd_052_debt_to_equity_252, 19)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_019_bsd_052_debt_to_equity_252'] = {'inputs': ['bsd_052_debt_to_equity_252'], 'func': bsd_base_universe_d2_019_bsd_052_debt_to_equity_252}


def bsd_base_universe_d2_020_bsd_053_debt_to_assets_378(bsd_053_debt_to_assets_378):
    return _base_universe_d2(bsd_053_debt_to_assets_378, 20)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_020_bsd_053_debt_to_assets_378'] = {'inputs': ['bsd_053_debt_to_assets_378'], 'func': bsd_base_universe_d2_020_bsd_053_debt_to_assets_378}


def bsd_base_universe_d2_021_bsd_055_interest_coverage_stress_756(bsd_055_interest_coverage_stress_756):
    return _base_universe_d2(bsd_055_interest_coverage_stress_756, 21)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_021_bsd_055_interest_coverage_stress_756'] = {'inputs': ['bsd_055_interest_coverage_stress_756'], 'func': bsd_base_universe_d2_021_bsd_055_interest_coverage_stress_756}


def bsd_base_universe_d2_022_bsd_060_accrual_gap_252(bsd_060_accrual_gap_252):
    return _base_universe_d2(bsd_060_accrual_gap_252, 22)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_022_bsd_060_accrual_gap_252'] = {'inputs': ['bsd_060_accrual_gap_252'], 'func': bsd_base_universe_d2_022_bsd_060_accrual_gap_252}


def bsd_base_universe_d2_023_bsd_basefill_001(bsd_basefill_001):
    return _base_universe_d2(bsd_basefill_001, 23)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_023_bsd_basefill_001'] = {'inputs': ['bsd_basefill_001'], 'func': bsd_base_universe_d2_023_bsd_basefill_001}


def bsd_base_universe_d2_024_bsd_basefill_002(bsd_basefill_002):
    return _base_universe_d2(bsd_basefill_002, 24)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_024_bsd_basefill_002'] = {'inputs': ['bsd_basefill_002'], 'func': bsd_base_universe_d2_024_bsd_basefill_002}


def bsd_base_universe_d2_025_bsd_basefill_006(bsd_basefill_006):
    return _base_universe_d2(bsd_basefill_006, 25)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_025_bsd_basefill_006'] = {'inputs': ['bsd_basefill_006'], 'func': bsd_base_universe_d2_025_bsd_basefill_006}


def bsd_base_universe_d2_026_bsd_basefill_008(bsd_basefill_008):
    return _base_universe_d2(bsd_basefill_008, 26)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_026_bsd_basefill_008'] = {'inputs': ['bsd_basefill_008'], 'func': bsd_base_universe_d2_026_bsd_basefill_008}


def bsd_base_universe_d2_027_bsd_basefill_009(bsd_basefill_009):
    return _base_universe_d2(bsd_basefill_009, 27)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_027_bsd_basefill_009'] = {'inputs': ['bsd_basefill_009'], 'func': bsd_base_universe_d2_027_bsd_basefill_009}


def bsd_base_universe_d2_028_bsd_basefill_010(bsd_basefill_010):
    return _base_universe_d2(bsd_basefill_010, 28)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_028_bsd_basefill_010'] = {'inputs': ['bsd_basefill_010'], 'func': bsd_base_universe_d2_028_bsd_basefill_010}


def bsd_base_universe_d2_029_bsd_basefill_011(bsd_basefill_011):
    return _base_universe_d2(bsd_basefill_011, 29)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_029_bsd_basefill_011'] = {'inputs': ['bsd_basefill_011'], 'func': bsd_base_universe_d2_029_bsd_basefill_011}


def bsd_base_universe_d2_030_bsd_basefill_013(bsd_basefill_013):
    return _base_universe_d2(bsd_basefill_013, 30)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_030_bsd_basefill_013'] = {'inputs': ['bsd_basefill_013'], 'func': bsd_base_universe_d2_030_bsd_basefill_013}


def bsd_base_universe_d2_031_bsd_basefill_014(bsd_basefill_014):
    return _base_universe_d2(bsd_basefill_014, 31)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_031_bsd_basefill_014'] = {'inputs': ['bsd_basefill_014'], 'func': bsd_base_universe_d2_031_bsd_basefill_014}


def bsd_base_universe_d2_032_bsd_basefill_015(bsd_basefill_015):
    return _base_universe_d2(bsd_basefill_015, 32)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_032_bsd_basefill_015'] = {'inputs': ['bsd_basefill_015'], 'func': bsd_base_universe_d2_032_bsd_basefill_015}


def bsd_base_universe_d2_033_bsd_basefill_018(bsd_basefill_018):
    return _base_universe_d2(bsd_basefill_018, 33)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_033_bsd_basefill_018'] = {'inputs': ['bsd_basefill_018'], 'func': bsd_base_universe_d2_033_bsd_basefill_018}


def bsd_base_universe_d2_034_bsd_basefill_020(bsd_basefill_020):
    return _base_universe_d2(bsd_basefill_020, 34)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_034_bsd_basefill_020'] = {'inputs': ['bsd_basefill_020'], 'func': bsd_base_universe_d2_034_bsd_basefill_020}


def bsd_base_universe_d2_035_bsd_basefill_021(bsd_basefill_021):
    return _base_universe_d2(bsd_basefill_021, 35)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_035_bsd_basefill_021'] = {'inputs': ['bsd_basefill_021'], 'func': bsd_base_universe_d2_035_bsd_basefill_021}


def bsd_base_universe_d2_036_bsd_basefill_022(bsd_basefill_022):
    return _base_universe_d2(bsd_basefill_022, 36)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_036_bsd_basefill_022'] = {'inputs': ['bsd_basefill_022'], 'func': bsd_base_universe_d2_036_bsd_basefill_022}


def bsd_base_universe_d2_037_bsd_basefill_023(bsd_basefill_023):
    return _base_universe_d2(bsd_basefill_023, 37)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_037_bsd_basefill_023'] = {'inputs': ['bsd_basefill_023'], 'func': bsd_base_universe_d2_037_bsd_basefill_023}


def bsd_base_universe_d2_038_bsd_basefill_025(bsd_basefill_025):
    return _base_universe_d2(bsd_basefill_025, 38)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_038_bsd_basefill_025'] = {'inputs': ['bsd_basefill_025'], 'func': bsd_base_universe_d2_038_bsd_basefill_025}


def bsd_base_universe_d2_039_bsd_basefill_026(bsd_basefill_026):
    return _base_universe_d2(bsd_basefill_026, 39)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_039_bsd_basefill_026'] = {'inputs': ['bsd_basefill_026'], 'func': bsd_base_universe_d2_039_bsd_basefill_026}


def bsd_base_universe_d2_040_bsd_basefill_030(bsd_basefill_030):
    return _base_universe_d2(bsd_basefill_030, 40)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_040_bsd_basefill_030'] = {'inputs': ['bsd_basefill_030'], 'func': bsd_base_universe_d2_040_bsd_basefill_030}


def bsd_base_universe_d2_041_bsd_basefill_032(bsd_basefill_032):
    return _base_universe_d2(bsd_basefill_032, 41)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_041_bsd_basefill_032'] = {'inputs': ['bsd_basefill_032'], 'func': bsd_base_universe_d2_041_bsd_basefill_032}


def bsd_base_universe_d2_042_bsd_basefill_033(bsd_basefill_033):
    return _base_universe_d2(bsd_basefill_033, 42)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_042_bsd_basefill_033'] = {'inputs': ['bsd_basefill_033'], 'func': bsd_base_universe_d2_042_bsd_basefill_033}


def bsd_base_universe_d2_043_bsd_basefill_034(bsd_basefill_034):
    return _base_universe_d2(bsd_basefill_034, 43)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_043_bsd_basefill_034'] = {'inputs': ['bsd_basefill_034'], 'func': bsd_base_universe_d2_043_bsd_basefill_034}


def bsd_base_universe_d2_044_bsd_basefill_035(bsd_basefill_035):
    return _base_universe_d2(bsd_basefill_035, 44)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_044_bsd_basefill_035'] = {'inputs': ['bsd_basefill_035'], 'func': bsd_base_universe_d2_044_bsd_basefill_035}


def bsd_base_universe_d2_045_bsd_basefill_037(bsd_basefill_037):
    return _base_universe_d2(bsd_basefill_037, 45)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_045_bsd_basefill_037'] = {'inputs': ['bsd_basefill_037'], 'func': bsd_base_universe_d2_045_bsd_basefill_037}


def bsd_base_universe_d2_046_bsd_basefill_038(bsd_basefill_038):
    return _base_universe_d2(bsd_basefill_038, 46)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_046_bsd_basefill_038'] = {'inputs': ['bsd_basefill_038'], 'func': bsd_base_universe_d2_046_bsd_basefill_038}


def bsd_base_universe_d2_047_bsd_basefill_042(bsd_basefill_042):
    return _base_universe_d2(bsd_basefill_042, 47)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_047_bsd_basefill_042'] = {'inputs': ['bsd_basefill_042'], 'func': bsd_base_universe_d2_047_bsd_basefill_042}


def bsd_base_universe_d2_048_bsd_basefill_044(bsd_basefill_044):
    return _base_universe_d2(bsd_basefill_044, 48)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_048_bsd_basefill_044'] = {'inputs': ['bsd_basefill_044'], 'func': bsd_base_universe_d2_048_bsd_basefill_044}


def bsd_base_universe_d2_049_bsd_basefill_045(bsd_basefill_045):
    return _base_universe_d2(bsd_basefill_045, 49)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_049_bsd_basefill_045'] = {'inputs': ['bsd_basefill_045'], 'func': bsd_base_universe_d2_049_bsd_basefill_045}


def bsd_base_universe_d2_050_bsd_basefill_046(bsd_basefill_046):
    return _base_universe_d2(bsd_basefill_046, 50)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_050_bsd_basefill_046'] = {'inputs': ['bsd_basefill_046'], 'func': bsd_base_universe_d2_050_bsd_basefill_046}


def bsd_base_universe_d2_051_bsd_basefill_047(bsd_basefill_047):
    return _base_universe_d2(bsd_basefill_047, 51)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_051_bsd_basefill_047'] = {'inputs': ['bsd_basefill_047'], 'func': bsd_base_universe_d2_051_bsd_basefill_047}


def bsd_base_universe_d2_052_bsd_basefill_049(bsd_basefill_049):
    return _base_universe_d2(bsd_basefill_049, 52)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_052_bsd_basefill_049'] = {'inputs': ['bsd_basefill_049'], 'func': bsd_base_universe_d2_052_bsd_basefill_049}


def bsd_base_universe_d2_053_bsd_basefill_050(bsd_basefill_050):
    return _base_universe_d2(bsd_basefill_050, 53)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_053_bsd_basefill_050'] = {'inputs': ['bsd_basefill_050'], 'func': bsd_base_universe_d2_053_bsd_basefill_050}


def bsd_base_universe_d2_054_bsd_basefill_054(bsd_basefill_054):
    return _base_universe_d2(bsd_basefill_054, 54)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_054_bsd_basefill_054'] = {'inputs': ['bsd_basefill_054'], 'func': bsd_base_universe_d2_054_bsd_basefill_054}


def bsd_base_universe_d2_055_bsd_basefill_056(bsd_basefill_056):
    return _base_universe_d2(bsd_basefill_056, 55)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_055_bsd_basefill_056'] = {'inputs': ['bsd_basefill_056'], 'func': bsd_base_universe_d2_055_bsd_basefill_056}


def bsd_base_universe_d2_056_bsd_basefill_057(bsd_basefill_057):
    return _base_universe_d2(bsd_basefill_057, 56)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_056_bsd_basefill_057'] = {'inputs': ['bsd_basefill_057'], 'func': bsd_base_universe_d2_056_bsd_basefill_057}


def bsd_base_universe_d2_057_bsd_basefill_058(bsd_basefill_058):
    return _base_universe_d2(bsd_basefill_058, 57)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_057_bsd_basefill_058'] = {'inputs': ['bsd_basefill_058'], 'func': bsd_base_universe_d2_057_bsd_basefill_058}


def bsd_base_universe_d2_058_bsd_basefill_059(bsd_basefill_059):
    return _base_universe_d2(bsd_basefill_059, 58)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_058_bsd_basefill_059'] = {'inputs': ['bsd_basefill_059'], 'func': bsd_base_universe_d2_058_bsd_basefill_059}


def bsd_base_universe_d2_059_bsd_basefill_061(bsd_basefill_061):
    return _base_universe_d2(bsd_basefill_061, 59)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_059_bsd_basefill_061'] = {'inputs': ['bsd_basefill_061'], 'func': bsd_base_universe_d2_059_bsd_basefill_061}


def bsd_base_universe_d2_060_bsd_basefill_062(bsd_basefill_062):
    return _base_universe_d2(bsd_basefill_062, 60)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_060_bsd_basefill_062'] = {'inputs': ['bsd_basefill_062'], 'func': bsd_base_universe_d2_060_bsd_basefill_062}


def bsd_base_universe_d2_061_bsd_basefill_063(bsd_basefill_063):
    return _base_universe_d2(bsd_basefill_063, 61)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_061_bsd_basefill_063'] = {'inputs': ['bsd_basefill_063'], 'func': bsd_base_universe_d2_061_bsd_basefill_063}


def bsd_base_universe_d2_062_bsd_basefill_064(bsd_basefill_064):
    return _base_universe_d2(bsd_basefill_064, 62)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_062_bsd_basefill_064'] = {'inputs': ['bsd_basefill_064'], 'func': bsd_base_universe_d2_062_bsd_basefill_064}


def bsd_base_universe_d2_063_bsd_basefill_065(bsd_basefill_065):
    return _base_universe_d2(bsd_basefill_065, 63)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_063_bsd_basefill_065'] = {'inputs': ['bsd_basefill_065'], 'func': bsd_base_universe_d2_063_bsd_basefill_065}


def bsd_base_universe_d2_064_bsd_basefill_066(bsd_basefill_066):
    return _base_universe_d2(bsd_basefill_066, 64)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_064_bsd_basefill_066'] = {'inputs': ['bsd_basefill_066'], 'func': bsd_base_universe_d2_064_bsd_basefill_066}


def bsd_base_universe_d2_065_bsd_basefill_067(bsd_basefill_067):
    return _base_universe_d2(bsd_basefill_067, 65)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_065_bsd_basefill_067'] = {'inputs': ['bsd_basefill_067'], 'func': bsd_base_universe_d2_065_bsd_basefill_067}


def bsd_base_universe_d2_066_bsd_basefill_068(bsd_basefill_068):
    return _base_universe_d2(bsd_basefill_068, 66)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_066_bsd_basefill_068'] = {'inputs': ['bsd_basefill_068'], 'func': bsd_base_universe_d2_066_bsd_basefill_068}


def bsd_base_universe_d2_067_bsd_basefill_069(bsd_basefill_069):
    return _base_universe_d2(bsd_basefill_069, 67)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_067_bsd_basefill_069'] = {'inputs': ['bsd_basefill_069'], 'func': bsd_base_universe_d2_067_bsd_basefill_069}


def bsd_base_universe_d2_068_bsd_basefill_070(bsd_basefill_070):
    return _base_universe_d2(bsd_basefill_070, 68)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_068_bsd_basefill_070'] = {'inputs': ['bsd_basefill_070'], 'func': bsd_base_universe_d2_068_bsd_basefill_070}


def bsd_base_universe_d2_069_bsd_basefill_071(bsd_basefill_071):
    return _base_universe_d2(bsd_basefill_071, 69)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_069_bsd_basefill_071'] = {'inputs': ['bsd_basefill_071'], 'func': bsd_base_universe_d2_069_bsd_basefill_071}


def bsd_base_universe_d2_070_bsd_basefill_072(bsd_basefill_072):
    return _base_universe_d2(bsd_basefill_072, 70)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_070_bsd_basefill_072'] = {'inputs': ['bsd_basefill_072'], 'func': bsd_base_universe_d2_070_bsd_basefill_072}


def bsd_base_universe_d2_071_bsd_basefill_073(bsd_basefill_073):
    return _base_universe_d2(bsd_basefill_073, 71)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_071_bsd_basefill_073'] = {'inputs': ['bsd_basefill_073'], 'func': bsd_base_universe_d2_071_bsd_basefill_073}


def bsd_base_universe_d2_072_bsd_basefill_074(bsd_basefill_074):
    return _base_universe_d2(bsd_basefill_074, 72)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_072_bsd_basefill_074'] = {'inputs': ['bsd_basefill_074'], 'func': bsd_base_universe_d2_072_bsd_basefill_074}


def bsd_base_universe_d2_073_bsd_basefill_075(bsd_basefill_075):
    return _base_universe_d2(bsd_basefill_075, 73)
BSD_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['bsd_base_universe_d2_073_bsd_basefill_075'] = {'inputs': ['bsd_basefill_075'], 'func': bsd_base_universe_d2_073_bsd_basefill_075}
