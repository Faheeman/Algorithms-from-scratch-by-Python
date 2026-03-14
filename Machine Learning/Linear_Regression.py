import numpy as np
x1= np.random.randn(100)
x2= np.random.randn(100)    
y_true = 2*x1 + 3*x2 + 1 + np.random.randn(100)*0.1
x=np.array([x1,x2])
w_init=np.array([0.0,0.0])
b_init=0.0
y=w_init[0]*x1 + w_init[1]*x2 + b_init
def mse(y,y_pred):
    n=len(y)
    loss=np.sum((y-y_pred)**2)/n
    return loss 
def gradient_descent(x,y,w,b,learning_rate=0.01,epochs=10000):
    n=len(y)
    for epoch in range(epochs):
        y_pred=np.dot(w,x)+b
        dw=-2*np.dot(x,(y-y_pred))/n
        db=-2*np.sum(y-y_pred)/n
        w-=learning_rate*dw
        b-=learning_rate*db
        if epoch % 500 == 0:
            loss = mse(y, y_pred)
            print(f"Epoch {epoch}: Loss {loss:.4f}")
    print("-"*20)
    print(f"Learned Weights: {w}")
    print(f"Learned Bias: {b:.4f}")
    print(f"Original was: [2, 3] and 1")
    return w,b
learned_w, learned_b = gradient_descent(x, y_true, w_init, b_init)
print(f"Predicted values: {learned_w[0]*x1 + learned_w[1]*x2 + learned_b}")
accuracy = np.mean((y_true - (learned_w[0]*x1 + learned_w[1]*x2 + learned_b))**2)
print(f"Mean Squared Error: {accuracy:.4f}")
