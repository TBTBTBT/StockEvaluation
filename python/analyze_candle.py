from enum import Enum
#陽線か陰線か
class CandleDirectionType(Enum):
    NONE = 99
    STAY = 0
    POSITIVE = 1
    NEGATIVE = 2

#大きさ
class CandleSizeType(Enum):
    NONE = 99
    BIG = 0 #長め
    SMALL = 1 #短め
    STRAIGHT = 2 # 坊主
    LINE = 3 # 最短
#ヒゲの位置
class CandleTailType(Enum):
    NONE = 99
    BIG = 0 #
    SMALL = 1
    STRAIGHT = 2 # 坊主
    UPSHADOW = 3 # 上影
    DOWNSHADOW = 4 #下影
    CENTER = 5
    #UPHUMMER = 6 # カラカサ
    #DOWNHUMMER = 7 # トンカチ

#ローソクの種類
class CandleState:
    def __init__(self,direction,body_length,up_tail_length,down_tail_length):
        self.direction = direction
        self.body_length = body_length
        self.up_tail_length = up_tail_length
        self.down_tail_length = down_tail_length
        #self.fluctuation = fluctuation
    def __repr__(self):
        return (
            " candle "
            + "\n direction        : '%s' " % (self.direction)
            + "\n body_length      : '%s' " % (self.body_length)
            + "\n up_tail_length   : '%s' " % (self.up_tail_length)
            + "\n down_tail_length : '%s' " % (self.down_tail_length))
            
#------------------------------------------------
#分析
class CandleAnalyzer:
    def __init__(self):
        pass
        #ローソク足分析
    def analyze_candle(self,data):
        o = data[0]
        h = data[1]
        l = data[2]
        c = data[3]
        direction   = self.analyze_candle_direction(o,c)
        length = self.analyze_candle_body_length(o,c)
        up_tail_length = self.analyze_candle_tail_up(o,h,c)
        down_tail_length = self.analyze_candle_tail_down(o,l,c)
        state = CandleState(
            direction,
            length,
            up_tail_length,
            down_tail_length)
        return state
        # 陰陽判定
    def analyze_candle_direction(self,o,c):
        ret = CandleDirectionType.NONE
        if o > c:
            ret = CandleDirectionType.NEGATIVE
        elif o < c:
            ret = CandleDirectionType.POSITIVE
        else:
            ret = CandleDirectionType.STAY
        return ret
    def analyze_candle_body_length(self,o,c):
        return abs(o-c)
        # ヒゲの長さ
    def analyze_candle_tail_up(self,o,h,c):
        head = c if o < c else o
        ret = h - head
        return ret
    def analyze_candle_tail_down(self,o,l,c):
        bottom = c if o > c else o
        ret = bottom - l
        return ret
        

