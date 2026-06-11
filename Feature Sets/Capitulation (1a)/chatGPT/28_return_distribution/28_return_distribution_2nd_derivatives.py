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



def rds_001_return_decay_roc_1(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 1)).reindex(feature.index)

def rds_007_return_decay_roc_5(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 5)).reindex(feature.index)

def rds_013_return_decay_roc_42(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 42)).reindex(feature.index)

def rds_154_rds_019_return_decay_42_019_roc_126(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 126)).reindex(feature.index)

def rds_155_rds_025_return_decay_5_025_roc_378(return_decay):
    feature = _s(return_decay)
    return (_roc(feature, 378)).reindex(feature.index)






















RETURN_DISTRIBUTION_REGISTRY_2ND_DERIVATIVES = {
    'rds_001_return_decay_roc_1': {'inputs': ['return_decay'], 'func': rds_001_return_decay_roc_1},
    'rds_007_return_decay_roc_5': {'inputs': ['return_decay'], 'func': rds_007_return_decay_roc_5},
    'rds_013_return_decay_roc_42': {'inputs': ['return_decay'], 'func': rds_013_return_decay_roc_42},
    'rds_154_rds_019_return_decay_42_019_roc_126': {'inputs': ['return_decay'], 'func': rds_154_rds_019_return_decay_42_019_roc_126},
    'rds_155_rds_025_return_decay_5_025_roc_378': {'inputs': ['return_decay'], 'func': rds_155_rds_025_return_decay_5_025_roc_378},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def rd_replacement_d2_001(rd_replacement_001):
    feature = _clean(rd_replacement_001)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_001'] = {'inputs': ['rd_replacement_001'], 'func': rd_replacement_d2_001}


def rd_replacement_d2_002(rd_replacement_002):
    feature = _clean(rd_replacement_002)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_002'] = {'inputs': ['rd_replacement_002'], 'func': rd_replacement_d2_002}


def rd_replacement_d2_003(rd_replacement_003):
    feature = _clean(rd_replacement_003)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_003'] = {'inputs': ['rd_replacement_003'], 'func': rd_replacement_d2_003}


def rd_replacement_d2_004(rd_replacement_004):
    feature = _clean(rd_replacement_004)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_004'] = {'inputs': ['rd_replacement_004'], 'func': rd_replacement_d2_004}


def rd_replacement_d2_005(rd_replacement_005):
    feature = _clean(rd_replacement_005)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_005'] = {'inputs': ['rd_replacement_005'], 'func': rd_replacement_d2_005}


def rd_replacement_d2_006(rd_replacement_006):
    feature = _clean(rd_replacement_006)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_006'] = {'inputs': ['rd_replacement_006'], 'func': rd_replacement_d2_006}


def rd_replacement_d2_007(rd_replacement_007):
    feature = _clean(rd_replacement_007)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_007'] = {'inputs': ['rd_replacement_007'], 'func': rd_replacement_d2_007}


def rd_replacement_d2_008(rd_replacement_008):
    feature = _clean(rd_replacement_008)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_008'] = {'inputs': ['rd_replacement_008'], 'func': rd_replacement_d2_008}


def rd_replacement_d2_009(rd_replacement_009):
    feature = _clean(rd_replacement_009)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_009'] = {'inputs': ['rd_replacement_009'], 'func': rd_replacement_d2_009}


def rd_replacement_d2_010(rd_replacement_010):
    feature = _clean(rd_replacement_010)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_010'] = {'inputs': ['rd_replacement_010'], 'func': rd_replacement_d2_010}


def rd_replacement_d2_011(rd_replacement_011):
    feature = _clean(rd_replacement_011)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_011'] = {'inputs': ['rd_replacement_011'], 'func': rd_replacement_d2_011}


def rd_replacement_d2_012(rd_replacement_012):
    feature = _clean(rd_replacement_012)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_012'] = {'inputs': ['rd_replacement_012'], 'func': rd_replacement_d2_012}


def rd_replacement_d2_013(rd_replacement_013):
    feature = _clean(rd_replacement_013)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_013'] = {'inputs': ['rd_replacement_013'], 'func': rd_replacement_d2_013}


def rd_replacement_d2_014(rd_replacement_014):
    feature = _clean(rd_replacement_014)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_014'] = {'inputs': ['rd_replacement_014'], 'func': rd_replacement_d2_014}


def rd_replacement_d2_015(rd_replacement_015):
    feature = _clean(rd_replacement_015)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_015'] = {'inputs': ['rd_replacement_015'], 'func': rd_replacement_d2_015}


def rd_replacement_d2_016(rd_replacement_016):
    feature = _clean(rd_replacement_016)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_016'] = {'inputs': ['rd_replacement_016'], 'func': rd_replacement_d2_016}


def rd_replacement_d2_017(rd_replacement_017):
    feature = _clean(rd_replacement_017)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_017'] = {'inputs': ['rd_replacement_017'], 'func': rd_replacement_d2_017}


def rd_replacement_d2_018(rd_replacement_018):
    feature = _clean(rd_replacement_018)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_018'] = {'inputs': ['rd_replacement_018'], 'func': rd_replacement_d2_018}


def rd_replacement_d2_019(rd_replacement_019):
    feature = _clean(rd_replacement_019)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_019'] = {'inputs': ['rd_replacement_019'], 'func': rd_replacement_d2_019}


def rd_replacement_d2_020(rd_replacement_020):
    feature = _clean(rd_replacement_020)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_020'] = {'inputs': ['rd_replacement_020'], 'func': rd_replacement_d2_020}


def rd_replacement_d2_021(rd_replacement_021):
    feature = _clean(rd_replacement_021)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_021'] = {'inputs': ['rd_replacement_021'], 'func': rd_replacement_d2_021}


def rd_replacement_d2_022(rd_replacement_022):
    feature = _clean(rd_replacement_022)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_022'] = {'inputs': ['rd_replacement_022'], 'func': rd_replacement_d2_022}


def rd_replacement_d2_023(rd_replacement_023):
    feature = _clean(rd_replacement_023)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_023'] = {'inputs': ['rd_replacement_023'], 'func': rd_replacement_d2_023}


def rd_replacement_d2_024(rd_replacement_024):
    feature = _clean(rd_replacement_024)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_024'] = {'inputs': ['rd_replacement_024'], 'func': rd_replacement_d2_024}


def rd_replacement_d2_025(rd_replacement_025):
    feature = _clean(rd_replacement_025)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_025'] = {'inputs': ['rd_replacement_025'], 'func': rd_replacement_d2_025}


def rd_replacement_d2_026(rd_replacement_026):
    feature = _clean(rd_replacement_026)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_026'] = {'inputs': ['rd_replacement_026'], 'func': rd_replacement_d2_026}


def rd_replacement_d2_027(rd_replacement_027):
    feature = _clean(rd_replacement_027)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_027'] = {'inputs': ['rd_replacement_027'], 'func': rd_replacement_d2_027}


def rd_replacement_d2_028(rd_replacement_028):
    feature = _clean(rd_replacement_028)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_028'] = {'inputs': ['rd_replacement_028'], 'func': rd_replacement_d2_028}


def rd_replacement_d2_029(rd_replacement_029):
    feature = _clean(rd_replacement_029)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_029'] = {'inputs': ['rd_replacement_029'], 'func': rd_replacement_d2_029}


def rd_replacement_d2_030(rd_replacement_030):
    feature = _clean(rd_replacement_030)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_030'] = {'inputs': ['rd_replacement_030'], 'func': rd_replacement_d2_030}


def rd_replacement_d2_031(rd_replacement_031):
    feature = _clean(rd_replacement_031)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_031'] = {'inputs': ['rd_replacement_031'], 'func': rd_replacement_d2_031}


def rd_replacement_d2_032(rd_replacement_032):
    feature = _clean(rd_replacement_032)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_032'] = {'inputs': ['rd_replacement_032'], 'func': rd_replacement_d2_032}


def rd_replacement_d2_033(rd_replacement_033):
    feature = _clean(rd_replacement_033)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_033'] = {'inputs': ['rd_replacement_033'], 'func': rd_replacement_d2_033}


def rd_replacement_d2_034(rd_replacement_034):
    feature = _clean(rd_replacement_034)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_034'] = {'inputs': ['rd_replacement_034'], 'func': rd_replacement_d2_034}


def rd_replacement_d2_035(rd_replacement_035):
    feature = _clean(rd_replacement_035)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_035'] = {'inputs': ['rd_replacement_035'], 'func': rd_replacement_d2_035}


def rd_replacement_d2_036(rd_replacement_036):
    feature = _clean(rd_replacement_036)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_036'] = {'inputs': ['rd_replacement_036'], 'func': rd_replacement_d2_036}


def rd_replacement_d2_037(rd_replacement_037):
    feature = _clean(rd_replacement_037)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_037'] = {'inputs': ['rd_replacement_037'], 'func': rd_replacement_d2_037}


def rd_replacement_d2_038(rd_replacement_038):
    feature = _clean(rd_replacement_038)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_038'] = {'inputs': ['rd_replacement_038'], 'func': rd_replacement_d2_038}


def rd_replacement_d2_039(rd_replacement_039):
    feature = _clean(rd_replacement_039)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_039'] = {'inputs': ['rd_replacement_039'], 'func': rd_replacement_d2_039}


def rd_replacement_d2_040(rd_replacement_040):
    feature = _clean(rd_replacement_040)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_040'] = {'inputs': ['rd_replacement_040'], 'func': rd_replacement_d2_040}


def rd_replacement_d2_041(rd_replacement_041):
    feature = _clean(rd_replacement_041)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_041'] = {'inputs': ['rd_replacement_041'], 'func': rd_replacement_d2_041}


def rd_replacement_d2_042(rd_replacement_042):
    feature = _clean(rd_replacement_042)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_042'] = {'inputs': ['rd_replacement_042'], 'func': rd_replacement_d2_042}


def rd_replacement_d2_043(rd_replacement_043):
    feature = _clean(rd_replacement_043)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_043'] = {'inputs': ['rd_replacement_043'], 'func': rd_replacement_d2_043}


def rd_replacement_d2_044(rd_replacement_044):
    feature = _clean(rd_replacement_044)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_044'] = {'inputs': ['rd_replacement_044'], 'func': rd_replacement_d2_044}


def rd_replacement_d2_045(rd_replacement_045):
    feature = _clean(rd_replacement_045)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_045'] = {'inputs': ['rd_replacement_045'], 'func': rd_replacement_d2_045}


def rd_replacement_d2_046(rd_replacement_046):
    feature = _clean(rd_replacement_046)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_046'] = {'inputs': ['rd_replacement_046'], 'func': rd_replacement_d2_046}


def rd_replacement_d2_047(rd_replacement_047):
    feature = _clean(rd_replacement_047)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_047'] = {'inputs': ['rd_replacement_047'], 'func': rd_replacement_d2_047}


def rd_replacement_d2_048(rd_replacement_048):
    feature = _clean(rd_replacement_048)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_048'] = {'inputs': ['rd_replacement_048'], 'func': rd_replacement_d2_048}


def rd_replacement_d2_049(rd_replacement_049):
    feature = _clean(rd_replacement_049)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_049'] = {'inputs': ['rd_replacement_049'], 'func': rd_replacement_d2_049}


def rd_replacement_d2_050(rd_replacement_050):
    feature = _clean(rd_replacement_050)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_050'] = {'inputs': ['rd_replacement_050'], 'func': rd_replacement_d2_050}


def rd_replacement_d2_051(rd_replacement_051):
    feature = _clean(rd_replacement_051)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_051'] = {'inputs': ['rd_replacement_051'], 'func': rd_replacement_d2_051}


def rd_replacement_d2_052(rd_replacement_052):
    feature = _clean(rd_replacement_052)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_052'] = {'inputs': ['rd_replacement_052'], 'func': rd_replacement_d2_052}


def rd_replacement_d2_053(rd_replacement_053):
    feature = _clean(rd_replacement_053)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_053'] = {'inputs': ['rd_replacement_053'], 'func': rd_replacement_d2_053}


def rd_replacement_d2_054(rd_replacement_054):
    feature = _clean(rd_replacement_054)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_054'] = {'inputs': ['rd_replacement_054'], 'func': rd_replacement_d2_054}


def rd_replacement_d2_055(rd_replacement_055):
    feature = _clean(rd_replacement_055)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_055'] = {'inputs': ['rd_replacement_055'], 'func': rd_replacement_d2_055}


def rd_replacement_d2_056(rd_replacement_056):
    feature = _clean(rd_replacement_056)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_056'] = {'inputs': ['rd_replacement_056'], 'func': rd_replacement_d2_056}


def rd_replacement_d2_057(rd_replacement_057):
    feature = _clean(rd_replacement_057)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_057'] = {'inputs': ['rd_replacement_057'], 'func': rd_replacement_d2_057}


def rd_replacement_d2_058(rd_replacement_058):
    feature = _clean(rd_replacement_058)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_058'] = {'inputs': ['rd_replacement_058'], 'func': rd_replacement_d2_058}


def rd_replacement_d2_059(rd_replacement_059):
    feature = _clean(rd_replacement_059)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_059'] = {'inputs': ['rd_replacement_059'], 'func': rd_replacement_d2_059}


def rd_replacement_d2_060(rd_replacement_060):
    feature = _clean(rd_replacement_060)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_060'] = {'inputs': ['rd_replacement_060'], 'func': rd_replacement_d2_060}


def rd_replacement_d2_061(rd_replacement_061):
    feature = _clean(rd_replacement_061)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_061'] = {'inputs': ['rd_replacement_061'], 'func': rd_replacement_d2_061}


def rd_replacement_d2_062(rd_replacement_062):
    feature = _clean(rd_replacement_062)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_062'] = {'inputs': ['rd_replacement_062'], 'func': rd_replacement_d2_062}


def rd_replacement_d2_063(rd_replacement_063):
    feature = _clean(rd_replacement_063)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_063'] = {'inputs': ['rd_replacement_063'], 'func': rd_replacement_d2_063}


def rd_replacement_d2_064(rd_replacement_064):
    feature = _clean(rd_replacement_064)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_064'] = {'inputs': ['rd_replacement_064'], 'func': rd_replacement_d2_064}


def rd_replacement_d2_065(rd_replacement_065):
    feature = _clean(rd_replacement_065)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_065'] = {'inputs': ['rd_replacement_065'], 'func': rd_replacement_d2_065}


def rd_replacement_d2_066(rd_replacement_066):
    feature = _clean(rd_replacement_066)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_066'] = {'inputs': ['rd_replacement_066'], 'func': rd_replacement_d2_066}


def rd_replacement_d2_067(rd_replacement_067):
    feature = _clean(rd_replacement_067)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_067'] = {'inputs': ['rd_replacement_067'], 'func': rd_replacement_d2_067}


def rd_replacement_d2_068(rd_replacement_068):
    feature = _clean(rd_replacement_068)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_068'] = {'inputs': ['rd_replacement_068'], 'func': rd_replacement_d2_068}


def rd_replacement_d2_069(rd_replacement_069):
    feature = _clean(rd_replacement_069)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_069'] = {'inputs': ['rd_replacement_069'], 'func': rd_replacement_d2_069}


def rd_replacement_d2_070(rd_replacement_070):
    feature = _clean(rd_replacement_070)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_070'] = {'inputs': ['rd_replacement_070'], 'func': rd_replacement_d2_070}


def rd_replacement_d2_071(rd_replacement_071):
    feature = _clean(rd_replacement_071)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_071'] = {'inputs': ['rd_replacement_071'], 'func': rd_replacement_d2_071}


def rd_replacement_d2_072(rd_replacement_072):
    feature = _clean(rd_replacement_072)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_072'] = {'inputs': ['rd_replacement_072'], 'func': rd_replacement_d2_072}


def rd_replacement_d2_073(rd_replacement_073):
    feature = _clean(rd_replacement_073)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_073'] = {'inputs': ['rd_replacement_073'], 'func': rd_replacement_d2_073}


def rd_replacement_d2_074(rd_replacement_074):
    feature = _clean(rd_replacement_074)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_074'] = {'inputs': ['rd_replacement_074'], 'func': rd_replacement_d2_074}


def rd_replacement_d2_075(rd_replacement_075):
    feature = _clean(rd_replacement_075)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_075'] = {'inputs': ['rd_replacement_075'], 'func': rd_replacement_d2_075}


def rd_replacement_d2_076(rd_replacement_076):
    feature = _clean(rd_replacement_076)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_076'] = {'inputs': ['rd_replacement_076'], 'func': rd_replacement_d2_076}


def rd_replacement_d2_077(rd_replacement_077):
    feature = _clean(rd_replacement_077)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_077'] = {'inputs': ['rd_replacement_077'], 'func': rd_replacement_d2_077}


def rd_replacement_d2_078(rd_replacement_078):
    feature = _clean(rd_replacement_078)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_078'] = {'inputs': ['rd_replacement_078'], 'func': rd_replacement_d2_078}


def rd_replacement_d2_079(rd_replacement_079):
    feature = _clean(rd_replacement_079)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_079'] = {'inputs': ['rd_replacement_079'], 'func': rd_replacement_d2_079}


def rd_replacement_d2_080(rd_replacement_080):
    feature = _clean(rd_replacement_080)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_080'] = {'inputs': ['rd_replacement_080'], 'func': rd_replacement_d2_080}


def rd_replacement_d2_081(rd_replacement_081):
    feature = _clean(rd_replacement_081)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_081'] = {'inputs': ['rd_replacement_081'], 'func': rd_replacement_d2_081}


def rd_replacement_d2_082(rd_replacement_082):
    feature = _clean(rd_replacement_082)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_082'] = {'inputs': ['rd_replacement_082'], 'func': rd_replacement_d2_082}


def rd_replacement_d2_083(rd_replacement_083):
    feature = _clean(rd_replacement_083)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_083'] = {'inputs': ['rd_replacement_083'], 'func': rd_replacement_d2_083}


def rd_replacement_d2_084(rd_replacement_084):
    feature = _clean(rd_replacement_084)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_084'] = {'inputs': ['rd_replacement_084'], 'func': rd_replacement_d2_084}


def rd_replacement_d2_085(rd_replacement_085):
    feature = _clean(rd_replacement_085)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_085'] = {'inputs': ['rd_replacement_085'], 'func': rd_replacement_d2_085}


def rd_replacement_d2_086(rd_replacement_086):
    feature = _clean(rd_replacement_086)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_086'] = {'inputs': ['rd_replacement_086'], 'func': rd_replacement_d2_086}


def rd_replacement_d2_087(rd_replacement_087):
    feature = _clean(rd_replacement_087)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_087'] = {'inputs': ['rd_replacement_087'], 'func': rd_replacement_d2_087}


def rd_replacement_d2_088(rd_replacement_088):
    feature = _clean(rd_replacement_088)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_088'] = {'inputs': ['rd_replacement_088'], 'func': rd_replacement_d2_088}


def rd_replacement_d2_089(rd_replacement_089):
    feature = _clean(rd_replacement_089)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_089'] = {'inputs': ['rd_replacement_089'], 'func': rd_replacement_d2_089}


def rd_replacement_d2_090(rd_replacement_090):
    feature = _clean(rd_replacement_090)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_090'] = {'inputs': ['rd_replacement_090'], 'func': rd_replacement_d2_090}


def rd_replacement_d2_091(rd_replacement_091):
    feature = _clean(rd_replacement_091)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_091'] = {'inputs': ['rd_replacement_091'], 'func': rd_replacement_d2_091}


def rd_replacement_d2_092(rd_replacement_092):
    feature = _clean(rd_replacement_092)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_092'] = {'inputs': ['rd_replacement_092'], 'func': rd_replacement_d2_092}


def rd_replacement_d2_093(rd_replacement_093):
    feature = _clean(rd_replacement_093)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_093'] = {'inputs': ['rd_replacement_093'], 'func': rd_replacement_d2_093}


def rd_replacement_d2_094(rd_replacement_094):
    feature = _clean(rd_replacement_094)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_094'] = {'inputs': ['rd_replacement_094'], 'func': rd_replacement_d2_094}


def rd_replacement_d2_095(rd_replacement_095):
    feature = _clean(rd_replacement_095)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_095'] = {'inputs': ['rd_replacement_095'], 'func': rd_replacement_d2_095}


def rd_replacement_d2_096(rd_replacement_096):
    feature = _clean(rd_replacement_096)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_096'] = {'inputs': ['rd_replacement_096'], 'func': rd_replacement_d2_096}


def rd_replacement_d2_097(rd_replacement_097):
    feature = _clean(rd_replacement_097)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_097'] = {'inputs': ['rd_replacement_097'], 'func': rd_replacement_d2_097}


def rd_replacement_d2_098(rd_replacement_098):
    feature = _clean(rd_replacement_098)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_098'] = {'inputs': ['rd_replacement_098'], 'func': rd_replacement_d2_098}


def rd_replacement_d2_099(rd_replacement_099):
    feature = _clean(rd_replacement_099)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_099'] = {'inputs': ['rd_replacement_099'], 'func': rd_replacement_d2_099}


def rd_replacement_d2_100(rd_replacement_100):
    feature = _clean(rd_replacement_100)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_100'] = {'inputs': ['rd_replacement_100'], 'func': rd_replacement_d2_100}


def rd_replacement_d2_101(rd_replacement_101):
    feature = _clean(rd_replacement_101)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_101'] = {'inputs': ['rd_replacement_101'], 'func': rd_replacement_d2_101}


def rd_replacement_d2_102(rd_replacement_102):
    feature = _clean(rd_replacement_102)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_102'] = {'inputs': ['rd_replacement_102'], 'func': rd_replacement_d2_102}


def rd_replacement_d2_103(rd_replacement_103):
    feature = _clean(rd_replacement_103)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_103'] = {'inputs': ['rd_replacement_103'], 'func': rd_replacement_d2_103}


def rd_replacement_d2_104(rd_replacement_104):
    feature = _clean(rd_replacement_104)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_104'] = {'inputs': ['rd_replacement_104'], 'func': rd_replacement_d2_104}


def rd_replacement_d2_105(rd_replacement_105):
    feature = _clean(rd_replacement_105)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_105'] = {'inputs': ['rd_replacement_105'], 'func': rd_replacement_d2_105}


def rd_replacement_d2_106(rd_replacement_106):
    feature = _clean(rd_replacement_106)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_106'] = {'inputs': ['rd_replacement_106'], 'func': rd_replacement_d2_106}


def rd_replacement_d2_107(rd_replacement_107):
    feature = _clean(rd_replacement_107)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_107'] = {'inputs': ['rd_replacement_107'], 'func': rd_replacement_d2_107}


def rd_replacement_d2_108(rd_replacement_108):
    feature = _clean(rd_replacement_108)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_108'] = {'inputs': ['rd_replacement_108'], 'func': rd_replacement_d2_108}


def rd_replacement_d2_109(rd_replacement_109):
    feature = _clean(rd_replacement_109)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_109'] = {'inputs': ['rd_replacement_109'], 'func': rd_replacement_d2_109}


def rd_replacement_d2_110(rd_replacement_110):
    feature = _clean(rd_replacement_110)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_110'] = {'inputs': ['rd_replacement_110'], 'func': rd_replacement_d2_110}


def rd_replacement_d2_111(rd_replacement_111):
    feature = _clean(rd_replacement_111)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_111'] = {'inputs': ['rd_replacement_111'], 'func': rd_replacement_d2_111}


def rd_replacement_d2_112(rd_replacement_112):
    feature = _clean(rd_replacement_112)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_112'] = {'inputs': ['rd_replacement_112'], 'func': rd_replacement_d2_112}


def rd_replacement_d2_113(rd_replacement_113):
    feature = _clean(rd_replacement_113)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_113'] = {'inputs': ['rd_replacement_113'], 'func': rd_replacement_d2_113}


def rd_replacement_d2_114(rd_replacement_114):
    feature = _clean(rd_replacement_114)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_114'] = {'inputs': ['rd_replacement_114'], 'func': rd_replacement_d2_114}


def rd_replacement_d2_115(rd_replacement_115):
    feature = _clean(rd_replacement_115)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_115'] = {'inputs': ['rd_replacement_115'], 'func': rd_replacement_d2_115}


def rd_replacement_d2_116(rd_replacement_116):
    feature = _clean(rd_replacement_116)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_116'] = {'inputs': ['rd_replacement_116'], 'func': rd_replacement_d2_116}


def rd_replacement_d2_117(rd_replacement_117):
    feature = _clean(rd_replacement_117)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_117'] = {'inputs': ['rd_replacement_117'], 'func': rd_replacement_d2_117}


def rd_replacement_d2_118(rd_replacement_118):
    feature = _clean(rd_replacement_118)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_118'] = {'inputs': ['rd_replacement_118'], 'func': rd_replacement_d2_118}


def rd_replacement_d2_119(rd_replacement_119):
    feature = _clean(rd_replacement_119)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_119'] = {'inputs': ['rd_replacement_119'], 'func': rd_replacement_d2_119}


def rd_replacement_d2_120(rd_replacement_120):
    feature = _clean(rd_replacement_120)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_120'] = {'inputs': ['rd_replacement_120'], 'func': rd_replacement_d2_120}


def rd_replacement_d2_121(rd_replacement_121):
    feature = _clean(rd_replacement_121)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_121'] = {'inputs': ['rd_replacement_121'], 'func': rd_replacement_d2_121}


def rd_replacement_d2_122(rd_replacement_122):
    feature = _clean(rd_replacement_122)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_122'] = {'inputs': ['rd_replacement_122'], 'func': rd_replacement_d2_122}


def rd_replacement_d2_123(rd_replacement_123):
    feature = _clean(rd_replacement_123)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_123'] = {'inputs': ['rd_replacement_123'], 'func': rd_replacement_d2_123}


def rd_replacement_d2_124(rd_replacement_124):
    feature = _clean(rd_replacement_124)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_124'] = {'inputs': ['rd_replacement_124'], 'func': rd_replacement_d2_124}


def rd_replacement_d2_125(rd_replacement_125):
    feature = _clean(rd_replacement_125)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_125'] = {'inputs': ['rd_replacement_125'], 'func': rd_replacement_d2_125}


def rd_replacement_d2_126(rd_replacement_126):
    feature = _clean(rd_replacement_126)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_126'] = {'inputs': ['rd_replacement_126'], 'func': rd_replacement_d2_126}


def rd_replacement_d2_127(rd_replacement_127):
    feature = _clean(rd_replacement_127)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_127'] = {'inputs': ['rd_replacement_127'], 'func': rd_replacement_d2_127}


def rd_replacement_d2_128(rd_replacement_128):
    feature = _clean(rd_replacement_128)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_128'] = {'inputs': ['rd_replacement_128'], 'func': rd_replacement_d2_128}


def rd_replacement_d2_129(rd_replacement_129):
    feature = _clean(rd_replacement_129)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_129'] = {'inputs': ['rd_replacement_129'], 'func': rd_replacement_d2_129}


def rd_replacement_d2_130(rd_replacement_130):
    feature = _clean(rd_replacement_130)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_130'] = {'inputs': ['rd_replacement_130'], 'func': rd_replacement_d2_130}


def rd_replacement_d2_131(rd_replacement_131):
    feature = _clean(rd_replacement_131)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_131'] = {'inputs': ['rd_replacement_131'], 'func': rd_replacement_d2_131}


def rd_replacement_d2_132(rd_replacement_132):
    feature = _clean(rd_replacement_132)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_132'] = {'inputs': ['rd_replacement_132'], 'func': rd_replacement_d2_132}


def rd_replacement_d2_133(rd_replacement_133):
    feature = _clean(rd_replacement_133)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_133'] = {'inputs': ['rd_replacement_133'], 'func': rd_replacement_d2_133}


def rd_replacement_d2_134(rd_replacement_134):
    feature = _clean(rd_replacement_134)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_134'] = {'inputs': ['rd_replacement_134'], 'func': rd_replacement_d2_134}


def rd_replacement_d2_135(rd_replacement_135):
    feature = _clean(rd_replacement_135)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_135'] = {'inputs': ['rd_replacement_135'], 'func': rd_replacement_d2_135}


def rd_replacement_d2_136(rd_replacement_136):
    feature = _clean(rd_replacement_136)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_136'] = {'inputs': ['rd_replacement_136'], 'func': rd_replacement_d2_136}


def rd_replacement_d2_137(rd_replacement_137):
    feature = _clean(rd_replacement_137)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_137'] = {'inputs': ['rd_replacement_137'], 'func': rd_replacement_d2_137}


def rd_replacement_d2_138(rd_replacement_138):
    feature = _clean(rd_replacement_138)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_138'] = {'inputs': ['rd_replacement_138'], 'func': rd_replacement_d2_138}


def rd_replacement_d2_139(rd_replacement_139):
    feature = _clean(rd_replacement_139)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00139000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_139'] = {'inputs': ['rd_replacement_139'], 'func': rd_replacement_d2_139}


def rd_replacement_d2_140(rd_replacement_140):
    feature = _clean(rd_replacement_140)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00140000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_140'] = {'inputs': ['rd_replacement_140'], 'func': rd_replacement_d2_140}


def rd_replacement_d2_141(rd_replacement_141):
    feature = _clean(rd_replacement_141)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00141000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_141'] = {'inputs': ['rd_replacement_141'], 'func': rd_replacement_d2_141}


def rd_replacement_d2_142(rd_replacement_142):
    feature = _clean(rd_replacement_142)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00142000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_142'] = {'inputs': ['rd_replacement_142'], 'func': rd_replacement_d2_142}


def rd_replacement_d2_143(rd_replacement_143):
    feature = _clean(rd_replacement_143)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00143000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_143'] = {'inputs': ['rd_replacement_143'], 'func': rd_replacement_d2_143}


def rd_replacement_d2_144(rd_replacement_144):
    feature = _clean(rd_replacement_144)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00144000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_144'] = {'inputs': ['rd_replacement_144'], 'func': rd_replacement_d2_144}


def rd_replacement_d2_145(rd_replacement_145):
    feature = _clean(rd_replacement_145)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00145000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_145'] = {'inputs': ['rd_replacement_145'], 'func': rd_replacement_d2_145}


def rd_replacement_d2_146(rd_replacement_146):
    feature = _clean(rd_replacement_146)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00146000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_146'] = {'inputs': ['rd_replacement_146'], 'func': rd_replacement_d2_146}


def rd_replacement_d2_147(rd_replacement_147):
    feature = _clean(rd_replacement_147)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00147000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_147'] = {'inputs': ['rd_replacement_147'], 'func': rd_replacement_d2_147}


def rd_replacement_d2_148(rd_replacement_148):
    feature = _clean(rd_replacement_148)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00148000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_148'] = {'inputs': ['rd_replacement_148'], 'func': rd_replacement_d2_148}


def rd_replacement_d2_149(rd_replacement_149):
    feature = _clean(rd_replacement_149)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00149000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_149'] = {'inputs': ['rd_replacement_149'], 'func': rd_replacement_d2_149}


def rd_replacement_d2_150(rd_replacement_150):
    feature = _clean(rd_replacement_150)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00150000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_150'] = {'inputs': ['rd_replacement_150'], 'func': rd_replacement_d2_150}


def rd_replacement_d2_151(rd_replacement_151):
    feature = _clean(rd_replacement_151)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00151000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_151'] = {'inputs': ['rd_replacement_151'], 'func': rd_replacement_d2_151}


def rd_replacement_d2_152(rd_replacement_152):
    feature = _clean(rd_replacement_152)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00152000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_152'] = {'inputs': ['rd_replacement_152'], 'func': rd_replacement_d2_152}


def rd_replacement_d2_153(rd_replacement_153):
    feature = _clean(rd_replacement_153)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00153000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_153'] = {'inputs': ['rd_replacement_153'], 'func': rd_replacement_d2_153}


def rd_replacement_d2_154(rd_replacement_154):
    feature = _clean(rd_replacement_154)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00154000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_154'] = {'inputs': ['rd_replacement_154'], 'func': rd_replacement_d2_154}


def rd_replacement_d2_155(rd_replacement_155):
    feature = _clean(rd_replacement_155)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00155000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_155'] = {'inputs': ['rd_replacement_155'], 'func': rd_replacement_d2_155}


def rd_replacement_d2_156(rd_replacement_156):
    feature = _clean(rd_replacement_156)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00156000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_156'] = {'inputs': ['rd_replacement_156'], 'func': rd_replacement_d2_156}


def rd_replacement_d2_157(rd_replacement_157):
    feature = _clean(rd_replacement_157)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00157000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_157'] = {'inputs': ['rd_replacement_157'], 'func': rd_replacement_d2_157}


def rd_replacement_d2_158(rd_replacement_158):
    feature = _clean(rd_replacement_158)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00158000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_158'] = {'inputs': ['rd_replacement_158'], 'func': rd_replacement_d2_158}


def rd_replacement_d2_159(rd_replacement_159):
    feature = _clean(rd_replacement_159)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00159000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_159'] = {'inputs': ['rd_replacement_159'], 'func': rd_replacement_d2_159}


def rd_replacement_d2_160(rd_replacement_160):
    feature = _clean(rd_replacement_160)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00160000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_160'] = {'inputs': ['rd_replacement_160'], 'func': rd_replacement_d2_160}


def rd_replacement_d2_161(rd_replacement_161):
    feature = _clean(rd_replacement_161)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00161000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_161'] = {'inputs': ['rd_replacement_161'], 'func': rd_replacement_d2_161}


def rd_replacement_d2_162(rd_replacement_162):
    feature = _clean(rd_replacement_162)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00162000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_162'] = {'inputs': ['rd_replacement_162'], 'func': rd_replacement_d2_162}


def rd_replacement_d2_163(rd_replacement_163):
    feature = _clean(rd_replacement_163)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00163000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_163'] = {'inputs': ['rd_replacement_163'], 'func': rd_replacement_d2_163}


def rd_replacement_d2_164(rd_replacement_164):
    feature = _clean(rd_replacement_164)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00164000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_164'] = {'inputs': ['rd_replacement_164'], 'func': rd_replacement_d2_164}


def rd_replacement_d2_165(rd_replacement_165):
    feature = _clean(rd_replacement_165)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00165000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_165'] = {'inputs': ['rd_replacement_165'], 'func': rd_replacement_d2_165}


def rd_replacement_d2_166(rd_replacement_166):
    feature = _clean(rd_replacement_166)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00166000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_166'] = {'inputs': ['rd_replacement_166'], 'func': rd_replacement_d2_166}


def rd_replacement_d2_167(rd_replacement_167):
    feature = _clean(rd_replacement_167)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00167000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_167'] = {'inputs': ['rd_replacement_167'], 'func': rd_replacement_d2_167}


def rd_replacement_d2_168(rd_replacement_168):
    feature = _clean(rd_replacement_168)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00168000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_168'] = {'inputs': ['rd_replacement_168'], 'func': rd_replacement_d2_168}


def rd_replacement_d2_169(rd_replacement_169):
    feature = _clean(rd_replacement_169)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00169000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_169'] = {'inputs': ['rd_replacement_169'], 'func': rd_replacement_d2_169}


def rd_replacement_d2_170(rd_replacement_170):
    feature = _clean(rd_replacement_170)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00170000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_170'] = {'inputs': ['rd_replacement_170'], 'func': rd_replacement_d2_170}


def rd_replacement_d2_171(rd_replacement_171):
    feature = _clean(rd_replacement_171)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00171000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_171'] = {'inputs': ['rd_replacement_171'], 'func': rd_replacement_d2_171}


def rd_replacement_d2_172(rd_replacement_172):
    feature = _clean(rd_replacement_172)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00172000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_172'] = {'inputs': ['rd_replacement_172'], 'func': rd_replacement_d2_172}


def rd_replacement_d2_173(rd_replacement_173):
    feature = _clean(rd_replacement_173)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00173000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_173'] = {'inputs': ['rd_replacement_173'], 'func': rd_replacement_d2_173}


def rd_replacement_d2_174(rd_replacement_174):
    feature = _clean(rd_replacement_174)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00174000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_174'] = {'inputs': ['rd_replacement_174'], 'func': rd_replacement_d2_174}


def rd_replacement_d2_175(rd_replacement_175):
    feature = _clean(rd_replacement_175)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00175000).reindex(feature.index)
RD_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['rd_replacement_d2_175'] = {'inputs': ['rd_replacement_175'], 'func': rd_replacement_d2_175}


# Base-universe derivative extensions for repaired first-base features.
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rds_base_universe_d2_001_rds_003_loss_streak_21_003(rds_003_loss_streak_21_003):
    return _base_universe_d2(rds_003_loss_streak_21_003, 1)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_001_rds_003_loss_streak_21_003'] = {'inputs': ['rds_003_loss_streak_21_003'], 'func': rds_base_universe_d2_001_rds_003_loss_streak_21_003}


def rds_base_universe_d2_002_rds_004_ma_distance_42_004(rds_004_ma_distance_42_004):
    return _base_universe_d2(rds_004_ma_distance_42_004, 2)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_002_rds_004_ma_distance_42_004'] = {'inputs': ['rds_004_ma_distance_42_004'], 'func': rds_base_universe_d2_002_rds_004_ma_distance_42_004}


def rds_base_universe_d2_003_rds_005_stochastic_position_63_005(rds_005_stochastic_position_63_005):
    return _base_universe_d2(rds_005_stochastic_position_63_005, 3)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_003_rds_005_stochastic_position_63_005'] = {'inputs': ['rds_005_stochastic_position_63_005'], 'func': rds_base_universe_d2_003_rds_005_stochastic_position_63_005}


def rds_base_universe_d2_004_rds_009_loss_streak_252_009(rds_009_loss_streak_252_009):
    return _base_universe_d2(rds_009_loss_streak_252_009, 4)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_004_rds_009_loss_streak_252_009'] = {'inputs': ['rds_009_loss_streak_252_009'], 'func': rds_base_universe_d2_004_rds_009_loss_streak_252_009}


def rds_base_universe_d2_005_rds_010_ma_distance_378_010(rds_010_ma_distance_378_010):
    return _base_universe_d2(rds_010_ma_distance_378_010, 5)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_005_rds_010_ma_distance_378_010'] = {'inputs': ['rds_010_ma_distance_378_010'], 'func': rds_base_universe_d2_005_rds_010_ma_distance_378_010}


def rds_base_universe_d2_006_rds_011_stochastic_position_504_011(rds_011_stochastic_position_504_011):
    return _base_universe_d2(rds_011_stochastic_position_504_011, 6)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_006_rds_011_stochastic_position_504_011'] = {'inputs': ['rds_011_stochastic_position_504_011'], 'func': rds_base_universe_d2_006_rds_011_stochastic_position_504_011}


def rds_base_universe_d2_007_rds_015_loss_streak_1512_015(rds_015_loss_streak_1512_015):
    return _base_universe_d2(rds_015_loss_streak_1512_015, 7)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_007_rds_015_loss_streak_1512_015'] = {'inputs': ['rds_015_loss_streak_1512_015'], 'func': rds_base_universe_d2_007_rds_015_loss_streak_1512_015}


def rds_base_universe_d2_008_rds_016_ma_distance_5_016(rds_016_ma_distance_5_016):
    return _base_universe_d2(rds_016_ma_distance_5_016, 8)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_008_rds_016_ma_distance_5_016'] = {'inputs': ['rds_016_ma_distance_5_016'], 'func': rds_base_universe_d2_008_rds_016_ma_distance_5_016}


def rds_base_universe_d2_009_rds_017_stochastic_position_10_017(rds_017_stochastic_position_10_017):
    return _base_universe_d2(rds_017_stochastic_position_10_017, 9)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_009_rds_017_stochastic_position_10_017'] = {'inputs': ['rds_017_stochastic_position_10_017'], 'func': rds_base_universe_d2_009_rds_017_stochastic_position_10_017}


def rds_base_universe_d2_010_rds_021_loss_streak_84_021(rds_021_loss_streak_84_021):
    return _base_universe_d2(rds_021_loss_streak_84_021, 10)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_010_rds_021_loss_streak_84_021'] = {'inputs': ['rds_021_loss_streak_84_021'], 'func': rds_base_universe_d2_010_rds_021_loss_streak_84_021}


def rds_base_universe_d2_011_rds_022_ma_distance_126_022(rds_022_ma_distance_126_022):
    return _base_universe_d2(rds_022_ma_distance_126_022, 11)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_011_rds_022_ma_distance_126_022'] = {'inputs': ['rds_022_ma_distance_126_022'], 'func': rds_base_universe_d2_011_rds_022_ma_distance_126_022}


def rds_base_universe_d2_012_rds_023_stochastic_position_189_023(rds_023_stochastic_position_189_023):
    return _base_universe_d2(rds_023_stochastic_position_189_023, 12)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_012_rds_023_stochastic_position_189_023'] = {'inputs': ['rds_023_stochastic_position_189_023'], 'func': rds_base_universe_d2_012_rds_023_stochastic_position_189_023}


def rds_base_universe_d2_013_rds_027_loss_streak_756_027(rds_027_loss_streak_756_027):
    return _base_universe_d2(rds_027_loss_streak_756_027, 13)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_013_rds_027_loss_streak_756_027'] = {'inputs': ['rds_027_loss_streak_756_027'], 'func': rds_base_universe_d2_013_rds_027_loss_streak_756_027}


def rds_base_universe_d2_014_rds_028_ma_distance_1008_028(rds_028_ma_distance_1008_028):
    return _base_universe_d2(rds_028_ma_distance_1008_028, 14)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_014_rds_028_ma_distance_1008_028'] = {'inputs': ['rds_028_ma_distance_1008_028'], 'func': rds_base_universe_d2_014_rds_028_ma_distance_1008_028}


def rds_base_universe_d2_015_rds_029_stochastic_position_1260_029(rds_029_stochastic_position_1260_029):
    return _base_universe_d2(rds_029_stochastic_position_1260_029, 15)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_015_rds_029_stochastic_position_1260_029'] = {'inputs': ['rds_029_stochastic_position_1260_029'], 'func': rds_base_universe_d2_015_rds_029_stochastic_position_1260_029}


def rds_base_universe_d2_016_rds_basefill_001(rds_basefill_001):
    return _base_universe_d2(rds_basefill_001, 16)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_016_rds_basefill_001'] = {'inputs': ['rds_basefill_001'], 'func': rds_base_universe_d2_016_rds_basefill_001}


def rds_base_universe_d2_017_rds_basefill_002(rds_basefill_002):
    return _base_universe_d2(rds_basefill_002, 17)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_017_rds_basefill_002'] = {'inputs': ['rds_basefill_002'], 'func': rds_base_universe_d2_017_rds_basefill_002}


def rds_base_universe_d2_018_rds_basefill_006(rds_basefill_006):
    return _base_universe_d2(rds_basefill_006, 18)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_018_rds_basefill_006'] = {'inputs': ['rds_basefill_006'], 'func': rds_base_universe_d2_018_rds_basefill_006}


def rds_base_universe_d2_019_rds_basefill_007(rds_basefill_007):
    return _base_universe_d2(rds_basefill_007, 19)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_019_rds_basefill_007'] = {'inputs': ['rds_basefill_007'], 'func': rds_base_universe_d2_019_rds_basefill_007}


def rds_base_universe_d2_020_rds_basefill_008(rds_basefill_008):
    return _base_universe_d2(rds_basefill_008, 20)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_020_rds_basefill_008'] = {'inputs': ['rds_basefill_008'], 'func': rds_base_universe_d2_020_rds_basefill_008}


def rds_base_universe_d2_021_rds_basefill_012(rds_basefill_012):
    return _base_universe_d2(rds_basefill_012, 21)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_021_rds_basefill_012'] = {'inputs': ['rds_basefill_012'], 'func': rds_base_universe_d2_021_rds_basefill_012}


def rds_base_universe_d2_022_rds_basefill_013(rds_basefill_013):
    return _base_universe_d2(rds_basefill_013, 22)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_022_rds_basefill_013'] = {'inputs': ['rds_basefill_013'], 'func': rds_base_universe_d2_022_rds_basefill_013}


def rds_base_universe_d2_023_rds_basefill_014(rds_basefill_014):
    return _base_universe_d2(rds_basefill_014, 23)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_023_rds_basefill_014'] = {'inputs': ['rds_basefill_014'], 'func': rds_base_universe_d2_023_rds_basefill_014}


def rds_base_universe_d2_024_rds_basefill_018(rds_basefill_018):
    return _base_universe_d2(rds_basefill_018, 24)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_024_rds_basefill_018'] = {'inputs': ['rds_basefill_018'], 'func': rds_base_universe_d2_024_rds_basefill_018}


def rds_base_universe_d2_025_rds_basefill_019(rds_basefill_019):
    return _base_universe_d2(rds_basefill_019, 25)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_025_rds_basefill_019'] = {'inputs': ['rds_basefill_019'], 'func': rds_base_universe_d2_025_rds_basefill_019}


def rds_base_universe_d2_026_rds_basefill_020(rds_basefill_020):
    return _base_universe_d2(rds_basefill_020, 26)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_026_rds_basefill_020'] = {'inputs': ['rds_basefill_020'], 'func': rds_base_universe_d2_026_rds_basefill_020}


def rds_base_universe_d2_027_rds_basefill_024(rds_basefill_024):
    return _base_universe_d2(rds_basefill_024, 27)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_027_rds_basefill_024'] = {'inputs': ['rds_basefill_024'], 'func': rds_base_universe_d2_027_rds_basefill_024}


def rds_base_universe_d2_028_rds_basefill_025(rds_basefill_025):
    return _base_universe_d2(rds_basefill_025, 28)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_028_rds_basefill_025'] = {'inputs': ['rds_basefill_025'], 'func': rds_base_universe_d2_028_rds_basefill_025}


def rds_base_universe_d2_029_rds_basefill_026(rds_basefill_026):
    return _base_universe_d2(rds_basefill_026, 29)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_029_rds_basefill_026'] = {'inputs': ['rds_basefill_026'], 'func': rds_base_universe_d2_029_rds_basefill_026}


def rds_base_universe_d2_030_rds_basefill_030(rds_basefill_030):
    return _base_universe_d2(rds_basefill_030, 30)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_030_rds_basefill_030'] = {'inputs': ['rds_basefill_030'], 'func': rds_base_universe_d2_030_rds_basefill_030}


def rds_base_universe_d2_031_rds_basefill_031(rds_basefill_031):
    return _base_universe_d2(rds_basefill_031, 31)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_031_rds_basefill_031'] = {'inputs': ['rds_basefill_031'], 'func': rds_base_universe_d2_031_rds_basefill_031}


def rds_base_universe_d2_032_rds_basefill_032(rds_basefill_032):
    return _base_universe_d2(rds_basefill_032, 32)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_032_rds_basefill_032'] = {'inputs': ['rds_basefill_032'], 'func': rds_base_universe_d2_032_rds_basefill_032}


def rds_base_universe_d2_033_rds_basefill_033(rds_basefill_033):
    return _base_universe_d2(rds_basefill_033, 33)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_033_rds_basefill_033'] = {'inputs': ['rds_basefill_033'], 'func': rds_base_universe_d2_033_rds_basefill_033}


def rds_base_universe_d2_034_rds_basefill_034(rds_basefill_034):
    return _base_universe_d2(rds_basefill_034, 34)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_034_rds_basefill_034'] = {'inputs': ['rds_basefill_034'], 'func': rds_base_universe_d2_034_rds_basefill_034}


def rds_base_universe_d2_035_rds_basefill_035(rds_basefill_035):
    return _base_universe_d2(rds_basefill_035, 35)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_035_rds_basefill_035'] = {'inputs': ['rds_basefill_035'], 'func': rds_base_universe_d2_035_rds_basefill_035}


def rds_base_universe_d2_036_rds_basefill_036(rds_basefill_036):
    return _base_universe_d2(rds_basefill_036, 36)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_036_rds_basefill_036'] = {'inputs': ['rds_basefill_036'], 'func': rds_base_universe_d2_036_rds_basefill_036}


def rds_base_universe_d2_037_rds_basefill_037(rds_basefill_037):
    return _base_universe_d2(rds_basefill_037, 37)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_037_rds_basefill_037'] = {'inputs': ['rds_basefill_037'], 'func': rds_base_universe_d2_037_rds_basefill_037}


def rds_base_universe_d2_038_rds_basefill_038(rds_basefill_038):
    return _base_universe_d2(rds_basefill_038, 38)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_038_rds_basefill_038'] = {'inputs': ['rds_basefill_038'], 'func': rds_base_universe_d2_038_rds_basefill_038}


def rds_base_universe_d2_039_rds_basefill_039(rds_basefill_039):
    return _base_universe_d2(rds_basefill_039, 39)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_039_rds_basefill_039'] = {'inputs': ['rds_basefill_039'], 'func': rds_base_universe_d2_039_rds_basefill_039}


def rds_base_universe_d2_040_rds_basefill_040(rds_basefill_040):
    return _base_universe_d2(rds_basefill_040, 40)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_040_rds_basefill_040'] = {'inputs': ['rds_basefill_040'], 'func': rds_base_universe_d2_040_rds_basefill_040}


def rds_base_universe_d2_041_rds_basefill_041(rds_basefill_041):
    return _base_universe_d2(rds_basefill_041, 41)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_041_rds_basefill_041'] = {'inputs': ['rds_basefill_041'], 'func': rds_base_universe_d2_041_rds_basefill_041}


def rds_base_universe_d2_042_rds_basefill_042(rds_basefill_042):
    return _base_universe_d2(rds_basefill_042, 42)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_042_rds_basefill_042'] = {'inputs': ['rds_basefill_042'], 'func': rds_base_universe_d2_042_rds_basefill_042}


def rds_base_universe_d2_043_rds_basefill_043(rds_basefill_043):
    return _base_universe_d2(rds_basefill_043, 43)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_043_rds_basefill_043'] = {'inputs': ['rds_basefill_043'], 'func': rds_base_universe_d2_043_rds_basefill_043}


def rds_base_universe_d2_044_rds_basefill_044(rds_basefill_044):
    return _base_universe_d2(rds_basefill_044, 44)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_044_rds_basefill_044'] = {'inputs': ['rds_basefill_044'], 'func': rds_base_universe_d2_044_rds_basefill_044}


def rds_base_universe_d2_045_rds_basefill_045(rds_basefill_045):
    return _base_universe_d2(rds_basefill_045, 45)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_045_rds_basefill_045'] = {'inputs': ['rds_basefill_045'], 'func': rds_base_universe_d2_045_rds_basefill_045}


def rds_base_universe_d2_046_rds_basefill_046(rds_basefill_046):
    return _base_universe_d2(rds_basefill_046, 46)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_046_rds_basefill_046'] = {'inputs': ['rds_basefill_046'], 'func': rds_base_universe_d2_046_rds_basefill_046}


def rds_base_universe_d2_047_rds_basefill_047(rds_basefill_047):
    return _base_universe_d2(rds_basefill_047, 47)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_047_rds_basefill_047'] = {'inputs': ['rds_basefill_047'], 'func': rds_base_universe_d2_047_rds_basefill_047}


def rds_base_universe_d2_048_rds_basefill_048(rds_basefill_048):
    return _base_universe_d2(rds_basefill_048, 48)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_048_rds_basefill_048'] = {'inputs': ['rds_basefill_048'], 'func': rds_base_universe_d2_048_rds_basefill_048}


def rds_base_universe_d2_049_rds_basefill_049(rds_basefill_049):
    return _base_universe_d2(rds_basefill_049, 49)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_049_rds_basefill_049'] = {'inputs': ['rds_basefill_049'], 'func': rds_base_universe_d2_049_rds_basefill_049}


def rds_base_universe_d2_050_rds_basefill_050(rds_basefill_050):
    return _base_universe_d2(rds_basefill_050, 50)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_050_rds_basefill_050'] = {'inputs': ['rds_basefill_050'], 'func': rds_base_universe_d2_050_rds_basefill_050}


def rds_base_universe_d2_051_rds_basefill_051(rds_basefill_051):
    return _base_universe_d2(rds_basefill_051, 51)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_051_rds_basefill_051'] = {'inputs': ['rds_basefill_051'], 'func': rds_base_universe_d2_051_rds_basefill_051}


def rds_base_universe_d2_052_rds_basefill_052(rds_basefill_052):
    return _base_universe_d2(rds_basefill_052, 52)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_052_rds_basefill_052'] = {'inputs': ['rds_basefill_052'], 'func': rds_base_universe_d2_052_rds_basefill_052}


def rds_base_universe_d2_053_rds_basefill_053(rds_basefill_053):
    return _base_universe_d2(rds_basefill_053, 53)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_053_rds_basefill_053'] = {'inputs': ['rds_basefill_053'], 'func': rds_base_universe_d2_053_rds_basefill_053}


def rds_base_universe_d2_054_rds_basefill_054(rds_basefill_054):
    return _base_universe_d2(rds_basefill_054, 54)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_054_rds_basefill_054'] = {'inputs': ['rds_basefill_054'], 'func': rds_base_universe_d2_054_rds_basefill_054}


def rds_base_universe_d2_055_rds_basefill_055(rds_basefill_055):
    return _base_universe_d2(rds_basefill_055, 55)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_055_rds_basefill_055'] = {'inputs': ['rds_basefill_055'], 'func': rds_base_universe_d2_055_rds_basefill_055}


def rds_base_universe_d2_056_rds_basefill_056(rds_basefill_056):
    return _base_universe_d2(rds_basefill_056, 56)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_056_rds_basefill_056'] = {'inputs': ['rds_basefill_056'], 'func': rds_base_universe_d2_056_rds_basefill_056}


def rds_base_universe_d2_057_rds_basefill_057(rds_basefill_057):
    return _base_universe_d2(rds_basefill_057, 57)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_057_rds_basefill_057'] = {'inputs': ['rds_basefill_057'], 'func': rds_base_universe_d2_057_rds_basefill_057}


def rds_base_universe_d2_058_rds_basefill_058(rds_basefill_058):
    return _base_universe_d2(rds_basefill_058, 58)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_058_rds_basefill_058'] = {'inputs': ['rds_basefill_058'], 'func': rds_base_universe_d2_058_rds_basefill_058}


def rds_base_universe_d2_059_rds_basefill_059(rds_basefill_059):
    return _base_universe_d2(rds_basefill_059, 59)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_059_rds_basefill_059'] = {'inputs': ['rds_basefill_059'], 'func': rds_base_universe_d2_059_rds_basefill_059}


def rds_base_universe_d2_060_rds_basefill_060(rds_basefill_060):
    return _base_universe_d2(rds_basefill_060, 60)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_060_rds_basefill_060'] = {'inputs': ['rds_basefill_060'], 'func': rds_base_universe_d2_060_rds_basefill_060}


def rds_base_universe_d2_061_rds_basefill_061(rds_basefill_061):
    return _base_universe_d2(rds_basefill_061, 61)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_061_rds_basefill_061'] = {'inputs': ['rds_basefill_061'], 'func': rds_base_universe_d2_061_rds_basefill_061}


def rds_base_universe_d2_062_rds_basefill_062(rds_basefill_062):
    return _base_universe_d2(rds_basefill_062, 62)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_062_rds_basefill_062'] = {'inputs': ['rds_basefill_062'], 'func': rds_base_universe_d2_062_rds_basefill_062}


def rds_base_universe_d2_063_rds_basefill_063(rds_basefill_063):
    return _base_universe_d2(rds_basefill_063, 63)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_063_rds_basefill_063'] = {'inputs': ['rds_basefill_063'], 'func': rds_base_universe_d2_063_rds_basefill_063}


def rds_base_universe_d2_064_rds_basefill_064(rds_basefill_064):
    return _base_universe_d2(rds_basefill_064, 64)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_064_rds_basefill_064'] = {'inputs': ['rds_basefill_064'], 'func': rds_base_universe_d2_064_rds_basefill_064}


def rds_base_universe_d2_065_rds_basefill_065(rds_basefill_065):
    return _base_universe_d2(rds_basefill_065, 65)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_065_rds_basefill_065'] = {'inputs': ['rds_basefill_065'], 'func': rds_base_universe_d2_065_rds_basefill_065}


def rds_base_universe_d2_066_rds_basefill_066(rds_basefill_066):
    return _base_universe_d2(rds_basefill_066, 66)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_066_rds_basefill_066'] = {'inputs': ['rds_basefill_066'], 'func': rds_base_universe_d2_066_rds_basefill_066}


def rds_base_universe_d2_067_rds_basefill_067(rds_basefill_067):
    return _base_universe_d2(rds_basefill_067, 67)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_067_rds_basefill_067'] = {'inputs': ['rds_basefill_067'], 'func': rds_base_universe_d2_067_rds_basefill_067}


def rds_base_universe_d2_068_rds_basefill_068(rds_basefill_068):
    return _base_universe_d2(rds_basefill_068, 68)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_068_rds_basefill_068'] = {'inputs': ['rds_basefill_068'], 'func': rds_base_universe_d2_068_rds_basefill_068}


def rds_base_universe_d2_069_rds_basefill_069(rds_basefill_069):
    return _base_universe_d2(rds_basefill_069, 69)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_069_rds_basefill_069'] = {'inputs': ['rds_basefill_069'], 'func': rds_base_universe_d2_069_rds_basefill_069}


def rds_base_universe_d2_070_rds_basefill_070(rds_basefill_070):
    return _base_universe_d2(rds_basefill_070, 70)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_070_rds_basefill_070'] = {'inputs': ['rds_basefill_070'], 'func': rds_base_universe_d2_070_rds_basefill_070}


def rds_base_universe_d2_071_rds_basefill_071(rds_basefill_071):
    return _base_universe_d2(rds_basefill_071, 71)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_071_rds_basefill_071'] = {'inputs': ['rds_basefill_071'], 'func': rds_base_universe_d2_071_rds_basefill_071}


def rds_base_universe_d2_072_rds_basefill_072(rds_basefill_072):
    return _base_universe_d2(rds_basefill_072, 72)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_072_rds_basefill_072'] = {'inputs': ['rds_basefill_072'], 'func': rds_base_universe_d2_072_rds_basefill_072}


def rds_base_universe_d2_073_rds_basefill_073(rds_basefill_073):
    return _base_universe_d2(rds_basefill_073, 73)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_073_rds_basefill_073'] = {'inputs': ['rds_basefill_073'], 'func': rds_base_universe_d2_073_rds_basefill_073}


def rds_base_universe_d2_074_rds_basefill_074(rds_basefill_074):
    return _base_universe_d2(rds_basefill_074, 74)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_074_rds_basefill_074'] = {'inputs': ['rds_basefill_074'], 'func': rds_base_universe_d2_074_rds_basefill_074}


def rds_base_universe_d2_075_rds_basefill_075(rds_basefill_075):
    return _base_universe_d2(rds_basefill_075, 75)
RDS_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['rds_base_universe_d2_075_rds_basefill_075'] = {'inputs': ['rds_basefill_075'], 'func': rds_base_universe_d2_075_rds_basefill_075}
