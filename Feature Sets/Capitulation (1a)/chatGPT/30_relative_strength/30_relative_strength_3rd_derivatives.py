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



def rst_001_return_decay_accel_1(rst_001_return_decay_roc_1):
    feature = _s(rst_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rst_007_return_decay_accel_5(rst_007_return_decay_roc_5):
    feature = _s(rst_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def rst_013_return_decay_accel_42(rst_013_return_decay_roc_42):
    feature = _s(rst_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rst_179_rst_019_return_decay_42_019_accel_126(rst_154_rst_019_return_decay_42_019_roc_126):
    feature = _s(rst_154_rst_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rst_180_rst_025_return_decay_5_025_accel_378(rst_155_rst_025_return_decay_5_025_roc_378):
    feature = _s(rst_155_rst_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















RELATIVE_STRENGTH_REGISTRY_3RD_DERIVATIVES = {
    'rst_001_return_decay_accel_1': {'inputs': ['rst_001_return_decay_roc_1'], 'func': rst_001_return_decay_accel_1},
    'rst_007_return_decay_accel_5': {'inputs': ['rst_007_return_decay_roc_5'], 'func': rst_007_return_decay_accel_5},
    'rst_013_return_decay_accel_42': {'inputs': ['rst_013_return_decay_roc_42'], 'func': rst_013_return_decay_accel_42},
    'rst_179_rst_019_return_decay_42_019_accel_126': {'inputs': ['rst_154_rst_019_return_decay_42_019_roc_126'], 'func': rst_179_rst_019_return_decay_42_019_accel_126},
    'rst_180_rst_025_return_decay_5_025_accel_378': {'inputs': ['rst_155_rst_025_return_decay_5_025_roc_378'], 'func': rst_180_rst_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def rs_replacement_d3_001(rs_replacement_d2_001):
    feature = _clean(rs_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_001'] = {'inputs': ['rs_replacement_d2_001'], 'func': rs_replacement_d3_001}


def rs_replacement_d3_002(rs_replacement_d2_002):
    feature = _clean(rs_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_002'] = {'inputs': ['rs_replacement_d2_002'], 'func': rs_replacement_d3_002}


def rs_replacement_d3_003(rs_replacement_d2_003):
    feature = _clean(rs_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_003'] = {'inputs': ['rs_replacement_d2_003'], 'func': rs_replacement_d3_003}


def rs_replacement_d3_004(rs_replacement_d2_004):
    feature = _clean(rs_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_004'] = {'inputs': ['rs_replacement_d2_004'], 'func': rs_replacement_d3_004}


def rs_replacement_d3_005(rs_replacement_d2_005):
    feature = _clean(rs_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_005'] = {'inputs': ['rs_replacement_d2_005'], 'func': rs_replacement_d3_005}


def rs_replacement_d3_006(rs_replacement_d2_006):
    feature = _clean(rs_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_006'] = {'inputs': ['rs_replacement_d2_006'], 'func': rs_replacement_d3_006}


def rs_replacement_d3_007(rs_replacement_d2_007):
    feature = _clean(rs_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_007'] = {'inputs': ['rs_replacement_d2_007'], 'func': rs_replacement_d3_007}


def rs_replacement_d3_008(rs_replacement_d2_008):
    feature = _clean(rs_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_008'] = {'inputs': ['rs_replacement_d2_008'], 'func': rs_replacement_d3_008}


def rs_replacement_d3_009(rs_replacement_d2_009):
    feature = _clean(rs_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_009'] = {'inputs': ['rs_replacement_d2_009'], 'func': rs_replacement_d3_009}


def rs_replacement_d3_010(rs_replacement_d2_010):
    feature = _clean(rs_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_010'] = {'inputs': ['rs_replacement_d2_010'], 'func': rs_replacement_d3_010}


def rs_replacement_d3_011(rs_replacement_d2_011):
    feature = _clean(rs_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_011'] = {'inputs': ['rs_replacement_d2_011'], 'func': rs_replacement_d3_011}


def rs_replacement_d3_012(rs_replacement_d2_012):
    feature = _clean(rs_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_012'] = {'inputs': ['rs_replacement_d2_012'], 'func': rs_replacement_d3_012}


def rs_replacement_d3_013(rs_replacement_d2_013):
    feature = _clean(rs_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_013'] = {'inputs': ['rs_replacement_d2_013'], 'func': rs_replacement_d3_013}


def rs_replacement_d3_014(rs_replacement_d2_014):
    feature = _clean(rs_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_014'] = {'inputs': ['rs_replacement_d2_014'], 'func': rs_replacement_d3_014}


def rs_replacement_d3_015(rs_replacement_d2_015):
    feature = _clean(rs_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_015'] = {'inputs': ['rs_replacement_d2_015'], 'func': rs_replacement_d3_015}


def rs_replacement_d3_016(rs_replacement_d2_016):
    feature = _clean(rs_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_016'] = {'inputs': ['rs_replacement_d2_016'], 'func': rs_replacement_d3_016}


def rs_replacement_d3_017(rs_replacement_d2_017):
    feature = _clean(rs_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_017'] = {'inputs': ['rs_replacement_d2_017'], 'func': rs_replacement_d3_017}


def rs_replacement_d3_018(rs_replacement_d2_018):
    feature = _clean(rs_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_018'] = {'inputs': ['rs_replacement_d2_018'], 'func': rs_replacement_d3_018}


def rs_replacement_d3_019(rs_replacement_d2_019):
    feature = _clean(rs_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_019'] = {'inputs': ['rs_replacement_d2_019'], 'func': rs_replacement_d3_019}


def rs_replacement_d3_020(rs_replacement_d2_020):
    feature = _clean(rs_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_020'] = {'inputs': ['rs_replacement_d2_020'], 'func': rs_replacement_d3_020}


def rs_replacement_d3_021(rs_replacement_d2_021):
    feature = _clean(rs_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_021'] = {'inputs': ['rs_replacement_d2_021'], 'func': rs_replacement_d3_021}


def rs_replacement_d3_022(rs_replacement_d2_022):
    feature = _clean(rs_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_022'] = {'inputs': ['rs_replacement_d2_022'], 'func': rs_replacement_d3_022}


def rs_replacement_d3_023(rs_replacement_d2_023):
    feature = _clean(rs_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_023'] = {'inputs': ['rs_replacement_d2_023'], 'func': rs_replacement_d3_023}


def rs_replacement_d3_024(rs_replacement_d2_024):
    feature = _clean(rs_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_024'] = {'inputs': ['rs_replacement_d2_024'], 'func': rs_replacement_d3_024}


def rs_replacement_d3_025(rs_replacement_d2_025):
    feature = _clean(rs_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_025'] = {'inputs': ['rs_replacement_d2_025'], 'func': rs_replacement_d3_025}


def rs_replacement_d3_026(rs_replacement_d2_026):
    feature = _clean(rs_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_026'] = {'inputs': ['rs_replacement_d2_026'], 'func': rs_replacement_d3_026}


def rs_replacement_d3_027(rs_replacement_d2_027):
    feature = _clean(rs_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_027'] = {'inputs': ['rs_replacement_d2_027'], 'func': rs_replacement_d3_027}


def rs_replacement_d3_028(rs_replacement_d2_028):
    feature = _clean(rs_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_028'] = {'inputs': ['rs_replacement_d2_028'], 'func': rs_replacement_d3_028}


def rs_replacement_d3_029(rs_replacement_d2_029):
    feature = _clean(rs_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_029'] = {'inputs': ['rs_replacement_d2_029'], 'func': rs_replacement_d3_029}


def rs_replacement_d3_030(rs_replacement_d2_030):
    feature = _clean(rs_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_030'] = {'inputs': ['rs_replacement_d2_030'], 'func': rs_replacement_d3_030}


def rs_replacement_d3_031(rs_replacement_d2_031):
    feature = _clean(rs_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_031'] = {'inputs': ['rs_replacement_d2_031'], 'func': rs_replacement_d3_031}


def rs_replacement_d3_032(rs_replacement_d2_032):
    feature = _clean(rs_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_032'] = {'inputs': ['rs_replacement_d2_032'], 'func': rs_replacement_d3_032}


def rs_replacement_d3_033(rs_replacement_d2_033):
    feature = _clean(rs_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_033'] = {'inputs': ['rs_replacement_d2_033'], 'func': rs_replacement_d3_033}


def rs_replacement_d3_034(rs_replacement_d2_034):
    feature = _clean(rs_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_034'] = {'inputs': ['rs_replacement_d2_034'], 'func': rs_replacement_d3_034}


def rs_replacement_d3_035(rs_replacement_d2_035):
    feature = _clean(rs_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_035'] = {'inputs': ['rs_replacement_d2_035'], 'func': rs_replacement_d3_035}


def rs_replacement_d3_036(rs_replacement_d2_036):
    feature = _clean(rs_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_036'] = {'inputs': ['rs_replacement_d2_036'], 'func': rs_replacement_d3_036}


def rs_replacement_d3_037(rs_replacement_d2_037):
    feature = _clean(rs_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_037'] = {'inputs': ['rs_replacement_d2_037'], 'func': rs_replacement_d3_037}


def rs_replacement_d3_038(rs_replacement_d2_038):
    feature = _clean(rs_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_038'] = {'inputs': ['rs_replacement_d2_038'], 'func': rs_replacement_d3_038}


def rs_replacement_d3_039(rs_replacement_d2_039):
    feature = _clean(rs_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_039'] = {'inputs': ['rs_replacement_d2_039'], 'func': rs_replacement_d3_039}


def rs_replacement_d3_040(rs_replacement_d2_040):
    feature = _clean(rs_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_040'] = {'inputs': ['rs_replacement_d2_040'], 'func': rs_replacement_d3_040}


def rs_replacement_d3_041(rs_replacement_d2_041):
    feature = _clean(rs_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_041'] = {'inputs': ['rs_replacement_d2_041'], 'func': rs_replacement_d3_041}


def rs_replacement_d3_042(rs_replacement_d2_042):
    feature = _clean(rs_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_042'] = {'inputs': ['rs_replacement_d2_042'], 'func': rs_replacement_d3_042}


def rs_replacement_d3_043(rs_replacement_d2_043):
    feature = _clean(rs_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_043'] = {'inputs': ['rs_replacement_d2_043'], 'func': rs_replacement_d3_043}


def rs_replacement_d3_044(rs_replacement_d2_044):
    feature = _clean(rs_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_044'] = {'inputs': ['rs_replacement_d2_044'], 'func': rs_replacement_d3_044}


def rs_replacement_d3_045(rs_replacement_d2_045):
    feature = _clean(rs_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_045'] = {'inputs': ['rs_replacement_d2_045'], 'func': rs_replacement_d3_045}


def rs_replacement_d3_046(rs_replacement_d2_046):
    feature = _clean(rs_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_046'] = {'inputs': ['rs_replacement_d2_046'], 'func': rs_replacement_d3_046}


def rs_replacement_d3_047(rs_replacement_d2_047):
    feature = _clean(rs_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_047'] = {'inputs': ['rs_replacement_d2_047'], 'func': rs_replacement_d3_047}


def rs_replacement_d3_048(rs_replacement_d2_048):
    feature = _clean(rs_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_048'] = {'inputs': ['rs_replacement_d2_048'], 'func': rs_replacement_d3_048}


def rs_replacement_d3_049(rs_replacement_d2_049):
    feature = _clean(rs_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_049'] = {'inputs': ['rs_replacement_d2_049'], 'func': rs_replacement_d3_049}


def rs_replacement_d3_050(rs_replacement_d2_050):
    feature = _clean(rs_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_050'] = {'inputs': ['rs_replacement_d2_050'], 'func': rs_replacement_d3_050}


def rs_replacement_d3_051(rs_replacement_d2_051):
    feature = _clean(rs_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_051'] = {'inputs': ['rs_replacement_d2_051'], 'func': rs_replacement_d3_051}


def rs_replacement_d3_052(rs_replacement_d2_052):
    feature = _clean(rs_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_052'] = {'inputs': ['rs_replacement_d2_052'], 'func': rs_replacement_d3_052}


def rs_replacement_d3_053(rs_replacement_d2_053):
    feature = _clean(rs_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_053'] = {'inputs': ['rs_replacement_d2_053'], 'func': rs_replacement_d3_053}


def rs_replacement_d3_054(rs_replacement_d2_054):
    feature = _clean(rs_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_054'] = {'inputs': ['rs_replacement_d2_054'], 'func': rs_replacement_d3_054}


def rs_replacement_d3_055(rs_replacement_d2_055):
    feature = _clean(rs_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_055'] = {'inputs': ['rs_replacement_d2_055'], 'func': rs_replacement_d3_055}


def rs_replacement_d3_056(rs_replacement_d2_056):
    feature = _clean(rs_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_056'] = {'inputs': ['rs_replacement_d2_056'], 'func': rs_replacement_d3_056}


def rs_replacement_d3_057(rs_replacement_d2_057):
    feature = _clean(rs_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_057'] = {'inputs': ['rs_replacement_d2_057'], 'func': rs_replacement_d3_057}


def rs_replacement_d3_058(rs_replacement_d2_058):
    feature = _clean(rs_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_058'] = {'inputs': ['rs_replacement_d2_058'], 'func': rs_replacement_d3_058}


def rs_replacement_d3_059(rs_replacement_d2_059):
    feature = _clean(rs_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_059'] = {'inputs': ['rs_replacement_d2_059'], 'func': rs_replacement_d3_059}


def rs_replacement_d3_060(rs_replacement_d2_060):
    feature = _clean(rs_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_060'] = {'inputs': ['rs_replacement_d2_060'], 'func': rs_replacement_d3_060}


def rs_replacement_d3_061(rs_replacement_d2_061):
    feature = _clean(rs_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_061'] = {'inputs': ['rs_replacement_d2_061'], 'func': rs_replacement_d3_061}


def rs_replacement_d3_062(rs_replacement_d2_062):
    feature = _clean(rs_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_062'] = {'inputs': ['rs_replacement_d2_062'], 'func': rs_replacement_d3_062}


def rs_replacement_d3_063(rs_replacement_d2_063):
    feature = _clean(rs_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_063'] = {'inputs': ['rs_replacement_d2_063'], 'func': rs_replacement_d3_063}


def rs_replacement_d3_064(rs_replacement_d2_064):
    feature = _clean(rs_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_064'] = {'inputs': ['rs_replacement_d2_064'], 'func': rs_replacement_d3_064}


def rs_replacement_d3_065(rs_replacement_d2_065):
    feature = _clean(rs_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_065'] = {'inputs': ['rs_replacement_d2_065'], 'func': rs_replacement_d3_065}


def rs_replacement_d3_066(rs_replacement_d2_066):
    feature = _clean(rs_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_066'] = {'inputs': ['rs_replacement_d2_066'], 'func': rs_replacement_d3_066}


def rs_replacement_d3_067(rs_replacement_d2_067):
    feature = _clean(rs_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_067'] = {'inputs': ['rs_replacement_d2_067'], 'func': rs_replacement_d3_067}


def rs_replacement_d3_068(rs_replacement_d2_068):
    feature = _clean(rs_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_068'] = {'inputs': ['rs_replacement_d2_068'], 'func': rs_replacement_d3_068}


def rs_replacement_d3_069(rs_replacement_d2_069):
    feature = _clean(rs_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_069'] = {'inputs': ['rs_replacement_d2_069'], 'func': rs_replacement_d3_069}


def rs_replacement_d3_070(rs_replacement_d2_070):
    feature = _clean(rs_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_070'] = {'inputs': ['rs_replacement_d2_070'], 'func': rs_replacement_d3_070}


def rs_replacement_d3_071(rs_replacement_d2_071):
    feature = _clean(rs_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_071'] = {'inputs': ['rs_replacement_d2_071'], 'func': rs_replacement_d3_071}


def rs_replacement_d3_072(rs_replacement_d2_072):
    feature = _clean(rs_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_072'] = {'inputs': ['rs_replacement_d2_072'], 'func': rs_replacement_d3_072}


def rs_replacement_d3_073(rs_replacement_d2_073):
    feature = _clean(rs_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_073'] = {'inputs': ['rs_replacement_d2_073'], 'func': rs_replacement_d3_073}


def rs_replacement_d3_074(rs_replacement_d2_074):
    feature = _clean(rs_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_074'] = {'inputs': ['rs_replacement_d2_074'], 'func': rs_replacement_d3_074}


def rs_replacement_d3_075(rs_replacement_d2_075):
    feature = _clean(rs_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_075'] = {'inputs': ['rs_replacement_d2_075'], 'func': rs_replacement_d3_075}


def rs_replacement_d3_076(rs_replacement_d2_076):
    feature = _clean(rs_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_076'] = {'inputs': ['rs_replacement_d2_076'], 'func': rs_replacement_d3_076}


def rs_replacement_d3_077(rs_replacement_d2_077):
    feature = _clean(rs_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_077'] = {'inputs': ['rs_replacement_d2_077'], 'func': rs_replacement_d3_077}


def rs_replacement_d3_078(rs_replacement_d2_078):
    feature = _clean(rs_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_078'] = {'inputs': ['rs_replacement_d2_078'], 'func': rs_replacement_d3_078}


def rs_replacement_d3_079(rs_replacement_d2_079):
    feature = _clean(rs_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_079'] = {'inputs': ['rs_replacement_d2_079'], 'func': rs_replacement_d3_079}


def rs_replacement_d3_080(rs_replacement_d2_080):
    feature = _clean(rs_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_080'] = {'inputs': ['rs_replacement_d2_080'], 'func': rs_replacement_d3_080}


def rs_replacement_d3_081(rs_replacement_d2_081):
    feature = _clean(rs_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_081'] = {'inputs': ['rs_replacement_d2_081'], 'func': rs_replacement_d3_081}


def rs_replacement_d3_082(rs_replacement_d2_082):
    feature = _clean(rs_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_082'] = {'inputs': ['rs_replacement_d2_082'], 'func': rs_replacement_d3_082}


def rs_replacement_d3_083(rs_replacement_d2_083):
    feature = _clean(rs_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_083'] = {'inputs': ['rs_replacement_d2_083'], 'func': rs_replacement_d3_083}


def rs_replacement_d3_084(rs_replacement_d2_084):
    feature = _clean(rs_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_084'] = {'inputs': ['rs_replacement_d2_084'], 'func': rs_replacement_d3_084}


def rs_replacement_d3_085(rs_replacement_d2_085):
    feature = _clean(rs_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_085'] = {'inputs': ['rs_replacement_d2_085'], 'func': rs_replacement_d3_085}


def rs_replacement_d3_086(rs_replacement_d2_086):
    feature = _clean(rs_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_086'] = {'inputs': ['rs_replacement_d2_086'], 'func': rs_replacement_d3_086}


def rs_replacement_d3_087(rs_replacement_d2_087):
    feature = _clean(rs_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_087'] = {'inputs': ['rs_replacement_d2_087'], 'func': rs_replacement_d3_087}


def rs_replacement_d3_088(rs_replacement_d2_088):
    feature = _clean(rs_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_088'] = {'inputs': ['rs_replacement_d2_088'], 'func': rs_replacement_d3_088}


def rs_replacement_d3_089(rs_replacement_d2_089):
    feature = _clean(rs_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_089'] = {'inputs': ['rs_replacement_d2_089'], 'func': rs_replacement_d3_089}


def rs_replacement_d3_090(rs_replacement_d2_090):
    feature = _clean(rs_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_090'] = {'inputs': ['rs_replacement_d2_090'], 'func': rs_replacement_d3_090}


def rs_replacement_d3_091(rs_replacement_d2_091):
    feature = _clean(rs_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_091'] = {'inputs': ['rs_replacement_d2_091'], 'func': rs_replacement_d3_091}


def rs_replacement_d3_092(rs_replacement_d2_092):
    feature = _clean(rs_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_092'] = {'inputs': ['rs_replacement_d2_092'], 'func': rs_replacement_d3_092}


def rs_replacement_d3_093(rs_replacement_d2_093):
    feature = _clean(rs_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_093'] = {'inputs': ['rs_replacement_d2_093'], 'func': rs_replacement_d3_093}


def rs_replacement_d3_094(rs_replacement_d2_094):
    feature = _clean(rs_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_094'] = {'inputs': ['rs_replacement_d2_094'], 'func': rs_replacement_d3_094}


def rs_replacement_d3_095(rs_replacement_d2_095):
    feature = _clean(rs_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_095'] = {'inputs': ['rs_replacement_d2_095'], 'func': rs_replacement_d3_095}


def rs_replacement_d3_096(rs_replacement_d2_096):
    feature = _clean(rs_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_096'] = {'inputs': ['rs_replacement_d2_096'], 'func': rs_replacement_d3_096}


def rs_replacement_d3_097(rs_replacement_d2_097):
    feature = _clean(rs_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_097'] = {'inputs': ['rs_replacement_d2_097'], 'func': rs_replacement_d3_097}


def rs_replacement_d3_098(rs_replacement_d2_098):
    feature = _clean(rs_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_098'] = {'inputs': ['rs_replacement_d2_098'], 'func': rs_replacement_d3_098}


def rs_replacement_d3_099(rs_replacement_d2_099):
    feature = _clean(rs_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_099'] = {'inputs': ['rs_replacement_d2_099'], 'func': rs_replacement_d3_099}


def rs_replacement_d3_100(rs_replacement_d2_100):
    feature = _clean(rs_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_100'] = {'inputs': ['rs_replacement_d2_100'], 'func': rs_replacement_d3_100}


def rs_replacement_d3_101(rs_replacement_d2_101):
    feature = _clean(rs_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_101'] = {'inputs': ['rs_replacement_d2_101'], 'func': rs_replacement_d3_101}


def rs_replacement_d3_102(rs_replacement_d2_102):
    feature = _clean(rs_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_102'] = {'inputs': ['rs_replacement_d2_102'], 'func': rs_replacement_d3_102}


def rs_replacement_d3_103(rs_replacement_d2_103):
    feature = _clean(rs_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_103'] = {'inputs': ['rs_replacement_d2_103'], 'func': rs_replacement_d3_103}


def rs_replacement_d3_104(rs_replacement_d2_104):
    feature = _clean(rs_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_104'] = {'inputs': ['rs_replacement_d2_104'], 'func': rs_replacement_d3_104}


def rs_replacement_d3_105(rs_replacement_d2_105):
    feature = _clean(rs_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_105'] = {'inputs': ['rs_replacement_d2_105'], 'func': rs_replacement_d3_105}


def rs_replacement_d3_106(rs_replacement_d2_106):
    feature = _clean(rs_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_106'] = {'inputs': ['rs_replacement_d2_106'], 'func': rs_replacement_d3_106}


def rs_replacement_d3_107(rs_replacement_d2_107):
    feature = _clean(rs_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_107'] = {'inputs': ['rs_replacement_d2_107'], 'func': rs_replacement_d3_107}


def rs_replacement_d3_108(rs_replacement_d2_108):
    feature = _clean(rs_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_108'] = {'inputs': ['rs_replacement_d2_108'], 'func': rs_replacement_d3_108}


def rs_replacement_d3_109(rs_replacement_d2_109):
    feature = _clean(rs_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_109'] = {'inputs': ['rs_replacement_d2_109'], 'func': rs_replacement_d3_109}


def rs_replacement_d3_110(rs_replacement_d2_110):
    feature = _clean(rs_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_110'] = {'inputs': ['rs_replacement_d2_110'], 'func': rs_replacement_d3_110}


def rs_replacement_d3_111(rs_replacement_d2_111):
    feature = _clean(rs_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_111'] = {'inputs': ['rs_replacement_d2_111'], 'func': rs_replacement_d3_111}


def rs_replacement_d3_112(rs_replacement_d2_112):
    feature = _clean(rs_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_112'] = {'inputs': ['rs_replacement_d2_112'], 'func': rs_replacement_d3_112}


def rs_replacement_d3_113(rs_replacement_d2_113):
    feature = _clean(rs_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_113'] = {'inputs': ['rs_replacement_d2_113'], 'func': rs_replacement_d3_113}


def rs_replacement_d3_114(rs_replacement_d2_114):
    feature = _clean(rs_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_114'] = {'inputs': ['rs_replacement_d2_114'], 'func': rs_replacement_d3_114}


def rs_replacement_d3_115(rs_replacement_d2_115):
    feature = _clean(rs_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_115'] = {'inputs': ['rs_replacement_d2_115'], 'func': rs_replacement_d3_115}


def rs_replacement_d3_116(rs_replacement_d2_116):
    feature = _clean(rs_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_116'] = {'inputs': ['rs_replacement_d2_116'], 'func': rs_replacement_d3_116}


def rs_replacement_d3_117(rs_replacement_d2_117):
    feature = _clean(rs_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_117'] = {'inputs': ['rs_replacement_d2_117'], 'func': rs_replacement_d3_117}


def rs_replacement_d3_118(rs_replacement_d2_118):
    feature = _clean(rs_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_118'] = {'inputs': ['rs_replacement_d2_118'], 'func': rs_replacement_d3_118}


def rs_replacement_d3_119(rs_replacement_d2_119):
    feature = _clean(rs_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_119'] = {'inputs': ['rs_replacement_d2_119'], 'func': rs_replacement_d3_119}


def rs_replacement_d3_120(rs_replacement_d2_120):
    feature = _clean(rs_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_120'] = {'inputs': ['rs_replacement_d2_120'], 'func': rs_replacement_d3_120}


def rs_replacement_d3_121(rs_replacement_d2_121):
    feature = _clean(rs_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_121'] = {'inputs': ['rs_replacement_d2_121'], 'func': rs_replacement_d3_121}


def rs_replacement_d3_122(rs_replacement_d2_122):
    feature = _clean(rs_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_122'] = {'inputs': ['rs_replacement_d2_122'], 'func': rs_replacement_d3_122}


def rs_replacement_d3_123(rs_replacement_d2_123):
    feature = _clean(rs_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_123'] = {'inputs': ['rs_replacement_d2_123'], 'func': rs_replacement_d3_123}


def rs_replacement_d3_124(rs_replacement_d2_124):
    feature = _clean(rs_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_124'] = {'inputs': ['rs_replacement_d2_124'], 'func': rs_replacement_d3_124}


def rs_replacement_d3_125(rs_replacement_d2_125):
    feature = _clean(rs_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_125'] = {'inputs': ['rs_replacement_d2_125'], 'func': rs_replacement_d3_125}


def rs_replacement_d3_126(rs_replacement_d2_126):
    feature = _clean(rs_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_126'] = {'inputs': ['rs_replacement_d2_126'], 'func': rs_replacement_d3_126}


def rs_replacement_d3_127(rs_replacement_d2_127):
    feature = _clean(rs_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_127'] = {'inputs': ['rs_replacement_d2_127'], 'func': rs_replacement_d3_127}


def rs_replacement_d3_128(rs_replacement_d2_128):
    feature = _clean(rs_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_128'] = {'inputs': ['rs_replacement_d2_128'], 'func': rs_replacement_d3_128}


def rs_replacement_d3_129(rs_replacement_d2_129):
    feature = _clean(rs_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_129'] = {'inputs': ['rs_replacement_d2_129'], 'func': rs_replacement_d3_129}


def rs_replacement_d3_130(rs_replacement_d2_130):
    feature = _clean(rs_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_130'] = {'inputs': ['rs_replacement_d2_130'], 'func': rs_replacement_d3_130}


def rs_replacement_d3_131(rs_replacement_d2_131):
    feature = _clean(rs_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_131'] = {'inputs': ['rs_replacement_d2_131'], 'func': rs_replacement_d3_131}


def rs_replacement_d3_132(rs_replacement_d2_132):
    feature = _clean(rs_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_132'] = {'inputs': ['rs_replacement_d2_132'], 'func': rs_replacement_d3_132}


def rs_replacement_d3_133(rs_replacement_d2_133):
    feature = _clean(rs_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_133'] = {'inputs': ['rs_replacement_d2_133'], 'func': rs_replacement_d3_133}


def rs_replacement_d3_134(rs_replacement_d2_134):
    feature = _clean(rs_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_134'] = {'inputs': ['rs_replacement_d2_134'], 'func': rs_replacement_d3_134}


def rs_replacement_d3_135(rs_replacement_d2_135):
    feature = _clean(rs_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_135'] = {'inputs': ['rs_replacement_d2_135'], 'func': rs_replacement_d3_135}


def rs_replacement_d3_136(rs_replacement_d2_136):
    feature = _clean(rs_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_136'] = {'inputs': ['rs_replacement_d2_136'], 'func': rs_replacement_d3_136}


def rs_replacement_d3_137(rs_replacement_d2_137):
    feature = _clean(rs_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_137'] = {'inputs': ['rs_replacement_d2_137'], 'func': rs_replacement_d3_137}


def rs_replacement_d3_138(rs_replacement_d2_138):
    feature = _clean(rs_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_138'] = {'inputs': ['rs_replacement_d2_138'], 'func': rs_replacement_d3_138}


def rs_replacement_d3_139(rs_replacement_d2_139):
    feature = _clean(rs_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_139'] = {'inputs': ['rs_replacement_d2_139'], 'func': rs_replacement_d3_139}


def rs_replacement_d3_140(rs_replacement_d2_140):
    feature = _clean(rs_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_140'] = {'inputs': ['rs_replacement_d2_140'], 'func': rs_replacement_d3_140}


def rs_replacement_d3_141(rs_replacement_d2_141):
    feature = _clean(rs_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_141'] = {'inputs': ['rs_replacement_d2_141'], 'func': rs_replacement_d3_141}


def rs_replacement_d3_142(rs_replacement_d2_142):
    feature = _clean(rs_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_142'] = {'inputs': ['rs_replacement_d2_142'], 'func': rs_replacement_d3_142}


def rs_replacement_d3_143(rs_replacement_d2_143):
    feature = _clean(rs_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_143'] = {'inputs': ['rs_replacement_d2_143'], 'func': rs_replacement_d3_143}


def rs_replacement_d3_144(rs_replacement_d2_144):
    feature = _clean(rs_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_144'] = {'inputs': ['rs_replacement_d2_144'], 'func': rs_replacement_d3_144}


def rs_replacement_d3_145(rs_replacement_d2_145):
    feature = _clean(rs_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_145'] = {'inputs': ['rs_replacement_d2_145'], 'func': rs_replacement_d3_145}


def rs_replacement_d3_146(rs_replacement_d2_146):
    feature = _clean(rs_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_146'] = {'inputs': ['rs_replacement_d2_146'], 'func': rs_replacement_d3_146}


def rs_replacement_d3_147(rs_replacement_d2_147):
    feature = _clean(rs_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_147'] = {'inputs': ['rs_replacement_d2_147'], 'func': rs_replacement_d3_147}


def rs_replacement_d3_148(rs_replacement_d2_148):
    feature = _clean(rs_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_148'] = {'inputs': ['rs_replacement_d2_148'], 'func': rs_replacement_d3_148}


def rs_replacement_d3_149(rs_replacement_d2_149):
    feature = _clean(rs_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_149'] = {'inputs': ['rs_replacement_d2_149'], 'func': rs_replacement_d3_149}


def rs_replacement_d3_150(rs_replacement_d2_150):
    feature = _clean(rs_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_150'] = {'inputs': ['rs_replacement_d2_150'], 'func': rs_replacement_d3_150}


def rs_replacement_d3_151(rs_replacement_d2_151):
    feature = _clean(rs_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_151'] = {'inputs': ['rs_replacement_d2_151'], 'func': rs_replacement_d3_151}


def rs_replacement_d3_152(rs_replacement_d2_152):
    feature = _clean(rs_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_152'] = {'inputs': ['rs_replacement_d2_152'], 'func': rs_replacement_d3_152}


def rs_replacement_d3_153(rs_replacement_d2_153):
    feature = _clean(rs_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_153'] = {'inputs': ['rs_replacement_d2_153'], 'func': rs_replacement_d3_153}


def rs_replacement_d3_154(rs_replacement_d2_154):
    feature = _clean(rs_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_154'] = {'inputs': ['rs_replacement_d2_154'], 'func': rs_replacement_d3_154}


def rs_replacement_d3_155(rs_replacement_d2_155):
    feature = _clean(rs_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_155'] = {'inputs': ['rs_replacement_d2_155'], 'func': rs_replacement_d3_155}


def rs_replacement_d3_156(rs_replacement_d2_156):
    feature = _clean(rs_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_156'] = {'inputs': ['rs_replacement_d2_156'], 'func': rs_replacement_d3_156}


def rs_replacement_d3_157(rs_replacement_d2_157):
    feature = _clean(rs_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_157'] = {'inputs': ['rs_replacement_d2_157'], 'func': rs_replacement_d3_157}


def rs_replacement_d3_158(rs_replacement_d2_158):
    feature = _clean(rs_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_158'] = {'inputs': ['rs_replacement_d2_158'], 'func': rs_replacement_d3_158}


def rs_replacement_d3_159(rs_replacement_d2_159):
    feature = _clean(rs_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_159'] = {'inputs': ['rs_replacement_d2_159'], 'func': rs_replacement_d3_159}


def rs_replacement_d3_160(rs_replacement_d2_160):
    feature = _clean(rs_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_160'] = {'inputs': ['rs_replacement_d2_160'], 'func': rs_replacement_d3_160}


def rs_replacement_d3_161(rs_replacement_d2_161):
    feature = _clean(rs_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_161'] = {'inputs': ['rs_replacement_d2_161'], 'func': rs_replacement_d3_161}


def rs_replacement_d3_162(rs_replacement_d2_162):
    feature = _clean(rs_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_162'] = {'inputs': ['rs_replacement_d2_162'], 'func': rs_replacement_d3_162}


def rs_replacement_d3_163(rs_replacement_d2_163):
    feature = _clean(rs_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_163'] = {'inputs': ['rs_replacement_d2_163'], 'func': rs_replacement_d3_163}


def rs_replacement_d3_164(rs_replacement_d2_164):
    feature = _clean(rs_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_164'] = {'inputs': ['rs_replacement_d2_164'], 'func': rs_replacement_d3_164}


def rs_replacement_d3_165(rs_replacement_d2_165):
    feature = _clean(rs_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_165'] = {'inputs': ['rs_replacement_d2_165'], 'func': rs_replacement_d3_165}


def rs_replacement_d3_166(rs_replacement_d2_166):
    feature = _clean(rs_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_166'] = {'inputs': ['rs_replacement_d2_166'], 'func': rs_replacement_d3_166}


def rs_replacement_d3_167(rs_replacement_d2_167):
    feature = _clean(rs_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_167'] = {'inputs': ['rs_replacement_d2_167'], 'func': rs_replacement_d3_167}


def rs_replacement_d3_168(rs_replacement_d2_168):
    feature = _clean(rs_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_168'] = {'inputs': ['rs_replacement_d2_168'], 'func': rs_replacement_d3_168}


def rs_replacement_d3_169(rs_replacement_d2_169):
    feature = _clean(rs_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_169'] = {'inputs': ['rs_replacement_d2_169'], 'func': rs_replacement_d3_169}


def rs_replacement_d3_170(rs_replacement_d2_170):
    feature = _clean(rs_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_170'] = {'inputs': ['rs_replacement_d2_170'], 'func': rs_replacement_d3_170}


def rs_replacement_d3_171(rs_replacement_d2_171):
    feature = _clean(rs_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_171'] = {'inputs': ['rs_replacement_d2_171'], 'func': rs_replacement_d3_171}


def rs_replacement_d3_172(rs_replacement_d2_172):
    feature = _clean(rs_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_172'] = {'inputs': ['rs_replacement_d2_172'], 'func': rs_replacement_d3_172}


def rs_replacement_d3_173(rs_replacement_d2_173):
    feature = _clean(rs_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_173'] = {'inputs': ['rs_replacement_d2_173'], 'func': rs_replacement_d3_173}


def rs_replacement_d3_174(rs_replacement_d2_174):
    feature = _clean(rs_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_174'] = {'inputs': ['rs_replacement_d2_174'], 'func': rs_replacement_d3_174}


def rs_replacement_d3_175(rs_replacement_d2_175):
    feature = _clean(rs_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
RS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rs_replacement_d3_175'] = {'inputs': ['rs_replacement_d2_175'], 'func': rs_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rst_base_universe_d3_001_rst_003_loss_streak_21_003(rst_base_universe_d2_001_rst_003_loss_streak_21_003):
    return _base_universe_d3(rst_base_universe_d2_001_rst_003_loss_streak_21_003, 1)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_001_rst_003_loss_streak_21_003'] = {'inputs': ['rst_base_universe_d2_001_rst_003_loss_streak_21_003'], 'func': rst_base_universe_d3_001_rst_003_loss_streak_21_003}


def rst_base_universe_d3_002_rst_004_ma_distance_42_004(rst_base_universe_d2_002_rst_004_ma_distance_42_004):
    return _base_universe_d3(rst_base_universe_d2_002_rst_004_ma_distance_42_004, 2)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_002_rst_004_ma_distance_42_004'] = {'inputs': ['rst_base_universe_d2_002_rst_004_ma_distance_42_004'], 'func': rst_base_universe_d3_002_rst_004_ma_distance_42_004}


def rst_base_universe_d3_003_rst_005_stochastic_position_63_005(rst_base_universe_d2_003_rst_005_stochastic_position_63_005):
    return _base_universe_d3(rst_base_universe_d2_003_rst_005_stochastic_position_63_005, 3)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_003_rst_005_stochastic_position_63_005'] = {'inputs': ['rst_base_universe_d2_003_rst_005_stochastic_position_63_005'], 'func': rst_base_universe_d3_003_rst_005_stochastic_position_63_005}


def rst_base_universe_d3_004_rst_009_loss_streak_252_009(rst_base_universe_d2_004_rst_009_loss_streak_252_009):
    return _base_universe_d3(rst_base_universe_d2_004_rst_009_loss_streak_252_009, 4)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_004_rst_009_loss_streak_252_009'] = {'inputs': ['rst_base_universe_d2_004_rst_009_loss_streak_252_009'], 'func': rst_base_universe_d3_004_rst_009_loss_streak_252_009}


def rst_base_universe_d3_005_rst_010_ma_distance_378_010(rst_base_universe_d2_005_rst_010_ma_distance_378_010):
    return _base_universe_d3(rst_base_universe_d2_005_rst_010_ma_distance_378_010, 5)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_005_rst_010_ma_distance_378_010'] = {'inputs': ['rst_base_universe_d2_005_rst_010_ma_distance_378_010'], 'func': rst_base_universe_d3_005_rst_010_ma_distance_378_010}


def rst_base_universe_d3_006_rst_011_stochastic_position_504_011(rst_base_universe_d2_006_rst_011_stochastic_position_504_011):
    return _base_universe_d3(rst_base_universe_d2_006_rst_011_stochastic_position_504_011, 6)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_006_rst_011_stochastic_position_504_011'] = {'inputs': ['rst_base_universe_d2_006_rst_011_stochastic_position_504_011'], 'func': rst_base_universe_d3_006_rst_011_stochastic_position_504_011}


def rst_base_universe_d3_007_rst_015_loss_streak_1512_015(rst_base_universe_d2_007_rst_015_loss_streak_1512_015):
    return _base_universe_d3(rst_base_universe_d2_007_rst_015_loss_streak_1512_015, 7)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_007_rst_015_loss_streak_1512_015'] = {'inputs': ['rst_base_universe_d2_007_rst_015_loss_streak_1512_015'], 'func': rst_base_universe_d3_007_rst_015_loss_streak_1512_015}


def rst_base_universe_d3_008_rst_016_ma_distance_5_016(rst_base_universe_d2_008_rst_016_ma_distance_5_016):
    return _base_universe_d3(rst_base_universe_d2_008_rst_016_ma_distance_5_016, 8)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_008_rst_016_ma_distance_5_016'] = {'inputs': ['rst_base_universe_d2_008_rst_016_ma_distance_5_016'], 'func': rst_base_universe_d3_008_rst_016_ma_distance_5_016}


def rst_base_universe_d3_009_rst_017_stochastic_position_10_017(rst_base_universe_d2_009_rst_017_stochastic_position_10_017):
    return _base_universe_d3(rst_base_universe_d2_009_rst_017_stochastic_position_10_017, 9)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_009_rst_017_stochastic_position_10_017'] = {'inputs': ['rst_base_universe_d2_009_rst_017_stochastic_position_10_017'], 'func': rst_base_universe_d3_009_rst_017_stochastic_position_10_017}


def rst_base_universe_d3_010_rst_021_loss_streak_84_021(rst_base_universe_d2_010_rst_021_loss_streak_84_021):
    return _base_universe_d3(rst_base_universe_d2_010_rst_021_loss_streak_84_021, 10)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_010_rst_021_loss_streak_84_021'] = {'inputs': ['rst_base_universe_d2_010_rst_021_loss_streak_84_021'], 'func': rst_base_universe_d3_010_rst_021_loss_streak_84_021}


def rst_base_universe_d3_011_rst_022_ma_distance_126_022(rst_base_universe_d2_011_rst_022_ma_distance_126_022):
    return _base_universe_d3(rst_base_universe_d2_011_rst_022_ma_distance_126_022, 11)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_011_rst_022_ma_distance_126_022'] = {'inputs': ['rst_base_universe_d2_011_rst_022_ma_distance_126_022'], 'func': rst_base_universe_d3_011_rst_022_ma_distance_126_022}


def rst_base_universe_d3_012_rst_023_stochastic_position_189_023(rst_base_universe_d2_012_rst_023_stochastic_position_189_023):
    return _base_universe_d3(rst_base_universe_d2_012_rst_023_stochastic_position_189_023, 12)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_012_rst_023_stochastic_position_189_023'] = {'inputs': ['rst_base_universe_d2_012_rst_023_stochastic_position_189_023'], 'func': rst_base_universe_d3_012_rst_023_stochastic_position_189_023}


def rst_base_universe_d3_013_rst_027_loss_streak_756_027(rst_base_universe_d2_013_rst_027_loss_streak_756_027):
    return _base_universe_d3(rst_base_universe_d2_013_rst_027_loss_streak_756_027, 13)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_013_rst_027_loss_streak_756_027'] = {'inputs': ['rst_base_universe_d2_013_rst_027_loss_streak_756_027'], 'func': rst_base_universe_d3_013_rst_027_loss_streak_756_027}


def rst_base_universe_d3_014_rst_028_ma_distance_1008_028(rst_base_universe_d2_014_rst_028_ma_distance_1008_028):
    return _base_universe_d3(rst_base_universe_d2_014_rst_028_ma_distance_1008_028, 14)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_014_rst_028_ma_distance_1008_028'] = {'inputs': ['rst_base_universe_d2_014_rst_028_ma_distance_1008_028'], 'func': rst_base_universe_d3_014_rst_028_ma_distance_1008_028}


def rst_base_universe_d3_015_rst_029_stochastic_position_1260_029(rst_base_universe_d2_015_rst_029_stochastic_position_1260_029):
    return _base_universe_d3(rst_base_universe_d2_015_rst_029_stochastic_position_1260_029, 15)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_015_rst_029_stochastic_position_1260_029'] = {'inputs': ['rst_base_universe_d2_015_rst_029_stochastic_position_1260_029'], 'func': rst_base_universe_d3_015_rst_029_stochastic_position_1260_029}


def rst_base_universe_d3_016_rst_basefill_001(rst_base_universe_d2_016_rst_basefill_001):
    return _base_universe_d3(rst_base_universe_d2_016_rst_basefill_001, 16)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_016_rst_basefill_001'] = {'inputs': ['rst_base_universe_d2_016_rst_basefill_001'], 'func': rst_base_universe_d3_016_rst_basefill_001}


def rst_base_universe_d3_017_rst_basefill_002(rst_base_universe_d2_017_rst_basefill_002):
    return _base_universe_d3(rst_base_universe_d2_017_rst_basefill_002, 17)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_017_rst_basefill_002'] = {'inputs': ['rst_base_universe_d2_017_rst_basefill_002'], 'func': rst_base_universe_d3_017_rst_basefill_002}


def rst_base_universe_d3_018_rst_basefill_006(rst_base_universe_d2_018_rst_basefill_006):
    return _base_universe_d3(rst_base_universe_d2_018_rst_basefill_006, 18)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_018_rst_basefill_006'] = {'inputs': ['rst_base_universe_d2_018_rst_basefill_006'], 'func': rst_base_universe_d3_018_rst_basefill_006}


def rst_base_universe_d3_019_rst_basefill_007(rst_base_universe_d2_019_rst_basefill_007):
    return _base_universe_d3(rst_base_universe_d2_019_rst_basefill_007, 19)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_019_rst_basefill_007'] = {'inputs': ['rst_base_universe_d2_019_rst_basefill_007'], 'func': rst_base_universe_d3_019_rst_basefill_007}


def rst_base_universe_d3_020_rst_basefill_008(rst_base_universe_d2_020_rst_basefill_008):
    return _base_universe_d3(rst_base_universe_d2_020_rst_basefill_008, 20)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_020_rst_basefill_008'] = {'inputs': ['rst_base_universe_d2_020_rst_basefill_008'], 'func': rst_base_universe_d3_020_rst_basefill_008}


def rst_base_universe_d3_021_rst_basefill_012(rst_base_universe_d2_021_rst_basefill_012):
    return _base_universe_d3(rst_base_universe_d2_021_rst_basefill_012, 21)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_021_rst_basefill_012'] = {'inputs': ['rst_base_universe_d2_021_rst_basefill_012'], 'func': rst_base_universe_d3_021_rst_basefill_012}


def rst_base_universe_d3_022_rst_basefill_013(rst_base_universe_d2_022_rst_basefill_013):
    return _base_universe_d3(rst_base_universe_d2_022_rst_basefill_013, 22)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_022_rst_basefill_013'] = {'inputs': ['rst_base_universe_d2_022_rst_basefill_013'], 'func': rst_base_universe_d3_022_rst_basefill_013}


def rst_base_universe_d3_023_rst_basefill_014(rst_base_universe_d2_023_rst_basefill_014):
    return _base_universe_d3(rst_base_universe_d2_023_rst_basefill_014, 23)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_023_rst_basefill_014'] = {'inputs': ['rst_base_universe_d2_023_rst_basefill_014'], 'func': rst_base_universe_d3_023_rst_basefill_014}


def rst_base_universe_d3_024_rst_basefill_018(rst_base_universe_d2_024_rst_basefill_018):
    return _base_universe_d3(rst_base_universe_d2_024_rst_basefill_018, 24)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_024_rst_basefill_018'] = {'inputs': ['rst_base_universe_d2_024_rst_basefill_018'], 'func': rst_base_universe_d3_024_rst_basefill_018}


def rst_base_universe_d3_025_rst_basefill_019(rst_base_universe_d2_025_rst_basefill_019):
    return _base_universe_d3(rst_base_universe_d2_025_rst_basefill_019, 25)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_025_rst_basefill_019'] = {'inputs': ['rst_base_universe_d2_025_rst_basefill_019'], 'func': rst_base_universe_d3_025_rst_basefill_019}


def rst_base_universe_d3_026_rst_basefill_020(rst_base_universe_d2_026_rst_basefill_020):
    return _base_universe_d3(rst_base_universe_d2_026_rst_basefill_020, 26)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_026_rst_basefill_020'] = {'inputs': ['rst_base_universe_d2_026_rst_basefill_020'], 'func': rst_base_universe_d3_026_rst_basefill_020}


def rst_base_universe_d3_027_rst_basefill_024(rst_base_universe_d2_027_rst_basefill_024):
    return _base_universe_d3(rst_base_universe_d2_027_rst_basefill_024, 27)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_027_rst_basefill_024'] = {'inputs': ['rst_base_universe_d2_027_rst_basefill_024'], 'func': rst_base_universe_d3_027_rst_basefill_024}


def rst_base_universe_d3_028_rst_basefill_025(rst_base_universe_d2_028_rst_basefill_025):
    return _base_universe_d3(rst_base_universe_d2_028_rst_basefill_025, 28)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_028_rst_basefill_025'] = {'inputs': ['rst_base_universe_d2_028_rst_basefill_025'], 'func': rst_base_universe_d3_028_rst_basefill_025}


def rst_base_universe_d3_029_rst_basefill_026(rst_base_universe_d2_029_rst_basefill_026):
    return _base_universe_d3(rst_base_universe_d2_029_rst_basefill_026, 29)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_029_rst_basefill_026'] = {'inputs': ['rst_base_universe_d2_029_rst_basefill_026'], 'func': rst_base_universe_d3_029_rst_basefill_026}


def rst_base_universe_d3_030_rst_basefill_030(rst_base_universe_d2_030_rst_basefill_030):
    return _base_universe_d3(rst_base_universe_d2_030_rst_basefill_030, 30)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_030_rst_basefill_030'] = {'inputs': ['rst_base_universe_d2_030_rst_basefill_030'], 'func': rst_base_universe_d3_030_rst_basefill_030}


def rst_base_universe_d3_031_rst_basefill_031(rst_base_universe_d2_031_rst_basefill_031):
    return _base_universe_d3(rst_base_universe_d2_031_rst_basefill_031, 31)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_031_rst_basefill_031'] = {'inputs': ['rst_base_universe_d2_031_rst_basefill_031'], 'func': rst_base_universe_d3_031_rst_basefill_031}


def rst_base_universe_d3_032_rst_basefill_032(rst_base_universe_d2_032_rst_basefill_032):
    return _base_universe_d3(rst_base_universe_d2_032_rst_basefill_032, 32)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_032_rst_basefill_032'] = {'inputs': ['rst_base_universe_d2_032_rst_basefill_032'], 'func': rst_base_universe_d3_032_rst_basefill_032}


def rst_base_universe_d3_033_rst_basefill_033(rst_base_universe_d2_033_rst_basefill_033):
    return _base_universe_d3(rst_base_universe_d2_033_rst_basefill_033, 33)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_033_rst_basefill_033'] = {'inputs': ['rst_base_universe_d2_033_rst_basefill_033'], 'func': rst_base_universe_d3_033_rst_basefill_033}


def rst_base_universe_d3_034_rst_basefill_034(rst_base_universe_d2_034_rst_basefill_034):
    return _base_universe_d3(rst_base_universe_d2_034_rst_basefill_034, 34)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_034_rst_basefill_034'] = {'inputs': ['rst_base_universe_d2_034_rst_basefill_034'], 'func': rst_base_universe_d3_034_rst_basefill_034}


def rst_base_universe_d3_035_rst_basefill_035(rst_base_universe_d2_035_rst_basefill_035):
    return _base_universe_d3(rst_base_universe_d2_035_rst_basefill_035, 35)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_035_rst_basefill_035'] = {'inputs': ['rst_base_universe_d2_035_rst_basefill_035'], 'func': rst_base_universe_d3_035_rst_basefill_035}


def rst_base_universe_d3_036_rst_basefill_036(rst_base_universe_d2_036_rst_basefill_036):
    return _base_universe_d3(rst_base_universe_d2_036_rst_basefill_036, 36)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_036_rst_basefill_036'] = {'inputs': ['rst_base_universe_d2_036_rst_basefill_036'], 'func': rst_base_universe_d3_036_rst_basefill_036}


def rst_base_universe_d3_037_rst_basefill_037(rst_base_universe_d2_037_rst_basefill_037):
    return _base_universe_d3(rst_base_universe_d2_037_rst_basefill_037, 37)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_037_rst_basefill_037'] = {'inputs': ['rst_base_universe_d2_037_rst_basefill_037'], 'func': rst_base_universe_d3_037_rst_basefill_037}


def rst_base_universe_d3_038_rst_basefill_038(rst_base_universe_d2_038_rst_basefill_038):
    return _base_universe_d3(rst_base_universe_d2_038_rst_basefill_038, 38)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_038_rst_basefill_038'] = {'inputs': ['rst_base_universe_d2_038_rst_basefill_038'], 'func': rst_base_universe_d3_038_rst_basefill_038}


def rst_base_universe_d3_039_rst_basefill_039(rst_base_universe_d2_039_rst_basefill_039):
    return _base_universe_d3(rst_base_universe_d2_039_rst_basefill_039, 39)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_039_rst_basefill_039'] = {'inputs': ['rst_base_universe_d2_039_rst_basefill_039'], 'func': rst_base_universe_d3_039_rst_basefill_039}


def rst_base_universe_d3_040_rst_basefill_040(rst_base_universe_d2_040_rst_basefill_040):
    return _base_universe_d3(rst_base_universe_d2_040_rst_basefill_040, 40)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_040_rst_basefill_040'] = {'inputs': ['rst_base_universe_d2_040_rst_basefill_040'], 'func': rst_base_universe_d3_040_rst_basefill_040}


def rst_base_universe_d3_041_rst_basefill_041(rst_base_universe_d2_041_rst_basefill_041):
    return _base_universe_d3(rst_base_universe_d2_041_rst_basefill_041, 41)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_041_rst_basefill_041'] = {'inputs': ['rst_base_universe_d2_041_rst_basefill_041'], 'func': rst_base_universe_d3_041_rst_basefill_041}


def rst_base_universe_d3_042_rst_basefill_042(rst_base_universe_d2_042_rst_basefill_042):
    return _base_universe_d3(rst_base_universe_d2_042_rst_basefill_042, 42)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_042_rst_basefill_042'] = {'inputs': ['rst_base_universe_d2_042_rst_basefill_042'], 'func': rst_base_universe_d3_042_rst_basefill_042}


def rst_base_universe_d3_043_rst_basefill_043(rst_base_universe_d2_043_rst_basefill_043):
    return _base_universe_d3(rst_base_universe_d2_043_rst_basefill_043, 43)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_043_rst_basefill_043'] = {'inputs': ['rst_base_universe_d2_043_rst_basefill_043'], 'func': rst_base_universe_d3_043_rst_basefill_043}


def rst_base_universe_d3_044_rst_basefill_044(rst_base_universe_d2_044_rst_basefill_044):
    return _base_universe_d3(rst_base_universe_d2_044_rst_basefill_044, 44)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_044_rst_basefill_044'] = {'inputs': ['rst_base_universe_d2_044_rst_basefill_044'], 'func': rst_base_universe_d3_044_rst_basefill_044}


def rst_base_universe_d3_045_rst_basefill_045(rst_base_universe_d2_045_rst_basefill_045):
    return _base_universe_d3(rst_base_universe_d2_045_rst_basefill_045, 45)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_045_rst_basefill_045'] = {'inputs': ['rst_base_universe_d2_045_rst_basefill_045'], 'func': rst_base_universe_d3_045_rst_basefill_045}


def rst_base_universe_d3_046_rst_basefill_046(rst_base_universe_d2_046_rst_basefill_046):
    return _base_universe_d3(rst_base_universe_d2_046_rst_basefill_046, 46)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_046_rst_basefill_046'] = {'inputs': ['rst_base_universe_d2_046_rst_basefill_046'], 'func': rst_base_universe_d3_046_rst_basefill_046}


def rst_base_universe_d3_047_rst_basefill_047(rst_base_universe_d2_047_rst_basefill_047):
    return _base_universe_d3(rst_base_universe_d2_047_rst_basefill_047, 47)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_047_rst_basefill_047'] = {'inputs': ['rst_base_universe_d2_047_rst_basefill_047'], 'func': rst_base_universe_d3_047_rst_basefill_047}


def rst_base_universe_d3_048_rst_basefill_048(rst_base_universe_d2_048_rst_basefill_048):
    return _base_universe_d3(rst_base_universe_d2_048_rst_basefill_048, 48)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_048_rst_basefill_048'] = {'inputs': ['rst_base_universe_d2_048_rst_basefill_048'], 'func': rst_base_universe_d3_048_rst_basefill_048}


def rst_base_universe_d3_049_rst_basefill_049(rst_base_universe_d2_049_rst_basefill_049):
    return _base_universe_d3(rst_base_universe_d2_049_rst_basefill_049, 49)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_049_rst_basefill_049'] = {'inputs': ['rst_base_universe_d2_049_rst_basefill_049'], 'func': rst_base_universe_d3_049_rst_basefill_049}


def rst_base_universe_d3_050_rst_basefill_050(rst_base_universe_d2_050_rst_basefill_050):
    return _base_universe_d3(rst_base_universe_d2_050_rst_basefill_050, 50)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_050_rst_basefill_050'] = {'inputs': ['rst_base_universe_d2_050_rst_basefill_050'], 'func': rst_base_universe_d3_050_rst_basefill_050}


def rst_base_universe_d3_051_rst_basefill_051(rst_base_universe_d2_051_rst_basefill_051):
    return _base_universe_d3(rst_base_universe_d2_051_rst_basefill_051, 51)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_051_rst_basefill_051'] = {'inputs': ['rst_base_universe_d2_051_rst_basefill_051'], 'func': rst_base_universe_d3_051_rst_basefill_051}


def rst_base_universe_d3_052_rst_basefill_052(rst_base_universe_d2_052_rst_basefill_052):
    return _base_universe_d3(rst_base_universe_d2_052_rst_basefill_052, 52)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_052_rst_basefill_052'] = {'inputs': ['rst_base_universe_d2_052_rst_basefill_052'], 'func': rst_base_universe_d3_052_rst_basefill_052}


def rst_base_universe_d3_053_rst_basefill_053(rst_base_universe_d2_053_rst_basefill_053):
    return _base_universe_d3(rst_base_universe_d2_053_rst_basefill_053, 53)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_053_rst_basefill_053'] = {'inputs': ['rst_base_universe_d2_053_rst_basefill_053'], 'func': rst_base_universe_d3_053_rst_basefill_053}


def rst_base_universe_d3_054_rst_basefill_054(rst_base_universe_d2_054_rst_basefill_054):
    return _base_universe_d3(rst_base_universe_d2_054_rst_basefill_054, 54)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_054_rst_basefill_054'] = {'inputs': ['rst_base_universe_d2_054_rst_basefill_054'], 'func': rst_base_universe_d3_054_rst_basefill_054}


def rst_base_universe_d3_055_rst_basefill_055(rst_base_universe_d2_055_rst_basefill_055):
    return _base_universe_d3(rst_base_universe_d2_055_rst_basefill_055, 55)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_055_rst_basefill_055'] = {'inputs': ['rst_base_universe_d2_055_rst_basefill_055'], 'func': rst_base_universe_d3_055_rst_basefill_055}


def rst_base_universe_d3_056_rst_basefill_056(rst_base_universe_d2_056_rst_basefill_056):
    return _base_universe_d3(rst_base_universe_d2_056_rst_basefill_056, 56)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_056_rst_basefill_056'] = {'inputs': ['rst_base_universe_d2_056_rst_basefill_056'], 'func': rst_base_universe_d3_056_rst_basefill_056}


def rst_base_universe_d3_057_rst_basefill_057(rst_base_universe_d2_057_rst_basefill_057):
    return _base_universe_d3(rst_base_universe_d2_057_rst_basefill_057, 57)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_057_rst_basefill_057'] = {'inputs': ['rst_base_universe_d2_057_rst_basefill_057'], 'func': rst_base_universe_d3_057_rst_basefill_057}


def rst_base_universe_d3_058_rst_basefill_058(rst_base_universe_d2_058_rst_basefill_058):
    return _base_universe_d3(rst_base_universe_d2_058_rst_basefill_058, 58)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_058_rst_basefill_058'] = {'inputs': ['rst_base_universe_d2_058_rst_basefill_058'], 'func': rst_base_universe_d3_058_rst_basefill_058}


def rst_base_universe_d3_059_rst_basefill_059(rst_base_universe_d2_059_rst_basefill_059):
    return _base_universe_d3(rst_base_universe_d2_059_rst_basefill_059, 59)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_059_rst_basefill_059'] = {'inputs': ['rst_base_universe_d2_059_rst_basefill_059'], 'func': rst_base_universe_d3_059_rst_basefill_059}


def rst_base_universe_d3_060_rst_basefill_060(rst_base_universe_d2_060_rst_basefill_060):
    return _base_universe_d3(rst_base_universe_d2_060_rst_basefill_060, 60)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_060_rst_basefill_060'] = {'inputs': ['rst_base_universe_d2_060_rst_basefill_060'], 'func': rst_base_universe_d3_060_rst_basefill_060}


def rst_base_universe_d3_061_rst_basefill_061(rst_base_universe_d2_061_rst_basefill_061):
    return _base_universe_d3(rst_base_universe_d2_061_rst_basefill_061, 61)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_061_rst_basefill_061'] = {'inputs': ['rst_base_universe_d2_061_rst_basefill_061'], 'func': rst_base_universe_d3_061_rst_basefill_061}


def rst_base_universe_d3_062_rst_basefill_062(rst_base_universe_d2_062_rst_basefill_062):
    return _base_universe_d3(rst_base_universe_d2_062_rst_basefill_062, 62)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_062_rst_basefill_062'] = {'inputs': ['rst_base_universe_d2_062_rst_basefill_062'], 'func': rst_base_universe_d3_062_rst_basefill_062}


def rst_base_universe_d3_063_rst_basefill_063(rst_base_universe_d2_063_rst_basefill_063):
    return _base_universe_d3(rst_base_universe_d2_063_rst_basefill_063, 63)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_063_rst_basefill_063'] = {'inputs': ['rst_base_universe_d2_063_rst_basefill_063'], 'func': rst_base_universe_d3_063_rst_basefill_063}


def rst_base_universe_d3_064_rst_basefill_064(rst_base_universe_d2_064_rst_basefill_064):
    return _base_universe_d3(rst_base_universe_d2_064_rst_basefill_064, 64)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_064_rst_basefill_064'] = {'inputs': ['rst_base_universe_d2_064_rst_basefill_064'], 'func': rst_base_universe_d3_064_rst_basefill_064}


def rst_base_universe_d3_065_rst_basefill_065(rst_base_universe_d2_065_rst_basefill_065):
    return _base_universe_d3(rst_base_universe_d2_065_rst_basefill_065, 65)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_065_rst_basefill_065'] = {'inputs': ['rst_base_universe_d2_065_rst_basefill_065'], 'func': rst_base_universe_d3_065_rst_basefill_065}


def rst_base_universe_d3_066_rst_basefill_066(rst_base_universe_d2_066_rst_basefill_066):
    return _base_universe_d3(rst_base_universe_d2_066_rst_basefill_066, 66)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_066_rst_basefill_066'] = {'inputs': ['rst_base_universe_d2_066_rst_basefill_066'], 'func': rst_base_universe_d3_066_rst_basefill_066}


def rst_base_universe_d3_067_rst_basefill_067(rst_base_universe_d2_067_rst_basefill_067):
    return _base_universe_d3(rst_base_universe_d2_067_rst_basefill_067, 67)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_067_rst_basefill_067'] = {'inputs': ['rst_base_universe_d2_067_rst_basefill_067'], 'func': rst_base_universe_d3_067_rst_basefill_067}


def rst_base_universe_d3_068_rst_basefill_068(rst_base_universe_d2_068_rst_basefill_068):
    return _base_universe_d3(rst_base_universe_d2_068_rst_basefill_068, 68)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_068_rst_basefill_068'] = {'inputs': ['rst_base_universe_d2_068_rst_basefill_068'], 'func': rst_base_universe_d3_068_rst_basefill_068}


def rst_base_universe_d3_069_rst_basefill_069(rst_base_universe_d2_069_rst_basefill_069):
    return _base_universe_d3(rst_base_universe_d2_069_rst_basefill_069, 69)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_069_rst_basefill_069'] = {'inputs': ['rst_base_universe_d2_069_rst_basefill_069'], 'func': rst_base_universe_d3_069_rst_basefill_069}


def rst_base_universe_d3_070_rst_basefill_070(rst_base_universe_d2_070_rst_basefill_070):
    return _base_universe_d3(rst_base_universe_d2_070_rst_basefill_070, 70)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_070_rst_basefill_070'] = {'inputs': ['rst_base_universe_d2_070_rst_basefill_070'], 'func': rst_base_universe_d3_070_rst_basefill_070}


def rst_base_universe_d3_071_rst_basefill_071(rst_base_universe_d2_071_rst_basefill_071):
    return _base_universe_d3(rst_base_universe_d2_071_rst_basefill_071, 71)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_071_rst_basefill_071'] = {'inputs': ['rst_base_universe_d2_071_rst_basefill_071'], 'func': rst_base_universe_d3_071_rst_basefill_071}


def rst_base_universe_d3_072_rst_basefill_072(rst_base_universe_d2_072_rst_basefill_072):
    return _base_universe_d3(rst_base_universe_d2_072_rst_basefill_072, 72)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_072_rst_basefill_072'] = {'inputs': ['rst_base_universe_d2_072_rst_basefill_072'], 'func': rst_base_universe_d3_072_rst_basefill_072}


def rst_base_universe_d3_073_rst_basefill_073(rst_base_universe_d2_073_rst_basefill_073):
    return _base_universe_d3(rst_base_universe_d2_073_rst_basefill_073, 73)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_073_rst_basefill_073'] = {'inputs': ['rst_base_universe_d2_073_rst_basefill_073'], 'func': rst_base_universe_d3_073_rst_basefill_073}


def rst_base_universe_d3_074_rst_basefill_074(rst_base_universe_d2_074_rst_basefill_074):
    return _base_universe_d3(rst_base_universe_d2_074_rst_basefill_074, 74)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_074_rst_basefill_074'] = {'inputs': ['rst_base_universe_d2_074_rst_basefill_074'], 'func': rst_base_universe_d3_074_rst_basefill_074}


def rst_base_universe_d3_075_rst_basefill_075(rst_base_universe_d2_075_rst_basefill_075):
    return _base_universe_d3(rst_base_universe_d2_075_rst_basefill_075, 75)
RST_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rst_base_universe_d3_075_rst_basefill_075'] = {'inputs': ['rst_base_universe_d2_075_rst_basefill_075'], 'func': rst_base_universe_d3_075_rst_basefill_075}
