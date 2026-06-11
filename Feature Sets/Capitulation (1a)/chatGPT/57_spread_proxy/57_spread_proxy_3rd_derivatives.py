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



def spr_001_amihud_illiquidity_accel_1(spr_001_amihud_illiquidity_roc_1):
    feature = _s(spr_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def spr_007_amihud_illiquidity_accel_5(spr_007_amihud_illiquidity_roc_5):
    feature = _s(spr_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def spr_013_amihud_illiquidity_accel_42(spr_013_amihud_illiquidity_roc_42):
    feature = _s(spr_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def spr_179_spr_019_amihud_illiquidity_42_019_accel_126(spr_154_spr_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(spr_154_spr_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def spr_180_spr_025_amihud_illiquidity_378_025_accel_378(spr_155_spr_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(spr_155_spr_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















SPREAD_PROXY_REGISTRY_3RD_DERIVATIVES = {
    'spr_001_amihud_illiquidity_accel_1': {'inputs': ['spr_001_amihud_illiquidity_roc_1'], 'func': spr_001_amihud_illiquidity_accel_1},
    'spr_007_amihud_illiquidity_accel_5': {'inputs': ['spr_007_amihud_illiquidity_roc_5'], 'func': spr_007_amihud_illiquidity_accel_5},
    'spr_013_amihud_illiquidity_accel_42': {'inputs': ['spr_013_amihud_illiquidity_roc_42'], 'func': spr_013_amihud_illiquidity_accel_42},
    'spr_179_spr_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['spr_154_spr_019_amihud_illiquidity_42_019_roc_126'], 'func': spr_179_spr_019_amihud_illiquidity_42_019_accel_126},
    'spr_180_spr_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['spr_155_spr_025_amihud_illiquidity_378_025_roc_378'], 'func': spr_180_spr_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def sp_replacement_d3_001(sp_replacement_d2_001):
    feature = _clean(sp_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_001'] = {'inputs': ['sp_replacement_d2_001'], 'func': sp_replacement_d3_001}


def sp_replacement_d3_002(sp_replacement_d2_002):
    feature = _clean(sp_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_002'] = {'inputs': ['sp_replacement_d2_002'], 'func': sp_replacement_d3_002}


def sp_replacement_d3_003(sp_replacement_d2_003):
    feature = _clean(sp_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_003'] = {'inputs': ['sp_replacement_d2_003'], 'func': sp_replacement_d3_003}


def sp_replacement_d3_004(sp_replacement_d2_004):
    feature = _clean(sp_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_004'] = {'inputs': ['sp_replacement_d2_004'], 'func': sp_replacement_d3_004}


def sp_replacement_d3_005(sp_replacement_d2_005):
    feature = _clean(sp_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_005'] = {'inputs': ['sp_replacement_d2_005'], 'func': sp_replacement_d3_005}


def sp_replacement_d3_006(sp_replacement_d2_006):
    feature = _clean(sp_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_006'] = {'inputs': ['sp_replacement_d2_006'], 'func': sp_replacement_d3_006}


def sp_replacement_d3_007(sp_replacement_d2_007):
    feature = _clean(sp_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_007'] = {'inputs': ['sp_replacement_d2_007'], 'func': sp_replacement_d3_007}


def sp_replacement_d3_008(sp_replacement_d2_008):
    feature = _clean(sp_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_008'] = {'inputs': ['sp_replacement_d2_008'], 'func': sp_replacement_d3_008}


def sp_replacement_d3_009(sp_replacement_d2_009):
    feature = _clean(sp_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_009'] = {'inputs': ['sp_replacement_d2_009'], 'func': sp_replacement_d3_009}


def sp_replacement_d3_010(sp_replacement_d2_010):
    feature = _clean(sp_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_010'] = {'inputs': ['sp_replacement_d2_010'], 'func': sp_replacement_d3_010}


def sp_replacement_d3_011(sp_replacement_d2_011):
    feature = _clean(sp_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_011'] = {'inputs': ['sp_replacement_d2_011'], 'func': sp_replacement_d3_011}


def sp_replacement_d3_012(sp_replacement_d2_012):
    feature = _clean(sp_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_012'] = {'inputs': ['sp_replacement_d2_012'], 'func': sp_replacement_d3_012}


def sp_replacement_d3_013(sp_replacement_d2_013):
    feature = _clean(sp_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_013'] = {'inputs': ['sp_replacement_d2_013'], 'func': sp_replacement_d3_013}


def sp_replacement_d3_014(sp_replacement_d2_014):
    feature = _clean(sp_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_014'] = {'inputs': ['sp_replacement_d2_014'], 'func': sp_replacement_d3_014}


def sp_replacement_d3_015(sp_replacement_d2_015):
    feature = _clean(sp_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_015'] = {'inputs': ['sp_replacement_d2_015'], 'func': sp_replacement_d3_015}


def sp_replacement_d3_016(sp_replacement_d2_016):
    feature = _clean(sp_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_016'] = {'inputs': ['sp_replacement_d2_016'], 'func': sp_replacement_d3_016}


def sp_replacement_d3_017(sp_replacement_d2_017):
    feature = _clean(sp_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_017'] = {'inputs': ['sp_replacement_d2_017'], 'func': sp_replacement_d3_017}


def sp_replacement_d3_018(sp_replacement_d2_018):
    feature = _clean(sp_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_018'] = {'inputs': ['sp_replacement_d2_018'], 'func': sp_replacement_d3_018}


def sp_replacement_d3_019(sp_replacement_d2_019):
    feature = _clean(sp_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_019'] = {'inputs': ['sp_replacement_d2_019'], 'func': sp_replacement_d3_019}


def sp_replacement_d3_020(sp_replacement_d2_020):
    feature = _clean(sp_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_020'] = {'inputs': ['sp_replacement_d2_020'], 'func': sp_replacement_d3_020}


def sp_replacement_d3_021(sp_replacement_d2_021):
    feature = _clean(sp_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_021'] = {'inputs': ['sp_replacement_d2_021'], 'func': sp_replacement_d3_021}


def sp_replacement_d3_022(sp_replacement_d2_022):
    feature = _clean(sp_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_022'] = {'inputs': ['sp_replacement_d2_022'], 'func': sp_replacement_d3_022}


def sp_replacement_d3_023(sp_replacement_d2_023):
    feature = _clean(sp_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_023'] = {'inputs': ['sp_replacement_d2_023'], 'func': sp_replacement_d3_023}


def sp_replacement_d3_024(sp_replacement_d2_024):
    feature = _clean(sp_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_024'] = {'inputs': ['sp_replacement_d2_024'], 'func': sp_replacement_d3_024}


def sp_replacement_d3_025(sp_replacement_d2_025):
    feature = _clean(sp_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_025'] = {'inputs': ['sp_replacement_d2_025'], 'func': sp_replacement_d3_025}


def sp_replacement_d3_026(sp_replacement_d2_026):
    feature = _clean(sp_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_026'] = {'inputs': ['sp_replacement_d2_026'], 'func': sp_replacement_d3_026}


def sp_replacement_d3_027(sp_replacement_d2_027):
    feature = _clean(sp_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_027'] = {'inputs': ['sp_replacement_d2_027'], 'func': sp_replacement_d3_027}


def sp_replacement_d3_028(sp_replacement_d2_028):
    feature = _clean(sp_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_028'] = {'inputs': ['sp_replacement_d2_028'], 'func': sp_replacement_d3_028}


def sp_replacement_d3_029(sp_replacement_d2_029):
    feature = _clean(sp_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_029'] = {'inputs': ['sp_replacement_d2_029'], 'func': sp_replacement_d3_029}


def sp_replacement_d3_030(sp_replacement_d2_030):
    feature = _clean(sp_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_030'] = {'inputs': ['sp_replacement_d2_030'], 'func': sp_replacement_d3_030}


def sp_replacement_d3_031(sp_replacement_d2_031):
    feature = _clean(sp_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_031'] = {'inputs': ['sp_replacement_d2_031'], 'func': sp_replacement_d3_031}


def sp_replacement_d3_032(sp_replacement_d2_032):
    feature = _clean(sp_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_032'] = {'inputs': ['sp_replacement_d2_032'], 'func': sp_replacement_d3_032}


def sp_replacement_d3_033(sp_replacement_d2_033):
    feature = _clean(sp_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_033'] = {'inputs': ['sp_replacement_d2_033'], 'func': sp_replacement_d3_033}


def sp_replacement_d3_034(sp_replacement_d2_034):
    feature = _clean(sp_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_034'] = {'inputs': ['sp_replacement_d2_034'], 'func': sp_replacement_d3_034}


def sp_replacement_d3_035(sp_replacement_d2_035):
    feature = _clean(sp_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_035'] = {'inputs': ['sp_replacement_d2_035'], 'func': sp_replacement_d3_035}


def sp_replacement_d3_036(sp_replacement_d2_036):
    feature = _clean(sp_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_036'] = {'inputs': ['sp_replacement_d2_036'], 'func': sp_replacement_d3_036}


def sp_replacement_d3_037(sp_replacement_d2_037):
    feature = _clean(sp_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_037'] = {'inputs': ['sp_replacement_d2_037'], 'func': sp_replacement_d3_037}


def sp_replacement_d3_038(sp_replacement_d2_038):
    feature = _clean(sp_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_038'] = {'inputs': ['sp_replacement_d2_038'], 'func': sp_replacement_d3_038}


def sp_replacement_d3_039(sp_replacement_d2_039):
    feature = _clean(sp_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_039'] = {'inputs': ['sp_replacement_d2_039'], 'func': sp_replacement_d3_039}


def sp_replacement_d3_040(sp_replacement_d2_040):
    feature = _clean(sp_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_040'] = {'inputs': ['sp_replacement_d2_040'], 'func': sp_replacement_d3_040}


def sp_replacement_d3_041(sp_replacement_d2_041):
    feature = _clean(sp_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_041'] = {'inputs': ['sp_replacement_d2_041'], 'func': sp_replacement_d3_041}


def sp_replacement_d3_042(sp_replacement_d2_042):
    feature = _clean(sp_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_042'] = {'inputs': ['sp_replacement_d2_042'], 'func': sp_replacement_d3_042}


def sp_replacement_d3_043(sp_replacement_d2_043):
    feature = _clean(sp_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_043'] = {'inputs': ['sp_replacement_d2_043'], 'func': sp_replacement_d3_043}


def sp_replacement_d3_044(sp_replacement_d2_044):
    feature = _clean(sp_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_044'] = {'inputs': ['sp_replacement_d2_044'], 'func': sp_replacement_d3_044}


def sp_replacement_d3_045(sp_replacement_d2_045):
    feature = _clean(sp_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_045'] = {'inputs': ['sp_replacement_d2_045'], 'func': sp_replacement_d3_045}


def sp_replacement_d3_046(sp_replacement_d2_046):
    feature = _clean(sp_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_046'] = {'inputs': ['sp_replacement_d2_046'], 'func': sp_replacement_d3_046}


def sp_replacement_d3_047(sp_replacement_d2_047):
    feature = _clean(sp_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_047'] = {'inputs': ['sp_replacement_d2_047'], 'func': sp_replacement_d3_047}


def sp_replacement_d3_048(sp_replacement_d2_048):
    feature = _clean(sp_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_048'] = {'inputs': ['sp_replacement_d2_048'], 'func': sp_replacement_d3_048}


def sp_replacement_d3_049(sp_replacement_d2_049):
    feature = _clean(sp_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_049'] = {'inputs': ['sp_replacement_d2_049'], 'func': sp_replacement_d3_049}


def sp_replacement_d3_050(sp_replacement_d2_050):
    feature = _clean(sp_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_050'] = {'inputs': ['sp_replacement_d2_050'], 'func': sp_replacement_d3_050}


def sp_replacement_d3_051(sp_replacement_d2_051):
    feature = _clean(sp_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_051'] = {'inputs': ['sp_replacement_d2_051'], 'func': sp_replacement_d3_051}


def sp_replacement_d3_052(sp_replacement_d2_052):
    feature = _clean(sp_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_052'] = {'inputs': ['sp_replacement_d2_052'], 'func': sp_replacement_d3_052}


def sp_replacement_d3_053(sp_replacement_d2_053):
    feature = _clean(sp_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_053'] = {'inputs': ['sp_replacement_d2_053'], 'func': sp_replacement_d3_053}


def sp_replacement_d3_054(sp_replacement_d2_054):
    feature = _clean(sp_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_054'] = {'inputs': ['sp_replacement_d2_054'], 'func': sp_replacement_d3_054}


def sp_replacement_d3_055(sp_replacement_d2_055):
    feature = _clean(sp_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_055'] = {'inputs': ['sp_replacement_d2_055'], 'func': sp_replacement_d3_055}


def sp_replacement_d3_056(sp_replacement_d2_056):
    feature = _clean(sp_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_056'] = {'inputs': ['sp_replacement_d2_056'], 'func': sp_replacement_d3_056}


def sp_replacement_d3_057(sp_replacement_d2_057):
    feature = _clean(sp_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_057'] = {'inputs': ['sp_replacement_d2_057'], 'func': sp_replacement_d3_057}


def sp_replacement_d3_058(sp_replacement_d2_058):
    feature = _clean(sp_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_058'] = {'inputs': ['sp_replacement_d2_058'], 'func': sp_replacement_d3_058}


def sp_replacement_d3_059(sp_replacement_d2_059):
    feature = _clean(sp_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_059'] = {'inputs': ['sp_replacement_d2_059'], 'func': sp_replacement_d3_059}


def sp_replacement_d3_060(sp_replacement_d2_060):
    feature = _clean(sp_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_060'] = {'inputs': ['sp_replacement_d2_060'], 'func': sp_replacement_d3_060}


def sp_replacement_d3_061(sp_replacement_d2_061):
    feature = _clean(sp_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_061'] = {'inputs': ['sp_replacement_d2_061'], 'func': sp_replacement_d3_061}


def sp_replacement_d3_062(sp_replacement_d2_062):
    feature = _clean(sp_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_062'] = {'inputs': ['sp_replacement_d2_062'], 'func': sp_replacement_d3_062}


def sp_replacement_d3_063(sp_replacement_d2_063):
    feature = _clean(sp_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_063'] = {'inputs': ['sp_replacement_d2_063'], 'func': sp_replacement_d3_063}


def sp_replacement_d3_064(sp_replacement_d2_064):
    feature = _clean(sp_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_064'] = {'inputs': ['sp_replacement_d2_064'], 'func': sp_replacement_d3_064}


def sp_replacement_d3_065(sp_replacement_d2_065):
    feature = _clean(sp_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_065'] = {'inputs': ['sp_replacement_d2_065'], 'func': sp_replacement_d3_065}


def sp_replacement_d3_066(sp_replacement_d2_066):
    feature = _clean(sp_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_066'] = {'inputs': ['sp_replacement_d2_066'], 'func': sp_replacement_d3_066}


def sp_replacement_d3_067(sp_replacement_d2_067):
    feature = _clean(sp_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_067'] = {'inputs': ['sp_replacement_d2_067'], 'func': sp_replacement_d3_067}


def sp_replacement_d3_068(sp_replacement_d2_068):
    feature = _clean(sp_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_068'] = {'inputs': ['sp_replacement_d2_068'], 'func': sp_replacement_d3_068}


def sp_replacement_d3_069(sp_replacement_d2_069):
    feature = _clean(sp_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_069'] = {'inputs': ['sp_replacement_d2_069'], 'func': sp_replacement_d3_069}


def sp_replacement_d3_070(sp_replacement_d2_070):
    feature = _clean(sp_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_070'] = {'inputs': ['sp_replacement_d2_070'], 'func': sp_replacement_d3_070}


def sp_replacement_d3_071(sp_replacement_d2_071):
    feature = _clean(sp_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_071'] = {'inputs': ['sp_replacement_d2_071'], 'func': sp_replacement_d3_071}


def sp_replacement_d3_072(sp_replacement_d2_072):
    feature = _clean(sp_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_072'] = {'inputs': ['sp_replacement_d2_072'], 'func': sp_replacement_d3_072}


def sp_replacement_d3_073(sp_replacement_d2_073):
    feature = _clean(sp_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_073'] = {'inputs': ['sp_replacement_d2_073'], 'func': sp_replacement_d3_073}


def sp_replacement_d3_074(sp_replacement_d2_074):
    feature = _clean(sp_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_074'] = {'inputs': ['sp_replacement_d2_074'], 'func': sp_replacement_d3_074}


def sp_replacement_d3_075(sp_replacement_d2_075):
    feature = _clean(sp_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_075'] = {'inputs': ['sp_replacement_d2_075'], 'func': sp_replacement_d3_075}


def sp_replacement_d3_076(sp_replacement_d2_076):
    feature = _clean(sp_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_076'] = {'inputs': ['sp_replacement_d2_076'], 'func': sp_replacement_d3_076}


def sp_replacement_d3_077(sp_replacement_d2_077):
    feature = _clean(sp_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_077'] = {'inputs': ['sp_replacement_d2_077'], 'func': sp_replacement_d3_077}


def sp_replacement_d3_078(sp_replacement_d2_078):
    feature = _clean(sp_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_078'] = {'inputs': ['sp_replacement_d2_078'], 'func': sp_replacement_d3_078}


def sp_replacement_d3_079(sp_replacement_d2_079):
    feature = _clean(sp_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_079'] = {'inputs': ['sp_replacement_d2_079'], 'func': sp_replacement_d3_079}


def sp_replacement_d3_080(sp_replacement_d2_080):
    feature = _clean(sp_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_080'] = {'inputs': ['sp_replacement_d2_080'], 'func': sp_replacement_d3_080}


def sp_replacement_d3_081(sp_replacement_d2_081):
    feature = _clean(sp_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_081'] = {'inputs': ['sp_replacement_d2_081'], 'func': sp_replacement_d3_081}


def sp_replacement_d3_082(sp_replacement_d2_082):
    feature = _clean(sp_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_082'] = {'inputs': ['sp_replacement_d2_082'], 'func': sp_replacement_d3_082}


def sp_replacement_d3_083(sp_replacement_d2_083):
    feature = _clean(sp_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_083'] = {'inputs': ['sp_replacement_d2_083'], 'func': sp_replacement_d3_083}


def sp_replacement_d3_084(sp_replacement_d2_084):
    feature = _clean(sp_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_084'] = {'inputs': ['sp_replacement_d2_084'], 'func': sp_replacement_d3_084}


def sp_replacement_d3_085(sp_replacement_d2_085):
    feature = _clean(sp_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_085'] = {'inputs': ['sp_replacement_d2_085'], 'func': sp_replacement_d3_085}


def sp_replacement_d3_086(sp_replacement_d2_086):
    feature = _clean(sp_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_086'] = {'inputs': ['sp_replacement_d2_086'], 'func': sp_replacement_d3_086}


def sp_replacement_d3_087(sp_replacement_d2_087):
    feature = _clean(sp_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_087'] = {'inputs': ['sp_replacement_d2_087'], 'func': sp_replacement_d3_087}


def sp_replacement_d3_088(sp_replacement_d2_088):
    feature = _clean(sp_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_088'] = {'inputs': ['sp_replacement_d2_088'], 'func': sp_replacement_d3_088}


def sp_replacement_d3_089(sp_replacement_d2_089):
    feature = _clean(sp_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_089'] = {'inputs': ['sp_replacement_d2_089'], 'func': sp_replacement_d3_089}


def sp_replacement_d3_090(sp_replacement_d2_090):
    feature = _clean(sp_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_090'] = {'inputs': ['sp_replacement_d2_090'], 'func': sp_replacement_d3_090}


def sp_replacement_d3_091(sp_replacement_d2_091):
    feature = _clean(sp_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_091'] = {'inputs': ['sp_replacement_d2_091'], 'func': sp_replacement_d3_091}


def sp_replacement_d3_092(sp_replacement_d2_092):
    feature = _clean(sp_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_092'] = {'inputs': ['sp_replacement_d2_092'], 'func': sp_replacement_d3_092}


def sp_replacement_d3_093(sp_replacement_d2_093):
    feature = _clean(sp_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_093'] = {'inputs': ['sp_replacement_d2_093'], 'func': sp_replacement_d3_093}


def sp_replacement_d3_094(sp_replacement_d2_094):
    feature = _clean(sp_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_094'] = {'inputs': ['sp_replacement_d2_094'], 'func': sp_replacement_d3_094}


def sp_replacement_d3_095(sp_replacement_d2_095):
    feature = _clean(sp_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_095'] = {'inputs': ['sp_replacement_d2_095'], 'func': sp_replacement_d3_095}


def sp_replacement_d3_096(sp_replacement_d2_096):
    feature = _clean(sp_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_096'] = {'inputs': ['sp_replacement_d2_096'], 'func': sp_replacement_d3_096}


def sp_replacement_d3_097(sp_replacement_d2_097):
    feature = _clean(sp_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_097'] = {'inputs': ['sp_replacement_d2_097'], 'func': sp_replacement_d3_097}


def sp_replacement_d3_098(sp_replacement_d2_098):
    feature = _clean(sp_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_098'] = {'inputs': ['sp_replacement_d2_098'], 'func': sp_replacement_d3_098}


def sp_replacement_d3_099(sp_replacement_d2_099):
    feature = _clean(sp_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_099'] = {'inputs': ['sp_replacement_d2_099'], 'func': sp_replacement_d3_099}


def sp_replacement_d3_100(sp_replacement_d2_100):
    feature = _clean(sp_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_100'] = {'inputs': ['sp_replacement_d2_100'], 'func': sp_replacement_d3_100}


def sp_replacement_d3_101(sp_replacement_d2_101):
    feature = _clean(sp_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_101'] = {'inputs': ['sp_replacement_d2_101'], 'func': sp_replacement_d3_101}


def sp_replacement_d3_102(sp_replacement_d2_102):
    feature = _clean(sp_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_102'] = {'inputs': ['sp_replacement_d2_102'], 'func': sp_replacement_d3_102}


def sp_replacement_d3_103(sp_replacement_d2_103):
    feature = _clean(sp_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_103'] = {'inputs': ['sp_replacement_d2_103'], 'func': sp_replacement_d3_103}


def sp_replacement_d3_104(sp_replacement_d2_104):
    feature = _clean(sp_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_104'] = {'inputs': ['sp_replacement_d2_104'], 'func': sp_replacement_d3_104}


def sp_replacement_d3_105(sp_replacement_d2_105):
    feature = _clean(sp_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_105'] = {'inputs': ['sp_replacement_d2_105'], 'func': sp_replacement_d3_105}


def sp_replacement_d3_106(sp_replacement_d2_106):
    feature = _clean(sp_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_106'] = {'inputs': ['sp_replacement_d2_106'], 'func': sp_replacement_d3_106}


def sp_replacement_d3_107(sp_replacement_d2_107):
    feature = _clean(sp_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_107'] = {'inputs': ['sp_replacement_d2_107'], 'func': sp_replacement_d3_107}


def sp_replacement_d3_108(sp_replacement_d2_108):
    feature = _clean(sp_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_108'] = {'inputs': ['sp_replacement_d2_108'], 'func': sp_replacement_d3_108}


def sp_replacement_d3_109(sp_replacement_d2_109):
    feature = _clean(sp_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_109'] = {'inputs': ['sp_replacement_d2_109'], 'func': sp_replacement_d3_109}


def sp_replacement_d3_110(sp_replacement_d2_110):
    feature = _clean(sp_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_110'] = {'inputs': ['sp_replacement_d2_110'], 'func': sp_replacement_d3_110}


def sp_replacement_d3_111(sp_replacement_d2_111):
    feature = _clean(sp_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_111'] = {'inputs': ['sp_replacement_d2_111'], 'func': sp_replacement_d3_111}


def sp_replacement_d3_112(sp_replacement_d2_112):
    feature = _clean(sp_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_112'] = {'inputs': ['sp_replacement_d2_112'], 'func': sp_replacement_d3_112}


def sp_replacement_d3_113(sp_replacement_d2_113):
    feature = _clean(sp_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_113'] = {'inputs': ['sp_replacement_d2_113'], 'func': sp_replacement_d3_113}


def sp_replacement_d3_114(sp_replacement_d2_114):
    feature = _clean(sp_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_114'] = {'inputs': ['sp_replacement_d2_114'], 'func': sp_replacement_d3_114}


def sp_replacement_d3_115(sp_replacement_d2_115):
    feature = _clean(sp_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_115'] = {'inputs': ['sp_replacement_d2_115'], 'func': sp_replacement_d3_115}


def sp_replacement_d3_116(sp_replacement_d2_116):
    feature = _clean(sp_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_116'] = {'inputs': ['sp_replacement_d2_116'], 'func': sp_replacement_d3_116}


def sp_replacement_d3_117(sp_replacement_d2_117):
    feature = _clean(sp_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_117'] = {'inputs': ['sp_replacement_d2_117'], 'func': sp_replacement_d3_117}


def sp_replacement_d3_118(sp_replacement_d2_118):
    feature = _clean(sp_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_118'] = {'inputs': ['sp_replacement_d2_118'], 'func': sp_replacement_d3_118}


def sp_replacement_d3_119(sp_replacement_d2_119):
    feature = _clean(sp_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_119'] = {'inputs': ['sp_replacement_d2_119'], 'func': sp_replacement_d3_119}


def sp_replacement_d3_120(sp_replacement_d2_120):
    feature = _clean(sp_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_120'] = {'inputs': ['sp_replacement_d2_120'], 'func': sp_replacement_d3_120}


def sp_replacement_d3_121(sp_replacement_d2_121):
    feature = _clean(sp_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_121'] = {'inputs': ['sp_replacement_d2_121'], 'func': sp_replacement_d3_121}


def sp_replacement_d3_122(sp_replacement_d2_122):
    feature = _clean(sp_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_122'] = {'inputs': ['sp_replacement_d2_122'], 'func': sp_replacement_d3_122}


def sp_replacement_d3_123(sp_replacement_d2_123):
    feature = _clean(sp_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_123'] = {'inputs': ['sp_replacement_d2_123'], 'func': sp_replacement_d3_123}


def sp_replacement_d3_124(sp_replacement_d2_124):
    feature = _clean(sp_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_124'] = {'inputs': ['sp_replacement_d2_124'], 'func': sp_replacement_d3_124}


def sp_replacement_d3_125(sp_replacement_d2_125):
    feature = _clean(sp_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_125'] = {'inputs': ['sp_replacement_d2_125'], 'func': sp_replacement_d3_125}


def sp_replacement_d3_126(sp_replacement_d2_126):
    feature = _clean(sp_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_126'] = {'inputs': ['sp_replacement_d2_126'], 'func': sp_replacement_d3_126}


def sp_replacement_d3_127(sp_replacement_d2_127):
    feature = _clean(sp_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_127'] = {'inputs': ['sp_replacement_d2_127'], 'func': sp_replacement_d3_127}


def sp_replacement_d3_128(sp_replacement_d2_128):
    feature = _clean(sp_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_128'] = {'inputs': ['sp_replacement_d2_128'], 'func': sp_replacement_d3_128}


def sp_replacement_d3_129(sp_replacement_d2_129):
    feature = _clean(sp_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_129'] = {'inputs': ['sp_replacement_d2_129'], 'func': sp_replacement_d3_129}


def sp_replacement_d3_130(sp_replacement_d2_130):
    feature = _clean(sp_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_130'] = {'inputs': ['sp_replacement_d2_130'], 'func': sp_replacement_d3_130}


def sp_replacement_d3_131(sp_replacement_d2_131):
    feature = _clean(sp_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_131'] = {'inputs': ['sp_replacement_d2_131'], 'func': sp_replacement_d3_131}


def sp_replacement_d3_132(sp_replacement_d2_132):
    feature = _clean(sp_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_132'] = {'inputs': ['sp_replacement_d2_132'], 'func': sp_replacement_d3_132}


def sp_replacement_d3_133(sp_replacement_d2_133):
    feature = _clean(sp_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_133'] = {'inputs': ['sp_replacement_d2_133'], 'func': sp_replacement_d3_133}


def sp_replacement_d3_134(sp_replacement_d2_134):
    feature = _clean(sp_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_134'] = {'inputs': ['sp_replacement_d2_134'], 'func': sp_replacement_d3_134}


def sp_replacement_d3_135(sp_replacement_d2_135):
    feature = _clean(sp_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_135'] = {'inputs': ['sp_replacement_d2_135'], 'func': sp_replacement_d3_135}


def sp_replacement_d3_136(sp_replacement_d2_136):
    feature = _clean(sp_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_136'] = {'inputs': ['sp_replacement_d2_136'], 'func': sp_replacement_d3_136}


def sp_replacement_d3_137(sp_replacement_d2_137):
    feature = _clean(sp_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_137'] = {'inputs': ['sp_replacement_d2_137'], 'func': sp_replacement_d3_137}


def sp_replacement_d3_138(sp_replacement_d2_138):
    feature = _clean(sp_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_138'] = {'inputs': ['sp_replacement_d2_138'], 'func': sp_replacement_d3_138}


def sp_replacement_d3_139(sp_replacement_d2_139):
    feature = _clean(sp_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_139'] = {'inputs': ['sp_replacement_d2_139'], 'func': sp_replacement_d3_139}


def sp_replacement_d3_140(sp_replacement_d2_140):
    feature = _clean(sp_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_140'] = {'inputs': ['sp_replacement_d2_140'], 'func': sp_replacement_d3_140}


def sp_replacement_d3_141(sp_replacement_d2_141):
    feature = _clean(sp_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_141'] = {'inputs': ['sp_replacement_d2_141'], 'func': sp_replacement_d3_141}


def sp_replacement_d3_142(sp_replacement_d2_142):
    feature = _clean(sp_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_142'] = {'inputs': ['sp_replacement_d2_142'], 'func': sp_replacement_d3_142}


def sp_replacement_d3_143(sp_replacement_d2_143):
    feature = _clean(sp_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_143'] = {'inputs': ['sp_replacement_d2_143'], 'func': sp_replacement_d3_143}


def sp_replacement_d3_144(sp_replacement_d2_144):
    feature = _clean(sp_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_144'] = {'inputs': ['sp_replacement_d2_144'], 'func': sp_replacement_d3_144}


def sp_replacement_d3_145(sp_replacement_d2_145):
    feature = _clean(sp_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_145'] = {'inputs': ['sp_replacement_d2_145'], 'func': sp_replacement_d3_145}


def sp_replacement_d3_146(sp_replacement_d2_146):
    feature = _clean(sp_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_146'] = {'inputs': ['sp_replacement_d2_146'], 'func': sp_replacement_d3_146}


def sp_replacement_d3_147(sp_replacement_d2_147):
    feature = _clean(sp_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_147'] = {'inputs': ['sp_replacement_d2_147'], 'func': sp_replacement_d3_147}


def sp_replacement_d3_148(sp_replacement_d2_148):
    feature = _clean(sp_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_148'] = {'inputs': ['sp_replacement_d2_148'], 'func': sp_replacement_d3_148}


def sp_replacement_d3_149(sp_replacement_d2_149):
    feature = _clean(sp_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_149'] = {'inputs': ['sp_replacement_d2_149'], 'func': sp_replacement_d3_149}


def sp_replacement_d3_150(sp_replacement_d2_150):
    feature = _clean(sp_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_150'] = {'inputs': ['sp_replacement_d2_150'], 'func': sp_replacement_d3_150}


def sp_replacement_d3_151(sp_replacement_d2_151):
    feature = _clean(sp_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_151'] = {'inputs': ['sp_replacement_d2_151'], 'func': sp_replacement_d3_151}


def sp_replacement_d3_152(sp_replacement_d2_152):
    feature = _clean(sp_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_152'] = {'inputs': ['sp_replacement_d2_152'], 'func': sp_replacement_d3_152}


def sp_replacement_d3_153(sp_replacement_d2_153):
    feature = _clean(sp_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_153'] = {'inputs': ['sp_replacement_d2_153'], 'func': sp_replacement_d3_153}


def sp_replacement_d3_154(sp_replacement_d2_154):
    feature = _clean(sp_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_154'] = {'inputs': ['sp_replacement_d2_154'], 'func': sp_replacement_d3_154}


def sp_replacement_d3_155(sp_replacement_d2_155):
    feature = _clean(sp_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_155'] = {'inputs': ['sp_replacement_d2_155'], 'func': sp_replacement_d3_155}


def sp_replacement_d3_156(sp_replacement_d2_156):
    feature = _clean(sp_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_156'] = {'inputs': ['sp_replacement_d2_156'], 'func': sp_replacement_d3_156}


def sp_replacement_d3_157(sp_replacement_d2_157):
    feature = _clean(sp_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_157'] = {'inputs': ['sp_replacement_d2_157'], 'func': sp_replacement_d3_157}


def sp_replacement_d3_158(sp_replacement_d2_158):
    feature = _clean(sp_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_158'] = {'inputs': ['sp_replacement_d2_158'], 'func': sp_replacement_d3_158}


def sp_replacement_d3_159(sp_replacement_d2_159):
    feature = _clean(sp_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_159'] = {'inputs': ['sp_replacement_d2_159'], 'func': sp_replacement_d3_159}


def sp_replacement_d3_160(sp_replacement_d2_160):
    feature = _clean(sp_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_160'] = {'inputs': ['sp_replacement_d2_160'], 'func': sp_replacement_d3_160}


def sp_replacement_d3_161(sp_replacement_d2_161):
    feature = _clean(sp_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_161'] = {'inputs': ['sp_replacement_d2_161'], 'func': sp_replacement_d3_161}


def sp_replacement_d3_162(sp_replacement_d2_162):
    feature = _clean(sp_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_162'] = {'inputs': ['sp_replacement_d2_162'], 'func': sp_replacement_d3_162}


def sp_replacement_d3_163(sp_replacement_d2_163):
    feature = _clean(sp_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_163'] = {'inputs': ['sp_replacement_d2_163'], 'func': sp_replacement_d3_163}


def sp_replacement_d3_164(sp_replacement_d2_164):
    feature = _clean(sp_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_164'] = {'inputs': ['sp_replacement_d2_164'], 'func': sp_replacement_d3_164}


def sp_replacement_d3_165(sp_replacement_d2_165):
    feature = _clean(sp_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_165'] = {'inputs': ['sp_replacement_d2_165'], 'func': sp_replacement_d3_165}


def sp_replacement_d3_166(sp_replacement_d2_166):
    feature = _clean(sp_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_166'] = {'inputs': ['sp_replacement_d2_166'], 'func': sp_replacement_d3_166}


def sp_replacement_d3_167(sp_replacement_d2_167):
    feature = _clean(sp_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_167'] = {'inputs': ['sp_replacement_d2_167'], 'func': sp_replacement_d3_167}


def sp_replacement_d3_168(sp_replacement_d2_168):
    feature = _clean(sp_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_168'] = {'inputs': ['sp_replacement_d2_168'], 'func': sp_replacement_d3_168}


def sp_replacement_d3_169(sp_replacement_d2_169):
    feature = _clean(sp_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_169'] = {'inputs': ['sp_replacement_d2_169'], 'func': sp_replacement_d3_169}


def sp_replacement_d3_170(sp_replacement_d2_170):
    feature = _clean(sp_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
SP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['sp_replacement_d3_170'] = {'inputs': ['sp_replacement_d2_170'], 'func': sp_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def spr_base_universe_d3_001_spr_002_zero_volume_frequency_10_002(spr_base_universe_d2_001_spr_002_zero_volume_frequency_10_002):
    return _base_universe_d3(spr_base_universe_d2_001_spr_002_zero_volume_frequency_10_002, 1)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_001_spr_002_zero_volume_frequency_10_002'] = {'inputs': ['spr_base_universe_d2_001_spr_002_zero_volume_frequency_10_002'], 'func': spr_base_universe_d3_001_spr_002_zero_volume_frequency_10_002}


def spr_base_universe_d3_002_spr_003_spread_proxy_21_003(spr_base_universe_d2_002_spr_003_spread_proxy_21_003):
    return _base_universe_d3(spr_base_universe_d2_002_spr_003_spread_proxy_21_003, 2)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_002_spr_003_spread_proxy_21_003'] = {'inputs': ['spr_base_universe_d2_002_spr_003_spread_proxy_21_003'], 'func': spr_base_universe_d3_002_spr_003_spread_proxy_21_003}


def spr_base_universe_d3_003_spr_004_trading_intensity_42_004(spr_base_universe_d2_003_spr_004_trading_intensity_42_004):
    return _base_universe_d3(spr_base_universe_d2_003_spr_004_trading_intensity_42_004, 3)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_003_spr_004_trading_intensity_42_004'] = {'inputs': ['spr_base_universe_d2_003_spr_004_trading_intensity_42_004'], 'func': spr_base_universe_d3_003_spr_004_trading_intensity_42_004}


def spr_base_universe_d3_004_spr_006_price_level_distress_84_006(spr_base_universe_d2_004_spr_006_price_level_distress_84_006):
    return _base_universe_d3(spr_base_universe_d2_004_spr_006_price_level_distress_84_006, 4)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_004_spr_006_price_level_distress_84_006'] = {'inputs': ['spr_base_universe_d2_004_spr_006_price_level_distress_84_006'], 'func': spr_base_universe_d3_004_spr_006_price_level_distress_84_006}


def spr_base_universe_d3_005_spr_008_zero_volume_frequency_189_008(spr_base_universe_d2_005_spr_008_zero_volume_frequency_189_008):
    return _base_universe_d3(spr_base_universe_d2_005_spr_008_zero_volume_frequency_189_008, 5)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_005_spr_008_zero_volume_frequency_189_008'] = {'inputs': ['spr_base_universe_d2_005_spr_008_zero_volume_frequency_189_008'], 'func': spr_base_universe_d3_005_spr_008_zero_volume_frequency_189_008}


def spr_base_universe_d3_006_spr_009_spread_proxy_252_009(spr_base_universe_d2_006_spr_009_spread_proxy_252_009):
    return _base_universe_d3(spr_base_universe_d2_006_spr_009_spread_proxy_252_009, 6)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_006_spr_009_spread_proxy_252_009'] = {'inputs': ['spr_base_universe_d2_006_spr_009_spread_proxy_252_009'], 'func': spr_base_universe_d3_006_spr_009_spread_proxy_252_009}


def spr_base_universe_d3_007_spr_010_trading_intensity_378_010(spr_base_universe_d2_007_spr_010_trading_intensity_378_010):
    return _base_universe_d3(spr_base_universe_d2_007_spr_010_trading_intensity_378_010, 7)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_007_spr_010_trading_intensity_378_010'] = {'inputs': ['spr_base_universe_d2_007_spr_010_trading_intensity_378_010'], 'func': spr_base_universe_d3_007_spr_010_trading_intensity_378_010}


def spr_base_universe_d3_008_spr_012_price_level_distress_756_012(spr_base_universe_d2_008_spr_012_price_level_distress_756_012):
    return _base_universe_d3(spr_base_universe_d2_008_spr_012_price_level_distress_756_012, 8)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_008_spr_012_price_level_distress_756_012'] = {'inputs': ['spr_base_universe_d2_008_spr_012_price_level_distress_756_012'], 'func': spr_base_universe_d3_008_spr_012_price_level_distress_756_012}


def spr_base_universe_d3_009_spr_014_zero_volume_frequency_1260_014(spr_base_universe_d2_009_spr_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(spr_base_universe_d2_009_spr_014_zero_volume_frequency_1260_014, 9)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_009_spr_014_zero_volume_frequency_1260_014'] = {'inputs': ['spr_base_universe_d2_009_spr_014_zero_volume_frequency_1260_014'], 'func': spr_base_universe_d3_009_spr_014_zero_volume_frequency_1260_014}


def spr_base_universe_d3_010_spr_015_spread_proxy_1512_015(spr_base_universe_d2_010_spr_015_spread_proxy_1512_015):
    return _base_universe_d3(spr_base_universe_d2_010_spr_015_spread_proxy_1512_015, 10)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_010_spr_015_spread_proxy_1512_015'] = {'inputs': ['spr_base_universe_d2_010_spr_015_spread_proxy_1512_015'], 'func': spr_base_universe_d3_010_spr_015_spread_proxy_1512_015}


def spr_base_universe_d3_011_spr_016_trading_intensity_5_016(spr_base_universe_d2_011_spr_016_trading_intensity_5_016):
    return _base_universe_d3(spr_base_universe_d2_011_spr_016_trading_intensity_5_016, 11)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_011_spr_016_trading_intensity_5_016'] = {'inputs': ['spr_base_universe_d2_011_spr_016_trading_intensity_5_016'], 'func': spr_base_universe_d3_011_spr_016_trading_intensity_5_016}


def spr_base_universe_d3_012_spr_018_price_level_distress_21_018(spr_base_universe_d2_012_spr_018_price_level_distress_21_018):
    return _base_universe_d3(spr_base_universe_d2_012_spr_018_price_level_distress_21_018, 12)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_012_spr_018_price_level_distress_21_018'] = {'inputs': ['spr_base_universe_d2_012_spr_018_price_level_distress_21_018'], 'func': spr_base_universe_d3_012_spr_018_price_level_distress_21_018}


def spr_base_universe_d3_013_spr_020_zero_volume_frequency_63_020(spr_base_universe_d2_013_spr_020_zero_volume_frequency_63_020):
    return _base_universe_d3(spr_base_universe_d2_013_spr_020_zero_volume_frequency_63_020, 13)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_013_spr_020_zero_volume_frequency_63_020'] = {'inputs': ['spr_base_universe_d2_013_spr_020_zero_volume_frequency_63_020'], 'func': spr_base_universe_d3_013_spr_020_zero_volume_frequency_63_020}


def spr_base_universe_d3_014_spr_021_spread_proxy_84_021(spr_base_universe_d2_014_spr_021_spread_proxy_84_021):
    return _base_universe_d3(spr_base_universe_d2_014_spr_021_spread_proxy_84_021, 14)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_014_spr_021_spread_proxy_84_021'] = {'inputs': ['spr_base_universe_d2_014_spr_021_spread_proxy_84_021'], 'func': spr_base_universe_d3_014_spr_021_spread_proxy_84_021}


def spr_base_universe_d3_015_spr_022_trading_intensity_126_022(spr_base_universe_d2_015_spr_022_trading_intensity_126_022):
    return _base_universe_d3(spr_base_universe_d2_015_spr_022_trading_intensity_126_022, 15)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_015_spr_022_trading_intensity_126_022'] = {'inputs': ['spr_base_universe_d2_015_spr_022_trading_intensity_126_022'], 'func': spr_base_universe_d3_015_spr_022_trading_intensity_126_022}


def spr_base_universe_d3_016_spr_024_price_level_distress_252_024(spr_base_universe_d2_016_spr_024_price_level_distress_252_024):
    return _base_universe_d3(spr_base_universe_d2_016_spr_024_price_level_distress_252_024, 16)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_016_spr_024_price_level_distress_252_024'] = {'inputs': ['spr_base_universe_d2_016_spr_024_price_level_distress_252_024'], 'func': spr_base_universe_d3_016_spr_024_price_level_distress_252_024}


def spr_base_universe_d3_017_spr_026_zero_volume_frequency_504_026(spr_base_universe_d2_017_spr_026_zero_volume_frequency_504_026):
    return _base_universe_d3(spr_base_universe_d2_017_spr_026_zero_volume_frequency_504_026, 17)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_017_spr_026_zero_volume_frequency_504_026'] = {'inputs': ['spr_base_universe_d2_017_spr_026_zero_volume_frequency_504_026'], 'func': spr_base_universe_d3_017_spr_026_zero_volume_frequency_504_026}


def spr_base_universe_d3_018_spr_027_spread_proxy_756_027(spr_base_universe_d2_018_spr_027_spread_proxy_756_027):
    return _base_universe_d3(spr_base_universe_d2_018_spr_027_spread_proxy_756_027, 18)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_018_spr_027_spread_proxy_756_027'] = {'inputs': ['spr_base_universe_d2_018_spr_027_spread_proxy_756_027'], 'func': spr_base_universe_d3_018_spr_027_spread_proxy_756_027}


def spr_base_universe_d3_019_spr_028_trading_intensity_1008_028(spr_base_universe_d2_019_spr_028_trading_intensity_1008_028):
    return _base_universe_d3(spr_base_universe_d2_019_spr_028_trading_intensity_1008_028, 19)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_019_spr_028_trading_intensity_1008_028'] = {'inputs': ['spr_base_universe_d2_019_spr_028_trading_intensity_1008_028'], 'func': spr_base_universe_d3_019_spr_028_trading_intensity_1008_028}


def spr_base_universe_d3_020_spr_030_price_level_distress_1512_030(spr_base_universe_d2_020_spr_030_price_level_distress_1512_030):
    return _base_universe_d3(spr_base_universe_d2_020_spr_030_price_level_distress_1512_030, 20)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_020_spr_030_price_level_distress_1512_030'] = {'inputs': ['spr_base_universe_d2_020_spr_030_price_level_distress_1512_030'], 'func': spr_base_universe_d3_020_spr_030_price_level_distress_1512_030}


def spr_base_universe_d3_021_spr_basefill_001(spr_base_universe_d2_021_spr_basefill_001):
    return _base_universe_d3(spr_base_universe_d2_021_spr_basefill_001, 21)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_021_spr_basefill_001'] = {'inputs': ['spr_base_universe_d2_021_spr_basefill_001'], 'func': spr_base_universe_d3_021_spr_basefill_001}


def spr_base_universe_d3_022_spr_basefill_005(spr_base_universe_d2_022_spr_basefill_005):
    return _base_universe_d3(spr_base_universe_d2_022_spr_basefill_005, 22)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_022_spr_basefill_005'] = {'inputs': ['spr_base_universe_d2_022_spr_basefill_005'], 'func': spr_base_universe_d3_022_spr_basefill_005}


def spr_base_universe_d3_023_spr_basefill_007(spr_base_universe_d2_023_spr_basefill_007):
    return _base_universe_d3(spr_base_universe_d2_023_spr_basefill_007, 23)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_023_spr_basefill_007'] = {'inputs': ['spr_base_universe_d2_023_spr_basefill_007'], 'func': spr_base_universe_d3_023_spr_basefill_007}


def spr_base_universe_d3_024_spr_basefill_011(spr_base_universe_d2_024_spr_basefill_011):
    return _base_universe_d3(spr_base_universe_d2_024_spr_basefill_011, 24)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_024_spr_basefill_011'] = {'inputs': ['spr_base_universe_d2_024_spr_basefill_011'], 'func': spr_base_universe_d3_024_spr_basefill_011}


def spr_base_universe_d3_025_spr_basefill_013(spr_base_universe_d2_025_spr_basefill_013):
    return _base_universe_d3(spr_base_universe_d2_025_spr_basefill_013, 25)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_025_spr_basefill_013'] = {'inputs': ['spr_base_universe_d2_025_spr_basefill_013'], 'func': spr_base_universe_d3_025_spr_basefill_013}


def spr_base_universe_d3_026_spr_basefill_017(spr_base_universe_d2_026_spr_basefill_017):
    return _base_universe_d3(spr_base_universe_d2_026_spr_basefill_017, 26)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_026_spr_basefill_017'] = {'inputs': ['spr_base_universe_d2_026_spr_basefill_017'], 'func': spr_base_universe_d3_026_spr_basefill_017}


def spr_base_universe_d3_027_spr_basefill_019(spr_base_universe_d2_027_spr_basefill_019):
    return _base_universe_d3(spr_base_universe_d2_027_spr_basefill_019, 27)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_027_spr_basefill_019'] = {'inputs': ['spr_base_universe_d2_027_spr_basefill_019'], 'func': spr_base_universe_d3_027_spr_basefill_019}


def spr_base_universe_d3_028_spr_basefill_023(spr_base_universe_d2_028_spr_basefill_023):
    return _base_universe_d3(spr_base_universe_d2_028_spr_basefill_023, 28)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_028_spr_basefill_023'] = {'inputs': ['spr_base_universe_d2_028_spr_basefill_023'], 'func': spr_base_universe_d3_028_spr_basefill_023}


def spr_base_universe_d3_029_spr_basefill_025(spr_base_universe_d2_029_spr_basefill_025):
    return _base_universe_d3(spr_base_universe_d2_029_spr_basefill_025, 29)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_029_spr_basefill_025'] = {'inputs': ['spr_base_universe_d2_029_spr_basefill_025'], 'func': spr_base_universe_d3_029_spr_basefill_025}


def spr_base_universe_d3_030_spr_basefill_029(spr_base_universe_d2_030_spr_basefill_029):
    return _base_universe_d3(spr_base_universe_d2_030_spr_basefill_029, 30)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_030_spr_basefill_029'] = {'inputs': ['spr_base_universe_d2_030_spr_basefill_029'], 'func': spr_base_universe_d3_030_spr_basefill_029}


def spr_base_universe_d3_031_spr_basefill_031(spr_base_universe_d2_031_spr_basefill_031):
    return _base_universe_d3(spr_base_universe_d2_031_spr_basefill_031, 31)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_031_spr_basefill_031'] = {'inputs': ['spr_base_universe_d2_031_spr_basefill_031'], 'func': spr_base_universe_d3_031_spr_basefill_031}


def spr_base_universe_d3_032_spr_basefill_032(spr_base_universe_d2_032_spr_basefill_032):
    return _base_universe_d3(spr_base_universe_d2_032_spr_basefill_032, 32)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_032_spr_basefill_032'] = {'inputs': ['spr_base_universe_d2_032_spr_basefill_032'], 'func': spr_base_universe_d3_032_spr_basefill_032}


def spr_base_universe_d3_033_spr_basefill_033(spr_base_universe_d2_033_spr_basefill_033):
    return _base_universe_d3(spr_base_universe_d2_033_spr_basefill_033, 33)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_033_spr_basefill_033'] = {'inputs': ['spr_base_universe_d2_033_spr_basefill_033'], 'func': spr_base_universe_d3_033_spr_basefill_033}


def spr_base_universe_d3_034_spr_basefill_034(spr_base_universe_d2_034_spr_basefill_034):
    return _base_universe_d3(spr_base_universe_d2_034_spr_basefill_034, 34)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_034_spr_basefill_034'] = {'inputs': ['spr_base_universe_d2_034_spr_basefill_034'], 'func': spr_base_universe_d3_034_spr_basefill_034}


def spr_base_universe_d3_035_spr_basefill_035(spr_base_universe_d2_035_spr_basefill_035):
    return _base_universe_d3(spr_base_universe_d2_035_spr_basefill_035, 35)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_035_spr_basefill_035'] = {'inputs': ['spr_base_universe_d2_035_spr_basefill_035'], 'func': spr_base_universe_d3_035_spr_basefill_035}


def spr_base_universe_d3_036_spr_basefill_036(spr_base_universe_d2_036_spr_basefill_036):
    return _base_universe_d3(spr_base_universe_d2_036_spr_basefill_036, 36)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_036_spr_basefill_036'] = {'inputs': ['spr_base_universe_d2_036_spr_basefill_036'], 'func': spr_base_universe_d3_036_spr_basefill_036}


def spr_base_universe_d3_037_spr_basefill_037(spr_base_universe_d2_037_spr_basefill_037):
    return _base_universe_d3(spr_base_universe_d2_037_spr_basefill_037, 37)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_037_spr_basefill_037'] = {'inputs': ['spr_base_universe_d2_037_spr_basefill_037'], 'func': spr_base_universe_d3_037_spr_basefill_037}


def spr_base_universe_d3_038_spr_basefill_038(spr_base_universe_d2_038_spr_basefill_038):
    return _base_universe_d3(spr_base_universe_d2_038_spr_basefill_038, 38)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_038_spr_basefill_038'] = {'inputs': ['spr_base_universe_d2_038_spr_basefill_038'], 'func': spr_base_universe_d3_038_spr_basefill_038}


def spr_base_universe_d3_039_spr_basefill_039(spr_base_universe_d2_039_spr_basefill_039):
    return _base_universe_d3(spr_base_universe_d2_039_spr_basefill_039, 39)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_039_spr_basefill_039'] = {'inputs': ['spr_base_universe_d2_039_spr_basefill_039'], 'func': spr_base_universe_d3_039_spr_basefill_039}


def spr_base_universe_d3_040_spr_basefill_040(spr_base_universe_d2_040_spr_basefill_040):
    return _base_universe_d3(spr_base_universe_d2_040_spr_basefill_040, 40)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_040_spr_basefill_040'] = {'inputs': ['spr_base_universe_d2_040_spr_basefill_040'], 'func': spr_base_universe_d3_040_spr_basefill_040}


def spr_base_universe_d3_041_spr_basefill_041(spr_base_universe_d2_041_spr_basefill_041):
    return _base_universe_d3(spr_base_universe_d2_041_spr_basefill_041, 41)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_041_spr_basefill_041'] = {'inputs': ['spr_base_universe_d2_041_spr_basefill_041'], 'func': spr_base_universe_d3_041_spr_basefill_041}


def spr_base_universe_d3_042_spr_basefill_042(spr_base_universe_d2_042_spr_basefill_042):
    return _base_universe_d3(spr_base_universe_d2_042_spr_basefill_042, 42)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_042_spr_basefill_042'] = {'inputs': ['spr_base_universe_d2_042_spr_basefill_042'], 'func': spr_base_universe_d3_042_spr_basefill_042}


def spr_base_universe_d3_043_spr_basefill_043(spr_base_universe_d2_043_spr_basefill_043):
    return _base_universe_d3(spr_base_universe_d2_043_spr_basefill_043, 43)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_043_spr_basefill_043'] = {'inputs': ['spr_base_universe_d2_043_spr_basefill_043'], 'func': spr_base_universe_d3_043_spr_basefill_043}


def spr_base_universe_d3_044_spr_basefill_044(spr_base_universe_d2_044_spr_basefill_044):
    return _base_universe_d3(spr_base_universe_d2_044_spr_basefill_044, 44)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_044_spr_basefill_044'] = {'inputs': ['spr_base_universe_d2_044_spr_basefill_044'], 'func': spr_base_universe_d3_044_spr_basefill_044}


def spr_base_universe_d3_045_spr_basefill_045(spr_base_universe_d2_045_spr_basefill_045):
    return _base_universe_d3(spr_base_universe_d2_045_spr_basefill_045, 45)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_045_spr_basefill_045'] = {'inputs': ['spr_base_universe_d2_045_spr_basefill_045'], 'func': spr_base_universe_d3_045_spr_basefill_045}


def spr_base_universe_d3_046_spr_basefill_046(spr_base_universe_d2_046_spr_basefill_046):
    return _base_universe_d3(spr_base_universe_d2_046_spr_basefill_046, 46)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_046_spr_basefill_046'] = {'inputs': ['spr_base_universe_d2_046_spr_basefill_046'], 'func': spr_base_universe_d3_046_spr_basefill_046}


def spr_base_universe_d3_047_spr_basefill_047(spr_base_universe_d2_047_spr_basefill_047):
    return _base_universe_d3(spr_base_universe_d2_047_spr_basefill_047, 47)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_047_spr_basefill_047'] = {'inputs': ['spr_base_universe_d2_047_spr_basefill_047'], 'func': spr_base_universe_d3_047_spr_basefill_047}


def spr_base_universe_d3_048_spr_basefill_048(spr_base_universe_d2_048_spr_basefill_048):
    return _base_universe_d3(spr_base_universe_d2_048_spr_basefill_048, 48)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_048_spr_basefill_048'] = {'inputs': ['spr_base_universe_d2_048_spr_basefill_048'], 'func': spr_base_universe_d3_048_spr_basefill_048}


def spr_base_universe_d3_049_spr_basefill_049(spr_base_universe_d2_049_spr_basefill_049):
    return _base_universe_d3(spr_base_universe_d2_049_spr_basefill_049, 49)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_049_spr_basefill_049'] = {'inputs': ['spr_base_universe_d2_049_spr_basefill_049'], 'func': spr_base_universe_d3_049_spr_basefill_049}


def spr_base_universe_d3_050_spr_basefill_050(spr_base_universe_d2_050_spr_basefill_050):
    return _base_universe_d3(spr_base_universe_d2_050_spr_basefill_050, 50)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_050_spr_basefill_050'] = {'inputs': ['spr_base_universe_d2_050_spr_basefill_050'], 'func': spr_base_universe_d3_050_spr_basefill_050}


def spr_base_universe_d3_051_spr_basefill_051(spr_base_universe_d2_051_spr_basefill_051):
    return _base_universe_d3(spr_base_universe_d2_051_spr_basefill_051, 51)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_051_spr_basefill_051'] = {'inputs': ['spr_base_universe_d2_051_spr_basefill_051'], 'func': spr_base_universe_d3_051_spr_basefill_051}


def spr_base_universe_d3_052_spr_basefill_052(spr_base_universe_d2_052_spr_basefill_052):
    return _base_universe_d3(spr_base_universe_d2_052_spr_basefill_052, 52)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_052_spr_basefill_052'] = {'inputs': ['spr_base_universe_d2_052_spr_basefill_052'], 'func': spr_base_universe_d3_052_spr_basefill_052}


def spr_base_universe_d3_053_spr_basefill_053(spr_base_universe_d2_053_spr_basefill_053):
    return _base_universe_d3(spr_base_universe_d2_053_spr_basefill_053, 53)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_053_spr_basefill_053'] = {'inputs': ['spr_base_universe_d2_053_spr_basefill_053'], 'func': spr_base_universe_d3_053_spr_basefill_053}


def spr_base_universe_d3_054_spr_basefill_054(spr_base_universe_d2_054_spr_basefill_054):
    return _base_universe_d3(spr_base_universe_d2_054_spr_basefill_054, 54)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_054_spr_basefill_054'] = {'inputs': ['spr_base_universe_d2_054_spr_basefill_054'], 'func': spr_base_universe_d3_054_spr_basefill_054}


def spr_base_universe_d3_055_spr_basefill_055(spr_base_universe_d2_055_spr_basefill_055):
    return _base_universe_d3(spr_base_universe_d2_055_spr_basefill_055, 55)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_055_spr_basefill_055'] = {'inputs': ['spr_base_universe_d2_055_spr_basefill_055'], 'func': spr_base_universe_d3_055_spr_basefill_055}


def spr_base_universe_d3_056_spr_basefill_056(spr_base_universe_d2_056_spr_basefill_056):
    return _base_universe_d3(spr_base_universe_d2_056_spr_basefill_056, 56)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_056_spr_basefill_056'] = {'inputs': ['spr_base_universe_d2_056_spr_basefill_056'], 'func': spr_base_universe_d3_056_spr_basefill_056}


def spr_base_universe_d3_057_spr_basefill_057(spr_base_universe_d2_057_spr_basefill_057):
    return _base_universe_d3(spr_base_universe_d2_057_spr_basefill_057, 57)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_057_spr_basefill_057'] = {'inputs': ['spr_base_universe_d2_057_spr_basefill_057'], 'func': spr_base_universe_d3_057_spr_basefill_057}


def spr_base_universe_d3_058_spr_basefill_058(spr_base_universe_d2_058_spr_basefill_058):
    return _base_universe_d3(spr_base_universe_d2_058_spr_basefill_058, 58)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_058_spr_basefill_058'] = {'inputs': ['spr_base_universe_d2_058_spr_basefill_058'], 'func': spr_base_universe_d3_058_spr_basefill_058}


def spr_base_universe_d3_059_spr_basefill_059(spr_base_universe_d2_059_spr_basefill_059):
    return _base_universe_d3(spr_base_universe_d2_059_spr_basefill_059, 59)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_059_spr_basefill_059'] = {'inputs': ['spr_base_universe_d2_059_spr_basefill_059'], 'func': spr_base_universe_d3_059_spr_basefill_059}


def spr_base_universe_d3_060_spr_basefill_060(spr_base_universe_d2_060_spr_basefill_060):
    return _base_universe_d3(spr_base_universe_d2_060_spr_basefill_060, 60)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_060_spr_basefill_060'] = {'inputs': ['spr_base_universe_d2_060_spr_basefill_060'], 'func': spr_base_universe_d3_060_spr_basefill_060}


def spr_base_universe_d3_061_spr_basefill_061(spr_base_universe_d2_061_spr_basefill_061):
    return _base_universe_d3(spr_base_universe_d2_061_spr_basefill_061, 61)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_061_spr_basefill_061'] = {'inputs': ['spr_base_universe_d2_061_spr_basefill_061'], 'func': spr_base_universe_d3_061_spr_basefill_061}


def spr_base_universe_d3_062_spr_basefill_062(spr_base_universe_d2_062_spr_basefill_062):
    return _base_universe_d3(spr_base_universe_d2_062_spr_basefill_062, 62)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_062_spr_basefill_062'] = {'inputs': ['spr_base_universe_d2_062_spr_basefill_062'], 'func': spr_base_universe_d3_062_spr_basefill_062}


def spr_base_universe_d3_063_spr_basefill_063(spr_base_universe_d2_063_spr_basefill_063):
    return _base_universe_d3(spr_base_universe_d2_063_spr_basefill_063, 63)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_063_spr_basefill_063'] = {'inputs': ['spr_base_universe_d2_063_spr_basefill_063'], 'func': spr_base_universe_d3_063_spr_basefill_063}


def spr_base_universe_d3_064_spr_basefill_064(spr_base_universe_d2_064_spr_basefill_064):
    return _base_universe_d3(spr_base_universe_d2_064_spr_basefill_064, 64)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_064_spr_basefill_064'] = {'inputs': ['spr_base_universe_d2_064_spr_basefill_064'], 'func': spr_base_universe_d3_064_spr_basefill_064}


def spr_base_universe_d3_065_spr_basefill_065(spr_base_universe_d2_065_spr_basefill_065):
    return _base_universe_d3(spr_base_universe_d2_065_spr_basefill_065, 65)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_065_spr_basefill_065'] = {'inputs': ['spr_base_universe_d2_065_spr_basefill_065'], 'func': spr_base_universe_d3_065_spr_basefill_065}


def spr_base_universe_d3_066_spr_basefill_066(spr_base_universe_d2_066_spr_basefill_066):
    return _base_universe_d3(spr_base_universe_d2_066_spr_basefill_066, 66)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_066_spr_basefill_066'] = {'inputs': ['spr_base_universe_d2_066_spr_basefill_066'], 'func': spr_base_universe_d3_066_spr_basefill_066}


def spr_base_universe_d3_067_spr_basefill_067(spr_base_universe_d2_067_spr_basefill_067):
    return _base_universe_d3(spr_base_universe_d2_067_spr_basefill_067, 67)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_067_spr_basefill_067'] = {'inputs': ['spr_base_universe_d2_067_spr_basefill_067'], 'func': spr_base_universe_d3_067_spr_basefill_067}


def spr_base_universe_d3_068_spr_basefill_068(spr_base_universe_d2_068_spr_basefill_068):
    return _base_universe_d3(spr_base_universe_d2_068_spr_basefill_068, 68)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_068_spr_basefill_068'] = {'inputs': ['spr_base_universe_d2_068_spr_basefill_068'], 'func': spr_base_universe_d3_068_spr_basefill_068}


def spr_base_universe_d3_069_spr_basefill_069(spr_base_universe_d2_069_spr_basefill_069):
    return _base_universe_d3(spr_base_universe_d2_069_spr_basefill_069, 69)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_069_spr_basefill_069'] = {'inputs': ['spr_base_universe_d2_069_spr_basefill_069'], 'func': spr_base_universe_d3_069_spr_basefill_069}


def spr_base_universe_d3_070_spr_basefill_070(spr_base_universe_d2_070_spr_basefill_070):
    return _base_universe_d3(spr_base_universe_d2_070_spr_basefill_070, 70)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_070_spr_basefill_070'] = {'inputs': ['spr_base_universe_d2_070_spr_basefill_070'], 'func': spr_base_universe_d3_070_spr_basefill_070}


def spr_base_universe_d3_071_spr_basefill_071(spr_base_universe_d2_071_spr_basefill_071):
    return _base_universe_d3(spr_base_universe_d2_071_spr_basefill_071, 71)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_071_spr_basefill_071'] = {'inputs': ['spr_base_universe_d2_071_spr_basefill_071'], 'func': spr_base_universe_d3_071_spr_basefill_071}


def spr_base_universe_d3_072_spr_basefill_072(spr_base_universe_d2_072_spr_basefill_072):
    return _base_universe_d3(spr_base_universe_d2_072_spr_basefill_072, 72)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_072_spr_basefill_072'] = {'inputs': ['spr_base_universe_d2_072_spr_basefill_072'], 'func': spr_base_universe_d3_072_spr_basefill_072}


def spr_base_universe_d3_073_spr_basefill_073(spr_base_universe_d2_073_spr_basefill_073):
    return _base_universe_d3(spr_base_universe_d2_073_spr_basefill_073, 73)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_073_spr_basefill_073'] = {'inputs': ['spr_base_universe_d2_073_spr_basefill_073'], 'func': spr_base_universe_d3_073_spr_basefill_073}


def spr_base_universe_d3_074_spr_basefill_074(spr_base_universe_d2_074_spr_basefill_074):
    return _base_universe_d3(spr_base_universe_d2_074_spr_basefill_074, 74)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_074_spr_basefill_074'] = {'inputs': ['spr_base_universe_d2_074_spr_basefill_074'], 'func': spr_base_universe_d3_074_spr_basefill_074}


def spr_base_universe_d3_075_spr_basefill_075(spr_base_universe_d2_075_spr_basefill_075):
    return _base_universe_d3(spr_base_universe_d2_075_spr_basefill_075, 75)
SPR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['spr_base_universe_d3_075_spr_basefill_075'] = {'inputs': ['spr_base_universe_d2_075_spr_basefill_075'], 'func': spr_base_universe_d3_075_spr_basefill_075}
