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



def idr_001_realized_vol_z_accel_1(idr_001_realized_vol_z_roc_1):
    feature = _s(idr_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def idr_007_realized_vol_z_accel_5(idr_007_realized_vol_z_roc_5):
    feature = _s(idr_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def idr_013_realized_vol_z_accel_42(idr_013_realized_vol_z_roc_42):
    feature = _s(idr_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def idr_179_idr_019_realized_vol_z_42_019_accel_126(idr_154_idr_019_realized_vol_z_42_019_roc_126):
    feature = _s(idr_154_idr_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def idr_180_idr_025_realized_vol_z_378_025_accel_378(idr_155_idr_025_realized_vol_z_378_025_roc_378):
    feature = _s(idr_155_idr_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















INTRADAY_RANGE_REGISTRY_3RD_DERIVATIVES = {
    'idr_001_realized_vol_z_accel_1': {'inputs': ['idr_001_realized_vol_z_roc_1'], 'func': idr_001_realized_vol_z_accel_1},
    'idr_007_realized_vol_z_accel_5': {'inputs': ['idr_007_realized_vol_z_roc_5'], 'func': idr_007_realized_vol_z_accel_5},
    'idr_013_realized_vol_z_accel_42': {'inputs': ['idr_013_realized_vol_z_roc_42'], 'func': idr_013_realized_vol_z_accel_42},
    'idr_179_idr_019_realized_vol_z_42_019_accel_126': {'inputs': ['idr_154_idr_019_realized_vol_z_42_019_roc_126'], 'func': idr_179_idr_019_realized_vol_z_42_019_accel_126},
    'idr_180_idr_025_realized_vol_z_378_025_accel_378': {'inputs': ['idr_155_idr_025_realized_vol_z_378_025_roc_378'], 'func': idr_180_idr_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ir_replacement_d3_001(ir_replacement_d2_001):
    feature = _clean(ir_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_001'] = {'inputs': ['ir_replacement_d2_001'], 'func': ir_replacement_d3_001}


def ir_replacement_d3_002(ir_replacement_d2_002):
    feature = _clean(ir_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_002'] = {'inputs': ['ir_replacement_d2_002'], 'func': ir_replacement_d3_002}


def ir_replacement_d3_003(ir_replacement_d2_003):
    feature = _clean(ir_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_003'] = {'inputs': ['ir_replacement_d2_003'], 'func': ir_replacement_d3_003}


def ir_replacement_d3_004(ir_replacement_d2_004):
    feature = _clean(ir_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_004'] = {'inputs': ['ir_replacement_d2_004'], 'func': ir_replacement_d3_004}


def ir_replacement_d3_005(ir_replacement_d2_005):
    feature = _clean(ir_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_005'] = {'inputs': ['ir_replacement_d2_005'], 'func': ir_replacement_d3_005}


def ir_replacement_d3_006(ir_replacement_d2_006):
    feature = _clean(ir_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_006'] = {'inputs': ['ir_replacement_d2_006'], 'func': ir_replacement_d3_006}


def ir_replacement_d3_007(ir_replacement_d2_007):
    feature = _clean(ir_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_007'] = {'inputs': ['ir_replacement_d2_007'], 'func': ir_replacement_d3_007}


def ir_replacement_d3_008(ir_replacement_d2_008):
    feature = _clean(ir_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_008'] = {'inputs': ['ir_replacement_d2_008'], 'func': ir_replacement_d3_008}


def ir_replacement_d3_009(ir_replacement_d2_009):
    feature = _clean(ir_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_009'] = {'inputs': ['ir_replacement_d2_009'], 'func': ir_replacement_d3_009}


def ir_replacement_d3_010(ir_replacement_d2_010):
    feature = _clean(ir_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_010'] = {'inputs': ['ir_replacement_d2_010'], 'func': ir_replacement_d3_010}


def ir_replacement_d3_011(ir_replacement_d2_011):
    feature = _clean(ir_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_011'] = {'inputs': ['ir_replacement_d2_011'], 'func': ir_replacement_d3_011}


def ir_replacement_d3_012(ir_replacement_d2_012):
    feature = _clean(ir_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_012'] = {'inputs': ['ir_replacement_d2_012'], 'func': ir_replacement_d3_012}


def ir_replacement_d3_013(ir_replacement_d2_013):
    feature = _clean(ir_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_013'] = {'inputs': ['ir_replacement_d2_013'], 'func': ir_replacement_d3_013}


def ir_replacement_d3_014(ir_replacement_d2_014):
    feature = _clean(ir_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_014'] = {'inputs': ['ir_replacement_d2_014'], 'func': ir_replacement_d3_014}


def ir_replacement_d3_015(ir_replacement_d2_015):
    feature = _clean(ir_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_015'] = {'inputs': ['ir_replacement_d2_015'], 'func': ir_replacement_d3_015}


def ir_replacement_d3_016(ir_replacement_d2_016):
    feature = _clean(ir_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_016'] = {'inputs': ['ir_replacement_d2_016'], 'func': ir_replacement_d3_016}


def ir_replacement_d3_017(ir_replacement_d2_017):
    feature = _clean(ir_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_017'] = {'inputs': ['ir_replacement_d2_017'], 'func': ir_replacement_d3_017}


def ir_replacement_d3_018(ir_replacement_d2_018):
    feature = _clean(ir_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_018'] = {'inputs': ['ir_replacement_d2_018'], 'func': ir_replacement_d3_018}


def ir_replacement_d3_019(ir_replacement_d2_019):
    feature = _clean(ir_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_019'] = {'inputs': ['ir_replacement_d2_019'], 'func': ir_replacement_d3_019}


def ir_replacement_d3_020(ir_replacement_d2_020):
    feature = _clean(ir_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_020'] = {'inputs': ['ir_replacement_d2_020'], 'func': ir_replacement_d3_020}


def ir_replacement_d3_021(ir_replacement_d2_021):
    feature = _clean(ir_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_021'] = {'inputs': ['ir_replacement_d2_021'], 'func': ir_replacement_d3_021}


def ir_replacement_d3_022(ir_replacement_d2_022):
    feature = _clean(ir_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_022'] = {'inputs': ['ir_replacement_d2_022'], 'func': ir_replacement_d3_022}


def ir_replacement_d3_023(ir_replacement_d2_023):
    feature = _clean(ir_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_023'] = {'inputs': ['ir_replacement_d2_023'], 'func': ir_replacement_d3_023}


def ir_replacement_d3_024(ir_replacement_d2_024):
    feature = _clean(ir_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_024'] = {'inputs': ['ir_replacement_d2_024'], 'func': ir_replacement_d3_024}


def ir_replacement_d3_025(ir_replacement_d2_025):
    feature = _clean(ir_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_025'] = {'inputs': ['ir_replacement_d2_025'], 'func': ir_replacement_d3_025}


def ir_replacement_d3_026(ir_replacement_d2_026):
    feature = _clean(ir_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_026'] = {'inputs': ['ir_replacement_d2_026'], 'func': ir_replacement_d3_026}


def ir_replacement_d3_027(ir_replacement_d2_027):
    feature = _clean(ir_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_027'] = {'inputs': ['ir_replacement_d2_027'], 'func': ir_replacement_d3_027}


def ir_replacement_d3_028(ir_replacement_d2_028):
    feature = _clean(ir_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_028'] = {'inputs': ['ir_replacement_d2_028'], 'func': ir_replacement_d3_028}


def ir_replacement_d3_029(ir_replacement_d2_029):
    feature = _clean(ir_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_029'] = {'inputs': ['ir_replacement_d2_029'], 'func': ir_replacement_d3_029}


def ir_replacement_d3_030(ir_replacement_d2_030):
    feature = _clean(ir_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_030'] = {'inputs': ['ir_replacement_d2_030'], 'func': ir_replacement_d3_030}


def ir_replacement_d3_031(ir_replacement_d2_031):
    feature = _clean(ir_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_031'] = {'inputs': ['ir_replacement_d2_031'], 'func': ir_replacement_d3_031}


def ir_replacement_d3_032(ir_replacement_d2_032):
    feature = _clean(ir_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_032'] = {'inputs': ['ir_replacement_d2_032'], 'func': ir_replacement_d3_032}


def ir_replacement_d3_033(ir_replacement_d2_033):
    feature = _clean(ir_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_033'] = {'inputs': ['ir_replacement_d2_033'], 'func': ir_replacement_d3_033}


def ir_replacement_d3_034(ir_replacement_d2_034):
    feature = _clean(ir_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_034'] = {'inputs': ['ir_replacement_d2_034'], 'func': ir_replacement_d3_034}


def ir_replacement_d3_035(ir_replacement_d2_035):
    feature = _clean(ir_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_035'] = {'inputs': ['ir_replacement_d2_035'], 'func': ir_replacement_d3_035}


def ir_replacement_d3_036(ir_replacement_d2_036):
    feature = _clean(ir_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_036'] = {'inputs': ['ir_replacement_d2_036'], 'func': ir_replacement_d3_036}


def ir_replacement_d3_037(ir_replacement_d2_037):
    feature = _clean(ir_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_037'] = {'inputs': ['ir_replacement_d2_037'], 'func': ir_replacement_d3_037}


def ir_replacement_d3_038(ir_replacement_d2_038):
    feature = _clean(ir_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_038'] = {'inputs': ['ir_replacement_d2_038'], 'func': ir_replacement_d3_038}


def ir_replacement_d3_039(ir_replacement_d2_039):
    feature = _clean(ir_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_039'] = {'inputs': ['ir_replacement_d2_039'], 'func': ir_replacement_d3_039}


def ir_replacement_d3_040(ir_replacement_d2_040):
    feature = _clean(ir_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_040'] = {'inputs': ['ir_replacement_d2_040'], 'func': ir_replacement_d3_040}


def ir_replacement_d3_041(ir_replacement_d2_041):
    feature = _clean(ir_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_041'] = {'inputs': ['ir_replacement_d2_041'], 'func': ir_replacement_d3_041}


def ir_replacement_d3_042(ir_replacement_d2_042):
    feature = _clean(ir_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_042'] = {'inputs': ['ir_replacement_d2_042'], 'func': ir_replacement_d3_042}


def ir_replacement_d3_043(ir_replacement_d2_043):
    feature = _clean(ir_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_043'] = {'inputs': ['ir_replacement_d2_043'], 'func': ir_replacement_d3_043}


def ir_replacement_d3_044(ir_replacement_d2_044):
    feature = _clean(ir_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_044'] = {'inputs': ['ir_replacement_d2_044'], 'func': ir_replacement_d3_044}


def ir_replacement_d3_045(ir_replacement_d2_045):
    feature = _clean(ir_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_045'] = {'inputs': ['ir_replacement_d2_045'], 'func': ir_replacement_d3_045}


def ir_replacement_d3_046(ir_replacement_d2_046):
    feature = _clean(ir_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_046'] = {'inputs': ['ir_replacement_d2_046'], 'func': ir_replacement_d3_046}


def ir_replacement_d3_047(ir_replacement_d2_047):
    feature = _clean(ir_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_047'] = {'inputs': ['ir_replacement_d2_047'], 'func': ir_replacement_d3_047}


def ir_replacement_d3_048(ir_replacement_d2_048):
    feature = _clean(ir_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_048'] = {'inputs': ['ir_replacement_d2_048'], 'func': ir_replacement_d3_048}


def ir_replacement_d3_049(ir_replacement_d2_049):
    feature = _clean(ir_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_049'] = {'inputs': ['ir_replacement_d2_049'], 'func': ir_replacement_d3_049}


def ir_replacement_d3_050(ir_replacement_d2_050):
    feature = _clean(ir_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_050'] = {'inputs': ['ir_replacement_d2_050'], 'func': ir_replacement_d3_050}


def ir_replacement_d3_051(ir_replacement_d2_051):
    feature = _clean(ir_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_051'] = {'inputs': ['ir_replacement_d2_051'], 'func': ir_replacement_d3_051}


def ir_replacement_d3_052(ir_replacement_d2_052):
    feature = _clean(ir_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_052'] = {'inputs': ['ir_replacement_d2_052'], 'func': ir_replacement_d3_052}


def ir_replacement_d3_053(ir_replacement_d2_053):
    feature = _clean(ir_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_053'] = {'inputs': ['ir_replacement_d2_053'], 'func': ir_replacement_d3_053}


def ir_replacement_d3_054(ir_replacement_d2_054):
    feature = _clean(ir_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_054'] = {'inputs': ['ir_replacement_d2_054'], 'func': ir_replacement_d3_054}


def ir_replacement_d3_055(ir_replacement_d2_055):
    feature = _clean(ir_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_055'] = {'inputs': ['ir_replacement_d2_055'], 'func': ir_replacement_d3_055}


def ir_replacement_d3_056(ir_replacement_d2_056):
    feature = _clean(ir_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_056'] = {'inputs': ['ir_replacement_d2_056'], 'func': ir_replacement_d3_056}


def ir_replacement_d3_057(ir_replacement_d2_057):
    feature = _clean(ir_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_057'] = {'inputs': ['ir_replacement_d2_057'], 'func': ir_replacement_d3_057}


def ir_replacement_d3_058(ir_replacement_d2_058):
    feature = _clean(ir_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_058'] = {'inputs': ['ir_replacement_d2_058'], 'func': ir_replacement_d3_058}


def ir_replacement_d3_059(ir_replacement_d2_059):
    feature = _clean(ir_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_059'] = {'inputs': ['ir_replacement_d2_059'], 'func': ir_replacement_d3_059}


def ir_replacement_d3_060(ir_replacement_d2_060):
    feature = _clean(ir_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_060'] = {'inputs': ['ir_replacement_d2_060'], 'func': ir_replacement_d3_060}


def ir_replacement_d3_061(ir_replacement_d2_061):
    feature = _clean(ir_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_061'] = {'inputs': ['ir_replacement_d2_061'], 'func': ir_replacement_d3_061}


def ir_replacement_d3_062(ir_replacement_d2_062):
    feature = _clean(ir_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_062'] = {'inputs': ['ir_replacement_d2_062'], 'func': ir_replacement_d3_062}


def ir_replacement_d3_063(ir_replacement_d2_063):
    feature = _clean(ir_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_063'] = {'inputs': ['ir_replacement_d2_063'], 'func': ir_replacement_d3_063}


def ir_replacement_d3_064(ir_replacement_d2_064):
    feature = _clean(ir_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_064'] = {'inputs': ['ir_replacement_d2_064'], 'func': ir_replacement_d3_064}


def ir_replacement_d3_065(ir_replacement_d2_065):
    feature = _clean(ir_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_065'] = {'inputs': ['ir_replacement_d2_065'], 'func': ir_replacement_d3_065}


def ir_replacement_d3_066(ir_replacement_d2_066):
    feature = _clean(ir_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_066'] = {'inputs': ['ir_replacement_d2_066'], 'func': ir_replacement_d3_066}


def ir_replacement_d3_067(ir_replacement_d2_067):
    feature = _clean(ir_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_067'] = {'inputs': ['ir_replacement_d2_067'], 'func': ir_replacement_d3_067}


def ir_replacement_d3_068(ir_replacement_d2_068):
    feature = _clean(ir_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_068'] = {'inputs': ['ir_replacement_d2_068'], 'func': ir_replacement_d3_068}


def ir_replacement_d3_069(ir_replacement_d2_069):
    feature = _clean(ir_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_069'] = {'inputs': ['ir_replacement_d2_069'], 'func': ir_replacement_d3_069}


def ir_replacement_d3_070(ir_replacement_d2_070):
    feature = _clean(ir_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_070'] = {'inputs': ['ir_replacement_d2_070'], 'func': ir_replacement_d3_070}


def ir_replacement_d3_071(ir_replacement_d2_071):
    feature = _clean(ir_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_071'] = {'inputs': ['ir_replacement_d2_071'], 'func': ir_replacement_d3_071}


def ir_replacement_d3_072(ir_replacement_d2_072):
    feature = _clean(ir_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_072'] = {'inputs': ['ir_replacement_d2_072'], 'func': ir_replacement_d3_072}


def ir_replacement_d3_073(ir_replacement_d2_073):
    feature = _clean(ir_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_073'] = {'inputs': ['ir_replacement_d2_073'], 'func': ir_replacement_d3_073}


def ir_replacement_d3_074(ir_replacement_d2_074):
    feature = _clean(ir_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_074'] = {'inputs': ['ir_replacement_d2_074'], 'func': ir_replacement_d3_074}


def ir_replacement_d3_075(ir_replacement_d2_075):
    feature = _clean(ir_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_075'] = {'inputs': ['ir_replacement_d2_075'], 'func': ir_replacement_d3_075}


def ir_replacement_d3_076(ir_replacement_d2_076):
    feature = _clean(ir_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_076'] = {'inputs': ['ir_replacement_d2_076'], 'func': ir_replacement_d3_076}


def ir_replacement_d3_077(ir_replacement_d2_077):
    feature = _clean(ir_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_077'] = {'inputs': ['ir_replacement_d2_077'], 'func': ir_replacement_d3_077}


def ir_replacement_d3_078(ir_replacement_d2_078):
    feature = _clean(ir_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_078'] = {'inputs': ['ir_replacement_d2_078'], 'func': ir_replacement_d3_078}


def ir_replacement_d3_079(ir_replacement_d2_079):
    feature = _clean(ir_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_079'] = {'inputs': ['ir_replacement_d2_079'], 'func': ir_replacement_d3_079}


def ir_replacement_d3_080(ir_replacement_d2_080):
    feature = _clean(ir_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_080'] = {'inputs': ['ir_replacement_d2_080'], 'func': ir_replacement_d3_080}


def ir_replacement_d3_081(ir_replacement_d2_081):
    feature = _clean(ir_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_081'] = {'inputs': ['ir_replacement_d2_081'], 'func': ir_replacement_d3_081}


def ir_replacement_d3_082(ir_replacement_d2_082):
    feature = _clean(ir_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_082'] = {'inputs': ['ir_replacement_d2_082'], 'func': ir_replacement_d3_082}


def ir_replacement_d3_083(ir_replacement_d2_083):
    feature = _clean(ir_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_083'] = {'inputs': ['ir_replacement_d2_083'], 'func': ir_replacement_d3_083}


def ir_replacement_d3_084(ir_replacement_d2_084):
    feature = _clean(ir_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_084'] = {'inputs': ['ir_replacement_d2_084'], 'func': ir_replacement_d3_084}


def ir_replacement_d3_085(ir_replacement_d2_085):
    feature = _clean(ir_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_085'] = {'inputs': ['ir_replacement_d2_085'], 'func': ir_replacement_d3_085}


def ir_replacement_d3_086(ir_replacement_d2_086):
    feature = _clean(ir_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_086'] = {'inputs': ['ir_replacement_d2_086'], 'func': ir_replacement_d3_086}


def ir_replacement_d3_087(ir_replacement_d2_087):
    feature = _clean(ir_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_087'] = {'inputs': ['ir_replacement_d2_087'], 'func': ir_replacement_d3_087}


def ir_replacement_d3_088(ir_replacement_d2_088):
    feature = _clean(ir_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_088'] = {'inputs': ['ir_replacement_d2_088'], 'func': ir_replacement_d3_088}


def ir_replacement_d3_089(ir_replacement_d2_089):
    feature = _clean(ir_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_089'] = {'inputs': ['ir_replacement_d2_089'], 'func': ir_replacement_d3_089}


def ir_replacement_d3_090(ir_replacement_d2_090):
    feature = _clean(ir_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_090'] = {'inputs': ['ir_replacement_d2_090'], 'func': ir_replacement_d3_090}


def ir_replacement_d3_091(ir_replacement_d2_091):
    feature = _clean(ir_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_091'] = {'inputs': ['ir_replacement_d2_091'], 'func': ir_replacement_d3_091}


def ir_replacement_d3_092(ir_replacement_d2_092):
    feature = _clean(ir_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_092'] = {'inputs': ['ir_replacement_d2_092'], 'func': ir_replacement_d3_092}


def ir_replacement_d3_093(ir_replacement_d2_093):
    feature = _clean(ir_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_093'] = {'inputs': ['ir_replacement_d2_093'], 'func': ir_replacement_d3_093}


def ir_replacement_d3_094(ir_replacement_d2_094):
    feature = _clean(ir_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_094'] = {'inputs': ['ir_replacement_d2_094'], 'func': ir_replacement_d3_094}


def ir_replacement_d3_095(ir_replacement_d2_095):
    feature = _clean(ir_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_095'] = {'inputs': ['ir_replacement_d2_095'], 'func': ir_replacement_d3_095}


def ir_replacement_d3_096(ir_replacement_d2_096):
    feature = _clean(ir_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_096'] = {'inputs': ['ir_replacement_d2_096'], 'func': ir_replacement_d3_096}


def ir_replacement_d3_097(ir_replacement_d2_097):
    feature = _clean(ir_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_097'] = {'inputs': ['ir_replacement_d2_097'], 'func': ir_replacement_d3_097}


def ir_replacement_d3_098(ir_replacement_d2_098):
    feature = _clean(ir_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_098'] = {'inputs': ['ir_replacement_d2_098'], 'func': ir_replacement_d3_098}


def ir_replacement_d3_099(ir_replacement_d2_099):
    feature = _clean(ir_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_099'] = {'inputs': ['ir_replacement_d2_099'], 'func': ir_replacement_d3_099}


def ir_replacement_d3_100(ir_replacement_d2_100):
    feature = _clean(ir_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_100'] = {'inputs': ['ir_replacement_d2_100'], 'func': ir_replacement_d3_100}


def ir_replacement_d3_101(ir_replacement_d2_101):
    feature = _clean(ir_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_101'] = {'inputs': ['ir_replacement_d2_101'], 'func': ir_replacement_d3_101}


def ir_replacement_d3_102(ir_replacement_d2_102):
    feature = _clean(ir_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_102'] = {'inputs': ['ir_replacement_d2_102'], 'func': ir_replacement_d3_102}


def ir_replacement_d3_103(ir_replacement_d2_103):
    feature = _clean(ir_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_103'] = {'inputs': ['ir_replacement_d2_103'], 'func': ir_replacement_d3_103}


def ir_replacement_d3_104(ir_replacement_d2_104):
    feature = _clean(ir_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_104'] = {'inputs': ['ir_replacement_d2_104'], 'func': ir_replacement_d3_104}


def ir_replacement_d3_105(ir_replacement_d2_105):
    feature = _clean(ir_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_105'] = {'inputs': ['ir_replacement_d2_105'], 'func': ir_replacement_d3_105}


def ir_replacement_d3_106(ir_replacement_d2_106):
    feature = _clean(ir_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_106'] = {'inputs': ['ir_replacement_d2_106'], 'func': ir_replacement_d3_106}


def ir_replacement_d3_107(ir_replacement_d2_107):
    feature = _clean(ir_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_107'] = {'inputs': ['ir_replacement_d2_107'], 'func': ir_replacement_d3_107}


def ir_replacement_d3_108(ir_replacement_d2_108):
    feature = _clean(ir_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_108'] = {'inputs': ['ir_replacement_d2_108'], 'func': ir_replacement_d3_108}


def ir_replacement_d3_109(ir_replacement_d2_109):
    feature = _clean(ir_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_109'] = {'inputs': ['ir_replacement_d2_109'], 'func': ir_replacement_d3_109}


def ir_replacement_d3_110(ir_replacement_d2_110):
    feature = _clean(ir_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_110'] = {'inputs': ['ir_replacement_d2_110'], 'func': ir_replacement_d3_110}


def ir_replacement_d3_111(ir_replacement_d2_111):
    feature = _clean(ir_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_111'] = {'inputs': ['ir_replacement_d2_111'], 'func': ir_replacement_d3_111}


def ir_replacement_d3_112(ir_replacement_d2_112):
    feature = _clean(ir_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_112'] = {'inputs': ['ir_replacement_d2_112'], 'func': ir_replacement_d3_112}


def ir_replacement_d3_113(ir_replacement_d2_113):
    feature = _clean(ir_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_113'] = {'inputs': ['ir_replacement_d2_113'], 'func': ir_replacement_d3_113}


def ir_replacement_d3_114(ir_replacement_d2_114):
    feature = _clean(ir_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_114'] = {'inputs': ['ir_replacement_d2_114'], 'func': ir_replacement_d3_114}


def ir_replacement_d3_115(ir_replacement_d2_115):
    feature = _clean(ir_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_115'] = {'inputs': ['ir_replacement_d2_115'], 'func': ir_replacement_d3_115}


def ir_replacement_d3_116(ir_replacement_d2_116):
    feature = _clean(ir_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_116'] = {'inputs': ['ir_replacement_d2_116'], 'func': ir_replacement_d3_116}


def ir_replacement_d3_117(ir_replacement_d2_117):
    feature = _clean(ir_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_117'] = {'inputs': ['ir_replacement_d2_117'], 'func': ir_replacement_d3_117}


def ir_replacement_d3_118(ir_replacement_d2_118):
    feature = _clean(ir_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_118'] = {'inputs': ['ir_replacement_d2_118'], 'func': ir_replacement_d3_118}


def ir_replacement_d3_119(ir_replacement_d2_119):
    feature = _clean(ir_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_119'] = {'inputs': ['ir_replacement_d2_119'], 'func': ir_replacement_d3_119}


def ir_replacement_d3_120(ir_replacement_d2_120):
    feature = _clean(ir_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_120'] = {'inputs': ['ir_replacement_d2_120'], 'func': ir_replacement_d3_120}


def ir_replacement_d3_121(ir_replacement_d2_121):
    feature = _clean(ir_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_121'] = {'inputs': ['ir_replacement_d2_121'], 'func': ir_replacement_d3_121}


def ir_replacement_d3_122(ir_replacement_d2_122):
    feature = _clean(ir_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_122'] = {'inputs': ['ir_replacement_d2_122'], 'func': ir_replacement_d3_122}


def ir_replacement_d3_123(ir_replacement_d2_123):
    feature = _clean(ir_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_123'] = {'inputs': ['ir_replacement_d2_123'], 'func': ir_replacement_d3_123}


def ir_replacement_d3_124(ir_replacement_d2_124):
    feature = _clean(ir_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_124'] = {'inputs': ['ir_replacement_d2_124'], 'func': ir_replacement_d3_124}


def ir_replacement_d3_125(ir_replacement_d2_125):
    feature = _clean(ir_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_125'] = {'inputs': ['ir_replacement_d2_125'], 'func': ir_replacement_d3_125}


def ir_replacement_d3_126(ir_replacement_d2_126):
    feature = _clean(ir_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_126'] = {'inputs': ['ir_replacement_d2_126'], 'func': ir_replacement_d3_126}


def ir_replacement_d3_127(ir_replacement_d2_127):
    feature = _clean(ir_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_127'] = {'inputs': ['ir_replacement_d2_127'], 'func': ir_replacement_d3_127}


def ir_replacement_d3_128(ir_replacement_d2_128):
    feature = _clean(ir_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_128'] = {'inputs': ['ir_replacement_d2_128'], 'func': ir_replacement_d3_128}


def ir_replacement_d3_129(ir_replacement_d2_129):
    feature = _clean(ir_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_129'] = {'inputs': ['ir_replacement_d2_129'], 'func': ir_replacement_d3_129}


def ir_replacement_d3_130(ir_replacement_d2_130):
    feature = _clean(ir_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_130'] = {'inputs': ['ir_replacement_d2_130'], 'func': ir_replacement_d3_130}


def ir_replacement_d3_131(ir_replacement_d2_131):
    feature = _clean(ir_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_131'] = {'inputs': ['ir_replacement_d2_131'], 'func': ir_replacement_d3_131}


def ir_replacement_d3_132(ir_replacement_d2_132):
    feature = _clean(ir_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_132'] = {'inputs': ['ir_replacement_d2_132'], 'func': ir_replacement_d3_132}


def ir_replacement_d3_133(ir_replacement_d2_133):
    feature = _clean(ir_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_133'] = {'inputs': ['ir_replacement_d2_133'], 'func': ir_replacement_d3_133}


def ir_replacement_d3_134(ir_replacement_d2_134):
    feature = _clean(ir_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_134'] = {'inputs': ['ir_replacement_d2_134'], 'func': ir_replacement_d3_134}


def ir_replacement_d3_135(ir_replacement_d2_135):
    feature = _clean(ir_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_135'] = {'inputs': ['ir_replacement_d2_135'], 'func': ir_replacement_d3_135}


def ir_replacement_d3_136(ir_replacement_d2_136):
    feature = _clean(ir_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_136'] = {'inputs': ['ir_replacement_d2_136'], 'func': ir_replacement_d3_136}


def ir_replacement_d3_137(ir_replacement_d2_137):
    feature = _clean(ir_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_137'] = {'inputs': ['ir_replacement_d2_137'], 'func': ir_replacement_d3_137}


def ir_replacement_d3_138(ir_replacement_d2_138):
    feature = _clean(ir_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_138'] = {'inputs': ['ir_replacement_d2_138'], 'func': ir_replacement_d3_138}


def ir_replacement_d3_139(ir_replacement_d2_139):
    feature = _clean(ir_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_139'] = {'inputs': ['ir_replacement_d2_139'], 'func': ir_replacement_d3_139}


def ir_replacement_d3_140(ir_replacement_d2_140):
    feature = _clean(ir_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_140'] = {'inputs': ['ir_replacement_d2_140'], 'func': ir_replacement_d3_140}


def ir_replacement_d3_141(ir_replacement_d2_141):
    feature = _clean(ir_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_141'] = {'inputs': ['ir_replacement_d2_141'], 'func': ir_replacement_d3_141}


def ir_replacement_d3_142(ir_replacement_d2_142):
    feature = _clean(ir_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_142'] = {'inputs': ['ir_replacement_d2_142'], 'func': ir_replacement_d3_142}


def ir_replacement_d3_143(ir_replacement_d2_143):
    feature = _clean(ir_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_143'] = {'inputs': ['ir_replacement_d2_143'], 'func': ir_replacement_d3_143}


def ir_replacement_d3_144(ir_replacement_d2_144):
    feature = _clean(ir_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_144'] = {'inputs': ['ir_replacement_d2_144'], 'func': ir_replacement_d3_144}


def ir_replacement_d3_145(ir_replacement_d2_145):
    feature = _clean(ir_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_145'] = {'inputs': ['ir_replacement_d2_145'], 'func': ir_replacement_d3_145}


def ir_replacement_d3_146(ir_replacement_d2_146):
    feature = _clean(ir_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_146'] = {'inputs': ['ir_replacement_d2_146'], 'func': ir_replacement_d3_146}


def ir_replacement_d3_147(ir_replacement_d2_147):
    feature = _clean(ir_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_147'] = {'inputs': ['ir_replacement_d2_147'], 'func': ir_replacement_d3_147}


def ir_replacement_d3_148(ir_replacement_d2_148):
    feature = _clean(ir_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_148'] = {'inputs': ['ir_replacement_d2_148'], 'func': ir_replacement_d3_148}


def ir_replacement_d3_149(ir_replacement_d2_149):
    feature = _clean(ir_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_149'] = {'inputs': ['ir_replacement_d2_149'], 'func': ir_replacement_d3_149}


def ir_replacement_d3_150(ir_replacement_d2_150):
    feature = _clean(ir_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_150'] = {'inputs': ['ir_replacement_d2_150'], 'func': ir_replacement_d3_150}


def ir_replacement_d3_151(ir_replacement_d2_151):
    feature = _clean(ir_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_151'] = {'inputs': ['ir_replacement_d2_151'], 'func': ir_replacement_d3_151}


def ir_replacement_d3_152(ir_replacement_d2_152):
    feature = _clean(ir_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_152'] = {'inputs': ['ir_replacement_d2_152'], 'func': ir_replacement_d3_152}


def ir_replacement_d3_153(ir_replacement_d2_153):
    feature = _clean(ir_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_153'] = {'inputs': ['ir_replacement_d2_153'], 'func': ir_replacement_d3_153}


def ir_replacement_d3_154(ir_replacement_d2_154):
    feature = _clean(ir_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_154'] = {'inputs': ['ir_replacement_d2_154'], 'func': ir_replacement_d3_154}


def ir_replacement_d3_155(ir_replacement_d2_155):
    feature = _clean(ir_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_155'] = {'inputs': ['ir_replacement_d2_155'], 'func': ir_replacement_d3_155}


def ir_replacement_d3_156(ir_replacement_d2_156):
    feature = _clean(ir_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_156'] = {'inputs': ['ir_replacement_d2_156'], 'func': ir_replacement_d3_156}


def ir_replacement_d3_157(ir_replacement_d2_157):
    feature = _clean(ir_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_157'] = {'inputs': ['ir_replacement_d2_157'], 'func': ir_replacement_d3_157}


def ir_replacement_d3_158(ir_replacement_d2_158):
    feature = _clean(ir_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_158'] = {'inputs': ['ir_replacement_d2_158'], 'func': ir_replacement_d3_158}


def ir_replacement_d3_159(ir_replacement_d2_159):
    feature = _clean(ir_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_159'] = {'inputs': ['ir_replacement_d2_159'], 'func': ir_replacement_d3_159}


def ir_replacement_d3_160(ir_replacement_d2_160):
    feature = _clean(ir_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_160'] = {'inputs': ['ir_replacement_d2_160'], 'func': ir_replacement_d3_160}


def ir_replacement_d3_161(ir_replacement_d2_161):
    feature = _clean(ir_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_161'] = {'inputs': ['ir_replacement_d2_161'], 'func': ir_replacement_d3_161}


def ir_replacement_d3_162(ir_replacement_d2_162):
    feature = _clean(ir_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_162'] = {'inputs': ['ir_replacement_d2_162'], 'func': ir_replacement_d3_162}


def ir_replacement_d3_163(ir_replacement_d2_163):
    feature = _clean(ir_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_163'] = {'inputs': ['ir_replacement_d2_163'], 'func': ir_replacement_d3_163}


def ir_replacement_d3_164(ir_replacement_d2_164):
    feature = _clean(ir_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_164'] = {'inputs': ['ir_replacement_d2_164'], 'func': ir_replacement_d3_164}


def ir_replacement_d3_165(ir_replacement_d2_165):
    feature = _clean(ir_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_165'] = {'inputs': ['ir_replacement_d2_165'], 'func': ir_replacement_d3_165}


def ir_replacement_d3_166(ir_replacement_d2_166):
    feature = _clean(ir_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_166'] = {'inputs': ['ir_replacement_d2_166'], 'func': ir_replacement_d3_166}


def ir_replacement_d3_167(ir_replacement_d2_167):
    feature = _clean(ir_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_167'] = {'inputs': ['ir_replacement_d2_167'], 'func': ir_replacement_d3_167}


def ir_replacement_d3_168(ir_replacement_d2_168):
    feature = _clean(ir_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_168'] = {'inputs': ['ir_replacement_d2_168'], 'func': ir_replacement_d3_168}


def ir_replacement_d3_169(ir_replacement_d2_169):
    feature = _clean(ir_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_169'] = {'inputs': ['ir_replacement_d2_169'], 'func': ir_replacement_d3_169}


def ir_replacement_d3_170(ir_replacement_d2_170):
    feature = _clean(ir_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_170'] = {'inputs': ['ir_replacement_d2_170'], 'func': ir_replacement_d3_170}


def ir_replacement_d3_171(ir_replacement_d2_171):
    feature = _clean(ir_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_171'] = {'inputs': ['ir_replacement_d2_171'], 'func': ir_replacement_d3_171}


def ir_replacement_d3_172(ir_replacement_d2_172):
    feature = _clean(ir_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_172'] = {'inputs': ['ir_replacement_d2_172'], 'func': ir_replacement_d3_172}


def ir_replacement_d3_173(ir_replacement_d2_173):
    feature = _clean(ir_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_173'] = {'inputs': ['ir_replacement_d2_173'], 'func': ir_replacement_d3_173}


def ir_replacement_d3_174(ir_replacement_d2_174):
    feature = _clean(ir_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_174'] = {'inputs': ['ir_replacement_d2_174'], 'func': ir_replacement_d3_174}


def ir_replacement_d3_175(ir_replacement_d2_175):
    feature = _clean(ir_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
IR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ir_replacement_d3_175'] = {'inputs': ['ir_replacement_d2_175'], 'func': ir_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def idr_base_universe_d3_001_idr_002_range_expansion_10_002(idr_base_universe_d2_001_idr_002_range_expansion_10_002):
    return _base_universe_d3(idr_base_universe_d2_001_idr_002_range_expansion_10_002, 1)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_001_idr_002_range_expansion_10_002'] = {'inputs': ['idr_base_universe_d2_001_idr_002_range_expansion_10_002'], 'func': idr_base_universe_d3_001_idr_002_range_expansion_10_002}


def idr_base_universe_d3_002_idr_004_close_location_42_004(idr_base_universe_d2_002_idr_004_close_location_42_004):
    return _base_universe_d3(idr_base_universe_d2_002_idr_004_close_location_42_004, 2)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_002_idr_004_close_location_42_004'] = {'inputs': ['idr_base_universe_d2_002_idr_004_close_location_42_004'], 'func': idr_base_universe_d3_002_idr_004_close_location_42_004}


def idr_base_universe_d3_003_idr_005_atr_move_63_005(idr_base_universe_d2_003_idr_005_atr_move_63_005):
    return _base_universe_d3(idr_base_universe_d2_003_idr_005_atr_move_63_005, 3)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_003_idr_005_atr_move_63_005'] = {'inputs': ['idr_base_universe_d2_003_idr_005_atr_move_63_005'], 'func': idr_base_universe_d3_003_idr_005_atr_move_63_005}


def idr_base_universe_d3_004_idr_008_range_expansion_189_008(idr_base_universe_d2_004_idr_008_range_expansion_189_008):
    return _base_universe_d3(idr_base_universe_d2_004_idr_008_range_expansion_189_008, 4)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_004_idr_008_range_expansion_189_008'] = {'inputs': ['idr_base_universe_d2_004_idr_008_range_expansion_189_008'], 'func': idr_base_universe_d3_004_idr_008_range_expansion_189_008}


def idr_base_universe_d3_005_idr_010_close_location_378_010(idr_base_universe_d2_005_idr_010_close_location_378_010):
    return _base_universe_d3(idr_base_universe_d2_005_idr_010_close_location_378_010, 5)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_005_idr_010_close_location_378_010'] = {'inputs': ['idr_base_universe_d2_005_idr_010_close_location_378_010'], 'func': idr_base_universe_d3_005_idr_010_close_location_378_010}


def idr_base_universe_d3_006_idr_011_atr_move_504_011(idr_base_universe_d2_006_idr_011_atr_move_504_011):
    return _base_universe_d3(idr_base_universe_d2_006_idr_011_atr_move_504_011, 6)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_006_idr_011_atr_move_504_011'] = {'inputs': ['idr_base_universe_d2_006_idr_011_atr_move_504_011'], 'func': idr_base_universe_d3_006_idr_011_atr_move_504_011}


def idr_base_universe_d3_007_idr_014_range_expansion_1260_014(idr_base_universe_d2_007_idr_014_range_expansion_1260_014):
    return _base_universe_d3(idr_base_universe_d2_007_idr_014_range_expansion_1260_014, 7)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_007_idr_014_range_expansion_1260_014'] = {'inputs': ['idr_base_universe_d2_007_idr_014_range_expansion_1260_014'], 'func': idr_base_universe_d3_007_idr_014_range_expansion_1260_014}


def idr_base_universe_d3_008_idr_016_close_location_5_016(idr_base_universe_d2_008_idr_016_close_location_5_016):
    return _base_universe_d3(idr_base_universe_d2_008_idr_016_close_location_5_016, 8)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_008_idr_016_close_location_5_016'] = {'inputs': ['idr_base_universe_d2_008_idr_016_close_location_5_016'], 'func': idr_base_universe_d3_008_idr_016_close_location_5_016}


def idr_base_universe_d3_009_idr_017_atr_move_10_017(idr_base_universe_d2_009_idr_017_atr_move_10_017):
    return _base_universe_d3(idr_base_universe_d2_009_idr_017_atr_move_10_017, 9)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_009_idr_017_atr_move_10_017'] = {'inputs': ['idr_base_universe_d2_009_idr_017_atr_move_10_017'], 'func': idr_base_universe_d3_009_idr_017_atr_move_10_017}


def idr_base_universe_d3_010_idr_020_range_expansion_63_020(idr_base_universe_d2_010_idr_020_range_expansion_63_020):
    return _base_universe_d3(idr_base_universe_d2_010_idr_020_range_expansion_63_020, 10)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_010_idr_020_range_expansion_63_020'] = {'inputs': ['idr_base_universe_d2_010_idr_020_range_expansion_63_020'], 'func': idr_base_universe_d3_010_idr_020_range_expansion_63_020}


def idr_base_universe_d3_011_idr_022_close_location_126_022(idr_base_universe_d2_011_idr_022_close_location_126_022):
    return _base_universe_d3(idr_base_universe_d2_011_idr_022_close_location_126_022, 11)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_011_idr_022_close_location_126_022'] = {'inputs': ['idr_base_universe_d2_011_idr_022_close_location_126_022'], 'func': idr_base_universe_d3_011_idr_022_close_location_126_022}


def idr_base_universe_d3_012_idr_023_atr_move_189_023(idr_base_universe_d2_012_idr_023_atr_move_189_023):
    return _base_universe_d3(idr_base_universe_d2_012_idr_023_atr_move_189_023, 12)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_012_idr_023_atr_move_189_023'] = {'inputs': ['idr_base_universe_d2_012_idr_023_atr_move_189_023'], 'func': idr_base_universe_d3_012_idr_023_atr_move_189_023}


def idr_base_universe_d3_013_idr_026_range_expansion_504_026(idr_base_universe_d2_013_idr_026_range_expansion_504_026):
    return _base_universe_d3(idr_base_universe_d2_013_idr_026_range_expansion_504_026, 13)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_013_idr_026_range_expansion_504_026'] = {'inputs': ['idr_base_universe_d2_013_idr_026_range_expansion_504_026'], 'func': idr_base_universe_d3_013_idr_026_range_expansion_504_026}


def idr_base_universe_d3_014_idr_028_close_location_1008_028(idr_base_universe_d2_014_idr_028_close_location_1008_028):
    return _base_universe_d3(idr_base_universe_d2_014_idr_028_close_location_1008_028, 14)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_014_idr_028_close_location_1008_028'] = {'inputs': ['idr_base_universe_d2_014_idr_028_close_location_1008_028'], 'func': idr_base_universe_d3_014_idr_028_close_location_1008_028}


def idr_base_universe_d3_015_idr_029_atr_move_1260_029(idr_base_universe_d2_015_idr_029_atr_move_1260_029):
    return _base_universe_d3(idr_base_universe_d2_015_idr_029_atr_move_1260_029, 15)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_015_idr_029_atr_move_1260_029'] = {'inputs': ['idr_base_universe_d2_015_idr_029_atr_move_1260_029'], 'func': idr_base_universe_d3_015_idr_029_atr_move_1260_029}


def idr_base_universe_d3_016_idr_basefill_001(idr_base_universe_d2_016_idr_basefill_001):
    return _base_universe_d3(idr_base_universe_d2_016_idr_basefill_001, 16)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_016_idr_basefill_001'] = {'inputs': ['idr_base_universe_d2_016_idr_basefill_001'], 'func': idr_base_universe_d3_016_idr_basefill_001}


def idr_base_universe_d3_017_idr_basefill_003(idr_base_universe_d2_017_idr_basefill_003):
    return _base_universe_d3(idr_base_universe_d2_017_idr_basefill_003, 17)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_017_idr_basefill_003'] = {'inputs': ['idr_base_universe_d2_017_idr_basefill_003'], 'func': idr_base_universe_d3_017_idr_basefill_003}


def idr_base_universe_d3_018_idr_basefill_006(idr_base_universe_d2_018_idr_basefill_006):
    return _base_universe_d3(idr_base_universe_d2_018_idr_basefill_006, 18)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_018_idr_basefill_006'] = {'inputs': ['idr_base_universe_d2_018_idr_basefill_006'], 'func': idr_base_universe_d3_018_idr_basefill_006}


def idr_base_universe_d3_019_idr_basefill_007(idr_base_universe_d2_019_idr_basefill_007):
    return _base_universe_d3(idr_base_universe_d2_019_idr_basefill_007, 19)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_019_idr_basefill_007'] = {'inputs': ['idr_base_universe_d2_019_idr_basefill_007'], 'func': idr_base_universe_d3_019_idr_basefill_007}


def idr_base_universe_d3_020_idr_basefill_009(idr_base_universe_d2_020_idr_basefill_009):
    return _base_universe_d3(idr_base_universe_d2_020_idr_basefill_009, 20)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_020_idr_basefill_009'] = {'inputs': ['idr_base_universe_d2_020_idr_basefill_009'], 'func': idr_base_universe_d3_020_idr_basefill_009}


def idr_base_universe_d3_021_idr_basefill_012(idr_base_universe_d2_021_idr_basefill_012):
    return _base_universe_d3(idr_base_universe_d2_021_idr_basefill_012, 21)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_021_idr_basefill_012'] = {'inputs': ['idr_base_universe_d2_021_idr_basefill_012'], 'func': idr_base_universe_d3_021_idr_basefill_012}


def idr_base_universe_d3_022_idr_basefill_013(idr_base_universe_d2_022_idr_basefill_013):
    return _base_universe_d3(idr_base_universe_d2_022_idr_basefill_013, 22)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_022_idr_basefill_013'] = {'inputs': ['idr_base_universe_d2_022_idr_basefill_013'], 'func': idr_base_universe_d3_022_idr_basefill_013}


def idr_base_universe_d3_023_idr_basefill_015(idr_base_universe_d2_023_idr_basefill_015):
    return _base_universe_d3(idr_base_universe_d2_023_idr_basefill_015, 23)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_023_idr_basefill_015'] = {'inputs': ['idr_base_universe_d2_023_idr_basefill_015'], 'func': idr_base_universe_d3_023_idr_basefill_015}


def idr_base_universe_d3_024_idr_basefill_018(idr_base_universe_d2_024_idr_basefill_018):
    return _base_universe_d3(idr_base_universe_d2_024_idr_basefill_018, 24)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_024_idr_basefill_018'] = {'inputs': ['idr_base_universe_d2_024_idr_basefill_018'], 'func': idr_base_universe_d3_024_idr_basefill_018}


def idr_base_universe_d3_025_idr_basefill_019(idr_base_universe_d2_025_idr_basefill_019):
    return _base_universe_d3(idr_base_universe_d2_025_idr_basefill_019, 25)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_025_idr_basefill_019'] = {'inputs': ['idr_base_universe_d2_025_idr_basefill_019'], 'func': idr_base_universe_d3_025_idr_basefill_019}


def idr_base_universe_d3_026_idr_basefill_021(idr_base_universe_d2_026_idr_basefill_021):
    return _base_universe_d3(idr_base_universe_d2_026_idr_basefill_021, 26)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_026_idr_basefill_021'] = {'inputs': ['idr_base_universe_d2_026_idr_basefill_021'], 'func': idr_base_universe_d3_026_idr_basefill_021}


def idr_base_universe_d3_027_idr_basefill_024(idr_base_universe_d2_027_idr_basefill_024):
    return _base_universe_d3(idr_base_universe_d2_027_idr_basefill_024, 27)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_027_idr_basefill_024'] = {'inputs': ['idr_base_universe_d2_027_idr_basefill_024'], 'func': idr_base_universe_d3_027_idr_basefill_024}


def idr_base_universe_d3_028_idr_basefill_025(idr_base_universe_d2_028_idr_basefill_025):
    return _base_universe_d3(idr_base_universe_d2_028_idr_basefill_025, 28)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_028_idr_basefill_025'] = {'inputs': ['idr_base_universe_d2_028_idr_basefill_025'], 'func': idr_base_universe_d3_028_idr_basefill_025}


def idr_base_universe_d3_029_idr_basefill_027(idr_base_universe_d2_029_idr_basefill_027):
    return _base_universe_d3(idr_base_universe_d2_029_idr_basefill_027, 29)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_029_idr_basefill_027'] = {'inputs': ['idr_base_universe_d2_029_idr_basefill_027'], 'func': idr_base_universe_d3_029_idr_basefill_027}


def idr_base_universe_d3_030_idr_basefill_030(idr_base_universe_d2_030_idr_basefill_030):
    return _base_universe_d3(idr_base_universe_d2_030_idr_basefill_030, 30)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_030_idr_basefill_030'] = {'inputs': ['idr_base_universe_d2_030_idr_basefill_030'], 'func': idr_base_universe_d3_030_idr_basefill_030}


def idr_base_universe_d3_031_idr_basefill_031(idr_base_universe_d2_031_idr_basefill_031):
    return _base_universe_d3(idr_base_universe_d2_031_idr_basefill_031, 31)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_031_idr_basefill_031'] = {'inputs': ['idr_base_universe_d2_031_idr_basefill_031'], 'func': idr_base_universe_d3_031_idr_basefill_031}


def idr_base_universe_d3_032_idr_basefill_032(idr_base_universe_d2_032_idr_basefill_032):
    return _base_universe_d3(idr_base_universe_d2_032_idr_basefill_032, 32)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_032_idr_basefill_032'] = {'inputs': ['idr_base_universe_d2_032_idr_basefill_032'], 'func': idr_base_universe_d3_032_idr_basefill_032}


def idr_base_universe_d3_033_idr_basefill_033(idr_base_universe_d2_033_idr_basefill_033):
    return _base_universe_d3(idr_base_universe_d2_033_idr_basefill_033, 33)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_033_idr_basefill_033'] = {'inputs': ['idr_base_universe_d2_033_idr_basefill_033'], 'func': idr_base_universe_d3_033_idr_basefill_033}


def idr_base_universe_d3_034_idr_basefill_034(idr_base_universe_d2_034_idr_basefill_034):
    return _base_universe_d3(idr_base_universe_d2_034_idr_basefill_034, 34)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_034_idr_basefill_034'] = {'inputs': ['idr_base_universe_d2_034_idr_basefill_034'], 'func': idr_base_universe_d3_034_idr_basefill_034}


def idr_base_universe_d3_035_idr_basefill_035(idr_base_universe_d2_035_idr_basefill_035):
    return _base_universe_d3(idr_base_universe_d2_035_idr_basefill_035, 35)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_035_idr_basefill_035'] = {'inputs': ['idr_base_universe_d2_035_idr_basefill_035'], 'func': idr_base_universe_d3_035_idr_basefill_035}


def idr_base_universe_d3_036_idr_basefill_036(idr_base_universe_d2_036_idr_basefill_036):
    return _base_universe_d3(idr_base_universe_d2_036_idr_basefill_036, 36)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_036_idr_basefill_036'] = {'inputs': ['idr_base_universe_d2_036_idr_basefill_036'], 'func': idr_base_universe_d3_036_idr_basefill_036}


def idr_base_universe_d3_037_idr_basefill_037(idr_base_universe_d2_037_idr_basefill_037):
    return _base_universe_d3(idr_base_universe_d2_037_idr_basefill_037, 37)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_037_idr_basefill_037'] = {'inputs': ['idr_base_universe_d2_037_idr_basefill_037'], 'func': idr_base_universe_d3_037_idr_basefill_037}


def idr_base_universe_d3_038_idr_basefill_038(idr_base_universe_d2_038_idr_basefill_038):
    return _base_universe_d3(idr_base_universe_d2_038_idr_basefill_038, 38)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_038_idr_basefill_038'] = {'inputs': ['idr_base_universe_d2_038_idr_basefill_038'], 'func': idr_base_universe_d3_038_idr_basefill_038}


def idr_base_universe_d3_039_idr_basefill_039(idr_base_universe_d2_039_idr_basefill_039):
    return _base_universe_d3(idr_base_universe_d2_039_idr_basefill_039, 39)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_039_idr_basefill_039'] = {'inputs': ['idr_base_universe_d2_039_idr_basefill_039'], 'func': idr_base_universe_d3_039_idr_basefill_039}


def idr_base_universe_d3_040_idr_basefill_040(idr_base_universe_d2_040_idr_basefill_040):
    return _base_universe_d3(idr_base_universe_d2_040_idr_basefill_040, 40)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_040_idr_basefill_040'] = {'inputs': ['idr_base_universe_d2_040_idr_basefill_040'], 'func': idr_base_universe_d3_040_idr_basefill_040}


def idr_base_universe_d3_041_idr_basefill_041(idr_base_universe_d2_041_idr_basefill_041):
    return _base_universe_d3(idr_base_universe_d2_041_idr_basefill_041, 41)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_041_idr_basefill_041'] = {'inputs': ['idr_base_universe_d2_041_idr_basefill_041'], 'func': idr_base_universe_d3_041_idr_basefill_041}


def idr_base_universe_d3_042_idr_basefill_042(idr_base_universe_d2_042_idr_basefill_042):
    return _base_universe_d3(idr_base_universe_d2_042_idr_basefill_042, 42)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_042_idr_basefill_042'] = {'inputs': ['idr_base_universe_d2_042_idr_basefill_042'], 'func': idr_base_universe_d3_042_idr_basefill_042}


def idr_base_universe_d3_043_idr_basefill_043(idr_base_universe_d2_043_idr_basefill_043):
    return _base_universe_d3(idr_base_universe_d2_043_idr_basefill_043, 43)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_043_idr_basefill_043'] = {'inputs': ['idr_base_universe_d2_043_idr_basefill_043'], 'func': idr_base_universe_d3_043_idr_basefill_043}


def idr_base_universe_d3_044_idr_basefill_044(idr_base_universe_d2_044_idr_basefill_044):
    return _base_universe_d3(idr_base_universe_d2_044_idr_basefill_044, 44)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_044_idr_basefill_044'] = {'inputs': ['idr_base_universe_d2_044_idr_basefill_044'], 'func': idr_base_universe_d3_044_idr_basefill_044}


def idr_base_universe_d3_045_idr_basefill_045(idr_base_universe_d2_045_idr_basefill_045):
    return _base_universe_d3(idr_base_universe_d2_045_idr_basefill_045, 45)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_045_idr_basefill_045'] = {'inputs': ['idr_base_universe_d2_045_idr_basefill_045'], 'func': idr_base_universe_d3_045_idr_basefill_045}


def idr_base_universe_d3_046_idr_basefill_046(idr_base_universe_d2_046_idr_basefill_046):
    return _base_universe_d3(idr_base_universe_d2_046_idr_basefill_046, 46)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_046_idr_basefill_046'] = {'inputs': ['idr_base_universe_d2_046_idr_basefill_046'], 'func': idr_base_universe_d3_046_idr_basefill_046}


def idr_base_universe_d3_047_idr_basefill_047(idr_base_universe_d2_047_idr_basefill_047):
    return _base_universe_d3(idr_base_universe_d2_047_idr_basefill_047, 47)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_047_idr_basefill_047'] = {'inputs': ['idr_base_universe_d2_047_idr_basefill_047'], 'func': idr_base_universe_d3_047_idr_basefill_047}


def idr_base_universe_d3_048_idr_basefill_048(idr_base_universe_d2_048_idr_basefill_048):
    return _base_universe_d3(idr_base_universe_d2_048_idr_basefill_048, 48)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_048_idr_basefill_048'] = {'inputs': ['idr_base_universe_d2_048_idr_basefill_048'], 'func': idr_base_universe_d3_048_idr_basefill_048}


def idr_base_universe_d3_049_idr_basefill_049(idr_base_universe_d2_049_idr_basefill_049):
    return _base_universe_d3(idr_base_universe_d2_049_idr_basefill_049, 49)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_049_idr_basefill_049'] = {'inputs': ['idr_base_universe_d2_049_idr_basefill_049'], 'func': idr_base_universe_d3_049_idr_basefill_049}


def idr_base_universe_d3_050_idr_basefill_050(idr_base_universe_d2_050_idr_basefill_050):
    return _base_universe_d3(idr_base_universe_d2_050_idr_basefill_050, 50)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_050_idr_basefill_050'] = {'inputs': ['idr_base_universe_d2_050_idr_basefill_050'], 'func': idr_base_universe_d3_050_idr_basefill_050}


def idr_base_universe_d3_051_idr_basefill_051(idr_base_universe_d2_051_idr_basefill_051):
    return _base_universe_d3(idr_base_universe_d2_051_idr_basefill_051, 51)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_051_idr_basefill_051'] = {'inputs': ['idr_base_universe_d2_051_idr_basefill_051'], 'func': idr_base_universe_d3_051_idr_basefill_051}


def idr_base_universe_d3_052_idr_basefill_052(idr_base_universe_d2_052_idr_basefill_052):
    return _base_universe_d3(idr_base_universe_d2_052_idr_basefill_052, 52)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_052_idr_basefill_052'] = {'inputs': ['idr_base_universe_d2_052_idr_basefill_052'], 'func': idr_base_universe_d3_052_idr_basefill_052}


def idr_base_universe_d3_053_idr_basefill_053(idr_base_universe_d2_053_idr_basefill_053):
    return _base_universe_d3(idr_base_universe_d2_053_idr_basefill_053, 53)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_053_idr_basefill_053'] = {'inputs': ['idr_base_universe_d2_053_idr_basefill_053'], 'func': idr_base_universe_d3_053_idr_basefill_053}


def idr_base_universe_d3_054_idr_basefill_054(idr_base_universe_d2_054_idr_basefill_054):
    return _base_universe_d3(idr_base_universe_d2_054_idr_basefill_054, 54)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_054_idr_basefill_054'] = {'inputs': ['idr_base_universe_d2_054_idr_basefill_054'], 'func': idr_base_universe_d3_054_idr_basefill_054}


def idr_base_universe_d3_055_idr_basefill_055(idr_base_universe_d2_055_idr_basefill_055):
    return _base_universe_d3(idr_base_universe_d2_055_idr_basefill_055, 55)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_055_idr_basefill_055'] = {'inputs': ['idr_base_universe_d2_055_idr_basefill_055'], 'func': idr_base_universe_d3_055_idr_basefill_055}


def idr_base_universe_d3_056_idr_basefill_056(idr_base_universe_d2_056_idr_basefill_056):
    return _base_universe_d3(idr_base_universe_d2_056_idr_basefill_056, 56)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_056_idr_basefill_056'] = {'inputs': ['idr_base_universe_d2_056_idr_basefill_056'], 'func': idr_base_universe_d3_056_idr_basefill_056}


def idr_base_universe_d3_057_idr_basefill_057(idr_base_universe_d2_057_idr_basefill_057):
    return _base_universe_d3(idr_base_universe_d2_057_idr_basefill_057, 57)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_057_idr_basefill_057'] = {'inputs': ['idr_base_universe_d2_057_idr_basefill_057'], 'func': idr_base_universe_d3_057_idr_basefill_057}


def idr_base_universe_d3_058_idr_basefill_058(idr_base_universe_d2_058_idr_basefill_058):
    return _base_universe_d3(idr_base_universe_d2_058_idr_basefill_058, 58)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_058_idr_basefill_058'] = {'inputs': ['idr_base_universe_d2_058_idr_basefill_058'], 'func': idr_base_universe_d3_058_idr_basefill_058}


def idr_base_universe_d3_059_idr_basefill_059(idr_base_universe_d2_059_idr_basefill_059):
    return _base_universe_d3(idr_base_universe_d2_059_idr_basefill_059, 59)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_059_idr_basefill_059'] = {'inputs': ['idr_base_universe_d2_059_idr_basefill_059'], 'func': idr_base_universe_d3_059_idr_basefill_059}


def idr_base_universe_d3_060_idr_basefill_060(idr_base_universe_d2_060_idr_basefill_060):
    return _base_universe_d3(idr_base_universe_d2_060_idr_basefill_060, 60)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_060_idr_basefill_060'] = {'inputs': ['idr_base_universe_d2_060_idr_basefill_060'], 'func': idr_base_universe_d3_060_idr_basefill_060}


def idr_base_universe_d3_061_idr_basefill_061(idr_base_universe_d2_061_idr_basefill_061):
    return _base_universe_d3(idr_base_universe_d2_061_idr_basefill_061, 61)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_061_idr_basefill_061'] = {'inputs': ['idr_base_universe_d2_061_idr_basefill_061'], 'func': idr_base_universe_d3_061_idr_basefill_061}


def idr_base_universe_d3_062_idr_basefill_062(idr_base_universe_d2_062_idr_basefill_062):
    return _base_universe_d3(idr_base_universe_d2_062_idr_basefill_062, 62)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_062_idr_basefill_062'] = {'inputs': ['idr_base_universe_d2_062_idr_basefill_062'], 'func': idr_base_universe_d3_062_idr_basefill_062}


def idr_base_universe_d3_063_idr_basefill_063(idr_base_universe_d2_063_idr_basefill_063):
    return _base_universe_d3(idr_base_universe_d2_063_idr_basefill_063, 63)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_063_idr_basefill_063'] = {'inputs': ['idr_base_universe_d2_063_idr_basefill_063'], 'func': idr_base_universe_d3_063_idr_basefill_063}


def idr_base_universe_d3_064_idr_basefill_064(idr_base_universe_d2_064_idr_basefill_064):
    return _base_universe_d3(idr_base_universe_d2_064_idr_basefill_064, 64)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_064_idr_basefill_064'] = {'inputs': ['idr_base_universe_d2_064_idr_basefill_064'], 'func': idr_base_universe_d3_064_idr_basefill_064}


def idr_base_universe_d3_065_idr_basefill_065(idr_base_universe_d2_065_idr_basefill_065):
    return _base_universe_d3(idr_base_universe_d2_065_idr_basefill_065, 65)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_065_idr_basefill_065'] = {'inputs': ['idr_base_universe_d2_065_idr_basefill_065'], 'func': idr_base_universe_d3_065_idr_basefill_065}


def idr_base_universe_d3_066_idr_basefill_066(idr_base_universe_d2_066_idr_basefill_066):
    return _base_universe_d3(idr_base_universe_d2_066_idr_basefill_066, 66)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_066_idr_basefill_066'] = {'inputs': ['idr_base_universe_d2_066_idr_basefill_066'], 'func': idr_base_universe_d3_066_idr_basefill_066}


def idr_base_universe_d3_067_idr_basefill_067(idr_base_universe_d2_067_idr_basefill_067):
    return _base_universe_d3(idr_base_universe_d2_067_idr_basefill_067, 67)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_067_idr_basefill_067'] = {'inputs': ['idr_base_universe_d2_067_idr_basefill_067'], 'func': idr_base_universe_d3_067_idr_basefill_067}


def idr_base_universe_d3_068_idr_basefill_068(idr_base_universe_d2_068_idr_basefill_068):
    return _base_universe_d3(idr_base_universe_d2_068_idr_basefill_068, 68)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_068_idr_basefill_068'] = {'inputs': ['idr_base_universe_d2_068_idr_basefill_068'], 'func': idr_base_universe_d3_068_idr_basefill_068}


def idr_base_universe_d3_069_idr_basefill_069(idr_base_universe_d2_069_idr_basefill_069):
    return _base_universe_d3(idr_base_universe_d2_069_idr_basefill_069, 69)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_069_idr_basefill_069'] = {'inputs': ['idr_base_universe_d2_069_idr_basefill_069'], 'func': idr_base_universe_d3_069_idr_basefill_069}


def idr_base_universe_d3_070_idr_basefill_070(idr_base_universe_d2_070_idr_basefill_070):
    return _base_universe_d3(idr_base_universe_d2_070_idr_basefill_070, 70)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_070_idr_basefill_070'] = {'inputs': ['idr_base_universe_d2_070_idr_basefill_070'], 'func': idr_base_universe_d3_070_idr_basefill_070}


def idr_base_universe_d3_071_idr_basefill_071(idr_base_universe_d2_071_idr_basefill_071):
    return _base_universe_d3(idr_base_universe_d2_071_idr_basefill_071, 71)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_071_idr_basefill_071'] = {'inputs': ['idr_base_universe_d2_071_idr_basefill_071'], 'func': idr_base_universe_d3_071_idr_basefill_071}


def idr_base_universe_d3_072_idr_basefill_072(idr_base_universe_d2_072_idr_basefill_072):
    return _base_universe_d3(idr_base_universe_d2_072_idr_basefill_072, 72)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_072_idr_basefill_072'] = {'inputs': ['idr_base_universe_d2_072_idr_basefill_072'], 'func': idr_base_universe_d3_072_idr_basefill_072}


def idr_base_universe_d3_073_idr_basefill_073(idr_base_universe_d2_073_idr_basefill_073):
    return _base_universe_d3(idr_base_universe_d2_073_idr_basefill_073, 73)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_073_idr_basefill_073'] = {'inputs': ['idr_base_universe_d2_073_idr_basefill_073'], 'func': idr_base_universe_d3_073_idr_basefill_073}


def idr_base_universe_d3_074_idr_basefill_074(idr_base_universe_d2_074_idr_basefill_074):
    return _base_universe_d3(idr_base_universe_d2_074_idr_basefill_074, 74)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_074_idr_basefill_074'] = {'inputs': ['idr_base_universe_d2_074_idr_basefill_074'], 'func': idr_base_universe_d3_074_idr_basefill_074}


def idr_base_universe_d3_075_idr_basefill_075(idr_base_universe_d2_075_idr_basefill_075):
    return _base_universe_d3(idr_base_universe_d2_075_idr_basefill_075, 75)
IDR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['idr_base_universe_d3_075_idr_basefill_075'] = {'inputs': ['idr_base_universe_d2_075_idr_basefill_075'], 'func': idr_base_universe_d3_075_idr_basefill_075}
