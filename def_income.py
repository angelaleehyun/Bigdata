import pandas as pd
import numpy as np


def income(arr):

    names = ['age','workclass','fnlwgt','education',
             'education-num','marital-status',
             'occupation','relationship','race','sex','capital-gain',
             'capital-loss','hours-per-week','native-country','income']
    data = pd.read_csv("Data/adult.data.txt",header=None,names=names)
    #print(data)
    # 나이, 직업분류, 학력,성별, 일하는시간, 직업, 수입

    df = data[['age','workclass','education','occupation','race','sex','hours-per-week','income']]
    # print(df)

    b_df = pd.get_dummies(df)
    # print(b_df)

    # 위의 데이타로 부터 문제는 x에 답은 y 에 담기.....
    print(b_df)

    x = b_df.loc[:,'age':'sex_ Female']
    y = b_df.iloc[:,-1]
    print("x",len(x.columns))
    # print(x)
    # print(y)
    # print(x.shape)    #차수 확인(32561, 43)   2차원
    # print(y.shape)    #(32561,)               1차원
    from sklearn import linear_model,model_selection, metrics
    #x 와 y를 가지고 훈련하는것과 검증할 데이타 불리(model_selection)
    train_x, test_x,train_y,test_y = model_selection.train_test_split(x,y)

    print(len(train_x),len(train_y))       #24420 24420
    print(len(test_x),len(test_y))         #8141 8141

    lr = linear_model.LogisticRegression()
    lr.fit(train_x,train_y)                #학습시키기
    r = lr.predict(test_x)                     #예측
    score = metrics.accuracy_score(test_y,r)  #확률(정답률)계산
    print('정답률: ',score)
    #확률(정답률)계산
    print(lr.score(test_x,test_y))
    result = r == test_y
    a = result.values
    b = a[a == True]
    print(b)
    #확률(정답률)계산
    print(len(b)/len(test_y)*100)

    #[[48 ' Private' ' 11th' ' Machine-op-inspct' ' White' ' Male' 40 ' <=50K']]
    #print(np.array(df.iloc[35]).reshape([1,-1]))
    print(arr)
    arr = pd.DataFrame(arr,columns=['age','workclass','education','occupation','race','sex','hours-per-week','income'])
    print(arr)
    df = df.append(arr)
    print('==========')

    b_test = pd.get_dummies(df)

    x1 = np.array(b_test.iloc[-1, :-3]).reshape(1,-1)
    print(x1)
    r = lr.predict(x1)
    print('r',r)
    return r


