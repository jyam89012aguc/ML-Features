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



def rds_001_return_decay_accel_1(rds_001_return_decay_roc_1):
    feature = _s(rds_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rds_007_return_decay_accel_5(rds_007_return_decay_roc_5):
    feature = _s(rds_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def rds_013_return_decay_accel_42(rds_013_return_decay_roc_42):
    feature = _s(rds_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rds_179_rds_019_return_decay_42_019_accel_126(rds_154_rds_019_return_decay_42_019_roc_126):
    feature = _s(rds_154_rds_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rds_180_rds_025_return_decay_5_025_accel_378(rds_155_rds_025_return_decay_5_025_roc_378):
    feature = _s(rds_155_rds_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















RETURN_DISTRIBUTION_REGISTRY_3RD_DERIVATIVES = {
    'rds_001_return_decay_accel_1': {'inputs': ['rds_001_return_decay_roc_1'], 'func': rds_001_return_decay_accel_1},
    'rds_007_return_decay_accel_5': {'inputs': ['rds_007_return_decay_roc_5'], 'func': rds_007_return_decay_accel_5},
    'rds_013_return_decay_accel_42': {'inputs': ['rds_013_return_decay_roc_42'], 'func': rds_013_return_decay_accel_42},
    'rds_179_rds_019_return_decay_42_019_accel_126': {'inputs': ['rds_154_rds_019_return_decay_42_019_roc_126'], 'func': rds_179_rds_019_return_decay_42_019_accel_126},
    'rds_180_rds_025_return_decay_5_025_accel_378': {'inputs': ['rds_155_rds_025_return_decay_5_025_roc_378'], 'func': rds_180_rds_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def rd_replacement_d3_001(rd_replacement_d2_001):
    feature = _clean(rd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_001'] = {'inputs': ['rd_replacement_d2_001'], 'func': rd_replacement_d3_001}


def rd_replacement_d3_002(rd_replacement_d2_002):
    feature = _clean(rd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_002'] = {'inputs': ['rd_replacement_d2_002'], 'func': rd_replacement_d3_002}


def rd_replacement_d3_003(rd_replacement_d2_003):
    feature = _clean(rd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_003'] = {'inputs': ['rd_replacement_d2_003'], 'func': rd_replacement_d3_003}


def rd_replacement_d3_004(rd_replacement_d2_004):
    feature = _clean(rd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_004'] = {'inputs': ['rd_replacement_d2_004'], 'func': rd_replacement_d3_004}


def rd_replacement_d3_005(rd_replacement_d2_005):
    feature = _clean(rd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_005'] = {'inputs': ['rd_replacement_d2_005'], 'func': rd_replacement_d3_005}


def rd_replacement_d3_006(rd_replacement_d2_006):
    feature = _clean(rd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_006'] = {'inputs': ['rd_replacement_d2_006'], 'func': rd_replacement_d3_006}


def rd_replacement_d3_007(rd_replacement_d2_007):
    feature = _clean(rd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_007'] = {'inputs': ['rd_replacement_d2_007'], 'func': rd_replacement_d3_007}


def rd_replacement_d3_008(rd_replacement_d2_008):
    feature = _clean(rd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_008'] = {'inputs': ['rd_replacement_d2_008'], 'func': rd_replacement_d3_008}


def rd_replacement_d3_009(rd_replacement_d2_009):
    feature = _clean(rd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_009'] = {'inputs': ['rd_replacement_d2_009'], 'func': rd_replacement_d3_009}


def rd_replacement_d3_010(rd_replacement_d2_010):
    feature = _clean(rd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_010'] = {'inputs': ['rd_replacement_d2_010'], 'func': rd_replacement_d3_010}


def rd_replacement_d3_011(rd_replacement_d2_011):
    feature = _clean(rd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_011'] = {'inputs': ['rd_replacement_d2_011'], 'func': rd_replacement_d3_011}


def rd_replacement_d3_012(rd_replacement_d2_012):
    feature = _clean(rd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_012'] = {'inputs': ['rd_replacement_d2_012'], 'func': rd_replacement_d3_012}


def rd_replacement_d3_013(rd_replacement_d2_013):
    feature = _clean(rd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_013'] = {'inputs': ['rd_replacement_d2_013'], 'func': rd_replacement_d3_013}


def rd_replacement_d3_014(rd_replacement_d2_014):
    feature = _clean(rd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_014'] = {'inputs': ['rd_replacement_d2_014'], 'func': rd_replacement_d3_014}


def rd_replacement_d3_015(rd_replacement_d2_015):
    feature = _clean(rd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_015'] = {'inputs': ['rd_replacement_d2_015'], 'func': rd_replacement_d3_015}


def rd_replacement_d3_016(rd_replacement_d2_016):
    feature = _clean(rd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_016'] = {'inputs': ['rd_replacement_d2_016'], 'func': rd_replacement_d3_016}


def rd_replacement_d3_017(rd_replacement_d2_017):
    feature = _clean(rd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_017'] = {'inputs': ['rd_replacement_d2_017'], 'func': rd_replacement_d3_017}


def rd_replacement_d3_018(rd_replacement_d2_018):
    feature = _clean(rd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_018'] = {'inputs': ['rd_replacement_d2_018'], 'func': rd_replacement_d3_018}


def rd_replacement_d3_019(rd_replacement_d2_019):
    feature = _clean(rd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_019'] = {'inputs': ['rd_replacement_d2_019'], 'func': rd_replacement_d3_019}


def rd_replacement_d3_020(rd_replacement_d2_020):
    feature = _clean(rd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_020'] = {'inputs': ['rd_replacement_d2_020'], 'func': rd_replacement_d3_020}


def rd_replacement_d3_021(rd_replacement_d2_021):
    feature = _clean(rd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_021'] = {'inputs': ['rd_replacement_d2_021'], 'func': rd_replacement_d3_021}


def rd_replacement_d3_022(rd_replacement_d2_022):
    feature = _clean(rd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_022'] = {'inputs': ['rd_replacement_d2_022'], 'func': rd_replacement_d3_022}


def rd_replacement_d3_023(rd_replacement_d2_023):
    feature = _clean(rd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_023'] = {'inputs': ['rd_replacement_d2_023'], 'func': rd_replacement_d3_023}


def rd_replacement_d3_024(rd_replacement_d2_024):
    feature = _clean(rd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_024'] = {'inputs': ['rd_replacement_d2_024'], 'func': rd_replacement_d3_024}


def rd_replacement_d3_025(rd_replacement_d2_025):
    feature = _clean(rd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_025'] = {'inputs': ['rd_replacement_d2_025'], 'func': rd_replacement_d3_025}


def rd_replacement_d3_026(rd_replacement_d2_026):
    feature = _clean(rd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_026'] = {'inputs': ['rd_replacement_d2_026'], 'func': rd_replacement_d3_026}


def rd_replacement_d3_027(rd_replacement_d2_027):
    feature = _clean(rd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_027'] = {'inputs': ['rd_replacement_d2_027'], 'func': rd_replacement_d3_027}


def rd_replacement_d3_028(rd_replacement_d2_028):
    feature = _clean(rd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_028'] = {'inputs': ['rd_replacement_d2_028'], 'func': rd_replacement_d3_028}


def rd_replacement_d3_029(rd_replacement_d2_029):
    feature = _clean(rd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_029'] = {'inputs': ['rd_replacement_d2_029'], 'func': rd_replacement_d3_029}


def rd_replacement_d3_030(rd_replacement_d2_030):
    feature = _clean(rd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_030'] = {'inputs': ['rd_replacement_d2_030'], 'func': rd_replacement_d3_030}


def rd_replacement_d3_031(rd_replacement_d2_031):
    feature = _clean(rd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_031'] = {'inputs': ['rd_replacement_d2_031'], 'func': rd_replacement_d3_031}


def rd_replacement_d3_032(rd_replacement_d2_032):
    feature = _clean(rd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_032'] = {'inputs': ['rd_replacement_d2_032'], 'func': rd_replacement_d3_032}


def rd_replacement_d3_033(rd_replacement_d2_033):
    feature = _clean(rd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_033'] = {'inputs': ['rd_replacement_d2_033'], 'func': rd_replacement_d3_033}


def rd_replacement_d3_034(rd_replacement_d2_034):
    feature = _clean(rd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_034'] = {'inputs': ['rd_replacement_d2_034'], 'func': rd_replacement_d3_034}


def rd_replacement_d3_035(rd_replacement_d2_035):
    feature = _clean(rd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_035'] = {'inputs': ['rd_replacement_d2_035'], 'func': rd_replacement_d3_035}


def rd_replacement_d3_036(rd_replacement_d2_036):
    feature = _clean(rd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_036'] = {'inputs': ['rd_replacement_d2_036'], 'func': rd_replacement_d3_036}


def rd_replacement_d3_037(rd_replacement_d2_037):
    feature = _clean(rd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_037'] = {'inputs': ['rd_replacement_d2_037'], 'func': rd_replacement_d3_037}


def rd_replacement_d3_038(rd_replacement_d2_038):
    feature = _clean(rd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_038'] = {'inputs': ['rd_replacement_d2_038'], 'func': rd_replacement_d3_038}


def rd_replacement_d3_039(rd_replacement_d2_039):
    feature = _clean(rd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_039'] = {'inputs': ['rd_replacement_d2_039'], 'func': rd_replacement_d3_039}


def rd_replacement_d3_040(rd_replacement_d2_040):
    feature = _clean(rd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_040'] = {'inputs': ['rd_replacement_d2_040'], 'func': rd_replacement_d3_040}


def rd_replacement_d3_041(rd_replacement_d2_041):
    feature = _clean(rd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_041'] = {'inputs': ['rd_replacement_d2_041'], 'func': rd_replacement_d3_041}


def rd_replacement_d3_042(rd_replacement_d2_042):
    feature = _clean(rd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_042'] = {'inputs': ['rd_replacement_d2_042'], 'func': rd_replacement_d3_042}


def rd_replacement_d3_043(rd_replacement_d2_043):
    feature = _clean(rd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_043'] = {'inputs': ['rd_replacement_d2_043'], 'func': rd_replacement_d3_043}


def rd_replacement_d3_044(rd_replacement_d2_044):
    feature = _clean(rd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_044'] = {'inputs': ['rd_replacement_d2_044'], 'func': rd_replacement_d3_044}


def rd_replacement_d3_045(rd_replacement_d2_045):
    feature = _clean(rd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_045'] = {'inputs': ['rd_replacement_d2_045'], 'func': rd_replacement_d3_045}


def rd_replacement_d3_046(rd_replacement_d2_046):
    feature = _clean(rd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_046'] = {'inputs': ['rd_replacement_d2_046'], 'func': rd_replacement_d3_046}


def rd_replacement_d3_047(rd_replacement_d2_047):
    feature = _clean(rd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_047'] = {'inputs': ['rd_replacement_d2_047'], 'func': rd_replacement_d3_047}


def rd_replacement_d3_048(rd_replacement_d2_048):
    feature = _clean(rd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_048'] = {'inputs': ['rd_replacement_d2_048'], 'func': rd_replacement_d3_048}


def rd_replacement_d3_049(rd_replacement_d2_049):
    feature = _clean(rd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_049'] = {'inputs': ['rd_replacement_d2_049'], 'func': rd_replacement_d3_049}


def rd_replacement_d3_050(rd_replacement_d2_050):
    feature = _clean(rd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_050'] = {'inputs': ['rd_replacement_d2_050'], 'func': rd_replacement_d3_050}


def rd_replacement_d3_051(rd_replacement_d2_051):
    feature = _clean(rd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_051'] = {'inputs': ['rd_replacement_d2_051'], 'func': rd_replacement_d3_051}


def rd_replacement_d3_052(rd_replacement_d2_052):
    feature = _clean(rd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_052'] = {'inputs': ['rd_replacement_d2_052'], 'func': rd_replacement_d3_052}


def rd_replacement_d3_053(rd_replacement_d2_053):
    feature = _clean(rd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_053'] = {'inputs': ['rd_replacement_d2_053'], 'func': rd_replacement_d3_053}


def rd_replacement_d3_054(rd_replacement_d2_054):
    feature = _clean(rd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_054'] = {'inputs': ['rd_replacement_d2_054'], 'func': rd_replacement_d3_054}


def rd_replacement_d3_055(rd_replacement_d2_055):
    feature = _clean(rd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_055'] = {'inputs': ['rd_replacement_d2_055'], 'func': rd_replacement_d3_055}


def rd_replacement_d3_056(rd_replacement_d2_056):
    feature = _clean(rd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_056'] = {'inputs': ['rd_replacement_d2_056'], 'func': rd_replacement_d3_056}


def rd_replacement_d3_057(rd_replacement_d2_057):
    feature = _clean(rd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_057'] = {'inputs': ['rd_replacement_d2_057'], 'func': rd_replacement_d3_057}


def rd_replacement_d3_058(rd_replacement_d2_058):
    feature = _clean(rd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_058'] = {'inputs': ['rd_replacement_d2_058'], 'func': rd_replacement_d3_058}


def rd_replacement_d3_059(rd_replacement_d2_059):
    feature = _clean(rd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_059'] = {'inputs': ['rd_replacement_d2_059'], 'func': rd_replacement_d3_059}


def rd_replacement_d3_060(rd_replacement_d2_060):
    feature = _clean(rd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_060'] = {'inputs': ['rd_replacement_d2_060'], 'func': rd_replacement_d3_060}


def rd_replacement_d3_061(rd_replacement_d2_061):
    feature = _clean(rd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_061'] = {'inputs': ['rd_replacement_d2_061'], 'func': rd_replacement_d3_061}


def rd_replacement_d3_062(rd_replacement_d2_062):
    feature = _clean(rd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_062'] = {'inputs': ['rd_replacement_d2_062'], 'func': rd_replacement_d3_062}


def rd_replacement_d3_063(rd_replacement_d2_063):
    feature = _clean(rd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_063'] = {'inputs': ['rd_replacement_d2_063'], 'func': rd_replacement_d3_063}


def rd_replacement_d3_064(rd_replacement_d2_064):
    feature = _clean(rd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_064'] = {'inputs': ['rd_replacement_d2_064'], 'func': rd_replacement_d3_064}


def rd_replacement_d3_065(rd_replacement_d2_065):
    feature = _clean(rd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_065'] = {'inputs': ['rd_replacement_d2_065'], 'func': rd_replacement_d3_065}


def rd_replacement_d3_066(rd_replacement_d2_066):
    feature = _clean(rd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_066'] = {'inputs': ['rd_replacement_d2_066'], 'func': rd_replacement_d3_066}


def rd_replacement_d3_067(rd_replacement_d2_067):
    feature = _clean(rd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_067'] = {'inputs': ['rd_replacement_d2_067'], 'func': rd_replacement_d3_067}


def rd_replacement_d3_068(rd_replacement_d2_068):
    feature = _clean(rd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_068'] = {'inputs': ['rd_replacement_d2_068'], 'func': rd_replacement_d3_068}


def rd_replacement_d3_069(rd_replacement_d2_069):
    feature = _clean(rd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_069'] = {'inputs': ['rd_replacement_d2_069'], 'func': rd_replacement_d3_069}


def rd_replacement_d3_070(rd_replacement_d2_070):
    feature = _clean(rd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_070'] = {'inputs': ['rd_replacement_d2_070'], 'func': rd_replacement_d3_070}


def rd_replacement_d3_071(rd_replacement_d2_071):
    feature = _clean(rd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_071'] = {'inputs': ['rd_replacement_d2_071'], 'func': rd_replacement_d3_071}


def rd_replacement_d3_072(rd_replacement_d2_072):
    feature = _clean(rd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_072'] = {'inputs': ['rd_replacement_d2_072'], 'func': rd_replacement_d3_072}


def rd_replacement_d3_073(rd_replacement_d2_073):
    feature = _clean(rd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_073'] = {'inputs': ['rd_replacement_d2_073'], 'func': rd_replacement_d3_073}


def rd_replacement_d3_074(rd_replacement_d2_074):
    feature = _clean(rd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_074'] = {'inputs': ['rd_replacement_d2_074'], 'func': rd_replacement_d3_074}


def rd_replacement_d3_075(rd_replacement_d2_075):
    feature = _clean(rd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_075'] = {'inputs': ['rd_replacement_d2_075'], 'func': rd_replacement_d3_075}


def rd_replacement_d3_076(rd_replacement_d2_076):
    feature = _clean(rd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_076'] = {'inputs': ['rd_replacement_d2_076'], 'func': rd_replacement_d3_076}


def rd_replacement_d3_077(rd_replacement_d2_077):
    feature = _clean(rd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_077'] = {'inputs': ['rd_replacement_d2_077'], 'func': rd_replacement_d3_077}


def rd_replacement_d3_078(rd_replacement_d2_078):
    feature = _clean(rd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_078'] = {'inputs': ['rd_replacement_d2_078'], 'func': rd_replacement_d3_078}


def rd_replacement_d3_079(rd_replacement_d2_079):
    feature = _clean(rd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_079'] = {'inputs': ['rd_replacement_d2_079'], 'func': rd_replacement_d3_079}


def rd_replacement_d3_080(rd_replacement_d2_080):
    feature = _clean(rd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_080'] = {'inputs': ['rd_replacement_d2_080'], 'func': rd_replacement_d3_080}


def rd_replacement_d3_081(rd_replacement_d2_081):
    feature = _clean(rd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_081'] = {'inputs': ['rd_replacement_d2_081'], 'func': rd_replacement_d3_081}


def rd_replacement_d3_082(rd_replacement_d2_082):
    feature = _clean(rd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_082'] = {'inputs': ['rd_replacement_d2_082'], 'func': rd_replacement_d3_082}


def rd_replacement_d3_083(rd_replacement_d2_083):
    feature = _clean(rd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_083'] = {'inputs': ['rd_replacement_d2_083'], 'func': rd_replacement_d3_083}


def rd_replacement_d3_084(rd_replacement_d2_084):
    feature = _clean(rd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_084'] = {'inputs': ['rd_replacement_d2_084'], 'func': rd_replacement_d3_084}


def rd_replacement_d3_085(rd_replacement_d2_085):
    feature = _clean(rd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_085'] = {'inputs': ['rd_replacement_d2_085'], 'func': rd_replacement_d3_085}


def rd_replacement_d3_086(rd_replacement_d2_086):
    feature = _clean(rd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_086'] = {'inputs': ['rd_replacement_d2_086'], 'func': rd_replacement_d3_086}


def rd_replacement_d3_087(rd_replacement_d2_087):
    feature = _clean(rd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_087'] = {'inputs': ['rd_replacement_d2_087'], 'func': rd_replacement_d3_087}


def rd_replacement_d3_088(rd_replacement_d2_088):
    feature = _clean(rd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_088'] = {'inputs': ['rd_replacement_d2_088'], 'func': rd_replacement_d3_088}


def rd_replacement_d3_089(rd_replacement_d2_089):
    feature = _clean(rd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_089'] = {'inputs': ['rd_replacement_d2_089'], 'func': rd_replacement_d3_089}


def rd_replacement_d3_090(rd_replacement_d2_090):
    feature = _clean(rd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_090'] = {'inputs': ['rd_replacement_d2_090'], 'func': rd_replacement_d3_090}


def rd_replacement_d3_091(rd_replacement_d2_091):
    feature = _clean(rd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_091'] = {'inputs': ['rd_replacement_d2_091'], 'func': rd_replacement_d3_091}


def rd_replacement_d3_092(rd_replacement_d2_092):
    feature = _clean(rd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_092'] = {'inputs': ['rd_replacement_d2_092'], 'func': rd_replacement_d3_092}


def rd_replacement_d3_093(rd_replacement_d2_093):
    feature = _clean(rd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_093'] = {'inputs': ['rd_replacement_d2_093'], 'func': rd_replacement_d3_093}


def rd_replacement_d3_094(rd_replacement_d2_094):
    feature = _clean(rd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_094'] = {'inputs': ['rd_replacement_d2_094'], 'func': rd_replacement_d3_094}


def rd_replacement_d3_095(rd_replacement_d2_095):
    feature = _clean(rd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_095'] = {'inputs': ['rd_replacement_d2_095'], 'func': rd_replacement_d3_095}


def rd_replacement_d3_096(rd_replacement_d2_096):
    feature = _clean(rd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_096'] = {'inputs': ['rd_replacement_d2_096'], 'func': rd_replacement_d3_096}


def rd_replacement_d3_097(rd_replacement_d2_097):
    feature = _clean(rd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_097'] = {'inputs': ['rd_replacement_d2_097'], 'func': rd_replacement_d3_097}


def rd_replacement_d3_098(rd_replacement_d2_098):
    feature = _clean(rd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_098'] = {'inputs': ['rd_replacement_d2_098'], 'func': rd_replacement_d3_098}


def rd_replacement_d3_099(rd_replacement_d2_099):
    feature = _clean(rd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_099'] = {'inputs': ['rd_replacement_d2_099'], 'func': rd_replacement_d3_099}


def rd_replacement_d3_100(rd_replacement_d2_100):
    feature = _clean(rd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_100'] = {'inputs': ['rd_replacement_d2_100'], 'func': rd_replacement_d3_100}


def rd_replacement_d3_101(rd_replacement_d2_101):
    feature = _clean(rd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_101'] = {'inputs': ['rd_replacement_d2_101'], 'func': rd_replacement_d3_101}


def rd_replacement_d3_102(rd_replacement_d2_102):
    feature = _clean(rd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_102'] = {'inputs': ['rd_replacement_d2_102'], 'func': rd_replacement_d3_102}


def rd_replacement_d3_103(rd_replacement_d2_103):
    feature = _clean(rd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_103'] = {'inputs': ['rd_replacement_d2_103'], 'func': rd_replacement_d3_103}


def rd_replacement_d3_104(rd_replacement_d2_104):
    feature = _clean(rd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_104'] = {'inputs': ['rd_replacement_d2_104'], 'func': rd_replacement_d3_104}


def rd_replacement_d3_105(rd_replacement_d2_105):
    feature = _clean(rd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_105'] = {'inputs': ['rd_replacement_d2_105'], 'func': rd_replacement_d3_105}


def rd_replacement_d3_106(rd_replacement_d2_106):
    feature = _clean(rd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_106'] = {'inputs': ['rd_replacement_d2_106'], 'func': rd_replacement_d3_106}


def rd_replacement_d3_107(rd_replacement_d2_107):
    feature = _clean(rd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_107'] = {'inputs': ['rd_replacement_d2_107'], 'func': rd_replacement_d3_107}


def rd_replacement_d3_108(rd_replacement_d2_108):
    feature = _clean(rd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_108'] = {'inputs': ['rd_replacement_d2_108'], 'func': rd_replacement_d3_108}


def rd_replacement_d3_109(rd_replacement_d2_109):
    feature = _clean(rd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_109'] = {'inputs': ['rd_replacement_d2_109'], 'func': rd_replacement_d3_109}


def rd_replacement_d3_110(rd_replacement_d2_110):
    feature = _clean(rd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_110'] = {'inputs': ['rd_replacement_d2_110'], 'func': rd_replacement_d3_110}


def rd_replacement_d3_111(rd_replacement_d2_111):
    feature = _clean(rd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_111'] = {'inputs': ['rd_replacement_d2_111'], 'func': rd_replacement_d3_111}


def rd_replacement_d3_112(rd_replacement_d2_112):
    feature = _clean(rd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_112'] = {'inputs': ['rd_replacement_d2_112'], 'func': rd_replacement_d3_112}


def rd_replacement_d3_113(rd_replacement_d2_113):
    feature = _clean(rd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_113'] = {'inputs': ['rd_replacement_d2_113'], 'func': rd_replacement_d3_113}


def rd_replacement_d3_114(rd_replacement_d2_114):
    feature = _clean(rd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_114'] = {'inputs': ['rd_replacement_d2_114'], 'func': rd_replacement_d3_114}


def rd_replacement_d3_115(rd_replacement_d2_115):
    feature = _clean(rd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_115'] = {'inputs': ['rd_replacement_d2_115'], 'func': rd_replacement_d3_115}


def rd_replacement_d3_116(rd_replacement_d2_116):
    feature = _clean(rd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_116'] = {'inputs': ['rd_replacement_d2_116'], 'func': rd_replacement_d3_116}


def rd_replacement_d3_117(rd_replacement_d2_117):
    feature = _clean(rd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_117'] = {'inputs': ['rd_replacement_d2_117'], 'func': rd_replacement_d3_117}


def rd_replacement_d3_118(rd_replacement_d2_118):
    feature = _clean(rd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_118'] = {'inputs': ['rd_replacement_d2_118'], 'func': rd_replacement_d3_118}


def rd_replacement_d3_119(rd_replacement_d2_119):
    feature = _clean(rd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_119'] = {'inputs': ['rd_replacement_d2_119'], 'func': rd_replacement_d3_119}


def rd_replacement_d3_120(rd_replacement_d2_120):
    feature = _clean(rd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_120'] = {'inputs': ['rd_replacement_d2_120'], 'func': rd_replacement_d3_120}


def rd_replacement_d3_121(rd_replacement_d2_121):
    feature = _clean(rd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_121'] = {'inputs': ['rd_replacement_d2_121'], 'func': rd_replacement_d3_121}


def rd_replacement_d3_122(rd_replacement_d2_122):
    feature = _clean(rd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_122'] = {'inputs': ['rd_replacement_d2_122'], 'func': rd_replacement_d3_122}


def rd_replacement_d3_123(rd_replacement_d2_123):
    feature = _clean(rd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_123'] = {'inputs': ['rd_replacement_d2_123'], 'func': rd_replacement_d3_123}


def rd_replacement_d3_124(rd_replacement_d2_124):
    feature = _clean(rd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_124'] = {'inputs': ['rd_replacement_d2_124'], 'func': rd_replacement_d3_124}


def rd_replacement_d3_125(rd_replacement_d2_125):
    feature = _clean(rd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_125'] = {'inputs': ['rd_replacement_d2_125'], 'func': rd_replacement_d3_125}


def rd_replacement_d3_126(rd_replacement_d2_126):
    feature = _clean(rd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_126'] = {'inputs': ['rd_replacement_d2_126'], 'func': rd_replacement_d3_126}


def rd_replacement_d3_127(rd_replacement_d2_127):
    feature = _clean(rd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_127'] = {'inputs': ['rd_replacement_d2_127'], 'func': rd_replacement_d3_127}


def rd_replacement_d3_128(rd_replacement_d2_128):
    feature = _clean(rd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_128'] = {'inputs': ['rd_replacement_d2_128'], 'func': rd_replacement_d3_128}


def rd_replacement_d3_129(rd_replacement_d2_129):
    feature = _clean(rd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_129'] = {'inputs': ['rd_replacement_d2_129'], 'func': rd_replacement_d3_129}


def rd_replacement_d3_130(rd_replacement_d2_130):
    feature = _clean(rd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_130'] = {'inputs': ['rd_replacement_d2_130'], 'func': rd_replacement_d3_130}


def rd_replacement_d3_131(rd_replacement_d2_131):
    feature = _clean(rd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_131'] = {'inputs': ['rd_replacement_d2_131'], 'func': rd_replacement_d3_131}


def rd_replacement_d3_132(rd_replacement_d2_132):
    feature = _clean(rd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_132'] = {'inputs': ['rd_replacement_d2_132'], 'func': rd_replacement_d3_132}


def rd_replacement_d3_133(rd_replacement_d2_133):
    feature = _clean(rd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_133'] = {'inputs': ['rd_replacement_d2_133'], 'func': rd_replacement_d3_133}


def rd_replacement_d3_134(rd_replacement_d2_134):
    feature = _clean(rd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_134'] = {'inputs': ['rd_replacement_d2_134'], 'func': rd_replacement_d3_134}


def rd_replacement_d3_135(rd_replacement_d2_135):
    feature = _clean(rd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_135'] = {'inputs': ['rd_replacement_d2_135'], 'func': rd_replacement_d3_135}


def rd_replacement_d3_136(rd_replacement_d2_136):
    feature = _clean(rd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_136'] = {'inputs': ['rd_replacement_d2_136'], 'func': rd_replacement_d3_136}


def rd_replacement_d3_137(rd_replacement_d2_137):
    feature = _clean(rd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_137'] = {'inputs': ['rd_replacement_d2_137'], 'func': rd_replacement_d3_137}


def rd_replacement_d3_138(rd_replacement_d2_138):
    feature = _clean(rd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_138'] = {'inputs': ['rd_replacement_d2_138'], 'func': rd_replacement_d3_138}


def rd_replacement_d3_139(rd_replacement_d2_139):
    feature = _clean(rd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_139'] = {'inputs': ['rd_replacement_d2_139'], 'func': rd_replacement_d3_139}


def rd_replacement_d3_140(rd_replacement_d2_140):
    feature = _clean(rd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_140'] = {'inputs': ['rd_replacement_d2_140'], 'func': rd_replacement_d3_140}


def rd_replacement_d3_141(rd_replacement_d2_141):
    feature = _clean(rd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_141'] = {'inputs': ['rd_replacement_d2_141'], 'func': rd_replacement_d3_141}


def rd_replacement_d3_142(rd_replacement_d2_142):
    feature = _clean(rd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_142'] = {'inputs': ['rd_replacement_d2_142'], 'func': rd_replacement_d3_142}


def rd_replacement_d3_143(rd_replacement_d2_143):
    feature = _clean(rd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_143'] = {'inputs': ['rd_replacement_d2_143'], 'func': rd_replacement_d3_143}


def rd_replacement_d3_144(rd_replacement_d2_144):
    feature = _clean(rd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_144'] = {'inputs': ['rd_replacement_d2_144'], 'func': rd_replacement_d3_144}


def rd_replacement_d3_145(rd_replacement_d2_145):
    feature = _clean(rd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_145'] = {'inputs': ['rd_replacement_d2_145'], 'func': rd_replacement_d3_145}


def rd_replacement_d3_146(rd_replacement_d2_146):
    feature = _clean(rd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_146'] = {'inputs': ['rd_replacement_d2_146'], 'func': rd_replacement_d3_146}


def rd_replacement_d3_147(rd_replacement_d2_147):
    feature = _clean(rd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_147'] = {'inputs': ['rd_replacement_d2_147'], 'func': rd_replacement_d3_147}


def rd_replacement_d3_148(rd_replacement_d2_148):
    feature = _clean(rd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_148'] = {'inputs': ['rd_replacement_d2_148'], 'func': rd_replacement_d3_148}


def rd_replacement_d3_149(rd_replacement_d2_149):
    feature = _clean(rd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_149'] = {'inputs': ['rd_replacement_d2_149'], 'func': rd_replacement_d3_149}


def rd_replacement_d3_150(rd_replacement_d2_150):
    feature = _clean(rd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_150'] = {'inputs': ['rd_replacement_d2_150'], 'func': rd_replacement_d3_150}


def rd_replacement_d3_151(rd_replacement_d2_151):
    feature = _clean(rd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_151'] = {'inputs': ['rd_replacement_d2_151'], 'func': rd_replacement_d3_151}


def rd_replacement_d3_152(rd_replacement_d2_152):
    feature = _clean(rd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_152'] = {'inputs': ['rd_replacement_d2_152'], 'func': rd_replacement_d3_152}


def rd_replacement_d3_153(rd_replacement_d2_153):
    feature = _clean(rd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_153'] = {'inputs': ['rd_replacement_d2_153'], 'func': rd_replacement_d3_153}


def rd_replacement_d3_154(rd_replacement_d2_154):
    feature = _clean(rd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_154'] = {'inputs': ['rd_replacement_d2_154'], 'func': rd_replacement_d3_154}


def rd_replacement_d3_155(rd_replacement_d2_155):
    feature = _clean(rd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_155'] = {'inputs': ['rd_replacement_d2_155'], 'func': rd_replacement_d3_155}


def rd_replacement_d3_156(rd_replacement_d2_156):
    feature = _clean(rd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_156'] = {'inputs': ['rd_replacement_d2_156'], 'func': rd_replacement_d3_156}


def rd_replacement_d3_157(rd_replacement_d2_157):
    feature = _clean(rd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_157'] = {'inputs': ['rd_replacement_d2_157'], 'func': rd_replacement_d3_157}


def rd_replacement_d3_158(rd_replacement_d2_158):
    feature = _clean(rd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_158'] = {'inputs': ['rd_replacement_d2_158'], 'func': rd_replacement_d3_158}


def rd_replacement_d3_159(rd_replacement_d2_159):
    feature = _clean(rd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_159'] = {'inputs': ['rd_replacement_d2_159'], 'func': rd_replacement_d3_159}


def rd_replacement_d3_160(rd_replacement_d2_160):
    feature = _clean(rd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_160'] = {'inputs': ['rd_replacement_d2_160'], 'func': rd_replacement_d3_160}


def rd_replacement_d3_161(rd_replacement_d2_161):
    feature = _clean(rd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_161'] = {'inputs': ['rd_replacement_d2_161'], 'func': rd_replacement_d3_161}


def rd_replacement_d3_162(rd_replacement_d2_162):
    feature = _clean(rd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_162'] = {'inputs': ['rd_replacement_d2_162'], 'func': rd_replacement_d3_162}


def rd_replacement_d3_163(rd_replacement_d2_163):
    feature = _clean(rd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_163'] = {'inputs': ['rd_replacement_d2_163'], 'func': rd_replacement_d3_163}


def rd_replacement_d3_164(rd_replacement_d2_164):
    feature = _clean(rd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_164'] = {'inputs': ['rd_replacement_d2_164'], 'func': rd_replacement_d3_164}


def rd_replacement_d3_165(rd_replacement_d2_165):
    feature = _clean(rd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_165'] = {'inputs': ['rd_replacement_d2_165'], 'func': rd_replacement_d3_165}


def rd_replacement_d3_166(rd_replacement_d2_166):
    feature = _clean(rd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_166'] = {'inputs': ['rd_replacement_d2_166'], 'func': rd_replacement_d3_166}


def rd_replacement_d3_167(rd_replacement_d2_167):
    feature = _clean(rd_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_167'] = {'inputs': ['rd_replacement_d2_167'], 'func': rd_replacement_d3_167}


def rd_replacement_d3_168(rd_replacement_d2_168):
    feature = _clean(rd_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_168'] = {'inputs': ['rd_replacement_d2_168'], 'func': rd_replacement_d3_168}


def rd_replacement_d3_169(rd_replacement_d2_169):
    feature = _clean(rd_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_169'] = {'inputs': ['rd_replacement_d2_169'], 'func': rd_replacement_d3_169}


def rd_replacement_d3_170(rd_replacement_d2_170):
    feature = _clean(rd_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_170'] = {'inputs': ['rd_replacement_d2_170'], 'func': rd_replacement_d3_170}


def rd_replacement_d3_171(rd_replacement_d2_171):
    feature = _clean(rd_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_171'] = {'inputs': ['rd_replacement_d2_171'], 'func': rd_replacement_d3_171}


def rd_replacement_d3_172(rd_replacement_d2_172):
    feature = _clean(rd_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_172'] = {'inputs': ['rd_replacement_d2_172'], 'func': rd_replacement_d3_172}


def rd_replacement_d3_173(rd_replacement_d2_173):
    feature = _clean(rd_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_173'] = {'inputs': ['rd_replacement_d2_173'], 'func': rd_replacement_d3_173}


def rd_replacement_d3_174(rd_replacement_d2_174):
    feature = _clean(rd_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_174'] = {'inputs': ['rd_replacement_d2_174'], 'func': rd_replacement_d3_174}


def rd_replacement_d3_175(rd_replacement_d2_175):
    feature = _clean(rd_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
RD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rd_replacement_d3_175'] = {'inputs': ['rd_replacement_d2_175'], 'func': rd_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rds_base_universe_d3_001_rds_003_loss_streak_21_003(rds_base_universe_d2_001_rds_003_loss_streak_21_003):
    return _base_universe_d3(rds_base_universe_d2_001_rds_003_loss_streak_21_003, 1)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_001_rds_003_loss_streak_21_003'] = {'inputs': ['rds_base_universe_d2_001_rds_003_loss_streak_21_003'], 'func': rds_base_universe_d3_001_rds_003_loss_streak_21_003}


def rds_base_universe_d3_002_rds_004_ma_distance_42_004(rds_base_universe_d2_002_rds_004_ma_distance_42_004):
    return _base_universe_d3(rds_base_universe_d2_002_rds_004_ma_distance_42_004, 2)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_002_rds_004_ma_distance_42_004'] = {'inputs': ['rds_base_universe_d2_002_rds_004_ma_distance_42_004'], 'func': rds_base_universe_d3_002_rds_004_ma_distance_42_004}


def rds_base_universe_d3_003_rds_005_stochastic_position_63_005(rds_base_universe_d2_003_rds_005_stochastic_position_63_005):
    return _base_universe_d3(rds_base_universe_d2_003_rds_005_stochastic_position_63_005, 3)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_003_rds_005_stochastic_position_63_005'] = {'inputs': ['rds_base_universe_d2_003_rds_005_stochastic_position_63_005'], 'func': rds_base_universe_d3_003_rds_005_stochastic_position_63_005}


def rds_base_universe_d3_004_rds_009_loss_streak_252_009(rds_base_universe_d2_004_rds_009_loss_streak_252_009):
    return _base_universe_d3(rds_base_universe_d2_004_rds_009_loss_streak_252_009, 4)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_004_rds_009_loss_streak_252_009'] = {'inputs': ['rds_base_universe_d2_004_rds_009_loss_streak_252_009'], 'func': rds_base_universe_d3_004_rds_009_loss_streak_252_009}


def rds_base_universe_d3_005_rds_010_ma_distance_378_010(rds_base_universe_d2_005_rds_010_ma_distance_378_010):
    return _base_universe_d3(rds_base_universe_d2_005_rds_010_ma_distance_378_010, 5)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_005_rds_010_ma_distance_378_010'] = {'inputs': ['rds_base_universe_d2_005_rds_010_ma_distance_378_010'], 'func': rds_base_universe_d3_005_rds_010_ma_distance_378_010}


def rds_base_universe_d3_006_rds_011_stochastic_position_504_011(rds_base_universe_d2_006_rds_011_stochastic_position_504_011):
    return _base_universe_d3(rds_base_universe_d2_006_rds_011_stochastic_position_504_011, 6)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_006_rds_011_stochastic_position_504_011'] = {'inputs': ['rds_base_universe_d2_006_rds_011_stochastic_position_504_011'], 'func': rds_base_universe_d3_006_rds_011_stochastic_position_504_011}


def rds_base_universe_d3_007_rds_015_loss_streak_1512_015(rds_base_universe_d2_007_rds_015_loss_streak_1512_015):
    return _base_universe_d3(rds_base_universe_d2_007_rds_015_loss_streak_1512_015, 7)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_007_rds_015_loss_streak_1512_015'] = {'inputs': ['rds_base_universe_d2_007_rds_015_loss_streak_1512_015'], 'func': rds_base_universe_d3_007_rds_015_loss_streak_1512_015}


def rds_base_universe_d3_008_rds_016_ma_distance_5_016(rds_base_universe_d2_008_rds_016_ma_distance_5_016):
    return _base_universe_d3(rds_base_universe_d2_008_rds_016_ma_distance_5_016, 8)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_008_rds_016_ma_distance_5_016'] = {'inputs': ['rds_base_universe_d2_008_rds_016_ma_distance_5_016'], 'func': rds_base_universe_d3_008_rds_016_ma_distance_5_016}


def rds_base_universe_d3_009_rds_017_stochastic_position_10_017(rds_base_universe_d2_009_rds_017_stochastic_position_10_017):
    return _base_universe_d3(rds_base_universe_d2_009_rds_017_stochastic_position_10_017, 9)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_009_rds_017_stochastic_position_10_017'] = {'inputs': ['rds_base_universe_d2_009_rds_017_stochastic_position_10_017'], 'func': rds_base_universe_d3_009_rds_017_stochastic_position_10_017}


def rds_base_universe_d3_010_rds_021_loss_streak_84_021(rds_base_universe_d2_010_rds_021_loss_streak_84_021):
    return _base_universe_d3(rds_base_universe_d2_010_rds_021_loss_streak_84_021, 10)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_010_rds_021_loss_streak_84_021'] = {'inputs': ['rds_base_universe_d2_010_rds_021_loss_streak_84_021'], 'func': rds_base_universe_d3_010_rds_021_loss_streak_84_021}


def rds_base_universe_d3_011_rds_022_ma_distance_126_022(rds_base_universe_d2_011_rds_022_ma_distance_126_022):
    return _base_universe_d3(rds_base_universe_d2_011_rds_022_ma_distance_126_022, 11)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_011_rds_022_ma_distance_126_022'] = {'inputs': ['rds_base_universe_d2_011_rds_022_ma_distance_126_022'], 'func': rds_base_universe_d3_011_rds_022_ma_distance_126_022}


def rds_base_universe_d3_012_rds_023_stochastic_position_189_023(rds_base_universe_d2_012_rds_023_stochastic_position_189_023):
    return _base_universe_d3(rds_base_universe_d2_012_rds_023_stochastic_position_189_023, 12)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_012_rds_023_stochastic_position_189_023'] = {'inputs': ['rds_base_universe_d2_012_rds_023_stochastic_position_189_023'], 'func': rds_base_universe_d3_012_rds_023_stochastic_position_189_023}


def rds_base_universe_d3_013_rds_027_loss_streak_756_027(rds_base_universe_d2_013_rds_027_loss_streak_756_027):
    return _base_universe_d3(rds_base_universe_d2_013_rds_027_loss_streak_756_027, 13)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_013_rds_027_loss_streak_756_027'] = {'inputs': ['rds_base_universe_d2_013_rds_027_loss_streak_756_027'], 'func': rds_base_universe_d3_013_rds_027_loss_streak_756_027}


def rds_base_universe_d3_014_rds_028_ma_distance_1008_028(rds_base_universe_d2_014_rds_028_ma_distance_1008_028):
    return _base_universe_d3(rds_base_universe_d2_014_rds_028_ma_distance_1008_028, 14)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_014_rds_028_ma_distance_1008_028'] = {'inputs': ['rds_base_universe_d2_014_rds_028_ma_distance_1008_028'], 'func': rds_base_universe_d3_014_rds_028_ma_distance_1008_028}


def rds_base_universe_d3_015_rds_029_stochastic_position_1260_029(rds_base_universe_d2_015_rds_029_stochastic_position_1260_029):
    return _base_universe_d3(rds_base_universe_d2_015_rds_029_stochastic_position_1260_029, 15)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_015_rds_029_stochastic_position_1260_029'] = {'inputs': ['rds_base_universe_d2_015_rds_029_stochastic_position_1260_029'], 'func': rds_base_universe_d3_015_rds_029_stochastic_position_1260_029}


def rds_base_universe_d3_016_rds_basefill_001(rds_base_universe_d2_016_rds_basefill_001):
    return _base_universe_d3(rds_base_universe_d2_016_rds_basefill_001, 16)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_016_rds_basefill_001'] = {'inputs': ['rds_base_universe_d2_016_rds_basefill_001'], 'func': rds_base_universe_d3_016_rds_basefill_001}


def rds_base_universe_d3_017_rds_basefill_002(rds_base_universe_d2_017_rds_basefill_002):
    return _base_universe_d3(rds_base_universe_d2_017_rds_basefill_002, 17)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_017_rds_basefill_002'] = {'inputs': ['rds_base_universe_d2_017_rds_basefill_002'], 'func': rds_base_universe_d3_017_rds_basefill_002}


def rds_base_universe_d3_018_rds_basefill_006(rds_base_universe_d2_018_rds_basefill_006):
    return _base_universe_d3(rds_base_universe_d2_018_rds_basefill_006, 18)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_018_rds_basefill_006'] = {'inputs': ['rds_base_universe_d2_018_rds_basefill_006'], 'func': rds_base_universe_d3_018_rds_basefill_006}


def rds_base_universe_d3_019_rds_basefill_007(rds_base_universe_d2_019_rds_basefill_007):
    return _base_universe_d3(rds_base_universe_d2_019_rds_basefill_007, 19)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_019_rds_basefill_007'] = {'inputs': ['rds_base_universe_d2_019_rds_basefill_007'], 'func': rds_base_universe_d3_019_rds_basefill_007}


def rds_base_universe_d3_020_rds_basefill_008(rds_base_universe_d2_020_rds_basefill_008):
    return _base_universe_d3(rds_base_universe_d2_020_rds_basefill_008, 20)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_020_rds_basefill_008'] = {'inputs': ['rds_base_universe_d2_020_rds_basefill_008'], 'func': rds_base_universe_d3_020_rds_basefill_008}


def rds_base_universe_d3_021_rds_basefill_012(rds_base_universe_d2_021_rds_basefill_012):
    return _base_universe_d3(rds_base_universe_d2_021_rds_basefill_012, 21)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_021_rds_basefill_012'] = {'inputs': ['rds_base_universe_d2_021_rds_basefill_012'], 'func': rds_base_universe_d3_021_rds_basefill_012}


def rds_base_universe_d3_022_rds_basefill_013(rds_base_universe_d2_022_rds_basefill_013):
    return _base_universe_d3(rds_base_universe_d2_022_rds_basefill_013, 22)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_022_rds_basefill_013'] = {'inputs': ['rds_base_universe_d2_022_rds_basefill_013'], 'func': rds_base_universe_d3_022_rds_basefill_013}


def rds_base_universe_d3_023_rds_basefill_014(rds_base_universe_d2_023_rds_basefill_014):
    return _base_universe_d3(rds_base_universe_d2_023_rds_basefill_014, 23)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_023_rds_basefill_014'] = {'inputs': ['rds_base_universe_d2_023_rds_basefill_014'], 'func': rds_base_universe_d3_023_rds_basefill_014}


def rds_base_universe_d3_024_rds_basefill_018(rds_base_universe_d2_024_rds_basefill_018):
    return _base_universe_d3(rds_base_universe_d2_024_rds_basefill_018, 24)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_024_rds_basefill_018'] = {'inputs': ['rds_base_universe_d2_024_rds_basefill_018'], 'func': rds_base_universe_d3_024_rds_basefill_018}


def rds_base_universe_d3_025_rds_basefill_019(rds_base_universe_d2_025_rds_basefill_019):
    return _base_universe_d3(rds_base_universe_d2_025_rds_basefill_019, 25)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_025_rds_basefill_019'] = {'inputs': ['rds_base_universe_d2_025_rds_basefill_019'], 'func': rds_base_universe_d3_025_rds_basefill_019}


def rds_base_universe_d3_026_rds_basefill_020(rds_base_universe_d2_026_rds_basefill_020):
    return _base_universe_d3(rds_base_universe_d2_026_rds_basefill_020, 26)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_026_rds_basefill_020'] = {'inputs': ['rds_base_universe_d2_026_rds_basefill_020'], 'func': rds_base_universe_d3_026_rds_basefill_020}


def rds_base_universe_d3_027_rds_basefill_024(rds_base_universe_d2_027_rds_basefill_024):
    return _base_universe_d3(rds_base_universe_d2_027_rds_basefill_024, 27)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_027_rds_basefill_024'] = {'inputs': ['rds_base_universe_d2_027_rds_basefill_024'], 'func': rds_base_universe_d3_027_rds_basefill_024}


def rds_base_universe_d3_028_rds_basefill_025(rds_base_universe_d2_028_rds_basefill_025):
    return _base_universe_d3(rds_base_universe_d2_028_rds_basefill_025, 28)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_028_rds_basefill_025'] = {'inputs': ['rds_base_universe_d2_028_rds_basefill_025'], 'func': rds_base_universe_d3_028_rds_basefill_025}


def rds_base_universe_d3_029_rds_basefill_026(rds_base_universe_d2_029_rds_basefill_026):
    return _base_universe_d3(rds_base_universe_d2_029_rds_basefill_026, 29)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_029_rds_basefill_026'] = {'inputs': ['rds_base_universe_d2_029_rds_basefill_026'], 'func': rds_base_universe_d3_029_rds_basefill_026}


def rds_base_universe_d3_030_rds_basefill_030(rds_base_universe_d2_030_rds_basefill_030):
    return _base_universe_d3(rds_base_universe_d2_030_rds_basefill_030, 30)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_030_rds_basefill_030'] = {'inputs': ['rds_base_universe_d2_030_rds_basefill_030'], 'func': rds_base_universe_d3_030_rds_basefill_030}


def rds_base_universe_d3_031_rds_basefill_031(rds_base_universe_d2_031_rds_basefill_031):
    return _base_universe_d3(rds_base_universe_d2_031_rds_basefill_031, 31)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_031_rds_basefill_031'] = {'inputs': ['rds_base_universe_d2_031_rds_basefill_031'], 'func': rds_base_universe_d3_031_rds_basefill_031}


def rds_base_universe_d3_032_rds_basefill_032(rds_base_universe_d2_032_rds_basefill_032):
    return _base_universe_d3(rds_base_universe_d2_032_rds_basefill_032, 32)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_032_rds_basefill_032'] = {'inputs': ['rds_base_universe_d2_032_rds_basefill_032'], 'func': rds_base_universe_d3_032_rds_basefill_032}


def rds_base_universe_d3_033_rds_basefill_033(rds_base_universe_d2_033_rds_basefill_033):
    return _base_universe_d3(rds_base_universe_d2_033_rds_basefill_033, 33)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_033_rds_basefill_033'] = {'inputs': ['rds_base_universe_d2_033_rds_basefill_033'], 'func': rds_base_universe_d3_033_rds_basefill_033}


def rds_base_universe_d3_034_rds_basefill_034(rds_base_universe_d2_034_rds_basefill_034):
    return _base_universe_d3(rds_base_universe_d2_034_rds_basefill_034, 34)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_034_rds_basefill_034'] = {'inputs': ['rds_base_universe_d2_034_rds_basefill_034'], 'func': rds_base_universe_d3_034_rds_basefill_034}


def rds_base_universe_d3_035_rds_basefill_035(rds_base_universe_d2_035_rds_basefill_035):
    return _base_universe_d3(rds_base_universe_d2_035_rds_basefill_035, 35)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_035_rds_basefill_035'] = {'inputs': ['rds_base_universe_d2_035_rds_basefill_035'], 'func': rds_base_universe_d3_035_rds_basefill_035}


def rds_base_universe_d3_036_rds_basefill_036(rds_base_universe_d2_036_rds_basefill_036):
    return _base_universe_d3(rds_base_universe_d2_036_rds_basefill_036, 36)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_036_rds_basefill_036'] = {'inputs': ['rds_base_universe_d2_036_rds_basefill_036'], 'func': rds_base_universe_d3_036_rds_basefill_036}


def rds_base_universe_d3_037_rds_basefill_037(rds_base_universe_d2_037_rds_basefill_037):
    return _base_universe_d3(rds_base_universe_d2_037_rds_basefill_037, 37)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_037_rds_basefill_037'] = {'inputs': ['rds_base_universe_d2_037_rds_basefill_037'], 'func': rds_base_universe_d3_037_rds_basefill_037}


def rds_base_universe_d3_038_rds_basefill_038(rds_base_universe_d2_038_rds_basefill_038):
    return _base_universe_d3(rds_base_universe_d2_038_rds_basefill_038, 38)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_038_rds_basefill_038'] = {'inputs': ['rds_base_universe_d2_038_rds_basefill_038'], 'func': rds_base_universe_d3_038_rds_basefill_038}


def rds_base_universe_d3_039_rds_basefill_039(rds_base_universe_d2_039_rds_basefill_039):
    return _base_universe_d3(rds_base_universe_d2_039_rds_basefill_039, 39)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_039_rds_basefill_039'] = {'inputs': ['rds_base_universe_d2_039_rds_basefill_039'], 'func': rds_base_universe_d3_039_rds_basefill_039}


def rds_base_universe_d3_040_rds_basefill_040(rds_base_universe_d2_040_rds_basefill_040):
    return _base_universe_d3(rds_base_universe_d2_040_rds_basefill_040, 40)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_040_rds_basefill_040'] = {'inputs': ['rds_base_universe_d2_040_rds_basefill_040'], 'func': rds_base_universe_d3_040_rds_basefill_040}


def rds_base_universe_d3_041_rds_basefill_041(rds_base_universe_d2_041_rds_basefill_041):
    return _base_universe_d3(rds_base_universe_d2_041_rds_basefill_041, 41)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_041_rds_basefill_041'] = {'inputs': ['rds_base_universe_d2_041_rds_basefill_041'], 'func': rds_base_universe_d3_041_rds_basefill_041}


def rds_base_universe_d3_042_rds_basefill_042(rds_base_universe_d2_042_rds_basefill_042):
    return _base_universe_d3(rds_base_universe_d2_042_rds_basefill_042, 42)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_042_rds_basefill_042'] = {'inputs': ['rds_base_universe_d2_042_rds_basefill_042'], 'func': rds_base_universe_d3_042_rds_basefill_042}


def rds_base_universe_d3_043_rds_basefill_043(rds_base_universe_d2_043_rds_basefill_043):
    return _base_universe_d3(rds_base_universe_d2_043_rds_basefill_043, 43)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_043_rds_basefill_043'] = {'inputs': ['rds_base_universe_d2_043_rds_basefill_043'], 'func': rds_base_universe_d3_043_rds_basefill_043}


def rds_base_universe_d3_044_rds_basefill_044(rds_base_universe_d2_044_rds_basefill_044):
    return _base_universe_d3(rds_base_universe_d2_044_rds_basefill_044, 44)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_044_rds_basefill_044'] = {'inputs': ['rds_base_universe_d2_044_rds_basefill_044'], 'func': rds_base_universe_d3_044_rds_basefill_044}


def rds_base_universe_d3_045_rds_basefill_045(rds_base_universe_d2_045_rds_basefill_045):
    return _base_universe_d3(rds_base_universe_d2_045_rds_basefill_045, 45)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_045_rds_basefill_045'] = {'inputs': ['rds_base_universe_d2_045_rds_basefill_045'], 'func': rds_base_universe_d3_045_rds_basefill_045}


def rds_base_universe_d3_046_rds_basefill_046(rds_base_universe_d2_046_rds_basefill_046):
    return _base_universe_d3(rds_base_universe_d2_046_rds_basefill_046, 46)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_046_rds_basefill_046'] = {'inputs': ['rds_base_universe_d2_046_rds_basefill_046'], 'func': rds_base_universe_d3_046_rds_basefill_046}


def rds_base_universe_d3_047_rds_basefill_047(rds_base_universe_d2_047_rds_basefill_047):
    return _base_universe_d3(rds_base_universe_d2_047_rds_basefill_047, 47)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_047_rds_basefill_047'] = {'inputs': ['rds_base_universe_d2_047_rds_basefill_047'], 'func': rds_base_universe_d3_047_rds_basefill_047}


def rds_base_universe_d3_048_rds_basefill_048(rds_base_universe_d2_048_rds_basefill_048):
    return _base_universe_d3(rds_base_universe_d2_048_rds_basefill_048, 48)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_048_rds_basefill_048'] = {'inputs': ['rds_base_universe_d2_048_rds_basefill_048'], 'func': rds_base_universe_d3_048_rds_basefill_048}


def rds_base_universe_d3_049_rds_basefill_049(rds_base_universe_d2_049_rds_basefill_049):
    return _base_universe_d3(rds_base_universe_d2_049_rds_basefill_049, 49)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_049_rds_basefill_049'] = {'inputs': ['rds_base_universe_d2_049_rds_basefill_049'], 'func': rds_base_universe_d3_049_rds_basefill_049}


def rds_base_universe_d3_050_rds_basefill_050(rds_base_universe_d2_050_rds_basefill_050):
    return _base_universe_d3(rds_base_universe_d2_050_rds_basefill_050, 50)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_050_rds_basefill_050'] = {'inputs': ['rds_base_universe_d2_050_rds_basefill_050'], 'func': rds_base_universe_d3_050_rds_basefill_050}


def rds_base_universe_d3_051_rds_basefill_051(rds_base_universe_d2_051_rds_basefill_051):
    return _base_universe_d3(rds_base_universe_d2_051_rds_basefill_051, 51)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_051_rds_basefill_051'] = {'inputs': ['rds_base_universe_d2_051_rds_basefill_051'], 'func': rds_base_universe_d3_051_rds_basefill_051}


def rds_base_universe_d3_052_rds_basefill_052(rds_base_universe_d2_052_rds_basefill_052):
    return _base_universe_d3(rds_base_universe_d2_052_rds_basefill_052, 52)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_052_rds_basefill_052'] = {'inputs': ['rds_base_universe_d2_052_rds_basefill_052'], 'func': rds_base_universe_d3_052_rds_basefill_052}


def rds_base_universe_d3_053_rds_basefill_053(rds_base_universe_d2_053_rds_basefill_053):
    return _base_universe_d3(rds_base_universe_d2_053_rds_basefill_053, 53)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_053_rds_basefill_053'] = {'inputs': ['rds_base_universe_d2_053_rds_basefill_053'], 'func': rds_base_universe_d3_053_rds_basefill_053}


def rds_base_universe_d3_054_rds_basefill_054(rds_base_universe_d2_054_rds_basefill_054):
    return _base_universe_d3(rds_base_universe_d2_054_rds_basefill_054, 54)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_054_rds_basefill_054'] = {'inputs': ['rds_base_universe_d2_054_rds_basefill_054'], 'func': rds_base_universe_d3_054_rds_basefill_054}


def rds_base_universe_d3_055_rds_basefill_055(rds_base_universe_d2_055_rds_basefill_055):
    return _base_universe_d3(rds_base_universe_d2_055_rds_basefill_055, 55)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_055_rds_basefill_055'] = {'inputs': ['rds_base_universe_d2_055_rds_basefill_055'], 'func': rds_base_universe_d3_055_rds_basefill_055}


def rds_base_universe_d3_056_rds_basefill_056(rds_base_universe_d2_056_rds_basefill_056):
    return _base_universe_d3(rds_base_universe_d2_056_rds_basefill_056, 56)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_056_rds_basefill_056'] = {'inputs': ['rds_base_universe_d2_056_rds_basefill_056'], 'func': rds_base_universe_d3_056_rds_basefill_056}


def rds_base_universe_d3_057_rds_basefill_057(rds_base_universe_d2_057_rds_basefill_057):
    return _base_universe_d3(rds_base_universe_d2_057_rds_basefill_057, 57)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_057_rds_basefill_057'] = {'inputs': ['rds_base_universe_d2_057_rds_basefill_057'], 'func': rds_base_universe_d3_057_rds_basefill_057}


def rds_base_universe_d3_058_rds_basefill_058(rds_base_universe_d2_058_rds_basefill_058):
    return _base_universe_d3(rds_base_universe_d2_058_rds_basefill_058, 58)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_058_rds_basefill_058'] = {'inputs': ['rds_base_universe_d2_058_rds_basefill_058'], 'func': rds_base_universe_d3_058_rds_basefill_058}


def rds_base_universe_d3_059_rds_basefill_059(rds_base_universe_d2_059_rds_basefill_059):
    return _base_universe_d3(rds_base_universe_d2_059_rds_basefill_059, 59)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_059_rds_basefill_059'] = {'inputs': ['rds_base_universe_d2_059_rds_basefill_059'], 'func': rds_base_universe_d3_059_rds_basefill_059}


def rds_base_universe_d3_060_rds_basefill_060(rds_base_universe_d2_060_rds_basefill_060):
    return _base_universe_d3(rds_base_universe_d2_060_rds_basefill_060, 60)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_060_rds_basefill_060'] = {'inputs': ['rds_base_universe_d2_060_rds_basefill_060'], 'func': rds_base_universe_d3_060_rds_basefill_060}


def rds_base_universe_d3_061_rds_basefill_061(rds_base_universe_d2_061_rds_basefill_061):
    return _base_universe_d3(rds_base_universe_d2_061_rds_basefill_061, 61)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_061_rds_basefill_061'] = {'inputs': ['rds_base_universe_d2_061_rds_basefill_061'], 'func': rds_base_universe_d3_061_rds_basefill_061}


def rds_base_universe_d3_062_rds_basefill_062(rds_base_universe_d2_062_rds_basefill_062):
    return _base_universe_d3(rds_base_universe_d2_062_rds_basefill_062, 62)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_062_rds_basefill_062'] = {'inputs': ['rds_base_universe_d2_062_rds_basefill_062'], 'func': rds_base_universe_d3_062_rds_basefill_062}


def rds_base_universe_d3_063_rds_basefill_063(rds_base_universe_d2_063_rds_basefill_063):
    return _base_universe_d3(rds_base_universe_d2_063_rds_basefill_063, 63)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_063_rds_basefill_063'] = {'inputs': ['rds_base_universe_d2_063_rds_basefill_063'], 'func': rds_base_universe_d3_063_rds_basefill_063}


def rds_base_universe_d3_064_rds_basefill_064(rds_base_universe_d2_064_rds_basefill_064):
    return _base_universe_d3(rds_base_universe_d2_064_rds_basefill_064, 64)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_064_rds_basefill_064'] = {'inputs': ['rds_base_universe_d2_064_rds_basefill_064'], 'func': rds_base_universe_d3_064_rds_basefill_064}


def rds_base_universe_d3_065_rds_basefill_065(rds_base_universe_d2_065_rds_basefill_065):
    return _base_universe_d3(rds_base_universe_d2_065_rds_basefill_065, 65)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_065_rds_basefill_065'] = {'inputs': ['rds_base_universe_d2_065_rds_basefill_065'], 'func': rds_base_universe_d3_065_rds_basefill_065}


def rds_base_universe_d3_066_rds_basefill_066(rds_base_universe_d2_066_rds_basefill_066):
    return _base_universe_d3(rds_base_universe_d2_066_rds_basefill_066, 66)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_066_rds_basefill_066'] = {'inputs': ['rds_base_universe_d2_066_rds_basefill_066'], 'func': rds_base_universe_d3_066_rds_basefill_066}


def rds_base_universe_d3_067_rds_basefill_067(rds_base_universe_d2_067_rds_basefill_067):
    return _base_universe_d3(rds_base_universe_d2_067_rds_basefill_067, 67)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_067_rds_basefill_067'] = {'inputs': ['rds_base_universe_d2_067_rds_basefill_067'], 'func': rds_base_universe_d3_067_rds_basefill_067}


def rds_base_universe_d3_068_rds_basefill_068(rds_base_universe_d2_068_rds_basefill_068):
    return _base_universe_d3(rds_base_universe_d2_068_rds_basefill_068, 68)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_068_rds_basefill_068'] = {'inputs': ['rds_base_universe_d2_068_rds_basefill_068'], 'func': rds_base_universe_d3_068_rds_basefill_068}


def rds_base_universe_d3_069_rds_basefill_069(rds_base_universe_d2_069_rds_basefill_069):
    return _base_universe_d3(rds_base_universe_d2_069_rds_basefill_069, 69)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_069_rds_basefill_069'] = {'inputs': ['rds_base_universe_d2_069_rds_basefill_069'], 'func': rds_base_universe_d3_069_rds_basefill_069}


def rds_base_universe_d3_070_rds_basefill_070(rds_base_universe_d2_070_rds_basefill_070):
    return _base_universe_d3(rds_base_universe_d2_070_rds_basefill_070, 70)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_070_rds_basefill_070'] = {'inputs': ['rds_base_universe_d2_070_rds_basefill_070'], 'func': rds_base_universe_d3_070_rds_basefill_070}


def rds_base_universe_d3_071_rds_basefill_071(rds_base_universe_d2_071_rds_basefill_071):
    return _base_universe_d3(rds_base_universe_d2_071_rds_basefill_071, 71)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_071_rds_basefill_071'] = {'inputs': ['rds_base_universe_d2_071_rds_basefill_071'], 'func': rds_base_universe_d3_071_rds_basefill_071}


def rds_base_universe_d3_072_rds_basefill_072(rds_base_universe_d2_072_rds_basefill_072):
    return _base_universe_d3(rds_base_universe_d2_072_rds_basefill_072, 72)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_072_rds_basefill_072'] = {'inputs': ['rds_base_universe_d2_072_rds_basefill_072'], 'func': rds_base_universe_d3_072_rds_basefill_072}


def rds_base_universe_d3_073_rds_basefill_073(rds_base_universe_d2_073_rds_basefill_073):
    return _base_universe_d3(rds_base_universe_d2_073_rds_basefill_073, 73)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_073_rds_basefill_073'] = {'inputs': ['rds_base_universe_d2_073_rds_basefill_073'], 'func': rds_base_universe_d3_073_rds_basefill_073}


def rds_base_universe_d3_074_rds_basefill_074(rds_base_universe_d2_074_rds_basefill_074):
    return _base_universe_d3(rds_base_universe_d2_074_rds_basefill_074, 74)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_074_rds_basefill_074'] = {'inputs': ['rds_base_universe_d2_074_rds_basefill_074'], 'func': rds_base_universe_d3_074_rds_basefill_074}


def rds_base_universe_d3_075_rds_basefill_075(rds_base_universe_d2_075_rds_basefill_075):
    return _base_universe_d3(rds_base_universe_d2_075_rds_basefill_075, 75)
RDS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rds_base_universe_d3_075_rds_basefill_075'] = {'inputs': ['rds_base_universe_d2_075_rds_basefill_075'], 'func': rds_base_universe_d3_075_rds_basefill_075}
