from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def needleman_wunsch(label, pred):
    m=len(label)
    n=len(pred)
    dp=[[1]*n for _ in range(m)]
    for i in range(m):
        if pred[0]!=label[i]:
            dp[i][0]=0
        else:
            break
    for j in range(n):
        if pred[j]!=label[0]:
            dp[0][j]=0
        else:
            break
            
    for i in range(1,m):
        for j in range(1,n):
            if pred[j]==label[i]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    return dp

def traceback(label,pred,dp):
    m=len(dp)
    n=len(dp[0])
    out_label, between, out_pred = "", "", ""
    i, j = m - 1, n - 1
    while i>0 and j>0:
        if label[i]==pred[j]:
            out_label += label[i]
            out_pred += pred[j]
            between += "|"

            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            out_label += label[i]
            out_pred += "-"
            between += " "

            i-=1
        else:
            out_label += "-"
            out_pred += pred[j]
            between += " "

            j-=1
    if i>0:
        while i>=0:
            if label[i]==pred[j]:
                out_label += label[i]
                out_pred += pred[j]
                between += "|"

                i-=1
                j-=1
            else:
                out_label += label[i]
                out_pred += "-"
                between += " "

                i-=1
    if j>0:
        while j>=0:
            if pred[j]==label[i]:
                out_label += label[i]
                out_pred += pred[j]
                between += "|"

                i-=1
                j-=1
            else:
                out_label += "-"
                out_pred += pred[j]
                between += " "

                j-=1
    if i==0 and j==0:
        out_label += label[i]
        out_pred += pred[j]
        between += "|"

    elif i==0:
        out_label += label[i]
        out_pred += "-"
        between += " "
    elif j==0:
        out_label += "-"
        out_pred += pred[j]
        between += " "

    return out_label, out_pred, between

y_true="GCATGCUCCAUC" #"GCATGCU"
y_pred="GATTACACGAUC" #"GATTACA"
dp=needleman_wunsch(y_true,y_pred)
out_label, out_pred, between = traceback(y_true, y_pred, dp)
print("--> Needleman-Wunsch result:\n")
print(out_label[::-1])
print(between[::-1])
print(out_pred[::-1])
print("  Score=",dp[-1][-1], sep = "")
print()
print("--> Pairwise results:\n")
alignments = pairwise2.align.globalxx(y_true, y_pred)
for align in alignments:
    print(format_alignment(*align))