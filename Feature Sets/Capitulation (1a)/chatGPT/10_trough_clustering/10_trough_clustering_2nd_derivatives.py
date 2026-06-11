import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


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


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def tcl_001_amihud_illiquidity_roc_1(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 1)).reindex(feature.index)

def tcl_007_amihud_illiquidity_roc_5(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 5)).reindex(feature.index)

def tcl_013_amihud_illiquidity_roc_42(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 42)).reindex(feature.index)

def tcl_154_tcl_019_amihud_illiquidity_42_019_roc_126(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 126)).reindex(feature.index)

def tcl_155_tcl_025_amihud_illiquidity_378_025_roc_378(amihud_illiquidity):
    feature = _s(amihud_illiquidity)
    return (_roc(feature, 378)).reindex(feature.index)






















TROUGH_CLUSTERING_REGISTRY_2ND_DERIVATIVES = {
    'tcl_001_amihud_illiquidity_roc_1': {'inputs': ['amihud_illiquidity'], 'func': tcl_001_amihud_illiquidity_roc_1},
    'tcl_007_amihud_illiquidity_roc_5': {'inputs': ['amihud_illiquidity'], 'func': tcl_007_amihud_illiquidity_roc_5},
    'tcl_013_amihud_illiquidity_roc_42': {'inputs': ['amihud_illiquidity'], 'func': tcl_013_amihud_illiquidity_roc_42},
    'tcl_154_tcl_019_amihud_illiquidity_42_019_roc_126': {'inputs': ['amihud_illiquidity'], 'func': tcl_154_tcl_019_amihud_illiquidity_42_019_roc_126},
    'tcl_155_tcl_025_amihud_illiquidity_378_025_roc_378': {'inputs': ['amihud_illiquidity'], 'func': tcl_155_tcl_025_amihud_illiquidity_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def tc_replacement_d2_001(tc_replacement_001):
    feature = _clean(tc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_001'] = {'inputs': ['tc_replacement_001'], 'func': tc_replacement_d2_001}


def tc_replacement_d2_002(tc_replacement_002):
    feature = _clean(tc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_002'] = {'inputs': ['tc_replacement_002'], 'func': tc_replacement_d2_002}


def tc_replacement_d2_003(tc_replacement_003):
    feature = _clean(tc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_003'] = {'inputs': ['tc_replacement_003'], 'func': tc_replacement_d2_003}


def tc_replacement_d2_004(tc_replacement_004):
    feature = _clean(tc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_004'] = {'inputs': ['tc_replacement_004'], 'func': tc_replacement_d2_004}


def tc_replacement_d2_005(tc_replacement_005):
    feature = _clean(tc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_005'] = {'inputs': ['tc_replacement_005'], 'func': tc_replacement_d2_005}


def tc_replacement_d2_006(tc_replacement_006):
    feature = _clean(tc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_006'] = {'inputs': ['tc_replacement_006'], 'func': tc_replacement_d2_006}


def tc_replacement_d2_007(tc_replacement_007):
    feature = _clean(tc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_007'] = {'inputs': ['tc_replacement_007'], 'func': tc_replacement_d2_007}


def tc_replacement_d2_008(tc_replacement_008):
    feature = _clean(tc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_008'] = {'inputs': ['tc_replacement_008'], 'func': tc_replacement_d2_008}


def tc_replacement_d2_009(tc_replacement_009):
    feature = _clean(tc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_009'] = {'inputs': ['tc_replacement_009'], 'func': tc_replacement_d2_009}


def tc_replacement_d2_010(tc_replacement_010):
    feature = _clean(tc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_010'] = {'inputs': ['tc_replacement_010'], 'func': tc_replacement_d2_010}


def tc_replacement_d2_011(tc_replacement_011):
    feature = _clean(tc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_011'] = {'inputs': ['tc_replacement_011'], 'func': tc_replacement_d2_011}


def tc_replacement_d2_012(tc_replacement_012):
    feature = _clean(tc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_012'] = {'inputs': ['tc_replacement_012'], 'func': tc_replacement_d2_012}


def tc_replacement_d2_013(tc_replacement_013):
    feature = _clean(tc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_013'] = {'inputs': ['tc_replacement_013'], 'func': tc_replacement_d2_013}


def tc_replacement_d2_014(tc_replacement_014):
    feature = _clean(tc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_014'] = {'inputs': ['tc_replacement_014'], 'func': tc_replacement_d2_014}


def tc_replacement_d2_015(tc_replacement_015):
    feature = _clean(tc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_015'] = {'inputs': ['tc_replacement_015'], 'func': tc_replacement_d2_015}


def tc_replacement_d2_016(tc_replacement_016):
    feature = _clean(tc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_016'] = {'inputs': ['tc_replacement_016'], 'func': tc_replacement_d2_016}


def tc_replacement_d2_017(tc_replacement_017):
    feature = _clean(tc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_017'] = {'inputs': ['tc_replacement_017'], 'func': tc_replacement_d2_017}


def tc_replacement_d2_018(tc_replacement_018):
    feature = _clean(tc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_018'] = {'inputs': ['tc_replacement_018'], 'func': tc_replacement_d2_018}


def tc_replacement_d2_019(tc_replacement_019):
    feature = _clean(tc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_019'] = {'inputs': ['tc_replacement_019'], 'func': tc_replacement_d2_019}


def tc_replacement_d2_020(tc_replacement_020):
    feature = _clean(tc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_020'] = {'inputs': ['tc_replacement_020'], 'func': tc_replacement_d2_020}


def tc_replacement_d2_021(tc_replacement_021):
    feature = _clean(tc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_021'] = {'inputs': ['tc_replacement_021'], 'func': tc_replacement_d2_021}


def tc_replacement_d2_022(tc_replacement_022):
    feature = _clean(tc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_022'] = {'inputs': ['tc_replacement_022'], 'func': tc_replacement_d2_022}


def tc_replacement_d2_023(tc_replacement_023):
    feature = _clean(tc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_023'] = {'inputs': ['tc_replacement_023'], 'func': tc_replacement_d2_023}


def tc_replacement_d2_024(tc_replacement_024):
    feature = _clean(tc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_024'] = {'inputs': ['tc_replacement_024'], 'func': tc_replacement_d2_024}


def tc_replacement_d2_025(tc_replacement_025):
    feature = _clean(tc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_025'] = {'inputs': ['tc_replacement_025'], 'func': tc_replacement_d2_025}


def tc_replacement_d2_026(tc_replacement_026):
    feature = _clean(tc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_026'] = {'inputs': ['tc_replacement_026'], 'func': tc_replacement_d2_026}


def tc_replacement_d2_027(tc_replacement_027):
    feature = _clean(tc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_027'] = {'inputs': ['tc_replacement_027'], 'func': tc_replacement_d2_027}


def tc_replacement_d2_028(tc_replacement_028):
    feature = _clean(tc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_028'] = {'inputs': ['tc_replacement_028'], 'func': tc_replacement_d2_028}


def tc_replacement_d2_029(tc_replacement_029):
    feature = _clean(tc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_029'] = {'inputs': ['tc_replacement_029'], 'func': tc_replacement_d2_029}


def tc_replacement_d2_030(tc_replacement_030):
    feature = _clean(tc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_030'] = {'inputs': ['tc_replacement_030'], 'func': tc_replacement_d2_030}


def tc_replacement_d2_031(tc_replacement_031):
    feature = _clean(tc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_031'] = {'inputs': ['tc_replacement_031'], 'func': tc_replacement_d2_031}


def tc_replacement_d2_032(tc_replacement_032):
    feature = _clean(tc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_032'] = {'inputs': ['tc_replacement_032'], 'func': tc_replacement_d2_032}


def tc_replacement_d2_033(tc_replacement_033):
    feature = _clean(tc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_033'] = {'inputs': ['tc_replacement_033'], 'func': tc_replacement_d2_033}


def tc_replacement_d2_034(tc_replacement_034):
    feature = _clean(tc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_034'] = {'inputs': ['tc_replacement_034'], 'func': tc_replacement_d2_034}


def tc_replacement_d2_035(tc_replacement_035):
    feature = _clean(tc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_035'] = {'inputs': ['tc_replacement_035'], 'func': tc_replacement_d2_035}


def tc_replacement_d2_036(tc_replacement_036):
    feature = _clean(tc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_036'] = {'inputs': ['tc_replacement_036'], 'func': tc_replacement_d2_036}


def tc_replacement_d2_037(tc_replacement_037):
    feature = _clean(tc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_037'] = {'inputs': ['tc_replacement_037'], 'func': tc_replacement_d2_037}


def tc_replacement_d2_038(tc_replacement_038):
    feature = _clean(tc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_038'] = {'inputs': ['tc_replacement_038'], 'func': tc_replacement_d2_038}


def tc_replacement_d2_039(tc_replacement_039):
    feature = _clean(tc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_039'] = {'inputs': ['tc_replacement_039'], 'func': tc_replacement_d2_039}


def tc_replacement_d2_040(tc_replacement_040):
    feature = _clean(tc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_040'] = {'inputs': ['tc_replacement_040'], 'func': tc_replacement_d2_040}


def tc_replacement_d2_041(tc_replacement_041):
    feature = _clean(tc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_041'] = {'inputs': ['tc_replacement_041'], 'func': tc_replacement_d2_041}


def tc_replacement_d2_042(tc_replacement_042):
    feature = _clean(tc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_042'] = {'inputs': ['tc_replacement_042'], 'func': tc_replacement_d2_042}


def tc_replacement_d2_043(tc_replacement_043):
    feature = _clean(tc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_043'] = {'inputs': ['tc_replacement_043'], 'func': tc_replacement_d2_043}


def tc_replacement_d2_044(tc_replacement_044):
    feature = _clean(tc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_044'] = {'inputs': ['tc_replacement_044'], 'func': tc_replacement_d2_044}


def tc_replacement_d2_045(tc_replacement_045):
    feature = _clean(tc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_045'] = {'inputs': ['tc_replacement_045'], 'func': tc_replacement_d2_045}


def tc_replacement_d2_046(tc_replacement_046):
    feature = _clean(tc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_046'] = {'inputs': ['tc_replacement_046'], 'func': tc_replacement_d2_046}


def tc_replacement_d2_047(tc_replacement_047):
    feature = _clean(tc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_047'] = {'inputs': ['tc_replacement_047'], 'func': tc_replacement_d2_047}


def tc_replacement_d2_048(tc_replacement_048):
    feature = _clean(tc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_048'] = {'inputs': ['tc_replacement_048'], 'func': tc_replacement_d2_048}


def tc_replacement_d2_049(tc_replacement_049):
    feature = _clean(tc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_049'] = {'inputs': ['tc_replacement_049'], 'func': tc_replacement_d2_049}


def tc_replacement_d2_050(tc_replacement_050):
    feature = _clean(tc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_050'] = {'inputs': ['tc_replacement_050'], 'func': tc_replacement_d2_050}


def tc_replacement_d2_051(tc_replacement_051):
    feature = _clean(tc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_051'] = {'inputs': ['tc_replacement_051'], 'func': tc_replacement_d2_051}


def tc_replacement_d2_052(tc_replacement_052):
    feature = _clean(tc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_052'] = {'inputs': ['tc_replacement_052'], 'func': tc_replacement_d2_052}


def tc_replacement_d2_053(tc_replacement_053):
    feature = _clean(tc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_053'] = {'inputs': ['tc_replacement_053'], 'func': tc_replacement_d2_053}


def tc_replacement_d2_054(tc_replacement_054):
    feature = _clean(tc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_054'] = {'inputs': ['tc_replacement_054'], 'func': tc_replacement_d2_054}


def tc_replacement_d2_055(tc_replacement_055):
    feature = _clean(tc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_055'] = {'inputs': ['tc_replacement_055'], 'func': tc_replacement_d2_055}


def tc_replacement_d2_056(tc_replacement_056):
    feature = _clean(tc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_056'] = {'inputs': ['tc_replacement_056'], 'func': tc_replacement_d2_056}


def tc_replacement_d2_057(tc_replacement_057):
    feature = _clean(tc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_057'] = {'inputs': ['tc_replacement_057'], 'func': tc_replacement_d2_057}


def tc_replacement_d2_058(tc_replacement_058):
    feature = _clean(tc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_058'] = {'inputs': ['tc_replacement_058'], 'func': tc_replacement_d2_058}


def tc_replacement_d2_059(tc_replacement_059):
    feature = _clean(tc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_059'] = {'inputs': ['tc_replacement_059'], 'func': tc_replacement_d2_059}


def tc_replacement_d2_060(tc_replacement_060):
    feature = _clean(tc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_060'] = {'inputs': ['tc_replacement_060'], 'func': tc_replacement_d2_060}


def tc_replacement_d2_061(tc_replacement_061):
    feature = _clean(tc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_061'] = {'inputs': ['tc_replacement_061'], 'func': tc_replacement_d2_061}


def tc_replacement_d2_062(tc_replacement_062):
    feature = _clean(tc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_062'] = {'inputs': ['tc_replacement_062'], 'func': tc_replacement_d2_062}


def tc_replacement_d2_063(tc_replacement_063):
    feature = _clean(tc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_063'] = {'inputs': ['tc_replacement_063'], 'func': tc_replacement_d2_063}


def tc_replacement_d2_064(tc_replacement_064):
    feature = _clean(tc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_064'] = {'inputs': ['tc_replacement_064'], 'func': tc_replacement_d2_064}


def tc_replacement_d2_065(tc_replacement_065):
    feature = _clean(tc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_065'] = {'inputs': ['tc_replacement_065'], 'func': tc_replacement_d2_065}


def tc_replacement_d2_066(tc_replacement_066):
    feature = _clean(tc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_066'] = {'inputs': ['tc_replacement_066'], 'func': tc_replacement_d2_066}


def tc_replacement_d2_067(tc_replacement_067):
    feature = _clean(tc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_067'] = {'inputs': ['tc_replacement_067'], 'func': tc_replacement_d2_067}


def tc_replacement_d2_068(tc_replacement_068):
    feature = _clean(tc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_068'] = {'inputs': ['tc_replacement_068'], 'func': tc_replacement_d2_068}


def tc_replacement_d2_069(tc_replacement_069):
    feature = _clean(tc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_069'] = {'inputs': ['tc_replacement_069'], 'func': tc_replacement_d2_069}


def tc_replacement_d2_070(tc_replacement_070):
    feature = _clean(tc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_070'] = {'inputs': ['tc_replacement_070'], 'func': tc_replacement_d2_070}


def tc_replacement_d2_071(tc_replacement_071):
    feature = _clean(tc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_071'] = {'inputs': ['tc_replacement_071'], 'func': tc_replacement_d2_071}


def tc_replacement_d2_072(tc_replacement_072):
    feature = _clean(tc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_072'] = {'inputs': ['tc_replacement_072'], 'func': tc_replacement_d2_072}


def tc_replacement_d2_073(tc_replacement_073):
    feature = _clean(tc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_073'] = {'inputs': ['tc_replacement_073'], 'func': tc_replacement_d2_073}


def tc_replacement_d2_074(tc_replacement_074):
    feature = _clean(tc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_074'] = {'inputs': ['tc_replacement_074'], 'func': tc_replacement_d2_074}


def tc_replacement_d2_075(tc_replacement_075):
    feature = _clean(tc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_075'] = {'inputs': ['tc_replacement_075'], 'func': tc_replacement_d2_075}


def tc_replacement_d2_076(tc_replacement_076):
    feature = _clean(tc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_076'] = {'inputs': ['tc_replacement_076'], 'func': tc_replacement_d2_076}


def tc_replacement_d2_077(tc_replacement_077):
    feature = _clean(tc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_077'] = {'inputs': ['tc_replacement_077'], 'func': tc_replacement_d2_077}


def tc_replacement_d2_078(tc_replacement_078):
    feature = _clean(tc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_078'] = {'inputs': ['tc_replacement_078'], 'func': tc_replacement_d2_078}


def tc_replacement_d2_079(tc_replacement_079):
    feature = _clean(tc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_079'] = {'inputs': ['tc_replacement_079'], 'func': tc_replacement_d2_079}


def tc_replacement_d2_080(tc_replacement_080):
    feature = _clean(tc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_080'] = {'inputs': ['tc_replacement_080'], 'func': tc_replacement_d2_080}


def tc_replacement_d2_081(tc_replacement_081):
    feature = _clean(tc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_081'] = {'inputs': ['tc_replacement_081'], 'func': tc_replacement_d2_081}


def tc_replacement_d2_082(tc_replacement_082):
    feature = _clean(tc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_082'] = {'inputs': ['tc_replacement_082'], 'func': tc_replacement_d2_082}


def tc_replacement_d2_083(tc_replacement_083):
    feature = _clean(tc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_083'] = {'inputs': ['tc_replacement_083'], 'func': tc_replacement_d2_083}


def tc_replacement_d2_084(tc_replacement_084):
    feature = _clean(tc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_084'] = {'inputs': ['tc_replacement_084'], 'func': tc_replacement_d2_084}


def tc_replacement_d2_085(tc_replacement_085):
    feature = _clean(tc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_085'] = {'inputs': ['tc_replacement_085'], 'func': tc_replacement_d2_085}


def tc_replacement_d2_086(tc_replacement_086):
    feature = _clean(tc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_086'] = {'inputs': ['tc_replacement_086'], 'func': tc_replacement_d2_086}


def tc_replacement_d2_087(tc_replacement_087):
    feature = _clean(tc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_087'] = {'inputs': ['tc_replacement_087'], 'func': tc_replacement_d2_087}


def tc_replacement_d2_088(tc_replacement_088):
    feature = _clean(tc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_088'] = {'inputs': ['tc_replacement_088'], 'func': tc_replacement_d2_088}


def tc_replacement_d2_089(tc_replacement_089):
    feature = _clean(tc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_089'] = {'inputs': ['tc_replacement_089'], 'func': tc_replacement_d2_089}


def tc_replacement_d2_090(tc_replacement_090):
    feature = _clean(tc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_090'] = {'inputs': ['tc_replacement_090'], 'func': tc_replacement_d2_090}


def tc_replacement_d2_091(tc_replacement_091):
    feature = _clean(tc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_091'] = {'inputs': ['tc_replacement_091'], 'func': tc_replacement_d2_091}


def tc_replacement_d2_092(tc_replacement_092):
    feature = _clean(tc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_092'] = {'inputs': ['tc_replacement_092'], 'func': tc_replacement_d2_092}


def tc_replacement_d2_093(tc_replacement_093):
    feature = _clean(tc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_093'] = {'inputs': ['tc_replacement_093'], 'func': tc_replacement_d2_093}


def tc_replacement_d2_094(tc_replacement_094):
    feature = _clean(tc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_094'] = {'inputs': ['tc_replacement_094'], 'func': tc_replacement_d2_094}


def tc_replacement_d2_095(tc_replacement_095):
    feature = _clean(tc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_095'] = {'inputs': ['tc_replacement_095'], 'func': tc_replacement_d2_095}


def tc_replacement_d2_096(tc_replacement_096):
    feature = _clean(tc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_096'] = {'inputs': ['tc_replacement_096'], 'func': tc_replacement_d2_096}


def tc_replacement_d2_097(tc_replacement_097):
    feature = _clean(tc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_097'] = {'inputs': ['tc_replacement_097'], 'func': tc_replacement_d2_097}


def tc_replacement_d2_098(tc_replacement_098):
    feature = _clean(tc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_098'] = {'inputs': ['tc_replacement_098'], 'func': tc_replacement_d2_098}


def tc_replacement_d2_099(tc_replacement_099):
    feature = _clean(tc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_099'] = {'inputs': ['tc_replacement_099'], 'func': tc_replacement_d2_099}


def tc_replacement_d2_100(tc_replacement_100):
    feature = _clean(tc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_100'] = {'inputs': ['tc_replacement_100'], 'func': tc_replacement_d2_100}


def tc_replacement_d2_101(tc_replacement_101):
    feature = _clean(tc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_101'] = {'inputs': ['tc_replacement_101'], 'func': tc_replacement_d2_101}


def tc_replacement_d2_102(tc_replacement_102):
    feature = _clean(tc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_102'] = {'inputs': ['tc_replacement_102'], 'func': tc_replacement_d2_102}


def tc_replacement_d2_103(tc_replacement_103):
    feature = _clean(tc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_103'] = {'inputs': ['tc_replacement_103'], 'func': tc_replacement_d2_103}


def tc_replacement_d2_104(tc_replacement_104):
    feature = _clean(tc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_104'] = {'inputs': ['tc_replacement_104'], 'func': tc_replacement_d2_104}


def tc_replacement_d2_105(tc_replacement_105):
    feature = _clean(tc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_105'] = {'inputs': ['tc_replacement_105'], 'func': tc_replacement_d2_105}


def tc_replacement_d2_106(tc_replacement_106):
    feature = _clean(tc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_106'] = {'inputs': ['tc_replacement_106'], 'func': tc_replacement_d2_106}


def tc_replacement_d2_107(tc_replacement_107):
    feature = _clean(tc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_107'] = {'inputs': ['tc_replacement_107'], 'func': tc_replacement_d2_107}


def tc_replacement_d2_108(tc_replacement_108):
    feature = _clean(tc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_108'] = {'inputs': ['tc_replacement_108'], 'func': tc_replacement_d2_108}


def tc_replacement_d2_109(tc_replacement_109):
    feature = _clean(tc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_109'] = {'inputs': ['tc_replacement_109'], 'func': tc_replacement_d2_109}


def tc_replacement_d2_110(tc_replacement_110):
    feature = _clean(tc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_110'] = {'inputs': ['tc_replacement_110'], 'func': tc_replacement_d2_110}


def tc_replacement_d2_111(tc_replacement_111):
    feature = _clean(tc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_111'] = {'inputs': ['tc_replacement_111'], 'func': tc_replacement_d2_111}


def tc_replacement_d2_112(tc_replacement_112):
    feature = _clean(tc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_112'] = {'inputs': ['tc_replacement_112'], 'func': tc_replacement_d2_112}


def tc_replacement_d2_113(tc_replacement_113):
    feature = _clean(tc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_113'] = {'inputs': ['tc_replacement_113'], 'func': tc_replacement_d2_113}


def tc_replacement_d2_114(tc_replacement_114):
    feature = _clean(tc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_114'] = {'inputs': ['tc_replacement_114'], 'func': tc_replacement_d2_114}


def tc_replacement_d2_115(tc_replacement_115):
    feature = _clean(tc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_115'] = {'inputs': ['tc_replacement_115'], 'func': tc_replacement_d2_115}


def tc_replacement_d2_116(tc_replacement_116):
    feature = _clean(tc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_116'] = {'inputs': ['tc_replacement_116'], 'func': tc_replacement_d2_116}


def tc_replacement_d2_117(tc_replacement_117):
    feature = _clean(tc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_117'] = {'inputs': ['tc_replacement_117'], 'func': tc_replacement_d2_117}


def tc_replacement_d2_118(tc_replacement_118):
    feature = _clean(tc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_118'] = {'inputs': ['tc_replacement_118'], 'func': tc_replacement_d2_118}


def tc_replacement_d2_119(tc_replacement_119):
    feature = _clean(tc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_119'] = {'inputs': ['tc_replacement_119'], 'func': tc_replacement_d2_119}


def tc_replacement_d2_120(tc_replacement_120):
    feature = _clean(tc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_120'] = {'inputs': ['tc_replacement_120'], 'func': tc_replacement_d2_120}


def tc_replacement_d2_121(tc_replacement_121):
    feature = _clean(tc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_121'] = {'inputs': ['tc_replacement_121'], 'func': tc_replacement_d2_121}


def tc_replacement_d2_122(tc_replacement_122):
    feature = _clean(tc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_122'] = {'inputs': ['tc_replacement_122'], 'func': tc_replacement_d2_122}


def tc_replacement_d2_123(tc_replacement_123):
    feature = _clean(tc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_123'] = {'inputs': ['tc_replacement_123'], 'func': tc_replacement_d2_123}


def tc_replacement_d2_124(tc_replacement_124):
    feature = _clean(tc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_124'] = {'inputs': ['tc_replacement_124'], 'func': tc_replacement_d2_124}


def tc_replacement_d2_125(tc_replacement_125):
    feature = _clean(tc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_125'] = {'inputs': ['tc_replacement_125'], 'func': tc_replacement_d2_125}


def tc_replacement_d2_126(tc_replacement_126):
    feature = _clean(tc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_126'] = {'inputs': ['tc_replacement_126'], 'func': tc_replacement_d2_126}


def tc_replacement_d2_127(tc_replacement_127):
    feature = _clean(tc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_127'] = {'inputs': ['tc_replacement_127'], 'func': tc_replacement_d2_127}


def tc_replacement_d2_128(tc_replacement_128):
    feature = _clean(tc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_128'] = {'inputs': ['tc_replacement_128'], 'func': tc_replacement_d2_128}


def tc_replacement_d2_129(tc_replacement_129):
    feature = _clean(tc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_129'] = {'inputs': ['tc_replacement_129'], 'func': tc_replacement_d2_129}


def tc_replacement_d2_130(tc_replacement_130):
    feature = _clean(tc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_130'] = {'inputs': ['tc_replacement_130'], 'func': tc_replacement_d2_130}


def tc_replacement_d2_131(tc_replacement_131):
    feature = _clean(tc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_131'] = {'inputs': ['tc_replacement_131'], 'func': tc_replacement_d2_131}


def tc_replacement_d2_132(tc_replacement_132):
    feature = _clean(tc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_132'] = {'inputs': ['tc_replacement_132'], 'func': tc_replacement_d2_132}


def tc_replacement_d2_133(tc_replacement_133):
    feature = _clean(tc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_133'] = {'inputs': ['tc_replacement_133'], 'func': tc_replacement_d2_133}


def tc_replacement_d2_134(tc_replacement_134):
    feature = _clean(tc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_134'] = {'inputs': ['tc_replacement_134'], 'func': tc_replacement_d2_134}


def tc_replacement_d2_135(tc_replacement_135):
    feature = _clean(tc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_135'] = {'inputs': ['tc_replacement_135'], 'func': tc_replacement_d2_135}


def tc_replacement_d2_136(tc_replacement_136):
    feature = _clean(tc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_136'] = {'inputs': ['tc_replacement_136'], 'func': tc_replacement_d2_136}


def tc_replacement_d2_137(tc_replacement_137):
    feature = _clean(tc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_137'] = {'inputs': ['tc_replacement_137'], 'func': tc_replacement_d2_137}


def tc_replacement_d2_138(tc_replacement_138):
    feature = _clean(tc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_138'] = {'inputs': ['tc_replacement_138'], 'func': tc_replacement_d2_138}


def tc_replacement_d2_139(tc_replacement_139):
    feature = _clean(tc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_139'] = {'inputs': ['tc_replacement_139'], 'func': tc_replacement_d2_139}


def tc_replacement_d2_140(tc_replacement_140):
    feature = _clean(tc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_140'] = {'inputs': ['tc_replacement_140'], 'func': tc_replacement_d2_140}


def tc_replacement_d2_141(tc_replacement_141):
    feature = _clean(tc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_141'] = {'inputs': ['tc_replacement_141'], 'func': tc_replacement_d2_141}


def tc_replacement_d2_142(tc_replacement_142):
    feature = _clean(tc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_142'] = {'inputs': ['tc_replacement_142'], 'func': tc_replacement_d2_142}


def tc_replacement_d2_143(tc_replacement_143):
    feature = _clean(tc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_143'] = {'inputs': ['tc_replacement_143'], 'func': tc_replacement_d2_143}


def tc_replacement_d2_144(tc_replacement_144):
    feature = _clean(tc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_144'] = {'inputs': ['tc_replacement_144'], 'func': tc_replacement_d2_144}


def tc_replacement_d2_145(tc_replacement_145):
    feature = _clean(tc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_145'] = {'inputs': ['tc_replacement_145'], 'func': tc_replacement_d2_145}


def tc_replacement_d2_146(tc_replacement_146):
    feature = _clean(tc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_146'] = {'inputs': ['tc_replacement_146'], 'func': tc_replacement_d2_146}


def tc_replacement_d2_147(tc_replacement_147):
    feature = _clean(tc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_147'] = {'inputs': ['tc_replacement_147'], 'func': tc_replacement_d2_147}


def tc_replacement_d2_148(tc_replacement_148):
    feature = _clean(tc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_148'] = {'inputs': ['tc_replacement_148'], 'func': tc_replacement_d2_148}


def tc_replacement_d2_149(tc_replacement_149):
    feature = _clean(tc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_149'] = {'inputs': ['tc_replacement_149'], 'func': tc_replacement_d2_149}


def tc_replacement_d2_150(tc_replacement_150):
    feature = _clean(tc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_150'] = {'inputs': ['tc_replacement_150'], 'func': tc_replacement_d2_150}


def tc_replacement_d2_151(tc_replacement_151):
    feature = _clean(tc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_151'] = {'inputs': ['tc_replacement_151'], 'func': tc_replacement_d2_151}


def tc_replacement_d2_152(tc_replacement_152):
    feature = _clean(tc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_152'] = {'inputs': ['tc_replacement_152'], 'func': tc_replacement_d2_152}


def tc_replacement_d2_153(tc_replacement_153):
    feature = _clean(tc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_153'] = {'inputs': ['tc_replacement_153'], 'func': tc_replacement_d2_153}


def tc_replacement_d2_154(tc_replacement_154):
    feature = _clean(tc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_154'] = {'inputs': ['tc_replacement_154'], 'func': tc_replacement_d2_154}


def tc_replacement_d2_155(tc_replacement_155):
    feature = _clean(tc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_155'] = {'inputs': ['tc_replacement_155'], 'func': tc_replacement_d2_155}


def tc_replacement_d2_156(tc_replacement_156):
    feature = _clean(tc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_156'] = {'inputs': ['tc_replacement_156'], 'func': tc_replacement_d2_156}


def tc_replacement_d2_157(tc_replacement_157):
    feature = _clean(tc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_157'] = {'inputs': ['tc_replacement_157'], 'func': tc_replacement_d2_157}


def tc_replacement_d2_158(tc_replacement_158):
    feature = _clean(tc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_158'] = {'inputs': ['tc_replacement_158'], 'func': tc_replacement_d2_158}


def tc_replacement_d2_159(tc_replacement_159):
    feature = _clean(tc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_159'] = {'inputs': ['tc_replacement_159'], 'func': tc_replacement_d2_159}


def tc_replacement_d2_160(tc_replacement_160):
    feature = _clean(tc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_160'] = {'inputs': ['tc_replacement_160'], 'func': tc_replacement_d2_160}


def tc_replacement_d2_161(tc_replacement_161):
    feature = _clean(tc_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_161'] = {'inputs': ['tc_replacement_161'], 'func': tc_replacement_d2_161}


def tc_replacement_d2_162(tc_replacement_162):
    feature = _clean(tc_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_162'] = {'inputs': ['tc_replacement_162'], 'func': tc_replacement_d2_162}


def tc_replacement_d2_163(tc_replacement_163):
    feature = _clean(tc_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_163'] = {'inputs': ['tc_replacement_163'], 'func': tc_replacement_d2_163}


def tc_replacement_d2_164(tc_replacement_164):
    feature = _clean(tc_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_164'] = {'inputs': ['tc_replacement_164'], 'func': tc_replacement_d2_164}


def tc_replacement_d2_165(tc_replacement_165):
    feature = _clean(tc_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_165'] = {'inputs': ['tc_replacement_165'], 'func': tc_replacement_d2_165}


def tc_replacement_d2_166(tc_replacement_166):
    feature = _clean(tc_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_166'] = {'inputs': ['tc_replacement_166'], 'func': tc_replacement_d2_166}


def tc_replacement_d2_167(tc_replacement_167):
    feature = _clean(tc_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_167'] = {'inputs': ['tc_replacement_167'], 'func': tc_replacement_d2_167}


def tc_replacement_d2_168(tc_replacement_168):
    feature = _clean(tc_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_168'] = {'inputs': ['tc_replacement_168'], 'func': tc_replacement_d2_168}


def tc_replacement_d2_169(tc_replacement_169):
    feature = _clean(tc_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_169'] = {'inputs': ['tc_replacement_169'], 'func': tc_replacement_d2_169}


def tc_replacement_d2_170(tc_replacement_170):
    feature = _clean(tc_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
TC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['tc_replacement_d2_170'] = {'inputs': ['tc_replacement_170'], 'func': tc_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tcl_base_universe_d2_001_tcl_002_zero_volume_frequency_10_002(tcl_002_zero_volume_frequency_10_002):
    return _base_universe_d2(tcl_002_zero_volume_frequency_10_002, 1)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_001_tcl_002_zero_volume_frequency_10_002'] = {'inputs': ['tcl_002_zero_volume_frequency_10_002'], 'func': tcl_base_universe_d2_001_tcl_002_zero_volume_frequency_10_002}


def tcl_base_universe_d2_002_tcl_003_spread_proxy_21_003(tcl_003_spread_proxy_21_003):
    return _base_universe_d2(tcl_003_spread_proxy_21_003, 2)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_002_tcl_003_spread_proxy_21_003'] = {'inputs': ['tcl_003_spread_proxy_21_003'], 'func': tcl_base_universe_d2_002_tcl_003_spread_proxy_21_003}


def tcl_base_universe_d2_003_tcl_004_trading_intensity_42_004(tcl_004_trading_intensity_42_004):
    return _base_universe_d2(tcl_004_trading_intensity_42_004, 3)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_003_tcl_004_trading_intensity_42_004'] = {'inputs': ['tcl_004_trading_intensity_42_004'], 'func': tcl_base_universe_d2_003_tcl_004_trading_intensity_42_004}


def tcl_base_universe_d2_004_tcl_006_price_level_distress_84_006(tcl_006_price_level_distress_84_006):
    return _base_universe_d2(tcl_006_price_level_distress_84_006, 4)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_004_tcl_006_price_level_distress_84_006'] = {'inputs': ['tcl_006_price_level_distress_84_006'], 'func': tcl_base_universe_d2_004_tcl_006_price_level_distress_84_006}


def tcl_base_universe_d2_005_tcl_008_zero_volume_frequency_189_008(tcl_008_zero_volume_frequency_189_008):
    return _base_universe_d2(tcl_008_zero_volume_frequency_189_008, 5)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_005_tcl_008_zero_volume_frequency_189_008'] = {'inputs': ['tcl_008_zero_volume_frequency_189_008'], 'func': tcl_base_universe_d2_005_tcl_008_zero_volume_frequency_189_008}


def tcl_base_universe_d2_006_tcl_009_spread_proxy_252_009(tcl_009_spread_proxy_252_009):
    return _base_universe_d2(tcl_009_spread_proxy_252_009, 6)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_006_tcl_009_spread_proxy_252_009'] = {'inputs': ['tcl_009_spread_proxy_252_009'], 'func': tcl_base_universe_d2_006_tcl_009_spread_proxy_252_009}


def tcl_base_universe_d2_007_tcl_010_trading_intensity_378_010(tcl_010_trading_intensity_378_010):
    return _base_universe_d2(tcl_010_trading_intensity_378_010, 7)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_007_tcl_010_trading_intensity_378_010'] = {'inputs': ['tcl_010_trading_intensity_378_010'], 'func': tcl_base_universe_d2_007_tcl_010_trading_intensity_378_010}


def tcl_base_universe_d2_008_tcl_012_price_level_distress_756_012(tcl_012_price_level_distress_756_012):
    return _base_universe_d2(tcl_012_price_level_distress_756_012, 8)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_008_tcl_012_price_level_distress_756_012'] = {'inputs': ['tcl_012_price_level_distress_756_012'], 'func': tcl_base_universe_d2_008_tcl_012_price_level_distress_756_012}


def tcl_base_universe_d2_009_tcl_014_zero_volume_frequency_1260_014(tcl_014_zero_volume_frequency_1260_014):
    return _base_universe_d2(tcl_014_zero_volume_frequency_1260_014, 9)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_009_tcl_014_zero_volume_frequency_1260_014'] = {'inputs': ['tcl_014_zero_volume_frequency_1260_014'], 'func': tcl_base_universe_d2_009_tcl_014_zero_volume_frequency_1260_014}


def tcl_base_universe_d2_010_tcl_015_spread_proxy_1512_015(tcl_015_spread_proxy_1512_015):
    return _base_universe_d2(tcl_015_spread_proxy_1512_015, 10)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_010_tcl_015_spread_proxy_1512_015'] = {'inputs': ['tcl_015_spread_proxy_1512_015'], 'func': tcl_base_universe_d2_010_tcl_015_spread_proxy_1512_015}


def tcl_base_universe_d2_011_tcl_016_trading_intensity_5_016(tcl_016_trading_intensity_5_016):
    return _base_universe_d2(tcl_016_trading_intensity_5_016, 11)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_011_tcl_016_trading_intensity_5_016'] = {'inputs': ['tcl_016_trading_intensity_5_016'], 'func': tcl_base_universe_d2_011_tcl_016_trading_intensity_5_016}


def tcl_base_universe_d2_012_tcl_018_price_level_distress_21_018(tcl_018_price_level_distress_21_018):
    return _base_universe_d2(tcl_018_price_level_distress_21_018, 12)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_012_tcl_018_price_level_distress_21_018'] = {'inputs': ['tcl_018_price_level_distress_21_018'], 'func': tcl_base_universe_d2_012_tcl_018_price_level_distress_21_018}


def tcl_base_universe_d2_013_tcl_020_zero_volume_frequency_63_020(tcl_020_zero_volume_frequency_63_020):
    return _base_universe_d2(tcl_020_zero_volume_frequency_63_020, 13)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_013_tcl_020_zero_volume_frequency_63_020'] = {'inputs': ['tcl_020_zero_volume_frequency_63_020'], 'func': tcl_base_universe_d2_013_tcl_020_zero_volume_frequency_63_020}


def tcl_base_universe_d2_014_tcl_021_spread_proxy_84_021(tcl_021_spread_proxy_84_021):
    return _base_universe_d2(tcl_021_spread_proxy_84_021, 14)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_014_tcl_021_spread_proxy_84_021'] = {'inputs': ['tcl_021_spread_proxy_84_021'], 'func': tcl_base_universe_d2_014_tcl_021_spread_proxy_84_021}


def tcl_base_universe_d2_015_tcl_022_trading_intensity_126_022(tcl_022_trading_intensity_126_022):
    return _base_universe_d2(tcl_022_trading_intensity_126_022, 15)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_015_tcl_022_trading_intensity_126_022'] = {'inputs': ['tcl_022_trading_intensity_126_022'], 'func': tcl_base_universe_d2_015_tcl_022_trading_intensity_126_022}


def tcl_base_universe_d2_016_tcl_024_price_level_distress_252_024(tcl_024_price_level_distress_252_024):
    return _base_universe_d2(tcl_024_price_level_distress_252_024, 16)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_016_tcl_024_price_level_distress_252_024'] = {'inputs': ['tcl_024_price_level_distress_252_024'], 'func': tcl_base_universe_d2_016_tcl_024_price_level_distress_252_024}


def tcl_base_universe_d2_017_tcl_026_zero_volume_frequency_504_026(tcl_026_zero_volume_frequency_504_026):
    return _base_universe_d2(tcl_026_zero_volume_frequency_504_026, 17)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_017_tcl_026_zero_volume_frequency_504_026'] = {'inputs': ['tcl_026_zero_volume_frequency_504_026'], 'func': tcl_base_universe_d2_017_tcl_026_zero_volume_frequency_504_026}


def tcl_base_universe_d2_018_tcl_027_spread_proxy_756_027(tcl_027_spread_proxy_756_027):
    return _base_universe_d2(tcl_027_spread_proxy_756_027, 18)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_018_tcl_027_spread_proxy_756_027'] = {'inputs': ['tcl_027_spread_proxy_756_027'], 'func': tcl_base_universe_d2_018_tcl_027_spread_proxy_756_027}


def tcl_base_universe_d2_019_tcl_028_trading_intensity_1008_028(tcl_028_trading_intensity_1008_028):
    return _base_universe_d2(tcl_028_trading_intensity_1008_028, 19)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_019_tcl_028_trading_intensity_1008_028'] = {'inputs': ['tcl_028_trading_intensity_1008_028'], 'func': tcl_base_universe_d2_019_tcl_028_trading_intensity_1008_028}


def tcl_base_universe_d2_020_tcl_030_price_level_distress_1512_030(tcl_030_price_level_distress_1512_030):
    return _base_universe_d2(tcl_030_price_level_distress_1512_030, 20)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_020_tcl_030_price_level_distress_1512_030'] = {'inputs': ['tcl_030_price_level_distress_1512_030'], 'func': tcl_base_universe_d2_020_tcl_030_price_level_distress_1512_030}


def tcl_base_universe_d2_021_tcl_basefill_001(tcl_basefill_001):
    return _base_universe_d2(tcl_basefill_001, 21)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_021_tcl_basefill_001'] = {'inputs': ['tcl_basefill_001'], 'func': tcl_base_universe_d2_021_tcl_basefill_001}


def tcl_base_universe_d2_022_tcl_basefill_005(tcl_basefill_005):
    return _base_universe_d2(tcl_basefill_005, 22)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_022_tcl_basefill_005'] = {'inputs': ['tcl_basefill_005'], 'func': tcl_base_universe_d2_022_tcl_basefill_005}


def tcl_base_universe_d2_023_tcl_basefill_007(tcl_basefill_007):
    return _base_universe_d2(tcl_basefill_007, 23)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_023_tcl_basefill_007'] = {'inputs': ['tcl_basefill_007'], 'func': tcl_base_universe_d2_023_tcl_basefill_007}


def tcl_base_universe_d2_024_tcl_basefill_011(tcl_basefill_011):
    return _base_universe_d2(tcl_basefill_011, 24)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_024_tcl_basefill_011'] = {'inputs': ['tcl_basefill_011'], 'func': tcl_base_universe_d2_024_tcl_basefill_011}


def tcl_base_universe_d2_025_tcl_basefill_013(tcl_basefill_013):
    return _base_universe_d2(tcl_basefill_013, 25)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_025_tcl_basefill_013'] = {'inputs': ['tcl_basefill_013'], 'func': tcl_base_universe_d2_025_tcl_basefill_013}


def tcl_base_universe_d2_026_tcl_basefill_017(tcl_basefill_017):
    return _base_universe_d2(tcl_basefill_017, 26)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_026_tcl_basefill_017'] = {'inputs': ['tcl_basefill_017'], 'func': tcl_base_universe_d2_026_tcl_basefill_017}


def tcl_base_universe_d2_027_tcl_basefill_019(tcl_basefill_019):
    return _base_universe_d2(tcl_basefill_019, 27)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_027_tcl_basefill_019'] = {'inputs': ['tcl_basefill_019'], 'func': tcl_base_universe_d2_027_tcl_basefill_019}


def tcl_base_universe_d2_028_tcl_basefill_023(tcl_basefill_023):
    return _base_universe_d2(tcl_basefill_023, 28)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_028_tcl_basefill_023'] = {'inputs': ['tcl_basefill_023'], 'func': tcl_base_universe_d2_028_tcl_basefill_023}


def tcl_base_universe_d2_029_tcl_basefill_025(tcl_basefill_025):
    return _base_universe_d2(tcl_basefill_025, 29)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_029_tcl_basefill_025'] = {'inputs': ['tcl_basefill_025'], 'func': tcl_base_universe_d2_029_tcl_basefill_025}


def tcl_base_universe_d2_030_tcl_basefill_029(tcl_basefill_029):
    return _base_universe_d2(tcl_basefill_029, 30)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_030_tcl_basefill_029'] = {'inputs': ['tcl_basefill_029'], 'func': tcl_base_universe_d2_030_tcl_basefill_029}


def tcl_base_universe_d2_031_tcl_basefill_031(tcl_basefill_031):
    return _base_universe_d2(tcl_basefill_031, 31)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_031_tcl_basefill_031'] = {'inputs': ['tcl_basefill_031'], 'func': tcl_base_universe_d2_031_tcl_basefill_031}


def tcl_base_universe_d2_032_tcl_basefill_032(tcl_basefill_032):
    return _base_universe_d2(tcl_basefill_032, 32)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_032_tcl_basefill_032'] = {'inputs': ['tcl_basefill_032'], 'func': tcl_base_universe_d2_032_tcl_basefill_032}


def tcl_base_universe_d2_033_tcl_basefill_033(tcl_basefill_033):
    return _base_universe_d2(tcl_basefill_033, 33)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_033_tcl_basefill_033'] = {'inputs': ['tcl_basefill_033'], 'func': tcl_base_universe_d2_033_tcl_basefill_033}


def tcl_base_universe_d2_034_tcl_basefill_034(tcl_basefill_034):
    return _base_universe_d2(tcl_basefill_034, 34)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_034_tcl_basefill_034'] = {'inputs': ['tcl_basefill_034'], 'func': tcl_base_universe_d2_034_tcl_basefill_034}


def tcl_base_universe_d2_035_tcl_basefill_035(tcl_basefill_035):
    return _base_universe_d2(tcl_basefill_035, 35)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_035_tcl_basefill_035'] = {'inputs': ['tcl_basefill_035'], 'func': tcl_base_universe_d2_035_tcl_basefill_035}


def tcl_base_universe_d2_036_tcl_basefill_036(tcl_basefill_036):
    return _base_universe_d2(tcl_basefill_036, 36)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_036_tcl_basefill_036'] = {'inputs': ['tcl_basefill_036'], 'func': tcl_base_universe_d2_036_tcl_basefill_036}


def tcl_base_universe_d2_037_tcl_basefill_037(tcl_basefill_037):
    return _base_universe_d2(tcl_basefill_037, 37)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_037_tcl_basefill_037'] = {'inputs': ['tcl_basefill_037'], 'func': tcl_base_universe_d2_037_tcl_basefill_037}


def tcl_base_universe_d2_038_tcl_basefill_038(tcl_basefill_038):
    return _base_universe_d2(tcl_basefill_038, 38)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_038_tcl_basefill_038'] = {'inputs': ['tcl_basefill_038'], 'func': tcl_base_universe_d2_038_tcl_basefill_038}


def tcl_base_universe_d2_039_tcl_basefill_039(tcl_basefill_039):
    return _base_universe_d2(tcl_basefill_039, 39)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_039_tcl_basefill_039'] = {'inputs': ['tcl_basefill_039'], 'func': tcl_base_universe_d2_039_tcl_basefill_039}


def tcl_base_universe_d2_040_tcl_basefill_040(tcl_basefill_040):
    return _base_universe_d2(tcl_basefill_040, 40)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_040_tcl_basefill_040'] = {'inputs': ['tcl_basefill_040'], 'func': tcl_base_universe_d2_040_tcl_basefill_040}


def tcl_base_universe_d2_041_tcl_basefill_041(tcl_basefill_041):
    return _base_universe_d2(tcl_basefill_041, 41)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_041_tcl_basefill_041'] = {'inputs': ['tcl_basefill_041'], 'func': tcl_base_universe_d2_041_tcl_basefill_041}


def tcl_base_universe_d2_042_tcl_basefill_042(tcl_basefill_042):
    return _base_universe_d2(tcl_basefill_042, 42)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_042_tcl_basefill_042'] = {'inputs': ['tcl_basefill_042'], 'func': tcl_base_universe_d2_042_tcl_basefill_042}


def tcl_base_universe_d2_043_tcl_basefill_043(tcl_basefill_043):
    return _base_universe_d2(tcl_basefill_043, 43)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_043_tcl_basefill_043'] = {'inputs': ['tcl_basefill_043'], 'func': tcl_base_universe_d2_043_tcl_basefill_043}


def tcl_base_universe_d2_044_tcl_basefill_044(tcl_basefill_044):
    return _base_universe_d2(tcl_basefill_044, 44)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_044_tcl_basefill_044'] = {'inputs': ['tcl_basefill_044'], 'func': tcl_base_universe_d2_044_tcl_basefill_044}


def tcl_base_universe_d2_045_tcl_basefill_045(tcl_basefill_045):
    return _base_universe_d2(tcl_basefill_045, 45)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_045_tcl_basefill_045'] = {'inputs': ['tcl_basefill_045'], 'func': tcl_base_universe_d2_045_tcl_basefill_045}


def tcl_base_universe_d2_046_tcl_basefill_046(tcl_basefill_046):
    return _base_universe_d2(tcl_basefill_046, 46)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_046_tcl_basefill_046'] = {'inputs': ['tcl_basefill_046'], 'func': tcl_base_universe_d2_046_tcl_basefill_046}


def tcl_base_universe_d2_047_tcl_basefill_047(tcl_basefill_047):
    return _base_universe_d2(tcl_basefill_047, 47)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_047_tcl_basefill_047'] = {'inputs': ['tcl_basefill_047'], 'func': tcl_base_universe_d2_047_tcl_basefill_047}


def tcl_base_universe_d2_048_tcl_basefill_048(tcl_basefill_048):
    return _base_universe_d2(tcl_basefill_048, 48)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_048_tcl_basefill_048'] = {'inputs': ['tcl_basefill_048'], 'func': tcl_base_universe_d2_048_tcl_basefill_048}


def tcl_base_universe_d2_049_tcl_basefill_049(tcl_basefill_049):
    return _base_universe_d2(tcl_basefill_049, 49)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_049_tcl_basefill_049'] = {'inputs': ['tcl_basefill_049'], 'func': tcl_base_universe_d2_049_tcl_basefill_049}


def tcl_base_universe_d2_050_tcl_basefill_050(tcl_basefill_050):
    return _base_universe_d2(tcl_basefill_050, 50)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_050_tcl_basefill_050'] = {'inputs': ['tcl_basefill_050'], 'func': tcl_base_universe_d2_050_tcl_basefill_050}


def tcl_base_universe_d2_051_tcl_basefill_051(tcl_basefill_051):
    return _base_universe_d2(tcl_basefill_051, 51)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_051_tcl_basefill_051'] = {'inputs': ['tcl_basefill_051'], 'func': tcl_base_universe_d2_051_tcl_basefill_051}


def tcl_base_universe_d2_052_tcl_basefill_052(tcl_basefill_052):
    return _base_universe_d2(tcl_basefill_052, 52)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_052_tcl_basefill_052'] = {'inputs': ['tcl_basefill_052'], 'func': tcl_base_universe_d2_052_tcl_basefill_052}


def tcl_base_universe_d2_053_tcl_basefill_053(tcl_basefill_053):
    return _base_universe_d2(tcl_basefill_053, 53)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_053_tcl_basefill_053'] = {'inputs': ['tcl_basefill_053'], 'func': tcl_base_universe_d2_053_tcl_basefill_053}


def tcl_base_universe_d2_054_tcl_basefill_054(tcl_basefill_054):
    return _base_universe_d2(tcl_basefill_054, 54)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_054_tcl_basefill_054'] = {'inputs': ['tcl_basefill_054'], 'func': tcl_base_universe_d2_054_tcl_basefill_054}


def tcl_base_universe_d2_055_tcl_basefill_055(tcl_basefill_055):
    return _base_universe_d2(tcl_basefill_055, 55)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_055_tcl_basefill_055'] = {'inputs': ['tcl_basefill_055'], 'func': tcl_base_universe_d2_055_tcl_basefill_055}


def tcl_base_universe_d2_056_tcl_basefill_056(tcl_basefill_056):
    return _base_universe_d2(tcl_basefill_056, 56)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_056_tcl_basefill_056'] = {'inputs': ['tcl_basefill_056'], 'func': tcl_base_universe_d2_056_tcl_basefill_056}


def tcl_base_universe_d2_057_tcl_basefill_057(tcl_basefill_057):
    return _base_universe_d2(tcl_basefill_057, 57)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_057_tcl_basefill_057'] = {'inputs': ['tcl_basefill_057'], 'func': tcl_base_universe_d2_057_tcl_basefill_057}


def tcl_base_universe_d2_058_tcl_basefill_058(tcl_basefill_058):
    return _base_universe_d2(tcl_basefill_058, 58)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_058_tcl_basefill_058'] = {'inputs': ['tcl_basefill_058'], 'func': tcl_base_universe_d2_058_tcl_basefill_058}


def tcl_base_universe_d2_059_tcl_basefill_059(tcl_basefill_059):
    return _base_universe_d2(tcl_basefill_059, 59)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_059_tcl_basefill_059'] = {'inputs': ['tcl_basefill_059'], 'func': tcl_base_universe_d2_059_tcl_basefill_059}


def tcl_base_universe_d2_060_tcl_basefill_060(tcl_basefill_060):
    return _base_universe_d2(tcl_basefill_060, 60)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_060_tcl_basefill_060'] = {'inputs': ['tcl_basefill_060'], 'func': tcl_base_universe_d2_060_tcl_basefill_060}


def tcl_base_universe_d2_061_tcl_basefill_061(tcl_basefill_061):
    return _base_universe_d2(tcl_basefill_061, 61)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_061_tcl_basefill_061'] = {'inputs': ['tcl_basefill_061'], 'func': tcl_base_universe_d2_061_tcl_basefill_061}


def tcl_base_universe_d2_062_tcl_basefill_062(tcl_basefill_062):
    return _base_universe_d2(tcl_basefill_062, 62)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_062_tcl_basefill_062'] = {'inputs': ['tcl_basefill_062'], 'func': tcl_base_universe_d2_062_tcl_basefill_062}


def tcl_base_universe_d2_063_tcl_basefill_063(tcl_basefill_063):
    return _base_universe_d2(tcl_basefill_063, 63)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_063_tcl_basefill_063'] = {'inputs': ['tcl_basefill_063'], 'func': tcl_base_universe_d2_063_tcl_basefill_063}


def tcl_base_universe_d2_064_tcl_basefill_064(tcl_basefill_064):
    return _base_universe_d2(tcl_basefill_064, 64)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_064_tcl_basefill_064'] = {'inputs': ['tcl_basefill_064'], 'func': tcl_base_universe_d2_064_tcl_basefill_064}


def tcl_base_universe_d2_065_tcl_basefill_065(tcl_basefill_065):
    return _base_universe_d2(tcl_basefill_065, 65)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_065_tcl_basefill_065'] = {'inputs': ['tcl_basefill_065'], 'func': tcl_base_universe_d2_065_tcl_basefill_065}


def tcl_base_universe_d2_066_tcl_basefill_066(tcl_basefill_066):
    return _base_universe_d2(tcl_basefill_066, 66)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_066_tcl_basefill_066'] = {'inputs': ['tcl_basefill_066'], 'func': tcl_base_universe_d2_066_tcl_basefill_066}


def tcl_base_universe_d2_067_tcl_basefill_067(tcl_basefill_067):
    return _base_universe_d2(tcl_basefill_067, 67)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_067_tcl_basefill_067'] = {'inputs': ['tcl_basefill_067'], 'func': tcl_base_universe_d2_067_tcl_basefill_067}


def tcl_base_universe_d2_068_tcl_basefill_068(tcl_basefill_068):
    return _base_universe_d2(tcl_basefill_068, 68)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_068_tcl_basefill_068'] = {'inputs': ['tcl_basefill_068'], 'func': tcl_base_universe_d2_068_tcl_basefill_068}


def tcl_base_universe_d2_069_tcl_basefill_069(tcl_basefill_069):
    return _base_universe_d2(tcl_basefill_069, 69)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_069_tcl_basefill_069'] = {'inputs': ['tcl_basefill_069'], 'func': tcl_base_universe_d2_069_tcl_basefill_069}


def tcl_base_universe_d2_070_tcl_basefill_070(tcl_basefill_070):
    return _base_universe_d2(tcl_basefill_070, 70)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_070_tcl_basefill_070'] = {'inputs': ['tcl_basefill_070'], 'func': tcl_base_universe_d2_070_tcl_basefill_070}


def tcl_base_universe_d2_071_tcl_basefill_071(tcl_basefill_071):
    return _base_universe_d2(tcl_basefill_071, 71)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_071_tcl_basefill_071'] = {'inputs': ['tcl_basefill_071'], 'func': tcl_base_universe_d2_071_tcl_basefill_071}


def tcl_base_universe_d2_072_tcl_basefill_072(tcl_basefill_072):
    return _base_universe_d2(tcl_basefill_072, 72)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_072_tcl_basefill_072'] = {'inputs': ['tcl_basefill_072'], 'func': tcl_base_universe_d2_072_tcl_basefill_072}


def tcl_base_universe_d2_073_tcl_basefill_073(tcl_basefill_073):
    return _base_universe_d2(tcl_basefill_073, 73)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_073_tcl_basefill_073'] = {'inputs': ['tcl_basefill_073'], 'func': tcl_base_universe_d2_073_tcl_basefill_073}


def tcl_base_universe_d2_074_tcl_basefill_074(tcl_basefill_074):
    return _base_universe_d2(tcl_basefill_074, 74)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_074_tcl_basefill_074'] = {'inputs': ['tcl_basefill_074'], 'func': tcl_base_universe_d2_074_tcl_basefill_074}


def tcl_base_universe_d2_075_tcl_basefill_075(tcl_basefill_075):
    return _base_universe_d2(tcl_basefill_075, 75)
TCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['tcl_base_universe_d2_075_tcl_basefill_075'] = {'inputs': ['tcl_basefill_075'], 'func': tcl_base_universe_d2_075_tcl_basefill_075}
