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



def tin_001_amihud_illiquidity_accel_1(tin_001_amihud_illiquidity_roc_1):
    feature = _s(tin_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def tin_007_amihud_illiquidity_accel_5(tin_007_amihud_illiquidity_roc_5):
    feature = _s(tin_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def tin_013_amihud_illiquidity_accel_42(tin_013_amihud_illiquidity_roc_42):
    feature = _s(tin_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def tin_179_tin_019_amihud_illiquidity_42_019_accel_126(tin_154_tin_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(tin_154_tin_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def tin_180_tin_025_amihud_illiquidity_378_025_accel_378(tin_155_tin_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(tin_155_tin_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















TRADING_INTENSITY_REGISTRY_3RD_DERIVATIVES = {
    'tin_001_amihud_illiquidity_accel_1': {'inputs': ['tin_001_amihud_illiquidity_roc_1'], 'func': tin_001_amihud_illiquidity_accel_1},
    'tin_007_amihud_illiquidity_accel_5': {'inputs': ['tin_007_amihud_illiquidity_roc_5'], 'func': tin_007_amihud_illiquidity_accel_5},
    'tin_013_amihud_illiquidity_accel_42': {'inputs': ['tin_013_amihud_illiquidity_roc_42'], 'func': tin_013_amihud_illiquidity_accel_42},
    'tin_179_tin_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['tin_154_tin_019_amihud_illiquidity_42_019_roc_126'], 'func': tin_179_tin_019_amihud_illiquidity_42_019_accel_126},
    'tin_180_tin_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['tin_155_tin_025_amihud_illiquidity_378_025_roc_378'], 'func': tin_180_tin_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ti_replacement_d3_001(ti_replacement_d2_001):
    feature = _clean(ti_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_001'] = {'inputs': ['ti_replacement_d2_001'], 'func': ti_replacement_d3_001}


def ti_replacement_d3_002(ti_replacement_d2_002):
    feature = _clean(ti_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_002'] = {'inputs': ['ti_replacement_d2_002'], 'func': ti_replacement_d3_002}


def ti_replacement_d3_003(ti_replacement_d2_003):
    feature = _clean(ti_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_003'] = {'inputs': ['ti_replacement_d2_003'], 'func': ti_replacement_d3_003}


def ti_replacement_d3_004(ti_replacement_d2_004):
    feature = _clean(ti_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_004'] = {'inputs': ['ti_replacement_d2_004'], 'func': ti_replacement_d3_004}


def ti_replacement_d3_005(ti_replacement_d2_005):
    feature = _clean(ti_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_005'] = {'inputs': ['ti_replacement_d2_005'], 'func': ti_replacement_d3_005}


def ti_replacement_d3_006(ti_replacement_d2_006):
    feature = _clean(ti_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_006'] = {'inputs': ['ti_replacement_d2_006'], 'func': ti_replacement_d3_006}


def ti_replacement_d3_007(ti_replacement_d2_007):
    feature = _clean(ti_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_007'] = {'inputs': ['ti_replacement_d2_007'], 'func': ti_replacement_d3_007}


def ti_replacement_d3_008(ti_replacement_d2_008):
    feature = _clean(ti_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_008'] = {'inputs': ['ti_replacement_d2_008'], 'func': ti_replacement_d3_008}


def ti_replacement_d3_009(ti_replacement_d2_009):
    feature = _clean(ti_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_009'] = {'inputs': ['ti_replacement_d2_009'], 'func': ti_replacement_d3_009}


def ti_replacement_d3_010(ti_replacement_d2_010):
    feature = _clean(ti_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_010'] = {'inputs': ['ti_replacement_d2_010'], 'func': ti_replacement_d3_010}


def ti_replacement_d3_011(ti_replacement_d2_011):
    feature = _clean(ti_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_011'] = {'inputs': ['ti_replacement_d2_011'], 'func': ti_replacement_d3_011}


def ti_replacement_d3_012(ti_replacement_d2_012):
    feature = _clean(ti_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_012'] = {'inputs': ['ti_replacement_d2_012'], 'func': ti_replacement_d3_012}


def ti_replacement_d3_013(ti_replacement_d2_013):
    feature = _clean(ti_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_013'] = {'inputs': ['ti_replacement_d2_013'], 'func': ti_replacement_d3_013}


def ti_replacement_d3_014(ti_replacement_d2_014):
    feature = _clean(ti_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_014'] = {'inputs': ['ti_replacement_d2_014'], 'func': ti_replacement_d3_014}


def ti_replacement_d3_015(ti_replacement_d2_015):
    feature = _clean(ti_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_015'] = {'inputs': ['ti_replacement_d2_015'], 'func': ti_replacement_d3_015}


def ti_replacement_d3_016(ti_replacement_d2_016):
    feature = _clean(ti_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_016'] = {'inputs': ['ti_replacement_d2_016'], 'func': ti_replacement_d3_016}


def ti_replacement_d3_017(ti_replacement_d2_017):
    feature = _clean(ti_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_017'] = {'inputs': ['ti_replacement_d2_017'], 'func': ti_replacement_d3_017}


def ti_replacement_d3_018(ti_replacement_d2_018):
    feature = _clean(ti_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_018'] = {'inputs': ['ti_replacement_d2_018'], 'func': ti_replacement_d3_018}


def ti_replacement_d3_019(ti_replacement_d2_019):
    feature = _clean(ti_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_019'] = {'inputs': ['ti_replacement_d2_019'], 'func': ti_replacement_d3_019}


def ti_replacement_d3_020(ti_replacement_d2_020):
    feature = _clean(ti_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_020'] = {'inputs': ['ti_replacement_d2_020'], 'func': ti_replacement_d3_020}


def ti_replacement_d3_021(ti_replacement_d2_021):
    feature = _clean(ti_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_021'] = {'inputs': ['ti_replacement_d2_021'], 'func': ti_replacement_d3_021}


def ti_replacement_d3_022(ti_replacement_d2_022):
    feature = _clean(ti_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_022'] = {'inputs': ['ti_replacement_d2_022'], 'func': ti_replacement_d3_022}


def ti_replacement_d3_023(ti_replacement_d2_023):
    feature = _clean(ti_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_023'] = {'inputs': ['ti_replacement_d2_023'], 'func': ti_replacement_d3_023}


def ti_replacement_d3_024(ti_replacement_d2_024):
    feature = _clean(ti_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_024'] = {'inputs': ['ti_replacement_d2_024'], 'func': ti_replacement_d3_024}


def ti_replacement_d3_025(ti_replacement_d2_025):
    feature = _clean(ti_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_025'] = {'inputs': ['ti_replacement_d2_025'], 'func': ti_replacement_d3_025}


def ti_replacement_d3_026(ti_replacement_d2_026):
    feature = _clean(ti_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_026'] = {'inputs': ['ti_replacement_d2_026'], 'func': ti_replacement_d3_026}


def ti_replacement_d3_027(ti_replacement_d2_027):
    feature = _clean(ti_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_027'] = {'inputs': ['ti_replacement_d2_027'], 'func': ti_replacement_d3_027}


def ti_replacement_d3_028(ti_replacement_d2_028):
    feature = _clean(ti_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_028'] = {'inputs': ['ti_replacement_d2_028'], 'func': ti_replacement_d3_028}


def ti_replacement_d3_029(ti_replacement_d2_029):
    feature = _clean(ti_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_029'] = {'inputs': ['ti_replacement_d2_029'], 'func': ti_replacement_d3_029}


def ti_replacement_d3_030(ti_replacement_d2_030):
    feature = _clean(ti_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_030'] = {'inputs': ['ti_replacement_d2_030'], 'func': ti_replacement_d3_030}


def ti_replacement_d3_031(ti_replacement_d2_031):
    feature = _clean(ti_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_031'] = {'inputs': ['ti_replacement_d2_031'], 'func': ti_replacement_d3_031}


def ti_replacement_d3_032(ti_replacement_d2_032):
    feature = _clean(ti_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_032'] = {'inputs': ['ti_replacement_d2_032'], 'func': ti_replacement_d3_032}


def ti_replacement_d3_033(ti_replacement_d2_033):
    feature = _clean(ti_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_033'] = {'inputs': ['ti_replacement_d2_033'], 'func': ti_replacement_d3_033}


def ti_replacement_d3_034(ti_replacement_d2_034):
    feature = _clean(ti_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_034'] = {'inputs': ['ti_replacement_d2_034'], 'func': ti_replacement_d3_034}


def ti_replacement_d3_035(ti_replacement_d2_035):
    feature = _clean(ti_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_035'] = {'inputs': ['ti_replacement_d2_035'], 'func': ti_replacement_d3_035}


def ti_replacement_d3_036(ti_replacement_d2_036):
    feature = _clean(ti_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_036'] = {'inputs': ['ti_replacement_d2_036'], 'func': ti_replacement_d3_036}


def ti_replacement_d3_037(ti_replacement_d2_037):
    feature = _clean(ti_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_037'] = {'inputs': ['ti_replacement_d2_037'], 'func': ti_replacement_d3_037}


def ti_replacement_d3_038(ti_replacement_d2_038):
    feature = _clean(ti_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_038'] = {'inputs': ['ti_replacement_d2_038'], 'func': ti_replacement_d3_038}


def ti_replacement_d3_039(ti_replacement_d2_039):
    feature = _clean(ti_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_039'] = {'inputs': ['ti_replacement_d2_039'], 'func': ti_replacement_d3_039}


def ti_replacement_d3_040(ti_replacement_d2_040):
    feature = _clean(ti_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_040'] = {'inputs': ['ti_replacement_d2_040'], 'func': ti_replacement_d3_040}


def ti_replacement_d3_041(ti_replacement_d2_041):
    feature = _clean(ti_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_041'] = {'inputs': ['ti_replacement_d2_041'], 'func': ti_replacement_d3_041}


def ti_replacement_d3_042(ti_replacement_d2_042):
    feature = _clean(ti_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_042'] = {'inputs': ['ti_replacement_d2_042'], 'func': ti_replacement_d3_042}


def ti_replacement_d3_043(ti_replacement_d2_043):
    feature = _clean(ti_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_043'] = {'inputs': ['ti_replacement_d2_043'], 'func': ti_replacement_d3_043}


def ti_replacement_d3_044(ti_replacement_d2_044):
    feature = _clean(ti_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_044'] = {'inputs': ['ti_replacement_d2_044'], 'func': ti_replacement_d3_044}


def ti_replacement_d3_045(ti_replacement_d2_045):
    feature = _clean(ti_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_045'] = {'inputs': ['ti_replacement_d2_045'], 'func': ti_replacement_d3_045}


def ti_replacement_d3_046(ti_replacement_d2_046):
    feature = _clean(ti_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_046'] = {'inputs': ['ti_replacement_d2_046'], 'func': ti_replacement_d3_046}


def ti_replacement_d3_047(ti_replacement_d2_047):
    feature = _clean(ti_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_047'] = {'inputs': ['ti_replacement_d2_047'], 'func': ti_replacement_d3_047}


def ti_replacement_d3_048(ti_replacement_d2_048):
    feature = _clean(ti_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_048'] = {'inputs': ['ti_replacement_d2_048'], 'func': ti_replacement_d3_048}


def ti_replacement_d3_049(ti_replacement_d2_049):
    feature = _clean(ti_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_049'] = {'inputs': ['ti_replacement_d2_049'], 'func': ti_replacement_d3_049}


def ti_replacement_d3_050(ti_replacement_d2_050):
    feature = _clean(ti_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_050'] = {'inputs': ['ti_replacement_d2_050'], 'func': ti_replacement_d3_050}


def ti_replacement_d3_051(ti_replacement_d2_051):
    feature = _clean(ti_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_051'] = {'inputs': ['ti_replacement_d2_051'], 'func': ti_replacement_d3_051}


def ti_replacement_d3_052(ti_replacement_d2_052):
    feature = _clean(ti_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_052'] = {'inputs': ['ti_replacement_d2_052'], 'func': ti_replacement_d3_052}


def ti_replacement_d3_053(ti_replacement_d2_053):
    feature = _clean(ti_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_053'] = {'inputs': ['ti_replacement_d2_053'], 'func': ti_replacement_d3_053}


def ti_replacement_d3_054(ti_replacement_d2_054):
    feature = _clean(ti_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_054'] = {'inputs': ['ti_replacement_d2_054'], 'func': ti_replacement_d3_054}


def ti_replacement_d3_055(ti_replacement_d2_055):
    feature = _clean(ti_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_055'] = {'inputs': ['ti_replacement_d2_055'], 'func': ti_replacement_d3_055}


def ti_replacement_d3_056(ti_replacement_d2_056):
    feature = _clean(ti_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_056'] = {'inputs': ['ti_replacement_d2_056'], 'func': ti_replacement_d3_056}


def ti_replacement_d3_057(ti_replacement_d2_057):
    feature = _clean(ti_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_057'] = {'inputs': ['ti_replacement_d2_057'], 'func': ti_replacement_d3_057}


def ti_replacement_d3_058(ti_replacement_d2_058):
    feature = _clean(ti_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_058'] = {'inputs': ['ti_replacement_d2_058'], 'func': ti_replacement_d3_058}


def ti_replacement_d3_059(ti_replacement_d2_059):
    feature = _clean(ti_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_059'] = {'inputs': ['ti_replacement_d2_059'], 'func': ti_replacement_d3_059}


def ti_replacement_d3_060(ti_replacement_d2_060):
    feature = _clean(ti_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_060'] = {'inputs': ['ti_replacement_d2_060'], 'func': ti_replacement_d3_060}


def ti_replacement_d3_061(ti_replacement_d2_061):
    feature = _clean(ti_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_061'] = {'inputs': ['ti_replacement_d2_061'], 'func': ti_replacement_d3_061}


def ti_replacement_d3_062(ti_replacement_d2_062):
    feature = _clean(ti_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_062'] = {'inputs': ['ti_replacement_d2_062'], 'func': ti_replacement_d3_062}


def ti_replacement_d3_063(ti_replacement_d2_063):
    feature = _clean(ti_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_063'] = {'inputs': ['ti_replacement_d2_063'], 'func': ti_replacement_d3_063}


def ti_replacement_d3_064(ti_replacement_d2_064):
    feature = _clean(ti_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_064'] = {'inputs': ['ti_replacement_d2_064'], 'func': ti_replacement_d3_064}


def ti_replacement_d3_065(ti_replacement_d2_065):
    feature = _clean(ti_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_065'] = {'inputs': ['ti_replacement_d2_065'], 'func': ti_replacement_d3_065}


def ti_replacement_d3_066(ti_replacement_d2_066):
    feature = _clean(ti_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_066'] = {'inputs': ['ti_replacement_d2_066'], 'func': ti_replacement_d3_066}


def ti_replacement_d3_067(ti_replacement_d2_067):
    feature = _clean(ti_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_067'] = {'inputs': ['ti_replacement_d2_067'], 'func': ti_replacement_d3_067}


def ti_replacement_d3_068(ti_replacement_d2_068):
    feature = _clean(ti_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_068'] = {'inputs': ['ti_replacement_d2_068'], 'func': ti_replacement_d3_068}


def ti_replacement_d3_069(ti_replacement_d2_069):
    feature = _clean(ti_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_069'] = {'inputs': ['ti_replacement_d2_069'], 'func': ti_replacement_d3_069}


def ti_replacement_d3_070(ti_replacement_d2_070):
    feature = _clean(ti_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_070'] = {'inputs': ['ti_replacement_d2_070'], 'func': ti_replacement_d3_070}


def ti_replacement_d3_071(ti_replacement_d2_071):
    feature = _clean(ti_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_071'] = {'inputs': ['ti_replacement_d2_071'], 'func': ti_replacement_d3_071}


def ti_replacement_d3_072(ti_replacement_d2_072):
    feature = _clean(ti_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_072'] = {'inputs': ['ti_replacement_d2_072'], 'func': ti_replacement_d3_072}


def ti_replacement_d3_073(ti_replacement_d2_073):
    feature = _clean(ti_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_073'] = {'inputs': ['ti_replacement_d2_073'], 'func': ti_replacement_d3_073}


def ti_replacement_d3_074(ti_replacement_d2_074):
    feature = _clean(ti_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_074'] = {'inputs': ['ti_replacement_d2_074'], 'func': ti_replacement_d3_074}


def ti_replacement_d3_075(ti_replacement_d2_075):
    feature = _clean(ti_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_075'] = {'inputs': ['ti_replacement_d2_075'], 'func': ti_replacement_d3_075}


def ti_replacement_d3_076(ti_replacement_d2_076):
    feature = _clean(ti_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_076'] = {'inputs': ['ti_replacement_d2_076'], 'func': ti_replacement_d3_076}


def ti_replacement_d3_077(ti_replacement_d2_077):
    feature = _clean(ti_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_077'] = {'inputs': ['ti_replacement_d2_077'], 'func': ti_replacement_d3_077}


def ti_replacement_d3_078(ti_replacement_d2_078):
    feature = _clean(ti_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_078'] = {'inputs': ['ti_replacement_d2_078'], 'func': ti_replacement_d3_078}


def ti_replacement_d3_079(ti_replacement_d2_079):
    feature = _clean(ti_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_079'] = {'inputs': ['ti_replacement_d2_079'], 'func': ti_replacement_d3_079}


def ti_replacement_d3_080(ti_replacement_d2_080):
    feature = _clean(ti_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_080'] = {'inputs': ['ti_replacement_d2_080'], 'func': ti_replacement_d3_080}


def ti_replacement_d3_081(ti_replacement_d2_081):
    feature = _clean(ti_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_081'] = {'inputs': ['ti_replacement_d2_081'], 'func': ti_replacement_d3_081}


def ti_replacement_d3_082(ti_replacement_d2_082):
    feature = _clean(ti_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_082'] = {'inputs': ['ti_replacement_d2_082'], 'func': ti_replacement_d3_082}


def ti_replacement_d3_083(ti_replacement_d2_083):
    feature = _clean(ti_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_083'] = {'inputs': ['ti_replacement_d2_083'], 'func': ti_replacement_d3_083}


def ti_replacement_d3_084(ti_replacement_d2_084):
    feature = _clean(ti_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_084'] = {'inputs': ['ti_replacement_d2_084'], 'func': ti_replacement_d3_084}


def ti_replacement_d3_085(ti_replacement_d2_085):
    feature = _clean(ti_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_085'] = {'inputs': ['ti_replacement_d2_085'], 'func': ti_replacement_d3_085}


def ti_replacement_d3_086(ti_replacement_d2_086):
    feature = _clean(ti_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_086'] = {'inputs': ['ti_replacement_d2_086'], 'func': ti_replacement_d3_086}


def ti_replacement_d3_087(ti_replacement_d2_087):
    feature = _clean(ti_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_087'] = {'inputs': ['ti_replacement_d2_087'], 'func': ti_replacement_d3_087}


def ti_replacement_d3_088(ti_replacement_d2_088):
    feature = _clean(ti_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_088'] = {'inputs': ['ti_replacement_d2_088'], 'func': ti_replacement_d3_088}


def ti_replacement_d3_089(ti_replacement_d2_089):
    feature = _clean(ti_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_089'] = {'inputs': ['ti_replacement_d2_089'], 'func': ti_replacement_d3_089}


def ti_replacement_d3_090(ti_replacement_d2_090):
    feature = _clean(ti_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_090'] = {'inputs': ['ti_replacement_d2_090'], 'func': ti_replacement_d3_090}


def ti_replacement_d3_091(ti_replacement_d2_091):
    feature = _clean(ti_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_091'] = {'inputs': ['ti_replacement_d2_091'], 'func': ti_replacement_d3_091}


def ti_replacement_d3_092(ti_replacement_d2_092):
    feature = _clean(ti_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_092'] = {'inputs': ['ti_replacement_d2_092'], 'func': ti_replacement_d3_092}


def ti_replacement_d3_093(ti_replacement_d2_093):
    feature = _clean(ti_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_093'] = {'inputs': ['ti_replacement_d2_093'], 'func': ti_replacement_d3_093}


def ti_replacement_d3_094(ti_replacement_d2_094):
    feature = _clean(ti_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_094'] = {'inputs': ['ti_replacement_d2_094'], 'func': ti_replacement_d3_094}


def ti_replacement_d3_095(ti_replacement_d2_095):
    feature = _clean(ti_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_095'] = {'inputs': ['ti_replacement_d2_095'], 'func': ti_replacement_d3_095}


def ti_replacement_d3_096(ti_replacement_d2_096):
    feature = _clean(ti_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_096'] = {'inputs': ['ti_replacement_d2_096'], 'func': ti_replacement_d3_096}


def ti_replacement_d3_097(ti_replacement_d2_097):
    feature = _clean(ti_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_097'] = {'inputs': ['ti_replacement_d2_097'], 'func': ti_replacement_d3_097}


def ti_replacement_d3_098(ti_replacement_d2_098):
    feature = _clean(ti_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_098'] = {'inputs': ['ti_replacement_d2_098'], 'func': ti_replacement_d3_098}


def ti_replacement_d3_099(ti_replacement_d2_099):
    feature = _clean(ti_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_099'] = {'inputs': ['ti_replacement_d2_099'], 'func': ti_replacement_d3_099}


def ti_replacement_d3_100(ti_replacement_d2_100):
    feature = _clean(ti_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_100'] = {'inputs': ['ti_replacement_d2_100'], 'func': ti_replacement_d3_100}


def ti_replacement_d3_101(ti_replacement_d2_101):
    feature = _clean(ti_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_101'] = {'inputs': ['ti_replacement_d2_101'], 'func': ti_replacement_d3_101}


def ti_replacement_d3_102(ti_replacement_d2_102):
    feature = _clean(ti_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_102'] = {'inputs': ['ti_replacement_d2_102'], 'func': ti_replacement_d3_102}


def ti_replacement_d3_103(ti_replacement_d2_103):
    feature = _clean(ti_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_103'] = {'inputs': ['ti_replacement_d2_103'], 'func': ti_replacement_d3_103}


def ti_replacement_d3_104(ti_replacement_d2_104):
    feature = _clean(ti_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_104'] = {'inputs': ['ti_replacement_d2_104'], 'func': ti_replacement_d3_104}


def ti_replacement_d3_105(ti_replacement_d2_105):
    feature = _clean(ti_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_105'] = {'inputs': ['ti_replacement_d2_105'], 'func': ti_replacement_d3_105}


def ti_replacement_d3_106(ti_replacement_d2_106):
    feature = _clean(ti_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_106'] = {'inputs': ['ti_replacement_d2_106'], 'func': ti_replacement_d3_106}


def ti_replacement_d3_107(ti_replacement_d2_107):
    feature = _clean(ti_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_107'] = {'inputs': ['ti_replacement_d2_107'], 'func': ti_replacement_d3_107}


def ti_replacement_d3_108(ti_replacement_d2_108):
    feature = _clean(ti_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_108'] = {'inputs': ['ti_replacement_d2_108'], 'func': ti_replacement_d3_108}


def ti_replacement_d3_109(ti_replacement_d2_109):
    feature = _clean(ti_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_109'] = {'inputs': ['ti_replacement_d2_109'], 'func': ti_replacement_d3_109}


def ti_replacement_d3_110(ti_replacement_d2_110):
    feature = _clean(ti_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_110'] = {'inputs': ['ti_replacement_d2_110'], 'func': ti_replacement_d3_110}


def ti_replacement_d3_111(ti_replacement_d2_111):
    feature = _clean(ti_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_111'] = {'inputs': ['ti_replacement_d2_111'], 'func': ti_replacement_d3_111}


def ti_replacement_d3_112(ti_replacement_d2_112):
    feature = _clean(ti_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_112'] = {'inputs': ['ti_replacement_d2_112'], 'func': ti_replacement_d3_112}


def ti_replacement_d3_113(ti_replacement_d2_113):
    feature = _clean(ti_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_113'] = {'inputs': ['ti_replacement_d2_113'], 'func': ti_replacement_d3_113}


def ti_replacement_d3_114(ti_replacement_d2_114):
    feature = _clean(ti_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_114'] = {'inputs': ['ti_replacement_d2_114'], 'func': ti_replacement_d3_114}


def ti_replacement_d3_115(ti_replacement_d2_115):
    feature = _clean(ti_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_115'] = {'inputs': ['ti_replacement_d2_115'], 'func': ti_replacement_d3_115}


def ti_replacement_d3_116(ti_replacement_d2_116):
    feature = _clean(ti_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_116'] = {'inputs': ['ti_replacement_d2_116'], 'func': ti_replacement_d3_116}


def ti_replacement_d3_117(ti_replacement_d2_117):
    feature = _clean(ti_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_117'] = {'inputs': ['ti_replacement_d2_117'], 'func': ti_replacement_d3_117}


def ti_replacement_d3_118(ti_replacement_d2_118):
    feature = _clean(ti_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_118'] = {'inputs': ['ti_replacement_d2_118'], 'func': ti_replacement_d3_118}


def ti_replacement_d3_119(ti_replacement_d2_119):
    feature = _clean(ti_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_119'] = {'inputs': ['ti_replacement_d2_119'], 'func': ti_replacement_d3_119}


def ti_replacement_d3_120(ti_replacement_d2_120):
    feature = _clean(ti_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_120'] = {'inputs': ['ti_replacement_d2_120'], 'func': ti_replacement_d3_120}


def ti_replacement_d3_121(ti_replacement_d2_121):
    feature = _clean(ti_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_121'] = {'inputs': ['ti_replacement_d2_121'], 'func': ti_replacement_d3_121}


def ti_replacement_d3_122(ti_replacement_d2_122):
    feature = _clean(ti_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_122'] = {'inputs': ['ti_replacement_d2_122'], 'func': ti_replacement_d3_122}


def ti_replacement_d3_123(ti_replacement_d2_123):
    feature = _clean(ti_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_123'] = {'inputs': ['ti_replacement_d2_123'], 'func': ti_replacement_d3_123}


def ti_replacement_d3_124(ti_replacement_d2_124):
    feature = _clean(ti_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_124'] = {'inputs': ['ti_replacement_d2_124'], 'func': ti_replacement_d3_124}


def ti_replacement_d3_125(ti_replacement_d2_125):
    feature = _clean(ti_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_125'] = {'inputs': ['ti_replacement_d2_125'], 'func': ti_replacement_d3_125}


def ti_replacement_d3_126(ti_replacement_d2_126):
    feature = _clean(ti_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_126'] = {'inputs': ['ti_replacement_d2_126'], 'func': ti_replacement_d3_126}


def ti_replacement_d3_127(ti_replacement_d2_127):
    feature = _clean(ti_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_127'] = {'inputs': ['ti_replacement_d2_127'], 'func': ti_replacement_d3_127}


def ti_replacement_d3_128(ti_replacement_d2_128):
    feature = _clean(ti_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_128'] = {'inputs': ['ti_replacement_d2_128'], 'func': ti_replacement_d3_128}


def ti_replacement_d3_129(ti_replacement_d2_129):
    feature = _clean(ti_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_129'] = {'inputs': ['ti_replacement_d2_129'], 'func': ti_replacement_d3_129}


def ti_replacement_d3_130(ti_replacement_d2_130):
    feature = _clean(ti_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_130'] = {'inputs': ['ti_replacement_d2_130'], 'func': ti_replacement_d3_130}


def ti_replacement_d3_131(ti_replacement_d2_131):
    feature = _clean(ti_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_131'] = {'inputs': ['ti_replacement_d2_131'], 'func': ti_replacement_d3_131}


def ti_replacement_d3_132(ti_replacement_d2_132):
    feature = _clean(ti_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_132'] = {'inputs': ['ti_replacement_d2_132'], 'func': ti_replacement_d3_132}


def ti_replacement_d3_133(ti_replacement_d2_133):
    feature = _clean(ti_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_133'] = {'inputs': ['ti_replacement_d2_133'], 'func': ti_replacement_d3_133}


def ti_replacement_d3_134(ti_replacement_d2_134):
    feature = _clean(ti_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_134'] = {'inputs': ['ti_replacement_d2_134'], 'func': ti_replacement_d3_134}


def ti_replacement_d3_135(ti_replacement_d2_135):
    feature = _clean(ti_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_135'] = {'inputs': ['ti_replacement_d2_135'], 'func': ti_replacement_d3_135}


def ti_replacement_d3_136(ti_replacement_d2_136):
    feature = _clean(ti_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_136'] = {'inputs': ['ti_replacement_d2_136'], 'func': ti_replacement_d3_136}


def ti_replacement_d3_137(ti_replacement_d2_137):
    feature = _clean(ti_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_137'] = {'inputs': ['ti_replacement_d2_137'], 'func': ti_replacement_d3_137}


def ti_replacement_d3_138(ti_replacement_d2_138):
    feature = _clean(ti_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_138'] = {'inputs': ['ti_replacement_d2_138'], 'func': ti_replacement_d3_138}


def ti_replacement_d3_139(ti_replacement_d2_139):
    feature = _clean(ti_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_139'] = {'inputs': ['ti_replacement_d2_139'], 'func': ti_replacement_d3_139}


def ti_replacement_d3_140(ti_replacement_d2_140):
    feature = _clean(ti_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_140'] = {'inputs': ['ti_replacement_d2_140'], 'func': ti_replacement_d3_140}


def ti_replacement_d3_141(ti_replacement_d2_141):
    feature = _clean(ti_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_141'] = {'inputs': ['ti_replacement_d2_141'], 'func': ti_replacement_d3_141}


def ti_replacement_d3_142(ti_replacement_d2_142):
    feature = _clean(ti_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_142'] = {'inputs': ['ti_replacement_d2_142'], 'func': ti_replacement_d3_142}


def ti_replacement_d3_143(ti_replacement_d2_143):
    feature = _clean(ti_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_143'] = {'inputs': ['ti_replacement_d2_143'], 'func': ti_replacement_d3_143}


def ti_replacement_d3_144(ti_replacement_d2_144):
    feature = _clean(ti_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_144'] = {'inputs': ['ti_replacement_d2_144'], 'func': ti_replacement_d3_144}


def ti_replacement_d3_145(ti_replacement_d2_145):
    feature = _clean(ti_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_145'] = {'inputs': ['ti_replacement_d2_145'], 'func': ti_replacement_d3_145}


def ti_replacement_d3_146(ti_replacement_d2_146):
    feature = _clean(ti_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_146'] = {'inputs': ['ti_replacement_d2_146'], 'func': ti_replacement_d3_146}


def ti_replacement_d3_147(ti_replacement_d2_147):
    feature = _clean(ti_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_147'] = {'inputs': ['ti_replacement_d2_147'], 'func': ti_replacement_d3_147}


def ti_replacement_d3_148(ti_replacement_d2_148):
    feature = _clean(ti_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_148'] = {'inputs': ['ti_replacement_d2_148'], 'func': ti_replacement_d3_148}


def ti_replacement_d3_149(ti_replacement_d2_149):
    feature = _clean(ti_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_149'] = {'inputs': ['ti_replacement_d2_149'], 'func': ti_replacement_d3_149}


def ti_replacement_d3_150(ti_replacement_d2_150):
    feature = _clean(ti_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_150'] = {'inputs': ['ti_replacement_d2_150'], 'func': ti_replacement_d3_150}


def ti_replacement_d3_151(ti_replacement_d2_151):
    feature = _clean(ti_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_151'] = {'inputs': ['ti_replacement_d2_151'], 'func': ti_replacement_d3_151}


def ti_replacement_d3_152(ti_replacement_d2_152):
    feature = _clean(ti_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_152'] = {'inputs': ['ti_replacement_d2_152'], 'func': ti_replacement_d3_152}


def ti_replacement_d3_153(ti_replacement_d2_153):
    feature = _clean(ti_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_153'] = {'inputs': ['ti_replacement_d2_153'], 'func': ti_replacement_d3_153}


def ti_replacement_d3_154(ti_replacement_d2_154):
    feature = _clean(ti_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_154'] = {'inputs': ['ti_replacement_d2_154'], 'func': ti_replacement_d3_154}


def ti_replacement_d3_155(ti_replacement_d2_155):
    feature = _clean(ti_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_155'] = {'inputs': ['ti_replacement_d2_155'], 'func': ti_replacement_d3_155}


def ti_replacement_d3_156(ti_replacement_d2_156):
    feature = _clean(ti_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_156'] = {'inputs': ['ti_replacement_d2_156'], 'func': ti_replacement_d3_156}


def ti_replacement_d3_157(ti_replacement_d2_157):
    feature = _clean(ti_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_157'] = {'inputs': ['ti_replacement_d2_157'], 'func': ti_replacement_d3_157}


def ti_replacement_d3_158(ti_replacement_d2_158):
    feature = _clean(ti_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_158'] = {'inputs': ['ti_replacement_d2_158'], 'func': ti_replacement_d3_158}


def ti_replacement_d3_159(ti_replacement_d2_159):
    feature = _clean(ti_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_159'] = {'inputs': ['ti_replacement_d2_159'], 'func': ti_replacement_d3_159}


def ti_replacement_d3_160(ti_replacement_d2_160):
    feature = _clean(ti_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_160'] = {'inputs': ['ti_replacement_d2_160'], 'func': ti_replacement_d3_160}


def ti_replacement_d3_161(ti_replacement_d2_161):
    feature = _clean(ti_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_161'] = {'inputs': ['ti_replacement_d2_161'], 'func': ti_replacement_d3_161}


def ti_replacement_d3_162(ti_replacement_d2_162):
    feature = _clean(ti_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_162'] = {'inputs': ['ti_replacement_d2_162'], 'func': ti_replacement_d3_162}


def ti_replacement_d3_163(ti_replacement_d2_163):
    feature = _clean(ti_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_163'] = {'inputs': ['ti_replacement_d2_163'], 'func': ti_replacement_d3_163}


def ti_replacement_d3_164(ti_replacement_d2_164):
    feature = _clean(ti_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_164'] = {'inputs': ['ti_replacement_d2_164'], 'func': ti_replacement_d3_164}


def ti_replacement_d3_165(ti_replacement_d2_165):
    feature = _clean(ti_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_165'] = {'inputs': ['ti_replacement_d2_165'], 'func': ti_replacement_d3_165}


def ti_replacement_d3_166(ti_replacement_d2_166):
    feature = _clean(ti_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_166'] = {'inputs': ['ti_replacement_d2_166'], 'func': ti_replacement_d3_166}


def ti_replacement_d3_167(ti_replacement_d2_167):
    feature = _clean(ti_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_167'] = {'inputs': ['ti_replacement_d2_167'], 'func': ti_replacement_d3_167}


def ti_replacement_d3_168(ti_replacement_d2_168):
    feature = _clean(ti_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_168'] = {'inputs': ['ti_replacement_d2_168'], 'func': ti_replacement_d3_168}


def ti_replacement_d3_169(ti_replacement_d2_169):
    feature = _clean(ti_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_169'] = {'inputs': ['ti_replacement_d2_169'], 'func': ti_replacement_d3_169}


def ti_replacement_d3_170(ti_replacement_d2_170):
    feature = _clean(ti_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
TI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ti_replacement_d3_170'] = {'inputs': ['ti_replacement_d2_170'], 'func': ti_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tin_base_universe_d3_001_tin_002_zero_volume_frequency_10_002(tin_base_universe_d2_001_tin_002_zero_volume_frequency_10_002):
    return _base_universe_d3(tin_base_universe_d2_001_tin_002_zero_volume_frequency_10_002, 1)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_001_tin_002_zero_volume_frequency_10_002'] = {'inputs': ['tin_base_universe_d2_001_tin_002_zero_volume_frequency_10_002'], 'func': tin_base_universe_d3_001_tin_002_zero_volume_frequency_10_002}


def tin_base_universe_d3_002_tin_003_spread_proxy_21_003(tin_base_universe_d2_002_tin_003_spread_proxy_21_003):
    return _base_universe_d3(tin_base_universe_d2_002_tin_003_spread_proxy_21_003, 2)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_002_tin_003_spread_proxy_21_003'] = {'inputs': ['tin_base_universe_d2_002_tin_003_spread_proxy_21_003'], 'func': tin_base_universe_d3_002_tin_003_spread_proxy_21_003}


def tin_base_universe_d3_003_tin_004_trading_intensity_42_004(tin_base_universe_d2_003_tin_004_trading_intensity_42_004):
    return _base_universe_d3(tin_base_universe_d2_003_tin_004_trading_intensity_42_004, 3)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_003_tin_004_trading_intensity_42_004'] = {'inputs': ['tin_base_universe_d2_003_tin_004_trading_intensity_42_004'], 'func': tin_base_universe_d3_003_tin_004_trading_intensity_42_004}


def tin_base_universe_d3_004_tin_006_price_level_distress_84_006(tin_base_universe_d2_004_tin_006_price_level_distress_84_006):
    return _base_universe_d3(tin_base_universe_d2_004_tin_006_price_level_distress_84_006, 4)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_004_tin_006_price_level_distress_84_006'] = {'inputs': ['tin_base_universe_d2_004_tin_006_price_level_distress_84_006'], 'func': tin_base_universe_d3_004_tin_006_price_level_distress_84_006}


def tin_base_universe_d3_005_tin_008_zero_volume_frequency_189_008(tin_base_universe_d2_005_tin_008_zero_volume_frequency_189_008):
    return _base_universe_d3(tin_base_universe_d2_005_tin_008_zero_volume_frequency_189_008, 5)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_005_tin_008_zero_volume_frequency_189_008'] = {'inputs': ['tin_base_universe_d2_005_tin_008_zero_volume_frequency_189_008'], 'func': tin_base_universe_d3_005_tin_008_zero_volume_frequency_189_008}


def tin_base_universe_d3_006_tin_009_spread_proxy_252_009(tin_base_universe_d2_006_tin_009_spread_proxy_252_009):
    return _base_universe_d3(tin_base_universe_d2_006_tin_009_spread_proxy_252_009, 6)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_006_tin_009_spread_proxy_252_009'] = {'inputs': ['tin_base_universe_d2_006_tin_009_spread_proxy_252_009'], 'func': tin_base_universe_d3_006_tin_009_spread_proxy_252_009}


def tin_base_universe_d3_007_tin_010_trading_intensity_378_010(tin_base_universe_d2_007_tin_010_trading_intensity_378_010):
    return _base_universe_d3(tin_base_universe_d2_007_tin_010_trading_intensity_378_010, 7)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_007_tin_010_trading_intensity_378_010'] = {'inputs': ['tin_base_universe_d2_007_tin_010_trading_intensity_378_010'], 'func': tin_base_universe_d3_007_tin_010_trading_intensity_378_010}


def tin_base_universe_d3_008_tin_012_price_level_distress_756_012(tin_base_universe_d2_008_tin_012_price_level_distress_756_012):
    return _base_universe_d3(tin_base_universe_d2_008_tin_012_price_level_distress_756_012, 8)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_008_tin_012_price_level_distress_756_012'] = {'inputs': ['tin_base_universe_d2_008_tin_012_price_level_distress_756_012'], 'func': tin_base_universe_d3_008_tin_012_price_level_distress_756_012}


def tin_base_universe_d3_009_tin_014_zero_volume_frequency_1260_014(tin_base_universe_d2_009_tin_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(tin_base_universe_d2_009_tin_014_zero_volume_frequency_1260_014, 9)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_009_tin_014_zero_volume_frequency_1260_014'] = {'inputs': ['tin_base_universe_d2_009_tin_014_zero_volume_frequency_1260_014'], 'func': tin_base_universe_d3_009_tin_014_zero_volume_frequency_1260_014}


def tin_base_universe_d3_010_tin_015_spread_proxy_1512_015(tin_base_universe_d2_010_tin_015_spread_proxy_1512_015):
    return _base_universe_d3(tin_base_universe_d2_010_tin_015_spread_proxy_1512_015, 10)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_010_tin_015_spread_proxy_1512_015'] = {'inputs': ['tin_base_universe_d2_010_tin_015_spread_proxy_1512_015'], 'func': tin_base_universe_d3_010_tin_015_spread_proxy_1512_015}


def tin_base_universe_d3_011_tin_016_trading_intensity_5_016(tin_base_universe_d2_011_tin_016_trading_intensity_5_016):
    return _base_universe_d3(tin_base_universe_d2_011_tin_016_trading_intensity_5_016, 11)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_011_tin_016_trading_intensity_5_016'] = {'inputs': ['tin_base_universe_d2_011_tin_016_trading_intensity_5_016'], 'func': tin_base_universe_d3_011_tin_016_trading_intensity_5_016}


def tin_base_universe_d3_012_tin_018_price_level_distress_21_018(tin_base_universe_d2_012_tin_018_price_level_distress_21_018):
    return _base_universe_d3(tin_base_universe_d2_012_tin_018_price_level_distress_21_018, 12)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_012_tin_018_price_level_distress_21_018'] = {'inputs': ['tin_base_universe_d2_012_tin_018_price_level_distress_21_018'], 'func': tin_base_universe_d3_012_tin_018_price_level_distress_21_018}


def tin_base_universe_d3_013_tin_020_zero_volume_frequency_63_020(tin_base_universe_d2_013_tin_020_zero_volume_frequency_63_020):
    return _base_universe_d3(tin_base_universe_d2_013_tin_020_zero_volume_frequency_63_020, 13)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_013_tin_020_zero_volume_frequency_63_020'] = {'inputs': ['tin_base_universe_d2_013_tin_020_zero_volume_frequency_63_020'], 'func': tin_base_universe_d3_013_tin_020_zero_volume_frequency_63_020}


def tin_base_universe_d3_014_tin_021_spread_proxy_84_021(tin_base_universe_d2_014_tin_021_spread_proxy_84_021):
    return _base_universe_d3(tin_base_universe_d2_014_tin_021_spread_proxy_84_021, 14)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_014_tin_021_spread_proxy_84_021'] = {'inputs': ['tin_base_universe_d2_014_tin_021_spread_proxy_84_021'], 'func': tin_base_universe_d3_014_tin_021_spread_proxy_84_021}


def tin_base_universe_d3_015_tin_022_trading_intensity_126_022(tin_base_universe_d2_015_tin_022_trading_intensity_126_022):
    return _base_universe_d3(tin_base_universe_d2_015_tin_022_trading_intensity_126_022, 15)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_015_tin_022_trading_intensity_126_022'] = {'inputs': ['tin_base_universe_d2_015_tin_022_trading_intensity_126_022'], 'func': tin_base_universe_d3_015_tin_022_trading_intensity_126_022}


def tin_base_universe_d3_016_tin_024_price_level_distress_252_024(tin_base_universe_d2_016_tin_024_price_level_distress_252_024):
    return _base_universe_d3(tin_base_universe_d2_016_tin_024_price_level_distress_252_024, 16)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_016_tin_024_price_level_distress_252_024'] = {'inputs': ['tin_base_universe_d2_016_tin_024_price_level_distress_252_024'], 'func': tin_base_universe_d3_016_tin_024_price_level_distress_252_024}


def tin_base_universe_d3_017_tin_026_zero_volume_frequency_504_026(tin_base_universe_d2_017_tin_026_zero_volume_frequency_504_026):
    return _base_universe_d3(tin_base_universe_d2_017_tin_026_zero_volume_frequency_504_026, 17)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_017_tin_026_zero_volume_frequency_504_026'] = {'inputs': ['tin_base_universe_d2_017_tin_026_zero_volume_frequency_504_026'], 'func': tin_base_universe_d3_017_tin_026_zero_volume_frequency_504_026}


def tin_base_universe_d3_018_tin_027_spread_proxy_756_027(tin_base_universe_d2_018_tin_027_spread_proxy_756_027):
    return _base_universe_d3(tin_base_universe_d2_018_tin_027_spread_proxy_756_027, 18)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_018_tin_027_spread_proxy_756_027'] = {'inputs': ['tin_base_universe_d2_018_tin_027_spread_proxy_756_027'], 'func': tin_base_universe_d3_018_tin_027_spread_proxy_756_027}


def tin_base_universe_d3_019_tin_028_trading_intensity_1008_028(tin_base_universe_d2_019_tin_028_trading_intensity_1008_028):
    return _base_universe_d3(tin_base_universe_d2_019_tin_028_trading_intensity_1008_028, 19)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_019_tin_028_trading_intensity_1008_028'] = {'inputs': ['tin_base_universe_d2_019_tin_028_trading_intensity_1008_028'], 'func': tin_base_universe_d3_019_tin_028_trading_intensity_1008_028}


def tin_base_universe_d3_020_tin_030_price_level_distress_1512_030(tin_base_universe_d2_020_tin_030_price_level_distress_1512_030):
    return _base_universe_d3(tin_base_universe_d2_020_tin_030_price_level_distress_1512_030, 20)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_020_tin_030_price_level_distress_1512_030'] = {'inputs': ['tin_base_universe_d2_020_tin_030_price_level_distress_1512_030'], 'func': tin_base_universe_d3_020_tin_030_price_level_distress_1512_030}


def tin_base_universe_d3_021_tin_basefill_001(tin_base_universe_d2_021_tin_basefill_001):
    return _base_universe_d3(tin_base_universe_d2_021_tin_basefill_001, 21)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_021_tin_basefill_001'] = {'inputs': ['tin_base_universe_d2_021_tin_basefill_001'], 'func': tin_base_universe_d3_021_tin_basefill_001}


def tin_base_universe_d3_022_tin_basefill_005(tin_base_universe_d2_022_tin_basefill_005):
    return _base_universe_d3(tin_base_universe_d2_022_tin_basefill_005, 22)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_022_tin_basefill_005'] = {'inputs': ['tin_base_universe_d2_022_tin_basefill_005'], 'func': tin_base_universe_d3_022_tin_basefill_005}


def tin_base_universe_d3_023_tin_basefill_007(tin_base_universe_d2_023_tin_basefill_007):
    return _base_universe_d3(tin_base_universe_d2_023_tin_basefill_007, 23)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_023_tin_basefill_007'] = {'inputs': ['tin_base_universe_d2_023_tin_basefill_007'], 'func': tin_base_universe_d3_023_tin_basefill_007}


def tin_base_universe_d3_024_tin_basefill_011(tin_base_universe_d2_024_tin_basefill_011):
    return _base_universe_d3(tin_base_universe_d2_024_tin_basefill_011, 24)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_024_tin_basefill_011'] = {'inputs': ['tin_base_universe_d2_024_tin_basefill_011'], 'func': tin_base_universe_d3_024_tin_basefill_011}


def tin_base_universe_d3_025_tin_basefill_013(tin_base_universe_d2_025_tin_basefill_013):
    return _base_universe_d3(tin_base_universe_d2_025_tin_basefill_013, 25)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_025_tin_basefill_013'] = {'inputs': ['tin_base_universe_d2_025_tin_basefill_013'], 'func': tin_base_universe_d3_025_tin_basefill_013}


def tin_base_universe_d3_026_tin_basefill_017(tin_base_universe_d2_026_tin_basefill_017):
    return _base_universe_d3(tin_base_universe_d2_026_tin_basefill_017, 26)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_026_tin_basefill_017'] = {'inputs': ['tin_base_universe_d2_026_tin_basefill_017'], 'func': tin_base_universe_d3_026_tin_basefill_017}


def tin_base_universe_d3_027_tin_basefill_019(tin_base_universe_d2_027_tin_basefill_019):
    return _base_universe_d3(tin_base_universe_d2_027_tin_basefill_019, 27)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_027_tin_basefill_019'] = {'inputs': ['tin_base_universe_d2_027_tin_basefill_019'], 'func': tin_base_universe_d3_027_tin_basefill_019}


def tin_base_universe_d3_028_tin_basefill_023(tin_base_universe_d2_028_tin_basefill_023):
    return _base_universe_d3(tin_base_universe_d2_028_tin_basefill_023, 28)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_028_tin_basefill_023'] = {'inputs': ['tin_base_universe_d2_028_tin_basefill_023'], 'func': tin_base_universe_d3_028_tin_basefill_023}


def tin_base_universe_d3_029_tin_basefill_025(tin_base_universe_d2_029_tin_basefill_025):
    return _base_universe_d3(tin_base_universe_d2_029_tin_basefill_025, 29)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_029_tin_basefill_025'] = {'inputs': ['tin_base_universe_d2_029_tin_basefill_025'], 'func': tin_base_universe_d3_029_tin_basefill_025}


def tin_base_universe_d3_030_tin_basefill_029(tin_base_universe_d2_030_tin_basefill_029):
    return _base_universe_d3(tin_base_universe_d2_030_tin_basefill_029, 30)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_030_tin_basefill_029'] = {'inputs': ['tin_base_universe_d2_030_tin_basefill_029'], 'func': tin_base_universe_d3_030_tin_basefill_029}


def tin_base_universe_d3_031_tin_basefill_031(tin_base_universe_d2_031_tin_basefill_031):
    return _base_universe_d3(tin_base_universe_d2_031_tin_basefill_031, 31)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_031_tin_basefill_031'] = {'inputs': ['tin_base_universe_d2_031_tin_basefill_031'], 'func': tin_base_universe_d3_031_tin_basefill_031}


def tin_base_universe_d3_032_tin_basefill_032(tin_base_universe_d2_032_tin_basefill_032):
    return _base_universe_d3(tin_base_universe_d2_032_tin_basefill_032, 32)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_032_tin_basefill_032'] = {'inputs': ['tin_base_universe_d2_032_tin_basefill_032'], 'func': tin_base_universe_d3_032_tin_basefill_032}


def tin_base_universe_d3_033_tin_basefill_033(tin_base_universe_d2_033_tin_basefill_033):
    return _base_universe_d3(tin_base_universe_d2_033_tin_basefill_033, 33)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_033_tin_basefill_033'] = {'inputs': ['tin_base_universe_d2_033_tin_basefill_033'], 'func': tin_base_universe_d3_033_tin_basefill_033}


def tin_base_universe_d3_034_tin_basefill_034(tin_base_universe_d2_034_tin_basefill_034):
    return _base_universe_d3(tin_base_universe_d2_034_tin_basefill_034, 34)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_034_tin_basefill_034'] = {'inputs': ['tin_base_universe_d2_034_tin_basefill_034'], 'func': tin_base_universe_d3_034_tin_basefill_034}


def tin_base_universe_d3_035_tin_basefill_035(tin_base_universe_d2_035_tin_basefill_035):
    return _base_universe_d3(tin_base_universe_d2_035_tin_basefill_035, 35)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_035_tin_basefill_035'] = {'inputs': ['tin_base_universe_d2_035_tin_basefill_035'], 'func': tin_base_universe_d3_035_tin_basefill_035}


def tin_base_universe_d3_036_tin_basefill_036(tin_base_universe_d2_036_tin_basefill_036):
    return _base_universe_d3(tin_base_universe_d2_036_tin_basefill_036, 36)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_036_tin_basefill_036'] = {'inputs': ['tin_base_universe_d2_036_tin_basefill_036'], 'func': tin_base_universe_d3_036_tin_basefill_036}


def tin_base_universe_d3_037_tin_basefill_037(tin_base_universe_d2_037_tin_basefill_037):
    return _base_universe_d3(tin_base_universe_d2_037_tin_basefill_037, 37)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_037_tin_basefill_037'] = {'inputs': ['tin_base_universe_d2_037_tin_basefill_037'], 'func': tin_base_universe_d3_037_tin_basefill_037}


def tin_base_universe_d3_038_tin_basefill_038(tin_base_universe_d2_038_tin_basefill_038):
    return _base_universe_d3(tin_base_universe_d2_038_tin_basefill_038, 38)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_038_tin_basefill_038'] = {'inputs': ['tin_base_universe_d2_038_tin_basefill_038'], 'func': tin_base_universe_d3_038_tin_basefill_038}


def tin_base_universe_d3_039_tin_basefill_039(tin_base_universe_d2_039_tin_basefill_039):
    return _base_universe_d3(tin_base_universe_d2_039_tin_basefill_039, 39)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_039_tin_basefill_039'] = {'inputs': ['tin_base_universe_d2_039_tin_basefill_039'], 'func': tin_base_universe_d3_039_tin_basefill_039}


def tin_base_universe_d3_040_tin_basefill_040(tin_base_universe_d2_040_tin_basefill_040):
    return _base_universe_d3(tin_base_universe_d2_040_tin_basefill_040, 40)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_040_tin_basefill_040'] = {'inputs': ['tin_base_universe_d2_040_tin_basefill_040'], 'func': tin_base_universe_d3_040_tin_basefill_040}


def tin_base_universe_d3_041_tin_basefill_041(tin_base_universe_d2_041_tin_basefill_041):
    return _base_universe_d3(tin_base_universe_d2_041_tin_basefill_041, 41)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_041_tin_basefill_041'] = {'inputs': ['tin_base_universe_d2_041_tin_basefill_041'], 'func': tin_base_universe_d3_041_tin_basefill_041}


def tin_base_universe_d3_042_tin_basefill_042(tin_base_universe_d2_042_tin_basefill_042):
    return _base_universe_d3(tin_base_universe_d2_042_tin_basefill_042, 42)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_042_tin_basefill_042'] = {'inputs': ['tin_base_universe_d2_042_tin_basefill_042'], 'func': tin_base_universe_d3_042_tin_basefill_042}


def tin_base_universe_d3_043_tin_basefill_043(tin_base_universe_d2_043_tin_basefill_043):
    return _base_universe_d3(tin_base_universe_d2_043_tin_basefill_043, 43)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_043_tin_basefill_043'] = {'inputs': ['tin_base_universe_d2_043_tin_basefill_043'], 'func': tin_base_universe_d3_043_tin_basefill_043}


def tin_base_universe_d3_044_tin_basefill_044(tin_base_universe_d2_044_tin_basefill_044):
    return _base_universe_d3(tin_base_universe_d2_044_tin_basefill_044, 44)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_044_tin_basefill_044'] = {'inputs': ['tin_base_universe_d2_044_tin_basefill_044'], 'func': tin_base_universe_d3_044_tin_basefill_044}


def tin_base_universe_d3_045_tin_basefill_045(tin_base_universe_d2_045_tin_basefill_045):
    return _base_universe_d3(tin_base_universe_d2_045_tin_basefill_045, 45)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_045_tin_basefill_045'] = {'inputs': ['tin_base_universe_d2_045_tin_basefill_045'], 'func': tin_base_universe_d3_045_tin_basefill_045}


def tin_base_universe_d3_046_tin_basefill_046(tin_base_universe_d2_046_tin_basefill_046):
    return _base_universe_d3(tin_base_universe_d2_046_tin_basefill_046, 46)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_046_tin_basefill_046'] = {'inputs': ['tin_base_universe_d2_046_tin_basefill_046'], 'func': tin_base_universe_d3_046_tin_basefill_046}


def tin_base_universe_d3_047_tin_basefill_047(tin_base_universe_d2_047_tin_basefill_047):
    return _base_universe_d3(tin_base_universe_d2_047_tin_basefill_047, 47)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_047_tin_basefill_047'] = {'inputs': ['tin_base_universe_d2_047_tin_basefill_047'], 'func': tin_base_universe_d3_047_tin_basefill_047}


def tin_base_universe_d3_048_tin_basefill_048(tin_base_universe_d2_048_tin_basefill_048):
    return _base_universe_d3(tin_base_universe_d2_048_tin_basefill_048, 48)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_048_tin_basefill_048'] = {'inputs': ['tin_base_universe_d2_048_tin_basefill_048'], 'func': tin_base_universe_d3_048_tin_basefill_048}


def tin_base_universe_d3_049_tin_basefill_049(tin_base_universe_d2_049_tin_basefill_049):
    return _base_universe_d3(tin_base_universe_d2_049_tin_basefill_049, 49)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_049_tin_basefill_049'] = {'inputs': ['tin_base_universe_d2_049_tin_basefill_049'], 'func': tin_base_universe_d3_049_tin_basefill_049}


def tin_base_universe_d3_050_tin_basefill_050(tin_base_universe_d2_050_tin_basefill_050):
    return _base_universe_d3(tin_base_universe_d2_050_tin_basefill_050, 50)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_050_tin_basefill_050'] = {'inputs': ['tin_base_universe_d2_050_tin_basefill_050'], 'func': tin_base_universe_d3_050_tin_basefill_050}


def tin_base_universe_d3_051_tin_basefill_051(tin_base_universe_d2_051_tin_basefill_051):
    return _base_universe_d3(tin_base_universe_d2_051_tin_basefill_051, 51)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_051_tin_basefill_051'] = {'inputs': ['tin_base_universe_d2_051_tin_basefill_051'], 'func': tin_base_universe_d3_051_tin_basefill_051}


def tin_base_universe_d3_052_tin_basefill_052(tin_base_universe_d2_052_tin_basefill_052):
    return _base_universe_d3(tin_base_universe_d2_052_tin_basefill_052, 52)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_052_tin_basefill_052'] = {'inputs': ['tin_base_universe_d2_052_tin_basefill_052'], 'func': tin_base_universe_d3_052_tin_basefill_052}


def tin_base_universe_d3_053_tin_basefill_053(tin_base_universe_d2_053_tin_basefill_053):
    return _base_universe_d3(tin_base_universe_d2_053_tin_basefill_053, 53)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_053_tin_basefill_053'] = {'inputs': ['tin_base_universe_d2_053_tin_basefill_053'], 'func': tin_base_universe_d3_053_tin_basefill_053}


def tin_base_universe_d3_054_tin_basefill_054(tin_base_universe_d2_054_tin_basefill_054):
    return _base_universe_d3(tin_base_universe_d2_054_tin_basefill_054, 54)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_054_tin_basefill_054'] = {'inputs': ['tin_base_universe_d2_054_tin_basefill_054'], 'func': tin_base_universe_d3_054_tin_basefill_054}


def tin_base_universe_d3_055_tin_basefill_055(tin_base_universe_d2_055_tin_basefill_055):
    return _base_universe_d3(tin_base_universe_d2_055_tin_basefill_055, 55)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_055_tin_basefill_055'] = {'inputs': ['tin_base_universe_d2_055_tin_basefill_055'], 'func': tin_base_universe_d3_055_tin_basefill_055}


def tin_base_universe_d3_056_tin_basefill_056(tin_base_universe_d2_056_tin_basefill_056):
    return _base_universe_d3(tin_base_universe_d2_056_tin_basefill_056, 56)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_056_tin_basefill_056'] = {'inputs': ['tin_base_universe_d2_056_tin_basefill_056'], 'func': tin_base_universe_d3_056_tin_basefill_056}


def tin_base_universe_d3_057_tin_basefill_057(tin_base_universe_d2_057_tin_basefill_057):
    return _base_universe_d3(tin_base_universe_d2_057_tin_basefill_057, 57)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_057_tin_basefill_057'] = {'inputs': ['tin_base_universe_d2_057_tin_basefill_057'], 'func': tin_base_universe_d3_057_tin_basefill_057}


def tin_base_universe_d3_058_tin_basefill_058(tin_base_universe_d2_058_tin_basefill_058):
    return _base_universe_d3(tin_base_universe_d2_058_tin_basefill_058, 58)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_058_tin_basefill_058'] = {'inputs': ['tin_base_universe_d2_058_tin_basefill_058'], 'func': tin_base_universe_d3_058_tin_basefill_058}


def tin_base_universe_d3_059_tin_basefill_059(tin_base_universe_d2_059_tin_basefill_059):
    return _base_universe_d3(tin_base_universe_d2_059_tin_basefill_059, 59)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_059_tin_basefill_059'] = {'inputs': ['tin_base_universe_d2_059_tin_basefill_059'], 'func': tin_base_universe_d3_059_tin_basefill_059}


def tin_base_universe_d3_060_tin_basefill_060(tin_base_universe_d2_060_tin_basefill_060):
    return _base_universe_d3(tin_base_universe_d2_060_tin_basefill_060, 60)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_060_tin_basefill_060'] = {'inputs': ['tin_base_universe_d2_060_tin_basefill_060'], 'func': tin_base_universe_d3_060_tin_basefill_060}


def tin_base_universe_d3_061_tin_basefill_061(tin_base_universe_d2_061_tin_basefill_061):
    return _base_universe_d3(tin_base_universe_d2_061_tin_basefill_061, 61)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_061_tin_basefill_061'] = {'inputs': ['tin_base_universe_d2_061_tin_basefill_061'], 'func': tin_base_universe_d3_061_tin_basefill_061}


def tin_base_universe_d3_062_tin_basefill_062(tin_base_universe_d2_062_tin_basefill_062):
    return _base_universe_d3(tin_base_universe_d2_062_tin_basefill_062, 62)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_062_tin_basefill_062'] = {'inputs': ['tin_base_universe_d2_062_tin_basefill_062'], 'func': tin_base_universe_d3_062_tin_basefill_062}


def tin_base_universe_d3_063_tin_basefill_063(tin_base_universe_d2_063_tin_basefill_063):
    return _base_universe_d3(tin_base_universe_d2_063_tin_basefill_063, 63)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_063_tin_basefill_063'] = {'inputs': ['tin_base_universe_d2_063_tin_basefill_063'], 'func': tin_base_universe_d3_063_tin_basefill_063}


def tin_base_universe_d3_064_tin_basefill_064(tin_base_universe_d2_064_tin_basefill_064):
    return _base_universe_d3(tin_base_universe_d2_064_tin_basefill_064, 64)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_064_tin_basefill_064'] = {'inputs': ['tin_base_universe_d2_064_tin_basefill_064'], 'func': tin_base_universe_d3_064_tin_basefill_064}


def tin_base_universe_d3_065_tin_basefill_065(tin_base_universe_d2_065_tin_basefill_065):
    return _base_universe_d3(tin_base_universe_d2_065_tin_basefill_065, 65)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_065_tin_basefill_065'] = {'inputs': ['tin_base_universe_d2_065_tin_basefill_065'], 'func': tin_base_universe_d3_065_tin_basefill_065}


def tin_base_universe_d3_066_tin_basefill_066(tin_base_universe_d2_066_tin_basefill_066):
    return _base_universe_d3(tin_base_universe_d2_066_tin_basefill_066, 66)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_066_tin_basefill_066'] = {'inputs': ['tin_base_universe_d2_066_tin_basefill_066'], 'func': tin_base_universe_d3_066_tin_basefill_066}


def tin_base_universe_d3_067_tin_basefill_067(tin_base_universe_d2_067_tin_basefill_067):
    return _base_universe_d3(tin_base_universe_d2_067_tin_basefill_067, 67)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_067_tin_basefill_067'] = {'inputs': ['tin_base_universe_d2_067_tin_basefill_067'], 'func': tin_base_universe_d3_067_tin_basefill_067}


def tin_base_universe_d3_068_tin_basefill_068(tin_base_universe_d2_068_tin_basefill_068):
    return _base_universe_d3(tin_base_universe_d2_068_tin_basefill_068, 68)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_068_tin_basefill_068'] = {'inputs': ['tin_base_universe_d2_068_tin_basefill_068'], 'func': tin_base_universe_d3_068_tin_basefill_068}


def tin_base_universe_d3_069_tin_basefill_069(tin_base_universe_d2_069_tin_basefill_069):
    return _base_universe_d3(tin_base_universe_d2_069_tin_basefill_069, 69)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_069_tin_basefill_069'] = {'inputs': ['tin_base_universe_d2_069_tin_basefill_069'], 'func': tin_base_universe_d3_069_tin_basefill_069}


def tin_base_universe_d3_070_tin_basefill_070(tin_base_universe_d2_070_tin_basefill_070):
    return _base_universe_d3(tin_base_universe_d2_070_tin_basefill_070, 70)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_070_tin_basefill_070'] = {'inputs': ['tin_base_universe_d2_070_tin_basefill_070'], 'func': tin_base_universe_d3_070_tin_basefill_070}


def tin_base_universe_d3_071_tin_basefill_071(tin_base_universe_d2_071_tin_basefill_071):
    return _base_universe_d3(tin_base_universe_d2_071_tin_basefill_071, 71)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_071_tin_basefill_071'] = {'inputs': ['tin_base_universe_d2_071_tin_basefill_071'], 'func': tin_base_universe_d3_071_tin_basefill_071}


def tin_base_universe_d3_072_tin_basefill_072(tin_base_universe_d2_072_tin_basefill_072):
    return _base_universe_d3(tin_base_universe_d2_072_tin_basefill_072, 72)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_072_tin_basefill_072'] = {'inputs': ['tin_base_universe_d2_072_tin_basefill_072'], 'func': tin_base_universe_d3_072_tin_basefill_072}


def tin_base_universe_d3_073_tin_basefill_073(tin_base_universe_d2_073_tin_basefill_073):
    return _base_universe_d3(tin_base_universe_d2_073_tin_basefill_073, 73)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_073_tin_basefill_073'] = {'inputs': ['tin_base_universe_d2_073_tin_basefill_073'], 'func': tin_base_universe_d3_073_tin_basefill_073}


def tin_base_universe_d3_074_tin_basefill_074(tin_base_universe_d2_074_tin_basefill_074):
    return _base_universe_d3(tin_base_universe_d2_074_tin_basefill_074, 74)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_074_tin_basefill_074'] = {'inputs': ['tin_base_universe_d2_074_tin_basefill_074'], 'func': tin_base_universe_d3_074_tin_basefill_074}


def tin_base_universe_d3_075_tin_basefill_075(tin_base_universe_d2_075_tin_basefill_075):
    return _base_universe_d3(tin_base_universe_d2_075_tin_basefill_075, 75)
TIN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tin_base_universe_d3_075_tin_basefill_075'] = {'inputs': ['tin_base_universe_d2_075_tin_basefill_075'], 'func': tin_base_universe_d3_075_tin_basefill_075}
