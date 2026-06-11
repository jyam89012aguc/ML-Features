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



def iex_151_iex_001_holder_exit_1_roc_1(iex_001_holder_exit_1):
    feature = _s(iex_001_holder_exit_1)
    return (_roc(feature, 1)).reindex(feature.index)

def iex_152_iex_007_holder_exit_1_roc_42(iex_007_holder_exit_1):
    feature = _s(iex_007_holder_exit_1)
    return (_roc(feature, 42)).reindex(feature.index)

def iex_153_iex_013_holder_exit_1_roc_126(iex_013_holder_exit_1):
    feature = _s(iex_013_holder_exit_1)
    return (_roc(feature, 126)).reindex(feature.index)

def iex_154_iex_019_holder_exit_1_roc_378(iex_019_holder_exit_1):
    feature = _s(iex_019_holder_exit_1)
    return (_roc(feature, 378)).reindex(feature.index)

def iex_155_iex_025_holder_exit_1_roc_4(iex_025_holder_exit_1):
    feature = _s(iex_025_holder_exit_1)
    return (_roc(feature, 4)).reindex(feature.index)






















INSTITUTIONAL_EXIT_REGISTRY_2ND_DERIVATIVES = {
    'iex_151_iex_001_holder_exit_1_roc_1': {'inputs': ['iex_001_holder_exit_1'], 'func': iex_151_iex_001_holder_exit_1_roc_1},
    'iex_152_iex_007_holder_exit_1_roc_42': {'inputs': ['iex_007_holder_exit_1'], 'func': iex_152_iex_007_holder_exit_1_roc_42},
    'iex_153_iex_013_holder_exit_1_roc_126': {'inputs': ['iex_013_holder_exit_1'], 'func': iex_153_iex_013_holder_exit_1_roc_126},
    'iex_154_iex_019_holder_exit_1_roc_378': {'inputs': ['iex_019_holder_exit_1'], 'func': iex_154_iex_019_holder_exit_1_roc_378},
    'iex_155_iex_025_holder_exit_1_roc_4': {'inputs': ['iex_025_holder_exit_1'], 'func': iex_155_iex_025_holder_exit_1_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ie_replacement_d2_001(iex_001_holder_exit_1):
    feature = _clean(iex_001_holder_exit_1)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_001'] = {'inputs': ['iex_001_holder_exit_1'], 'func': ie_replacement_d2_001}


def ie_replacement_d2_002(iex_007_holder_exit_1):
    feature = _clean(iex_007_holder_exit_1)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_002'] = {'inputs': ['iex_007_holder_exit_1'], 'func': ie_replacement_d2_002}


def ie_replacement_d2_003(iex_013_holder_exit_1):
    feature = _clean(iex_013_holder_exit_1)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_003'] = {'inputs': ['iex_013_holder_exit_1'], 'func': ie_replacement_d2_003}


def ie_replacement_d2_004(iex_019_holder_exit_1):
    feature = _clean(iex_019_holder_exit_1)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_004'] = {'inputs': ['iex_019_holder_exit_1'], 'func': ie_replacement_d2_004}


def ie_replacement_d2_005(iex_025_holder_exit_1):
    feature = _clean(iex_025_holder_exit_1)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_005'] = {'inputs': ['iex_025_holder_exit_1'], 'func': ie_replacement_d2_005}


def ie_replacement_d2_006(ie_replacement_001):
    feature = _clean(ie_replacement_001)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_006'] = {'inputs': ['ie_replacement_001'], 'func': ie_replacement_d2_006}


def ie_replacement_d2_007(ie_replacement_002):
    feature = _clean(ie_replacement_002)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_007'] = {'inputs': ['ie_replacement_002'], 'func': ie_replacement_d2_007}


def ie_replacement_d2_008(ie_replacement_003):
    feature = _clean(ie_replacement_003)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_008'] = {'inputs': ['ie_replacement_003'], 'func': ie_replacement_d2_008}


def ie_replacement_d2_009(ie_replacement_004):
    feature = _clean(ie_replacement_004)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_009'] = {'inputs': ['ie_replacement_004'], 'func': ie_replacement_d2_009}


def ie_replacement_d2_010(ie_replacement_005):
    feature = _clean(ie_replacement_005)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_010'] = {'inputs': ['ie_replacement_005'], 'func': ie_replacement_d2_010}


def ie_replacement_d2_011(ie_replacement_006):
    feature = _clean(ie_replacement_006)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_011'] = {'inputs': ['ie_replacement_006'], 'func': ie_replacement_d2_011}


def ie_replacement_d2_012(ie_replacement_007):
    feature = _clean(ie_replacement_007)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_012'] = {'inputs': ['ie_replacement_007'], 'func': ie_replacement_d2_012}


def ie_replacement_d2_013(ie_replacement_008):
    feature = _clean(ie_replacement_008)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_013'] = {'inputs': ['ie_replacement_008'], 'func': ie_replacement_d2_013}


def ie_replacement_d2_014(ie_replacement_009):
    feature = _clean(ie_replacement_009)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_014'] = {'inputs': ['ie_replacement_009'], 'func': ie_replacement_d2_014}


def ie_replacement_d2_015(ie_replacement_010):
    feature = _clean(ie_replacement_010)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_015'] = {'inputs': ['ie_replacement_010'], 'func': ie_replacement_d2_015}


def ie_replacement_d2_016(ie_replacement_011):
    feature = _clean(ie_replacement_011)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_016'] = {'inputs': ['ie_replacement_011'], 'func': ie_replacement_d2_016}


def ie_replacement_d2_017(ie_replacement_012):
    feature = _clean(ie_replacement_012)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_017'] = {'inputs': ['ie_replacement_012'], 'func': ie_replacement_d2_017}


def ie_replacement_d2_018(ie_replacement_013):
    feature = _clean(ie_replacement_013)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_018'] = {'inputs': ['ie_replacement_013'], 'func': ie_replacement_d2_018}


def ie_replacement_d2_019(ie_replacement_014):
    feature = _clean(ie_replacement_014)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_019'] = {'inputs': ['ie_replacement_014'], 'func': ie_replacement_d2_019}


def ie_replacement_d2_020(ie_replacement_015):
    feature = _clean(ie_replacement_015)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_020'] = {'inputs': ['ie_replacement_015'], 'func': ie_replacement_d2_020}


def ie_replacement_d2_021(ie_replacement_016):
    feature = _clean(ie_replacement_016)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_021'] = {'inputs': ['ie_replacement_016'], 'func': ie_replacement_d2_021}


def ie_replacement_d2_022(ie_replacement_017):
    feature = _clean(ie_replacement_017)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_022'] = {'inputs': ['ie_replacement_017'], 'func': ie_replacement_d2_022}


def ie_replacement_d2_023(ie_replacement_018):
    feature = _clean(ie_replacement_018)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_023'] = {'inputs': ['ie_replacement_018'], 'func': ie_replacement_d2_023}


def ie_replacement_d2_024(ie_replacement_019):
    feature = _clean(ie_replacement_019)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_024'] = {'inputs': ['ie_replacement_019'], 'func': ie_replacement_d2_024}


def ie_replacement_d2_025(ie_replacement_020):
    feature = _clean(ie_replacement_020)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_025'] = {'inputs': ['ie_replacement_020'], 'func': ie_replacement_d2_025}


def ie_replacement_d2_026(ie_replacement_021):
    feature = _clean(ie_replacement_021)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_026'] = {'inputs': ['ie_replacement_021'], 'func': ie_replacement_d2_026}


def ie_replacement_d2_027(ie_replacement_022):
    feature = _clean(ie_replacement_022)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_027'] = {'inputs': ['ie_replacement_022'], 'func': ie_replacement_d2_027}


def ie_replacement_d2_028(ie_replacement_023):
    feature = _clean(ie_replacement_023)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_028'] = {'inputs': ['ie_replacement_023'], 'func': ie_replacement_d2_028}


def ie_replacement_d2_029(ie_replacement_024):
    feature = _clean(ie_replacement_024)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_029'] = {'inputs': ['ie_replacement_024'], 'func': ie_replacement_d2_029}


def ie_replacement_d2_030(ie_replacement_025):
    feature = _clean(ie_replacement_025)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_030'] = {'inputs': ['ie_replacement_025'], 'func': ie_replacement_d2_030}


def ie_replacement_d2_031(ie_replacement_026):
    feature = _clean(ie_replacement_026)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_031'] = {'inputs': ['ie_replacement_026'], 'func': ie_replacement_d2_031}


def ie_replacement_d2_032(ie_replacement_027):
    feature = _clean(ie_replacement_027)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_032'] = {'inputs': ['ie_replacement_027'], 'func': ie_replacement_d2_032}


def ie_replacement_d2_033(ie_replacement_028):
    feature = _clean(ie_replacement_028)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_033'] = {'inputs': ['ie_replacement_028'], 'func': ie_replacement_d2_033}


def ie_replacement_d2_034(ie_replacement_029):
    feature = _clean(ie_replacement_029)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_034'] = {'inputs': ['ie_replacement_029'], 'func': ie_replacement_d2_034}


def ie_replacement_d2_035(ie_replacement_030):
    feature = _clean(ie_replacement_030)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_035'] = {'inputs': ['ie_replacement_030'], 'func': ie_replacement_d2_035}


def ie_replacement_d2_036(ie_replacement_031):
    feature = _clean(ie_replacement_031)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_036'] = {'inputs': ['ie_replacement_031'], 'func': ie_replacement_d2_036}


def ie_replacement_d2_037(ie_replacement_032):
    feature = _clean(ie_replacement_032)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_037'] = {'inputs': ['ie_replacement_032'], 'func': ie_replacement_d2_037}


def ie_replacement_d2_038(ie_replacement_033):
    feature = _clean(ie_replacement_033)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_038'] = {'inputs': ['ie_replacement_033'], 'func': ie_replacement_d2_038}


def ie_replacement_d2_039(ie_replacement_034):
    feature = _clean(ie_replacement_034)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_039'] = {'inputs': ['ie_replacement_034'], 'func': ie_replacement_d2_039}


def ie_replacement_d2_040(ie_replacement_035):
    feature = _clean(ie_replacement_035)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_040'] = {'inputs': ['ie_replacement_035'], 'func': ie_replacement_d2_040}


def ie_replacement_d2_041(ie_replacement_036):
    feature = _clean(ie_replacement_036)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_041'] = {'inputs': ['ie_replacement_036'], 'func': ie_replacement_d2_041}


def ie_replacement_d2_042(ie_replacement_037):
    feature = _clean(ie_replacement_037)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_042'] = {'inputs': ['ie_replacement_037'], 'func': ie_replacement_d2_042}


def ie_replacement_d2_043(ie_replacement_038):
    feature = _clean(ie_replacement_038)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_043'] = {'inputs': ['ie_replacement_038'], 'func': ie_replacement_d2_043}


def ie_replacement_d2_044(ie_replacement_039):
    feature = _clean(ie_replacement_039)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_044'] = {'inputs': ['ie_replacement_039'], 'func': ie_replacement_d2_044}


def ie_replacement_d2_045(ie_replacement_040):
    feature = _clean(ie_replacement_040)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_045'] = {'inputs': ['ie_replacement_040'], 'func': ie_replacement_d2_045}


def ie_replacement_d2_046(ie_replacement_041):
    feature = _clean(ie_replacement_041)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_046'] = {'inputs': ['ie_replacement_041'], 'func': ie_replacement_d2_046}


def ie_replacement_d2_047(ie_replacement_042):
    feature = _clean(ie_replacement_042)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_047'] = {'inputs': ['ie_replacement_042'], 'func': ie_replacement_d2_047}


def ie_replacement_d2_048(ie_replacement_043):
    feature = _clean(ie_replacement_043)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_048'] = {'inputs': ['ie_replacement_043'], 'func': ie_replacement_d2_048}


def ie_replacement_d2_049(ie_replacement_044):
    feature = _clean(ie_replacement_044)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_049'] = {'inputs': ['ie_replacement_044'], 'func': ie_replacement_d2_049}


def ie_replacement_d2_050(ie_replacement_045):
    feature = _clean(ie_replacement_045)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_050'] = {'inputs': ['ie_replacement_045'], 'func': ie_replacement_d2_050}


def ie_replacement_d2_051(ie_replacement_046):
    feature = _clean(ie_replacement_046)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_051'] = {'inputs': ['ie_replacement_046'], 'func': ie_replacement_d2_051}


def ie_replacement_d2_052(ie_replacement_047):
    feature = _clean(ie_replacement_047)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_052'] = {'inputs': ['ie_replacement_047'], 'func': ie_replacement_d2_052}


def ie_replacement_d2_053(ie_replacement_048):
    feature = _clean(ie_replacement_048)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_053'] = {'inputs': ['ie_replacement_048'], 'func': ie_replacement_d2_053}


def ie_replacement_d2_054(ie_replacement_049):
    feature = _clean(ie_replacement_049)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_054'] = {'inputs': ['ie_replacement_049'], 'func': ie_replacement_d2_054}


def ie_replacement_d2_055(ie_replacement_050):
    feature = _clean(ie_replacement_050)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_055'] = {'inputs': ['ie_replacement_050'], 'func': ie_replacement_d2_055}


def ie_replacement_d2_056(ie_replacement_051):
    feature = _clean(ie_replacement_051)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_056'] = {'inputs': ['ie_replacement_051'], 'func': ie_replacement_d2_056}


def ie_replacement_d2_057(ie_replacement_052):
    feature = _clean(ie_replacement_052)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_057'] = {'inputs': ['ie_replacement_052'], 'func': ie_replacement_d2_057}


def ie_replacement_d2_058(ie_replacement_053):
    feature = _clean(ie_replacement_053)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_058'] = {'inputs': ['ie_replacement_053'], 'func': ie_replacement_d2_058}


def ie_replacement_d2_059(ie_replacement_054):
    feature = _clean(ie_replacement_054)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_059'] = {'inputs': ['ie_replacement_054'], 'func': ie_replacement_d2_059}


def ie_replacement_d2_060(ie_replacement_055):
    feature = _clean(ie_replacement_055)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_060'] = {'inputs': ['ie_replacement_055'], 'func': ie_replacement_d2_060}


def ie_replacement_d2_061(ie_replacement_056):
    feature = _clean(ie_replacement_056)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_061'] = {'inputs': ['ie_replacement_056'], 'func': ie_replacement_d2_061}


def ie_replacement_d2_062(ie_replacement_057):
    feature = _clean(ie_replacement_057)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_062'] = {'inputs': ['ie_replacement_057'], 'func': ie_replacement_d2_062}


def ie_replacement_d2_063(ie_replacement_058):
    feature = _clean(ie_replacement_058)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_063'] = {'inputs': ['ie_replacement_058'], 'func': ie_replacement_d2_063}


def ie_replacement_d2_064(ie_replacement_059):
    feature = _clean(ie_replacement_059)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_064'] = {'inputs': ['ie_replacement_059'], 'func': ie_replacement_d2_064}


def ie_replacement_d2_065(ie_replacement_060):
    feature = _clean(ie_replacement_060)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_065'] = {'inputs': ['ie_replacement_060'], 'func': ie_replacement_d2_065}


def ie_replacement_d2_066(ie_replacement_061):
    feature = _clean(ie_replacement_061)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_066'] = {'inputs': ['ie_replacement_061'], 'func': ie_replacement_d2_066}


def ie_replacement_d2_067(ie_replacement_062):
    feature = _clean(ie_replacement_062)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_067'] = {'inputs': ['ie_replacement_062'], 'func': ie_replacement_d2_067}


def ie_replacement_d2_068(ie_replacement_063):
    feature = _clean(ie_replacement_063)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_068'] = {'inputs': ['ie_replacement_063'], 'func': ie_replacement_d2_068}


def ie_replacement_d2_069(ie_replacement_064):
    feature = _clean(ie_replacement_064)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_069'] = {'inputs': ['ie_replacement_064'], 'func': ie_replacement_d2_069}


def ie_replacement_d2_070(ie_replacement_065):
    feature = _clean(ie_replacement_065)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_070'] = {'inputs': ['ie_replacement_065'], 'func': ie_replacement_d2_070}


def ie_replacement_d2_071(ie_replacement_066):
    feature = _clean(ie_replacement_066)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_071'] = {'inputs': ['ie_replacement_066'], 'func': ie_replacement_d2_071}


def ie_replacement_d2_072(ie_replacement_067):
    feature = _clean(ie_replacement_067)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_072'] = {'inputs': ['ie_replacement_067'], 'func': ie_replacement_d2_072}


def ie_replacement_d2_073(ie_replacement_068):
    feature = _clean(ie_replacement_068)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_073'] = {'inputs': ['ie_replacement_068'], 'func': ie_replacement_d2_073}


def ie_replacement_d2_074(ie_replacement_069):
    feature = _clean(ie_replacement_069)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_074'] = {'inputs': ['ie_replacement_069'], 'func': ie_replacement_d2_074}


def ie_replacement_d2_075(ie_replacement_070):
    feature = _clean(ie_replacement_070)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_075'] = {'inputs': ['ie_replacement_070'], 'func': ie_replacement_d2_075}


def ie_replacement_d2_076(ie_replacement_071):
    feature = _clean(ie_replacement_071)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_076'] = {'inputs': ['ie_replacement_071'], 'func': ie_replacement_d2_076}


def ie_replacement_d2_077(ie_replacement_072):
    feature = _clean(ie_replacement_072)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_077'] = {'inputs': ['ie_replacement_072'], 'func': ie_replacement_d2_077}


def ie_replacement_d2_078(ie_replacement_073):
    feature = _clean(ie_replacement_073)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_078'] = {'inputs': ['ie_replacement_073'], 'func': ie_replacement_d2_078}


def ie_replacement_d2_079(ie_replacement_074):
    feature = _clean(ie_replacement_074)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_079'] = {'inputs': ['ie_replacement_074'], 'func': ie_replacement_d2_079}


def ie_replacement_d2_080(ie_replacement_075):
    feature = _clean(ie_replacement_075)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_080'] = {'inputs': ['ie_replacement_075'], 'func': ie_replacement_d2_080}


def ie_replacement_d2_081(ie_replacement_076):
    feature = _clean(ie_replacement_076)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_081'] = {'inputs': ['ie_replacement_076'], 'func': ie_replacement_d2_081}


def ie_replacement_d2_082(ie_replacement_077):
    feature = _clean(ie_replacement_077)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_082'] = {'inputs': ['ie_replacement_077'], 'func': ie_replacement_d2_082}


def ie_replacement_d2_083(ie_replacement_078):
    feature = _clean(ie_replacement_078)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_083'] = {'inputs': ['ie_replacement_078'], 'func': ie_replacement_d2_083}


def ie_replacement_d2_084(ie_replacement_079):
    feature = _clean(ie_replacement_079)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_084'] = {'inputs': ['ie_replacement_079'], 'func': ie_replacement_d2_084}


def ie_replacement_d2_085(ie_replacement_080):
    feature = _clean(ie_replacement_080)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_085'] = {'inputs': ['ie_replacement_080'], 'func': ie_replacement_d2_085}


def ie_replacement_d2_086(ie_replacement_081):
    feature = _clean(ie_replacement_081)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_086'] = {'inputs': ['ie_replacement_081'], 'func': ie_replacement_d2_086}


def ie_replacement_d2_087(ie_replacement_082):
    feature = _clean(ie_replacement_082)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_087'] = {'inputs': ['ie_replacement_082'], 'func': ie_replacement_d2_087}


def ie_replacement_d2_088(ie_replacement_083):
    feature = _clean(ie_replacement_083)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_088'] = {'inputs': ['ie_replacement_083'], 'func': ie_replacement_d2_088}


def ie_replacement_d2_089(ie_replacement_084):
    feature = _clean(ie_replacement_084)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_089'] = {'inputs': ['ie_replacement_084'], 'func': ie_replacement_d2_089}


def ie_replacement_d2_090(ie_replacement_085):
    feature = _clean(ie_replacement_085)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_090'] = {'inputs': ['ie_replacement_085'], 'func': ie_replacement_d2_090}


def ie_replacement_d2_091(ie_replacement_086):
    feature = _clean(ie_replacement_086)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_091'] = {'inputs': ['ie_replacement_086'], 'func': ie_replacement_d2_091}


def ie_replacement_d2_092(ie_replacement_087):
    feature = _clean(ie_replacement_087)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_092'] = {'inputs': ['ie_replacement_087'], 'func': ie_replacement_d2_092}


def ie_replacement_d2_093(ie_replacement_088):
    feature = _clean(ie_replacement_088)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_093'] = {'inputs': ['ie_replacement_088'], 'func': ie_replacement_d2_093}


def ie_replacement_d2_094(ie_replacement_089):
    feature = _clean(ie_replacement_089)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_094'] = {'inputs': ['ie_replacement_089'], 'func': ie_replacement_d2_094}


def ie_replacement_d2_095(ie_replacement_090):
    feature = _clean(ie_replacement_090)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_095'] = {'inputs': ['ie_replacement_090'], 'func': ie_replacement_d2_095}


def ie_replacement_d2_096(ie_replacement_091):
    feature = _clean(ie_replacement_091)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_096'] = {'inputs': ['ie_replacement_091'], 'func': ie_replacement_d2_096}


def ie_replacement_d2_097(ie_replacement_092):
    feature = _clean(ie_replacement_092)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_097'] = {'inputs': ['ie_replacement_092'], 'func': ie_replacement_d2_097}


def ie_replacement_d2_098(ie_replacement_093):
    feature = _clean(ie_replacement_093)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_098'] = {'inputs': ['ie_replacement_093'], 'func': ie_replacement_d2_098}


def ie_replacement_d2_099(ie_replacement_094):
    feature = _clean(ie_replacement_094)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_099'] = {'inputs': ['ie_replacement_094'], 'func': ie_replacement_d2_099}


def ie_replacement_d2_100(ie_replacement_095):
    feature = _clean(ie_replacement_095)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_100'] = {'inputs': ['ie_replacement_095'], 'func': ie_replacement_d2_100}


def ie_replacement_d2_101(ie_replacement_096):
    feature = _clean(ie_replacement_096)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_101'] = {'inputs': ['ie_replacement_096'], 'func': ie_replacement_d2_101}


def ie_replacement_d2_102(ie_replacement_097):
    feature = _clean(ie_replacement_097)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_102'] = {'inputs': ['ie_replacement_097'], 'func': ie_replacement_d2_102}


def ie_replacement_d2_103(ie_replacement_098):
    feature = _clean(ie_replacement_098)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_103'] = {'inputs': ['ie_replacement_098'], 'func': ie_replacement_d2_103}


def ie_replacement_d2_104(ie_replacement_099):
    feature = _clean(ie_replacement_099)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_104'] = {'inputs': ['ie_replacement_099'], 'func': ie_replacement_d2_104}


def ie_replacement_d2_105(ie_replacement_100):
    feature = _clean(ie_replacement_100)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_105'] = {'inputs': ['ie_replacement_100'], 'func': ie_replacement_d2_105}


def ie_replacement_d2_106(ie_replacement_101):
    feature = _clean(ie_replacement_101)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_106'] = {'inputs': ['ie_replacement_101'], 'func': ie_replacement_d2_106}


def ie_replacement_d2_107(ie_replacement_102):
    feature = _clean(ie_replacement_102)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_107'] = {'inputs': ['ie_replacement_102'], 'func': ie_replacement_d2_107}


def ie_replacement_d2_108(ie_replacement_103):
    feature = _clean(ie_replacement_103)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_108'] = {'inputs': ['ie_replacement_103'], 'func': ie_replacement_d2_108}


def ie_replacement_d2_109(ie_replacement_104):
    feature = _clean(ie_replacement_104)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_109'] = {'inputs': ['ie_replacement_104'], 'func': ie_replacement_d2_109}


def ie_replacement_d2_110(ie_replacement_105):
    feature = _clean(ie_replacement_105)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_110'] = {'inputs': ['ie_replacement_105'], 'func': ie_replacement_d2_110}


def ie_replacement_d2_111(ie_replacement_106):
    feature = _clean(ie_replacement_106)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_111'] = {'inputs': ['ie_replacement_106'], 'func': ie_replacement_d2_111}


def ie_replacement_d2_112(ie_replacement_107):
    feature = _clean(ie_replacement_107)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_112'] = {'inputs': ['ie_replacement_107'], 'func': ie_replacement_d2_112}


def ie_replacement_d2_113(ie_replacement_108):
    feature = _clean(ie_replacement_108)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_113'] = {'inputs': ['ie_replacement_108'], 'func': ie_replacement_d2_113}


def ie_replacement_d2_114(ie_replacement_109):
    feature = _clean(ie_replacement_109)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_114'] = {'inputs': ['ie_replacement_109'], 'func': ie_replacement_d2_114}


def ie_replacement_d2_115(ie_replacement_110):
    feature = _clean(ie_replacement_110)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_115'] = {'inputs': ['ie_replacement_110'], 'func': ie_replacement_d2_115}


def ie_replacement_d2_116(ie_replacement_111):
    feature = _clean(ie_replacement_111)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_116'] = {'inputs': ['ie_replacement_111'], 'func': ie_replacement_d2_116}


def ie_replacement_d2_117(ie_replacement_112):
    feature = _clean(ie_replacement_112)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_117'] = {'inputs': ['ie_replacement_112'], 'func': ie_replacement_d2_117}


def ie_replacement_d2_118(ie_replacement_113):
    feature = _clean(ie_replacement_113)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_118'] = {'inputs': ['ie_replacement_113'], 'func': ie_replacement_d2_118}


def ie_replacement_d2_119(ie_replacement_114):
    feature = _clean(ie_replacement_114)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_119'] = {'inputs': ['ie_replacement_114'], 'func': ie_replacement_d2_119}


def ie_replacement_d2_120(ie_replacement_115):
    feature = _clean(ie_replacement_115)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_120'] = {'inputs': ['ie_replacement_115'], 'func': ie_replacement_d2_120}


def ie_replacement_d2_121(ie_replacement_116):
    feature = _clean(ie_replacement_116)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_121'] = {'inputs': ['ie_replacement_116'], 'func': ie_replacement_d2_121}


def ie_replacement_d2_122(ie_replacement_117):
    feature = _clean(ie_replacement_117)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_122'] = {'inputs': ['ie_replacement_117'], 'func': ie_replacement_d2_122}


def ie_replacement_d2_123(ie_replacement_118):
    feature = _clean(ie_replacement_118)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_123'] = {'inputs': ['ie_replacement_118'], 'func': ie_replacement_d2_123}


def ie_replacement_d2_124(ie_replacement_119):
    feature = _clean(ie_replacement_119)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_124'] = {'inputs': ['ie_replacement_119'], 'func': ie_replacement_d2_124}


def ie_replacement_d2_125(ie_replacement_120):
    feature = _clean(ie_replacement_120)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_125'] = {'inputs': ['ie_replacement_120'], 'func': ie_replacement_d2_125}


def ie_replacement_d2_126(ie_replacement_121):
    feature = _clean(ie_replacement_121)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_126'] = {'inputs': ['ie_replacement_121'], 'func': ie_replacement_d2_126}


def ie_replacement_d2_127(ie_replacement_122):
    feature = _clean(ie_replacement_122)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_127'] = {'inputs': ['ie_replacement_122'], 'func': ie_replacement_d2_127}


def ie_replacement_d2_128(ie_replacement_123):
    feature = _clean(ie_replacement_123)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_128'] = {'inputs': ['ie_replacement_123'], 'func': ie_replacement_d2_128}


def ie_replacement_d2_129(ie_replacement_124):
    feature = _clean(ie_replacement_124)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_129'] = {'inputs': ['ie_replacement_124'], 'func': ie_replacement_d2_129}


def ie_replacement_d2_130(ie_replacement_125):
    feature = _clean(ie_replacement_125)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_130'] = {'inputs': ['ie_replacement_125'], 'func': ie_replacement_d2_130}


def ie_replacement_d2_131(ie_replacement_126):
    feature = _clean(ie_replacement_126)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_131'] = {'inputs': ['ie_replacement_126'], 'func': ie_replacement_d2_131}


def ie_replacement_d2_132(ie_replacement_127):
    feature = _clean(ie_replacement_127)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_132'] = {'inputs': ['ie_replacement_127'], 'func': ie_replacement_d2_132}


def ie_replacement_d2_133(ie_replacement_128):
    feature = _clean(ie_replacement_128)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_133'] = {'inputs': ['ie_replacement_128'], 'func': ie_replacement_d2_133}


def ie_replacement_d2_134(ie_replacement_129):
    feature = _clean(ie_replacement_129)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_134'] = {'inputs': ['ie_replacement_129'], 'func': ie_replacement_d2_134}


def ie_replacement_d2_135(ie_replacement_130):
    feature = _clean(ie_replacement_130)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_135'] = {'inputs': ['ie_replacement_130'], 'func': ie_replacement_d2_135}


def ie_replacement_d2_136(ie_replacement_131):
    feature = _clean(ie_replacement_131)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_136'] = {'inputs': ['ie_replacement_131'], 'func': ie_replacement_d2_136}


def ie_replacement_d2_137(ie_replacement_132):
    feature = _clean(ie_replacement_132)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_137'] = {'inputs': ['ie_replacement_132'], 'func': ie_replacement_d2_137}


def ie_replacement_d2_138(ie_replacement_133):
    feature = _clean(ie_replacement_133)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_138'] = {'inputs': ['ie_replacement_133'], 'func': ie_replacement_d2_138}


def ie_replacement_d2_139(ie_replacement_134):
    feature = _clean(ie_replacement_134)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_139'] = {'inputs': ['ie_replacement_134'], 'func': ie_replacement_d2_139}


def ie_replacement_d2_140(ie_replacement_135):
    feature = _clean(ie_replacement_135)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_140'] = {'inputs': ['ie_replacement_135'], 'func': ie_replacement_d2_140}


def ie_replacement_d2_141(ie_replacement_136):
    feature = _clean(ie_replacement_136)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_141'] = {'inputs': ['ie_replacement_136'], 'func': ie_replacement_d2_141}


def ie_replacement_d2_142(ie_replacement_137):
    feature = _clean(ie_replacement_137)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_142'] = {'inputs': ['ie_replacement_137'], 'func': ie_replacement_d2_142}


def ie_replacement_d2_143(ie_replacement_138):
    feature = _clean(ie_replacement_138)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_143'] = {'inputs': ['ie_replacement_138'], 'func': ie_replacement_d2_143}


def ie_replacement_d2_144(ie_replacement_139):
    feature = _clean(ie_replacement_139)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_144'] = {'inputs': ['ie_replacement_139'], 'func': ie_replacement_d2_144}


def ie_replacement_d2_145(ie_replacement_140):
    feature = _clean(ie_replacement_140)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_145'] = {'inputs': ['ie_replacement_140'], 'func': ie_replacement_d2_145}


def ie_replacement_d2_146(ie_replacement_141):
    feature = _clean(ie_replacement_141)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_146'] = {'inputs': ['ie_replacement_141'], 'func': ie_replacement_d2_146}


def ie_replacement_d2_147(ie_replacement_142):
    feature = _clean(ie_replacement_142)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_147'] = {'inputs': ['ie_replacement_142'], 'func': ie_replacement_d2_147}


def ie_replacement_d2_148(ie_replacement_143):
    feature = _clean(ie_replacement_143)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_148'] = {'inputs': ['ie_replacement_143'], 'func': ie_replacement_d2_148}


def ie_replacement_d2_149(ie_replacement_144):
    feature = _clean(ie_replacement_144)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_149'] = {'inputs': ['ie_replacement_144'], 'func': ie_replacement_d2_149}


def ie_replacement_d2_150(ie_replacement_145):
    feature = _clean(ie_replacement_145)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_150'] = {'inputs': ['ie_replacement_145'], 'func': ie_replacement_d2_150}


def ie_replacement_d2_151(ie_replacement_146):
    feature = _clean(ie_replacement_146)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_151'] = {'inputs': ['ie_replacement_146'], 'func': ie_replacement_d2_151}


def ie_replacement_d2_152(ie_replacement_147):
    feature = _clean(ie_replacement_147)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_152'] = {'inputs': ['ie_replacement_147'], 'func': ie_replacement_d2_152}


def ie_replacement_d2_153(ie_replacement_148):
    feature = _clean(ie_replacement_148)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_153'] = {'inputs': ['ie_replacement_148'], 'func': ie_replacement_d2_153}


def ie_replacement_d2_154(ie_replacement_149):
    feature = _clean(ie_replacement_149)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_154'] = {'inputs': ['ie_replacement_149'], 'func': ie_replacement_d2_154}


def ie_replacement_d2_155(ie_replacement_150):
    feature = _clean(ie_replacement_150)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_155'] = {'inputs': ['ie_replacement_150'], 'func': ie_replacement_d2_155}


def ie_replacement_d2_156(ie_replacement_151):
    feature = _clean(ie_replacement_151)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_156'] = {'inputs': ['ie_replacement_151'], 'func': ie_replacement_d2_156}


def ie_replacement_d2_157(ie_replacement_152):
    feature = _clean(ie_replacement_152)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_157'] = {'inputs': ['ie_replacement_152'], 'func': ie_replacement_d2_157}


def ie_replacement_d2_158(ie_replacement_153):
    feature = _clean(ie_replacement_153)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_158'] = {'inputs': ['ie_replacement_153'], 'func': ie_replacement_d2_158}


def ie_replacement_d2_159(ie_replacement_154):
    feature = _clean(ie_replacement_154)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_159'] = {'inputs': ['ie_replacement_154'], 'func': ie_replacement_d2_159}


def ie_replacement_d2_160(ie_replacement_155):
    feature = _clean(ie_replacement_155)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_160'] = {'inputs': ['ie_replacement_155'], 'func': ie_replacement_d2_160}


def ie_replacement_d2_161(ie_replacement_156):
    feature = _clean(ie_replacement_156)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_161'] = {'inputs': ['ie_replacement_156'], 'func': ie_replacement_d2_161}


def ie_replacement_d2_162(ie_replacement_157):
    feature = _clean(ie_replacement_157)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_162'] = {'inputs': ['ie_replacement_157'], 'func': ie_replacement_d2_162}


def ie_replacement_d2_163(ie_replacement_158):
    feature = _clean(ie_replacement_158)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_163'] = {'inputs': ['ie_replacement_158'], 'func': ie_replacement_d2_163}


def ie_replacement_d2_164(ie_replacement_159):
    feature = _clean(ie_replacement_159)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_164'] = {'inputs': ['ie_replacement_159'], 'func': ie_replacement_d2_164}


def ie_replacement_d2_165(ie_replacement_160):
    feature = _clean(ie_replacement_160)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_165'] = {'inputs': ['ie_replacement_160'], 'func': ie_replacement_d2_165}


def ie_replacement_d2_166(ie_replacement_161):
    feature = _clean(ie_replacement_161)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_166'] = {'inputs': ['ie_replacement_161'], 'func': ie_replacement_d2_166}


def ie_replacement_d2_167(ie_replacement_162):
    feature = _clean(ie_replacement_162)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_167'] = {'inputs': ['ie_replacement_162'], 'func': ie_replacement_d2_167}


def ie_replacement_d2_168(ie_replacement_163):
    feature = _clean(ie_replacement_163)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_168'] = {'inputs': ['ie_replacement_163'], 'func': ie_replacement_d2_168}


def ie_replacement_d2_169(ie_replacement_164):
    feature = _clean(ie_replacement_164)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_169'] = {'inputs': ['ie_replacement_164'], 'func': ie_replacement_d2_169}


def ie_replacement_d2_170(ie_replacement_165):
    feature = _clean(ie_replacement_165)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
IE_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ie_replacement_d2_170'] = {'inputs': ['ie_replacement_165'], 'func': ie_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def iex_base_universe_d2_001_iex_003_top_holder_concentration_63(iex_003_top_holder_concentration_63):
    return _base_universe_d2(iex_003_top_holder_concentration_63, 1)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_001_iex_003_top_holder_concentration_63'] = {'inputs': ['iex_003_top_holder_concentration_63'], 'func': iex_base_universe_d2_001_iex_003_top_holder_concentration_63}


def iex_base_universe_d2_002_iex_004_institutional_net_flow_84(iex_004_institutional_net_flow_84):
    return _base_universe_d2(iex_004_institutional_net_flow_84, 2)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_002_iex_004_institutional_net_flow_84'] = {'inputs': ['iex_004_institutional_net_flow_84'], 'func': iex_base_universe_d2_002_iex_004_institutional_net_flow_84}


def iex_base_universe_d2_003_iex_005_forced_selling_pressure_126(iex_005_forced_selling_pressure_126):
    return _base_universe_d2(iex_005_forced_selling_pressure_126, 3)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_003_iex_005_forced_selling_pressure_126'] = {'inputs': ['iex_005_forced_selling_pressure_126'], 'func': iex_base_universe_d2_003_iex_005_forced_selling_pressure_126}


def iex_base_universe_d2_004_iex_006_holder_base_volatility_189(iex_006_holder_base_volatility_189):
    return _base_universe_d2(iex_006_holder_base_volatility_189, 4)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_004_iex_006_holder_base_volatility_189'] = {'inputs': ['iex_006_holder_base_volatility_189'], 'func': iex_base_universe_d2_004_iex_006_holder_base_volatility_189}


def iex_base_universe_d2_005_iex_009_top_holder_concentration_504(iex_009_top_holder_concentration_504):
    return _base_universe_d2(iex_009_top_holder_concentration_504, 5)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_005_iex_009_top_holder_concentration_504'] = {'inputs': ['iex_009_top_holder_concentration_504'], 'func': iex_base_universe_d2_005_iex_009_top_holder_concentration_504}


def iex_base_universe_d2_006_iex_010_institutional_net_flow_756(iex_010_institutional_net_flow_756):
    return _base_universe_d2(iex_010_institutional_net_flow_756, 6)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_006_iex_010_institutional_net_flow_756'] = {'inputs': ['iex_010_institutional_net_flow_756'], 'func': iex_base_universe_d2_006_iex_010_institutional_net_flow_756}


def iex_base_universe_d2_007_iex_011_forced_selling_pressure_1008(iex_011_forced_selling_pressure_1008):
    return _base_universe_d2(iex_011_forced_selling_pressure_1008, 7)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_007_iex_011_forced_selling_pressure_1008'] = {'inputs': ['iex_011_forced_selling_pressure_1008'], 'func': iex_base_universe_d2_007_iex_011_forced_selling_pressure_1008}


def iex_base_universe_d2_008_iex_012_holder_base_volatility_1260(iex_012_holder_base_volatility_1260):
    return _base_universe_d2(iex_012_holder_base_volatility_1260, 8)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_008_iex_012_holder_base_volatility_1260'] = {'inputs': ['iex_012_holder_base_volatility_1260'], 'func': iex_base_universe_d2_008_iex_012_holder_base_volatility_1260}


def iex_base_universe_d2_009_iex_015_top_holder_concentration_252(iex_015_top_holder_concentration_252):
    return _base_universe_d2(iex_015_top_holder_concentration_252, 9)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_009_iex_015_top_holder_concentration_252'] = {'inputs': ['iex_015_top_holder_concentration_252'], 'func': iex_base_universe_d2_009_iex_015_top_holder_concentration_252}


def iex_base_universe_d2_010_iex_016_institutional_net_flow_21(iex_016_institutional_net_flow_21):
    return _base_universe_d2(iex_016_institutional_net_flow_21, 10)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_010_iex_016_institutional_net_flow_21'] = {'inputs': ['iex_016_institutional_net_flow_21'], 'func': iex_base_universe_d2_010_iex_016_institutional_net_flow_21}


def iex_base_universe_d2_011_iex_017_forced_selling_pressure_42(iex_017_forced_selling_pressure_42):
    return _base_universe_d2(iex_017_forced_selling_pressure_42, 11)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_011_iex_017_forced_selling_pressure_42'] = {'inputs': ['iex_017_forced_selling_pressure_42'], 'func': iex_base_universe_d2_011_iex_017_forced_selling_pressure_42}


def iex_base_universe_d2_012_iex_018_holder_base_volatility_63(iex_018_holder_base_volatility_63):
    return _base_universe_d2(iex_018_holder_base_volatility_63, 12)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_012_iex_018_holder_base_volatility_63'] = {'inputs': ['iex_018_holder_base_volatility_63'], 'func': iex_base_universe_d2_012_iex_018_holder_base_volatility_63}


def iex_base_universe_d2_013_iex_021_top_holder_concentration_189(iex_021_top_holder_concentration_189):
    return _base_universe_d2(iex_021_top_holder_concentration_189, 13)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_013_iex_021_top_holder_concentration_189'] = {'inputs': ['iex_021_top_holder_concentration_189'], 'func': iex_base_universe_d2_013_iex_021_top_holder_concentration_189}


def iex_base_universe_d2_014_iex_022_institutional_net_flow_252(iex_022_institutional_net_flow_252):
    return _base_universe_d2(iex_022_institutional_net_flow_252, 14)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_014_iex_022_institutional_net_flow_252'] = {'inputs': ['iex_022_institutional_net_flow_252'], 'func': iex_base_universe_d2_014_iex_022_institutional_net_flow_252}


def iex_base_universe_d2_015_iex_023_forced_selling_pressure_378(iex_023_forced_selling_pressure_378):
    return _base_universe_d2(iex_023_forced_selling_pressure_378, 15)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_015_iex_023_forced_selling_pressure_378'] = {'inputs': ['iex_023_forced_selling_pressure_378'], 'func': iex_base_universe_d2_015_iex_023_forced_selling_pressure_378}


def iex_base_universe_d2_016_iex_024_holder_base_volatility_504(iex_024_holder_base_volatility_504):
    return _base_universe_d2(iex_024_holder_base_volatility_504, 16)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_016_iex_024_holder_base_volatility_504'] = {'inputs': ['iex_024_holder_base_volatility_504'], 'func': iex_base_universe_d2_016_iex_024_holder_base_volatility_504}


def iex_base_universe_d2_017_iex_027_top_holder_concentration_1260(iex_027_top_holder_concentration_1260):
    return _base_universe_d2(iex_027_top_holder_concentration_1260, 17)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_017_iex_027_top_holder_concentration_1260'] = {'inputs': ['iex_027_top_holder_concentration_1260'], 'func': iex_base_universe_d2_017_iex_027_top_holder_concentration_1260}


def iex_base_universe_d2_018_iex_028_institutional_net_flow_1512(iex_028_institutional_net_flow_1512):
    return _base_universe_d2(iex_028_institutional_net_flow_1512, 18)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_018_iex_028_institutional_net_flow_1512'] = {'inputs': ['iex_028_institutional_net_flow_1512'], 'func': iex_base_universe_d2_018_iex_028_institutional_net_flow_1512}


def iex_base_universe_d2_019_iex_029_forced_selling_pressure_63(iex_029_forced_selling_pressure_63):
    return _base_universe_d2(iex_029_forced_selling_pressure_63, 19)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_019_iex_029_forced_selling_pressure_63'] = {'inputs': ['iex_029_forced_selling_pressure_63'], 'func': iex_base_universe_d2_019_iex_029_forced_selling_pressure_63}


def iex_base_universe_d2_020_iex_030_holder_base_volatility_252(iex_030_holder_base_volatility_252):
    return _base_universe_d2(iex_030_holder_base_volatility_252, 20)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_020_iex_030_holder_base_volatility_252'] = {'inputs': ['iex_030_holder_base_volatility_252'], 'func': iex_base_universe_d2_020_iex_030_holder_base_volatility_252}


def iex_base_universe_d2_021_iex_basefill_001(iex_basefill_001):
    return _base_universe_d2(iex_basefill_001, 21)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_021_iex_basefill_001'] = {'inputs': ['iex_basefill_001'], 'func': iex_base_universe_d2_021_iex_basefill_001}


def iex_base_universe_d2_022_iex_basefill_002(iex_basefill_002):
    return _base_universe_d2(iex_basefill_002, 22)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_022_iex_basefill_002'] = {'inputs': ['iex_basefill_002'], 'func': iex_base_universe_d2_022_iex_basefill_002}


def iex_base_universe_d2_023_iex_basefill_007(iex_basefill_007):
    return _base_universe_d2(iex_basefill_007, 23)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_023_iex_basefill_007'] = {'inputs': ['iex_basefill_007'], 'func': iex_base_universe_d2_023_iex_basefill_007}


def iex_base_universe_d2_024_iex_basefill_008(iex_basefill_008):
    return _base_universe_d2(iex_basefill_008, 24)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_024_iex_basefill_008'] = {'inputs': ['iex_basefill_008'], 'func': iex_base_universe_d2_024_iex_basefill_008}


def iex_base_universe_d2_025_iex_basefill_013(iex_basefill_013):
    return _base_universe_d2(iex_basefill_013, 25)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_025_iex_basefill_013'] = {'inputs': ['iex_basefill_013'], 'func': iex_base_universe_d2_025_iex_basefill_013}


def iex_base_universe_d2_026_iex_basefill_014(iex_basefill_014):
    return _base_universe_d2(iex_basefill_014, 26)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_026_iex_basefill_014'] = {'inputs': ['iex_basefill_014'], 'func': iex_base_universe_d2_026_iex_basefill_014}


def iex_base_universe_d2_027_iex_basefill_019(iex_basefill_019):
    return _base_universe_d2(iex_basefill_019, 27)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_027_iex_basefill_019'] = {'inputs': ['iex_basefill_019'], 'func': iex_base_universe_d2_027_iex_basefill_019}


def iex_base_universe_d2_028_iex_basefill_020(iex_basefill_020):
    return _base_universe_d2(iex_basefill_020, 28)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_028_iex_basefill_020'] = {'inputs': ['iex_basefill_020'], 'func': iex_base_universe_d2_028_iex_basefill_020}


def iex_base_universe_d2_029_iex_basefill_025(iex_basefill_025):
    return _base_universe_d2(iex_basefill_025, 29)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_029_iex_basefill_025'] = {'inputs': ['iex_basefill_025'], 'func': iex_base_universe_d2_029_iex_basefill_025}


def iex_base_universe_d2_030_iex_basefill_026(iex_basefill_026):
    return _base_universe_d2(iex_basefill_026, 30)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_030_iex_basefill_026'] = {'inputs': ['iex_basefill_026'], 'func': iex_base_universe_d2_030_iex_basefill_026}


def iex_base_universe_d2_031_iex_basefill_031(iex_basefill_031):
    return _base_universe_d2(iex_basefill_031, 31)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_031_iex_basefill_031'] = {'inputs': ['iex_basefill_031'], 'func': iex_base_universe_d2_031_iex_basefill_031}


def iex_base_universe_d2_032_iex_basefill_032(iex_basefill_032):
    return _base_universe_d2(iex_basefill_032, 32)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_032_iex_basefill_032'] = {'inputs': ['iex_basefill_032'], 'func': iex_base_universe_d2_032_iex_basefill_032}


def iex_base_universe_d2_033_iex_basefill_033(iex_basefill_033):
    return _base_universe_d2(iex_basefill_033, 33)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_033_iex_basefill_033'] = {'inputs': ['iex_basefill_033'], 'func': iex_base_universe_d2_033_iex_basefill_033}


def iex_base_universe_d2_034_iex_basefill_034(iex_basefill_034):
    return _base_universe_d2(iex_basefill_034, 34)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_034_iex_basefill_034'] = {'inputs': ['iex_basefill_034'], 'func': iex_base_universe_d2_034_iex_basefill_034}


def iex_base_universe_d2_035_iex_basefill_035(iex_basefill_035):
    return _base_universe_d2(iex_basefill_035, 35)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_035_iex_basefill_035'] = {'inputs': ['iex_basefill_035'], 'func': iex_base_universe_d2_035_iex_basefill_035}


def iex_base_universe_d2_036_iex_basefill_036(iex_basefill_036):
    return _base_universe_d2(iex_basefill_036, 36)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_036_iex_basefill_036'] = {'inputs': ['iex_basefill_036'], 'func': iex_base_universe_d2_036_iex_basefill_036}


def iex_base_universe_d2_037_iex_basefill_037(iex_basefill_037):
    return _base_universe_d2(iex_basefill_037, 37)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_037_iex_basefill_037'] = {'inputs': ['iex_basefill_037'], 'func': iex_base_universe_d2_037_iex_basefill_037}


def iex_base_universe_d2_038_iex_basefill_038(iex_basefill_038):
    return _base_universe_d2(iex_basefill_038, 38)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_038_iex_basefill_038'] = {'inputs': ['iex_basefill_038'], 'func': iex_base_universe_d2_038_iex_basefill_038}


def iex_base_universe_d2_039_iex_basefill_039(iex_basefill_039):
    return _base_universe_d2(iex_basefill_039, 39)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_039_iex_basefill_039'] = {'inputs': ['iex_basefill_039'], 'func': iex_base_universe_d2_039_iex_basefill_039}


def iex_base_universe_d2_040_iex_basefill_040(iex_basefill_040):
    return _base_universe_d2(iex_basefill_040, 40)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_040_iex_basefill_040'] = {'inputs': ['iex_basefill_040'], 'func': iex_base_universe_d2_040_iex_basefill_040}


def iex_base_universe_d2_041_iex_basefill_041(iex_basefill_041):
    return _base_universe_d2(iex_basefill_041, 41)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_041_iex_basefill_041'] = {'inputs': ['iex_basefill_041'], 'func': iex_base_universe_d2_041_iex_basefill_041}


def iex_base_universe_d2_042_iex_basefill_042(iex_basefill_042):
    return _base_universe_d2(iex_basefill_042, 42)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_042_iex_basefill_042'] = {'inputs': ['iex_basefill_042'], 'func': iex_base_universe_d2_042_iex_basefill_042}


def iex_base_universe_d2_043_iex_basefill_043(iex_basefill_043):
    return _base_universe_d2(iex_basefill_043, 43)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_043_iex_basefill_043'] = {'inputs': ['iex_basefill_043'], 'func': iex_base_universe_d2_043_iex_basefill_043}


def iex_base_universe_d2_044_iex_basefill_044(iex_basefill_044):
    return _base_universe_d2(iex_basefill_044, 44)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_044_iex_basefill_044'] = {'inputs': ['iex_basefill_044'], 'func': iex_base_universe_d2_044_iex_basefill_044}


def iex_base_universe_d2_045_iex_basefill_045(iex_basefill_045):
    return _base_universe_d2(iex_basefill_045, 45)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_045_iex_basefill_045'] = {'inputs': ['iex_basefill_045'], 'func': iex_base_universe_d2_045_iex_basefill_045}


def iex_base_universe_d2_046_iex_basefill_046(iex_basefill_046):
    return _base_universe_d2(iex_basefill_046, 46)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_046_iex_basefill_046'] = {'inputs': ['iex_basefill_046'], 'func': iex_base_universe_d2_046_iex_basefill_046}


def iex_base_universe_d2_047_iex_basefill_047(iex_basefill_047):
    return _base_universe_d2(iex_basefill_047, 47)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_047_iex_basefill_047'] = {'inputs': ['iex_basefill_047'], 'func': iex_base_universe_d2_047_iex_basefill_047}


def iex_base_universe_d2_048_iex_basefill_048(iex_basefill_048):
    return _base_universe_d2(iex_basefill_048, 48)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_048_iex_basefill_048'] = {'inputs': ['iex_basefill_048'], 'func': iex_base_universe_d2_048_iex_basefill_048}


def iex_base_universe_d2_049_iex_basefill_049(iex_basefill_049):
    return _base_universe_d2(iex_basefill_049, 49)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_049_iex_basefill_049'] = {'inputs': ['iex_basefill_049'], 'func': iex_base_universe_d2_049_iex_basefill_049}


def iex_base_universe_d2_050_iex_basefill_050(iex_basefill_050):
    return _base_universe_d2(iex_basefill_050, 50)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_050_iex_basefill_050'] = {'inputs': ['iex_basefill_050'], 'func': iex_base_universe_d2_050_iex_basefill_050}


def iex_base_universe_d2_051_iex_basefill_051(iex_basefill_051):
    return _base_universe_d2(iex_basefill_051, 51)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_051_iex_basefill_051'] = {'inputs': ['iex_basefill_051'], 'func': iex_base_universe_d2_051_iex_basefill_051}


def iex_base_universe_d2_052_iex_basefill_052(iex_basefill_052):
    return _base_universe_d2(iex_basefill_052, 52)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_052_iex_basefill_052'] = {'inputs': ['iex_basefill_052'], 'func': iex_base_universe_d2_052_iex_basefill_052}


def iex_base_universe_d2_053_iex_basefill_053(iex_basefill_053):
    return _base_universe_d2(iex_basefill_053, 53)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_053_iex_basefill_053'] = {'inputs': ['iex_basefill_053'], 'func': iex_base_universe_d2_053_iex_basefill_053}


def iex_base_universe_d2_054_iex_basefill_054(iex_basefill_054):
    return _base_universe_d2(iex_basefill_054, 54)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_054_iex_basefill_054'] = {'inputs': ['iex_basefill_054'], 'func': iex_base_universe_d2_054_iex_basefill_054}


def iex_base_universe_d2_055_iex_basefill_055(iex_basefill_055):
    return _base_universe_d2(iex_basefill_055, 55)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_055_iex_basefill_055'] = {'inputs': ['iex_basefill_055'], 'func': iex_base_universe_d2_055_iex_basefill_055}


def iex_base_universe_d2_056_iex_basefill_056(iex_basefill_056):
    return _base_universe_d2(iex_basefill_056, 56)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_056_iex_basefill_056'] = {'inputs': ['iex_basefill_056'], 'func': iex_base_universe_d2_056_iex_basefill_056}


def iex_base_universe_d2_057_iex_basefill_057(iex_basefill_057):
    return _base_universe_d2(iex_basefill_057, 57)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_057_iex_basefill_057'] = {'inputs': ['iex_basefill_057'], 'func': iex_base_universe_d2_057_iex_basefill_057}


def iex_base_universe_d2_058_iex_basefill_058(iex_basefill_058):
    return _base_universe_d2(iex_basefill_058, 58)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_058_iex_basefill_058'] = {'inputs': ['iex_basefill_058'], 'func': iex_base_universe_d2_058_iex_basefill_058}


def iex_base_universe_d2_059_iex_basefill_059(iex_basefill_059):
    return _base_universe_d2(iex_basefill_059, 59)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_059_iex_basefill_059'] = {'inputs': ['iex_basefill_059'], 'func': iex_base_universe_d2_059_iex_basefill_059}


def iex_base_universe_d2_060_iex_basefill_060(iex_basefill_060):
    return _base_universe_d2(iex_basefill_060, 60)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_060_iex_basefill_060'] = {'inputs': ['iex_basefill_060'], 'func': iex_base_universe_d2_060_iex_basefill_060}


def iex_base_universe_d2_061_iex_basefill_061(iex_basefill_061):
    return _base_universe_d2(iex_basefill_061, 61)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_061_iex_basefill_061'] = {'inputs': ['iex_basefill_061'], 'func': iex_base_universe_d2_061_iex_basefill_061}


def iex_base_universe_d2_062_iex_basefill_062(iex_basefill_062):
    return _base_universe_d2(iex_basefill_062, 62)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_062_iex_basefill_062'] = {'inputs': ['iex_basefill_062'], 'func': iex_base_universe_d2_062_iex_basefill_062}


def iex_base_universe_d2_063_iex_basefill_063(iex_basefill_063):
    return _base_universe_d2(iex_basefill_063, 63)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_063_iex_basefill_063'] = {'inputs': ['iex_basefill_063'], 'func': iex_base_universe_d2_063_iex_basefill_063}


def iex_base_universe_d2_064_iex_basefill_064(iex_basefill_064):
    return _base_universe_d2(iex_basefill_064, 64)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_064_iex_basefill_064'] = {'inputs': ['iex_basefill_064'], 'func': iex_base_universe_d2_064_iex_basefill_064}


def iex_base_universe_d2_065_iex_basefill_065(iex_basefill_065):
    return _base_universe_d2(iex_basefill_065, 65)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_065_iex_basefill_065'] = {'inputs': ['iex_basefill_065'], 'func': iex_base_universe_d2_065_iex_basefill_065}


def iex_base_universe_d2_066_iex_basefill_066(iex_basefill_066):
    return _base_universe_d2(iex_basefill_066, 66)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_066_iex_basefill_066'] = {'inputs': ['iex_basefill_066'], 'func': iex_base_universe_d2_066_iex_basefill_066}


def iex_base_universe_d2_067_iex_basefill_067(iex_basefill_067):
    return _base_universe_d2(iex_basefill_067, 67)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_067_iex_basefill_067'] = {'inputs': ['iex_basefill_067'], 'func': iex_base_universe_d2_067_iex_basefill_067}


def iex_base_universe_d2_068_iex_basefill_068(iex_basefill_068):
    return _base_universe_d2(iex_basefill_068, 68)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_068_iex_basefill_068'] = {'inputs': ['iex_basefill_068'], 'func': iex_base_universe_d2_068_iex_basefill_068}


def iex_base_universe_d2_069_iex_basefill_069(iex_basefill_069):
    return _base_universe_d2(iex_basefill_069, 69)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_069_iex_basefill_069'] = {'inputs': ['iex_basefill_069'], 'func': iex_base_universe_d2_069_iex_basefill_069}


def iex_base_universe_d2_070_iex_basefill_070(iex_basefill_070):
    return _base_universe_d2(iex_basefill_070, 70)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_070_iex_basefill_070'] = {'inputs': ['iex_basefill_070'], 'func': iex_base_universe_d2_070_iex_basefill_070}


def iex_base_universe_d2_071_iex_basefill_071(iex_basefill_071):
    return _base_universe_d2(iex_basefill_071, 71)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_071_iex_basefill_071'] = {'inputs': ['iex_basefill_071'], 'func': iex_base_universe_d2_071_iex_basefill_071}


def iex_base_universe_d2_072_iex_basefill_072(iex_basefill_072):
    return _base_universe_d2(iex_basefill_072, 72)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_072_iex_basefill_072'] = {'inputs': ['iex_basefill_072'], 'func': iex_base_universe_d2_072_iex_basefill_072}


def iex_base_universe_d2_073_iex_basefill_073(iex_basefill_073):
    return _base_universe_d2(iex_basefill_073, 73)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_073_iex_basefill_073'] = {'inputs': ['iex_basefill_073'], 'func': iex_base_universe_d2_073_iex_basefill_073}


def iex_base_universe_d2_074_iex_basefill_074(iex_basefill_074):
    return _base_universe_d2(iex_basefill_074, 74)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_074_iex_basefill_074'] = {'inputs': ['iex_basefill_074'], 'func': iex_base_universe_d2_074_iex_basefill_074}


def iex_base_universe_d2_075_iex_basefill_075(iex_basefill_075):
    return _base_universe_d2(iex_basefill_075, 75)
IEX_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['iex_base_universe_d2_075_iex_basefill_075'] = {'inputs': ['iex_basefill_075'], 'func': iex_base_universe_d2_075_iex_basefill_075}
