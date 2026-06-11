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



def ptt_151_ptt_001_drawdown_from_high_5_001_roc_1(ptt_001_drawdown_from_high_5_001):
    feature = _s(ptt_001_drawdown_from_high_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def ptt_152_ptt_007_drawdown_from_high_126_007_roc_5(ptt_007_drawdown_from_high_126_007):
    feature = _s(ptt_007_drawdown_from_high_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def ptt_153_ptt_013_drawdown_from_high_1008_013_roc_42(ptt_013_drawdown_from_high_1008_013):
    feature = _s(ptt_013_drawdown_from_high_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def ptt_154_ptt_019_drawdown_from_high_42_019_roc_126(ptt_019_drawdown_from_high_42_019):
    feature = _s(ptt_019_drawdown_from_high_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def ptt_155_ptt_025_drawdown_from_high_378_025_roc_378(ptt_025_drawdown_from_high_378_025):
    feature = _s(ptt_025_drawdown_from_high_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















PEAK_TO_TROUGH_REGISTRY_2ND_DERIVATIVES = {
    'ptt_151_ptt_001_drawdown_from_high_5_001_roc_1': {'inputs': ['ptt_001_drawdown_from_high_5_001'], 'func': ptt_151_ptt_001_drawdown_from_high_5_001_roc_1},
    'ptt_152_ptt_007_drawdown_from_high_126_007_roc_5': {'inputs': ['ptt_007_drawdown_from_high_126_007'], 'func': ptt_152_ptt_007_drawdown_from_high_126_007_roc_5},
    'ptt_153_ptt_013_drawdown_from_high_1008_013_roc_42': {'inputs': ['ptt_013_drawdown_from_high_1008_013'], 'func': ptt_153_ptt_013_drawdown_from_high_1008_013_roc_42},
    'ptt_154_ptt_019_drawdown_from_high_42_019_roc_126': {'inputs': ['ptt_019_drawdown_from_high_42_019'], 'func': ptt_154_ptt_019_drawdown_from_high_42_019_roc_126},
    'ptt_155_ptt_025_drawdown_from_high_378_025_roc_378': {'inputs': ['ptt_025_drawdown_from_high_378_025'], 'func': ptt_155_ptt_025_drawdown_from_high_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def ptt_replacement_d2_001(ptt_replacement_001):
    feature = _clean(ptt_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_001'] = {'inputs': ['ptt_replacement_001'], 'func': ptt_replacement_d2_001}


def ptt_replacement_d2_002(ptt_replacement_002):
    feature = _clean(ptt_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_002'] = {'inputs': ['ptt_replacement_002'], 'func': ptt_replacement_d2_002}


def ptt_replacement_d2_003(ptt_replacement_003):
    feature = _clean(ptt_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_003'] = {'inputs': ['ptt_replacement_003'], 'func': ptt_replacement_d2_003}


def ptt_replacement_d2_004(ptt_replacement_004):
    feature = _clean(ptt_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_004'] = {'inputs': ['ptt_replacement_004'], 'func': ptt_replacement_d2_004}


def ptt_replacement_d2_005(ptt_replacement_005):
    feature = _clean(ptt_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_005'] = {'inputs': ['ptt_replacement_005'], 'func': ptt_replacement_d2_005}


def ptt_replacement_d2_006(ptt_replacement_006):
    feature = _clean(ptt_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_006'] = {'inputs': ['ptt_replacement_006'], 'func': ptt_replacement_d2_006}


def ptt_replacement_d2_007(ptt_replacement_007):
    feature = _clean(ptt_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_007'] = {'inputs': ['ptt_replacement_007'], 'func': ptt_replacement_d2_007}


def ptt_replacement_d2_008(ptt_replacement_008):
    feature = _clean(ptt_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_008'] = {'inputs': ['ptt_replacement_008'], 'func': ptt_replacement_d2_008}


def ptt_replacement_d2_009(ptt_replacement_009):
    feature = _clean(ptt_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_009'] = {'inputs': ['ptt_replacement_009'], 'func': ptt_replacement_d2_009}


def ptt_replacement_d2_010(ptt_replacement_010):
    feature = _clean(ptt_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_010'] = {'inputs': ['ptt_replacement_010'], 'func': ptt_replacement_d2_010}


def ptt_replacement_d2_011(ptt_replacement_011):
    feature = _clean(ptt_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_011'] = {'inputs': ['ptt_replacement_011'], 'func': ptt_replacement_d2_011}


def ptt_replacement_d2_012(ptt_replacement_012):
    feature = _clean(ptt_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_012'] = {'inputs': ['ptt_replacement_012'], 'func': ptt_replacement_d2_012}


def ptt_replacement_d2_013(ptt_replacement_013):
    feature = _clean(ptt_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_013'] = {'inputs': ['ptt_replacement_013'], 'func': ptt_replacement_d2_013}


def ptt_replacement_d2_014(ptt_replacement_014):
    feature = _clean(ptt_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_014'] = {'inputs': ['ptt_replacement_014'], 'func': ptt_replacement_d2_014}


def ptt_replacement_d2_015(ptt_replacement_015):
    feature = _clean(ptt_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_015'] = {'inputs': ['ptt_replacement_015'], 'func': ptt_replacement_d2_015}


def ptt_replacement_d2_016(ptt_replacement_016):
    feature = _clean(ptt_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_016'] = {'inputs': ['ptt_replacement_016'], 'func': ptt_replacement_d2_016}


def ptt_replacement_d2_017(ptt_replacement_017):
    feature = _clean(ptt_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_017'] = {'inputs': ['ptt_replacement_017'], 'func': ptt_replacement_d2_017}


def ptt_replacement_d2_018(ptt_replacement_018):
    feature = _clean(ptt_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_018'] = {'inputs': ['ptt_replacement_018'], 'func': ptt_replacement_d2_018}


def ptt_replacement_d2_019(ptt_replacement_019):
    feature = _clean(ptt_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_019'] = {'inputs': ['ptt_replacement_019'], 'func': ptt_replacement_d2_019}


def ptt_replacement_d2_020(ptt_replacement_020):
    feature = _clean(ptt_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_020'] = {'inputs': ['ptt_replacement_020'], 'func': ptt_replacement_d2_020}


def ptt_replacement_d2_021(ptt_replacement_021):
    feature = _clean(ptt_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_021'] = {'inputs': ['ptt_replacement_021'], 'func': ptt_replacement_d2_021}


def ptt_replacement_d2_022(ptt_replacement_022):
    feature = _clean(ptt_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_022'] = {'inputs': ['ptt_replacement_022'], 'func': ptt_replacement_d2_022}


def ptt_replacement_d2_023(ptt_replacement_023):
    feature = _clean(ptt_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_023'] = {'inputs': ['ptt_replacement_023'], 'func': ptt_replacement_d2_023}


def ptt_replacement_d2_024(ptt_replacement_024):
    feature = _clean(ptt_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_024'] = {'inputs': ['ptt_replacement_024'], 'func': ptt_replacement_d2_024}


def ptt_replacement_d2_025(ptt_replacement_025):
    feature = _clean(ptt_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_025'] = {'inputs': ['ptt_replacement_025'], 'func': ptt_replacement_d2_025}


def ptt_replacement_d2_026(ptt_replacement_026):
    feature = _clean(ptt_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_026'] = {'inputs': ['ptt_replacement_026'], 'func': ptt_replacement_d2_026}


def ptt_replacement_d2_027(ptt_replacement_027):
    feature = _clean(ptt_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_027'] = {'inputs': ['ptt_replacement_027'], 'func': ptt_replacement_d2_027}


def ptt_replacement_d2_028(ptt_replacement_028):
    feature = _clean(ptt_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_028'] = {'inputs': ['ptt_replacement_028'], 'func': ptt_replacement_d2_028}


def ptt_replacement_d2_029(ptt_replacement_029):
    feature = _clean(ptt_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_029'] = {'inputs': ['ptt_replacement_029'], 'func': ptt_replacement_d2_029}


def ptt_replacement_d2_030(ptt_replacement_030):
    feature = _clean(ptt_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_030'] = {'inputs': ['ptt_replacement_030'], 'func': ptt_replacement_d2_030}


def ptt_replacement_d2_031(ptt_replacement_031):
    feature = _clean(ptt_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_031'] = {'inputs': ['ptt_replacement_031'], 'func': ptt_replacement_d2_031}


def ptt_replacement_d2_032(ptt_replacement_032):
    feature = _clean(ptt_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_032'] = {'inputs': ['ptt_replacement_032'], 'func': ptt_replacement_d2_032}


def ptt_replacement_d2_033(ptt_replacement_033):
    feature = _clean(ptt_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_033'] = {'inputs': ['ptt_replacement_033'], 'func': ptt_replacement_d2_033}


def ptt_replacement_d2_034(ptt_replacement_034):
    feature = _clean(ptt_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_034'] = {'inputs': ['ptt_replacement_034'], 'func': ptt_replacement_d2_034}


def ptt_replacement_d2_035(ptt_replacement_035):
    feature = _clean(ptt_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_035'] = {'inputs': ['ptt_replacement_035'], 'func': ptt_replacement_d2_035}


def ptt_replacement_d2_036(ptt_replacement_036):
    feature = _clean(ptt_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_036'] = {'inputs': ['ptt_replacement_036'], 'func': ptt_replacement_d2_036}


def ptt_replacement_d2_037(ptt_replacement_037):
    feature = _clean(ptt_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_037'] = {'inputs': ['ptt_replacement_037'], 'func': ptt_replacement_d2_037}


def ptt_replacement_d2_038(ptt_replacement_038):
    feature = _clean(ptt_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_038'] = {'inputs': ['ptt_replacement_038'], 'func': ptt_replacement_d2_038}


def ptt_replacement_d2_039(ptt_replacement_039):
    feature = _clean(ptt_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_039'] = {'inputs': ['ptt_replacement_039'], 'func': ptt_replacement_d2_039}


def ptt_replacement_d2_040(ptt_replacement_040):
    feature = _clean(ptt_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_040'] = {'inputs': ['ptt_replacement_040'], 'func': ptt_replacement_d2_040}


def ptt_replacement_d2_041(ptt_replacement_041):
    feature = _clean(ptt_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_041'] = {'inputs': ['ptt_replacement_041'], 'func': ptt_replacement_d2_041}


def ptt_replacement_d2_042(ptt_replacement_042):
    feature = _clean(ptt_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_042'] = {'inputs': ['ptt_replacement_042'], 'func': ptt_replacement_d2_042}


def ptt_replacement_d2_043(ptt_replacement_043):
    feature = _clean(ptt_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_043'] = {'inputs': ['ptt_replacement_043'], 'func': ptt_replacement_d2_043}


def ptt_replacement_d2_044(ptt_replacement_044):
    feature = _clean(ptt_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_044'] = {'inputs': ['ptt_replacement_044'], 'func': ptt_replacement_d2_044}


def ptt_replacement_d2_045(ptt_replacement_045):
    feature = _clean(ptt_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_045'] = {'inputs': ['ptt_replacement_045'], 'func': ptt_replacement_d2_045}


def ptt_replacement_d2_046(ptt_replacement_046):
    feature = _clean(ptt_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_046'] = {'inputs': ['ptt_replacement_046'], 'func': ptt_replacement_d2_046}


def ptt_replacement_d2_047(ptt_replacement_047):
    feature = _clean(ptt_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_047'] = {'inputs': ['ptt_replacement_047'], 'func': ptt_replacement_d2_047}


def ptt_replacement_d2_048(ptt_replacement_048):
    feature = _clean(ptt_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_048'] = {'inputs': ['ptt_replacement_048'], 'func': ptt_replacement_d2_048}


def ptt_replacement_d2_049(ptt_replacement_049):
    feature = _clean(ptt_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_049'] = {'inputs': ['ptt_replacement_049'], 'func': ptt_replacement_d2_049}


def ptt_replacement_d2_050(ptt_replacement_050):
    feature = _clean(ptt_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_050'] = {'inputs': ['ptt_replacement_050'], 'func': ptt_replacement_d2_050}


def ptt_replacement_d2_051(ptt_replacement_051):
    feature = _clean(ptt_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_051'] = {'inputs': ['ptt_replacement_051'], 'func': ptt_replacement_d2_051}


def ptt_replacement_d2_052(ptt_replacement_052):
    feature = _clean(ptt_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_052'] = {'inputs': ['ptt_replacement_052'], 'func': ptt_replacement_d2_052}


def ptt_replacement_d2_053(ptt_replacement_053):
    feature = _clean(ptt_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_053'] = {'inputs': ['ptt_replacement_053'], 'func': ptt_replacement_d2_053}


def ptt_replacement_d2_054(ptt_replacement_054):
    feature = _clean(ptt_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_054'] = {'inputs': ['ptt_replacement_054'], 'func': ptt_replacement_d2_054}


def ptt_replacement_d2_055(ptt_replacement_055):
    feature = _clean(ptt_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_055'] = {'inputs': ['ptt_replacement_055'], 'func': ptt_replacement_d2_055}


def ptt_replacement_d2_056(ptt_replacement_056):
    feature = _clean(ptt_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_056'] = {'inputs': ['ptt_replacement_056'], 'func': ptt_replacement_d2_056}


def ptt_replacement_d2_057(ptt_replacement_057):
    feature = _clean(ptt_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_057'] = {'inputs': ['ptt_replacement_057'], 'func': ptt_replacement_d2_057}


def ptt_replacement_d2_058(ptt_replacement_058):
    feature = _clean(ptt_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_058'] = {'inputs': ['ptt_replacement_058'], 'func': ptt_replacement_d2_058}


def ptt_replacement_d2_059(ptt_replacement_059):
    feature = _clean(ptt_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_059'] = {'inputs': ['ptt_replacement_059'], 'func': ptt_replacement_d2_059}


def ptt_replacement_d2_060(ptt_replacement_060):
    feature = _clean(ptt_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_060'] = {'inputs': ['ptt_replacement_060'], 'func': ptt_replacement_d2_060}


def ptt_replacement_d2_061(ptt_replacement_061):
    feature = _clean(ptt_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_061'] = {'inputs': ['ptt_replacement_061'], 'func': ptt_replacement_d2_061}


def ptt_replacement_d2_062(ptt_replacement_062):
    feature = _clean(ptt_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_062'] = {'inputs': ['ptt_replacement_062'], 'func': ptt_replacement_d2_062}


def ptt_replacement_d2_063(ptt_replacement_063):
    feature = _clean(ptt_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_063'] = {'inputs': ['ptt_replacement_063'], 'func': ptt_replacement_d2_063}


def ptt_replacement_d2_064(ptt_replacement_064):
    feature = _clean(ptt_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_064'] = {'inputs': ['ptt_replacement_064'], 'func': ptt_replacement_d2_064}


def ptt_replacement_d2_065(ptt_replacement_065):
    feature = _clean(ptt_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_065'] = {'inputs': ['ptt_replacement_065'], 'func': ptt_replacement_d2_065}


def ptt_replacement_d2_066(ptt_replacement_066):
    feature = _clean(ptt_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_066'] = {'inputs': ['ptt_replacement_066'], 'func': ptt_replacement_d2_066}


def ptt_replacement_d2_067(ptt_replacement_067):
    feature = _clean(ptt_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_067'] = {'inputs': ['ptt_replacement_067'], 'func': ptt_replacement_d2_067}


def ptt_replacement_d2_068(ptt_replacement_068):
    feature = _clean(ptt_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_068'] = {'inputs': ['ptt_replacement_068'], 'func': ptt_replacement_d2_068}


def ptt_replacement_d2_069(ptt_replacement_069):
    feature = _clean(ptt_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_069'] = {'inputs': ['ptt_replacement_069'], 'func': ptt_replacement_d2_069}


def ptt_replacement_d2_070(ptt_replacement_070):
    feature = _clean(ptt_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_070'] = {'inputs': ['ptt_replacement_070'], 'func': ptt_replacement_d2_070}


def ptt_replacement_d2_071(ptt_replacement_071):
    feature = _clean(ptt_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_071'] = {'inputs': ['ptt_replacement_071'], 'func': ptt_replacement_d2_071}


def ptt_replacement_d2_072(ptt_replacement_072):
    feature = _clean(ptt_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_072'] = {'inputs': ['ptt_replacement_072'], 'func': ptt_replacement_d2_072}


def ptt_replacement_d2_073(ptt_replacement_073):
    feature = _clean(ptt_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_073'] = {'inputs': ['ptt_replacement_073'], 'func': ptt_replacement_d2_073}


def ptt_replacement_d2_074(ptt_replacement_074):
    feature = _clean(ptt_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_074'] = {'inputs': ['ptt_replacement_074'], 'func': ptt_replacement_d2_074}


def ptt_replacement_d2_075(ptt_replacement_075):
    feature = _clean(ptt_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_075'] = {'inputs': ['ptt_replacement_075'], 'func': ptt_replacement_d2_075}


def ptt_replacement_d2_076(ptt_replacement_076):
    feature = _clean(ptt_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_076'] = {'inputs': ['ptt_replacement_076'], 'func': ptt_replacement_d2_076}


def ptt_replacement_d2_077(ptt_replacement_077):
    feature = _clean(ptt_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_077'] = {'inputs': ['ptt_replacement_077'], 'func': ptt_replacement_d2_077}


def ptt_replacement_d2_078(ptt_replacement_078):
    feature = _clean(ptt_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_078'] = {'inputs': ['ptt_replacement_078'], 'func': ptt_replacement_d2_078}


def ptt_replacement_d2_079(ptt_replacement_079):
    feature = _clean(ptt_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_079'] = {'inputs': ['ptt_replacement_079'], 'func': ptt_replacement_d2_079}


def ptt_replacement_d2_080(ptt_replacement_080):
    feature = _clean(ptt_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_080'] = {'inputs': ['ptt_replacement_080'], 'func': ptt_replacement_d2_080}


def ptt_replacement_d2_081(ptt_replacement_081):
    feature = _clean(ptt_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_081'] = {'inputs': ['ptt_replacement_081'], 'func': ptt_replacement_d2_081}


def ptt_replacement_d2_082(ptt_replacement_082):
    feature = _clean(ptt_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_082'] = {'inputs': ['ptt_replacement_082'], 'func': ptt_replacement_d2_082}


def ptt_replacement_d2_083(ptt_replacement_083):
    feature = _clean(ptt_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_083'] = {'inputs': ['ptt_replacement_083'], 'func': ptt_replacement_d2_083}


def ptt_replacement_d2_084(ptt_replacement_084):
    feature = _clean(ptt_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_084'] = {'inputs': ['ptt_replacement_084'], 'func': ptt_replacement_d2_084}


def ptt_replacement_d2_085(ptt_replacement_085):
    feature = _clean(ptt_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_085'] = {'inputs': ['ptt_replacement_085'], 'func': ptt_replacement_d2_085}


def ptt_replacement_d2_086(ptt_replacement_086):
    feature = _clean(ptt_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_086'] = {'inputs': ['ptt_replacement_086'], 'func': ptt_replacement_d2_086}


def ptt_replacement_d2_087(ptt_replacement_087):
    feature = _clean(ptt_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_087'] = {'inputs': ['ptt_replacement_087'], 'func': ptt_replacement_d2_087}


def ptt_replacement_d2_088(ptt_replacement_088):
    feature = _clean(ptt_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_088'] = {'inputs': ['ptt_replacement_088'], 'func': ptt_replacement_d2_088}


def ptt_replacement_d2_089(ptt_replacement_089):
    feature = _clean(ptt_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_089'] = {'inputs': ['ptt_replacement_089'], 'func': ptt_replacement_d2_089}


def ptt_replacement_d2_090(ptt_replacement_090):
    feature = _clean(ptt_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_090'] = {'inputs': ['ptt_replacement_090'], 'func': ptt_replacement_d2_090}


def ptt_replacement_d2_091(ptt_replacement_091):
    feature = _clean(ptt_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_091'] = {'inputs': ['ptt_replacement_091'], 'func': ptt_replacement_d2_091}


def ptt_replacement_d2_092(ptt_replacement_092):
    feature = _clean(ptt_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_092'] = {'inputs': ['ptt_replacement_092'], 'func': ptt_replacement_d2_092}


def ptt_replacement_d2_093(ptt_replacement_093):
    feature = _clean(ptt_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_093'] = {'inputs': ['ptt_replacement_093'], 'func': ptt_replacement_d2_093}


def ptt_replacement_d2_094(ptt_replacement_094):
    feature = _clean(ptt_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_094'] = {'inputs': ['ptt_replacement_094'], 'func': ptt_replacement_d2_094}


def ptt_replacement_d2_095(ptt_replacement_095):
    feature = _clean(ptt_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_095'] = {'inputs': ['ptt_replacement_095'], 'func': ptt_replacement_d2_095}


def ptt_replacement_d2_096(ptt_replacement_096):
    feature = _clean(ptt_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_096'] = {'inputs': ['ptt_replacement_096'], 'func': ptt_replacement_d2_096}


def ptt_replacement_d2_097(ptt_replacement_097):
    feature = _clean(ptt_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_097'] = {'inputs': ['ptt_replacement_097'], 'func': ptt_replacement_d2_097}


def ptt_replacement_d2_098(ptt_replacement_098):
    feature = _clean(ptt_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_098'] = {'inputs': ['ptt_replacement_098'], 'func': ptt_replacement_d2_098}


def ptt_replacement_d2_099(ptt_replacement_099):
    feature = _clean(ptt_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_099'] = {'inputs': ['ptt_replacement_099'], 'func': ptt_replacement_d2_099}


def ptt_replacement_d2_100(ptt_replacement_100):
    feature = _clean(ptt_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_100'] = {'inputs': ['ptt_replacement_100'], 'func': ptt_replacement_d2_100}


def ptt_replacement_d2_101(ptt_replacement_101):
    feature = _clean(ptt_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_101'] = {'inputs': ['ptt_replacement_101'], 'func': ptt_replacement_d2_101}


def ptt_replacement_d2_102(ptt_replacement_102):
    feature = _clean(ptt_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_102'] = {'inputs': ['ptt_replacement_102'], 'func': ptt_replacement_d2_102}


def ptt_replacement_d2_103(ptt_replacement_103):
    feature = _clean(ptt_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_103'] = {'inputs': ['ptt_replacement_103'], 'func': ptt_replacement_d2_103}


def ptt_replacement_d2_104(ptt_replacement_104):
    feature = _clean(ptt_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_104'] = {'inputs': ['ptt_replacement_104'], 'func': ptt_replacement_d2_104}


def ptt_replacement_d2_105(ptt_replacement_105):
    feature = _clean(ptt_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_105'] = {'inputs': ['ptt_replacement_105'], 'func': ptt_replacement_d2_105}


def ptt_replacement_d2_106(ptt_replacement_106):
    feature = _clean(ptt_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_106'] = {'inputs': ['ptt_replacement_106'], 'func': ptt_replacement_d2_106}


def ptt_replacement_d2_107(ptt_replacement_107):
    feature = _clean(ptt_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_107'] = {'inputs': ['ptt_replacement_107'], 'func': ptt_replacement_d2_107}


def ptt_replacement_d2_108(ptt_replacement_108):
    feature = _clean(ptt_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_108'] = {'inputs': ['ptt_replacement_108'], 'func': ptt_replacement_d2_108}


def ptt_replacement_d2_109(ptt_replacement_109):
    feature = _clean(ptt_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_109'] = {'inputs': ['ptt_replacement_109'], 'func': ptt_replacement_d2_109}


def ptt_replacement_d2_110(ptt_replacement_110):
    feature = _clean(ptt_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_110'] = {'inputs': ['ptt_replacement_110'], 'func': ptt_replacement_d2_110}


def ptt_replacement_d2_111(ptt_replacement_111):
    feature = _clean(ptt_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_111'] = {'inputs': ['ptt_replacement_111'], 'func': ptt_replacement_d2_111}


def ptt_replacement_d2_112(ptt_replacement_112):
    feature = _clean(ptt_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_112'] = {'inputs': ['ptt_replacement_112'], 'func': ptt_replacement_d2_112}


def ptt_replacement_d2_113(ptt_replacement_113):
    feature = _clean(ptt_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_113'] = {'inputs': ['ptt_replacement_113'], 'func': ptt_replacement_d2_113}


def ptt_replacement_d2_114(ptt_replacement_114):
    feature = _clean(ptt_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_114'] = {'inputs': ['ptt_replacement_114'], 'func': ptt_replacement_d2_114}


def ptt_replacement_d2_115(ptt_replacement_115):
    feature = _clean(ptt_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_115'] = {'inputs': ['ptt_replacement_115'], 'func': ptt_replacement_d2_115}


def ptt_replacement_d2_116(ptt_replacement_116):
    feature = _clean(ptt_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_116'] = {'inputs': ['ptt_replacement_116'], 'func': ptt_replacement_d2_116}


def ptt_replacement_d2_117(ptt_replacement_117):
    feature = _clean(ptt_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_117'] = {'inputs': ['ptt_replacement_117'], 'func': ptt_replacement_d2_117}


def ptt_replacement_d2_118(ptt_replacement_118):
    feature = _clean(ptt_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_118'] = {'inputs': ['ptt_replacement_118'], 'func': ptt_replacement_d2_118}


def ptt_replacement_d2_119(ptt_replacement_119):
    feature = _clean(ptt_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_119'] = {'inputs': ['ptt_replacement_119'], 'func': ptt_replacement_d2_119}


def ptt_replacement_d2_120(ptt_replacement_120):
    feature = _clean(ptt_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_120'] = {'inputs': ['ptt_replacement_120'], 'func': ptt_replacement_d2_120}


def ptt_replacement_d2_121(ptt_replacement_121):
    feature = _clean(ptt_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_121'] = {'inputs': ['ptt_replacement_121'], 'func': ptt_replacement_d2_121}


def ptt_replacement_d2_122(ptt_replacement_122):
    feature = _clean(ptt_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_122'] = {'inputs': ['ptt_replacement_122'], 'func': ptt_replacement_d2_122}


def ptt_replacement_d2_123(ptt_replacement_123):
    feature = _clean(ptt_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_123'] = {'inputs': ['ptt_replacement_123'], 'func': ptt_replacement_d2_123}


def ptt_replacement_d2_124(ptt_replacement_124):
    feature = _clean(ptt_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_124'] = {'inputs': ['ptt_replacement_124'], 'func': ptt_replacement_d2_124}


def ptt_replacement_d2_125(ptt_replacement_125):
    feature = _clean(ptt_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_125'] = {'inputs': ['ptt_replacement_125'], 'func': ptt_replacement_d2_125}


def ptt_replacement_d2_126(ptt_replacement_126):
    feature = _clean(ptt_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_126'] = {'inputs': ['ptt_replacement_126'], 'func': ptt_replacement_d2_126}


def ptt_replacement_d2_127(ptt_replacement_127):
    feature = _clean(ptt_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_127'] = {'inputs': ['ptt_replacement_127'], 'func': ptt_replacement_d2_127}


def ptt_replacement_d2_128(ptt_replacement_128):
    feature = _clean(ptt_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_128'] = {'inputs': ['ptt_replacement_128'], 'func': ptt_replacement_d2_128}


def ptt_replacement_d2_129(ptt_replacement_129):
    feature = _clean(ptt_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_129'] = {'inputs': ['ptt_replacement_129'], 'func': ptt_replacement_d2_129}


def ptt_replacement_d2_130(ptt_replacement_130):
    feature = _clean(ptt_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_130'] = {'inputs': ['ptt_replacement_130'], 'func': ptt_replacement_d2_130}


def ptt_replacement_d2_131(ptt_replacement_131):
    feature = _clean(ptt_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_131'] = {'inputs': ['ptt_replacement_131'], 'func': ptt_replacement_d2_131}


def ptt_replacement_d2_132(ptt_replacement_132):
    feature = _clean(ptt_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_132'] = {'inputs': ['ptt_replacement_132'], 'func': ptt_replacement_d2_132}


def ptt_replacement_d2_133(ptt_replacement_133):
    feature = _clean(ptt_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_133'] = {'inputs': ['ptt_replacement_133'], 'func': ptt_replacement_d2_133}


def ptt_replacement_d2_134(ptt_replacement_134):
    feature = _clean(ptt_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_134'] = {'inputs': ['ptt_replacement_134'], 'func': ptt_replacement_d2_134}


def ptt_replacement_d2_135(ptt_replacement_135):
    feature = _clean(ptt_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_135'] = {'inputs': ['ptt_replacement_135'], 'func': ptt_replacement_d2_135}


def ptt_replacement_d2_136(ptt_replacement_136):
    feature = _clean(ptt_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_136'] = {'inputs': ['ptt_replacement_136'], 'func': ptt_replacement_d2_136}


def ptt_replacement_d2_137(ptt_replacement_137):
    feature = _clean(ptt_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_137'] = {'inputs': ['ptt_replacement_137'], 'func': ptt_replacement_d2_137}


def ptt_replacement_d2_138(ptt_replacement_138):
    feature = _clean(ptt_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_138'] = {'inputs': ['ptt_replacement_138'], 'func': ptt_replacement_d2_138}


def ptt_replacement_d2_139(ptt_replacement_139):
    feature = _clean(ptt_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_139'] = {'inputs': ['ptt_replacement_139'], 'func': ptt_replacement_d2_139}


def ptt_replacement_d2_140(ptt_replacement_140):
    feature = _clean(ptt_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_140'] = {'inputs': ['ptt_replacement_140'], 'func': ptt_replacement_d2_140}


def ptt_replacement_d2_141(ptt_replacement_141):
    feature = _clean(ptt_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_141'] = {'inputs': ['ptt_replacement_141'], 'func': ptt_replacement_d2_141}


def ptt_replacement_d2_142(ptt_replacement_142):
    feature = _clean(ptt_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_142'] = {'inputs': ['ptt_replacement_142'], 'func': ptt_replacement_d2_142}


def ptt_replacement_d2_143(ptt_replacement_143):
    feature = _clean(ptt_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_143'] = {'inputs': ['ptt_replacement_143'], 'func': ptt_replacement_d2_143}


def ptt_replacement_d2_144(ptt_replacement_144):
    feature = _clean(ptt_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_144'] = {'inputs': ['ptt_replacement_144'], 'func': ptt_replacement_d2_144}


def ptt_replacement_d2_145(ptt_replacement_145):
    feature = _clean(ptt_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_145'] = {'inputs': ['ptt_replacement_145'], 'func': ptt_replacement_d2_145}


def ptt_replacement_d2_146(ptt_replacement_146):
    feature = _clean(ptt_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_146'] = {'inputs': ['ptt_replacement_146'], 'func': ptt_replacement_d2_146}


def ptt_replacement_d2_147(ptt_replacement_147):
    feature = _clean(ptt_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_147'] = {'inputs': ['ptt_replacement_147'], 'func': ptt_replacement_d2_147}


def ptt_replacement_d2_148(ptt_replacement_148):
    feature = _clean(ptt_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_148'] = {'inputs': ['ptt_replacement_148'], 'func': ptt_replacement_d2_148}


def ptt_replacement_d2_149(ptt_replacement_149):
    feature = _clean(ptt_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_149'] = {'inputs': ['ptt_replacement_149'], 'func': ptt_replacement_d2_149}


def ptt_replacement_d2_150(ptt_replacement_150):
    feature = _clean(ptt_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_150'] = {'inputs': ['ptt_replacement_150'], 'func': ptt_replacement_d2_150}


def ptt_replacement_d2_151(ptt_replacement_151):
    feature = _clean(ptt_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_151'] = {'inputs': ['ptt_replacement_151'], 'func': ptt_replacement_d2_151}


def ptt_replacement_d2_152(ptt_replacement_152):
    feature = _clean(ptt_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_152'] = {'inputs': ['ptt_replacement_152'], 'func': ptt_replacement_d2_152}


def ptt_replacement_d2_153(ptt_replacement_153):
    feature = _clean(ptt_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_153'] = {'inputs': ['ptt_replacement_153'], 'func': ptt_replacement_d2_153}


def ptt_replacement_d2_154(ptt_replacement_154):
    feature = _clean(ptt_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_154'] = {'inputs': ['ptt_replacement_154'], 'func': ptt_replacement_d2_154}


def ptt_replacement_d2_155(ptt_replacement_155):
    feature = _clean(ptt_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_155'] = {'inputs': ['ptt_replacement_155'], 'func': ptt_replacement_d2_155}


def ptt_replacement_d2_156(ptt_replacement_156):
    feature = _clean(ptt_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_156'] = {'inputs': ['ptt_replacement_156'], 'func': ptt_replacement_d2_156}


def ptt_replacement_d2_157(ptt_replacement_157):
    feature = _clean(ptt_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_157'] = {'inputs': ['ptt_replacement_157'], 'func': ptt_replacement_d2_157}


def ptt_replacement_d2_158(ptt_replacement_158):
    feature = _clean(ptt_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_158'] = {'inputs': ['ptt_replacement_158'], 'func': ptt_replacement_d2_158}


def ptt_replacement_d2_159(ptt_replacement_159):
    feature = _clean(ptt_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_159'] = {'inputs': ['ptt_replacement_159'], 'func': ptt_replacement_d2_159}


def ptt_replacement_d2_160(ptt_replacement_160):
    feature = _clean(ptt_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_160'] = {'inputs': ['ptt_replacement_160'], 'func': ptt_replacement_d2_160}


def ptt_replacement_d2_161(ptt_replacement_161):
    feature = _clean(ptt_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_161'] = {'inputs': ['ptt_replacement_161'], 'func': ptt_replacement_d2_161}


def ptt_replacement_d2_162(ptt_replacement_162):
    feature = _clean(ptt_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_162'] = {'inputs': ['ptt_replacement_162'], 'func': ptt_replacement_d2_162}


def ptt_replacement_d2_163(ptt_replacement_163):
    feature = _clean(ptt_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_163'] = {'inputs': ['ptt_replacement_163'], 'func': ptt_replacement_d2_163}


def ptt_replacement_d2_164(ptt_replacement_164):
    feature = _clean(ptt_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_164'] = {'inputs': ['ptt_replacement_164'], 'func': ptt_replacement_d2_164}


def ptt_replacement_d2_165(ptt_replacement_165):
    feature = _clean(ptt_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_165'] = {'inputs': ['ptt_replacement_165'], 'func': ptt_replacement_d2_165}


def ptt_replacement_d2_166(ptt_replacement_166):
    feature = _clean(ptt_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_166'] = {'inputs': ['ptt_replacement_166'], 'func': ptt_replacement_d2_166}


def ptt_replacement_d2_167(ptt_replacement_167):
    feature = _clean(ptt_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_167'] = {'inputs': ['ptt_replacement_167'], 'func': ptt_replacement_d2_167}


def ptt_replacement_d2_168(ptt_replacement_168):
    feature = _clean(ptt_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_168'] = {'inputs': ['ptt_replacement_168'], 'func': ptt_replacement_d2_168}


def ptt_replacement_d2_169(ptt_replacement_169):
    feature = _clean(ptt_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_169'] = {'inputs': ['ptt_replacement_169'], 'func': ptt_replacement_d2_169}


def ptt_replacement_d2_170(ptt_replacement_170):
    feature = _clean(ptt_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
PTT_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['ptt_replacement_d2_170'] = {'inputs': ['ptt_replacement_170'], 'func': ptt_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ptt_base_universe_d2_001_ptt_002_low_distance_10_002(ptt_002_low_distance_10_002):
    return _base_universe_d2(ptt_002_low_distance_10_002, 1)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_001_ptt_002_low_distance_10_002'] = {'inputs': ['ptt_002_low_distance_10_002'], 'func': ptt_base_universe_d2_001_ptt_002_low_distance_10_002}


def ptt_base_universe_d2_002_ptt_003_underwater_area_21_003(ptt_003_underwater_area_21_003):
    return _base_universe_d2(ptt_003_underwater_area_21_003, 2)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_002_ptt_003_underwater_area_21_003'] = {'inputs': ['ptt_003_underwater_area_21_003'], 'func': ptt_base_universe_d2_002_ptt_003_underwater_area_21_003}


def ptt_base_universe_d2_003_ptt_006_lower_high_ratio_84_006(ptt_006_lower_high_ratio_84_006):
    return _base_universe_d2(ptt_006_lower_high_ratio_84_006, 3)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_003_ptt_006_lower_high_ratio_84_006'] = {'inputs': ['ptt_006_lower_high_ratio_84_006'], 'func': ptt_base_universe_d2_003_ptt_006_lower_high_ratio_84_006}


def ptt_base_universe_d2_004_ptt_008_low_distance_189_008(ptt_008_low_distance_189_008):
    return _base_universe_d2(ptt_008_low_distance_189_008, 4)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_004_ptt_008_low_distance_189_008'] = {'inputs': ['ptt_008_low_distance_189_008'], 'func': ptt_base_universe_d2_004_ptt_008_low_distance_189_008}


def ptt_base_universe_d2_005_ptt_009_underwater_area_252_009(ptt_009_underwater_area_252_009):
    return _base_universe_d2(ptt_009_underwater_area_252_009, 5)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_005_ptt_009_underwater_area_252_009'] = {'inputs': ['ptt_009_underwater_area_252_009'], 'func': ptt_base_universe_d2_005_ptt_009_underwater_area_252_009}


def ptt_base_universe_d2_006_ptt_012_lower_high_ratio_756_012(ptt_012_lower_high_ratio_756_012):
    return _base_universe_d2(ptt_012_lower_high_ratio_756_012, 6)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_006_ptt_012_lower_high_ratio_756_012'] = {'inputs': ['ptt_012_lower_high_ratio_756_012'], 'func': ptt_base_universe_d2_006_ptt_012_lower_high_ratio_756_012}


def ptt_base_universe_d2_007_ptt_014_low_distance_1260_014(ptt_014_low_distance_1260_014):
    return _base_universe_d2(ptt_014_low_distance_1260_014, 7)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_007_ptt_014_low_distance_1260_014'] = {'inputs': ['ptt_014_low_distance_1260_014'], 'func': ptt_base_universe_d2_007_ptt_014_low_distance_1260_014}


def ptt_base_universe_d2_008_ptt_015_underwater_area_1512_015(ptt_015_underwater_area_1512_015):
    return _base_universe_d2(ptt_015_underwater_area_1512_015, 8)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_008_ptt_015_underwater_area_1512_015'] = {'inputs': ['ptt_015_underwater_area_1512_015'], 'func': ptt_base_universe_d2_008_ptt_015_underwater_area_1512_015}


def ptt_base_universe_d2_009_ptt_018_lower_high_ratio_21_018(ptt_018_lower_high_ratio_21_018):
    return _base_universe_d2(ptt_018_lower_high_ratio_21_018, 9)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_009_ptt_018_lower_high_ratio_21_018'] = {'inputs': ['ptt_018_lower_high_ratio_21_018'], 'func': ptt_base_universe_d2_009_ptt_018_lower_high_ratio_21_018}


def ptt_base_universe_d2_010_ptt_020_low_distance_63_020(ptt_020_low_distance_63_020):
    return _base_universe_d2(ptt_020_low_distance_63_020, 10)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_010_ptt_020_low_distance_63_020'] = {'inputs': ['ptt_020_low_distance_63_020'], 'func': ptt_base_universe_d2_010_ptt_020_low_distance_63_020}


def ptt_base_universe_d2_011_ptt_021_underwater_area_84_021(ptt_021_underwater_area_84_021):
    return _base_universe_d2(ptt_021_underwater_area_84_021, 11)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_011_ptt_021_underwater_area_84_021'] = {'inputs': ['ptt_021_underwater_area_84_021'], 'func': ptt_base_universe_d2_011_ptt_021_underwater_area_84_021}


def ptt_base_universe_d2_012_ptt_024_lower_high_ratio_252_024(ptt_024_lower_high_ratio_252_024):
    return _base_universe_d2(ptt_024_lower_high_ratio_252_024, 12)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_012_ptt_024_lower_high_ratio_252_024'] = {'inputs': ['ptt_024_lower_high_ratio_252_024'], 'func': ptt_base_universe_d2_012_ptt_024_lower_high_ratio_252_024}


def ptt_base_universe_d2_013_ptt_026_low_distance_504_026(ptt_026_low_distance_504_026):
    return _base_universe_d2(ptt_026_low_distance_504_026, 13)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_013_ptt_026_low_distance_504_026'] = {'inputs': ['ptt_026_low_distance_504_026'], 'func': ptt_base_universe_d2_013_ptt_026_low_distance_504_026}


def ptt_base_universe_d2_014_ptt_027_underwater_area_756_027(ptt_027_underwater_area_756_027):
    return _base_universe_d2(ptt_027_underwater_area_756_027, 14)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_014_ptt_027_underwater_area_756_027'] = {'inputs': ['ptt_027_underwater_area_756_027'], 'func': ptt_base_universe_d2_014_ptt_027_underwater_area_756_027}


def ptt_base_universe_d2_015_ptt_030_lower_high_ratio_1512_030(ptt_030_lower_high_ratio_1512_030):
    return _base_universe_d2(ptt_030_lower_high_ratio_1512_030, 15)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_015_ptt_030_lower_high_ratio_1512_030'] = {'inputs': ['ptt_030_lower_high_ratio_1512_030'], 'func': ptt_base_universe_d2_015_ptt_030_lower_high_ratio_1512_030}


def ptt_base_universe_d2_016_ptt_basefill_004(ptt_basefill_004):
    return _base_universe_d2(ptt_basefill_004, 16)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_016_ptt_basefill_004'] = {'inputs': ['ptt_basefill_004'], 'func': ptt_base_universe_d2_016_ptt_basefill_004}


def ptt_base_universe_d2_017_ptt_basefill_005(ptt_basefill_005):
    return _base_universe_d2(ptt_basefill_005, 17)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_017_ptt_basefill_005'] = {'inputs': ['ptt_basefill_005'], 'func': ptt_base_universe_d2_017_ptt_basefill_005}


def ptt_base_universe_d2_018_ptt_basefill_010(ptt_basefill_010):
    return _base_universe_d2(ptt_basefill_010, 18)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_018_ptt_basefill_010'] = {'inputs': ['ptt_basefill_010'], 'func': ptt_base_universe_d2_018_ptt_basefill_010}


def ptt_base_universe_d2_019_ptt_basefill_011(ptt_basefill_011):
    return _base_universe_d2(ptt_basefill_011, 19)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_019_ptt_basefill_011'] = {'inputs': ['ptt_basefill_011'], 'func': ptt_base_universe_d2_019_ptt_basefill_011}


def ptt_base_universe_d2_020_ptt_basefill_016(ptt_basefill_016):
    return _base_universe_d2(ptt_basefill_016, 20)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_020_ptt_basefill_016'] = {'inputs': ['ptt_basefill_016'], 'func': ptt_base_universe_d2_020_ptt_basefill_016}


def ptt_base_universe_d2_021_ptt_basefill_017(ptt_basefill_017):
    return _base_universe_d2(ptt_basefill_017, 21)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_021_ptt_basefill_017'] = {'inputs': ['ptt_basefill_017'], 'func': ptt_base_universe_d2_021_ptt_basefill_017}


def ptt_base_universe_d2_022_ptt_basefill_022(ptt_basefill_022):
    return _base_universe_d2(ptt_basefill_022, 22)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_022_ptt_basefill_022'] = {'inputs': ['ptt_basefill_022'], 'func': ptt_base_universe_d2_022_ptt_basefill_022}


def ptt_base_universe_d2_023_ptt_basefill_023(ptt_basefill_023):
    return _base_universe_d2(ptt_basefill_023, 23)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_023_ptt_basefill_023'] = {'inputs': ['ptt_basefill_023'], 'func': ptt_base_universe_d2_023_ptt_basefill_023}


def ptt_base_universe_d2_024_ptt_basefill_028(ptt_basefill_028):
    return _base_universe_d2(ptt_basefill_028, 24)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_024_ptt_basefill_028'] = {'inputs': ['ptt_basefill_028'], 'func': ptt_base_universe_d2_024_ptt_basefill_028}


def ptt_base_universe_d2_025_ptt_basefill_029(ptt_basefill_029):
    return _base_universe_d2(ptt_basefill_029, 25)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_025_ptt_basefill_029'] = {'inputs': ['ptt_basefill_029'], 'func': ptt_base_universe_d2_025_ptt_basefill_029}


def ptt_base_universe_d2_026_ptt_basefill_031(ptt_basefill_031):
    return _base_universe_d2(ptt_basefill_031, 26)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_026_ptt_basefill_031'] = {'inputs': ['ptt_basefill_031'], 'func': ptt_base_universe_d2_026_ptt_basefill_031}


def ptt_base_universe_d2_027_ptt_basefill_032(ptt_basefill_032):
    return _base_universe_d2(ptt_basefill_032, 27)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_027_ptt_basefill_032'] = {'inputs': ['ptt_basefill_032'], 'func': ptt_base_universe_d2_027_ptt_basefill_032}


def ptt_base_universe_d2_028_ptt_basefill_033(ptt_basefill_033):
    return _base_universe_d2(ptt_basefill_033, 28)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_028_ptt_basefill_033'] = {'inputs': ['ptt_basefill_033'], 'func': ptt_base_universe_d2_028_ptt_basefill_033}


def ptt_base_universe_d2_029_ptt_basefill_034(ptt_basefill_034):
    return _base_universe_d2(ptt_basefill_034, 29)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_029_ptt_basefill_034'] = {'inputs': ['ptt_basefill_034'], 'func': ptt_base_universe_d2_029_ptt_basefill_034}


def ptt_base_universe_d2_030_ptt_basefill_035(ptt_basefill_035):
    return _base_universe_d2(ptt_basefill_035, 30)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_030_ptt_basefill_035'] = {'inputs': ['ptt_basefill_035'], 'func': ptt_base_universe_d2_030_ptt_basefill_035}


def ptt_base_universe_d2_031_ptt_basefill_036(ptt_basefill_036):
    return _base_universe_d2(ptt_basefill_036, 31)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_031_ptt_basefill_036'] = {'inputs': ['ptt_basefill_036'], 'func': ptt_base_universe_d2_031_ptt_basefill_036}


def ptt_base_universe_d2_032_ptt_basefill_037(ptt_basefill_037):
    return _base_universe_d2(ptt_basefill_037, 32)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_032_ptt_basefill_037'] = {'inputs': ['ptt_basefill_037'], 'func': ptt_base_universe_d2_032_ptt_basefill_037}


def ptt_base_universe_d2_033_ptt_basefill_038(ptt_basefill_038):
    return _base_universe_d2(ptt_basefill_038, 33)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_033_ptt_basefill_038'] = {'inputs': ['ptt_basefill_038'], 'func': ptt_base_universe_d2_033_ptt_basefill_038}


def ptt_base_universe_d2_034_ptt_basefill_039(ptt_basefill_039):
    return _base_universe_d2(ptt_basefill_039, 34)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_034_ptt_basefill_039'] = {'inputs': ['ptt_basefill_039'], 'func': ptt_base_universe_d2_034_ptt_basefill_039}


def ptt_base_universe_d2_035_ptt_basefill_040(ptt_basefill_040):
    return _base_universe_d2(ptt_basefill_040, 35)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_035_ptt_basefill_040'] = {'inputs': ['ptt_basefill_040'], 'func': ptt_base_universe_d2_035_ptt_basefill_040}


def ptt_base_universe_d2_036_ptt_basefill_041(ptt_basefill_041):
    return _base_universe_d2(ptt_basefill_041, 36)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_036_ptt_basefill_041'] = {'inputs': ['ptt_basefill_041'], 'func': ptt_base_universe_d2_036_ptt_basefill_041}


def ptt_base_universe_d2_037_ptt_basefill_042(ptt_basefill_042):
    return _base_universe_d2(ptt_basefill_042, 37)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_037_ptt_basefill_042'] = {'inputs': ['ptt_basefill_042'], 'func': ptt_base_universe_d2_037_ptt_basefill_042}


def ptt_base_universe_d2_038_ptt_basefill_043(ptt_basefill_043):
    return _base_universe_d2(ptt_basefill_043, 38)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_038_ptt_basefill_043'] = {'inputs': ['ptt_basefill_043'], 'func': ptt_base_universe_d2_038_ptt_basefill_043}


def ptt_base_universe_d2_039_ptt_basefill_044(ptt_basefill_044):
    return _base_universe_d2(ptt_basefill_044, 39)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_039_ptt_basefill_044'] = {'inputs': ['ptt_basefill_044'], 'func': ptt_base_universe_d2_039_ptt_basefill_044}


def ptt_base_universe_d2_040_ptt_basefill_045(ptt_basefill_045):
    return _base_universe_d2(ptt_basefill_045, 40)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_040_ptt_basefill_045'] = {'inputs': ['ptt_basefill_045'], 'func': ptt_base_universe_d2_040_ptt_basefill_045}


def ptt_base_universe_d2_041_ptt_basefill_046(ptt_basefill_046):
    return _base_universe_d2(ptt_basefill_046, 41)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_041_ptt_basefill_046'] = {'inputs': ['ptt_basefill_046'], 'func': ptt_base_universe_d2_041_ptt_basefill_046}


def ptt_base_universe_d2_042_ptt_basefill_047(ptt_basefill_047):
    return _base_universe_d2(ptt_basefill_047, 42)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_042_ptt_basefill_047'] = {'inputs': ['ptt_basefill_047'], 'func': ptt_base_universe_d2_042_ptt_basefill_047}


def ptt_base_universe_d2_043_ptt_basefill_048(ptt_basefill_048):
    return _base_universe_d2(ptt_basefill_048, 43)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_043_ptt_basefill_048'] = {'inputs': ['ptt_basefill_048'], 'func': ptt_base_universe_d2_043_ptt_basefill_048}


def ptt_base_universe_d2_044_ptt_basefill_049(ptt_basefill_049):
    return _base_universe_d2(ptt_basefill_049, 44)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_044_ptt_basefill_049'] = {'inputs': ['ptt_basefill_049'], 'func': ptt_base_universe_d2_044_ptt_basefill_049}


def ptt_base_universe_d2_045_ptt_basefill_050(ptt_basefill_050):
    return _base_universe_d2(ptt_basefill_050, 45)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_045_ptt_basefill_050'] = {'inputs': ['ptt_basefill_050'], 'func': ptt_base_universe_d2_045_ptt_basefill_050}


def ptt_base_universe_d2_046_ptt_basefill_051(ptt_basefill_051):
    return _base_universe_d2(ptt_basefill_051, 46)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_046_ptt_basefill_051'] = {'inputs': ['ptt_basefill_051'], 'func': ptt_base_universe_d2_046_ptt_basefill_051}


def ptt_base_universe_d2_047_ptt_basefill_052(ptt_basefill_052):
    return _base_universe_d2(ptt_basefill_052, 47)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_047_ptt_basefill_052'] = {'inputs': ['ptt_basefill_052'], 'func': ptt_base_universe_d2_047_ptt_basefill_052}


def ptt_base_universe_d2_048_ptt_basefill_053(ptt_basefill_053):
    return _base_universe_d2(ptt_basefill_053, 48)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_048_ptt_basefill_053'] = {'inputs': ['ptt_basefill_053'], 'func': ptt_base_universe_d2_048_ptt_basefill_053}


def ptt_base_universe_d2_049_ptt_basefill_054(ptt_basefill_054):
    return _base_universe_d2(ptt_basefill_054, 49)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_049_ptt_basefill_054'] = {'inputs': ['ptt_basefill_054'], 'func': ptt_base_universe_d2_049_ptt_basefill_054}


def ptt_base_universe_d2_050_ptt_basefill_055(ptt_basefill_055):
    return _base_universe_d2(ptt_basefill_055, 50)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_050_ptt_basefill_055'] = {'inputs': ['ptt_basefill_055'], 'func': ptt_base_universe_d2_050_ptt_basefill_055}


def ptt_base_universe_d2_051_ptt_basefill_056(ptt_basefill_056):
    return _base_universe_d2(ptt_basefill_056, 51)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_051_ptt_basefill_056'] = {'inputs': ['ptt_basefill_056'], 'func': ptt_base_universe_d2_051_ptt_basefill_056}


def ptt_base_universe_d2_052_ptt_basefill_057(ptt_basefill_057):
    return _base_universe_d2(ptt_basefill_057, 52)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_052_ptt_basefill_057'] = {'inputs': ['ptt_basefill_057'], 'func': ptt_base_universe_d2_052_ptt_basefill_057}


def ptt_base_universe_d2_053_ptt_basefill_058(ptt_basefill_058):
    return _base_universe_d2(ptt_basefill_058, 53)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_053_ptt_basefill_058'] = {'inputs': ['ptt_basefill_058'], 'func': ptt_base_universe_d2_053_ptt_basefill_058}


def ptt_base_universe_d2_054_ptt_basefill_059(ptt_basefill_059):
    return _base_universe_d2(ptt_basefill_059, 54)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_054_ptt_basefill_059'] = {'inputs': ['ptt_basefill_059'], 'func': ptt_base_universe_d2_054_ptt_basefill_059}


def ptt_base_universe_d2_055_ptt_basefill_060(ptt_basefill_060):
    return _base_universe_d2(ptt_basefill_060, 55)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_055_ptt_basefill_060'] = {'inputs': ['ptt_basefill_060'], 'func': ptt_base_universe_d2_055_ptt_basefill_060}


def ptt_base_universe_d2_056_ptt_basefill_061(ptt_basefill_061):
    return _base_universe_d2(ptt_basefill_061, 56)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_056_ptt_basefill_061'] = {'inputs': ['ptt_basefill_061'], 'func': ptt_base_universe_d2_056_ptt_basefill_061}


def ptt_base_universe_d2_057_ptt_basefill_062(ptt_basefill_062):
    return _base_universe_d2(ptt_basefill_062, 57)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_057_ptt_basefill_062'] = {'inputs': ['ptt_basefill_062'], 'func': ptt_base_universe_d2_057_ptt_basefill_062}


def ptt_base_universe_d2_058_ptt_basefill_063(ptt_basefill_063):
    return _base_universe_d2(ptt_basefill_063, 58)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_058_ptt_basefill_063'] = {'inputs': ['ptt_basefill_063'], 'func': ptt_base_universe_d2_058_ptt_basefill_063}


def ptt_base_universe_d2_059_ptt_basefill_064(ptt_basefill_064):
    return _base_universe_d2(ptt_basefill_064, 59)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_059_ptt_basefill_064'] = {'inputs': ['ptt_basefill_064'], 'func': ptt_base_universe_d2_059_ptt_basefill_064}


def ptt_base_universe_d2_060_ptt_basefill_065(ptt_basefill_065):
    return _base_universe_d2(ptt_basefill_065, 60)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_060_ptt_basefill_065'] = {'inputs': ['ptt_basefill_065'], 'func': ptt_base_universe_d2_060_ptt_basefill_065}


def ptt_base_universe_d2_061_ptt_basefill_066(ptt_basefill_066):
    return _base_universe_d2(ptt_basefill_066, 61)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_061_ptt_basefill_066'] = {'inputs': ['ptt_basefill_066'], 'func': ptt_base_universe_d2_061_ptt_basefill_066}


def ptt_base_universe_d2_062_ptt_basefill_067(ptt_basefill_067):
    return _base_universe_d2(ptt_basefill_067, 62)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_062_ptt_basefill_067'] = {'inputs': ['ptt_basefill_067'], 'func': ptt_base_universe_d2_062_ptt_basefill_067}


def ptt_base_universe_d2_063_ptt_basefill_068(ptt_basefill_068):
    return _base_universe_d2(ptt_basefill_068, 63)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_063_ptt_basefill_068'] = {'inputs': ['ptt_basefill_068'], 'func': ptt_base_universe_d2_063_ptt_basefill_068}


def ptt_base_universe_d2_064_ptt_basefill_069(ptt_basefill_069):
    return _base_universe_d2(ptt_basefill_069, 64)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_064_ptt_basefill_069'] = {'inputs': ['ptt_basefill_069'], 'func': ptt_base_universe_d2_064_ptt_basefill_069}


def ptt_base_universe_d2_065_ptt_basefill_070(ptt_basefill_070):
    return _base_universe_d2(ptt_basefill_070, 65)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_065_ptt_basefill_070'] = {'inputs': ['ptt_basefill_070'], 'func': ptt_base_universe_d2_065_ptt_basefill_070}


def ptt_base_universe_d2_066_ptt_basefill_071(ptt_basefill_071):
    return _base_universe_d2(ptt_basefill_071, 66)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_066_ptt_basefill_071'] = {'inputs': ['ptt_basefill_071'], 'func': ptt_base_universe_d2_066_ptt_basefill_071}


def ptt_base_universe_d2_067_ptt_basefill_072(ptt_basefill_072):
    return _base_universe_d2(ptt_basefill_072, 67)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_067_ptt_basefill_072'] = {'inputs': ['ptt_basefill_072'], 'func': ptt_base_universe_d2_067_ptt_basefill_072}


def ptt_base_universe_d2_068_ptt_basefill_073(ptt_basefill_073):
    return _base_universe_d2(ptt_basefill_073, 68)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_068_ptt_basefill_073'] = {'inputs': ['ptt_basefill_073'], 'func': ptt_base_universe_d2_068_ptt_basefill_073}


def ptt_base_universe_d2_069_ptt_basefill_074(ptt_basefill_074):
    return _base_universe_d2(ptt_basefill_074, 69)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_069_ptt_basefill_074'] = {'inputs': ['ptt_basefill_074'], 'func': ptt_base_universe_d2_069_ptt_basefill_074}


def ptt_base_universe_d2_070_ptt_basefill_075(ptt_basefill_075):
    return _base_universe_d2(ptt_basefill_075, 70)
PTT_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['ptt_base_universe_d2_070_ptt_basefill_075'] = {'inputs': ['ptt_basefill_075'], 'func': ptt_base_universe_d2_070_ptt_basefill_075}
