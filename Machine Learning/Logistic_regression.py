import numpy as np
x1 = np.random.randn(100)
x2 = np.random.randn(100)
y = (2*x1 - 3*x2 + 1 > 0).astype(int)
x=np.array([x1,x2])
w_init = np.array([0.0, 0.0]) 
b_init = 0.0
def sigmoid(x,w,b):
    z= np.dot(w,x)+b
    y_dash=1/(1+np.exp(-z))
    return y_dash
def bce(y,y_pred):
    n=len(y)
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
    loss=-np.sum(y*np.log(y_pred)+(1-y)*np.log(1-y_pred))/n
    return loss
def gradient_descent(x,y,w,b,learning_rate=0.01,epochs=1000):
    n=len(y)
    for epoch in range(epochs):
        y_pred=sigmoid(x,w,b)
        dz=y_pred-y
        dw=np.dot(x,dz)/n
        db=np.sum(dz)/n
        w-=learning_rate*dw
        b-=learning_rate*db
        if epoch % 500 == 0:
            loss = bce(y, y_pred)

            print(f"Epoch {epoch}: Loss {loss:.4f}")

    print("-" * 20)
    print(f"Learned Weights: {w}")
    print(f"Learned Bias: {b:.4f}")
    print(f"Original was: [2, -3] and 1")
    return w,b
learned_w, learned_b = gradient_descent(x, y, w_init, b_init)