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



def uw_151_uw_001_drawdown_from_high_5_001_roc_1(uw_001_drawdown_from_high_5_001):
    feature = _s(uw_001_drawdown_from_high_5_001)
    return (_roc(feature, 1)).reindex(feature.index)

def uw_152_uw_007_drawdown_from_high_126_007_roc_5(uw_007_drawdown_from_high_126_007):
    feature = _s(uw_007_drawdown_from_high_126_007)
    return (_roc(feature, 5)).reindex(feature.index)

def uw_153_uw_013_drawdown_from_high_1008_013_roc_42(uw_013_drawdown_from_high_1008_013):
    feature = _s(uw_013_drawdown_from_high_1008_013)
    return (_roc(feature, 42)).reindex(feature.index)

def uw_154_uw_019_drawdown_from_high_42_019_roc_126(uw_019_drawdown_from_high_42_019):
    feature = _s(uw_019_drawdown_from_high_42_019)
    return (_roc(feature, 126)).reindex(feature.index)

def uw_155_uw_025_drawdown_from_high_378_025_roc_378(uw_025_drawdown_from_high_378_025):
    feature = _s(uw_025_drawdown_from_high_378_025)
    return (_roc(feature, 378)).reindex(feature.index)






















UNDERWATER_CURVE_REGISTRY_2ND_DERIVATIVES = {
    'uw_151_uw_001_drawdown_from_high_5_001_roc_1': {'inputs': ['uw_001_drawdown_from_high_5_001'], 'func': uw_151_uw_001_drawdown_from_high_5_001_roc_1},
    'uw_152_uw_007_drawdown_from_high_126_007_roc_5': {'inputs': ['uw_007_drawdown_from_high_126_007'], 'func': uw_152_uw_007_drawdown_from_high_126_007_roc_5},
    'uw_153_uw_013_drawdown_from_high_1008_013_roc_42': {'inputs': ['uw_013_drawdown_from_high_1008_013'], 'func': uw_153_uw_013_drawdown_from_high_1008_013_roc_42},
    'uw_154_uw_019_drawdown_from_high_42_019_roc_126': {'inputs': ['uw_019_drawdown_from_high_42_019'], 'func': uw_154_uw_019_drawdown_from_high_42_019_roc_126},
    'uw_155_uw_025_drawdown_from_high_378_025_roc_378': {'inputs': ['uw_025_drawdown_from_high_378_025'], 'func': uw_155_uw_025_drawdown_from_high_378_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def uc_replacement_d2_001(uc_replacement_001):
    feature = _clean(uc_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_001'] = {'inputs': ['uc_replacement_001'], 'func': uc_replacement_d2_001}


def uc_replacement_d2_002(uc_replacement_002):
    feature = _clean(uc_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_002'] = {'inputs': ['uc_replacement_002'], 'func': uc_replacement_d2_002}


def uc_replacement_d2_003(uc_replacement_003):
    feature = _clean(uc_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_003'] = {'inputs': ['uc_replacement_003'], 'func': uc_replacement_d2_003}


def uc_replacement_d2_004(uc_replacement_004):
    feature = _clean(uc_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_004'] = {'inputs': ['uc_replacement_004'], 'func': uc_replacement_d2_004}


def uc_replacement_d2_005(uc_replacement_005):
    feature = _clean(uc_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_005'] = {'inputs': ['uc_replacement_005'], 'func': uc_replacement_d2_005}


def uc_replacement_d2_006(uc_replacement_006):
    feature = _clean(uc_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_006'] = {'inputs': ['uc_replacement_006'], 'func': uc_replacement_d2_006}


def uc_replacement_d2_007(uc_replacement_007):
    feature = _clean(uc_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_007'] = {'inputs': ['uc_replacement_007'], 'func': uc_replacement_d2_007}


def uc_replacement_d2_008(uc_replacement_008):
    feature = _clean(uc_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_008'] = {'inputs': ['uc_replacement_008'], 'func': uc_replacement_d2_008}


def uc_replacement_d2_009(uc_replacement_009):
    feature = _clean(uc_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_009'] = {'inputs': ['uc_replacement_009'], 'func': uc_replacement_d2_009}


def uc_replacement_d2_010(uc_replacement_010):
    feature = _clean(uc_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_010'] = {'inputs': ['uc_replacement_010'], 'func': uc_replacement_d2_010}


def uc_replacement_d2_011(uc_replacement_011):
    feature = _clean(uc_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_011'] = {'inputs': ['uc_replacement_011'], 'func': uc_replacement_d2_011}


def uc_replacement_d2_012(uc_replacement_012):
    feature = _clean(uc_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_012'] = {'inputs': ['uc_replacement_012'], 'func': uc_replacement_d2_012}


def uc_replacement_d2_013(uc_replacement_013):
    feature = _clean(uc_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_013'] = {'inputs': ['uc_replacement_013'], 'func': uc_replacement_d2_013}


def uc_replacement_d2_014(uc_replacement_014):
    feature = _clean(uc_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_014'] = {'inputs': ['uc_replacement_014'], 'func': uc_replacement_d2_014}


def uc_replacement_d2_015(uc_replacement_015):
    feature = _clean(uc_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_015'] = {'inputs': ['uc_replacement_015'], 'func': uc_replacement_d2_015}


def uc_replacement_d2_016(uc_replacement_016):
    feature = _clean(uc_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_016'] = {'inputs': ['uc_replacement_016'], 'func': uc_replacement_d2_016}


def uc_replacement_d2_017(uc_replacement_017):
    feature = _clean(uc_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_017'] = {'inputs': ['uc_replacement_017'], 'func': uc_replacement_d2_017}


def uc_replacement_d2_018(uc_replacement_018):
    feature = _clean(uc_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_018'] = {'inputs': ['uc_replacement_018'], 'func': uc_replacement_d2_018}


def uc_replacement_d2_019(uc_replacement_019):
    feature = _clean(uc_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_019'] = {'inputs': ['uc_replacement_019'], 'func': uc_replacement_d2_019}


def uc_replacement_d2_020(uc_replacement_020):
    feature = _clean(uc_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_020'] = {'inputs': ['uc_replacement_020'], 'func': uc_replacement_d2_020}


def uc_replacement_d2_021(uc_replacement_021):
    feature = _clean(uc_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_021'] = {'inputs': ['uc_replacement_021'], 'func': uc_replacement_d2_021}


def uc_replacement_d2_022(uc_replacement_022):
    feature = _clean(uc_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_022'] = {'inputs': ['uc_replacement_022'], 'func': uc_replacement_d2_022}


def uc_replacement_d2_023(uc_replacement_023):
    feature = _clean(uc_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_023'] = {'inputs': ['uc_replacement_023'], 'func': uc_replacement_d2_023}


def uc_replacement_d2_024(uc_replacement_024):
    feature = _clean(uc_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_024'] = {'inputs': ['uc_replacement_024'], 'func': uc_replacement_d2_024}


def uc_replacement_d2_025(uc_replacement_025):
    feature = _clean(uc_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_025'] = {'inputs': ['uc_replacement_025'], 'func': uc_replacement_d2_025}


def uc_replacement_d2_026(uc_replacement_026):
    feature = _clean(uc_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_026'] = {'inputs': ['uc_replacement_026'], 'func': uc_replacement_d2_026}


def uc_replacement_d2_027(uc_replacement_027):
    feature = _clean(uc_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_027'] = {'inputs': ['uc_replacement_027'], 'func': uc_replacement_d2_027}


def uc_replacement_d2_028(uc_replacement_028):
    feature = _clean(uc_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_028'] = {'inputs': ['uc_replacement_028'], 'func': uc_replacement_d2_028}


def uc_replacement_d2_029(uc_replacement_029):
    feature = _clean(uc_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_029'] = {'inputs': ['uc_replacement_029'], 'func': uc_replacement_d2_029}


def uc_replacement_d2_030(uc_replacement_030):
    feature = _clean(uc_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_030'] = {'inputs': ['uc_replacement_030'], 'func': uc_replacement_d2_030}


def uc_replacement_d2_031(uc_replacement_031):
    feature = _clean(uc_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_031'] = {'inputs': ['uc_replacement_031'], 'func': uc_replacement_d2_031}


def uc_replacement_d2_032(uc_replacement_032):
    feature = _clean(uc_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_032'] = {'inputs': ['uc_replacement_032'], 'func': uc_replacement_d2_032}


def uc_replacement_d2_033(uc_replacement_033):
    feature = _clean(uc_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_033'] = {'inputs': ['uc_replacement_033'], 'func': uc_replacement_d2_033}


def uc_replacement_d2_034(uc_replacement_034):
    feature = _clean(uc_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_034'] = {'inputs': ['uc_replacement_034'], 'func': uc_replacement_d2_034}


def uc_replacement_d2_035(uc_replacement_035):
    feature = _clean(uc_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_035'] = {'inputs': ['uc_replacement_035'], 'func': uc_replacement_d2_035}


def uc_replacement_d2_036(uc_replacement_036):
    feature = _clean(uc_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_036'] = {'inputs': ['uc_replacement_036'], 'func': uc_replacement_d2_036}


def uc_replacement_d2_037(uc_replacement_037):
    feature = _clean(uc_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_037'] = {'inputs': ['uc_replacement_037'], 'func': uc_replacement_d2_037}


def uc_replacement_d2_038(uc_replacement_038):
    feature = _clean(uc_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_038'] = {'inputs': ['uc_replacement_038'], 'func': uc_replacement_d2_038}


def uc_replacement_d2_039(uc_replacement_039):
    feature = _clean(uc_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_039'] = {'inputs': ['uc_replacement_039'], 'func': uc_replacement_d2_039}


def uc_replacement_d2_040(uc_replacement_040):
    feature = _clean(uc_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_040'] = {'inputs': ['uc_replacement_040'], 'func': uc_replacement_d2_040}


def uc_replacement_d2_041(uc_replacement_041):
    feature = _clean(uc_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_041'] = {'inputs': ['uc_replacement_041'], 'func': uc_replacement_d2_041}


def uc_replacement_d2_042(uc_replacement_042):
    feature = _clean(uc_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_042'] = {'inputs': ['uc_replacement_042'], 'func': uc_replacement_d2_042}


def uc_replacement_d2_043(uc_replacement_043):
    feature = _clean(uc_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_043'] = {'inputs': ['uc_replacement_043'], 'func': uc_replacement_d2_043}


def uc_replacement_d2_044(uc_replacement_044):
    feature = _clean(uc_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_044'] = {'inputs': ['uc_replacement_044'], 'func': uc_replacement_d2_044}


def uc_replacement_d2_045(uc_replacement_045):
    feature = _clean(uc_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_045'] = {'inputs': ['uc_replacement_045'], 'func': uc_replacement_d2_045}


def uc_replacement_d2_046(uc_replacement_046):
    feature = _clean(uc_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_046'] = {'inputs': ['uc_replacement_046'], 'func': uc_replacement_d2_046}


def uc_replacement_d2_047(uc_replacement_047):
    feature = _clean(uc_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_047'] = {'inputs': ['uc_replacement_047'], 'func': uc_replacement_d2_047}


def uc_replacement_d2_048(uc_replacement_048):
    feature = _clean(uc_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_048'] = {'inputs': ['uc_replacement_048'], 'func': uc_replacement_d2_048}


def uc_replacement_d2_049(uc_replacement_049):
    feature = _clean(uc_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_049'] = {'inputs': ['uc_replacement_049'], 'func': uc_replacement_d2_049}


def uc_replacement_d2_050(uc_replacement_050):
    feature = _clean(uc_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_050'] = {'inputs': ['uc_replacement_050'], 'func': uc_replacement_d2_050}


def uc_replacement_d2_051(uc_replacement_051):
    feature = _clean(uc_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_051'] = {'inputs': ['uc_replacement_051'], 'func': uc_replacement_d2_051}


def uc_replacement_d2_052(uc_replacement_052):
    feature = _clean(uc_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_052'] = {'inputs': ['uc_replacement_052'], 'func': uc_replacement_d2_052}


def uc_replacement_d2_053(uc_replacement_053):
    feature = _clean(uc_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_053'] = {'inputs': ['uc_replacement_053'], 'func': uc_replacement_d2_053}


def uc_replacement_d2_054(uc_replacement_054):
    feature = _clean(uc_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_054'] = {'inputs': ['uc_replacement_054'], 'func': uc_replacement_d2_054}


def uc_replacement_d2_055(uc_replacement_055):
    feature = _clean(uc_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_055'] = {'inputs': ['uc_replacement_055'], 'func': uc_replacement_d2_055}


def uc_replacement_d2_056(uc_replacement_056):
    feature = _clean(uc_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_056'] = {'inputs': ['uc_replacement_056'], 'func': uc_replacement_d2_056}


def uc_replacement_d2_057(uc_replacement_057):
    feature = _clean(uc_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_057'] = {'inputs': ['uc_replacement_057'], 'func': uc_replacement_d2_057}


def uc_replacement_d2_058(uc_replacement_058):
    feature = _clean(uc_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_058'] = {'inputs': ['uc_replacement_058'], 'func': uc_replacement_d2_058}


def uc_replacement_d2_059(uc_replacement_059):
    feature = _clean(uc_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_059'] = {'inputs': ['uc_replacement_059'], 'func': uc_replacement_d2_059}


def uc_replacement_d2_060(uc_replacement_060):
    feature = _clean(uc_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_060'] = {'inputs': ['uc_replacement_060'], 'func': uc_replacement_d2_060}


def uc_replacement_d2_061(uc_replacement_061):
    feature = _clean(uc_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_061'] = {'inputs': ['uc_replacement_061'], 'func': uc_replacement_d2_061}


def uc_replacement_d2_062(uc_replacement_062):
    feature = _clean(uc_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_062'] = {'inputs': ['uc_replacement_062'], 'func': uc_replacement_d2_062}


def uc_replacement_d2_063(uc_replacement_063):
    feature = _clean(uc_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_063'] = {'inputs': ['uc_replacement_063'], 'func': uc_replacement_d2_063}


def uc_replacement_d2_064(uc_replacement_064):
    feature = _clean(uc_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_064'] = {'inputs': ['uc_replacement_064'], 'func': uc_replacement_d2_064}


def uc_replacement_d2_065(uc_replacement_065):
    feature = _clean(uc_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_065'] = {'inputs': ['uc_replacement_065'], 'func': uc_replacement_d2_065}


def uc_replacement_d2_066(uc_replacement_066):
    feature = _clean(uc_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_066'] = {'inputs': ['uc_replacement_066'], 'func': uc_replacement_d2_066}


def uc_replacement_d2_067(uc_replacement_067):
    feature = _clean(uc_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_067'] = {'inputs': ['uc_replacement_067'], 'func': uc_replacement_d2_067}


def uc_replacement_d2_068(uc_replacement_068):
    feature = _clean(uc_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_068'] = {'inputs': ['uc_replacement_068'], 'func': uc_replacement_d2_068}


def uc_replacement_d2_069(uc_replacement_069):
    feature = _clean(uc_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_069'] = {'inputs': ['uc_replacement_069'], 'func': uc_replacement_d2_069}


def uc_replacement_d2_070(uc_replacement_070):
    feature = _clean(uc_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_070'] = {'inputs': ['uc_replacement_070'], 'func': uc_replacement_d2_070}


def uc_replacement_d2_071(uc_replacement_071):
    feature = _clean(uc_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_071'] = {'inputs': ['uc_replacement_071'], 'func': uc_replacement_d2_071}


def uc_replacement_d2_072(uc_replacement_072):
    feature = _clean(uc_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_072'] = {'inputs': ['uc_replacement_072'], 'func': uc_replacement_d2_072}


def uc_replacement_d2_073(uc_replacement_073):
    feature = _clean(uc_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_073'] = {'inputs': ['uc_replacement_073'], 'func': uc_replacement_d2_073}


def uc_replacement_d2_074(uc_replacement_074):
    feature = _clean(uc_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_074'] = {'inputs': ['uc_replacement_074'], 'func': uc_replacement_d2_074}


def uc_replacement_d2_075(uc_replacement_075):
    feature = _clean(uc_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_075'] = {'inputs': ['uc_replacement_075'], 'func': uc_replacement_d2_075}


def uc_replacement_d2_076(uc_replacement_076):
    feature = _clean(uc_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_076'] = {'inputs': ['uc_replacement_076'], 'func': uc_replacement_d2_076}


def uc_replacement_d2_077(uc_replacement_077):
    feature = _clean(uc_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_077'] = {'inputs': ['uc_replacement_077'], 'func': uc_replacement_d2_077}


def uc_replacement_d2_078(uc_replacement_078):
    feature = _clean(uc_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_078'] = {'inputs': ['uc_replacement_078'], 'func': uc_replacement_d2_078}


def uc_replacement_d2_079(uc_replacement_079):
    feature = _clean(uc_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_079'] = {'inputs': ['uc_replacement_079'], 'func': uc_replacement_d2_079}


def uc_replacement_d2_080(uc_replacement_080):
    feature = _clean(uc_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_080'] = {'inputs': ['uc_replacement_080'], 'func': uc_replacement_d2_080}


def uc_replacement_d2_081(uc_replacement_081):
    feature = _clean(uc_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_081'] = {'inputs': ['uc_replacement_081'], 'func': uc_replacement_d2_081}


def uc_replacement_d2_082(uc_replacement_082):
    feature = _clean(uc_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_082'] = {'inputs': ['uc_replacement_082'], 'func': uc_replacement_d2_082}


def uc_replacement_d2_083(uc_replacement_083):
    feature = _clean(uc_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_083'] = {'inputs': ['uc_replacement_083'], 'func': uc_replacement_d2_083}


def uc_replacement_d2_084(uc_replacement_084):
    feature = _clean(uc_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_084'] = {'inputs': ['uc_replacement_084'], 'func': uc_replacement_d2_084}


def uc_replacement_d2_085(uc_replacement_085):
    feature = _clean(uc_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_085'] = {'inputs': ['uc_replacement_085'], 'func': uc_replacement_d2_085}


def uc_replacement_d2_086(uc_replacement_086):
    feature = _clean(uc_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_086'] = {'inputs': ['uc_replacement_086'], 'func': uc_replacement_d2_086}


def uc_replacement_d2_087(uc_replacement_087):
    feature = _clean(uc_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_087'] = {'inputs': ['uc_replacement_087'], 'func': uc_replacement_d2_087}


def uc_replacement_d2_088(uc_replacement_088):
    feature = _clean(uc_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_088'] = {'inputs': ['uc_replacement_088'], 'func': uc_replacement_d2_088}


def uc_replacement_d2_089(uc_replacement_089):
    feature = _clean(uc_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_089'] = {'inputs': ['uc_replacement_089'], 'func': uc_replacement_d2_089}


def uc_replacement_d2_090(uc_replacement_090):
    feature = _clean(uc_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_090'] = {'inputs': ['uc_replacement_090'], 'func': uc_replacement_d2_090}


def uc_replacement_d2_091(uc_replacement_091):
    feature = _clean(uc_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_091'] = {'inputs': ['uc_replacement_091'], 'func': uc_replacement_d2_091}


def uc_replacement_d2_092(uc_replacement_092):
    feature = _clean(uc_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_092'] = {'inputs': ['uc_replacement_092'], 'func': uc_replacement_d2_092}


def uc_replacement_d2_093(uc_replacement_093):
    feature = _clean(uc_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_093'] = {'inputs': ['uc_replacement_093'], 'func': uc_replacement_d2_093}


def uc_replacement_d2_094(uc_replacement_094):
    feature = _clean(uc_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_094'] = {'inputs': ['uc_replacement_094'], 'func': uc_replacement_d2_094}


def uc_replacement_d2_095(uc_replacement_095):
    feature = _clean(uc_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_095'] = {'inputs': ['uc_replacement_095'], 'func': uc_replacement_d2_095}


def uc_replacement_d2_096(uc_replacement_096):
    feature = _clean(uc_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_096'] = {'inputs': ['uc_replacement_096'], 'func': uc_replacement_d2_096}


def uc_replacement_d2_097(uc_replacement_097):
    feature = _clean(uc_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_097'] = {'inputs': ['uc_replacement_097'], 'func': uc_replacement_d2_097}


def uc_replacement_d2_098(uc_replacement_098):
    feature = _clean(uc_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_098'] = {'inputs': ['uc_replacement_098'], 'func': uc_replacement_d2_098}


def uc_replacement_d2_099(uc_replacement_099):
    feature = _clean(uc_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_099'] = {'inputs': ['uc_replacement_099'], 'func': uc_replacement_d2_099}


def uc_replacement_d2_100(uc_replacement_100):
    feature = _clean(uc_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_100'] = {'inputs': ['uc_replacement_100'], 'func': uc_replacement_d2_100}


def uc_replacement_d2_101(uc_replacement_101):
    feature = _clean(uc_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_101'] = {'inputs': ['uc_replacement_101'], 'func': uc_replacement_d2_101}


def uc_replacement_d2_102(uc_replacement_102):
    feature = _clean(uc_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_102'] = {'inputs': ['uc_replacement_102'], 'func': uc_replacement_d2_102}


def uc_replacement_d2_103(uc_replacement_103):
    feature = _clean(uc_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_103'] = {'inputs': ['uc_replacement_103'], 'func': uc_replacement_d2_103}


def uc_replacement_d2_104(uc_replacement_104):
    feature = _clean(uc_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_104'] = {'inputs': ['uc_replacement_104'], 'func': uc_replacement_d2_104}


def uc_replacement_d2_105(uc_replacement_105):
    feature = _clean(uc_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_105'] = {'inputs': ['uc_replacement_105'], 'func': uc_replacement_d2_105}


def uc_replacement_d2_106(uc_replacement_106):
    feature = _clean(uc_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_106'] = {'inputs': ['uc_replacement_106'], 'func': uc_replacement_d2_106}


def uc_replacement_d2_107(uc_replacement_107):
    feature = _clean(uc_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_107'] = {'inputs': ['uc_replacement_107'], 'func': uc_replacement_d2_107}


def uc_replacement_d2_108(uc_replacement_108):
    feature = _clean(uc_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_108'] = {'inputs': ['uc_replacement_108'], 'func': uc_replacement_d2_108}


def uc_replacement_d2_109(uc_replacement_109):
    feature = _clean(uc_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_109'] = {'inputs': ['uc_replacement_109'], 'func': uc_replacement_d2_109}


def uc_replacement_d2_110(uc_replacement_110):
    feature = _clean(uc_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_110'] = {'inputs': ['uc_replacement_110'], 'func': uc_replacement_d2_110}


def uc_replacement_d2_111(uc_replacement_111):
    feature = _clean(uc_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_111'] = {'inputs': ['uc_replacement_111'], 'func': uc_replacement_d2_111}


def uc_replacement_d2_112(uc_replacement_112):
    feature = _clean(uc_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_112'] = {'inputs': ['uc_replacement_112'], 'func': uc_replacement_d2_112}


def uc_replacement_d2_113(uc_replacement_113):
    feature = _clean(uc_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_113'] = {'inputs': ['uc_replacement_113'], 'func': uc_replacement_d2_113}


def uc_replacement_d2_114(uc_replacement_114):
    feature = _clean(uc_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_114'] = {'inputs': ['uc_replacement_114'], 'func': uc_replacement_d2_114}


def uc_replacement_d2_115(uc_replacement_115):
    feature = _clean(uc_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_115'] = {'inputs': ['uc_replacement_115'], 'func': uc_replacement_d2_115}


def uc_replacement_d2_116(uc_replacement_116):
    feature = _clean(uc_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_116'] = {'inputs': ['uc_replacement_116'], 'func': uc_replacement_d2_116}


def uc_replacement_d2_117(uc_replacement_117):
    feature = _clean(uc_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_117'] = {'inputs': ['uc_replacement_117'], 'func': uc_replacement_d2_117}


def uc_replacement_d2_118(uc_replacement_118):
    feature = _clean(uc_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_118'] = {'inputs': ['uc_replacement_118'], 'func': uc_replacement_d2_118}


def uc_replacement_d2_119(uc_replacement_119):
    feature = _clean(uc_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_119'] = {'inputs': ['uc_replacement_119'], 'func': uc_replacement_d2_119}


def uc_replacement_d2_120(uc_replacement_120):
    feature = _clean(uc_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_120'] = {'inputs': ['uc_replacement_120'], 'func': uc_replacement_d2_120}


def uc_replacement_d2_121(uc_replacement_121):
    feature = _clean(uc_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_121'] = {'inputs': ['uc_replacement_121'], 'func': uc_replacement_d2_121}


def uc_replacement_d2_122(uc_replacement_122):
    feature = _clean(uc_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_122'] = {'inputs': ['uc_replacement_122'], 'func': uc_replacement_d2_122}


def uc_replacement_d2_123(uc_replacement_123):
    feature = _clean(uc_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_123'] = {'inputs': ['uc_replacement_123'], 'func': uc_replacement_d2_123}


def uc_replacement_d2_124(uc_replacement_124):
    feature = _clean(uc_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_124'] = {'inputs': ['uc_replacement_124'], 'func': uc_replacement_d2_124}


def uc_replacement_d2_125(uc_replacement_125):
    feature = _clean(uc_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_125'] = {'inputs': ['uc_replacement_125'], 'func': uc_replacement_d2_125}


def uc_replacement_d2_126(uc_replacement_126):
    feature = _clean(uc_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_126'] = {'inputs': ['uc_replacement_126'], 'func': uc_replacement_d2_126}


def uc_replacement_d2_127(uc_replacement_127):
    feature = _clean(uc_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_127'] = {'inputs': ['uc_replacement_127'], 'func': uc_replacement_d2_127}


def uc_replacement_d2_128(uc_replacement_128):
    feature = _clean(uc_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_128'] = {'inputs': ['uc_replacement_128'], 'func': uc_replacement_d2_128}


def uc_replacement_d2_129(uc_replacement_129):
    feature = _clean(uc_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_129'] = {'inputs': ['uc_replacement_129'], 'func': uc_replacement_d2_129}


def uc_replacement_d2_130(uc_replacement_130):
    feature = _clean(uc_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_130'] = {'inputs': ['uc_replacement_130'], 'func': uc_replacement_d2_130}


def uc_replacement_d2_131(uc_replacement_131):
    feature = _clean(uc_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_131'] = {'inputs': ['uc_replacement_131'], 'func': uc_replacement_d2_131}


def uc_replacement_d2_132(uc_replacement_132):
    feature = _clean(uc_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_132'] = {'inputs': ['uc_replacement_132'], 'func': uc_replacement_d2_132}


def uc_replacement_d2_133(uc_replacement_133):
    feature = _clean(uc_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_133'] = {'inputs': ['uc_replacement_133'], 'func': uc_replacement_d2_133}


def uc_replacement_d2_134(uc_replacement_134):
    feature = _clean(uc_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_134'] = {'inputs': ['uc_replacement_134'], 'func': uc_replacement_d2_134}


def uc_replacement_d2_135(uc_replacement_135):
    feature = _clean(uc_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_135'] = {'inputs': ['uc_replacement_135'], 'func': uc_replacement_d2_135}


def uc_replacement_d2_136(uc_replacement_136):
    feature = _clean(uc_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_136'] = {'inputs': ['uc_replacement_136'], 'func': uc_replacement_d2_136}


def uc_replacement_d2_137(uc_replacement_137):
    feature = _clean(uc_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_137'] = {'inputs': ['uc_replacement_137'], 'func': uc_replacement_d2_137}


def uc_replacement_d2_138(uc_replacement_138):
    feature = _clean(uc_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_138'] = {'inputs': ['uc_replacement_138'], 'func': uc_replacement_d2_138}


def uc_replacement_d2_139(uc_replacement_139):
    feature = _clean(uc_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_139'] = {'inputs': ['uc_replacement_139'], 'func': uc_replacement_d2_139}


def uc_replacement_d2_140(uc_replacement_140):
    feature = _clean(uc_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_140'] = {'inputs': ['uc_replacement_140'], 'func': uc_replacement_d2_140}


def uc_replacement_d2_141(uc_replacement_141):
    feature = _clean(uc_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_141'] = {'inputs': ['uc_replacement_141'], 'func': uc_replacement_d2_141}


def uc_replacement_d2_142(uc_replacement_142):
    feature = _clean(uc_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_142'] = {'inputs': ['uc_replacement_142'], 'func': uc_replacement_d2_142}


def uc_replacement_d2_143(uc_replacement_143):
    feature = _clean(uc_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_143'] = {'inputs': ['uc_replacement_143'], 'func': uc_replacement_d2_143}


def uc_replacement_d2_144(uc_replacement_144):
    feature = _clean(uc_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_144'] = {'inputs': ['uc_replacement_144'], 'func': uc_replacement_d2_144}


def uc_replacement_d2_145(uc_replacement_145):
    feature = _clean(uc_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_145'] = {'inputs': ['uc_replacement_145'], 'func': uc_replacement_d2_145}


def uc_replacement_d2_146(uc_replacement_146):
    feature = _clean(uc_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_146'] = {'inputs': ['uc_replacement_146'], 'func': uc_replacement_d2_146}


def uc_replacement_d2_147(uc_replacement_147):
    feature = _clean(uc_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_147'] = {'inputs': ['uc_replacement_147'], 'func': uc_replacement_d2_147}


def uc_replacement_d2_148(uc_replacement_148):
    feature = _clean(uc_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_148'] = {'inputs': ['uc_replacement_148'], 'func': uc_replacement_d2_148}


def uc_replacement_d2_149(uc_replacement_149):
    feature = _clean(uc_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_149'] = {'inputs': ['uc_replacement_149'], 'func': uc_replacement_d2_149}


def uc_replacement_d2_150(uc_replacement_150):
    feature = _clean(uc_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_150'] = {'inputs': ['uc_replacement_150'], 'func': uc_replacement_d2_150}


def uc_replacement_d2_151(uc_replacement_151):
    feature = _clean(uc_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_151'] = {'inputs': ['uc_replacement_151'], 'func': uc_replacement_d2_151}


def uc_replacement_d2_152(uc_replacement_152):
    feature = _clean(uc_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_152'] = {'inputs': ['uc_replacement_152'], 'func': uc_replacement_d2_152}


def uc_replacement_d2_153(uc_replacement_153):
    feature = _clean(uc_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_153'] = {'inputs': ['uc_replacement_153'], 'func': uc_replacement_d2_153}


def uc_replacement_d2_154(uc_replacement_154):
    feature = _clean(uc_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_154'] = {'inputs': ['uc_replacement_154'], 'func': uc_replacement_d2_154}


def uc_replacement_d2_155(uc_replacement_155):
    feature = _clean(uc_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_155'] = {'inputs': ['uc_replacement_155'], 'func': uc_replacement_d2_155}


def uc_replacement_d2_156(uc_replacement_156):
    feature = _clean(uc_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_156'] = {'inputs': ['uc_replacement_156'], 'func': uc_replacement_d2_156}


def uc_replacement_d2_157(uc_replacement_157):
    feature = _clean(uc_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_157'] = {'inputs': ['uc_replacement_157'], 'func': uc_replacement_d2_157}


def uc_replacement_d2_158(uc_replacement_158):
    feature = _clean(uc_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_158'] = {'inputs': ['uc_replacement_158'], 'func': uc_replacement_d2_158}


def uc_replacement_d2_159(uc_replacement_159):
    feature = _clean(uc_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_159'] = {'inputs': ['uc_replacement_159'], 'func': uc_replacement_d2_159}


def uc_replacement_d2_160(uc_replacement_160):
    feature = _clean(uc_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_160'] = {'inputs': ['uc_replacement_160'], 'func': uc_replacement_d2_160}


def uc_replacement_d2_161(uc_replacement_161):
    feature = _clean(uc_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_161'] = {'inputs': ['uc_replacement_161'], 'func': uc_replacement_d2_161}


def uc_replacement_d2_162(uc_replacement_162):
    feature = _clean(uc_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_162'] = {'inputs': ['uc_replacement_162'], 'func': uc_replacement_d2_162}


def uc_replacement_d2_163(uc_replacement_163):
    feature = _clean(uc_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_163'] = {'inputs': ['uc_replacement_163'], 'func': uc_replacement_d2_163}


def uc_replacement_d2_164(uc_replacement_164):
    feature = _clean(uc_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_164'] = {'inputs': ['uc_replacement_164'], 'func': uc_replacement_d2_164}


def uc_replacement_d2_165(uc_replacement_165):
    feature = _clean(uc_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_165'] = {'inputs': ['uc_replacement_165'], 'func': uc_replacement_d2_165}


def uc_replacement_d2_166(uc_replacement_166):
    feature = _clean(uc_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_166'] = {'inputs': ['uc_replacement_166'], 'func': uc_replacement_d2_166}


def uc_replacement_d2_167(uc_replacement_167):
    feature = _clean(uc_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_167'] = {'inputs': ['uc_replacement_167'], 'func': uc_replacement_d2_167}


def uc_replacement_d2_168(uc_replacement_168):
    feature = _clean(uc_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_168'] = {'inputs': ['uc_replacement_168'], 'func': uc_replacement_d2_168}


def uc_replacement_d2_169(uc_replacement_169):
    feature = _clean(uc_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_169'] = {'inputs': ['uc_replacement_169'], 'func': uc_replacement_d2_169}


def uc_replacement_d2_170(uc_replacement_170):
    feature = _clean(uc_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
UC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['uc_replacement_d2_170'] = {'inputs': ['uc_replacement_170'], 'func': uc_replacement_d2_170}


# Base-universe derivative extensions for repaired first-base features.
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def uw_base_universe_d2_001_uw_002_low_distance_10_002(uw_002_low_distance_10_002):
    return _base_universe_d2(uw_002_low_distance_10_002, 1)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_001_uw_002_low_distance_10_002'] = {'inputs': ['uw_002_low_distance_10_002'], 'func': uw_base_universe_d2_001_uw_002_low_distance_10_002}


def uw_base_universe_d2_002_uw_003_underwater_area_21_003(uw_003_underwater_area_21_003):
    return _base_universe_d2(uw_003_underwater_area_21_003, 2)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_002_uw_003_underwater_area_21_003'] = {'inputs': ['uw_003_underwater_area_21_003'], 'func': uw_base_universe_d2_002_uw_003_underwater_area_21_003}


def uw_base_universe_d2_003_uw_006_lower_high_ratio_84_006(uw_006_lower_high_ratio_84_006):
    return _base_universe_d2(uw_006_lower_high_ratio_84_006, 3)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_003_uw_006_lower_high_ratio_84_006'] = {'inputs': ['uw_006_lower_high_ratio_84_006'], 'func': uw_base_universe_d2_003_uw_006_lower_high_ratio_84_006}


def uw_base_universe_d2_004_uw_008_low_distance_189_008(uw_008_low_distance_189_008):
    return _base_universe_d2(uw_008_low_distance_189_008, 4)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_004_uw_008_low_distance_189_008'] = {'inputs': ['uw_008_low_distance_189_008'], 'func': uw_base_universe_d2_004_uw_008_low_distance_189_008}


def uw_base_universe_d2_005_uw_009_underwater_area_252_009(uw_009_underwater_area_252_009):
    return _base_universe_d2(uw_009_underwater_area_252_009, 5)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_005_uw_009_underwater_area_252_009'] = {'inputs': ['uw_009_underwater_area_252_009'], 'func': uw_base_universe_d2_005_uw_009_underwater_area_252_009}


def uw_base_universe_d2_006_uw_012_lower_high_ratio_756_012(uw_012_lower_high_ratio_756_012):
    return _base_universe_d2(uw_012_lower_high_ratio_756_012, 6)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_006_uw_012_lower_high_ratio_756_012'] = {'inputs': ['uw_012_lower_high_ratio_756_012'], 'func': uw_base_universe_d2_006_uw_012_lower_high_ratio_756_012}


def uw_base_universe_d2_007_uw_014_low_distance_1260_014(uw_014_low_distance_1260_014):
    return _base_universe_d2(uw_014_low_distance_1260_014, 7)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_007_uw_014_low_distance_1260_014'] = {'inputs': ['uw_014_low_distance_1260_014'], 'func': uw_base_universe_d2_007_uw_014_low_distance_1260_014}


def uw_base_universe_d2_008_uw_015_underwater_area_1512_015(uw_015_underwater_area_1512_015):
    return _base_universe_d2(uw_015_underwater_area_1512_015, 8)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_008_uw_015_underwater_area_1512_015'] = {'inputs': ['uw_015_underwater_area_1512_015'], 'func': uw_base_universe_d2_008_uw_015_underwater_area_1512_015}


def uw_base_universe_d2_009_uw_018_lower_high_ratio_21_018(uw_018_lower_high_ratio_21_018):
    return _base_universe_d2(uw_018_lower_high_ratio_21_018, 9)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_009_uw_018_lower_high_ratio_21_018'] = {'inputs': ['uw_018_lower_high_ratio_21_018'], 'func': uw_base_universe_d2_009_uw_018_lower_high_ratio_21_018}


def uw_base_universe_d2_010_uw_020_low_distance_63_020(uw_020_low_distance_63_020):
    return _base_universe_d2(uw_020_low_distance_63_020, 10)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_010_uw_020_low_distance_63_020'] = {'inputs': ['uw_020_low_distance_63_020'], 'func': uw_base_universe_d2_010_uw_020_low_distance_63_020}


def uw_base_universe_d2_011_uw_021_underwater_area_84_021(uw_021_underwater_area_84_021):
    return _base_universe_d2(uw_021_underwater_area_84_021, 11)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_011_uw_021_underwater_area_84_021'] = {'inputs': ['uw_021_underwater_area_84_021'], 'func': uw_base_universe_d2_011_uw_021_underwater_area_84_021}


def uw_base_universe_d2_012_uw_024_lower_high_ratio_252_024(uw_024_lower_high_ratio_252_024):
    return _base_universe_d2(uw_024_lower_high_ratio_252_024, 12)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_012_uw_024_lower_high_ratio_252_024'] = {'inputs': ['uw_024_lower_high_ratio_252_024'], 'func': uw_base_universe_d2_012_uw_024_lower_high_ratio_252_024}


def uw_base_universe_d2_013_uw_026_low_distance_504_026(uw_026_low_distance_504_026):
    return _base_universe_d2(uw_026_low_distance_504_026, 13)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_013_uw_026_low_distance_504_026'] = {'inputs': ['uw_026_low_distance_504_026'], 'func': uw_base_universe_d2_013_uw_026_low_distance_504_026}


def uw_base_universe_d2_014_uw_027_underwater_area_756_027(uw_027_underwater_area_756_027):
    return _base_universe_d2(uw_027_underwater_area_756_027, 14)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_014_uw_027_underwater_area_756_027'] = {'inputs': ['uw_027_underwater_area_756_027'], 'func': uw_base_universe_d2_014_uw_027_underwater_area_756_027}


def uw_base_universe_d2_015_uw_030_lower_high_ratio_1512_030(uw_030_lower_high_ratio_1512_030):
    return _base_universe_d2(uw_030_lower_high_ratio_1512_030, 15)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_015_uw_030_lower_high_ratio_1512_030'] = {'inputs': ['uw_030_lower_high_ratio_1512_030'], 'func': uw_base_universe_d2_015_uw_030_lower_high_ratio_1512_030}


def uw_base_universe_d2_016_uw_basefill_004(uw_basefill_004):
    return _base_universe_d2(uw_basefill_004, 16)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_016_uw_basefill_004'] = {'inputs': ['uw_basefill_004'], 'func': uw_base_universe_d2_016_uw_basefill_004}


def uw_base_universe_d2_017_uw_basefill_005(uw_basefill_005):
    return _base_universe_d2(uw_basefill_005, 17)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_017_uw_basefill_005'] = {'inputs': ['uw_basefill_005'], 'func': uw_base_universe_d2_017_uw_basefill_005}


def uw_base_universe_d2_018_uw_basefill_010(uw_basefill_010):
    return _base_universe_d2(uw_basefill_010, 18)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_018_uw_basefill_010'] = {'inputs': ['uw_basefill_010'], 'func': uw_base_universe_d2_018_uw_basefill_010}


def uw_base_universe_d2_019_uw_basefill_011(uw_basefill_011):
    return _base_universe_d2(uw_basefill_011, 19)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_019_uw_basefill_011'] = {'inputs': ['uw_basefill_011'], 'func': uw_base_universe_d2_019_uw_basefill_011}


def uw_base_universe_d2_020_uw_basefill_016(uw_basefill_016):
    return _base_universe_d2(uw_basefill_016, 20)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_020_uw_basefill_016'] = {'inputs': ['uw_basefill_016'], 'func': uw_base_universe_d2_020_uw_basefill_016}


def uw_base_universe_d2_021_uw_basefill_017(uw_basefill_017):
    return _base_universe_d2(uw_basefill_017, 21)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_021_uw_basefill_017'] = {'inputs': ['uw_basefill_017'], 'func': uw_base_universe_d2_021_uw_basefill_017}


def uw_base_universe_d2_022_uw_basefill_022(uw_basefill_022):
    return _base_universe_d2(uw_basefill_022, 22)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_022_uw_basefill_022'] = {'inputs': ['uw_basefill_022'], 'func': uw_base_universe_d2_022_uw_basefill_022}


def uw_base_universe_d2_023_uw_basefill_023(uw_basefill_023):
    return _base_universe_d2(uw_basefill_023, 23)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_023_uw_basefill_023'] = {'inputs': ['uw_basefill_023'], 'func': uw_base_universe_d2_023_uw_basefill_023}


def uw_base_universe_d2_024_uw_basefill_028(uw_basefill_028):
    return _base_universe_d2(uw_basefill_028, 24)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_024_uw_basefill_028'] = {'inputs': ['uw_basefill_028'], 'func': uw_base_universe_d2_024_uw_basefill_028}


def uw_base_universe_d2_025_uw_basefill_029(uw_basefill_029):
    return _base_universe_d2(uw_basefill_029, 25)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_025_uw_basefill_029'] = {'inputs': ['uw_basefill_029'], 'func': uw_base_universe_d2_025_uw_basefill_029}


def uw_base_universe_d2_026_uw_basefill_031(uw_basefill_031):
    return _base_universe_d2(uw_basefill_031, 26)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_026_uw_basefill_031'] = {'inputs': ['uw_basefill_031'], 'func': uw_base_universe_d2_026_uw_basefill_031}


def uw_base_universe_d2_027_uw_basefill_032(uw_basefill_032):
    return _base_universe_d2(uw_basefill_032, 27)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_027_uw_basefill_032'] = {'inputs': ['uw_basefill_032'], 'func': uw_base_universe_d2_027_uw_basefill_032}


def uw_base_universe_d2_028_uw_basefill_033(uw_basefill_033):
    return _base_universe_d2(uw_basefill_033, 28)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_028_uw_basefill_033'] = {'inputs': ['uw_basefill_033'], 'func': uw_base_universe_d2_028_uw_basefill_033}


def uw_base_universe_d2_029_uw_basefill_034(uw_basefill_034):
    return _base_universe_d2(uw_basefill_034, 29)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_029_uw_basefill_034'] = {'inputs': ['uw_basefill_034'], 'func': uw_base_universe_d2_029_uw_basefill_034}


def uw_base_universe_d2_030_uw_basefill_035(uw_basefill_035):
    return _base_universe_d2(uw_basefill_035, 30)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_030_uw_basefill_035'] = {'inputs': ['uw_basefill_035'], 'func': uw_base_universe_d2_030_uw_basefill_035}


def uw_base_universe_d2_031_uw_basefill_036(uw_basefill_036):
    return _base_universe_d2(uw_basefill_036, 31)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_031_uw_basefill_036'] = {'inputs': ['uw_basefill_036'], 'func': uw_base_universe_d2_031_uw_basefill_036}


def uw_base_universe_d2_032_uw_basefill_037(uw_basefill_037):
    return _base_universe_d2(uw_basefill_037, 32)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_032_uw_basefill_037'] = {'inputs': ['uw_basefill_037'], 'func': uw_base_universe_d2_032_uw_basefill_037}


def uw_base_universe_d2_033_uw_basefill_038(uw_basefill_038):
    return _base_universe_d2(uw_basefill_038, 33)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_033_uw_basefill_038'] = {'inputs': ['uw_basefill_038'], 'func': uw_base_universe_d2_033_uw_basefill_038}


def uw_base_universe_d2_034_uw_basefill_039(uw_basefill_039):
    return _base_universe_d2(uw_basefill_039, 34)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_034_uw_basefill_039'] = {'inputs': ['uw_basefill_039'], 'func': uw_base_universe_d2_034_uw_basefill_039}


def uw_base_universe_d2_035_uw_basefill_040(uw_basefill_040):
    return _base_universe_d2(uw_basefill_040, 35)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_035_uw_basefill_040'] = {'inputs': ['uw_basefill_040'], 'func': uw_base_universe_d2_035_uw_basefill_040}


def uw_base_universe_d2_036_uw_basefill_041(uw_basefill_041):
    return _base_universe_d2(uw_basefill_041, 36)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_036_uw_basefill_041'] = {'inputs': ['uw_basefill_041'], 'func': uw_base_universe_d2_036_uw_basefill_041}


def uw_base_universe_d2_037_uw_basefill_042(uw_basefill_042):
    return _base_universe_d2(uw_basefill_042, 37)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_037_uw_basefill_042'] = {'inputs': ['uw_basefill_042'], 'func': uw_base_universe_d2_037_uw_basefill_042}


def uw_base_universe_d2_038_uw_basefill_043(uw_basefill_043):
    return _base_universe_d2(uw_basefill_043, 38)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_038_uw_basefill_043'] = {'inputs': ['uw_basefill_043'], 'func': uw_base_universe_d2_038_uw_basefill_043}


def uw_base_universe_d2_039_uw_basefill_044(uw_basefill_044):
    return _base_universe_d2(uw_basefill_044, 39)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_039_uw_basefill_044'] = {'inputs': ['uw_basefill_044'], 'func': uw_base_universe_d2_039_uw_basefill_044}


def uw_base_universe_d2_040_uw_basefill_045(uw_basefill_045):
    return _base_universe_d2(uw_basefill_045, 40)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_040_uw_basefill_045'] = {'inputs': ['uw_basefill_045'], 'func': uw_base_universe_d2_040_uw_basefill_045}


def uw_base_universe_d2_041_uw_basefill_046(uw_basefill_046):
    return _base_universe_d2(uw_basefill_046, 41)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_041_uw_basefill_046'] = {'inputs': ['uw_basefill_046'], 'func': uw_base_universe_d2_041_uw_basefill_046}


def uw_base_universe_d2_042_uw_basefill_047(uw_basefill_047):
    return _base_universe_d2(uw_basefill_047, 42)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_042_uw_basefill_047'] = {'inputs': ['uw_basefill_047'], 'func': uw_base_universe_d2_042_uw_basefill_047}


def uw_base_universe_d2_043_uw_basefill_048(uw_basefill_048):
    return _base_universe_d2(uw_basefill_048, 43)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_043_uw_basefill_048'] = {'inputs': ['uw_basefill_048'], 'func': uw_base_universe_d2_043_uw_basefill_048}


def uw_base_universe_d2_044_uw_basefill_049(uw_basefill_049):
    return _base_universe_d2(uw_basefill_049, 44)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_044_uw_basefill_049'] = {'inputs': ['uw_basefill_049'], 'func': uw_base_universe_d2_044_uw_basefill_049}


def uw_base_universe_d2_045_uw_basefill_050(uw_basefill_050):
    return _base_universe_d2(uw_basefill_050, 45)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_045_uw_basefill_050'] = {'inputs': ['uw_basefill_050'], 'func': uw_base_universe_d2_045_uw_basefill_050}


def uw_base_universe_d2_046_uw_basefill_051(uw_basefill_051):
    return _base_universe_d2(uw_basefill_051, 46)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_046_uw_basefill_051'] = {'inputs': ['uw_basefill_051'], 'func': uw_base_universe_d2_046_uw_basefill_051}


def uw_base_universe_d2_047_uw_basefill_052(uw_basefill_052):
    return _base_universe_d2(uw_basefill_052, 47)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_047_uw_basefill_052'] = {'inputs': ['uw_basefill_052'], 'func': uw_base_universe_d2_047_uw_basefill_052}


def uw_base_universe_d2_048_uw_basefill_053(uw_basefill_053):
    return _base_universe_d2(uw_basefill_053, 48)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_048_uw_basefill_053'] = {'inputs': ['uw_basefill_053'], 'func': uw_base_universe_d2_048_uw_basefill_053}


def uw_base_universe_d2_049_uw_basefill_054(uw_basefill_054):
    return _base_universe_d2(uw_basefill_054, 49)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_049_uw_basefill_054'] = {'inputs': ['uw_basefill_054'], 'func': uw_base_universe_d2_049_uw_basefill_054}


def uw_base_universe_d2_050_uw_basefill_055(uw_basefill_055):
    return _base_universe_d2(uw_basefill_055, 50)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_050_uw_basefill_055'] = {'inputs': ['uw_basefill_055'], 'func': uw_base_universe_d2_050_uw_basefill_055}


def uw_base_universe_d2_051_uw_basefill_056(uw_basefill_056):
    return _base_universe_d2(uw_basefill_056, 51)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_051_uw_basefill_056'] = {'inputs': ['uw_basefill_056'], 'func': uw_base_universe_d2_051_uw_basefill_056}


def uw_base_universe_d2_052_uw_basefill_057(uw_basefill_057):
    return _base_universe_d2(uw_basefill_057, 52)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_052_uw_basefill_057'] = {'inputs': ['uw_basefill_057'], 'func': uw_base_universe_d2_052_uw_basefill_057}


def uw_base_universe_d2_053_uw_basefill_058(uw_basefill_058):
    return _base_universe_d2(uw_basefill_058, 53)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_053_uw_basefill_058'] = {'inputs': ['uw_basefill_058'], 'func': uw_base_universe_d2_053_uw_basefill_058}


def uw_base_universe_d2_054_uw_basefill_059(uw_basefill_059):
    return _base_universe_d2(uw_basefill_059, 54)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_054_uw_basefill_059'] = {'inputs': ['uw_basefill_059'], 'func': uw_base_universe_d2_054_uw_basefill_059}


def uw_base_universe_d2_055_uw_basefill_060(uw_basefill_060):
    return _base_universe_d2(uw_basefill_060, 55)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_055_uw_basefill_060'] = {'inputs': ['uw_basefill_060'], 'func': uw_base_universe_d2_055_uw_basefill_060}


def uw_base_universe_d2_056_uw_basefill_061(uw_basefill_061):
    return _base_universe_d2(uw_basefill_061, 56)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_056_uw_basefill_061'] = {'inputs': ['uw_basefill_061'], 'func': uw_base_universe_d2_056_uw_basefill_061}


def uw_base_universe_d2_057_uw_basefill_062(uw_basefill_062):
    return _base_universe_d2(uw_basefill_062, 57)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_057_uw_basefill_062'] = {'inputs': ['uw_basefill_062'], 'func': uw_base_universe_d2_057_uw_basefill_062}


def uw_base_universe_d2_058_uw_basefill_063(uw_basefill_063):
    return _base_universe_d2(uw_basefill_063, 58)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_058_uw_basefill_063'] = {'inputs': ['uw_basefill_063'], 'func': uw_base_universe_d2_058_uw_basefill_063}


def uw_base_universe_d2_059_uw_basefill_064(uw_basefill_064):
    return _base_universe_d2(uw_basefill_064, 59)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_059_uw_basefill_064'] = {'inputs': ['uw_basefill_064'], 'func': uw_base_universe_d2_059_uw_basefill_064}


def uw_base_universe_d2_060_uw_basefill_065(uw_basefill_065):
    return _base_universe_d2(uw_basefill_065, 60)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_060_uw_basefill_065'] = {'inputs': ['uw_basefill_065'], 'func': uw_base_universe_d2_060_uw_basefill_065}


def uw_base_universe_d2_061_uw_basefill_066(uw_basefill_066):
    return _base_universe_d2(uw_basefill_066, 61)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_061_uw_basefill_066'] = {'inputs': ['uw_basefill_066'], 'func': uw_base_universe_d2_061_uw_basefill_066}


def uw_base_universe_d2_062_uw_basefill_067(uw_basefill_067):
    return _base_universe_d2(uw_basefill_067, 62)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_062_uw_basefill_067'] = {'inputs': ['uw_basefill_067'], 'func': uw_base_universe_d2_062_uw_basefill_067}


def uw_base_universe_d2_063_uw_basefill_068(uw_basefill_068):
    return _base_universe_d2(uw_basefill_068, 63)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_063_uw_basefill_068'] = {'inputs': ['uw_basefill_068'], 'func': uw_base_universe_d2_063_uw_basefill_068}


def uw_base_universe_d2_064_uw_basefill_069(uw_basefill_069):
    return _base_universe_d2(uw_basefill_069, 64)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_064_uw_basefill_069'] = {'inputs': ['uw_basefill_069'], 'func': uw_base_universe_d2_064_uw_basefill_069}


def uw_base_universe_d2_065_uw_basefill_070(uw_basefill_070):
    return _base_universe_d2(uw_basefill_070, 65)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_065_uw_basefill_070'] = {'inputs': ['uw_basefill_070'], 'func': uw_base_universe_d2_065_uw_basefill_070}


def uw_base_universe_d2_066_uw_basefill_071(uw_basefill_071):
    return _base_universe_d2(uw_basefill_071, 66)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_066_uw_basefill_071'] = {'inputs': ['uw_basefill_071'], 'func': uw_base_universe_d2_066_uw_basefill_071}


def uw_base_universe_d2_067_uw_basefill_072(uw_basefill_072):
    return _base_universe_d2(uw_basefill_072, 67)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_067_uw_basefill_072'] = {'inputs': ['uw_basefill_072'], 'func': uw_base_universe_d2_067_uw_basefill_072}


def uw_base_universe_d2_068_uw_basefill_073(uw_basefill_073):
    return _base_universe_d2(uw_basefill_073, 68)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_068_uw_basefill_073'] = {'inputs': ['uw_basefill_073'], 'func': uw_base_universe_d2_068_uw_basefill_073}


def uw_base_universe_d2_069_uw_basefill_074(uw_basefill_074):
    return _base_universe_d2(uw_basefill_074, 69)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_069_uw_basefill_074'] = {'inputs': ['uw_basefill_074'], 'func': uw_base_universe_d2_069_uw_basefill_074}


def uw_base_universe_d2_070_uw_basefill_075(uw_basefill_075):
    return _base_universe_d2(uw_basefill_075, 70)
UW_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['uw_base_universe_d2_070_uw_basefill_075'] = {'inputs': ['uw_basefill_075'], 'func': uw_base_universe_d2_070_uw_basefill_075}
