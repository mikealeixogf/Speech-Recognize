
from scipy import signal
import numpy as np

def ruidoum(sig, ruido):
        length= len(sig)
        nsample= np.array(range(length)) #creates an array of signal length
        r=5000 #delay factor sample
        a=0.8 #attenuation factor
        sign = signal.fftconvolve(sinal, ruido) # convolution between signal and impulse response
        sign /= np.max(np.abs(sig)) # normalize output (-1,1)
        
        #Index for delay
        index= np.round(nsample-r)
        index[index<0]= 0 
        index[index>(length-1)]= length-1

        out_sig= np.zeros(length) #Imput Signal

        for j in range(length): #loop to calculation  each sample
          out_sig[j]= np.float(sig[j]) + a*np.float(sig[int(index[j])]) #Add Delayed signal
        plt.figure(figsize=(10, 7))
        plt.plot(out_sig,'r',sig,'b')
        plt.show()

        return sign#[1:int(sample_interest_out_sig)]
