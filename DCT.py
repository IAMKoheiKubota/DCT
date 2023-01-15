import math
import numpy as np

#8*8のブロックの画素
eight_eight_block=[
    [167,173,156,132,163,173,170,170],
    [167,174,153,125,159,170,167,169],
    [168,174,152,133,168,172,166,168],
    [169,172,147,135,168,171,167,167],
    [170,173,147,136,167,170,170,171],
    [169,172,140,136,171,171,169,167],
    [170,174,144,142,173,171,168,169],
    [173,175,137,135,170,171,170,170]
]

#DCT変換する関数
def DCT(block):
    z = np.zeros((8,8))
    #iは行のインデックス、jは列のインデックス、kがその要素値
    for i,a in enumerate(z):
        for j,k in enumerate(a):
            if i==0 and j==0:
                #lは画素ブロックの行インデックス、mは列のインデックス、nは画素値
                for l,b in enumerate(block):
                    for m,n in enumerate(b):
                        #二次元DCT変換の公式。16は2*N（Nはブロック数なので8）
                        k += n*math.cos(((2*l+1)*i*math.pi)/16)*math.cos(((2*m+1)*j*math.pi)/16)
                k*=2*(1/math.sqrt(2))*(1/math.sqrt(2))/8
                z[i][j]=k
            elif i!=0 and j==0:
                for l,b in enumerate(block):
                    for m,n in enumerate(b):
                        k += n*math.cos(((2*l+1)*i*math.pi)/16)*math.cos(((2*m+1)*j*math.pi)/16)
                k *= 2*(1)*(1/math.sqrt(2))/8
                z[i][j]=k
            elif i==0 and j!=0:
                for l,b in enumerate(block):
                    for m,n in enumerate(b):
                        k += n*math.cos(((2*l+1)*i*math.pi)/16)*math.cos(((2*m+1)*j*math.pi)/16)
                k *= 2*(1/math.sqrt(2))*1/8
                z[i][j]=k
            else:
                for l,b in enumerate(block):
                    for m,n in enumerate(b):
                        k += n*math.cos(((2*l+1)*i*math.pi)/16)*math.cos(((2*m+1)*j*math.pi)/16)
                k *= 2*(1)*(1)/8
                z[i][j]=k
    return z




#初期の画素
print("ブロック f(i,j)")
print(*eight_eight_block,sep='\n')
print('\n')

#DCT変換
z=DCT(eight_eight_block)

#DCT係数
print("f(i,j)のDCT係数 F(u,v)")
np.set_printoptions(precision=2,floatmode='fixed',suppress=True)
print(*z,sep='\n')